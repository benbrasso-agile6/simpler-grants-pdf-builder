"""
Canonical HHS Department Governance policy-language slots, transcribed from
the pre-final FY27 HHS-wide NOFO Master Template (provided 2026-08-11) and,
for DG-004, the "Simpler Cost Sharing" tool document.

This covers every Department Governance slot identified during the four-pass
review of the Master Template, except DG-039 (a 17-item eligible-applicants
checklist) and the 3-item system checklist nested inside DG-041 - both
deliberately excluded as canonical text: their candidate spans are single- or
two-word labels ("Individuals", "SAM.gov"), and span_within_subsection checks
every subsection in a NOFO regardless of name, so text that short and generic
would false-match against unrelated prose elsewhere in the document.

Checklist-shaped content (a shared instruction followed by several
independently keep-or-delete lines, e.g. DG-006a/b, DG-015a-f, DG-026a-d,
DG-033a-d, DG-040/040a-c, DG-044a-d, DG-046a-c, DG-047/047a-f) is modeled as
one independent optional slot per line, per the resolved schema decision -
never one slot with sub-options.

Each slot is a dict with:
    slot_key           human-readable id, e.g. "DG-017"
    name                short label
    slot_type           "fixed" | "fixed_with_placeholders" | "one_of_n_options" | "parameterized_family"
    match_scope         "whole_subsection" (default) | "span_within_subsection"
    required            bool - is total absence of this slot itself a flag
    flag_prominently    bool - elevated treatment at export when non-intact
    variants            list of {label, parameter_value, canonical_text}
                         - most slots have exactly one variant
                         - one_of_n_options / parameterized_family slots have several
"""

TEMPLATE_VERSION = "FY27-draft-2026-08-11"

