import random
import uuid
from .scenario_builder import build_scenario


def _pick(rng, items):
    return items[rng.randrange(0, len(items))]


def _make_mcq(*, prompt, options, correct_index, explanation, marks=1, hint_trigger=None):
    return {
        "id": f"acct10_gaap_mcq_{uuid.uuid4().hex[:12]}",
        "question_type": "mcq",
        "prompt": prompt,
        "options": options,
        "correct_index": int(correct_index),
        "explanation": explanation,
        "expected_answer_type": "mcq",
        "marks": marks,
        "hint_trigger": hint_trigger or explanation,
        "guidelines": [hint_trigger or explanation],
        "visual_aid_key": "gaap_principles_overview",
    }


def _make_typed(*, prompt, answer, explanation, grading_rubric, marks=2):
    return {
        "id": f"acct10_gaap_typed_{uuid.uuid4().hex[:12]}",
        "question_type": "typed",
        "prompt": prompt,
        "sample_answer": answer,
        "expected_answer_type": "text",
        "explanation": explanation,
        "grading_rubric": grading_rubric,
        "marks": marks,
        "hint_trigger": f"Ensure your answer mentions: {', '.join(grading_rubric)}",
        "guidelines": [f"Ensure your answer mentions: {', '.join(grading_rubric)}"],
        "visual_aid_key": "gaap_principles_overview",
    }


def _make_table_wordbank(*, prompt, left_col_title, right_col_title, pairs, distractors=None, marks=10):
    word_bank = []
    correct_map = {}
    rows = []

    for i, (left, right) in enumerate(pairs):
        row_key = str(i)
        token_id = f"acct10_gaap_token_{uuid.uuid4().hex[:10]}"
        rows.append([left, ""])
        word_bank.append({"id": token_id, "label": right})
        correct_map[row_key] = {"2": token_id}

    if distractors:
        for right in distractors:
            word_bank.append({"id": f"acct10_gaap_token_{uuid.uuid4().hex[:10]}", "label": right})

    return {
        "id": f"acct10_gaap_table_wordbank_{uuid.uuid4().hex[:12]}",
        "question_type": "table_wordbank",
        "prompt": prompt,
        "table": {
            "headers": [left_col_title, right_col_title],
            "rows": rows,
        },
        "word_bank": word_bank,
        "correct_map": correct_map,
        "guidelines": ["Choose a word or term from the word bank to match each row."],
        "expected_answer_type": "table_wordbank",
        "marks": marks,
        "explanation": "Match each definition/example to the correct GAAP principle.",
        "visual_aid_key": "gaap_matching_table",
    }


