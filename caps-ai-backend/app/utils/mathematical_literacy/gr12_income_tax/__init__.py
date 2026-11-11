"""Grade 12 Mathematical Literacy: INCOME TAX.
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 1 Finance:
Taxable Income, SARS Progressive Tax Brackets, Primary/Secondary/Tertiary Rebates,
Tax Thresholds, Medical Scheme Fees Tax Credits, Payslip Take-Home Pay, and IRP5 Assessments/Refunds.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .foundations_taxable_income import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .tax_brackets_calculation import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .rebates_age_groups import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .thresholds_effective_rate import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .medical_tax_credits import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .payslip_take_home_pay import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .irp5_assessments_refunds import (
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
)

_RAW_FUNCS = [
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
]

SUBSKILLS: List[str] = [f"tax_gr12_{i:02d}" for i in range(1, 53)]

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, fn in enumerate(_RAW_FUNCS, start=1):
    key = f"tax_gr12_{idx:02d}"
    alt_key = f"gr12_tax_subskill_{idx}"
    BUILDERS[key] = fn
    DISPATCH_TABLE[key] = fn
    DISPATCH_TABLE[alt_key] = fn
    DISPATCH_TABLE[idx] = fn
    DISPATCH_TABLE[str(idx)] = fn

SUBSKILLS_METADATA: List[Dict[str, Any]] = [
    {"id": 1, "key": "tax_gr12_01", "name": "Distinction Between Gross Income and Taxable Income", "category": "Foundations"},
    {"id": 2, "key": "tax_gr12_02", "name": "Tax-Deductible vs Non-Deductible Deductions", "category": "Foundations"},
    {"id": 3, "key": "tax_gr12_03", "name": "Allowable Pension Fund Deduction Cap Calculation", "category": "Foundations"},
    {"id": 4, "key": "tax_gr12_04", "name": "Calculating Monthly Taxable Income from Gross & Pension", "category": "Foundations"},
    {"id": 5, "key": "tax_gr12_05", "name": "Annualising Monthly Taxable Income for Tax Year Assessment", "category": "Foundations"},
    {"id": 6, "key": "tax_gr12_06", "name": "Determining Taxable Remuneration with Multiple Income Sources", "category": "Foundations"},
    {"id": 7, "key": "tax_gr12_07", "name": "UIF Statutory Deduction Calculation (1% Capped)", "category": "Foundations"},
    {"id": 8, "key": "tax_gr12_08", "name": "Non-Taxable Allowances and Fringe Benefits Handling", "category": "Foundations"},
    {"id": 9, "key": "tax_gr12_09", "name": "Identifying Applicable SARS Tax Bracket from Annual Taxable Income", "category": "Tax Brackets"},
    {"id": 10, "key": "tax_gr12_10", "name": "Bracket 1 Tax Calculation (18% Baseline)", "category": "Tax Brackets"},
    {"id": 11, "key": "tax_gr12_11", "name": "Bracket 2 Tax Calculation (Base + 25% Above Threshold)", "category": "Tax Brackets"},
    {"id": 12, "key": "tax_gr12_12", "name": "Bracket 3 Tax Calculation (Base + 30% Above Threshold)", "category": "Tax Brackets"},
    {"id": 13, "key": "tax_gr12_13", "name": "Bracket 4 Tax Calculation (Base + 35% Above Threshold)", "category": "Tax Brackets"},
    {"id": 14, "key": "tax_gr12_14", "name": "Bracket 5 Tax Calculation (Base + 38% Above Threshold)", "category": "Tax Brackets"},
    {"id": 15, "key": "tax_gr12_15", "name": "Bracket 6 Top Tier Tax Calculation (Base + 40% Above Threshold)", "category": "Tax Brackets"},
    {"id": 16, "key": "tax_gr12_16", "name": "Understanding Fixed Base Tax Derivation across Bracket Boundaries", "category": "Tax Brackets"},
    {"id": 17, "key": "tax_gr12_17", "name": "Primary Rebate Application for Taxpayers Under Age 65", "category": "Rebates"},
    {"id": 18, "key": "tax_gr12_18", "name": "Secondary Rebate Application for Taxpayers Aged 65 to 74", "category": "Rebates"},
    {"id": 19, "key": "tax_gr12_19", "name": "Tertiary Rebate Application for Taxpayers Aged 75 and Older", "category": "Rebates"},
    {"id": 20, "key": "tax_gr12_20", "name": "Comparative Net Tax Liability across Age Brackets with Identical Income", "category": "Rebates"},
    {"id": 21, "key": "tax_gr12_21", "name": "Calculating Monthly PAYE from Net Annual Tax after Rebates", "category": "Rebates"},
    {"id": 22, "key": "tax_gr12_22", "name": "Impact of Birthday Turning 65 During the Tax Year", "category": "Rebates"},
    {"id": 23, "key": "tax_gr12_23", "name": "Rebate Ceiling Rule: Non-Refundable Nature of Personal Rebates", "category": "Rebates"},
    {"id": 24, "key": "tax_gr12_24", "name": "Net Tax Due after Combining Primary, Secondary, and Tertiary Rebates", "category": "Rebates"},
    {"id": 25, "key": "tax_gr12_25", "name": "SARS Tax Threshold Verification for Taxpayers Under 65", "category": "Thresholds & Rates"},
    {"id": 26, "key": "tax_gr12_26", "name": "SARS Tax Threshold Verification for Taxpayers Aged 65 to 74", "category": "Thresholds & Rates"},
    {"id": 27, "key": "tax_gr12_27", "name": "SARS Tax Threshold Verification for Taxpayers Aged 75 and Older", "category": "Thresholds & Rates"},
    {"id": 28, "key": "tax_gr12_28", "name": "Deriving the Mathematical Tax Threshold from Primary Rebate / Rate", "category": "Thresholds & Rates"},
    {"id": 29, "key": "tax_gr12_29", "name": "Effective (Average) Tax Rate vs Marginal Tax Rate Comparison", "category": "Thresholds & Rates"},
    {"id": 30, "key": "tax_gr12_30", "name": "Calculating Percentage Effective Tax Rate for a Mid-Income Earner", "category": "Thresholds & Rates"},
    {"id": 31, "key": "tax_gr12_31", "name": "Marginal Tax Bracket Creep Analysis Following an Overtime Bonus", "category": "Thresholds & Rates"},
    {"id": 32, "key": "tax_gr12_32", "name": "Comparative Effective Tax Rates across Two Distinct Income Brackets", "category": "Thresholds & Rates"},
    {"id": 33, "key": "tax_gr12_33", "name": "Medical Tax Credit (MTC) for Primary / Main Member Alone", "category": "Medical Credits"},
    {"id": 34, "key": "tax_gr12_34", "name": "Medical Tax Credit for Main Member plus First Dependant", "category": "Medical Credits"},
    {"id": 35, "key": "tax_gr12_35", "name": "Medical Tax Credit for Family Unit (Main Member + Spouse + Dependants)", "category": "Medical Credits"},
    {"id": 36, "key": "tax_gr12_36", "name": "Annual Medical Tax Credit Determination (Monthly Credit x 12)", "category": "Medical Credits"},
    {"id": 37, "key": "tax_gr12_37", "name": "Net Annual Tax Payable after Deducting Rebates and Medical Tax Credits", "category": "Medical Credits"},
    {"id": 38, "key": "tax_gr12_38", "name": "Monthly PAYE Calculation Incorporating Both Rebates and Medical Credits", "category": "Medical Credits"},
    {"id": 39, "key": "tax_gr12_39", "name": "Tax Benefit of Adding an Additional Dependant to Medical Aid Scheme", "category": "Medical Credits"},
    {"id": 40, "key": "tax_gr12_40", "name": "Distinction Between Medical Aid Contribution Deduction and Tax Credit", "category": "Medical Credits"},
    {"id": 41, "key": "tax_gr12_41", "name": "Calculating Total Statutory and Voluntary Payslip Deductions", "category": "Payslip & Take-Home"},
    {"id": 42, "key": "tax_gr12_42", "name": "Net Take-Home Pay Calculation from Gross Remuneration and Deductions", "category": "Payslip & Take-Home"},
    {"id": 43, "key": "tax_gr12_43", "name": "Net Take-Home Pay as a Percentage of Gross Salary", "category": "Payslip & Take-Home"},
    {"id": 44, "key": "tax_gr12_44", "name": "Impact of an Annual Salary Raise on Net Take-Home Pay", "category": "Payslip & Take-Home"},
    {"id": 45, "key": "tax_gr12_45", "name": "Debunking the 'Tax Bracket Penalty' Fallacy (Higher Bracket Never Decreases Net Pay)", "category": "Payslip & Take-Home"},
    {"id": 46, "key": "tax_gr12_46", "name": "Comprehensive Payslip Summary Audit and Verification", "category": "Payslip & Take-Home"},
    {"id": 47, "key": "tax_gr12_47", "name": "IRP5 Tax Certificate Source Code Interpretation (Gross vs Taxable)", "category": "IRP5 & Assessment"},
    {"id": 48, "key": "tax_gr12_48", "name": "Reconciliation of Monthly PAYE Withheld vs Annual Assessed Tax", "category": "IRP5 & Assessment"},
    {"id": 49, "key": "tax_gr12_49", "name": "Tax Refund Calculation from Section 18A Donation / Private RA Deductions", "category": "IRP5 & Assessment"},
    {"id": 50, "key": "tax_gr12_50", "name": "Additional Tax Payable on Assessment (Unwithheld Freelance / Rental Income)", "category": "IRP5 & Assessment"},
    {"id": 51, "key": "tax_gr12_51", "name": "Taxation of an Annual Bonus (13th Cheque) & Marginal Method", "category": "IRP5 & Assessment"},
    {"id": 52, "key": "tax_gr12_52", "name": "Dual-Employment Tax Liability Consolidation and Shortfall Calculation", "category": "IRP5 & Assessment"},
]
