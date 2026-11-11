"""Grade 10 Accounting: GAAP and Accounting Principles Generator.
Grounded in curriculum_docs_auto/Accounting_Gr10/Term 1/01. Accounting principles.md
(Via Afrika Grade 10 Accounting, Topic 3, Pages 24-29).

Covers 7 distinct, non-overlapping curriculum subskills:
1. gaap_concepts_and_policy (Definition, SAICA role, IFRS alignment, Accounting Policy)
2. historical_cost_principle (Cost price recording, revaluation vs balance sheet, objective proof)
3. business_entity_rule (Drawings vs expenses, personal bank accounts, separate legal/accounting unit)
4. matching_principle (Matching expenses to revenue in same period, prepaid & accrued adjustments)
5. prudence_conservatism_principle (Conservative reporting under uncertainty, bad debts, stock valuation)
6. materiality_and_going_concern (Materiality threshold for separate disclosure, going concern assumption)
7. gaap_matching_table (Full tabular matching of real transactions to GAAP principles with markdown table memo)
"""
from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional

from app.utils.sole_trader.names import pick_business_name, pick_person_names

SUBSKILLS = [
    "gaap_concepts_and_policy",
    "historical_cost_principle",
    "business_entity_rule",
    "matching_principle",
    "prudence_conservatism_principle",
    "materiality_and_going_concern",
    "gaap_matching_table",
]

ARCHETYPES = SUBSKILLS
VALID_SUBSKILLS = SUBSKILLS


def _clean_sole_trader_name(biz_name: str) -> str:
    """Removes (Pty) Ltd, Ltd, or CC suffixes for Grade 10 Sole Trader syllabus compliance."""
    for suffix in [" (Pty) Ltd", " Pty Ltd", " (Pty)", " Ltd", " CC", " (CC)"]:
        if biz_name.endswith(suffix):
            biz_name = biz_name[:-len(suffix)].strip()
    return biz_name


def _build_context(rng: random.Random) -> Dict[str, str]:
    raw_biz = pick_business_name(r=rng)
    biz = _clean_sole_trader_name(raw_biz)
    owner = pick_person_names(r=rng, k=1)[0]
    towns = [
        "Polokwane", "Nelspruit", "Rustenburg", "Kimberley", "Bloemfontein",
        "Pietermaritzburg", "Soweto", "Umlazi", "George", "Mthatha", "Mahikeng"
    ]
    town = rng.choice(towns)
    return {"owner": owner, "business": biz, "town": town}


