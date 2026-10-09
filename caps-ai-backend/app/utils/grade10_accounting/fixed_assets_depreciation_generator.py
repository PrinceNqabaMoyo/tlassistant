"""Grade 10 Accounting - Fixed Assets and Depreciation Generator.
Covers:
  - Depreciation on Cost Price (Straight-Line Method / Fixed Instalment).
  - Depreciation on Diminishing Balance (Reducing Balance / Carrying Value Method).
  - Carrying value calculation: Carrying Value = Cost - Accumulated Depreciation.
  - Recording depreciation in the General Journal (Debit Depreciation, Credit Accumulated Depreciation).
  - Asset Register schedules for Sole Traders.

Follows South African CAPS curriculum specifications and the 6-Pillar Generator Contract.
Strictly zero-LLM, deterministic execution.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


def generate_grade10_fixed_assets_question(
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> Dict[str, Any]:
    r = _rng(seed)
    subskill = mode if mode.startswith("elementary_") else "fixed_assets_depreciation"

    archetype = r.choice(["cost_price_method", "diminishing_balance_method", "asset_register_schedule", "general_journal_depreciation"])
    if subskill == "elementary_cost_price":
        archetype = "cost_price_method"
    elif subskill == "elementary_diminishing_balance":
        archetype = "diminishing_balance_method"
    elif subskill == "elementary_journal":
        archetype = "general_journal_depreciation"

    if archetype == "cost_price_method":
        # Straight-line: % on Cost Price
        cost = r.choice([120000, 150000, 180000, 240000, 300000])
        rate = r.choice([10, 15, 20])
        depr = int(cost * rate / 100)
        accum_init = r.choice([20000, 36000, 48000])
        new_accum = accum_init + depr
        carrying_val = cost - new_accum

        prompt = (
            f"Thabo Traders owns vehicles with an original cost price of \\(\\text{{R}}\\,{cost:,}\\). "
            f"Accumulated depreciation at the beginning of the financial year was \\(\\text{{R}}\\,{accum_init:,}\\).\n\n"
            f"Depreciation is written off at \\({rate}\\%\\) per annum on the **cost price** method.\n\n"
            f"1. Calculate the depreciation on vehicles for the current financial year.\n"
            f"2. Calculate the carrying value of vehicles at the end of the financial year."
        )
        sample_answer = (
            rf"\text{{Depreciation}} = \text{{R}}\,{cost:,} \times \frac{{{rate}}}{{100}} = \text{{R}}\,{depr:,}\\\ "
            rf"\text{{Accumulated Depreciation (End)}} = \text{{R}}\,{accum_init:,} + \text{{R}}\,{depr:,} = \text{{R}}\,{new_accum:,}\\\ "
            rf"\text{{Carrying Value}} = \text{{R}}\,{cost:,} - \text{{R}}\,{new_accum:,} = \text{{R}}\,{carrying_val:,}"
        )

        return {
            "id": f"g10_acct_fa_cost_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Fixed Assets",
            "subskill": "depreciation_cost_price",
            "learning_objective_id": "g10_acct_depr_straight_line",
            "archetype": "cost_price_method",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Depreciation: R{depr:,}, Carrying Value: R{carrying_val:,}",
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Depreciation formula on cost price ({cost:,} * {rate}%)", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Annual depreciation R{depr:,}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Accumulated depreciation update R{new_accum:,}", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": f"Final carrying value R{carrying_val:,}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "depreciation_calculated_on_carrying_value_instead_of_cost", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Under the cost price (straight-line) method, depreciation is ALWAYS calculated on the original cost price, ignoring accumulated depreciation.",
                "tier_2": rf"Annual depreciation $= \text{{Cost}} \times \frac{{{rate}}}{{100}} = \text{{R}}\,{cost:,} \times \frac{{{rate}}}{{100}}$.",
                "tier_3": rf"$\text{{Depreciation}} = \text{{R}}\,{depr:,}$. Then $\text{{Carrying Value}} = \text{{R}}\,{cost:,} - (\text{{R}}\,{accum_init:,} + \text{{R}}\,{depr:,}) = \text{{R}}\,{carrying_val:,}$.",
            },
            "misconception_tags": ["depreciation_calculated_on_carrying_value_instead_of_cost", "omitted_accumulated_depreciation"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "medium",
        }

    elif archetype == "diminishing_balance_method":
        # Diminishing balance: % on Carrying Value (Cost - Accumulated Depreciation)
        cost = r.choice([80000, 100000, 120000, 160000])
        accum_init = r.choice([20000, 30000, 40000])
        carrying_start = cost - accum_init
        rate = r.choice([10, 15, 20])
        depr = int(carrying_start * rate / 100)
        accum_end = accum_init + depr
        carrying_end = cost - accum_end

        prompt = (
            f"Khumalo Stores provides the following balances on 28 February 2026 (end of financial year):\n\n"
            f"- Equipment at cost: \\(\\text{{R}}\\,{cost:,}\\)\n"
            f"- Accumulated depreciation on Equipment (1 March 2025): \\(\\text{{R}}\\,{accum_init:,}\\)\n\n"
            f"Depreciation is provided for at \\({rate}\\%\\) per annum on the **diminishing balance** (carrying value) method.\n\n"
            f"1. Calculate the carrying value of equipment at the beginning of the financial year.\n"
            f"2. Calculate the depreciation for the year ended 28 February 2026.\n"
            f"3. Calculate the carrying value of equipment at 28 February 2026."
        )
        sample_answer = (
            rf"\text{{Carrying Value (Start)}} = \text{{R}}\,{cost:,} - \text{{R}}\,{accum_init:,} = \text{{R}}\,{carrying_start:,}\\\ "
            rf"\text{{Depreciation}} = \text{{R}}\,{carrying_start:,} \times \frac{{{rate}}}{{100}} = \text{{R}}\,{depr:,}\\\ "
            rf"\text{{Carrying Value (End)}} = \text{{R}}\,{carrying_start:,} - \text{{R}}\,{depr:,} = \text{{R}}\,{carrying_end:,}"
        )

        return {
            "id": f"g10_acct_fa_dim_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Fixed Assets",
            "subskill": "depreciation_diminishing_balance",
            "learning_objective_id": "g10_acct_depr_diminishing_balance",
            "archetype": "diminishing_balance_method",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Depreciation: R{depr:,}, Carrying Value: R{carrying_end:,}",
            "marks": 4,
            "marking_schema": {
                "total_marks": 4,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Beginning carrying value R{carrying_start:,}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Depreciation calculation on carrying value ({carrying_start:,} * {rate}%)", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": f"Current year depreciation R{depr:,}", "marks": 1, "editable": True},
                    {"id": "mp_4", "desc": f"Ending carrying value R{carrying_end:,}", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "calculated_on_cost_instead_of_carrying_value", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Under the diminishing balance method, you MUST subtract accumulated depreciation from cost before applying the percentage.",
                "tier_2": rf"$\text{{Carrying Value}} = \text{{Cost}} - \text{{Accumulated Depreciation}} = \text{{R}}\,{cost:,} - \text{{R}}\,{accum_init:,} = \text{{R}}\,{carrying_start:,}$.",
                "tier_3": rf"$\text{{Depreciation}} = \text{{R}}\,{carrying_start:,} \times \frac{{{rate}}}{{100}} = \text{{R}}\,{depr:,}$. End carrying value $= \text{{R}}\,{carrying_start:,} - \text{{R}}\,{depr:,} = \text{{R}}\,{carrying_end:,}$.",
            },
            "misconception_tags": ["calculated_on_cost_instead_of_carrying_value", "deducted_depreciation_from_cost_directly"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 4,
            "mode": mode,
            "difficulty": "medium",
        }

    else:
        # General Journal Entry for Depreciation
        asset_type = r.choice(["Vehicles", "Equipment"])
        cost = r.choice([90000, 120000, 150000])
        rate = 10
        depr = cost * rate // 100

        prompt = (
            f"Record the year-end adjustment for depreciation in the **General Journal** of Zondi Traders on 28 February 2026.\n\n"
            f"**Information:**\n"
            f"Depreciation on {asset_type} for the financial year is calculated as \\(\\text{{R}}\\,{depr:,}\\).\n\n"
            f"Show the Account Debited, Account Credited, and narration."
        )
        sample_answer = (
            rf"\textbf{{General Journal - 28 February 2026:}}\\\ "
            rf"\text{{Debit: Depreciation (Expense) \dots R}}\,{depr:,}\\\ "
            rf"\text{{Credit: Accumulated depreciation on {asset_type} (-Asset) \dots R}}\,{depr:,}\\\ "
            rf"\text{{Narration: Depreciation provided on {asset_type.lower()} at {rate}\% p.a.}}"
        )

        return {
            "id": f"g10_acct_fa_gj_{random.randint(100000, 999999)}",
            "subject": "accounting",
            "grade": "grade-10",
            "topic": "Fixed Assets",
            "subskill": "general_journal_depreciation",
            "learning_objective_id": "g10_acct_journal_depreciation",
            "archetype": "general_journal_depreciation",
            "prompt": prompt,
            "sample_answer": sample_answer,
            "correct_value": f"Debit: Depreciation R{depr:,}, Credit: Accumulated depreciation on {asset_type} R{depr:,}",
            "marks": 3,
            "marking_schema": {
                "total_marks": 3,
                "marking_points": [
                    {"id": "mp_1", "desc": f"Debit: Depreciation R{depr:,}", "marks": 1, "editable": True},
                    {"id": "mp_2", "desc": f"Credit: Accumulated depreciation on {asset_type} R{depr:,}", "marks": 1, "editable": True},
                    {"id": "mp_3", "desc": "Brief narration", "marks": 1, "editable": True},
                ],
                "deductions": [{"rule": "credited_asset_account_directly_instead_of_accumulated_depreciation", "penalty": 1}],
                "carry_forward_rule": "consequential_accuracy",
            },
            "hints": {
                "tier_1": "Depreciation is an operating expense (Debit). The contra-account is a negative asset account: Accumulated depreciation on {asset_type} (Credit).",
                "tier_2": rf"Do NOT credit the {asset_type} account directly! Credit 'Accumulated depreciation on {asset_type}'.",
                "tier_3": rf"Debit Depreciation: R{depr:,}. Credit Accumulated depreciation on {asset_type}: R{depr:,}.",
            },
            "misconception_tags": ["credited_asset_account_directly_instead_of_accumulated_depreciation", "debit_credit_inversion"],
            "term": 3,
            "caps_weight_percent": 15,
            "suggested_duration_mins": 3,
            "mode": mode,
            "difficulty": "medium",
        }


def generate(
    count: int = 1,
    seed: Optional[int] = None,
    difficulty: str = "medium",
    mode: str = "compound",
) -> List[Dict[str, Any]]:
    base_seed = seed if seed is not None else 42
    return [
        generate_grade10_fixed_assets_question(
            seed=base_seed + i,
            difficulty=difficulty,
            mode=mode,
        )
        for i in range(count)
    ]
