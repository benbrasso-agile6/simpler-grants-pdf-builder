"""
Canonical HHS Department Governance policy-language slots, transcribed from
the pre-final FY27 HHS-wide NOFO Master Template (provided 2026-08-11) and,
for DG-004, the "Simpler Cost Sharing" tool document.

This is a representative subset of the ~50 slots identified during the full
review of the Master Template, not the complete catalog. It covers every
slot_type, match_scope, and flag_prominently case that was identified, so the
ingestion command can be exercised end-to-end. The remaining slots follow the
identical structure and can be appended here directly by transcribing them
from the reference doc — that's mechanical data entry, not a design question.

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
]
