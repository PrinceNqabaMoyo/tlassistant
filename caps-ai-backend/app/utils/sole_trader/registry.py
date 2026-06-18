from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from .core import make_calc, make_mcq, make_typed, rng, round_money
from .journals.crj import make_crj_single_row_question
from .journals.dj import make_dj_single_row_question


def _ledger_headers() -> List[str]:
    return [
        "Account",
        "Debit (Dr)",
        "Credit (Cr)",
    ]


def _t_account_ledger_headers() -> List[str]:
    return [
        "Date",
        "Details",
        "Fol",
        "Amount",
        "Date",
        "Details",
        "Fol",
        "Amount",
    ]


def _trial_balance_headers() -> List[str]:
    return [
        "Account",
        "Debit",
        "Credit",
    ]


def _fmt_money(x: Optional[float]) -> str:
    if x is None:
        return ""
    return f"{round_money(x):.2f}"


def _calc_cost_price_from_selling_price_and_margin(*, sp: float, profit_margin_pct: float) -> float:
    return round_money(sp / (1.0 + (profit_margin_pct / 100.0)))


def _make_accounting_cycle_question(*, r: random.Random) -> Dict[str, Any]:
    variants = [
        (
            "Put the following steps of the accounting cycle in the correct order (start to finish):\n"
            "A. Prepare a trial balance\n"
            "B. Record transactions in journals\n"
            "C. Post to the ledger\n"
            "D. Prepare financial statements\n"
            "E. Make year-end adjustments / closing entries",
            "B, C, A, E, D",
        ),
        (
            "In a bookkeeping system, which comes FIRST after a transaction takes place?",
            "Record it in the relevant journal (source document).",
        ),
        (
            "Which record is used to GROUP accounts and show their balances after posting from journals?",
            "The general ledger (ledger accounts).",
        ),
    ]

    prompt, sample = r.choice(variants)
    return make_typed(prompt=prompt, sample_answer=sample)


def _make_simple_cpj_question(*, r: random.Random) -> Dict[str, Any]:
    return make_typed(
        prompt=(
            "Name the subsidiary journal used to record CASH payments by cheque/EFT, and state one example transaction."
        ),
        sample_answer=(
            "Cash Payments Journal (CPJ) – e.g. paying a creditor by cheque, paying wages by cheque, or buying stock for cash by cheque."
        ),
    )


def _make_simple_daj_question(*, r: random.Random) -> Dict[str, Any]:
    return make_typed(
        prompt="What is recorded in the Debtors Allowances Journal (DAJ)?",
        sample_answer="Credit sales returns/allowances (credit notes) granted to debtors, and (under perpetual) the related cost of sales reversal.",
    )


def _make_simple_cj_question(*, r: random.Random) -> Dict[str, Any]:
    return make_typed(
        prompt="What is recorded in the Creditors Journal (CJ)?",
        sample_answer="Credit purchases from creditors (invoices) – total posted to Creditors Control and analysed into stock/stationery/equipment/sundry.",
    )


def _make_simple_caj_question(*, r: random.Random) -> Dict[str, Any]:
    return make_typed(
        prompt="What is recorded in the Creditors Allowances Journal (CAJ)?",
        sample_answer="Returns/allowances from creditors (debit notes) – total posted to Creditors Control and analysed into relevant columns.",
    )


def _make_ledger_posting_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])
    day = int(r.choice([2, 5, 10, 14, 18, 22, 26, 29]))

    amount = float(r.choice([450, 800, 1200, 1800, 2400, 3600, 5200]))
    kind = r.choice(["cash_sales", "pay_wages"])

    if kind == "cash_sales":
        prompt_tx = f"{day} {month}: Cash sales, R{amount:.2f}."
        debit_account = "Bank"
        credit_account = "Sales"
    else:
        prompt_tx = f"{day} {month}: Paid wages by cheque, R{amount:.2f}."
        debit_account = "Wages"
        credit_account = "Bank"

    headers = _ledger_headers()

    # This is a typed question for now (interactive ledger module will follow in the next refactor step)
    return make_typed(
        prompt=(
            f"{business}\nLedger posting for {month}\n\nContext:\n- {prompt_tx}\n\n"
            "Required:\nState the debit account and credit account (double entry)."
        ),
        sample_answer=f"Debit {debit_account}; Credit {credit_account}; Amount R{amount:.2f}.",
    )


def _make_trial_balance_question(*, r: random.Random, difficulty: str = "easy") -> Dict[str, Any]:
    business = r.choice(["Khumalo Traders", "Mokoena Stores", "Dlamini Spares"])
    month = r.choice(["January", "February", "March", "April", "May", "June"])

    bank = float(r.choice([12500, 18200, 23650, 30500]))
    trading_stock = float(r.choice([7800, 9200, 10600, 12400]))
    sales = float(r.choice([18500, 24200, 36000, 42000]))
    capital = bank + trading_stock - sales

    return make_typed(
        prompt=(
            f"{business}\nTrial Balance for {month}\n\n"
            "Use the balances below to prepare a Trial Balance (Dr/Cr):\n"
            f"- Bank: R{bank:.2f} (Dr)\n"
            f"- Trading stock: R{trading_stock:.2f} (Dr)\n"
            f"- Sales: R{sales:.2f} (Cr)\n"
            "- Capital: (balancing figure)\n\n"
            "Required:\nGive the Capital balance and state whether the trial balance balances."
        ),
        sample_answer=f"Capital: R{capital:.2f} (Cr). Debits equal credits.",
    )