# ---------------------------------------------------------------------------
# 1. GAAP Concepts & Policy Builder
# ---------------------------------------------------------------------------
def _build_gaap_concepts_and_policy(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    variant_type = rng.choice(["policy_definition", "saica_role", "standardization_purpose"])
    owner = ctx["owner"]
    biz = ctx["business"]
    town = ctx["town"]

    if variant_type == "policy_definition":
        prompt = (
            f"{owner} runs a sole proprietorship called **{biz}** in {town}. "
            f"The business engages in repetitive transactions such as buying inventory on credit and depreciating vehicles.\n\n"
            f"**Question:**\n"
            f"Define what is meant by an **Accounting Policy**, and explain why it is essential for {biz} to state its accounting policies in the notes to the Financial Statements."
        )
        sample_answer = (
            "An accounting policy is a predetermined set of decisions and rules governing how a business manages and records repetitive transactions to ensure consistent results across financial periods. "
            "It must be stated in the notes so that users of financial statements understand the basis of calculation (e.g., the method of depreciation used) and can compare results reliably."
        )
        sol = (
            "**Step 1: Definition of Accounting Policy**\n"
            "An accounting policy is a specific set of rules, principles, and guidelines adopted by a business to manage, record, and present repetitive transactions consistently.\n\n"
            "**Step 2: Reason for Disclosure**\n"
            "Because transactions (such as calculating depreciation or valuing stock) can be managed using different methods, publicising the accounting policy in the notes informs lenders, SARS, and the owner exactly which methods were applied, ensuring consistency and transparency."
        )
        rubric = ["set of decisions/rules for repetitive transactions", "ensures consistency", "informs users/enables comparison"]
        return {
            "id": f"acct10_gaap_policy_{uuid.uuid4().hex[:10]}",
            "question_type": "typed",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "expected_answer": sample_answer,
            "worked_solution": sol,
            "explanation": "Accounting policy provides consistent rules for repetitive events, disclosed in notes for comparability.",
            "marking_schema": rubric,
            "grading_rubric": rubric,
            "marks": 4,
            "subskill": "gaap_concepts_and_policy",
            "hints": {
                "tier_1": "Think about why a business needs a regular rule for transactions that happen again and again.",
                "tier_2": "Consider what happens if one year you use straight-line depreciation and the next year diminishing balance without explaining it.",
                "tier_3": "Mention that policy is a predetermined set of decisions ensuring consistent reporting, disclosed in notes for transparency."
            },
            "difficulty": "medium",
            "modality": "accounting",
            "solution_type": "short_answer",
        }

    elif variant_type == "saica_role":
        prompt = (
            f"In South Africa, financial accounting standards are grounded in international best practice.\n\n"
            f"Which professional body is responsible for training, developing, and regulating chartered accountants and issuing statements regarding GAAP in South Africa?\n\n"
            f"A. South African Revenue Service (SARS)\n"
            f"B. South African Institute of Chartered Accountants (SAICA)\n"
            f"C. Financial Sector Conduct Authority (FSCA)\n"
            f"D. Companies and Intellectual Property Commission (CIPC)"
        )
        options = [
            "South African Revenue Service (SARS)",
            "South African Institute of Chartered Accountants (SAICA)",
            "Financial Sector Conduct Authority (FSCA)",
            "Companies and Intellectual Property Commission (CIPC)"
        ]
        sol = (
            "**Correct Answer:** **B. South African Institute of Chartered Accountants (SAICA)**\n\n"
            "**Explanation:**\n"
            "- **SAICA** is the primary professional body in South Africa responsible for the education, training, and standard-setting of professional accountants.\n"
            "- **SARS** collects national revenue and administers tax legislation.\n"
            "- **CIPC** registers businesses and intellectual property.\n"
            "- **FSCA** regulates market conduct of financial institutions."
        )
        return {
            "id": f"acct10_gaap_saica_{uuid.uuid4().hex[:10]}",
            "question_type": "multiple_choice",
            "prompt": prompt,
            "options": options,
            "correct_index": 1,
            "correct_idx": 1,
            "correct_answer": "South African Institute of Chartered Accountants (SAICA)",
            "expected_answer": "South African Institute of Chartered Accountants (SAICA)",
            "worked_solution": sol,
            "explanation": "SAICA is the professional body governing accounting standards and training in South Africa.",
            "marks": 2,
            "subskill": "gaap_concepts_and_policy",
            "hints": {
                "tier_1": "Look for the institute that specifically trains and certifies Chartered Accountants (CAs).",
                "tier_2": "The acronym begins with 'SA' and ends with 'CA' (Chartered Accountants).",
                "tier_3": "Select South African Institute of Chartered Accountants (SAICA)."
            },
            "difficulty": "easy",
            "modality": "accounting",
            "solution_type": "multiple_choice",
        }

    else:
        prompt = (
            f"{owner}, owner of **{biz}**, asks their bookkeeper: *'Why must I follow GAAP rules? Why can't I just present my financial records in whatever format I prefer?'*\n\n"
            f"Which of the following is the most fundamental reason why all businesses must adhere to Generally Accepted Accounting Practice (GAAP)?\n\n"
            f"A. GAAP guarantees that the business will achieve an operating profit each year.\n"
            f"B. GAAP replaces the requirement to keep physical source documents.\n"
            f"C. GAAP provides a standardised framework ensuring financial statements are consistent, reliable, and comparable across different businesses and time periods.\n"
            f"D. GAAP allows the sole trader to avoid paying personal income tax."
        )
        options = [
            "GAAP guarantees that the business will achieve an operating profit each year.",
            "GAAP replaces the requirement to keep physical source documents.",
            "GAAP provides a standardised framework ensuring financial statements are consistent, reliable, and comparable across different businesses and time periods.",
            "GAAP allows the sole trader to avoid paying personal income tax."
        ]
        sol = (
            "**Correct Answer:** **C. GAAP provides a standardised framework ensuring financial statements are consistent, reliable, and comparable across different businesses and time periods.**\n\n"
            "**Explanation:**\n"
            "Without GAAP, each business would create its own reporting rules, making it impossible for banks, investors, SARS, and suppliers to evaluate or compare financial performance."
        )
        return {
            "id": f"acct10_gaap_standard_{uuid.uuid4().hex[:10]}",
            "question_type": "multiple_choice",
            "prompt": prompt,
            "options": options,
            "correct_index": 2,
            "correct_idx": 2,
            "correct_answer": options[2],
            "expected_answer": options[2],
            "worked_solution": sol,
            "explanation": "GAAP establishes standardized rules ensuring comparability, consistency, and reliability in financial reporting.",
            "marks": 2,
            "subskill": "gaap_concepts_and_policy",
            "hints": {
                "tier_1": "Think about what happens if two companies use completely different languages to describe their profit.",
                "tier_2": "Focus on consistency, reliability, and comparability for outside stakeholders.",
                "tier_3": "Select the option emphasizing the standardized framework for consistency and comparability."
            },
            "difficulty": "easy",
            "modality": "accounting",
            "solution_type": "multiple_choice",
        }


# ---------------------------------------------------------------------------
# 2. Historical Cost Principle Builder
# ---------------------------------------------------------------------------
def _build_historical_cost_principle(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]
    years_ago = rng.randint(2, 5)
    cost_price = rng.randint(45, 95) * 10000  # R450,000 to R950,000
    appreciation = rng.randint(15, 40) * 10000
    market_value = cost_price + appreciation

    prompt = (
        f"{years_ago} years ago, {owner} purchased Land and Buildings for **{biz}** at a total purchase cost of **R{cost_price:,.2f}**, supported by a title deed and transfer documents.\n\n"
        f"At the end of the current financial year, an accredited real estate appraiser values the property at **R{market_value:,.2f}** due to commercial development in the area.\n\n"
        f"**Required:**\n"
        f"1. According to the **Historical Cost Principle**, state the exact valuation amount that must be recorded for Land and Buildings in the Balance Sheet at year-end.\n"
        f"2. In 1–2 sentences, explain why accounting standards require this historical cost amount rather than the current market valuation of R{market_value:,.2f}."
    )

    sol = (
        f"**1. Valuation in Balance Sheet:**\n"
        f"$$\\mathbf{{R{cost_price:,.2f}}}$$\n\n"
        f"**2. Accounting Justification:**\n"
        f"Under the **Historical Cost Principle**, assets must always be recorded at their original cost of acquisition. "
        f"The purchase price of R{cost_price:,.2f} is supported by verifiable, objective source documents (transfer contract, receipts), "
        f"whereas the market value of R{market_value:,.2f} is an unverified subjective estimate that fluctuates over time."
    )

    sample_answer = f"1. R{cost_price:,.2f}\n2. The historical cost principle requires assets to be shown at original cost price because it is objective and supported by documentary evidence, whereas market value is subjective."
    rubric = [f"R{cost_price:,.2f}", "recorded at cost price/original purchase price", "objective/verifiable documentary proof vs subjective valuation"]

    return {
        "id": f"acct10_gaap_hist_cost_{uuid.uuid4().hex[:10]}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "worked_solution": sol,
        "explanation": "Historical cost requires assets to remain recorded at original acquisition cost because it is verifiable and objective.",
        "marking_schema": rubric,
        "grading_rubric": rubric,
        "marks": 4,
        "subskill": "historical_cost_principle",
        "hints": {
            "tier_1": "Does the historical cost principle allow a business to write up the value of an asset just because market prices rose?",
            "tier_2": "Look at the original price paid on the source document versus the estimated appraisal price.",
            "tier_3": f"Enter R{cost_price:,.2f} and explain that historical cost is objective and verifiable."
        },
        "difficulty": "medium",
        "modality": "accounting",
        "solution_type": "short_answer",
    }


# ---------------------------------------------------------------------------
# 3. Business Entity Rule Builder
# ---------------------------------------------------------------------------
def _build_business_entity_rule(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]
    rent_expense = rng.randint(18, 35) * 1000
    salaries = rng.randint(40, 80) * 1000
    school_fees = rng.randint(8, 18) * 1000
    personal_groceries = rng.randint(3, 7) * 1000
    total_drawings = school_fees + personal_groceries
    true_operating = rent_expense + salaries
    total_withdrawn = true_operating + total_drawings

    prompt = (
        f"During the financial year, {owner}, the sole proprietor of **{biz}**, made several payments totaling **R{total_withdrawn:,.2f}** from the business bank account:\n\n"
        f"- Rent for the business premises: **R{rent_expense:,.2f}**\n"
        f"- Staff salaries: **R{salaries:,.2f}**\n"
        f"- School fees for {owner}'s children: **R{school_fees:,.2f}**\n"
        f"- Private household groceries for {owner}'s family: **R{personal_groceries:,.2f}**\n\n"
        f"**Required:**\n"
        f"1. State the **GAAP principle** that forbids recording the school fees and personal groceries as business operating expenses.\n"
        f"2. State the account in the General Ledger to which the R{total_drawings:,.2f} (R{school_fees:,.2f} + R{personal_groceries:,.2f}) must be debited.\n"
        f"3. Calculate the total allowable **Operating Expenses** for {biz}."
    )

    sol = (
        "**1. Applicable GAAP Principle:**\n"
        "$$\\mathbf{Business\\ Entity\\ Rule}$$\n\n"
        "**2. General Ledger Account:**\n"
        "$$\\mathbf{Drawings}$$\n\n"
        f"**3. Calculation of Allowable Business Operating Expenses:**\n"
        f"$$\\text{{Operating Expenses}} = \\text{{Rent}} + \\text{{Salaries}}$$\n"
        f"$$\\text{{Operating Expenses}} = R{rent_expense:,.2f} + R{salaries:,.2f} = \\mathbf{{R{true_operating:,.2f}}}$$\n\n"
        f"*(Note: The personal expenses of R{total_drawings:,.2f} reduce Owner's Equity via Drawings and must never be shown on the Income Statement).*"
    )

    sample_answer = f"1. Business Entity Rule\n2. Drawings\n3. R{true_operating:,.2f}"
    rubric = ["Business Entity Rule", "Drawings", f"R{true_operating:,.2f}"]

    return {
        "id": f"acct10_gaap_entity_{uuid.uuid4().hex[:10]}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "worked_solution": sol,
        "explanation": "Business entity rule separates owner personal affairs from business records. Personal expenses are Drawings.",
        "marking_schema": rubric,
        "grading_rubric": rubric,
        "marks": 5,
        "subskill": "business_entity_rule",
        "hints": {
            "tier_1": "Which principle states that the owner and the business are two separate accounting entities?",
            "tier_2": "Personal expenses paid with business funds belong in the Drawings account, not in operating expenses.",
            "tier_3": f"Principle: Business Entity Rule. Account: Drawings. Operating expenses = R{rent_expense:,.2f} + R{salaries:,.2f} = R{true_operating:,.2f}."
        },
        "difficulty": "medium",
        "modality": "accounting",
        "solution_type": "short_answer",
    }


# ---------------------------------------------------------------------------
# 4. Matching Principle Builder
# ---------------------------------------------------------------------------
def _build_matching_principle(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]
    monthly_rent = rng.randint(4, 9) * 1000  # R4,000 to R9,000 / month
    is_prepaid = rng.choice([True, False])

    if is_prepaid:
        months_paid = 13
        total_paid = monthly_rent * months_paid
        correct_expense = monthly_rent * 12
        adjustment_amt = monthly_rent
        adj_name = "Prepaid Expense (Asset)"
        note_name = "Trade and Other Receivables"
        scenario_text = (
            f"The trial balance of **{biz}** on 28 February 2024 reflects Rent Expense as **R{total_paid:,.2f}**. "
            f"An audit of the lease agreement indicates that rent was paid for **13 months** (up to 31 March 2024) at **R{monthly_rent:,.2f}** per month."
        )
    else:
        months_paid = 11
        total_paid = monthly_rent * months_paid
        correct_expense = monthly_rent * 12
        adjustment_amt = monthly_rent
        adj_name = "Accrued Expense (Liability)"
        note_name = "Trade and Other Payables"
        scenario_text = (
            f"The trial balance of **{biz}** on 28 February 2024 reflects Rent Expense as **R{total_paid:,.2f}**. "
            f"An audit of the lease agreement reveals that rent was only paid for **11 months** at **R{monthly_rent:,.2f}** per month; the rent for February has not yet been paid."
        )

    prompt = (
        f"{scenario_text}\n\n"
        f"**Required:**\n"
        f"1. Name the **GAAP principle** that dictates the rent expense for the financial year must cover exactly 12 months.\n"
        f"2. Calculate the exact amount of Rent Expense that must be reported in the **Income Statement** for the year ended 28 February 2024.\n"
        f"3. State the amount and the classification (**{adj_name}**) to be recorded in the Balance Sheet note (**{note_name}**)."
    )

    sol = (
        "**1. GAAP Principle:**\n"
        "$$\\mathbf{Matching\\ Principle}$$\n"
        "*(All expenses incurred to generate income must be matched to that income during the current 12-month accounting period, regardless of when cash is paid).*\n\n"
        f"**2. Income Statement Amount (12 Months):**\n"
        f"$$\\text{{Rent Expense}} = 12 \\times R{monthly_rent:,.2f} = \\mathbf{{R{correct_expense:,.2f}}}$$\n\n"
        f"**3. Year-end Balance Sheet Adjustment:**\n"
        f"- Adjustment Amount: $R{total_paid:,.2f} - R{correct_expense:,.2f} = \\mathbf{{R{adjustment_amt:,.2f}}}$ (or 1 month outstanding)\n"
        f"- Classification: **{adj_name}** in the **{note_name}** note."
    )

    sample_answer = f"1. Matching Principle\n2. R{correct_expense:,.2f}\n3. R{adjustment_amt:,.2f} ({adj_name} in {note_name})"
    rubric = ["Matching Principle", f"R{correct_expense:,.2f}", f"R{adjustment_amt:,.2f}", adj_name]

    return {
        "id": f"acct10_gaap_matching_{uuid.uuid4().hex[:10]}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "worked_solution": sol,
        "explanation": "Matching principle matches expenses incurred to income earned in the same 12-month period.",
        "marking_schema": rubric,
        "grading_rubric": rubric,
        "marks": 5,
        "subskill": "matching_principle",
        "hints": {
            "tier_1": "Which principle links expenses directly to the 12-month financial period they helped produce income for?",
            "tier_2": f"Calculate 12 months × R{monthly_rent:,.2f} to find the true Income Statement figure.",
            "tier_3": f"Matching Principle. Income Statement: R{correct_expense:,.2f}. Balance Sheet adjustment: R{adjustment_amt:,.2f} ({adj_name})."
        },
        "difficulty": "hard",
        "modality": "accounting",
        "solution_type": "short_answer",
    }


# ---------------------------------------------------------------------------
# 5. Prudence & Conservatism Principle Builder
# ---------------------------------------------------------------------------
def _build_prudence_conservatism_principle(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]
    debtor_name = pick_person_names(r=rng, k=1)[0]
    debt_amount = rng.randint(35, 95) * 100
    cost_stock = rng.randint(40, 80) * 1000
    nrv_stock = cost_stock - (rng.randint(6, 15) * 1000)

    prompt = (
        f"At the financial year-end of **{biz}**, the bookkeeper encounters two uncertain situations:\n\n"
        f"**Situation A:** A debtor, {debtor_name}, owes **R{debt_amount:,.2f}** but has been declared insolvent. Although {owner} hopes to recover some funds in the future, the bookkeeper writes off the debt as **Bad Debts** immediately.\n\n"
        f"**Situation B:** Trading inventory that cost **R{cost_stock:,.2f}** is damaged and can now only be sold for a net realizable value of **R{nrv_stock:,.2f}**. The bookkeeper values the inventory in the Balance Sheet at R{nrv_stock:,.2f}.\n\n"
        f"**Required:**\n"
        f"1. Name the **GAAP principle** applied in both situations.\n"
        f"2. Explain what this principle requires the accountant to do when facing uncertainties regarding asset values."
    )

    sol = (
        "**1. Applicable GAAP Principle:**\n"
        "$$\\mathbf{Prudence\\ (Conservatism)\\ Principle}$$\n\n"
        "**2. Explanation:**\n"
        "The **Prudence Principle** dictates that when an accountant faces uncertainty about the valuation of assets or income, "
        "they must exercise conservatism. Potential losses (such as bad debts or inventory markdowns) must be anticipated and recorded immediately, "
        "while potential gains are never recognized until realized. The accountant must choose the valuation that has the **least favorable impact on Owner's Equity** to avoid overstating assets."
    )

    sample_answer = "1. Prudence (Conservatism) Principle\n2. The accountant must be conservative when uncertain, recording potential losses immediately and choosing values that do not overstate assets or equity."
    rubric = ["Prudence/Conservatism", "conservative approach to uncertainty", "losses anticipated immediately / avoid overstating assets/equity"]

    return {
        "id": f"acct10_gaap_prudence_{uuid.uuid4().hex[:10]}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer": sample_answer,
        "worked_solution": sol,
        "explanation": "Prudence requires conservative valuation under uncertainty to prevent overstating assets and profits.",
        "marking_schema": rubric,
        "grading_rubric": rubric,
        "marks": 4,
        "subskill": "prudence_conservatism_principle",
        "hints": {
            "tier_1": "Which principle is also known as conservatism and tells the accountant not to be overly optimistic?",
            "tier_2": "Think about why accountants write off bad debts immediately rather than hoping for payment.",
            "tier_3": "Prudence Principle. The accountant must anticipate losses and avoid overstating assets or equity."
        },
        "difficulty": "medium",
        "modality": "accounting",
        "solution_type": "short_answer",
    }


# ---------------------------------------------------------------------------
# 6. Materiality & Going Concern Builder
# ---------------------------------------------------------------------------
def _build_materiality_and_going_concern(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]
    variant = rng.choice(["materiality", "going_concern"])

    if variant == "materiality":
        interest_amt = rng.randint(12, 45) * 1000
        stapler_cost = rng.randint(120, 350)
        prompt = (
            f"In preparing the financial records of **{biz}**, two transactions occurred:\n\n"
            f"- Transaction 1: The business paid **R{interest_amt:,.2f}** in interest on a bank overdraft. This is disclosed as a separate line item (**Interest Expense**) in the notes to the Financial Statements.\n"
            f"- Transaction 2: The business bought heavy-duty office staplers for **R{stapler_cost:,.2f}** that will last for 5 years. Instead of recording them as Fixed Assets and depreciating them over 5 years, the bookkeeper wrote off the entire R{stapler_cost:,.2f} as **Stationery / Consumable Stores** expense.\n\n"
            f"**Required:**\n"
            f"Name the **GAAP principle** that governs both decisions, and explain why significant amounts must be separated while trivial amounts can be grouped or expensed immediately."
        )
        sol = (
            "**1. Applicable GAAP Principle:**\n"
            "$$\\mathbf{Principle\\ of\\ Materiality}$$\n\n"
            "**2. Explanation:**\n"
            "- Significant (material) amounts (such as interest of R{interest_amt:,.2f}) can influence the economic decisions of lenders and investors and must be disclosed separately.\n"
            "- Trivial (immaterial) amounts (such as a R{stapler_cost:,.2f} stapler) would clutter the financial statements and add unnecessary bookkeeping costs without providing useful insight, so they are expensed immediately."
        )
        sample_answer = "1. Materiality Principle\n2. Material items influence financial decision-making and must be disclosed separately; immaterial items do not affect decisions and can be grouped or expensed to avoid clutter."
        rubric = ["Materiality", "influences financial decisions", "separate disclosure for significant vs grouped/expensed for immaterial"]
        return {
            "id": f"acct10_gaap_materiality_{uuid.uuid4().hex[:10]}",
            "question_type": "typed",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "expected_answer": sample_answer,
            "worked_solution": sol,
            "explanation": "Materiality requires separate disclosure for significant items, allowing trivial items to be grouped or expensed.",
            "marking_schema": rubric,
            "grading_rubric": rubric,
            "marks": 4,
            "subskill": "materiality_and_going_concern",
            "hints": {
                "tier_1": "Think about whether an item is large enough or important enough to change someone's decision.",
                "tier_2": "The principle has 'material' in its name.",
                "tier_3": "Principle of Materiality. Significant amounts influence decisions; insignificant amounts are grouped."
            },
            "difficulty": "medium",
            "modality": "accounting",
            "solution_type": "short_answer",
        }

    else:
        book_val = rng.randint(30, 60) * 10000
        forced_val = book_val // 2
        prompt = (
            f"The trading stock and delivery equipment of **{biz}** have a combined carrying value of **R{book_val:,.2f}** in the ledger.\n\n"
            f"If {biz} were to shut down immediately today and hold an emergency auction, these assets would only fetch **R{forced_val:,.2f}**.\n\n"
            f"However, the financial statements are prepared assuming that {biz} will continue operating for the foreseeable future, so the assets are not written down to forced-liquidation value.\n\n"
            f"**Required:**\n"
            f"State the **GAAP principle** that justifies valuing assets on an operating basis rather than an emergency liquidation basis."
        )
        sol = (
            "**Correct GAAP Principle:**\n"
            "$$\\mathbf{Going\\ Concern\\ Concept}$$\n\n"
            "**Explanation:**\n"
            "The **Going Concern** principle assumes that a business will continue to exist and operate for the foreseeable future. "
            "Therefore, non-current and current assets are valued based on their ongoing operational cost, rather than the distress/break-up values that would occur in an immediate liquidation."
        )
        sample_answer = "Going Concern Concept"
        rubric = ["Going Concern"]
        return {
            "id": f"acct10_gaap_going_concern_{uuid.uuid4().hex[:10]}",
            "question_type": "typed",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "expected_answer": sample_answer,
            "worked_solution": sol,
            "explanation": "Going concern assumes the business will continue operating indefinitely, avoiding liquidation valuations.",
            "marking_schema": rubric,
            "grading_rubric": rubric,
            "marks": 2,
            "subskill": "materiality_and_going_concern",
            "hints": {
                "tier_1": "Which principle assumes that the business will 'keep going'?",
                "tier_2": "It is a two-word term meaning the entity will continue operating.",
                "tier_3": "Going Concern Concept."
            },
            "difficulty": "easy",
            "modality": "accounting",
            "solution_type": "short_answer",
        }


# ---------------------------------------------------------------------------
# 7. GAAP Matching Table Builder (Via Afrika Activity 1 Standard)
# ---------------------------------------------------------------------------
def _build_gaap_matching_table(rng: random.Random, ctx: Dict[str, str]) -> Dict[str, Any]:
    owner = ctx["owner"]
    biz = ctx["business"]

    # Authentic pool of 8 scenarios grounded in Via Afrika Grade 10 Topic 3 Page 29
    scenario_pool = [
        (
            f"Assets purchased by {biz} must be recorded in the books at original purchase cost price.",
            "Historical cost"
        ),
        (
            f"All transactions taking place during the 12-month financial period must be recorded in that period, regardless of when cash is received or paid.",
            "Matching principle"
        ),
        (
            f"The personal financial affairs of {owner} must be kept completely separate from the business records of {biz}.",
            "Business entity rule"
        ),
        (
            f"Financial statements are prepared under the assumption that {biz} will continue to operate for the foreseeable future.",
            "Going concern"
        ),
        (
            f"When uncertain about an asset valuation, the accountant chooses the conservative value with the least favorable effect on equity (e.g. writing off Bad Debts).",
            "Prudence (conservatism)"
        ),
        (
            f"Significant items such as interest expense must be disclosed separately, while trivial stationery purchases are expensed immediately.",
            "Materiality"
        ),
        (
            f"{owner} cannot record their personal private vehicle as an asset of {biz}.",
            "Business entity rule"
        ),
        (
            f"Vehicles bought 3 years ago are still shown at cost price in the balance sheet note, even though market values have changed.",
            "Historical cost"
        ),
    ]

    # Select 6 items deterministically
    shuffled = list(scenario_pool)
    rng.shuffle(shuffled)
    selected_pairs = shuffled[:6]

    principles = [
        "Historical cost",
        "Prudence (conservatism)",
        "Materiality",
        "Business entity rule",
        "Going concern",
        "Matching principle"
    ]

    prompt_table_rows = []
    memo_table_rows = []
    answers_dict = {}

    for i, (desc, ans) in enumerate(selected_pairs, 1):
        prompt_table_rows.append(f"| {i} | {desc} | [ Option A–F ] |")
        memo_table_rows.append(f"| {i} | {desc} | **{ans}** |")
        answers_dict[str(i)] = ans

    prompt_table = (
        "| # | Transaction / Accounting Scenario | GAAP Principle (Match A–F) |\n"
        "| :---: | :--- | :--- |\n" +
        "\n".join(prompt_table_rows)
    )

    memo_table = (
        "| # | Transaction / Accounting Scenario | Correct GAAP Principle |\n"
        "| :---: | :--- | :--- |\n" +
        "\n".join(memo_table_rows)
    )

    principles_key = "\n".join([f"**{chr(65+idx)}.** {p}" for idx, p in enumerate(principles)])

    prompt = (
        f"**Activity: Matching GAAP Principles to Business Transactions**\n\n"
        f"{owner} has reviewed the following transactions for **{biz}**. "
        f"Match each scenario in the table below to the correct GAAP principle from the word bank.\n\n"
        f"**Word Bank:**\n"
        f"{principles_key}\n\n"
        f"{prompt_table}\n\n"
        f"**Required:** Write down the matching GAAP principle for numbers 1 to 6."
    )

    sol = (
        "### Memorandum & Worked Solution:\n\n"
        f"{memo_table}\n\n"
        "**Scoring Rubric:** 1 mark per correct match (Total: 6 marks)."
    )

    return {
        "id": f"acct10_gaap_match_tbl_{uuid.uuid4().hex[:10]}",
        "question_type": "table_fill",
        "prompt": prompt,
        "sample_answer": sol,
        "expected_answer": answers_dict,
        "worked_solution": sol,
        "explanation": "Matching authentic South African business transactions to the 6 core GAAP principles.",
        "marking_schema": [f"Item {k}: {v}" for k, v in answers_dict.items()],
        "grading_rubric": [f"Item {k}: {v}" for k, v in answers_dict.items()],
        "marks": 6,
        "subskill": "gaap_matching_table",
        "hints": {
            "tier_1": "Review the definitions: Historical cost (purchase price), Entity (owner vs business), Matching (12-month period), Prudence (conservative/losses), Materiality (significance), Going concern (continues operating).",
            "tier_2": "Match each description directly against the core word in the word bank.",
            "tier_3": "Refer to the memorandum table for the exact matched pairs."
        },
        "difficulty": "medium",
        "modality": "accounting",
        "solution_type": "tabular_entry",
    }


# ---------------------------------------------------------------------------
# Master Generator Function
# ---------------------------------------------------------------------------
def generate_grade10_gaap_questions(
    *,
    subskill: Optional[str] = None,
    difficulty: str = "medium",
    question_type: Optional[str] = None,
    count: int = 1,
    seed: Optional[int] = None,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master entry point for Grade 10 Accounting GAAP questions."""
    rng = random.Random(seed if seed is not None else 101)
    n = max(1, min(int(count), 20))
    ctx = _build_context(rng)

    subskill_builder_map = {
        "gaap_concepts_and_policy": _build_gaap_concepts_and_policy,
        "historical_cost_principle": _build_historical_cost_principle,
        "business_entity_rule": _build_business_entity_rule,
        "matching_principle": _build_matching_principle,
        "prudence_conservatism_principle": _build_prudence_conservatism_principle,
        "materiality_and_going_concern": _build_materiality_and_going_concern,
        "gaap_matching_table": _build_gaap_matching_table,
    }

    results = []
    for i in range(n):
        # Determine exact target subskill
        target_sub = subskill
        if not target_sub or target_sub in ("mixed", "all", "concepts", "gaap"):
            target_sub = SUBSKILLS[i % len(SUBSKILLS)]

        builder = subskill_builder_map.get(target_sub, _build_gaap_concepts_and_policy)
        q = builder(rng, ctx)
        results.append(q)

    return results


# Export standard generate function
generate = generate_grade10_gaap_questions