def generate_grade10_gaap_questions(
    *,
    seed=None,
    subskill=None,
    difficulty="easy",
    question_type=None,
    count=1,
):
    rng = random.Random()
    if seed is not None:
        rng.seed(seed)
    
    # Generate Scenario for Context Injection
    scenario = build_scenario(seed=seed)
    intro = scenario["intro"]

    pools = {
        "intro": [
            lambda: _make_typed(
                prompt=f"{intro}\n\n{scenario['owner']} is preparing financial statements for the {scenario['industry']} but isn't sure why they must follow standardized rules.\n\nIn one sentence, explain what GAAP means.",
                answer="GAAP is a collection of rules, procedures and guidelines used to record and report financial information consistently and reliably.",
                explanation="GAAP provides a common framework so financial information is accurate, relevant, reliable, and comparable.",
                grading_rubric=["rules/procedures/guidelines", "record and report", "consistently/reliably"],
                marks=2,
            ),
            lambda: _make_typed(
                prompt=f"{intro}\n\nWhat does the abbreviation GAAP stand for?",
                answer="Generally Accepted Accounting Practice",
                explanation="GAAP stands for Generally Accepted Accounting Practice.",
                grading_rubric=["Generally Accepted Accounting Practice"],
                marks=1,
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\nWhy is GAAP important for {scenario['business']}?",
                options=[
                    f"It allows {scenario['owner']} to report in any style they prefer to attract investors.",
                    "It helps ensure financial information is consistent, reliable, and comparable across different businesses.",
                    "It replaces the need to keep source documents for transactions.",
                    f"It guarantees {scenario['business']} will make a stable profit.",
                ],
                correct_index=1,
                explanation="GAAP standardises how financial information is recorded and presented so users can trust and compare statements.",
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\nIn South Africa, which professional body is primarily responsible for training and developing the accounting profession, issuing statements related to GAAP?",
                options=[
                    "South African Revenue Service (SARS)",
                    "Accounting Standards Board (ASB)",
                    "South African Institute of Chartered Accountants (SAICA)",
                    "International Financial Reporting Standards (IFRS)"
                ],
                correct_index=2,
                explanation="SAICA is the professional body responsible for training and developing the accounting profession.",
            ),
        ],
        "principles": [
            lambda: _make_mcq(
                prompt=f"{intro}\n\n{scenario['business']} purchased a delivery vehicle 5 years ago for R150,000. It is currently worth R80,000. Which GAAP principle states the asset must remain recorded at R150,000 in the main ledger?",
                options=["Materiality", "Historical cost", "Going concern", "Matching"],
                correct_index=1,
                explanation="Historical cost requires assets to be recorded at original cost price.",
                hint_trigger="Think about how assets maintain their original purchase value in the records.",
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\n{scenario['owner']} took R1,000 from the till to pay for their child's school fees. Which GAAP principle requires this to be recorded as Drawings and not as a business expense?",
                options=["Business entity rule", "Prudence", "Matching", "Materiality"],
                correct_index=0,
                explanation="Business entity rule means the business is a separate entity from the owner.",
                hint_trigger="The owner and the business are treated as two separate people.",
            ),
            lambda: _make_typed(
                prompt=f"{intro}\n\n{scenario['business']} paid rent for 13 months instead of 12. Name the GAAP principle that dictates only 12 months' rent should be shown as an expense for the current financial year.",
                answer="Matching principle",
                explanation="Matching links expenses to the income they helped generate within the same accounting period.",
                grading_rubric=["Matching principle"],
                marks=2,
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\nA debtor owes {scenario['business']} money but is in severe financial difficulty. {scenario['owner']} decides to write off the account as bad debts to avoid overstating assets. Which principle is being applied?",
                options=["Prudence", "Going concern", "Historical cost", "Materiality"],
                correct_index=0,
                explanation="The Prudence principle dictates that accountants should be conservative when uncertain and not overstate assets.",
                hint_trigger="Being conservative about uncertain future income.",
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\n{scenario['owner']} decides to show 'Interest Expense' separate from the Bank overdraft account in the Financial Statements because it is a significant amount that will influence decision-making. Which principle is applied here?",
                options=["Matching", "Business entity rule", "Prudence", "Materiality"],
                correct_index=3,
                explanation="Materiality demands that all important (large) transactions and events should be indicated separately as they may influence decision-making.",
                hint_trigger="Think about whether the information is 'material' or important enough to show separately.",
            ),
            lambda: _make_mcq(
                prompt=f"{intro}\n\n{scenario['business']} assumes it will continue to operate for the foreseeable future, so it does not value its stock based on the amount it would receive if sold immediately today. Which GAAP principle is this?",
                options=["Going concern", "Historical cost", "Prudence", "Matching"],
                correct_index=0,
                explanation="The Going concern concept provides that the financial statements of a business are prepared based on the assumption that the business will continue to operate for the foreseeable future.",
                hint_trigger="Assuming the business will 'keep going'.",
            ),
            lambda: _make_typed(
                prompt=f"{intro}\n\n{scenario['business']} bought land and buildings 3 years ago for R500,000. Today, it is re-valued at R650,000. Under which GAAP principle must the amount entered in the Financial Statements remain R500,000?",
                answer="Historical cost",
                explanation="The Historical cost concept means that assets purchased by a business must be recorded in the books at cost price.",
                grading_rubric=["Historical cost"],
                marks=2,
            ),
            lambda: _make_typed(
                prompt=f"{intro}\n\n{scenario['owner']} recently inherited R500,000 from a grandparent and deposited it into their personal bank account, rather than {scenario['business']}'s bank account. Which GAAP principle ensures these financial affairs are kept separate?",
                answer="Business entity rule",
                explanation="The Business entity rule states that the financial affairs of the business must be kept separately from the financial affairs of the owners.",
                grading_rubric=["Business entity rule"],
                marks=2,
            ),
            lambda: _make_typed(
                prompt=f"{intro}\n\n{scenario['owner']} decides to write off a debtor's account even though {scenario['business']} will try to recover the money. Which principle requires the accountant to take this conservative approach?",
                answer="Prudence",
                explanation="Prudence (conservatism) dictates that the accountant should be conservative when uncertain and use the value that has the least influence on equity.",
                grading_rubric=["Prudence", "Conservatism"],
                marks=2,
            ),
        ],
        "matching_activity": [
            lambda: _make_table_wordbank(
                prompt=f"{intro}\n\nActivity 1: Match Column A to Column B to test your knowledge of GAAP principles.",
                left_col_title="Column A (Definition / Example)",
                right_col_title="Column B (GAAP principle)",
                pairs=[
                    ("All transactions or events that take place during a certain financial period must be recorded in the books during that financial period – irrespectively of when the cash is received or paid.", "Matching principle"),
                    ("An entity (business) will continue to exist for a certain period and that the Financial Statements of a business are prepared as though the business will continue to exist for some time.", "Going concern"),
                    ("Assets purchased by a business must be recorded in the books at cost price (purchased price).", "Historical cost"),
                    ("The accountant preparing the Financial Statements should be conservative in their approach to uncertainties by using the value that has the least influence on the equity of the business.", "Prudence (conservatism)"),
                    ("The financial affairs of the business must be kept separately from the financial affairs of the owners.", "Business entity rule"),
                    ("All important (large) transactions and events should be indicated separately in the Financial Statements, as these may influence decision-making.", "Materiality"),
                    ("Bad Debts written off is an example of this principle.", "Prudence (conservatism)"),
                    ("Interest expense has to appear separate to a Bank overdraft account in the Financial Statements.", "Materiality"),
                    ("Vehicles recorded at cost price.", "Historical cost"),
                    ("The owner of the business cannot list his Mercedes for personal use as a business asset.", "Business entity rule"),
                ],
                distractors=[],
                marks=10,
            )
        ],
    }

    pools["mixed"] = pools["intro"] + pools["principles"] + pools["matching_activity"]
    pools["gaap"] = pools["mixed"]

    effective_subskill = subskill or "gaap"
    if effective_subskill not in pools:
        effective_subskill = "gaap"

    effective_question_type = question_type

    def _filter_by_type(items):
        if not effective_question_type or effective_question_type == "mixed":
            return items

        out = []
        for fn in items:
            q = fn()
            if q.get("question_type") == effective_question_type:
                out.append(lambda q=q: q)
        return out or items

    pool = _filter_by_type(pools[effective_subskill])

    questions = []
    for _ in range(max(1, int(count or 1))):
        q = _pick(rng, pool)()
        questions.append(q)

    return {
        "success": True,
        "topic": "grade10_accounting_gaap",
        "subskill": effective_subskill,
        "difficulty": difficulty,
        "questions": questions,
    }
