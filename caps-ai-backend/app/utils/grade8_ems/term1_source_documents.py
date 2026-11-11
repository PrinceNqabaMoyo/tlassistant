"""Grade 8 EMS — Source Documents (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 2/02. Source documents.md

Covers CAPS subskills:
  1. visual_documents: Authentic vector source document plates (Duplicate Receipt, Cheque Counterfoil, Deposit Slip, Bank Statement, Cash Register Roll) and journal routing.
  2. concepts: Purpose and definition of source documents, original vs duplicate copies, audit trail requirement ("no document, no entry").
  3. discussion: Flow of source documents into subsidiary journals (CRJ/CPJ) and general ledger accounts.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

SUBSKILLS = [
    "visual_documents",
    "concepts",
    "discussion",
]

TOPIC_KEY = "grade8_ems_source_documents"
LO = "g8_ems_source_docs"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _with_metadata(
    item: Dict[str, Any],
    *,
    subskill: str,
    learning_objective_id: str,
    question_family_id: str,
    concept_id: Optional[str] = None,
    concept_group: str = "source_documents",
    misconception_tags: Optional[List[str]] = None,
    diagnostic_tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    enriched = dict(item)
    enriched.update({
        "topic_id": "grade8_ems",
        "subtopic_id": "term1_source_documents",
        "subskill": subskill,
        "learning_objective_id": learning_objective_id,
        "concept_id": concept_id or subskill,
        "concept_group": concept_group,
        "question_family_id": question_family_id,
        "curriculum_reference": "Term 2 > Source documents",
        "misconception_tags": misconception_tags or [],
        "diagnostic_tags": diagnostic_tags or ["accounting", "source_documents"],
    })
    return enriched


def _mcq_question(rng: random.Random, item: Dict[str, Any], mode: str = "scaffold") -> Dict[str, Any]:
    c_idx = int(item["correct_index"])
    correct_option = item["options"][c_idx]
    correct_letter = chr(65 + c_idx)
    marks = item.get("marks", 2)
    ans_text = f"{correct_letter}. {correct_option}"
    worked_sol = f"**{ans_text}** [{marks} mark{'s' if marks > 1 else ''}]\n\n{item.get('explanation', '')}"

    question = {
        "worked_solution": worked_sol,
        "canonical_solution": worked_sol,
        "id": f"g8_ems_doc_mcq_{rng.randint(1000, 999999)}",
        "title": item.get("title", "Source Documents Concept Check"),
        "question_type": "mcq",
        "topic": "Source documents",
        "prompt": item["prompt"],
        "options": item["options"],
        "correct_index": str(c_idx),
        "correct_answer": ans_text,
        "sample_answer": ans_text,
        "explanation": item["explanation"],
        "marks": marks,
        "hints": item.get("hints", {
            "tier_1": "Recall the purpose of source documents in proving financial transactions.",
            "tier_2": "Original copies go to the customer/bank; duplicate copies stay in the business books.",
            "tier_3": f"Correct answer is {ans_text}.",
        }),
        **{k: v for k, v in item.items() if k not in ["prompt", "options", "correct_index", "explanation", "title", "marks", "hints"]},
    }
    return question


def _typed_question(rng: random.Random, item: Dict[str, Any], mode: str = "scaffold") -> Dict[str, Any]:
    question = {
        "id": f"g8_ems_doc_typed_{rng.randint(1000, 999999)}",
        "title": item.get("title", "Source Document Interpretation"),
        "question_type": "typed",
        "topic": "Source documents",
        "prompt": item["prompt"],
        "marks": item["marks"],
        "marking_points": item["marking_points"],
        "sample_answer": item["sample_answer"],
        "ideal_answer": item.get("ideal_answer", item["sample_answer"]),
        "worked_solution": item["worked_solution"],
        "canonical_solution": item["worked_solution"],
        "hints": item.get("hints", {
            "tier_1": "Examine the document title, amounts, and parties involved.",
            "tier_2": "Money received goes to Cash Receipts Journal (CRJ); money paid goes to Cash Payments Journal (CPJ).",
            "tier_3": item["sample_answer"],
        }),
        **{k: v for k, v in item.items() if k not in ["prompt", "marks", "marking_points", "sample_answer", "ideal_answer", "title", "worked_solution", "hints"]},
    }
    return question


def _concept_pool(rng: random.Random) -> List[Dict[str, Any]]:
    return [
        _with_metadata({
            "title": "Purpose of a Receipt",
            "prompt": "What is the primary function of a receipt as a financial source document?",
            "options": [
                "To request payment from a debtor who bought goods on credit",
                "To serve as authentic written proof that cash has been received by the business",
                "To record money owed to trade suppliers for monthly purchases",
                "To summarize monthly profit and calculate VAT liability",
            ],
            "correct_index": 1,
            "explanation": "A receipt is an authentic written acknowledgement that money has been received. The duplicate copy is retained by the business to record the transaction in the Cash Receipts Journal (CRJ).",
            "marks": 2,
            "hints": {
                "tier_1": "Think about what happens when you pay cash at a store.",
                "tier_2": "A receipt proves that money was received.",
                "tier_3": "Correct answer is B (proof that cash has been received).",
            },
        }, subskill="concepts", learning_objective_id=f"{LO}_receipt_purpose", question_family_id="doc_purpose_mcq", concept_id="receipt"),

        _with_metadata({
            "title": "Deposit Slip Function",
            "prompt": "In South African commercial banking, a bank deposit slip is used by a business to:",
            "options": [
                "Withdraw emergency coins and petty cash from an ATM",
                "Deposit cash notes, coins, and cheques into the business bank account",
                "Authorize a customer to purchase equipment on 60 days credit",
                "Instruct SARS to issue an immediate income tax refund",
            ],
            "correct_index": 1,
            "explanation": "A deposit slip is completed when depositing money into a bank account. Once stamped by the teller, it serves as authentic audit proof verifying the Bank column in the CRJ.",
            "marks": 2,
            "hints": {
                "tier_1": "To 'deposit' means to put money into your account.",
                "tier_2": "A deposit slip records cash and cheques paid into the bank account.",
                "tier_3": "Correct answer is B.",
            },
        }, subskill="concepts", learning_objective_id=f"{LO}_deposit_slip_purpose", question_family_id="doc_purpose_mcq", concept_id="deposit_slip"),

        _with_metadata({
            "title": "The Golden Rule of Accounting Records",
            "prompt": "In accounting, what is the significance of the fundamental rule: 'No source document, no entry in the books'?",
            "options": [
                "It prevents accountants from having to balance journals at month-end",
                "It ensures that every recorded transaction has verifiable proof to prevent fraud and errors",
                "It legally exempts sole traders from having to open a business bank account",
                "It allows businesses to record estimated sales without calculating actual figures",
            ],
            "correct_index": 1,
            "explanation": "Every accounting entry must be supported by an authentic source document to maintain an auditable paper trail, verify transactions, and prevent fraudulent entries.",
            "marks": 2,
            "hints": {
                "tier_1": "Think about why businesses need proof before writing amounts in books.",
                "tier_2": "Source documents provide verifiable proof for auditing and prevent fraud.",
                "tier_3": "Correct answer is B.",
            },
        }, subskill="concepts", learning_objective_id=f"{LO}_rule_purpose", question_family_id="doc_rule_mcq", concept_id="accounting_rule"),

        _with_metadata({
            "title": "Original vs Duplicate Source Documents",
            "prompt": "When a service business issues a receipt to a customer for cash received, which copy is handed to the customer and which is kept by the business?",
            "options": [
                "Original to customer; Duplicate retained by the business for book entries",
                "Duplicate to customer; Original retained by the business for book entries",
                "Both original and duplicate are sent to the commercial bank",
                "The customer keeps both copies until month-end balancing",
            ],
            "correct_index": 0,
            "explanation": "The original document always goes to the external party (the customer), while the business retains the duplicate copy to record the transaction in the subsidiary journal (CRJ).",
            "marks": 2,
            "hints": {
                "tier_1": "Who gets the original copy when a document is written?",
                "tier_2": "The customer receives the original; the business files the duplicate.",
                "tier_3": "Correct answer is A.",
            },
        }, subskill="concepts", learning_objective_id=f"{LO}_orig_vs_dup", question_family_id="orig_dup_mcq", concept_id="orig_vs_dup"),
    ]


def _discussion_pool(rng: random.Random) -> List[Dict[str, Any]]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]

    return [
        _with_metadata({
            "title": "Accounting Cycle Audit Flow",
            "prompt": (
                f"Explain why source documents represent the first critical stage in the accounting cycle for {owner}'s "
                f"business. State two specific source documents and identify which subsidiary journal each document is entered into. (4 marks)"
            ),
            "marks": 4,
            "marking_points": [
                "Source documents provide verifiable, written proof that a financial transaction took place.",
                "They provide all necessary data: date, parties, transaction amount, and nature of the transaction.",
                "Duplicate Receipt -> entered into the Cash Receipts Journal (CRJ).",
                "Cheque Counterfoil / Bank Statement -> entered into the Cash Payments Journal (CPJ).",
            ],
            "sample_answer": (
                "(a) Source documents provide authentic written evidence and verified amounts for every transaction, preventing fraud.\n"
                "(b) Duplicate Receipt is entered into the Cash Receipts Journal (CRJ).\n"
                "(c) Cheque Counterfoil is entered into the Cash Payments Journal (CPJ)."
            ),
            "worked_solution": (
                "(a) **Authentic proof and audit trail** [1 mark]: Source documents provide verifiable written proof that a transaction occurred, preventing fraud.\n\n"
                "(b) **Details provided** [1 mark]: They contain the date, amount, payee/payer, and purpose necessary to make journal entries.\n\n"
                "(c) **Example 1 — Duplicate Receipt** [1 mark]: Entered into the Cash Receipts Journal (CRJ) to record cash received.\n\n"
                "(d) **Example 2 — Cheque Counterfoil** [1 mark]: Entered into the Cash Payments Journal (CPJ) to record payments made."
            ),
        }, subskill="discussion", learning_objective_id=f"{LO}_flow_essay", question_family_id="doc_flow_drill"),
    ]


def _visual_document_pool(rng: random.Random) -> List[Dict[str, Any]]:
    scenario = get_ems_scenario(rng)
    owner = scenario["entrepreneur"]
    area = scenario["area"]

    rent_amt = rng.randint(2, 6) * 500
    stat_amt = rng.randint(3, 9) * 100
    dep_notes = rng.randint(15, 35) * 100
    dep_cheques = rng.randint(10, 20) * 100
    dep_total = dep_notes + dep_cheques
    bank_fee = rng.choice([185, 220, 245, 290])
    crr_amt = rng.randint(4, 12) * 100

    docs = [
        # Document 1: Duplicate Receipt
        _with_metadata({
            "title": "Source Document Interpretation: Duplicate Receipt",
            "prompt": (
                f"Carefully examine the source document issued by {owner}'s service business in {area} shown below.\n\n"
                f"Answer the following questions:\n"
                f"1. Identify the name of this source document.\n"
                f"2. Into which subsidiary journal (CRJ or CPJ) must this transaction be entered?\n"
                f"3. Which account in the General Ledger will be credited?\n"
                f"4. What is the monetary amount received?"
            ),
            "diagram_spec": {
                "kind": "source_document",
                "diagram_role": "context",
                "document_type": "receipt",
                "title": "DUPLICATE RECEIPT",
                "doc_number": "082",
                "date": "14 June 2024",
                "business_name": f"{owner} Professional Services",
                "received_from": "M. Ndlovu",
                "amount": rent_amt,
                "description": "Rent of storeroom",
                "received_by": owner,
            },
            "marks": 4,
            "marking_points": [
                "Duplicate Receipt",
                "Cash Receipts Journal (CRJ)",
                "Rent Income",
                f"R{rent_amt}",
            ],
            "sample_answer": f"1. Duplicate Receipt\n2. Cash Receipts Journal (CRJ)\n3. Rent Income\n4. R{rent_amt}",
            "worked_solution": (
                f"(a) **Duplicate Receipt** [1 mark]\n\n"
                f"(b) **Cash Receipts Journal (CRJ)** [1 mark]\n\n"
                f"(c) **Rent Income** [1 mark]\n\n"
                f"(d) **R{rent_amt}** [1 mark]"
            ),
        }, subskill="visual_documents", learning_objective_id=f"{LO}_visual_receipt", question_family_id="visual_doc_drill"),

        # Document 2: Cheque Counterfoil
        _with_metadata({
            "title": "Source Document Interpretation: Cheque Counterfoil",
            "prompt": (
                f"Carefully examine the cheque counterfoil retained by {owner}'s enterprise in {area} shown below.\n\n"
                f"Answer the following questions:\n"
                f"1. Identify the name of this source document.\n"
                f"2. Into which subsidiary journal (CRJ or CPJ) must this transaction be recorded?\n"
                f"3. Which account in the General Ledger will be debited?\n"
                f"4. Who is the payee (the party receiving the payment)?"
            ),
            "diagram_spec": {
                "kind": "source_document",
                "diagram_role": "context",
                "document_type": "cheque_counterfoil",
                "title": "CHEQUE COUNTERFOIL",
                "doc_number": "204",
                "date": "22 June 2024",
                "business_name": f"{owner} Services",
                "payee": "Waltons Stationers",
                "amount": stat_amt,
                "description": "Office stationery and paper",
            },
            "marks": 4,
            "marking_points": [
                "Cheque Counterfoil",
                "Cash Payments Journal (CPJ)",
                "Stationery",
                "Waltons Stationers",
            ],
            "sample_answer": f"1. Cheque Counterfoil\n2. Cash Payments Journal (CPJ)\n3. Stationery\n4. Waltons Stationers",
            "worked_solution": (
                f"(a) **Cheque Counterfoil** [1 mark]\n\n"
                f"(b) **Cash Payments Journal (CPJ)** [1 mark]\n\n"
                f"(c) **Stationery** [1 mark]\n\n"
                f"(d) **Waltons Stationers** [1 mark]"
            ),
        }, subskill="visual_documents", learning_objective_id=f"{LO}_visual_counterfoil", question_family_id="visual_doc_drill"),

        # Document 3: Bank Deposit Slip
        _with_metadata({
            "title": "Source Document Interpretation: Bank Deposit Slip",
            "prompt": (
                f"Carefully examine the stamped bank deposit slip completed by {owner} in {area} shown below.\n\n"
                f"Answer the following questions:\n"
                f"1. Name the source document shown above.\n"
                f"2. What total monetary amount was deposited into the business bank account?\n"
                f"3. In the Cash Receipts Journal (CRJ), which column does this stamped document verify?\n"
                f"4. Why does the business retain a stamped teller copy of this document?"
            ),
            "diagram_spec": {
                "kind": "source_document",
                "diagram_role": "context",
                "document_type": "deposit_slip",
                "title": "BANK DEPOSIT SLIP",
                "bank_name": "Standard Bank",
                "date": "05 June 2024",
                "account_name": f"{owner} Services",
                "account_number": "104829104",
                "cash_amount": dep_notes,
                "cheque_amount": dep_cheques,
                "total_amount": dep_total,
            },
            "marks": 4,
            "marking_points": [
                "Bank Deposit Slip",
                f"R{dep_total}",
                "Bank column",
                "Authentic proof of deposit for audit and accounting records",
            ],
            "sample_answer": f"1. Bank Deposit Slip\n2. R{dep_total}\n3. Bank column\n4. Proof of deposit for audit and accounting records",
            "worked_solution": (
                f"(a) **Bank Deposit Slip** [1 mark]\n\n"
                f"(b) **R{dep_total}** [1 mark]\n\n"
                f"(c) **Bank column** [1 mark]\n\n"
                f"(d) **Proof of deposit for audit and accounting records** [1 mark]"
            ),
        }, subskill="visual_documents", learning_objective_id=f"{LO}_visual_deposit_slip", question_family_id="visual_doc_drill"),

        # Document 4: Bank Statement
        _with_metadata({
            "title": "Source Document Interpretation: Bank Statement",
            "prompt": (
                f"Carefully examine the bank statement excerpt for {owner}'s service business shown below.\n\n"
                f"Answer the following questions:\n"
                f"1. Identify the source document.\n"
                f"2. Into which subsidiary journal must these bank charges be recorded?\n"
                f"3. Which account in the General Ledger will be debited for this transaction?\n"
                f"4. Which account in the General Ledger will be credited?"
            ),
            "diagram_spec": {
                "kind": "source_document",
                "diagram_role": "context",
                "document_type": "bank_statement",
                "title": "BANK STATEMENT EXCERPT",
                "bank_name": "Nedbank",
                "date": "30 June 2024",
                "account_name": f"{owner} Services",
                "description": "Monthly Service Fees & Electronic Levy",
                "amount": bank_fee,
                "entry_type": "Debit",
            },
            "marks": 4,
            "marking_points": [
                "Bank Statement",
                "Cash Payments Journal (CPJ)",
                "Bank Charges",
                "Bank",
            ],
            "sample_answer": f"1. Bank Statement\n2. Cash Payments Journal (CPJ)\n3. Bank Charges\n4. Bank",
            "worked_solution": (
                f"(a) **Bank Statement** [1 mark]\n\n"
                f"(b) **Cash Payments Journal (CPJ)** [1 mark]\n\n"
                f"(c) **Bank Charges** [1 mark]\n\n"
                f"(d) **Bank** [1 mark]"
            ),
        }, subskill="visual_documents", learning_objective_id=f"{LO}_visual_bank_statement", question_family_id="visual_doc_drill"),

        # Document 5: Cash Register Roll (CRR)
        _with_metadata({
            "title": "Source Document Interpretation: Cash Register Roll",
            "prompt": (
                f"Carefully examine the cash register till roll (CRR) for {owner}'s business shown below.\n\n"
                f"Answer the following questions:\n"
                f"1. Identify the source document.\n"
                f"2. Into which subsidiary journal (CRJ or CPJ) is this transaction entered?\n"
                f"3. In which column in the subsidiary journal is the cash first recorded before banking?\n"
                f"4. Which account in the General Ledger will be credited?"
            ),
            "diagram_spec": {
                "kind": "source_document",
                "diagram_role": "context",
                "document_type": "cash_register_tape",
                "title": "CASH REGISTER ROLL (CRR)",
                "business_name": f"{owner} Services",
                "date": "18 June 2024",
                "crr_number": "CRR 01",
                "amount": crr_amt,
                "description": "Services Rendered (Cash)",
            },
            "marks": 4,
            "marking_points": [
                "Cash Register Roll (CRR) / Till Slip",
                "Cash Receipts Journal (CRJ)",
                "Analysis of Receipts",
                "Current Income",
            ],
            "sample_answer": f"1. Cash Register Roll (CRR)\n2. Cash Receipts Journal (CRJ)\n3. Analysis of Receipts\n4. Current Income",
            "worked_solution": (
                f"(a) **Cash Register Roll (CRR)** [1 mark]\n\n"
                f"(b) **Cash Receipts Journal (CRJ)** [1 mark]\n\n"
                f"(c) **Analysis of Receipts** [1 mark]\n\n"
                f"(d) **Current Income** [1 mark]"
            ),
        }, subskill="visual_documents", learning_objective_id=f"{LO}_visual_crr", question_family_id="visual_doc_drill"),
    ]
    return docs


def generate(subskill: str = "mixed", difficulty: str = "medium", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> Any:
    rng = _rng(seed)
    sub = str(subskill or "mixed").strip().lower()

    if sub in ("visual_documents", "documents", "reading_documents"):
        pool = _visual_document_pool(rng)
        chosen = rng.sample(pool, min(count, len(pool)))
        out = [_typed_question(rng, item, mode=mode) for item in chosen]
    elif sub == "discussion":
        pool = _discussion_pool(rng)
        chosen = rng.sample(pool, min(count, len(pool)))
        out = [_typed_question(rng, item, mode=mode) for item in chosen]
    elif sub == "concepts":
        pool = _concept_pool(rng)
        chosen = rng.sample(pool, min(count, len(pool)))
        out = [_mcq_question(rng, item, mode=mode) for item in chosen]
    else:
        # Mixed: sample across visual documents and concepts
        v_pool = _visual_document_pool(rng)
        c_pool = _concept_pool(rng)
        d_pool = _discussion_pool(rng)
        all_items = v_pool + c_pool + d_pool
        chosen = rng.sample(all_items, min(count, len(all_items)))
        out = []
        for item in chosen:
            if item.get("question_type") == "mcq" or "options" in item:
                out.append(_mcq_question(rng, item, mode=mode))
            else:
                out.append(_typed_question(rng, item, mode=mode))

    if count == 1 and len(out) == 1:
        return out[0]
    return out
