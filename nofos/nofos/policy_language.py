"""
Department Governance policy-language detection.

Called once, at import time, from _build_document() in nofo.py - the same
pass that builds Section/Subsection rows - never at export time. Export
(a later phase) only consumes the policy_language_status/policy_language_slot
that got set here; it never re-runs detection itself.

Two chained steps, per the design:
    1. Alignment - which canonical PolicyLanguageSlot (if any) does a given
       Subsection correspond to.
    2. Verification - does the Subsection's content match that slot's
       canonical text closely enough to call it intact.

Ambiguity rule: a confident non-match (no alignment at all) -> "none", no
review needed. Anything that aligns to a slot but doesn't cleanly verify as
intact or as a prior canonical version -> "may_be_altered", never silently
downgraded to "none" - that would let real policy-language drift through
undetected.
"""

import re

from bs4 import BeautifulSoup
from martor.utils import markdownify

from .models import PolicyLanguageSlot

PLACEHOLDER_PATTERN = re.compile(r"\{[^{}]*\}")

# Smart-quote/dash/non-breaking-space normalization: the representation noise
# that would otherwise false-flag unchanged text as altered. Deliberately
# does not touch case or punctuation that could carry real meaning.
_NORMALIZE_TRANSLATION = str.maketrans(
    {
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        " ": " ",
    }
)


def normalize_for_comparison(text):
    """Collapse whitespace and normalize smart quotes/dashes/nbsp so cosmetic
    rendering differences don't register as content differences."""
    text = (text or "").translate(_NORMALIZE_TRANSLATION)
    return re.sub(r"\s+", " ", text).strip()


def _subsection_plain_text(raw_markdown_body):
    """
    Render a Subsection's stored Markdown body to HTML the same way
    nofo_compare.py does for cross-version diffing (martor's markdownify
    renders Markdown -> HTML, despite the name), then strip tags down to
    plain text for placeholder-pattern matching.
    """
    html = markdownify(raw_markdown_body or "")
    text = BeautifulSoup(html, "html.parser").get_text(" ", strip=True)
    return normalize_for_comparison(text)


def _fixed_span_to_regex(span):
    """Turn one fixed (non-placeholder) span of canonical text into a regex
    that tolerates whitespace-amount differences but nothing else."""
    words = [w for w in re.split(r"\s+", span.strip()) if w]
    return r"\s+".join(re.escape(word) for word in words)


def _variant_matches(canonical_text, candidate_text, match_scope):
    """
    True if candidate_text matches canonical_text's shape: every fixed span
    (the parts of canonical_text NOT inside {...}) must appear in
    candidate_text, in order, with placeholder spans allowed to contain
    anything (or nothing) in between. A canonical_text with zero {...}
    spans degrades to a plain exact-text check - this is deliberately one
    matching function for 'fixed' and 'fixed_with_placeholders' alike,
    rather than two, since 'fixed' is just the zero-placeholder case.

    match_scope="whole_subsection" requires the match to cover the entire
    candidate_text (fullmatch) - a subsection that contains the canonical
    text plus substantial extra content is not "intact", it's altered.
    match_scope="span_within_subsection" allows the canonical text to be a
    fragment anywhere inside a larger, partly-variable body.
    """
    canonical_text = normalize_for_comparison(canonical_text)
    raw_spans = PLACEHOLDER_PATTERN.split(canonical_text)
    span_patterns = [_fixed_span_to_regex(s) for s in raw_spans if s.strip()]
    if not span_patterns:
        return False

    gap = r"(?:.|\n)*?"
    pattern = gap.join(span_patterns)

    if match_scope == "span_within_subsection":
        return re.search(pattern, candidate_text, re.DOTALL) is not None

    return re.fullmatch(gap + pattern + gap, candidate_text, re.DOTALL) is not None


def _matches_any_variant(slot, candidate_text):
    """
    Checks candidate_text against every stored variant for this slot.
    Brute-force across variants rather than a slot-specific parameter
    extraction: correct and slot-type-agnostic for every slot_type
    (fixed / fixed_with_placeholders / one_of_n_options /
    parameterized_family all reduce to "does any known variant match").
    With only a handful of variants per slot in the current data, this is
    plenty fast; a parameterized_family slot that grows to the full ~99
    variants (DG-004's real shape) would be a reasonable place to add a
    parameter-extraction shortcut later purely as a performance
    optimization - it wouldn't change the result, just how it's found.
    """
    return any(
        _variant_matches(variant.canonical_text, candidate_text, slot.match_scope)
        for variant in slot.variants.all()
    )


