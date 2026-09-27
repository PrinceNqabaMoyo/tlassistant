"""
SimuLearn Animation Script Engine (Layer B)
Produces data-light (~2KB) declarative animation scripts for canonical worked examples.
Replays step-by-step cursor moves, cell typing, formula expansions, and conceptual callouts
at 0.1% the data cost of streaming video.
"""

from typing import Dict, Any, List, Optional


CANONICAL_SCRIPTS: Dict[str, Dict[str, Any]] = {
    # 1. Accounting / EMS: Cash Receipts Journal & VAT Split
    "accounting_crj_vat": {
        "archetype": "crj_vat_split",
        "title": "Recording Cash Sales with 15% VAT in the CRJ",
        "subject": "Accounting",
        "total_duration_ms": 12000,
        "grid_type": "journal_table",
        "headers": ["Day", "Details", "Bank (Gross)", "Sales (Excl)", "VAT (15%)", "Cost of Sales"],
        "frames": [
            {
                "time_ms": 0,
                "action": "highlight_prompt",
                "target": "prompt_text",
                "narrative": "Transaction: Sold merchandise for R1,150 cash. Cost of sales is R800. (VAT rate is 15%)."
            },
            {
                "time_ms": 2500,
                "action": "type_cell",
                "cell_id": "r0_c0",
                "value": "12",
                "label": "Day of transaction",
                "narrative": "Record the date (12) in the Day column."
            },
            {
                "time_ms": 4500,
                "action": "type_cell",
                "cell_id": "r0_c1",
                "value": "Cash",
                "label": "Details column",
                "narrative": "Details is 'Cash' (or CRT for cash register tape)."
            },
            {
                "time_ms": 6500,
                "action": "type_cell",
                "cell_id": "r0_c2",
                "value": "1150.00",
                "label": "Bank Gross (VAT Inclusive)",
                "narrative": "Bank always receives the total gross cash amount: R1,150.00."
            },
            {
                "time_ms": 8500,
                "action": "formula_callout",
                "latex": r"\text{Sales (Excl)} = 1150 \times \frac{100}{115} = 1000.00",
                "narrative": "Extract VAT: Divide gross by 1.15 to find net Sales of R1,000.00."
            },
            {
                "time_ms": 10000,
                "action": "type_cell",
                "cell_id": "r0_c3",
                "value": "1000.00",
                "label": "Sales Column (Exclusive)",
                "narrative": "Record R1,000.00 in Sales and R150.00 in Output VAT."
            }
        ]
    },

    # 2. Mathematics: Quadratic Trinomial Factorisation
    "math_quadratic_trinomial": {
        "archetype": "quadratic_factorisation",
        "title": "Factorising a Quadratic Trinomial: x² + 5x + 6",
        "subject": "Mathematics",
        "total_duration_ms": 10000,
        "grid_type": "stepwise_math",
        "frames": [
            {
                "time_ms": 0,
                "action": "show_expression",
                "latex": "x^2 + 5x + 6",
                "narrative": "Goal: Factorise the trinomial into two binomial brackets (x + a)(x + b)."
            },
            {
                "time_ms": 2500,
                "action": "formula_callout",
                "latex": r"\text{Find two numbers } a, b \text{ where } a \cdot b = 6 \text{ and } a + b = 5",
                "narrative": "Step 1: Look for factors of the constant term (+6) that add up to the middle coefficient (+5)."
            },
            {
                "time_ms": 5500,
                "action": "show_step",
                "latex": r"2 \times 3 = 6 \quad \text{and} \quad 2 + 3 = 5",
                "narrative": "Step 2: The factor pair is +2 and +3."
            },
            {
                "time_ms": 8000,
                "action": "final_solution",
                "latex": "(x + 2)(x + 3)",
                "narrative": "Step 3: Write the factorised form: (x + 2)(x + 3)."
            }
        ]
    },

    # 3. Physical Sciences: Kinematics 1D Motion
    "physics_kinematics_dx": {
        "archetype": "kinematics_1d",
        "title": "Applying the Displacement Equation: Δx = v_i Δt + ½ a Δt²",
        "subject": "Physical Sciences",
        "total_duration_ms": 11000,
        "grid_type": "stepwise_math",
        "frames": [
            {
                "time_ms": 0,
                "action": "list_knowns",
                "latex": r"v_i = 10\text{ m/s}, \quad a = 2\text{ m/s}^2, \quad \Delta t = 4\text{ s}",
                "narrative": "Step 1: Write down all known variables from the problem statement."
            },
            {
                "time_ms": 3000,
                "action": "show_formula",
                "latex": r"\Delta x = v_i \Delta t + \frac{1}{2} a \Delta t^2",
                "narrative": "Step 2: Select the kinematic formula connecting vi, a, and Δt to displacement Δx."
            },
            {
                "time_ms": 6500,
                "action": "substitute_values",
                "latex": r"\Delta x = (10)(4) + \frac{1}{2}(2)(4)^2 = 40 + (1)(16)",
                "narrative": "Step 3: Substitute the known values. Remember to square the time (4² = 16) first."
            },
            {
                "time_ms": 9500,
                "action": "final_solution",
                "latex": r"\Delta x = 56\text{ m}",
                "narrative": "Step 4: Compute the final displacement: 56 metres."
            }
        ]
    },

    # 4. Life Sciences: Monohybrid Genetic Cross (Punnett Square)
    "lifesciences_punnett_square": {
        "archetype": "monohybrid_cross",
        "title": "Monohybrid Genetic Cross: Heterozygous Parents (Bb × Bb)",
        "subject": "Life Sciences",
        "total_duration_ms": 12000,
        "grid_type": "punnett_grid",
        "headers": ["Gametes", "B", "b"],
        "frames": [
            {
                "time_ms": 0,
                "action": "highlight_prompt",
                "latex": r"\text{Parents: } Bb \times Bb \quad (\text{Brown eyes dominant to blue})",
                "narrative": "Parental genotypes: Both parents are heterozygous (Bb)."
            },
            {
                "time_ms": 2500,
                "action": "type_cell",
                "cell_id": "r0_c0",
                "value": "BB",
                "label": "Top-left: B from Mother, B from Father",
                "narrative": "Square 1: Homozygous Dominant (BB) - Brown phenotype."
            },
            {
                "time_ms": 5000,
                "action": "type_cell",
                "cell_id": "r0_c1",
                "value": "Bb",
                "label": "Top-right: B from Mother, b from Father",
                "narrative": "Square 2: Heterozygous (Bb) - Brown phenotype."
            },
            {
                "time_ms": 7500,
                "action": "type_cell",
                "cell_id": "r1_c0",
                "value": "Bb",
                "label": "Bottom-left: b from Mother, B from Father",
                "narrative": "Square 3: Heterozygous (Bb) - Brown phenotype."
            },
            {
                "time_ms": 9500,
                "action": "type_cell",
                "cell_id": "r1_c1",
                "value": "bb",
                "label": "Bottom-right: b from Mother, b from Father",
                "narrative": "Square 4: Homozygous Recessive (bb) - Blue phenotype."
            },
            {
                "time_ms": 11000,
                "action": "final_solution",
                "latex": r"\text{Phenotypic Ratio: } 3\text{ Brown} : 1\text{ Blue} \quad (75\% : 25\%)",
                "narrative": "Summary: 3 : 1 phenotypic ratio (75% probability of dominant trait)."
            }
        ]
    },

    # 5. Mathematical Literacy: SARS Income Tax Calculation
    "mathlit_sars_income_tax": {
        "archetype": "sars_income_tax",
        "title": "SARS Personal Income Tax & Rebates Calculation",
        "subject": "Mathematical Literacy",
        "total_duration_ms": 11000,
        "grid_type": "stepwise_math",
        "frames": [
            {
                "time_ms": 0,
                "action": "list_knowns",
                "latex": r"\text{Taxable Income} = \text{R}300{,}000, \quad \text{Age} = 34 \text{ (Primary Rebate: R}17{,}235\text{)}",
                "narrative": "Income falls in Tax Bracket 2 (R237,101 – R370,500): R42,678 + 26% of amount above R237,100."
            },
            {
                "time_ms": 3000,
                "action": "show_formula",
                "latex": r"\text{Tax before rebate} = 42{,}678 + 0{,}26 \times (300{,}000 - 237{,}100)",
                "narrative": "Step 1: Calculate tax on amount exceeding the bracket threshold: R300,000 - R237,100 = R62,900."
            },
            {
                "time_ms": 6500,
                "action": "substitute_values",
                "latex": r"\text{Tax before rebate} = 42{,}678 + 16{,}354 = \text{R}59{,}032",
                "narrative": "Step 2: Base tax R42,678 + Marginal portion R16,354 = R59,032 gross tax."
            },
            {
                "time_ms": 9500,
                "action": "final_solution",
                "latex": r"\text{Final Tax Payable} = 59{,}032 - 17{,}235 = \text{R}41{,}797\text{ per annum}",
                "narrative": "Step 3: Deduct Primary Rebate of R17,235 to arrive at final annual tax payable: R41,797 (R3,483.08/mo)."
            }
        ]
    }
}


