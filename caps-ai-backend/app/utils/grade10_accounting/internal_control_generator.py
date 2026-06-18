from __future__ import annotations

import random
import uuid
from typing import Any, Dict, List, Optional
from .scenario_builder import build_scenario


def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def _make_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def _make_mcq(*, prompt: str, options: List[str], correct_index: int, explanation: str, hint_trigger: Optional[str] = None) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_ic_mcq"),
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": 2,
        "hint_trigger": hint_trigger or explanation,
        "guidelines": [hint_trigger or explanation],
        "visual_aid_key": "internal_controls_overview",
    }


def _make_typed(*, prompt: str, sample_answer: str, grading_rubric: List[str]) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_ic_typed"),
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": sample_answer,
        "expected_answer_type": "text",
        "grading_rubric": grading_rubric,
        "marks": 4,
        "hint_trigger": f"Your answer should discuss: {', '.join(grading_rubric)}",
        "guidelines": [f"Your answer should discuss: {', '.join(grading_rubric)}"],
        "visual_aid_key": "internal_controls_typed",
    }


def _make_table_wordbank(
    *,
    prompt: str,
    headers: List[str],
    rows: List[List[str]],
    word_bank: List[Dict[str, str]],
    correct_map: Dict[str, Dict[str, str]],
    guidelines: Optional[List[str]] = None,
) -> Dict[str, Any]:
    return {
        "id": _make_id("acct10_ic_table_wordbank"),
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {
            "headers": headers,
            "rows": rows,
        },
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": guidelines or [],
        "expected_answer_type": "table_wordbank",
        "marks": len(rows) * 2,
        "visual_aid_key": "internal_controls_matching",
    }


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = _rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()

    # Generate Narrative Scenario 
    scenario = build_scenario(seed=seed)
    intro = scenario["intro"]

    def _maybe_filter(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if qtype_norm in ("", "mixed"):
            return items
        return [q for q in items if q.get("question_type") == qtype_norm] or items

    definition_pool: List[Dict[str, Any]] = []
    processes_pool: List[Dict[str, Any]] = []
    stock_pool: List[Dict[str, Any]] = []
    debtors_pool: List[Dict[str, Any]] = []
    creditors_pool: List[Dict[str, Any]] = []
    fixed_assets_pool: List[Dict[str, Any]] = []
    consumables_pool: List[Dict[str, Any]] = []
    cash_pool: List[Dict[str, Any]] = []
    activity_pool: List[Dict[str, Any]] = []

    # --- DEFINITION ---
    definition_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['owner']} wants to protect the assets of the business but does not know what internal control is.\n\nIn your own words, define internal control in a business.",
            sample_answer="Internal control is what management and staff do inside the business to exercise authority over activities, reduce risks (fraud/theft/errors), and help the business achieve its objectives and profit.",
            grading_rubric=["management and staff actions", "reduce risks/fraud/theft", "achieve objectives"],
        )
    )

    definition_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWho is ultimately responsible for following internal control measures at {scenario['business']}?",
            options=[
                f"Only the external auditor who visits {scenario['business']} once a year.",
                f"Only the owner, {scenario['owner']}.",
                "All employees, led by management.",
                "Only the accountant who prepares the books.",
            ],
            correct_index=2,
            explanation="Internal control is not only management's responsibility; all employees must follow and support control measures.",
        )
    )

    # --- PROCESSES ---
    processes_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\n{scenario['owner']} wants to implement a new control process to fix inventory shortages. Which sequence best describes the general control process?",
            options=[
                "Act against shortcomings \u2192 Analyse \u2192 Gather information \u2192 Decide objectives",
                "Decide objectives \u2192 Gather information \u2192 Analyse \u2192 Act against shortcomings",
                "Gather information \u2192 Decide objectives \u2192 Act \u2192 Analyse",
                "Analyse \u2192 Act \u2192 Decide objectives \u2192 Gather information",
            ],
            correct_index=1,
            explanation="Control starts by deciding objectives, then gathering and analysing information, then acting against shortcomings.",
        )
    )

    # --- STOCK CONTROL ---
    stock_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\n{scenario['owner']} has noticed missing items from the warehouse. Which is an example of a good stock control measure they should implement?",
            options=[
                "Allow any employee to access the storeroom.",
                "Do regular physical stocktaking and keep stock lists up to date.",
                "Delay recording stock purchases until month-end.",
                "Leave the warehouse doors unlocked during trading hours.",
            ],
            correct_index=1,
            explanation="Regular stocktaking helps prevent losses and ensures inventory records accurately reflect actual quantities on hand.",
            hint_trigger="Think about how restricting access and counting physical boxes would deter theft.",
        )
    )
    
    stock_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['owner']} suspects that either the customers or his employees are stealing stock from the shop.\n\nList THREE internal control measures that {scenario['owner']} should apply to solve the stock problem.",
            sample_answer="1. Check stock delivered to the shop against the invoice.\n2. Do regular physical stock counts.\n3. Install security cameras and tags on stock.\n4. Have security guards at the door.\n5. Separate duties among staff.",
            grading_rubric=["Regular stock counts", "Security tags / cameras / guards", "Separation of duties", "Check delivery against invoice"],
        )
    )

    # --- DEBTORS CONTROL ---
    debtors_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['owner']} noticed that several large credit customers are defaulting on their payments, causing cash flow issues for {scenario['business']}.\n\nGive TWO internal control measures for debtors to encourage early payments.",
            sample_answer="Examples: screen debtors carefully before offering credit (credit checks); keep complete records up to date; send regular monthly statements; charge interest on overdue accounts; pause credit if long overdue; give discount for early payments.",
            grading_rubric=["screen / credit checks", "send monthly statements", "charge interest on overdue accounts", "stop credit for bad payers", "give discount for early payment"],
        )
    )

    debtors_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhich of the following is the BEST way to encourage debtors to pay their accounts on time?",
            options=[
                "Only send statements at the end of the year.",
                "Grant cash discounts for early settlement and charge interest on overdue accounts.",
                "Stop selling to all debtors and only accept cash.",
                "Do not screen debtors before granting credit.",
            ],
            correct_index=1,
            explanation="Offering discounts for early payments and penalizing late payments with interest encourages prompt settlement.",
        )
    )

    # --- CREDITORS CONTROL ---
    creditors_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhen {scenario['owner']} chooses a new supplier (creditor) for {scenario['business']}, which factor is most relevant to internal control?",
            options=[
                "Does the supplier provide goods reliably and offer clear payment terms/invoices?",
                "Does the supplier allow blank cheques to be signed?",
                "Does the supplier avoid giving any physical invoices/source documents?",
                "Does the supplier insist on undocumented cash only for all transactions?",
            ],
            correct_index=0,
            explanation="Internal control requires reliable suppliers, clear terms, and proper documentation (source documents) for goods received.",
        )
    )

    creditors_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['business']} buys goods in large quantities. However, the stock received often includes damaged goods or goods that were not ordered. \n\nProvide TWO internal control measures that the supplier should implement to manage stock effectively before delivery.",
            sample_answer="1. Ensure packaging material is of good quality to prevent damage.\n2. Check if the stock is in good condition before delivery to customers.\n3. Check if the stock packaged matches the order that was placed by the customer.",
            grading_rubric=["Good quality packaging", "Check condition before delivery", "Check stock matches the order"],
        )
    )

    # --- FIXED ASSETS CONTROL ---
    fixed_assets_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['business']} recently bought two new delivery vans. The drivers have been using them for personal weekend trips.\n\nName TWO internal control measures for vehicles used by the business.",
            sample_answer="Examples: Keep usage/log books to track mileage; maintain vehicles regularly (services); authorize trips beforehand; park vehicles on the premises overnight.",
            grading_rubric=["Keep a logbook / track mileage", "authorize trips", "park on premises overnight", "regular maintenance"],
        )
    )

    fixed_assets_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\n{scenario['owner']} wants to protect the business's new computer equipment. Which control measure is most appropriate?",
            options=[
                "Wait until the equipment breaks to replace it.",
                "Allow any employee to take laptops home without signing them out.",
                "Maintain equipment regularly and write off depreciation appropriately.",
                "Only buy equipment that is already obsolete.",
            ],
            correct_index=2,
            explanation="Proper maintenance and accurately writing off depreciation are key controls for equipment.",
        )
    )

    # --- CONSUMABLES CONTROL ---
    consumables_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhat is a key internal control measure to prevent the waste of consumable goods (e.g., stationery or packaging) at {scenario['business']}?",
            options=[
                "No one is assigned responsibility for consumables.",
                "Appoint a responsible person to keep stock and record issues/purchases out of a locked cupboard.",
                "Issue consumables without keeping any formal records.",
                "Store them on an open desk where anyone can take them without supervision.",
            ],
            correct_index=1,
            explanation="Consumables should be managed by a responsible person who keeps stock and records purchases and issues.",
        )
    )

    # --- CASH CONTROL ---
    cash_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\n{scenario['owner']} has found cash missing from the till at the end of the day. Which is a correct internal control for cash receipts?",
            options=[
                "Store cash in an unlocked drawer until the weekend.",
                "Issue a source document for all cash received and deposit cash at the bank as soon as possible (daily).",
                "Never record cash receipts in the books.",
                "Allow one person to receive the cash, record it, and deposit it without checks.",
            ],
            correct_index=1,
            explanation="Cash receipts should be supported by documents, recorded promptly, kept safe, and deposited quickly (preferably daily) by different staff members (division of duties).",
        )
    )

    cash_pool.append(
        _make_mcq(
            prompt=f"{intro}\n\nWhich statement about cheques and the Cash Payments Journal is a correct internal control measure?",
            options=[
                f"{scenario['owner']} can sign blank cheques in advance for convenience.",
                "Cheque books should be kept safely under lock and key and recorded in consecutive numbers.",
                "Cheques should never be entered in the Cash Payments Journal.",
                "Only one undocumented signature is needed for safety.",
            ],
            correct_index=1,
            explanation="Control requires safe storage of cheques and recording issued cheques in sequence. Blank cheques must never be signed.",
        )
    )

    cash_pool.append(
        _make_typed(
            prompt=f"{intro}\n\n{scenario['owner']} puts a fixed amount in the petty cash every month, but there is never enough money available to make small payments. The petty cashier cannot explain what happened to the money.\n\nList TWO internal control measures that {scenario['owner']} should apply to solve the petty cash problem.",
            sample_answer="1. Payments from petty cash need to be authorised.\n2. Petty cash vouchers should be completed and authorised.\n3. The petty cash box should be locked in the safe.\n4. Proof of payments/till slips should be kept along with the voucher.\n5. Vouchers must be recorded in a Petty Cash Journal daily.",
            grading_rubric=["Authorise payments", "Complete vouchers", "Lock box in safe", "Keep proof of payments/till slips", "Record daily in journal"],
        )
    )

    # --- ACTIVITY / MATCHING ---
    matching_pairs_1 = [
        ("Deposit cash in the bank within 24 hours.", "Cash receipts control"),
        ("Blank cheques should never be signed in advance.", "Cash payments control"),
        ("Access to petty cash limited to one specific person.", "Petty cash control"),
        ("Regular physical stocktaking is completed.", "Stock control"),
        ("Send regular monthly statements of account.", "Debtors control"),
    ]

    wb_tokens_1: List[Dict[str, str]] = []
    wb_correct_1: Dict[str, Dict[str, str]] = {}
    wb_rows_1: List[List[str]] = []

    for i, (_, label) in enumerate(matching_pairs_1):
        token_id = f"acct10_ic_token_{uuid.uuid4().hex[:10]}"
        wb_tokens_1.append({"id": token_id, "label": label})
        wb_correct_1[str(i)] = {"2": token_id}

    distractors_1 = ["Ethics Control", "GAAP Standards", "Budgeting"]
    for label in distractors_1:
        wb_tokens_1.append({"id": f"acct10_ic_token_{uuid.uuid4().hex[:10]}", "label": label})

    for left, _ in matching_pairs_1:
        wb_rows_1.append([left, ""])

    r.shuffle(wb_tokens_1)

    activity_pool.append(
        _make_table_wordbank(
            prompt=f"{intro}\n\nMatch each internal control action for {scenario['business']} to the correct control area.",
            headers=["Action", "Control area"],
            rows=wb_rows_1,
            word_bank=wb_tokens_1,
            correct_map=wb_correct_1,
            guidelines=["Click a word-bank item, then click a slot to place it."],
        )
    )

    matching_pairs_2 = [
        ("Keep a logbook and authorise trips beforehand.", "Vehicles"),
        ("Screen customers carefully before granting credit.", "Debtors"),
        ("Check goods delivered against the invoice.", "Stock"),
        ("Write off depreciation appropriately and do regular maintenance.", "Equipment"),
        ("Check if the supplier provides trade discounts.", "Creditors"),
    ]

    wb_tokens_2: List[Dict[str, str]] = []
    wb_correct_2: Dict[str, Dict[str, str]] = {}
    wb_rows_2: List[List[str]] = []

    for i, (_, label) in enumerate(matching_pairs_2):
        token_id = f"acct10_ic_token_{uuid.uuid4().hex[:10]}"
        wb_tokens_2.append({"id": token_id, "label": label})
        wb_correct_2[str(i)] = {"2": token_id}

    distractors_2 = ["Consumable goods", "Land and Buildings", "Petty cash"]
    for label in distractors_2:
        wb_tokens_2.append({"id": f"acct10_ic_token_{uuid.uuid4().hex[:10]}", "label": label})

    for left, _ in matching_pairs_2:
        wb_rows_2.append([left, ""])
    
    r.shuffle(wb_tokens_2)

    activity_pool.append(
        _make_table_wordbank(
            prompt=f"{intro}\n\nMatch each internal control action to the asset or area it protects.",
            headers=["Action", "Asset / Area"],
            rows=wb_rows_2,
            word_bank=wb_tokens_2,
            correct_map=wb_correct_2,
            guidelines=["Click a word-bank item, then click a slot to place it."],
        )
    )

    pools_by_subskill = {
        "definition": definition_pool,
        "processes": processes_pool,
        "stock": stock_pool,
        "debtors": debtors_pool,
        "creditors": creditors_pool,
        "fixed_assets": fixed_assets_pool,
        "consumables": consumables_pool,
        "cash": cash_pool,
        "activity_1": activity_pool,
        "mixed": definition_pool + processes_pool + stock_pool + debtors_pool + creditors_pool + fixed_assets_pool + consumables_pool + cash_pool + activity_pool,
    }

    pool = pools_by_subskill.get(subskill_norm, pools_by_subskill["mixed"])
    pool = _maybe_filter(pool)

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out