def get_candidate_slots():
    """
    All PolicyLanguageSlot rows - current AND superseded - grouped by
    slot_key. Superseded rows must stay in the candidate set: that's what
    lets detection distinguish "matches_prior_version" (matches an older,
    still-legitimate HHS revision) from "may_be_altered" (doesn't match
    anything we know about).
    """
    slots = list(PolicyLanguageSlot.objects.all().prefetch_related("variants"))
    grouped = {}
    for slot in slots:
        grouped.setdefault(slot.slot_key, []).append(slot)
    return grouped


def detect_policy_language_status(subsection_name, subsection_body, candidate_slots=None):
    """
    Determine the (policy_language_status, matched_slot) for one subsection,
    given its name and raw Markdown body. Pure function of its inputs so it
    can run against an in-memory Subsection object before it's saved
    (see _build_document in nofo.py), not just a persisted one.

    candidate_slots: the dict from get_candidate_slots(), fetched once per
    import and reused across all subsections in that NOFO rather than
    re-queried per subsection.

    Returns a (status, slot) tuple. slot is the *current* revision of
    whatever slot_key matched, if any is current, even when the status is
    "matches_prior_version" - export-time behavior (e.g. flag_prominently)
    should reflect the slot as HHS currently defines it, not a stale
    historical row.
    """
    if candidate_slots is None:
        candidate_slots = get_candidate_slots()

    candidate_text = _subsection_plain_text(subsection_body)

    # Span-scoped slots aren't tied to a heading of their own - they're
    # fragments embedded inside a differently-named subsection - so they're
    # checked against every subsection's body regardless of its name.
    for slot_versions in candidate_slots.values():
        for slot in slot_versions:
            if slot.match_scope != "span_within_subsection":
                continue
            status = _check_slot_versions([slot], candidate_text)
            if status:
                return status

    # Whole-subsection slots: align by name first. No name, or no name match
    # against any known slot -> a confident non-match, not ambiguous.
    name = (subsection_name or "").strip().lower()
    if not name:
        return "none", None

    for slot_versions in candidate_slots.values():
        whole_versions = [
            s for s in slot_versions if s.match_scope != "span_within_subsection"
        ]
        if not whole_versions:
            continue
        if (whole_versions[0].name or "").strip().lower() != name:
            continue

        status = _check_slot_versions(whole_versions, candidate_text)
        if status:
            return status

        # Aligned by name, but didn't cleanly verify against any known
        # version (current or superseded). Never silently downgrade this to
        # "none" - that would let real drift through unflagged.
        current = next((s for s in whole_versions if s.is_current), whole_versions[0])
        return "may_be_altered", current

    return "none", None


def _check_slot_versions(slot_versions, candidate_text):
    """Checks candidate_text against a slot's current version first, then its
    superseded versions. Returns (status, slot) or None if nothing matches."""
    current = next((s for s in slot_versions if s.is_current), None)
    superseded = [s for s in slot_versions if not s.is_current]

    if current and _matches_any_variant(current, candidate_text):
        return "intact", current

    for old_slot in superseded:
        if _matches_any_variant(old_slot, candidate_text):
            # Point at the current slot, not the superseded one that actually
            # matched: export-time behavior (flag_prominently, etc.) should
            # reflect how HHS defines this slot today.
            return "matches_prior_version", (current or old_slot)

    return None


def get_missing_required_slots(nofo):
    """
    Required slots with no matching subsection anywhere in this NOFO. This is
    a Nofo-level fact, not a per-Subsection one - deliberately not stored on
    Subsection.policy_language_status (see that field's help_text). Intended
    for use at export time (a later phase), not computed here at import time.
    """
    matched_slot_ids = set(
        nofo.sections.values_list(
            "subsections__policy_language_slot_id", flat=True
        ).distinct()
    )
    matched_slot_ids.discard(None)

    missing = []
    for slot in PolicyLanguageSlot.objects.filter(is_current=True, required=True):
        if slot.id not in matched_slot_ids:
            missing.append(slot)
    return missing
