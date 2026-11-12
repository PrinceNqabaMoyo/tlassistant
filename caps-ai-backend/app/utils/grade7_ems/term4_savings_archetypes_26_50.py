"""Grade 7 EMS — Savings: Archetypes 26 to 50.
100% Aligned with South African National Curriculum Standards (Term 4: Financial Literacy).
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 4/01. Savings.md.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from app.utils.ems_namelist import AREAS, NAMES, RURAL_AREAS, URBAN_AREAS

from .term4_savings_archetypes_01_25 import (
    BANKS_SA,
    _fmt_comma,
    _fmt_zar,
    _mcq,
    _svg_bar_chart,
    _table_q,
    _typed,
)


def arch_26_stokvel_definition_and_apartheid_history(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    members = rng.randint(10, 20)
    prompt = (
        f"In {area}, {members} neighbours form an indigenous South African rotating savings club where each person "
        f"contributes a fixed monthly sum and takes turns receiving the lump sum.\n\n"
        f"What is this savings association called, and what historical context shaped its rise in South Africa?"
    )
    correct = (
        "A stokvel — born in communities historically excluded from formal banking under apartheid as a trusted way to pool credit and savings"
    )
    distractors = [
        "A foreign stock exchange reserved solely for offshore bond traders",
        "A commercial mortgage bank owned by central European railways",
        "A compulsory national payroll tax deducted automatically by SARS",
    ]
    return _mcq(
        rng,
        subskill="26_stokvel_definition_and_apartheid_history",
        title="Stokvels: Meaning and South African History",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "Stokvels originated as mutual-aid community savings clubs among black South Africans denied fair access to "
            "formal banks under apartheid, evolving into multi-billion-Rand community finance networks today."
        ),
        hints={
            "tier_1": "Name the traditional South African rotating community savings club.",
            "tier_2": "Think of why historically excluded communities needed pooled self-help finance.",
            "tier_3": "Select 'A stokvel — born in communities historically excluded from formal banking under apartheid as a trusted way to pool credit and savings'.",
        },
        learning_objective_id="lo_sav_stokvel_history",
        concept_id="stokvel_definition_history",
        misconception_tags=["confuses_stokvel_with_stock_market"],
    )


def arch_27_stokvel_rotational_lump_sum_calculation(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    members = rng.choice([8, 10, 12, 15])
    monthly = rng.choice([300, 400, 500, 600])
    lump_sum = members * monthly
    prompt = (
        f"A stokvel in {area} has {members} members, and every member contributes {_fmt_zar(monthly)} each month into the "
        f"rotational pool.\n\n"
        f"How much money does ONE member receive as their rotational lump-sum payout when it is their turn?"
    )
    return _typed(
        rng,
        subskill="27_stokvel_rotational_lump_sum_calculation",
        title="Calculating a Stokvel Rotational Lump-Sum Payout",
        prompt=prompt,
        sample_answer=(
            f"Monthly lump-sum payout = {members} members x {_fmt_zar(monthly)} = {_fmt_zar(lump_sum)}.\n"
            f"Every member receives {_fmt_zar(lump_sum)} once during the {members}-month cycle."
        ),
        marking_points=[
            f"Multiply number of members ({members}) by monthly contribution ({_fmt_zar(monthly)}) [1]",
            f"Correct payout = {_fmt_zar(lump_sum)} [1]",
        ],
        hints={
            "tier_1": "Add every member's contribution for that single month together.",
            "tier_2": f"Multiply {members} members by {_fmt_zar(monthly)}.",
            "tier_3": f"{members} x {_fmt_zar(monthly)} = {_fmt_zar(lump_sum)}.",
        },
        learning_objective_id="lo_sav_stokvel_payout_calc",
        concept_id="stokvel_lump_sum",
        misconception_tags=["divides_instead_of_multiplies"],
        marks=2,
        correct_answer=_fmt_zar(lump_sum),
        correct_value=float(lump_sum),
        worked_solution=f"Lump sum = {members} x {monthly} = {_fmt_zar(lump_sum)}",
    )


def arch_28_stokvel_payout_schedule_table(rng: random.Random) -> Dict[str, Any]:
    members = rng.choice([10, 12])
    contrib = rng.choice([250, 350, 450])
    monthly_pool = members * contrib
    cum_2 = monthly_pool * 2
    cum_3 = monthly_pool * 3
    m1_name, m2_name, m3_name = rng.sample(NAMES, 3)

    headers = ["Cycle Month", "Monthly Member Pool (R)", "Recipient Payout (R)", "Cumulative Payouts to Date (R)", "Verified"]
    raw_rows = [
        [
            {"type": "given", "value": f"Month 1 ({m1_name})"},
            {"type": "given", "value": _fmt_zar(monthly_pool)},
            {"type": "required", "expected": _fmt_zar(monthly_pool)},
            {"type": "given", "value": _fmt_zar(monthly_pool)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": f"Month 2 ({m2_name})"},
            {"type": "given", "value": _fmt_zar(monthly_pool)},
            {"type": "given", "value": _fmt_zar(monthly_pool)},
            {"type": "required", "expected": _fmt_zar(cum_2)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": f"Month 3 ({m3_name})"},
            {"type": "required", "expected": _fmt_zar(monthly_pool)},
            {"type": "given", "value": _fmt_zar(monthly_pool)},
            {"type": "required", "expected": _fmt_zar(cum_3)},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": f"Month 1 recipient receives the full pool ({_fmt_zar(monthly_pool)}).",
        "r1_c3": f"Month 1 cumulative + Month 2 payout = {_fmt_zar(monthly_pool)} + {_fmt_zar(monthly_pool)}.",
        "r2_c1": f"All {members} members pay {_fmt_zar(contrib)} each month ({_fmt_zar(monthly_pool)}).",
        "r2_c3": f"Month 2 cumulative ({_fmt_zar(cum_2)}) + Month 3 payout ({_fmt_zar(monthly_pool)}).",
    }
    derivations = [
        f"Monthly pool = {members} members x {_fmt_zar(contrib)} = {_fmt_zar(monthly_pool)}",
        f"Month 2 cumulative = {_fmt_zar(monthly_pool)} x 2 = {_fmt_zar(cum_2)}",
        f"Month 3 cumulative = {_fmt_zar(monthly_pool)} x 3 = {_fmt_zar(cum_3)}",
    ]
    return _table_q(
        rng,
        subskill="28_stokvel_payout_schedule_table",
        title="Stokvel Rotational Payout Ledger",
        prompt=(
            f"Complete the first three months of a {members}-member rotational stokvel ledger where each member pays "
            f"{_fmt_zar(contrib)} per month. Leave the 'Verified' column empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Each month, the recipient receives 100% of the Monthly Member Pool.",
            "tier_2": "Cumulative Payouts add the current month's payout onto the previous cumulative total.",
            "tier_3": f"Monthly pool={_fmt_zar(monthly_pool)}; Cum Month 2={_fmt_zar(cum_2)}; Cum Month 3={_fmt_zar(cum_3)}.",
        },
        learning_objective_id="lo_sav_stokvel_ledger",
        concept_id="stokvel_schedule_table",
        misconception_tags=["forgets_cumulative_sum", "fills_must_be_empty_cell"],
    )


def arch_29_stokvel_bank_account_advantages(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    members = rng.randint(14, 24)
    prompt = (
        f"A {members}-member community stokvel in {area} decides to move away from passing envelopes of cash at "
        f"monthly meetings and instead opens a dedicated group Stokvel Bank Account (such as an FNB Stokvel account).\n\n"
        f"Explain TWO advantages of holding stokvel funds in a formal group bank account."
    )
    return _typed(
        rng,
        subskill="29_stokvel_bank_account_advantages",
        title="Why Modern Stokvels Use Group Bank Accounts",
        prompt=prompt,
        sample_answer=(
            "1. Dual-signature security: Multiple office-bearers must approve withdrawals, protecting against cash robbery at meetings or misuse by one individual.\n"
            "2. Interest earnings & transparent statements: Pooled funds earn higher group interest rates and generate written bank statements every member can audit."
        ),
        marking_points=[
            "Protection against cash theft and fraud through dual/multiple signatory rules [1]",
            "Pooled group funds earn interest and receive transparent monthly audit statements [1]",
        ],
        hints={
            "tier_1": "Think of physical cash safety AND what happens to pooled money sitting in a bank.",
            "tier_2": "Mention multi-signature governance/anti-theft protection + earning group interest & clear records.",
            "tier_3": "Give two points: safer multi-signature security against theft/fraud, and earning interest with transparent bank records.",
        },
        learning_objective_id="lo_sav_stokvel_bank_benefits",
        concept_id="stokvel_bank_accounts",
        misconception_tags=["thinks_banks_ban_stokvels"],
        marks=2,
    )


def arch_30_grocery_clubs_and_bulk_buying_savings(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    members = rng.randint(15, 30)
    monthly = rng.choice([250, 300, 400])
    prompt = (
        f"Every month, {members} families in {area} contribute {_fmt_zar(monthly)} to a year-end Grocery Club so they can "
        f"purchase rice, cooking oil, sugar, and soap together directly from wholesalers.\n\n"
        f"How does a stokvel Grocery Club reduce annual household food expenses?"
    )
    correct = (
        "Collective bulk buying secures wholesale volume discounts far below individual retail shelf prices while spreading costs evenly across 12 months"
    )
    distractors = [
        "Wholesalers double item prices whenever 20 families pool bulk orders",
        "Members throw away half the food in January to stay eligible for credit",
        "Grocery clubs replace supermarkets by printing their own government currency",
    ]
    return _mcq(
        rng,
        subskill="30_grocery_clubs_and_bulk_buying_savings",
        title="Grocery Clubs and Bulk Wholesale Discounts",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"By pooling {members} x {_fmt_zar(monthly)} monthly, the Grocery Club negotiates wholesale bulk discounts "
            f"and ensures families face December/January without expensive store debt."
        ),
        hints={
            "tier_1": "Compare buying 1 sack of maize flour at retail against buying 30 sacks at a wholesaler.",
            "tier_2": "Pooling monthly savings unlocks bulk wholesale prices and smooths year-end expenses.",
            "tier_3": "Select the option mentioning wholesale bulk discounts and spreading costs across 12 months.",
        },
        learning_objective_id="lo_sav_grocery_clubs",
        concept_id="grocery_clubs",
        misconception_tags=["ignores_bulk_wholesale_savings"],
    )


def arch_31_burial_and_funeral_societies_role(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    monthly = rng.choice([80, 100, 120])
    prompt = (
        f"Households across {area} pay {_fmt_zar(monthly)} each month into a community burial / funeral society.\n\n"
        f"What is the primary financial purpose of a burial society?"
    )
    correct = (
        "Pooling affordable regular contributions to cover sudden funeral expenses and bereavement support so families avoid ruinous debt"
    )
    distractors = [
        "Funding speculative foreign currency trading on international stock markets",
        "Eliminating all primary school fees for commercial banks",
        "Charging 80% weekly interest to grieving neighbours during funerals",
    ]
    return _mcq(
        rng,
        subskill="31_burial_and_funeral_societies_role",
        title="Role of Community Burial Societies",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Funerals carry large unexpected costs; paying {_fmt_zar(monthly)}/month into a burial society shares the "
            f"risk collectively and protects families from high-interest emergency debt."
        ),
        hints={
            "tier_1": "Think about sudden funeral expenses that can overwhelm one household alone.",
            "tier_2": "A burial society acts as collective community risk-pooling for dignified funerals.",
            "tier_3": "Select 'Pooling affordable regular contributions to cover sudden funeral expenses and bereavement support so families avoid ruinous debt'.",
        },
        learning_objective_id="lo_sav_burial_societies",
        concept_id="burial_societies",
        misconception_tags=["confuses_burial_society_with_loan_shark"],
    )


def arch_32_informal_vs_formal_savings_comparison_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Savings Method", "Safety Against Theft/Fire", "Interest Growth", "Community Solidarity", "Code"]
    raw_rows = [
        [
            {"type": "given", "value": "Cash in Home Tin"},
            {"type": "required", "expected": "Very low"},
            {"type": "given", "value": "Zero interest"},
            {"type": "given", "value": "Individual only"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Bank Savings Account"},
            {"type": "given", "value": "Very high"},
            {"type": "required", "expected": "Earns bank interest"},
            {"type": "given", "value": "Individual customer"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Banked Stokvel Club"},
            {"type": "given", "value": "High (dual sign-off)"},
            {"type": "given", "value": "Group interest earned"},
            {"type": "required", "expected": "Strong mutual support"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Exact phrase: 'Very low'.",
        "r1_c2": "Exact phrase: 'Earns bank interest'.",
        "r2_c3": "Exact phrase: 'Strong mutual support'.",
    }
    derivations = [
        "Cash hidden at home faces Very low security against burglary or fire.",
        "Formal bank accounts keep funds safe and Earns bank interest.",
        "Banked stokvels combine group safety with Strong mutual support.",
    ]
    return _table_q(
        rng,
        subskill="32_informal_vs_formal_savings_comparison_table",
        title="Informal Cash vs Formal Bank vs Stokvel Matrix",
        prompt=(
            f"Compare three saving options available to residents in {area} using these exact phrases: "
            f"'Very low', 'Earns bank interest', and 'Strong mutual support'. Leave 'Code' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Evaluate security for home cash, financial return for banks, and social value for stokvels.",
            "tier_2": "Use the three exact given phrases in the three blanks.",
            "tier_3": "r0_c1='Very low'; r1_c2='Earns bank interest'; r2_c3='Strong mutual support'.",
        },
        learning_objective_id="lo_sav_methods_matrix",
        concept_id="savings_methods_comparison",
        misconception_tags=["ranks_home_cash_as_high_security", "fills_must_be_empty_cell"],
    )


def arch_33_south_african_reserve_bank_sarb_role(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    prompt = (
        f"During a Grade 7 EMS lesson in {area}, learners examine a Rand banknote bearing the signature of the "
        f"Governor of the South African Reserve Bank (SARB).\n\n"
        f"What is the PRIMARY mandate and role of the South African Reserve Bank?"
    )
    correct = (
        "Acting as South Africa's central bank: issuing currency, protecting price/Rand stability, regulating commercial banks, and banking for government"
    )
    distractors = [
        "Opening retail chequing branches inside shopping malls to sell personal store credit cards",
        "Operating neighbourhood grocery stokvels for primary school classrooms",
        "Manufacturing clothing and exporting raw iron ore across the Atlantic",
    ]
    return _mcq(
        rng,
        subskill="33_south_african_reserve_bank_sarb_role",
        title="Role of the South African Reserve Bank (SARB)",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "SARB is South Africa's central bank — not a high-street retail bank for individuals — tasked with controlling "
            "inflation (price stability), issuing notes/coins, supervising commercial banks, and serving as government's banker."
        ),
        hints={
            "tier_1": "Distinguish the national CENTRAL bank from commercial retail banks like Absa or Capitec.",
            "tier_2": "Can an ordinary Grade 7 learner walk into SARB to open a R10 savings account? No!",
            "tier_3": "Select 'Acting as South Africa's central bank: issuing currency, protecting price/Rand stability, regulating commercial banks, and banking for government'.",
        },
        learning_objective_id="lo_sav_sarb_role",
        concept_id="south_african_reserve_bank",
        misconception_tags=["thinks_sarb_takes_personal_deposits"],
    )


def arch_34_financial_institutions_matching_matrix(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Financial Institution", "SA Example", "Primary Function", "Tag"]
    raw_rows = [
        [
            {"type": "given", "value": "Central Bank"},
            {"type": "given", "value": "South African Reserve Bank"},
            {"type": "required", "expected": "Issues currency and guards price stability"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Private Commercial Bank"},
            {"type": "given", "value": "Absa / FNB / Capitec"},
            {"type": "required", "expected": "Takes public deposits and grants loans"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Life Insurer & Pension Fund"},
            {"type": "given", "value": "Old Mutual / Liberty"},
            {"type": "required", "expected": "Long-term cover and retirement savings"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c2": "Exact phrase: 'Issues currency and guards price stability'.",
        "r1_c2": "Exact phrase: 'Takes public deposits and grants loans'.",
        "r2_c2": "Exact phrase: 'Long-term cover and retirement savings'.",
    }
    derivations = [
        "SARB -> Issues currency and guards price stability.",
        "Commercial Banks -> Takes public deposits and grants loans.",
        "Old Mutual / Liberty -> Long-term cover and retirement savings.",
    ]
    return _table_q(
        rng,
        subskill="34_financial_institutions_matching_matrix",
        title="South African Financial Institutions Matrix",
        prompt=(
            f"Classify three categories of South African financial institutions for a research assignment in {area}. "
            f"Use exact functions: 'Issues currency and guards price stability', 'Takes public deposits and grants loans', "
            f"and 'Long-term cover and retirement savings'. Leave 'Tag' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Separate the Central Bank (SARB) from retail deposit-takers and life insurers/pension providers.",
            "tier_2": "Match Old Mutual / Liberty to life cover & retirement, and SARB to currency & price stability.",
            "tier_3": "Fill the Primary Function column using the three exact provided strings.",
        },
        learning_objective_id="lo_sav_financial_institutions_table",
        concept_id="financial_institutions_matrix",
        misconception_tags=["confuses_sarb_with_old_mutual", "fills_must_be_empty_cell"],
    )


def arch_35_life_insurance_pension_and_provident_funds(rng: random.Random) -> Dict[str, Any]:
    insurer = rng.choice(["Old Mutual", "Liberty", "Sanlam"])
    monthly_contrib = rng.choice([450, 650, 850])
    prompt = (
        f"A salaried mechanic contributes {_fmt_zar(monthly_contrib)} monthly to {insurer} toward both life insurance "
        f"cover and a workplace pension/provident fund.\n\n"
        f"Distinguish the purpose of LIFE INSURANCE from the purpose of a PENSION / PROVIDENT FUND."
    )
    return _typed(
        rng,
        subskill="35_life_insurance_pension_and_provident_funds",
        title="Life Insurance vs Pension / Provident Funds",
        prompt=prompt,
        sample_answer=(
            f"1. Life insurance (via insurers like {insurer}): Pays a guaranteed lump sum to surviving dependants if the policyholder dies or becomes permanently disabled, shielding family income.\n"
            "2. Pension / provident fund: Long-term retirement savings invested over a worker's career to pay a monthly pension or lump sum once the worker retires."
        ),
        marking_points=[
            "Life insurance protects dependants financially in case of death or severe disability [1]",
            "Pension/provident funds accumulate savings over working years to provide retirement income [1]",
        ],
        hints={
            "tier_1": "Ask WHICH event triggers a payout: premature death/disability vs reaching retirement age.",
            "tier_2": "Life cover protects dependants on loss of life; pensions replace salary in retirement.",
            "tier_3": "Clearly contrast life insurance (death/disability protection for dependants) and pension/provident funds (retirement income).",
        },
        learning_objective_id="lo_sav_insurance_vs_pension",
        concept_id="life_insurance_and_pensions",
        misconception_tags=["treats_life_insurance_as_short_term_spending_account"],
        marks=2,
    )


def arch_36_startup_capital_definition_for_small_business(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    biz = rng.choice(["car-wash kiosk", "fresh-juice stall", "school uniform sewing studio"])
    prompt = (
        f"{name} wants to open a {biz} in {area} and calculates how much cash is needed before Day 1 to buy tools, "
        f"opening stock, trading permits, and pay the first month's rent.\n\n"
        f"What is this initial pool of money called in EMS?"
    )
    correct = "Start-up capital"
    distractors = [
        "Income tax refund",
        "Household grocery deficit",
        "Consumer store debt",
    ]
    return _mcq(
        rng,
        subskill="36_startup_capital_definition_for_small_business",
        title="Meaning of Start-Up Capital",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Start-up capital is the initial funding needed to purchase equipment, stock, licences, and pay opening "
            f"expenses until the {biz} earns sufficient sales cash."
        ),
        hints={
            "tier_1": "Identify the financial capital required specifically to LAUNCH a new enterprise.",
            "tier_2": "Equipment + initial stock + opening rent + permits = start-up capital.",
            "tier_3": "Select 'Start-up capital'.",
        },
        learning_objective_id="lo_sav_startup_capital_def",
        concept_id="startup_capital_definition",
        misconception_tags=["confuses_startup_capital_with_net_profit"],
    )


def arch_37_startup_capital_requirement_calculation(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    equip = rng.choice([8500, 10500, 12000])
    stock = rng.choice([3500, 4200, 5000])
    rent_dep = rng.choice([2500, 3000, 4000])
    own_savings = rng.choice([6000, 7500, 9000])
    total_needed = equip + stock + rent_dep
    shortfall = total_needed - own_savings
    prompt = (
        f"{name} estimates the start-up requirements for a baking stall: ovens/mixers {_fmt_zar(equip)}, opening flour "
        f"and sugar stock {_fmt_zar(stock)}, and kiosk rent deposit {_fmt_zar(rent_dep)}. {name} already saved {_fmt_zar(own_savings)}.\n\n"
        f"Calculate the remaining funding gap {name} still needs to raise."
    )
    return _typed(
        rng,
        subskill="37_startup_capital_requirement_calculation",
        title="Calculating Start-Up Capital Shortfall",
        prompt=prompt,
        sample_answer=(
            f"Total start-up capital required = {_fmt_zar(equip)} + {_fmt_zar(stock)} + {_fmt_zar(rent_dep)} = {_fmt_zar(total_needed)}\n"
            f"Remaining shortfall = {_fmt_zar(total_needed)} - {_fmt_zar(own_savings)} = {_fmt_zar(shortfall)}"
        ),
        marking_points=[
            f"Sum all start-up costs: {_fmt_zar(total_needed)} [1]",
            f"Subtract own savings ({_fmt_zar(own_savings)}) = {_fmt_zar(shortfall)} shortfall [2]",
        ],
        hints={
            "tier_1": "First add equipment, initial stock, and rent deposit to get total start-up capital needed.",
            "tier_2": f"Subtract {name}'s own savings ({_fmt_zar(own_savings)}) from that total.",
            "tier_3": f"Total={_fmt_zar(total_needed)}; Shortfall={_fmt_zar(total_needed)} - {_fmt_zar(own_savings)} = {_fmt_zar(shortfall)}.",
        },
        learning_objective_id="lo_sav_startup_capital_calc",
        concept_id="startup_capital_calculation",
        misconception_tags=["forgets_to_subtract_own_savings"],
        marks=3,
        correct_answer=_fmt_zar(shortfall),
        correct_value=float(shortfall),
        worked_solution=f"Total = {total_needed}; Shortfall = {total_needed} - {own_savings} = {_fmt_zar(shortfall)}",
    )


def arch_38_loan_capital_borrowed_with_interest(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    loan_amt = rng.choice([20000, 35000, 50000])
    prompt = (
        f"An entrepreneur borrows {_fmt_zar(loan_amt)} as a business loan from {bank} to purchase welding gear.\n\n"
        f"Which condition ALWAYS applies to LOAN (debt) capital?"
    )
    correct = (
        "The principal plus agreed interest must be repaid on schedule whether the business makes a profit or a loss"
    )
    distractors = [
        "Repayment is permanently cancelled if monthly sales drop during winter",
        "The bank automatically takes 50% active daily management control forever with zero debt owed",
        "Loans require zero repayment as long as the money buys tools instead of food",
    ]
    return _mcq(
        rng,
        subskill="38_loan_capital_borrowed_with_interest",
        title="Nature of Loan Capital (Borrowed Funds)",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Borrowing {_fmt_zar(loan_amt)} creates a legal debt obligation: interest and principal must be repaid to "
            f"{bank} regardless of monthly business profit."
        ),
        hints={
            "tier_1": "What happens to a bank loan contract even if the business has a slow sales month?",
            "tier_2": "A lender does not share business losses—repayments plus interest remain due.",
            "tier_3": "Select 'The principal plus agreed interest must be repaid on schedule whether the business makes a profit or a loss'.",
        },
        learning_objective_id="lo_sav_loan_capital",
        concept_id="loan_capital",
        misconception_tags=["believes_loan_repayment_depends_on_profit"],
    )


def arch_39_partner_equity_capital_shared_ownership(rng: random.Random) -> Dict[str, Any]:
    n1, n2 = rng.sample(NAMES, 2)
    invest = rng.choice([15000, 22000, 30000])
    prompt = (
        f"Instead of taking a bank loan, {n1} invites {n2} to invest {_fmt_zar(invest)} into a graphic-printing shop as "
        f"a co-owner.\n\n"
        f"How does bringing in PARTNER EQUITY capital differ from taking a bank loan?"
    )
    correct = (
        "There is no mandatory debt interest repayment, because the partner becomes a co-owner who shares future profits, losses, and decisions"
    )
    distractors = [
        "The founder keeps 100% ownership and never shares any profits or decisions with the partner",
        "The partner charges 25% compound monthly penalty interest whether profits exist or not",
        "Equity partners are strictly illegal for small South African businesses",
    ]
    return _mcq(
        rng,
        subskill="39_partner_equity_capital_shared_ownership",
        title="Partner Equity Capital and Shared Ownership",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"Partner equity exchanges shared business ownership, decision-making, and profit-sharing with {n2} for cash "
            f"and skills, avoiding fixed monthly debt interest."
        ),
        hints={
            "tier_1": "Does an equity partner charge fixed monthly loan interest, or earn a share of profits?",
            "tier_2": "Equity capital trades part of ownership/profits in return for permanent risk-sharing investment.",
            "tier_3": "Select the option noting zero fixed debt interest and shared ownership, profits, losses, and decisions.",
        },
        learning_objective_id="lo_sav_partner_equity",
        concept_id="partner_equity_capital",
        misconception_tags=["thinks_equity_partner_gets_zero_ownership"],
    )


def arch_40_loan_vs_equity_capital_comparison_table(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    headers = ["Financing Characteristic", "Loan Capital (Debt)", "Partner Equity Capital", "Check"]
    raw_rows = [
        [
            {"type": "given", "value": "Repayment Obligation"},
            {"type": "required", "expected": "Must repay with interest"},
            {"type": "given", "value": "No fixed debt repayment"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Business Ownership"},
            {"type": "given", "value": "Founder retains 100%"},
            {"type": "required", "expected": "Shared with partner"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "If Business Makes a Loss"},
            {"type": "required", "expected": "Loan still payable"},
            {"type": "given", "value": "Loss shared by owners"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r0_c1": "Exact phrase: 'Must repay with interest'.",
        "r1_c2": "Exact phrase: 'Shared with partner'.",
        "r2_c1": "Exact phrase: 'Loan still payable'.",
    }
    derivations = [
        "Loan capital -> Must repay with interest.",
        "Partner equity -> Ownership is Shared with partner.",
        "In a loss-making month -> Loan still payable.",
    ]
    return _table_q(
        rng,
        subskill="40_loan_vs_equity_capital_comparison_table",
        title="Loan Capital vs Partner Equity Table",
        prompt=(
            f"An entrepreneur in {area} compares borrowing from a bank against bringing in an equity partner. Complete the "
            f"blanks using exact phrases: 'Must repay with interest', 'Shared with partner', and 'Loan still payable'. "
            f"Leave 'Check' empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Remember who owns the business and who bears losses under debt vs equity.",
            "tier_2": "Banks demand fixed repayment even during losses; partners share ownership and profits/losses.",
            "tier_3": "r0_c1='Must repay with interest'; r1_c2='Shared with partner'; r2_c1='Loan still payable'.",
        },
        learning_objective_id="lo_sav_loan_vs_equity_table",
        concept_id="loan_vs_equity_table",
        misconception_tags=["swaps_ownership_and_repayment_cells", "fills_must_be_empty_cell"],
    )


def arch_41_small_business_support_seda_and_dti(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    biz = rng.choice(["spaza bakery", "solar repair workshop", "leathercraft co-op"])
    prompt = (
        f"Starting a {biz} in {area}, an entrepreneur seeks government-backed guidance on business registration, "
        f"financial planning, and mentoring.\n\n"
        f"Which pair of national South African institutions leads small-enterprise advice and policy support?"
    )
    correct = "The Department of Trade and Industry (the dti) and SEDA (Small Enterprise Development Agency)"
    distractors = [
        "The South African Weather Service and municipal traffic departments",
        "Foreign diamond exchanges and private luxury resorts",
        "Primary school tuckshops acting as central monetary regulators",
    ]
    return _mcq(
        rng,
        subskill="41_small_business_support_seda_and_dti",
        title="SA SMME Support: the dti and SEDA",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            "South Africa's Department of Trade and Industry (the dti) and SEDA (Small Enterprise Development Agency) "
            "deliver non-financial mentoring, training, and registration support to emerging small businesses."
        ),
        hints={
            "tier_1": "Identify South Africa's Trade & Industry department and Small Enterprise Development Agency.",
            "tier_2": "Match the acronym SEDA to Small Enterprise Development Agency.",
            "tier_3": "Select 'The Department of Trade and Industry (the dti) and SEDA (Small Enterprise Development Agency)'.",
        },
        learning_objective_id="lo_sav_seda_dti",
        concept_id="smme_support_seda_dti",
        misconception_tags=["confuses_seda_with_commercial_lenders"],
    )


def arch_42_small_business_support_idc_nyda_khula_bee(rng: random.Random) -> Dict[str, Any]:
    area = rng.choice(AREAS)
    age = rng.randint(20, 26)
    prompt = (
        f"A {age}-year-old aspiring manufacturer in {area} investigates funding and mentorship beyond `the dti` and SEDA.\n\n"
        f"Name THREE additional South African support bodies or private-sector initiatives (such as youth agencies, "
        f"development finance corporations, NGOs, or bank enterprise desks) that assist small businesses and explain what ONE of them provides."
    )
    return _typed(
        rng,
        subskill="42_small_business_support_idc_nyda_khula_bee",
        title="South African SMME Finance & Mentorship Network",
        prompt=prompt,
        sample_answer=(
            "Three support bodies/programmes: (1) NYDA / Umsobomvu Youth Fund (NYDA), (2) IDC (Industrial Development Corporation), "
            "(3) Khula Enterprise Finance (SEFA) — plus BEE equity funds, NGOs, and Absa/Nedbank/Shell LiveWIRE enterprise desks.\n"
            f"Example role: NYDA equips young entrepreneurs (aged {age}) with entrepreneurship training, mentorship, and small start-up grants/vouchers."
        ),
        marking_points=[
            "Names three valid South African SMME support institutions/programmes (e.g. NYDA/UYF, IDC, Khula/SEFA, BEE, NGOs, Absa/Nedbank/Shell) [3]",
            "Accurately explains the role of at least one named organisation (grants, loan guarantees, industrial finance, or mentoring) [1]",
        ],
        hints={
            "tier_1": "Recall youth funds (UYF/NYDA), industrial lenders (IDC), loan-guarantee agencies (Khula), and corporate desks (Absa/Nedbank/Shell).",
            "tier_2": "List three distinct organisations and describe what one of them actually gives a founder.",
            "tier_3": "Include NYDA/UYF, IDC, and Khula/SEFA (or Absa/Nedbank/Shell) with a concrete explanation of training, grants, or finance.",
        },
        learning_objective_id="lo_sav_idc_nyda_khula",
        concept_id="smme_support_network",
        misconception_tags=["confuses_support_bodies_with_credit_cards"],
        marks=4,
    )


def arch_43_selecting_financing_source_scenario(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    cost = rng.choice([12000, 16000, 20000])
    prompt = (
        f"{name} wants {_fmt_zar(cost)} to launch a mobile cellphone-repair stall in {area}, but has zero collateral "
        f"and expects slow sales during the first four months.\n\n"
        f"Should {name} accept an expensive short-term informal loan charging 30% monthly interest, OR combine personal "
        f"savings with a trusted partner/NYDA-SEDA support? Give TWO financial reasons."
    )
    return _typed(
        rng,
        subskill="43_selecting_financing_source_scenario",
        title="Choosing Wise Start-Up Financing",
        prompt=prompt,
        sample_answer=(
            f"{name} should use personal savings plus NYDA/SEDA support or a partner rather than the 30% monthly loan.\n"
            "1. Fixed 30% monthly interest on slow early sales would quickly bankrupt the stall before revenue stabilises.\n"
            "2. Personal savings, NYDA grants/training, or an equity partner avoid crushing monthly interest debt and supply valuable mentoring."
        ),
        marking_points=[
            "Recommends personal savings + NYDA/SEDA/partner instead of high-interest debt [1]",
            "Reason 1: Avoids punitive 30% monthly interest during slow initial months [1]",
            "Reason 2: Gains zero-debt equity/grants plus SEDA/NYDA mentoring support [1]",
        ],
        hints={
            "tier_1": "Calculate what 30% monthly interest would do while early sales are still low.",
            "tier_2": "Weigh crippling fixed debt repayments against debt-free savings, mentorship, and shared partner risk.",
            "tier_3": "Recommend savings + NYDA/SEDA/partner, citing interest-free survival in slow early months and mentorship.",
        },
        learning_objective_id="lo_sav_financing_choice",
        concept_id="selecting_startup_finance",
        misconception_tags=["chooses_high_interest_debt_despite_slow_sales"],
        marks=3,
    )


def arch_44_bank_loan_simple_interest_repayment_calculation(rng: random.Random) -> Dict[str, Any]:
    bank = rng.choice(BANKS_SA)
    principal = rng.choice([10000, 15000, 20000, 25000])
    rate = rng.choice([10, 12, 15])
    interest = int(round(principal * rate / 100.0))
    total_repay = principal + interest
    prompt = (
        f"A small craft business borrows {_fmt_zar(principal)} from {bank} for exactly 1 year at a simple interest rate "
        f"of {rate}% per annum.\n\n"
        f"Calculate the TOTAL amount (Principal + Interest) the business must repay to {bank} at the end of the year."
    )
    return _typed(
        rng,
        subskill="44_bank_loan_simple_interest_repayment_calculation",
        title="Simple Annual Interest & Total Loan Repayment",
        prompt=prompt,
        sample_answer=(
            f"1-year interest = {rate}% of {_fmt_zar(principal)} = {_fmt_zar(interest)}\n"
            f"Total repayment = {_fmt_zar(principal)} + {_fmt_zar(interest)} = {_fmt_zar(total_repay)}"
        ),
        marking_points=[
            f"Compute interest: ({rate} / 100) x {_fmt_zar(principal)} = {_fmt_zar(interest)} [1]",
            f"Add principal + interest = {_fmt_zar(total_repay)} [2]",
        ],
        hints={
            "tier_1": f"First find {rate}% of {_fmt_zar(principal)} for 1 year.",
            "tier_2": f"Next add that interest ({_fmt_zar(interest)}) back onto the original {_fmt_zar(principal)} loan.",
            "tier_3": f"Interest={_fmt_zar(interest)}; Total repayment={_fmt_zar(principal)} + {_fmt_zar(interest)} = {_fmt_zar(total_repay)}.",
        },
        learning_objective_id="lo_sav_simple_interest_calc",
        concept_id="simple_interest_loan_repayment",
        misconception_tags=["submits_interest_only_instead_of_total_repayment"],
        marks=3,
        correct_answer=_fmt_zar(total_repay),
        correct_value=float(total_repay),
        worked_solution=f"Interest = {interest}; Total = {principal} + {interest} = {_fmt_zar(total_repay)}",
    )


def arch_45_deficit_net_profit_inventory_liquidity_definitions(rng: random.Random) -> Dict[str, Any]:
    cases = [
        ("Expenses exceed Income in a given period, leaving a financial shortfall", "Deficit"),
        ("Goods and stock held by a business ready to be sold to customers", "Inventory"),
        ("How quickly and easily an asset can be converted into spendable cash without losing value", "Liquidity"),
        ("Total income earned minus all operating expenses over a financial period (when income > expenses)", "Net profit"),
    ]
    desc, correct = rng.choice(cases)
    all_terms = ["Deficit", "Inventory", "Liquidity", "Net profit"]
    distractors = [t for t in all_terms if t != correct]
    prompt = (
        f"In Grade 7 financial literacy terminology, which concept is defined as:\n\n"
        f"\"{desc}\"?"
    )
    return _mcq(
        rng,
        subskill="45_deficit_net_profit_inventory_liquidity_definitions",
        title="Financial Literacy Terms: Deficit, Net Profit, Inventory & Liquidity",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"'{correct}' matches: {desc}. Remember all four key terms: Deficit (Expenses > Income), "
            f"Net profit (Income > Expenses), Inventory (trading stock), and Liquidity (ease of conversion to cash)."
        ),
        hints={
            "tier_1": "Distinguish Deficit (loss/shortfall), Net profit (surplus), Inventory (goods held for sale), and Liquidity (cash speed).",
            "tier_2": "Re-read the definition carefully to match the exact financial term.",
            "tier_3": f"Select '{correct}'.",
        },
        learning_objective_id="lo_sav_exam_glossary_terms",
        concept_id="financial_literacy_glossary",
        misconception_tags=["confuses_liquidity_with_inventory_or_deficit"],
    )


def arch_46_statement_of_net_worth_assets_vs_liabilities_concept(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    assets = rng.choice([45000, 58000, 72000])
    liab = rng.choice([12000, 18000, 22000])
    prompt = (
        f"{name} prepares a personal Statement of Net Worth showing Total Assets of {_fmt_zar(assets)} (bank savings, "
        f"laptop, bicycle) and Total Liabilities of {_fmt_zar(liab)} (store-card balance and family loan).\n\n"
        f"Which equation calculates {name}'s NET WORTH?"
    )
    correct = "Net Worth = Total Assets minus Total Liabilities"
    distractors = [
        "Net Worth = Total Assets plus Total Liabilities",
        "Net Worth = Monthly Expenses minus Bank Savings",
        "Net Worth = Total Liabilities divided by Interest Rate",
    ]
    return _mcq(
        rng,
        subskill="46_statement_of_net_worth_assets_vs_liabilities_concept",
        title="Understanding the Statement of Net Worth",
        prompt=prompt,
        correct=correct,
        distractors=distractors,
        explanation=(
            f"A Statement of Net Worth measures true financial wealth at a moment in time: Total Assets ({_fmt_zar(assets)}) "
            f"minus Total Liabilities ({_fmt_zar(liab)}) = {_fmt_zar(assets - liab)}."
        ),
        hints={
            "tier_1": "Assets are what you OWN; Liabilities are what you OWE.",
            "tier_2": "To find what remains truly yours debt-free, subtract debts (liabilities) from assets.",
            "tier_3": "Select 'Net Worth = Total Assets minus Total Liabilities'.",
        },
        learning_objective_id="lo_sav_net_worth_concept",
        concept_id="statement_of_net_worth_formula",
        misconception_tags=["adds_liabilities_to_assets"],
    )


def arch_47_statement_of_net_worth_ledger_table(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    savings_bal = rng.choice([6500, 8200, 9500])
    bicycle_val = rng.choice([3200, 3800, 4500])
    laptop_val = rng.choice([5500, 6500, 7500])
    tot_assets = savings_bal + bicycle_val + laptop_val

    store_debt = rng.choice([1800, 2400, 3000])
    study_loan = rng.choice([2500, 3200, 4000])
    tot_liab = store_debt + study_loan
    net_worth = tot_assets - tot_liab

    headers = ["Statement of Net Worth Item", "Assets (R)", "Liabilities (R)", "Audit"]
    raw_rows = [
        [
            {"type": "given", "value": "Bank Savings Account"},
            {"type": "given", "value": _fmt_zar(savings_bal)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Bicycle & Laptop Computer"},
            {"type": "given", "value": _fmt_zar(bicycle_val + laptop_val)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Total Assets"},
            {"type": "required", "expected": _fmt_zar(tot_assets)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Store Credit & Study Loan Owed"},
            {"type": "must_be_empty"},
            {"type": "given", "value": _fmt_zar(tot_liab)},
            {"type": "must_be_empty"},
        ],
        [
            {"type": "given", "value": "Personal Net Worth"},
            {"type": "required", "expected": _fmt_zar(net_worth)},
            {"type": "must_be_empty"},
            {"type": "must_be_empty"},
        ],
    ]
    cell_hints = {
        "r2_c1": f"Add {_fmt_zar(savings_bal)} + {_fmt_zar(bicycle_val + laptop_val)}.",
        "r4_c1": f"Subtract Total Liabilities ({_fmt_zar(tot_liab)}) from Total Assets ({_fmt_zar(tot_assets)}).",
    }
    derivations = [
        f"Total Assets = {_fmt_zar(savings_bal)} + {_fmt_zar(bicycle_val + laptop_val)} = {_fmt_zar(tot_assets)}",
        f"Total Liabilities = {_fmt_zar(store_debt)} (store debt) + {_fmt_zar(study_loan)} (loan) = {_fmt_zar(tot_liab)}",
        f"Personal Net Worth = {_fmt_zar(tot_assets)} - {_fmt_zar(tot_liab)} = {_fmt_zar(net_worth)}",
    ]
    return _table_q(
        rng,
        subskill="47_statement_of_net_worth_ledger_table",
        title="Statement of Net Worth 2D Ledger",
        prompt=(
            f"Prepare {name}'s Statement of Net Worth: Bank savings {_fmt_zar(savings_bal)}, Bicycle & Laptop "
            f"{_fmt_zar(bicycle_val + laptop_val)}, and Debts (store card {_fmt_zar(store_debt)} + study loan "
            f"{_fmt_zar(study_loan)} = {_fmt_zar(tot_liab)}). Complete Total Assets and Personal Net Worth. Leave shaded columns empty."
        ),
        headers=headers,
        raw_rows=raw_rows,
        cell_hints=cell_hints,
        derivations=derivations,
        hints={
            "tier_1": "Sum all assets in the Assets column first.",
            "tier_2": "Next compute Personal Net Worth = Total Assets - Total Liabilities.",
            "tier_3": f"Total Assets={_fmt_zar(tot_assets)}; Personal Net Worth={_fmt_zar(net_worth)}.",
        },
        learning_objective_id="lo_sav_net_worth_ledger",
        concept_id="statement_of_net_worth_table",
        misconception_tags=["adds_liabilities_to_assets", "fills_must_be_empty_cell"],
    )


def arch_48_net_worth_comparison_bar_graph(rng: random.Random) -> Dict[str, Any]:
    h1_assets = rng.choice([42000, 48000, 54000])
    h1_liab = rng.choice([8000, 10000, 12000])
    h1_nw = h1_assets - h1_liab

    h2_assets = rng.choice([40000, 44000, 48000])
    h2_liab = rng.choice([24000, 26000, 28000])
    h2_nw = h2_assets - h2_liab
    diff = h1_nw - h2_nw

    svg = _svg_bar_chart(
        title="Household Financial Comparison: Assets vs Liabilities (R)",
        y_label="Amount (R)",
        bars=[
            ("A Assets", float(h1_assets), "#15803D"),
            ("A Debts", float(h1_liab), "#F59E0B"),
            ("B Assets", float(h2_assets), "#1D4ED8"),
            ("B Debts", float(h2_liab), "#DC2626"),
        ],
        max_val=float(h1_assets + 8000),
        unit_suffix="",
    )
    prompt = (
        f"Refer to the bar graph below comparing Household A (Assets {_fmt_zar(h1_assets)}, Debts {_fmt_zar(h1_liab)}) "
        f"with Household B (Assets {_fmt_zar(h2_assets)}, Debts {_fmt_zar(h2_liab)}).\n\n"
        f"Calculate how much HIGHER Household A's Net Worth is than Household B's Net Worth."
    )
    return _typed(
        rng,
        subskill="48_net_worth_comparison_bar_graph",
        title="Comparing Household Net Worth (Bar Graph)",
        prompt=prompt,
        sample_answer=(
            f"Household A Net Worth = {_fmt_zar(h1_assets)} - {_fmt_zar(h1_liab)} = {_fmt_zar(h1_nw)}\n"
            f"Household B Net Worth = {_fmt_zar(h2_assets)} - {_fmt_zar(h2_liab)} = {_fmt_zar(h2_nw)}\n"
            f"Difference = {_fmt_zar(h1_nw)} - {_fmt_zar(h2_nw)} = {_fmt_zar(diff)}"
        ),
        marking_points=[
            f"Calculate Household A Net Worth = {_fmt_zar(h1_nw)} [1]",
            f"Calculate Household B Net Worth = {_fmt_zar(h2_nw)} [1]",
            f"Calculate Net Worth advantage = {_fmt_zar(diff)} [1]",
        ],
        hints={
            "tier_1": "Find Net Worth = Assets - Debts for Household A and Household B separately.",
            "tier_2": "Then subtract Household B's Net Worth from Household A's Net Worth.",
            "tier_3": f"A NW={_fmt_zar(h1_nw)}; B NW={_fmt_zar(h2_nw)}; Difference={_fmt_zar(diff)}.",
        },
        learning_objective_id="lo_sav_net_worth_graph",
        concept_id="net_worth_comparison_graph",
        misconception_tags=["compares_gross_assets_ignoring_debts"],
        marks=3,
        correct_answer=_fmt_zar(diff),
        correct_value=float(diff),
        diagram_spec={"kind": "inline_svg", "title": "Household Assets vs Liabilities", "svg": svg, "diagram_role": "context"},
        worked_solution=f"A NW={h1_nw}; B NW={h2_nw}; Advantage = {_fmt_zar(diff)}",
    )


def arch_49_compound_saving_habit_household_resilience(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    monthly = rng.choice([350, 450, 600])
    prompt = (
        f"In {area}, {name} commits to saving {_fmt_zar(monthly)} monthly in a bank savings account while also belonging "
        f"to a banked community grocery stokvel instead of buying furniture on store credit.\n\n"
        f"Explain TWO long-term ways this combined saving habit strengthens household net worth and financial resilience."
    )
    return _typed(
        rng,
        subskill="49_compound_saving_habit_household_resilience",
        title="Consistent Saving Habits and Financial Resilience",
        prompt=prompt,
        sample_answer=(
            f"1. Compound asset growth without interest leakages: Saving {_fmt_zar(monthly)}/month earns bank interest while "
            "avoiding high-interest store debt, steadily growing Net Worth.\n"
            "2. Dual shock protection: Formal liquid bank savings cover sudden medical/repair emergencies, while bulk stokvel discounts reduce year-end food expenses."
        ),
        marking_points=[
            "Positive interest earnings plus avoiding store-card interest directly expand household Assets and Net Worth [1]",
            "Combining liquid bank reserves with bulk grocery stokvel savings absorbs emergencies and seasonal spikes without debt [1]",
        ],
        hints={
            "tier_1": "Think about both Assets/interest vs store debt AND surviving sudden emergencies or December food spikes.",
            "tier_2": "Tie bank interest + avoided store credit + wholesale stokvel resilience directly to Net Worth.",
            "tier_3": "State asset growth without debt leakage AND resilient emergency/year-end cash protection.",
        },
        learning_objective_id="lo_sav_resilience_habit",
        concept_id="household_saving_resilience",
        misconception_tags=["treats_saving_as_sacrificing_future_security"],
        marks=2,
    )


def arch_50_integrated_savings_banking_entrepreneurship_synthesis(rng: random.Random) -> Dict[str, Any]:
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    bank = rng.choice(BANKS_SA)
    goal_zar = rng.choice([24000, 30000, 36000])
    prompt = (
        f"{name}, a young resident in {area}, dreams of building {_fmt_zar(goal_zar)} to open a neighbourhood tailoring "
        f"workshop while helping neighbours escape loan-shark debt.\n\n"
        f"Synthesise FOUR concepts from this topic explaining: (1) how personal savings (`Income - Expenses`) start the fund, "
        f"(2) how {bank} supports safety, EFTs, and capital investment, (3) how a banked community stokvel helps neighbours "
        f"pool resources, and (4) why pairing own savings with SEDA/NYDA advice or partner equity beats reckless borrowing."
    )
    return _typed(
        rng,
        subskill="50_integrated_savings_banking_entrepreneurship_synthesis",
        title="Integrated Savings, Banking & Start-Up Capital Synthesis",
        prompt=prompt,
        sample_answer=(
            f"1. Personal Savings: By spending less than income each month, {name} builds debt-free seed capital toward {_fmt_zar(goal_zar)}.\n"
            f"2. Commercial Banking ({bank}): Guards deposits safely, pays interest, executes EFT supplier payments, and acts as an intermediary channelling pooled savings into GDP-growing businesses.\n"
            "3. Banked Stokvel: Neighbours pool monthly contributions into a dual-signatory group account or grocery club, protecting members from predatory lenders.\n"
            "4. Wise Start-Up Finance: Combining savings with SEDA/NYDA mentoring or equity partners avoids fixed loan-interest ruin during early launch months."
        ),
        marking_points=[
            "Shows personal savings (Income - Expenses) as foundational debt-free seed capital [1]",
            f"Explains {bank}'s roles (safekeeping, interest, EFTs, financial intermediation) [1]",
            "Explains banked stokvel mutual solidarity and theft/debt protection [1]",
            "Evaluates why savings + SEDA/NYDA/equity partner beats high-interest launch debt [1]",
        ],
        hints={
            "tier_1": "Cover each of the four numbered pillars systematically.",
            "tier_2": "Connect personal surplus -> bank intermediation -> banked community stokvel -> wise start-up funding.",
            "tier_3": "Include Income-Expenses savings, bank safety/intermediation/EFTs, banked stokvel solidarity, and SEDA/NYDA/equity vs reckless debt.",
        },
        learning_objective_id="lo_sav_integrated_synthesis",
        concept_id="integrated_savings_synthesis",
        misconception_tags=["omits_one_of_four_pillars"],
        marks=4,
    )


BUILDERS_26_50 = {
    "26_stokvel_definition_and_apartheid_history": arch_26_stokvel_definition_and_apartheid_history,
    "27_stokvel_rotational_lump_sum_calculation": arch_27_stokvel_rotational_lump_sum_calculation,
    "28_stokvel_payout_schedule_table": arch_28_stokvel_payout_schedule_table,
    "29_stokvel_bank_account_advantages": arch_29_stokvel_bank_account_advantages,
    "30_grocery_clubs_and_bulk_buying_savings": arch_30_grocery_clubs_and_bulk_buying_savings,
    "31_burial_and_funeral_societies_role": arch_31_burial_and_funeral_societies_role,
    "32_informal_vs_formal_savings_comparison_table": arch_32_informal_vs_formal_savings_comparison_table,
    "33_south_african_reserve_bank_sarb_role": arch_33_south_african_reserve_bank_sarb_role,
    "34_financial_institutions_matching_matrix": arch_34_financial_institutions_matching_matrix,
    "35_life_insurance_pension_and_provident_funds": arch_35_life_insurance_pension_and_provident_funds,
    "36_startup_capital_definition_for_small_business": arch_36_startup_capital_definition_for_small_business,
    "37_startup_capital_requirement_calculation": arch_37_startup_capital_requirement_calculation,
    "38_loan_capital_borrowed_with_interest": arch_38_loan_capital_borrowed_with_interest,
    "39_partner_equity_capital_shared_ownership": arch_39_partner_equity_capital_shared_ownership,
    "40_loan_vs_equity_capital_comparison_table": arch_40_loan_vs_equity_capital_comparison_table,
    "41_small_business_support_seda_and_dti": arch_41_small_business_support_seda_and_dti,
    "42_small_business_support_idc_nyda_khula_bee": arch_42_small_business_support_idc_nyda_khula_bee,
    "43_selecting_financing_source_scenario": arch_43_selecting_financing_source_scenario,
    "44_bank_loan_simple_interest_repayment_calculation": arch_44_bank_loan_simple_interest_repayment_calculation,
    "45_deficit_net_profit_inventory_liquidity_definitions": arch_45_deficit_net_profit_inventory_liquidity_definitions,
    "46_statement_of_net_worth_assets_vs_liabilities_concept": arch_46_statement_of_net_worth_assets_vs_liabilities_concept,
    "47_statement_of_net_worth_ledger_table": arch_47_statement_of_net_worth_ledger_table,
    "48_net_worth_comparison_bar_graph": arch_48_net_worth_comparison_bar_graph,
    "49_compound_saving_habit_household_resilience": arch_49_compound_saving_habit_household_resilience,
    "50_integrated_savings_banking_entrepreneurship_synthesis": arch_50_integrated_savings_banking_entrepreneurship_synthesis,
}