def generate_questions(
    *,
    subskill: str = "mixed",
    difficulty: str = "easy",
    question_type: str = "mixed",
    count: int = 1,
    seed: Optional[int] = None,
) -> List[Dict[str, Any]]:
    r = rng(seed)

    n = int(count) if isinstance(count, int) else 1
    if n < 1:
        n = 1
    if n > 20:
        n = 20

    subskill_norm = str(subskill or "mixed").strip().lower()
    qtype_norm = str(question_type or "mixed").strip().lower()

    def _maybe_filter(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        if qtype_norm in ("", "mixed"):
            return items
        return [q for q in items if q.get("question_type") == qtype_norm] or items

    concepts_pool: List[Dict[str, Any]] = []
    accounting_cycle_pool: List[Dict[str, Any]] = []
    equation_pool: List[Dict[str, Any]] = []
    crj_pool: List[Dict[str, Any]] = []
    cpj_pool: List[Dict[str, Any]] = []
    dj_pool: List[Dict[str, Any]] = []
    daj_pool: List[Dict[str, Any]] = []
    cj_pool: List[Dict[str, Any]] = []
    caj_pool: List[Dict[str, Any]] = []
    ledger_pool: List[Dict[str, Any]] = []
    trial_balance_pool: List[Dict[str, Any]] = []
    journals_pool: List[Dict[str, Any]] = []

    concepts_pool.extend(
        [
            make_mcq(
                prompt="A sole proprietor is best described as:",
                options=[
                    "A business owned by many shareholders",
                    "A one-person business where the owner receives all profits/losses",
                    "A partnership of 2 to 20 partners",
                    "A government-owned enterprise",
                ],
                correct_index=1,
                explanation="A sole proprietor (sole trader) is owned by one person.",
            ),
            make_typed(
                prompt="Explain the business entity principle in a sole trader context.",
                sample_answer="The owner and the business are separate entities; business transactions must be recorded separately from the owner's personal transactions.",
            ),
        ]
    )

    equation_pool.append(
        make_mcq(
            prompt="Which accounting equation is correct?",
            options=[
                "Assets = Owner's equity + Liabilities",
                "Assets = Owner's equity - Liabilities",
                "Owner's equity = Assets + Liabilities",
                "Liabilities = Owner's equity - Assets",
            ],
            correct_index=0,
            explanation="The basic accounting equation is Assets = Owner's equity + Liabilities.",
        )
    )

    if difficulty in ("medium", "hard"):
        sp = float(r.choice([20800, 24000, 60000, 80000]))
        pm = float(r.choice([25, 50, 66.6667]))
        cp = _calc_cost_price_from_selling_price_and_margin(sp=sp, profit_margin_pct=pm)
        equation_pool.append(
            make_calc(
                prompt=f"A trader sells goods for R{sp:.2f}. The profit margin is {pm:g}%. Calculate the cost price.",
                correct_value=cp,
                unit="R",
            )
        )

    crj_pool.extend([
        make_crj_single_row_question(r=r, difficulty=difficulty),
    ])

    dj_pool.extend([
        make_dj_single_row_question(r=r, difficulty=difficulty),
    ])

    cpj_pool.append(_make_simple_cpj_question(r=r))
    daj_pool.append(_make_simple_daj_question(r=r))
    cj_pool.append(_make_simple_cj_question(r=r))
    caj_pool.append(_make_simple_caj_question(r=r))

    ledger_pool.append(_make_ledger_posting_question(r=r, difficulty=difficulty))
    trial_balance_pool.append(_make_trial_balance_question(r=r, difficulty=difficulty))

    accounting_cycle_pool.extend([
        _make_accounting_cycle_question(r=r),
        _make_accounting_cycle_question(r=r),
    ])

    journals_pool.extend(crj_pool + cpj_pool + dj_pool + daj_pool + cj_pool + caj_pool)

    pools_by_subskill = {
        "concepts": concepts_pool,
        "definition": concepts_pool,
        "accounting_cycle": accounting_cycle_pool,
        "accounting cycle": accounting_cycle_pool,
        "equation": equation_pool,
        "accounting equation": equation_pool,
        "ledgers": ledger_pool,
        "ledger": ledger_pool,
        "trial_balance": trial_balance_pool,
        "trial balance": trial_balance_pool,
        "journals": journals_pool,
        "journal": journals_pool,
        "crj": crj_pool,
        "cpj": cpj_pool,
        "dj": dj_pool,
        "daj": daj_pool,
        "cj": cj_pool,
        "caj": caj_pool,
        "pcj": journals_pool,
        "gj": journals_pool,
        "mixed": concepts_pool + accounting_cycle_pool + equation_pool + ledger_pool + trial_balance_pool + journals_pool,
    }

    pool = pools_by_subskill.get(subskill_norm, pools_by_subskill["mixed"])
    pool = _maybe_filter(pool)

    out: List[Dict[str, Any]] = []
    for _ in range(n):
        out.append(r.choice(pool))

    return out