SLOTS = [
    {
        "slot_key": "DG-001",
        "name": "SAM.gov registration requirement",
        "slot_type": "fixed",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Your organization must have an active account with SAM.gov to "
                    "apply unless you are exempt under 2 CFR 25. SAM.gov registration "
                    "can take several weeks."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-002",
        "name": "Application portal selection",
        "slot_type": "one_of_n_options",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "label": "Option 1: Grants.gov",
                "canonical_text": (
                    "To apply for this opportunity, your organization and the people "
                    "who will work on your application must have an active account "
                    "with Grants.gov. You can follow the step-by-step instructions at "
                    "the Grants.gov Quick Start Guide for Applicants. We recommend "
                    "that you register and set up your organization's account at "
                    "least four weeks before the application deadline."
                ),
            },
            {
                "label": "Option 2: eRA Commons",
                "canonical_text": (
                    "To apply for this opportunity, your organization must register "
                    "in eRA Commons. Your senior and key personnel must also register "
                    "and affiliate their accounts with your organization's account. "
                    "We recommend that you register and set up your organization's "
                    "account at least four weeks before the application deadline."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-003",
        "name": "Cost sharing, not required",
        "slot_type": "fixed",
        # Conceptually one of two mutually-exclusive cost-sharing paths, but its
        # sibling (DG-004) is architecturally a separate parameterized_family
        # slot, not a second variant here - presence of either is optional.
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "This program has no cost sharing requirement, meaning that you "
                    "do not need to provide additional funds or contributions to the "
                    "costs of this project. If you choose to include cost sharing in "
                    "your application, we will not consider it during application "
                    "review. If you receive an award, we will include your voluntary "
                    "cost sharing commitment in the Notice of Award amount and you "
                    "must include the cost sharing funds in any required financial "
                    "and performance reports."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-004",
        "name": "Cost sharing, percentage requirement",
        "slot_type": "parameterized_family",
        "required": False,
        "flag_prominently": False,
        # Representative sample of the 99 whole-number-percentage variants (source:
        # Simpler_Cost_Sharing.docx). Text is verbatim, including the source
        # document's own errors (20% and 99% below) - see the reference doc for why.
        "variants": [
            {
                "label": "1%",
                "parameter_value": "1",
                "canonical_text": (
                    "This program requires you to contribute 1% of the project's "
                    "total cost. You can calculate this cost-sharing requirement in "
                    "two ways: Method 1: Start with the federal share. Calculation: "
                    "Divide the federal by 99. For example: $118,800 / 99 = $1,200. "
                    "Method 2: Start with the total project cost. Calculation: "
                    "Multiply the total project cost by 1%. For example: $120,000 x "
                    "1% = $1,200."
                ),
            },
            {
                "label": "15%",
                "parameter_value": "15",
                "canonical_text": (
                    "This program requires you to contribute 15% of the project's "
                    "total cost. You can calculate this cost-sharing requirement in "
                    "two ways: Method 1: Start with the federal share. Calculation: "
                    "Multiply the federal share by 15 and divide that product by 85. "
                    "For example: ($102,000 x 15) / 85 = $18,000. Method 2: Start "
                    "with the total project cost. Calculation: Multiply the total "
                    "project cost by 15%. For example: $120,000 x 15% = $18,000."
                ),
            },
            {
                "label": "20%",
                "parameter_value": "20",
                "canonical_text": (
                    "This program requires you to contribute 20% of the project's "
                    "cost. You can calculate this cost-sharing requirement in two "
                    "ways: Method 1: Start with the federal share. Calculation: "
                    "Divide the federal share by 4. For example: $96,000 / = "
                    "$24,000. Method 2: Start with the total project cost. "
                    "Calculation: Multiply the total project cost by 20%. For "
                    "example: $120,000 x 20% = $24,000."
                ),
            },
            {
                "label": "50%",
                "parameter_value": "50",
                "canonical_text": (
                    "This program requires you to contribute 50% of the project's "
                    "cost. You can calculate this cost-sharing requirement in two "
                    "ways: Method 1: Start with the federal share. Calculation: Your "
                    "cost share will equal the federal share. For example: $60,000 "
                    "federal share = $60,000 cost share. Method 2: Start with the "
                    "total project cost. Calculation: Multiply the total project "
                    "cost by 50%. For example: $120,000 x 50% = $60,000."
                ),
            },
            {
                "label": "99%",
                "parameter_value": "99",
                "canonical_text": (
                    "This program requires you to contribute 99% of the project's "
                    "cost. You can calculate this cost-sharing requirement in two "
                    "ways: Method 1: Start with the federal share. Calculation: "
                    "Multiply the federal share by 99 and divide that product by 1. "
                    "For example: ($1,200 x 99) / 1 = $11,8800. Method 2: Start with "
                    "the total project cost. Calculation: Multiply the total project "
                    "cost by 99%. For example: $120,000 x 99% = $118,800."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-005",
        "name": "Waiver of cost sharing requirements for insular areas",
        "slot_type": "fixed_with_placeholders",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Cost sharing is not required for amounts under $200,000 to the "
                    "U.S. Virgin Islands, Guam, American Samoa, and the Commonwealth "
                    "of the Northern Mariana Islands. (48 U.S.C. 1469a) We are also "
                    "extending this waiver to the Freely Associated States of the "
                    "Pacific (the Republic of the Marshall Islands, the Federated "
                    "States of Micronesia, and the Republic of Palau)."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-008",
        "name": "Indirect costs definition",
        "slot_type": "fixed",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Indirect costs are costs shared across multiple projects that "
                    "are not easily separated or allocated to a single award. See 2 "
                    "CFR 200.414."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-016",
        "name": "Initial review",
        "slot_type": "fixed",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We will review your application to make sure that it meets the "
                    "responsiveness criteria. If your application does not meet the "
                    "criteria, we will not continue to consider it."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-017",
        "name": "Risk review",
        "slot_type": "fixed",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Before we make an award, we review the risk that you may not "
                    "manage federal funds responsibly. We review your past federal "
                    "awards and your business practices to see whether you have "
                    "managed federal funds well. We use the entity information in "
                    "SAM.gov to review your history with federal awards. You may "
                    "submit comments on your organization's information in SAM.gov. "
                    "We will consider your comments before we decide your risk "
                    "level. We may also review your previous or current awards for "
                    "issues or concerns. Based on this risk review, we may ask you "
                    "for more information. If we identify a significant risk, we "
                    "may decide not to fund your application. We may also place "
                    "specific conditions on your award. To learn more about risk "
                    "reviews, see 2 CFR 200.206."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-018",
        "name": "Funding preferences/priorities for alignment with agency priorities",
        "slot_type": "fixed_with_placeholders",
        "required": True,
        "flag_prominently": True,  # confirmed: politically sensitive, elevated treatment
        "variants": [
            {
                "canonical_text": (
                    "To the extent allowed by law and court orders, we will give a "
                    "{funding preference / funding priority of [x] points} to "
                    "applications that align with Administration and agency "
                    "priorities. Before we make final funding decisions, agency "
                    "leadership will review all potential awards. In determining "
                    "whether this preference or priority applies, reviewers will "
                    "use these criteria: The project will clearly advance the "
                    "Administration's policy priorities. The project's purpose, "
                    "goals, and activities align to agency priorities (see {name of "
                    "agency priorities webpage with embedded link}). All else being "
                    "equal, preference will be given to applicants with lower "
                    "indirect cost rates. {This criterion does not apply to NIH} "
                    "The award will contribute to distributing agency funding "
                    "across a broad range of recipients rather than concentrating "
                    "funding among a select group of repeat recipients. For "
                    "scientific research, the application includes a commitment to "
                    "comply with Administration policies, procedures, and guidance "
                    "on Gold Standard Science. The applicant or project will not "
                    "promote: Racial preferences or other forms of racial "
                    "discrimination, including using race or intentional proxies "
                    "for race as a criterion for employment or program "
                    "participation. The denial of the human sex binary or the view "
                    "that sex is a chosen or changeable characteristic. Illegal "
                    "immigration. Other initiatives that compromise public safety "
                    "or promote anti-American values."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-019",
        "name": "Award notices",
        "slot_type": "fixed_with_placeholders",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If your application is successful, we will email a Notice of "
                    "Award (NoA) to your organization's authorized official. We will "
                    "also email you if we do not award your application. The NoA is "
                    "the only official award document. It tells you about the "
                    "amount of the award, important dates, and the terms and "
                    "conditions you need to follow. Until you receive the NoA, you "
                    "don't have permission to start work. If you want to know more "
                    "about terms that apply to your NoA, go to {webpage name with "
                    "embedded link to agency standard terms and conditions or "
                    "sample NoA}."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-020",
        "name": "Administrative and national policy requirements",
        "slot_type": "fixed_with_placeholders",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "There are important rules you need to read and know if you "
                    "get an award. To the extent permitted by applicable court "
                    "orders, you must follow: All terms and conditions in the NoA, "
                    "including agency-specific, program-specific, and NoA-specific "
                    "terms and conditions. The NoA also incorporates the "
                    "requirements of this NOFO. The rules in 2 CFR 200, Uniform "
                    "Administrative Requirements, Cost Principles, and Audit "
                    "Requirements and HHS-specific rules in 2 CFR 300. The HHS "
                    "Grants Policy Statement (GPS). This document includes policies "
                    "relevant to your award. If there are any exceptions to the "
                    "GPS, they'll be in your NoA. All federal statutes and "
                    "regulations, including the cited authority in this award, the "
                    "funding authority used for this award, and those highlighted "
                    "in the HHS GPS, Appendix D, HHS Administrative and National "
                    "Policy Requirements. All anti-discrimination laws: By "
                    "accepting federal funds from HHS, recipients certify "
                    "compliance with all federal anti-discrimination laws and "
                    "requirements and that complying with those laws is a material "
                    "condition of receiving federal funding. Recipients must ensure "
                    "that subrecipients, contractors, and partners also comply."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-022",
        "name": "Health IT interoperability requirements",
        "slot_type": "fixed",
        "required": False,  # conditional section
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If your project involves implementing, acquiring, or "
                    "upgrading health IT you must comply with certain Health IT "
                    "interoperability standards, as detailed in the HHS "
                    "Administrative and National Policy Requirements (HHS Grants "
                    "Policy Statement Appendix D.5.1.2). These conditions also "
                    "apply to all subrecipients."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-023",
        "name": "Cybersecurity requirements",
        "slot_type": "fixed",
        "required": False,  # conditional section
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You'll need to follow specific cybersecurity guidelines if "
                    "you receive an award and will be accessing HHS systems or "
                    "handling personal identifiable information or personal health "
                    "information, as detailed in the HHS Administrative and "
                    "National Policy Requirements (HHS Grants Policy Statement "
                    "Appendix D.5.1.1). Model your cybersecurity plan and "
                    "procedures after the National Institute of Standards and "
                    "Technology (NIST) Cybersecurity Framework."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-024-025",
        "name": "Intergovernmental review",
        "slot_type": "one_of_n_options",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "label": "Option 1: does not apply",
                "canonical_text": (
                    "Executive Order 12372, Intergovernmental Review of Federal "
                    "Programs does not apply to this NOFO. You do not need to take "
                    "any action."
                ),
            },
            {
                "label": "Option 2: applies",
                "canonical_text": (
                    "You may need to submit application information for "
                    "intergovernmental review under Executive Order 12372, "
                    "Intergovernmental Review of Federal Programs. To find if your "
                    "state requires review, see the list of state single points of "
                    "contact [PDF]. If you find a contact for your state, contact "
                    "them to learn their process. If you do not find a contact for "
                    "your state, you don't need to do anything further. This "
                    "requirement never applies to American Indian and Alaska "
                    "Native tribes or tribal organizations."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-026a",
        "name": "Get help: Grants.gov",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Grants.gov provides 24/7 support. Hold on to your ticket "
                    "number. Phone: 1-800-518-4726. Email: support@grants.gov"
                ),
            },
        ],
    },
    {
        "slot_key": "DG-026b",
        "name": "Get help: SAM.gov",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you need help, you can: Phone: 866-606-8220. Live chat "
                    "with the Federal Service Desk."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-026c",
        "name": "Get help: GrantSolutions",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "For help, contact the GrantSolutions help desk: Phone: "
                    "866-577-0771. E-mail: help@grantsolutions.gov"
                ),
            },
        ],
    },
    {
        "slot_key": "DG-026d",
        "name": "Get help: eRA Commons",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "For questions on eRA Commons registration, tracking "
                    "application status, and post-submission issues: Online: eRA "
                    "Commons Help Desk. Phone: 301-402-7469, 866-504-9552, or TTY "
                    "301-451-5939. E-mail: commons@od.nih.gov. Open Monday through "
                    "Friday from 7 a.m. to 8 p.m. ET. Closed on federal holidays."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-027",
        "name": "Future funding beyond the initial budget period",
        "slot_type": "fixed_with_placeholders",
        "match_scope": "span_within_subsection",  # nested inside a placeholder-heavy block
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Future funding beyond the initial budget period is not "
                    "guaranteed. We may provide funding for future budget periods "
                    "only if: You perform satisfactorily under this award. "
                    "Appropriated funds are available. You agree to comply with "
                    "any updated award terms and conditions. To request funding "
                    "for a future budget period, you must submit a {choose "
                    "between: competing or non-competing} continuation "
                    "application for each subsequent budget period."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-037-038",
        "name": "Application submission logistics",
        "slot_type": "one_of_n_options",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "label": "Option 1: Grants.gov",
                "canonical_text": (
                    "You must submit your application through Grants.gov. For "
                    "instructions, see the Quick Start Guide for Applicants. Keep "
                    "in mind: Grants.gov creates a date and time record when it "
                    "receives the application. If you submit the same application "
                    "more than once, we will accept the last on-time submission. "
                    "Your organization's authorized official must certify your "
                    "application. Do not encrypt, zip, or password-protect any "
                    "files. Make sure your application passes the Grants.gov "
                    "validation checks, or we may not receive it. The grants "
                    "management officer may extend an application due date based "
                    "on emergency situations such as documented natural disasters "
                    "or a verifiable widespread disruption of electric or mail "
                    "service. See Contacts and Support if you need help."
                ),
            },
            {
                "label": "Option 2: eRA ASSIST",
                "canonical_text": (
                    "To submit your application, you have three choices: Prepare "
                    "and submit your application directly in Grants.gov using "
                    "Workspace and use eRA Commons to track your application. Use "
                    "eRA ASSIST, to prepare, submit, and track your application. "
                    "Use your institution's system-to-system interface of your "
                    "choice that connects to Grants.gov. You can then use eRA "
                    "Commons to track your application. Your organization's "
                    "authorized official must certify your application. The "
                    "applicant organization must ensure that the unique entity "
                    "identifier provided on the application is the same "
                    "identifier used in the organization's profile in the eRA "
                    "Commons and for the System for Award Management. Grants.gov: "
                    "For instructions on how to submit in Grants.gov, see the "
                    "Quick Start Guide for Applicants. Make sure your application "
                    "passes the Grants.gov validation checks. See Contacts and "
                    "Support if you need help. eRA ASSIST: The Application "
                    "Submission System and Interface for Submission Tracking "
                    "(ASSIST) helps you prepare your application, submit it "
                    "through Grants.gov, and track it. You must have an eRA "
                    "Commons ID to use this system. The system will prompt your "
                    "signing official to enter the Grants.gov Authorized "
                    "Organizational Representative (AOR) credentials to submit "
                    "the application. Get help: For assistance with your "
                    "electronic application or for more information on the "
                    "electronic submission process, visit the How to Apply – "
                    "Application Guide. See tips for avoiding common errors. See "
                    "Contacts and Support, for help with systems."
                ),
            },
        ],
    },
    # ------------------------------------------------------------------
    # Remaining slots from the second/third/fourth passes over the Master
    # Template. Two things worth knowing before touching this section:
    #
    # - Checklist-shaped content (a shared instruction followed by several
    #   independently keep-or-delete lines) is modeled as one independent
    #   optional slot per line, per the resolved schema decision - not one
    #   slot with sub-options.
    # - match_scope is span_within_subsection wherever the reference doc
    #   notes that other, untracked content (an excluded placeholder, a
    #   sibling checklist line, a table header) shares the same Subsection
    #   body. whole_subsection now requires the ENTIRE body to be exactly
    #   the canonical text (see the _variant_matches fix in
    #   policy_language.py) - marking something whole_subsection when its
    #   real subsection also contains untracked sibling content would
    #   misreport every real occurrence as "may_be_altered".
    #
    # Deliberately NOT transcribed: DG-039 (the 17-item eligible-applicants
    # checklist) and DG-041's 3-item "SAM.gov / Grants.gov / eRA Commons"
    # checklist. Both are single- or two-word labels, and span_within_subsection
    # checks every subsection in the NOFO regardless of name - a canonical
    # span that short and generic ("Individuals", "SAM.gov") would false-match
    # against unrelated prose elsewhere in the document. Not worth the noise.
    # ------------------------------------------------------------------
    {
        "slot_key": "DG-006a",
        "name": "Cost sharing type: cash contributions",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Cash contributed by your organization, partners, or other "
                    "third parties."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-006b",
        "name": "Cost sharing type: in-kind contributions",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "In-kind (non-cash) contributions from partners or other "
                    "third parties."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-007",
        "name": "Cost sharing commitments",
        "slot_type": "fixed",
        "required": False,  # conditional: only applies when cost sharing applies
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you receive an award, you must provide any cost sharing "
                    "funds you committed to in your application, even if that "
                    "amount exceeds the required minimum. Cost sharing commitments "
                    "are subject to the requirements of 2 CFR 200.306. We will "
                    "include your commitment in the Notice of Award. If you don't "
                    "provide your voluntary cost share amount, we may decrease the "
                    "amount of funding we give you. You'll have to include your "
                    "cost sharing funds in your federal financial reports."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-009",
        "name": "Indirect costs, Standard rate methods",
        "slot_type": "fixed",
        "required": False,  # optional per the template's own instruction
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "To charge indirect costs you can select one of two methods: "
                    "Method 1 — Approved rate. If you currently have an indirect "
                    "cost rate approved by your cognizant federal agency, you may "
                    "use that rate. Method 2 — De minimis rate. If you do not have "
                    "an approved indirect cost rate, you may charge a de minimis "
                    "rate (see 2 CFR 200.414(f)). This rate is up to 15% of "
                    "modified total direct costs. See the definition at 2 CFR "
                    "200.1. You can use this rate indefinitely."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-010",
        "name": "Indirect costs, Training awards",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We limit indirect costs on training grants to a fixed rate "
                    "of 8% of modified total direct costs (MTDC). MTDC means 8% "
                    "of your total direct costs minus: Tuition and related fees. "
                    "Direct equipment costs. Any part of a subaward over $25,000. "
                    "See 2 CFR 300.414(a)."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-011",
        "name": "Indirect costs, Foreign entity awards",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We may pay indirect costs on grants to foreign organizations "
                    "and foreign public entities to help them meet federal "
                    "requirements. To qualify, the organization must carry out "
                    "the entire project outside U.S. territorial limits. We "
                    "limit these indirect costs to a fixed rate of 8% of "
                    "modified total direct costs (MTDC). MTDC means 8% of your "
                    "total direct costs minus: Tuition and related fees. Direct "
                    "equipment costs. Any part of a subaward over $25,000. See "
                    "2 CFR 300.414(b)."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-012",
        "name": "Program income",
        "slot_type": "fixed",
        "required": False,  # not every program generates program income
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Program income is money earned from award-supported project "
                    "activities. You must use program income for the same "
                    "purposes and under the terms and conditions of the award. "
                    "Find more about program income at 2 CFR 200.307."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-013",
        "name": "Cooperative agreement terms intro",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # sits above untracked {Bulleted list} placeholders
        "required": False,  # whole section is conditional (cooperative agreements only)
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "A cooperative agreement requires our substantial "
                    "involvement. In a cooperative agreement, HHS staff will be "
                    "actively involved in the project by providing guidance, "
                    "coordination, technical assistance, or other support."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-014",
        "name": "Find the application package",
        "slot_type": "fixed",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "The application package has all the forms you need to "
                    "apply. You can find them at this NOFO's Grants.gov "
                    "opportunity page. Then select the Package tab. We recommend "
                    "that you select the Subscribe button from the View Grant "
                    "Opportunity page for this NOFO to get updates."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-015",
        "name": "Letter of intent scaffolding",
        "slot_type": "fixed",
        "required": False,  # whole section is deletable if the agency doesn't use LOIs
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Submitting a letter of intent is optional. We use letters "
                    "of intent to estimate the number of expert reviewers needed "
                    "to evaluate applications. If you do not submit a letter of "
                    "intent, you may still apply."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-015a",
        "name": "LOI info: funding opportunity number and title",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Funding opportunity number and title."}],
    },
    {
        "slot_key": "DG-015b",
        "name": "LOI info: organization name and address",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Your organization's name and address."}],
    },
    {
        "slot_key": "DG-015c",
        "name": "LOI info: contact information",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "A contact name, phone number, and email address."}
        ],
    },
    {
        "slot_key": "DG-015d",
        "name": "LOI info: statement of interest",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "A statement of your interest in applying."}
        ],
    },
    {
        "slot_key": "DG-015e",
        "name": "LOI info: geographic areas of participation",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "The proposed geographic areas of participation."}
        ],
    },
    {
        "slot_key": "DG-015f",
        "name": "LOI info: brief organization description",
        "slot_type": "fixed",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "A brief description of your organization."}
        ],
    },
    {
        "slot_key": "DG-021",
        "name": "Alignment with agency priorities",
        "slot_type": "fixed_with_placeholders",
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Recipients must use any funds awarded under this NOFO to "
                    "advance program goals or agency priorities in alignment "
                    "with the agency priorities at {insert hyperlink to agency "
                    "priorities}, when authorized by applicable law, the program "
                    "statute, and court orders."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-028",
        "name": "Attachments submission instruction (non-research NOFOs)",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # sits inside a table alongside header labels
        "required": False,  # non-research track only
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "Insert each in a single Other Attachments form."}
        ],
    },
    {
        "slot_key": "DG-029",
        "name": "Other required forms instruction (non-research NOFOs)",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Complete these forms in Grants.gov."}],
    },
    {
        "slot_key": "DG-030",
        "name": "Application contents and format (research/R&R NOFOs)",
        "slot_type": "fixed_with_placeholders",
        "required": False,  # research/R&R track only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You must follow the instructions in the How to Apply: "
                    "Application Guide unless this NOFO says otherwise. Use the "
                    "instructions for {choose between: Research OR Career "
                    "Development OR Training OR Fellowship OR Multi-Project OR "
                    "SBIR/STTR.} We strictly enforce these requirements. If you "
                    "do not follow them, we may delay or not accept your "
                    "application for review. See responsiveness criteria to make "
                    "sure you meet all requirements. As you build your "
                    "application, keep the review criteria in mind."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-031",
        "name": "PHS 398 Research Plan form intro",
        "slot_type": "fixed",
        "required": False,  # research track only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You will use the PHS 398 Research Plan form to complete "
                    "your research plan. You will upload each of the following "
                    "parts of the form as a separate attachment. Some parts may "
                    "not be required for your application. We provide guidance "
                    "here and in the Application Guide. Follow all instructions "
                    "for this form in the application guide. We note additional "
                    "instructions in this NOFO."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-032",
        "name": "Introduction (resubmission/revision applications)",
        "slot_type": "fixed",
        "required": False,  # resubmission/revision applications only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "This section only applies to resubmission or revision "
                    "applications. Do not include this section if you are "
                    "submitting a new or renewal application."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-033a",
        "name": "Other research plan section: vertebrate animals condition",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # one row of a table with other, non-canonical rows
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you answer 'Yes' to the question 'Are Vertebrate Animals "
                    "Used?' on the R.220 - R&R Other Project Information Form."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-033b",
        "name": "Other research plan section: select agent research condition",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If your proposed activities involve the use of select "
                    "agents at any time during the proposed period of "
                    "performance."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-033c",
        "name": "Other research plan section: multiple PI/PD leadership plan condition",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you designate multiple PD/PIs (on the R.240 - R&R "
                    "Senior/Key Person Profile (Expanded) Form)."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-033d",
        "name": (
            "Other research plan section: consortium and contractual "
            "arrangements condition"
        ),
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you include any consortiums or contracts in your budget."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-034",
        "name": "Appendix (research/R&R NOFOs)",
        "slot_type": "fixed_with_placeholders",
        "required": False,  # research/R&R track only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We allow only limited appendix materials. Do not use the "
                    "appendix to get around page limits. You may attach up to "
                    "10 PDF documents in the appendix."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-035",
        "name": "PHS 398 Modular Budget Form eligibility",
        "slot_type": "fixed",
        "required": False,  # conditional on that budget-form flexibility being offered
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If the applicant is a domestic organization requesting "
                    "$250,000 or less in direct costs per budget period, you may "
                    "opt to use the PHS 398 Modular Budget Form instead of the "
                    "R&R Budget Form."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-036",
        "name": "Other Attachments Form instruction (research/R&R NOFOs)",
        "slot_type": "fixed",
        "required": False,  # research/R&R track only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You will use the Other Attachments form to upload the "
                    "following attachments."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-040",
        "name": "Responsiveness criteria intro",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # nested intro to 3 independently-deletable bullets
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We will review your application to make sure it meets "
                    "these requirements. We won't consider an application that:"
                ),
            },
        ],
    },
    {
        "slot_key": "DG-040a",
        "name": "Responsiveness criteria: eligibility",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Does not meet all eligibility criteria."}],
    },
    {
        "slot_key": "DG-040b",
        "name": "Responsiveness criteria: deadline",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Is submitted after the deadline."}],
    },
    {
        "slot_key": "DG-040c",
        "name": "Responsiveness criteria: required forms",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Does not include all required forms and documents in the "
                    "application checklist."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-041a",
        "name": "Get registered recap intro",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # nested intro to a system checklist, deliberately not transcribed (too short/generic - see file header note)
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Make sure you have an active account with:"}],
    },
    {
        "slot_key": "DG-041b",
        "name": "Get registered recap closing",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "See Before You Get Started to learn how. Need help? See "
                    "Contacts and Support."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-042",
        "name": "Salary rate limitation",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # one fixed bullet among otherwise-placeholder siblings
        "required": False,  # deletable if not funded by the Annual Appropriations Act
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "The salary rate limitation in the current appropriations "
                    "act applies to this program. You may not use funds under "
                    "this award to pay all or part of a salary that is higher "
                    "than the current Federal Executive Level II rate. This "
                    "salary rate applies to both direct and indirect costs."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-043",
        "name": "Unallowable costs, fixed framing",
        "slot_type": "fixed_with_placeholders",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You may not use funds for: {Insert bulleted list of "
                    "unallowable costs} For guidance on some types of "
                    "restricted or not allowed costs, see 2 CFR 200.420 "
                    "(Considerations for Selected Items of Cost), 2 CFR "
                    "300.218, and 2 CFR 300.219."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-044a",
        "name": "Narrative format requirement: font color",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # font size is an excluded, untracked sibling placeholder
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Font color: Black"}],
    },
    {
        "slot_key": "DG-044b",
        "name": "Narrative format requirement: spacing",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Spacing: Single-spaced"}],
    },
    {
        "slot_key": "DG-044c",
        "name": "Narrative format requirement: margins",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Margins: 1-inch"}],
    },
    {
        "slot_key": "DG-044d",
        "name": "Narrative format requirement: page size",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Size: 8.5 by 11 inches"}],
    },
    {
        "slot_key": "DG-045",
        "name": "Project summary instructions",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # shares a body with the DG-046 checklist
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Page limit: 1. Write a one-page summary of your proposed "
                    "project using the instructions. Do not include any "
                    "proprietary or confidential information, jargon, or "
                    "acronyms. We will use this document for information "
                    "sharing and public information requests if you receive an "
                    "award."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-046a",
        "name": "Project summary basic info: organization name",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "The name of your organization."}],
    },
    {
        "slot_key": "DG-046b",
        "name": "Project summary basic info: subrecipients",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "The names of any subrecipients or sub-awardee "
                    "organizations, if applicable."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-046c",
        "name": "Project summary basic info: total budget amount",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Total budget amount."}],
    },
    {
        "slot_key": "DG-047",
        "name": "Award description guidance intro",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # nested intro to 6 independently-deletable bullets
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "We may use this portion of your project summary publicly "
                    "on USASpending.gov. In plain language, briefly describe:"
                ),
            },
        ],
    },
    {
        "slot_key": "DG-047a",
        "name": "Award description guidance: purpose",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "The award's purpose."}],
    },
    {
        "slot_key": "DG-047b",
        "name": "Award description guidance: activities",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {"canonical_text": "An understanding of the project's activities."}
        ],
    },
    {
        "slot_key": "DG-047c",
        "name": "Award description guidance: deliverables and outcomes",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "The expected deliverables and expected outcomes."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-047d",
        "name": "Award description guidance: beneficiaries",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Who will benefit from the award."}],
    },
    {
        "slot_key": "DG-047e",
        "name": "Award description guidance: main goals",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Your project's main goals."}],
    },
    {
        "slot_key": "DG-047f",
        "name": "Award description guidance: subrecipient activities",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",
        "required": False,
        "flag_prominently": False,
        "variants": [{"canonical_text": "Any known subrecipient activities."}],
    },
    {
        "slot_key": "DG-048",
        "name": "Project narrative heading instruction",
        "slot_type": "fixed",
        "match_scope": "span_within_subsection",  # followed by untracked, placeholder-paired headings
        "required": True,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "Your project narrative must use these exact headings, "
                    "subheadings, and order:"
                ),
            },
        ],
    },
    {
        "slot_key": "DG-049",
        "name": "Scoring process, non-research NOFOs",
        "slot_type": "fixed",
        "required": False,  # non-research track only
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "You can find the merit review criteria for each relevant "
                    "application section in Step 3: Build Your Application."
                ),
            },
        ],
    },
    {
        "slot_key": "DG-050",
        "name": "Reporting, fixed framing",
        "slot_type": "fixed_with_placeholders",
        "required": False,
        "flag_prominently": False,
        "variants": [
            {
                "canonical_text": (
                    "If you receive an award, you will have to submit "
                    "financial and performance reports. These include "
                    "financial and performance reports. {Insert NOFO-specific "
                    "reporting detail} To learn more about these reporting "
                    "requirements, see {name of site with embedded link} on "
                    "our website."
                ),
            },
        ],
    },
]
