

def _make_crj_cpj_adjustments(*, r: random.Random, difficulty: str, mode: str) -> Dict[str, Any]:
    """G11 CRJ/CPJ adjustments from bank statement + reconciliation context."""
    business = r.choice(["Mass Traders", "Baloyi Stores", "Mamba Traders"])
    month = r.choice(["March", "June", "September", "December"])
    year = int(r.choice([20, 21, 22, 23, 24]))

    opening_balance = float(r.choice([5000, 8500, 12300, 15600]))

    bank_charges = float(r.choice([250, 350, 450]))
    eft_cr = float(r.choice([0, 1200, 2500]))
    rd_amount = float(r.choice([0, 500, 800]))
    dishonoured = float(r.choice([0, 1800, 2400, 3000]))
    rent_income = float(r.choice([3500, 4200, 5000]))
    interest = float(r.choice([800, 1200, 1500]))

    crj_total = rent_income + interest + eft_cr + rd_amount
    cpj_total = bank_charges + dishonoured

    closing_balance = opening_balance + crj_total - cpj_total

    headers = ["Doc.no.", "Day", "Details", "Fol.", "Bank", "Sundry accounts", "Amount", "Details"]

    rows: List[List[Optional[str]]] = [
        ["", f"{month}", "", "", "", "", "", ""],
        ["", "5", "Rent income", "GL", _money(rent_income), "", "", ""],
        ["", "12", "Interest received", "GL", _money(interest), "", "", ""],
    ]
    if eft_cr > 0:
        rows.append(["EFT", "", "EFT received", "GL", _money(eft_cr), "", "", ""])
    if rd_amount > 0:
        rows.append(["", "", "RD Revenue", "GL", _money(rd_amount), "", "", ""])

    sundry_start = len(rows)
    rows.append(["", "Sundry accounts:", "", "", "", "", "", ""])
    rows.append(["", "Rent income", "GL", "", "", "", _money(rent_income), "Rent income"])
    rows.append(["", "Interest received", "GL", "", "", "", _money(interest), "Interest received"])
    if eft_cr > 0:
        rows.append(["", "Bank", "GL", "", "", "", _money(eft_cr), "EFT"])
    if rd_amount > 0:
        rows.append(["", "Revenue Dept", "GL", "", "", "", _money(rd_amount), "RD"])

    prompt = f"""G11 Controlled Test — Cash Journals Adjustments

You are provided with the Bank Statement for {business} for {month} 20{year}. 
Some transactions have not yet been recorded in the Cash Receipts Journal (CRJ) and Cash Payments Journal (CPJ).

Bank Reconciliation context:
- Opening Bank balance (favourable): R{_money(opening_balance)}
- Bank charges not yet recorded: R{_money(bank_charges)}
- Dishonoured cheque not yet recorded: R{_money(dishonoured)}
- EFT received: R{_money(eft_cr)}
- RD (Revenue Department): R{_money(rd_amount)}
- Rent income: R{_money(rent_income)}
- Interest received: R{_money(interest)}

Required: Record the missing entries in the CRJ below. CPJ entries should be recorded similarly (separate question)."""

    cell_hints: Dict[str, str] = {}
    if str(mode or "").strip().lower() == "scaffold":
        cell_hints["t0_r1_c4"] = "Enter the rent income amount in the Bank column."
        cell_hints["t0_r2_c4"] = "Enter the interest amount in the Bank column."

    return _mk_journal(
        prompt=prompt,
        journal_type="crj_adjustments",
        headers=headers,
        values_rows=rows,
        difficulty=difficulty,
        mode=mode,
        base_editable_cols=[0, 1, 2, 3, 4, 6, 7],
        title_fields=[
            {"label": "CASH RECEIPTS JOURNAL", "value": f"of {business}"},
            {"label": "Month", "value": f"{month} 20{year}"},
        ],
        cell_hints=cell_hints,
        archetype_key="g11_ct1_q2_crj_cpj_adjustments",
    )
