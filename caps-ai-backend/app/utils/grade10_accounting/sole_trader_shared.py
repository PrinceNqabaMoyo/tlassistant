from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple

from ..sole_trader.core import fmt_money as _fmt_money


def make_rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r


def ta_headers_activity23() -> List[str]:
    return [
        "Nr",
        "Source document",
        "Account debited",
        "Account credited",
        "A",
        "OE",
        "L",
    ]


def ta_headers_activity24() -> List[str]:
    return [
        "Nr",
        "Source document",
        "Account debited",
        "Account credited",
        "Amount",
        "A",
        "O",
        "L",
    ]


def ta_schema_headers(schema: str) -> List[str]:
    if schema == "activity23":
        return ta_headers_activity23()
    if schema == "activity24":
        return ta_headers_activity24()
    if schema == "gl_amount_aol":
        return ["No.", "Account debited", "Account credited", "Amount", "A", "O", "L"]
    if schema == "gl_aol":
        return ["No.", "Account debited", "Account credited", "A", "O", "L"]
    if schema == "source_gl_amount_aol":
        return ["No.", "Source document", "Account debited", "Account credited", "Amount", "A", "O", "L"]
    if schema == "journal_gl_amount_aol":
        return ["No.", "Subsidiary Journal", "Account debited", "Account credited", "Amount", "A", "O", "L"]
    if schema == "gl_subledger_amount_aol":
        return ["No.", "GL Dr", "GL Cr", "Subsidiary Dr", "Subsidiary Cr", "Amount", "A", "O", "L"]
    if schema == "internal_gl_amount_aol":
        return ["No.", "Internal Document", "Account debited", "Account credited", "Amount", "Assets", "Equity", "Liabilities"]
    if schema == "reason_effect":
        return ["No.", "Assets (Reason)", "Assets (Effect)", "Owner's Equity (Reason)", "Owner's Equity (Effect)", "Liabilities (Reason)", "Liabilities (Effect)"]
    return ta_headers_activity24()


def ta_fmt_sign(v: float) -> str:
    if abs(v) < 1e-9:
        return "0"
    return "+" if v > 0 else "-"


def ta_fmt_amount(v: float, *, prefer_pm: bool = False) -> str:
    if abs(v) < 1e-9:
        return "0"
    amt = _fmt_money(abs(v))
    if prefer_pm:
        return f"±{amt}"
    return ("+" if v > 0 else "-") + amt


def ta_effects_to_signs(a: float, o: float, l: float) -> Tuple[str, str, str]:
    return (ta_fmt_sign(a), ta_fmt_sign(o), ta_fmt_sign(l))


def ta_effects_to_signed_amounts(a: float, o: float, l: float) -> Tuple[str, str, str]:
    return (ta_fmt_amount(a), ta_fmt_amount(o), ta_fmt_amount(l))


def ta_schema_to_row(schema: str, t: Dict[str, Any]) -> List[Optional[str]]:
    nr = str(t.get("nr") or "")
    source = str(t.get("source") or "")
    jrnl = str(t.get("journal") or "")
    internal = str(t.get("internal") or "")
    dr = str(t.get("dr") or "")
    cr = str(t.get("cr") or "")
    sub_dr = str(t.get("sub_dr") or "")
    sub_cr = str(t.get("sub_cr") or "")
    amt = t.get("amount")
    a = float(t.get("a") or 0.0)
    o0 = float(t.get("o") or 0.0)
    l0 = float(t.get("l") or 0.0)

    a_s, o_s, l_s = ta_effects_to_signs(a, o0, l0)
    a_amt, o_amt, l_amt = ta_effects_to_signed_amounts(a, o0, l0)

    # Optional display overrides for special archetypes where multiple values are shown in one cell.
    a_override = t.get("a_override")
    o_override = t.get("o_override")
    l_override = t.get("l_override")
    if a_override is not None:
        a_s = str(a_override)
        a_amt = str(a_override)
    if o_override is not None:
        o_s = str(o_override)
        o_amt = str(o_override)
    if l_override is not None:
        l_s = str(l_override)
        l_amt = str(l_override)

    # For reason/effect schemas, provide a "reason" account name based on which side changes.
    # This is intentionally simple but consistent with debit/credit behavior:
    # - Asset increase usually debits an asset account; decrease usually credits it.
    # - Equity increase usually credits an income/capital account; decrease usually debits an expense/drawings account.
    # - Liability increase usually credits a liability; decrease usually debits it.
    assets_reason = ""
    if abs(a) > 1e-9:
        assets_reason = dr if a > 0 else cr
    equity_reason = ""
    if abs(o0) > 1e-9:
        equity_reason = cr if o0 > 0 else dr
    liabilities_reason = ""
    if abs(l0) > 1e-9:
        liabilities_reason = cr if l0 > 0 else dr
    if schema == "activity23":
        return [nr, source, dr, cr, a_amt, o_amt, l_amt]
    if schema == "activity24":
        return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
    if schema == "gl_amount_aol":
        return [nr, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
    if schema == "gl_aol":
        return [nr, dr, cr, a_amt, o_amt, l_amt]
    if schema == "source_gl_amount_aol":
        return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
    if schema == "journal_gl_amount_aol":
        return [nr, jrnl, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
    if schema == "gl_subledger_amount_aol":
        return [nr, dr, cr, sub_dr, sub_cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]
    if schema == "internal_gl_amount_aol":
        return [nr, internal or source, dr, cr, "" if amt is None else _fmt_money(amt), a_amt, o_amt, l_amt]
    if schema == "reason_effect":
        return [nr, assets_reason, a_s, equity_reason, o_s, liabilities_reason, l_s]
    return [nr, source, dr, cr, "" if amt is None else _fmt_money(amt), a_s, o_s, l_s]


def make_ta_tx(
    *,
    nr: str,
    source: str = "",
    journal: str = "",
    internal: str = "",
    dr: str,
    cr: str,
    amount: Optional[float],
    a: float,
    o: float,
    l: float,
) -> Dict[str, Any]:
    return {
        "nr": nr,
        "source": source,
        "journal": journal,
        "internal": internal,
        "dr": dr,
        "cr": cr,
        "amount": amount,
        "a": a,
        "o": o,
        "l": l,
    }