def get_simulearn_script(archetype_key: str) -> Optional[Dict[str, Any]]:
    """Returns the canonical animation script for an archetype, or a general fallback."""
    if archetype_key in CANONICAL_SCRIPTS:
        return CANONICAL_SCRIPTS[archetype_key]
    
    # Fuzzy match by subject prefix
    key_lower = archetype_key.lower()
    if "math" in key_lower:
        return CANONICAL_SCRIPTS["math_quadratic_trinomial"]
    elif "physic" in key_lower or "science" in key_lower:
        return CANONICAL_SCRIPTS["physics_kinematics_dx"]
    elif "life" in key_lower or "bio" in key_lower:
        return CANONICAL_SCRIPTS["lifesciences_punnett_square"]
    elif "tax" in key_lower or "lit" in key_lower:
        return CANONICAL_SCRIPTS["mathlit_sars_income_tax"]
    
    return CANONICAL_SCRIPTS["accounting_crj_vat"]


def list_available_simulations() -> List[Dict[str, Any]]:
    """Lists metadata for all canonical simulation scripts."""
    return [
        {
            "key": k,
            "title": v["title"],
            "subject": v["subject"],
            "archetype": v["archetype"],
            "duration_ms": v["total_duration_ms"],
            "frameCount": len(v["frames"])
        }
        for k, v in CANONICAL_SCRIPTS.items()
    ]
