"""Grade 12 Mathematical Literacy: MEASURING WEIGHT, BMI AND MEDICINE DOSAGES.
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 2 Measurement:
1. Adult Body Mass Index (BMI) Calculations & Classifications (Subskills 01–08)
2. Child Growth Curves & BMI-for-Age Percentiles (Subskills 09–16)
3. Height & Weight Percentile Charts & Growth Benchmarks (Subskills 17–24)
4. Basal Metabolic Rate (BMR) & Ideal Body Weight Formulas (Subskills 25–32)
5. Pediatric Dosing Regimens & Liquid Suspensions (Subskills 33–40)
6. Historical Dosage Rules & Body Surface Area (BSA) Dosing (Subskills 41–46)
7. Clinical Dispensing, IV Flow Rates & Nutrition Calculations (Subskills 47–52)
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .adult_bmi_calculations import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .child_growth_bmi_percentiles import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .height_weight_percentiles import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .bmr_ideal_weight import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .pediatric_dosing_suspensions import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .dosage_rules_bsa import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .clinical_dispensing_iv_rates import (
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
)

BUILDERS: List[Callable[[random.Random], Dict[str, Any]]] = [
    gen_subskill_01, gen_subskill_02, gen_subskill_03, gen_subskill_04,
    gen_subskill_05, gen_subskill_06, gen_subskill_07, gen_subskill_08,
    gen_subskill_09, gen_subskill_10, gen_subskill_11, gen_subskill_12,
    gen_subskill_13, gen_subskill_14, gen_subskill_15, gen_subskill_16,
    gen_subskill_17, gen_subskill_18, gen_subskill_19, gen_subskill_20,
    gen_subskill_21, gen_subskill_22, gen_subskill_23, gen_subskill_24,
    gen_subskill_25, gen_subskill_26, gen_subskill_27, gen_subskill_28,
    gen_subskill_29, gen_subskill_30, gen_subskill_31, gen_subskill_32,
    gen_subskill_33, gen_subskill_34, gen_subskill_35, gen_subskill_36,
    gen_subskill_37, gen_subskill_38, gen_subskill_39, gen_subskill_40,
    gen_subskill_41, gen_subskill_42, gen_subskill_43, gen_subskill_44,
    gen_subskill_45, gen_subskill_46, gen_subskill_47, gen_subskill_48,
    gen_subskill_49, gen_subskill_50, gen_subskill_51, gen_subskill_52,
]

SUBSKILLS = [
    # 01-08: Adult BMI Calculations & Classifications
    "01_adult_bmi_from_weight_and_height",
    "02_adult_bmi_cm_to_m_conversion",
    "03_adult_who_bmi_classification",
    "04_imperial_units_bmi_conversion",
    "05_reverse_bmi_obesity_weight_threshold",
    "06_target_weight_loss_overweight_to_normal",
    "07_target_weight_gain_underweight_to_healthy",
    "08_limitations_of_bmi_athletes_elderly",
    # 09-16: Child Growth Curves & BMI-for-Age Percentiles
    "09_girls_bmi_for_age_percentile_reading",
    "10_boys_bmi_for_age_percentile_reading",
    "11_child_underweight_classification_under_5th",
    "12_child_healthy_weight_5th_to_85th",
    "13_child_at_risk_overweight_85th_to_95th",
    "14_child_overweight_ge_95th",
    "15_age_vs_bmi_identical_value_different_status",
    "16_percentile_longitudinal_curve_tracking",
    # 17-24: Height & Weight Percentile Charts
    "17_boys_stature_for_age_percentile",
    "18_girls_stature_for_age_percentile",
    "19_boys_weight_for_age_percentile",
    "20_girls_weight_for_age_percentile",
    "21_statistical_percentile_interpretation",
    "22_median_benchmark_50th_percentile_curve",
    "23_identifying_stunted_growth_height_deficit",
    "24_identifying_acute_wasting_weight_deficit",
    # 25-32: BMR & Ideal Body Weight
    "25_bmr_calculation_female_formula",
    "26_bmr_calculation_male_formula",
    "27_aging_metabolic_rate_decline_effect",
    "28_tdee_physical_activity_multiplier",
    "29_caloric_deficit_weight_loss_fat_reduction",
    "30_robinson_ideal_body_weight_women",
    "31_robinson_ideal_body_weight_men",
    "32_biological_limitations_ideal_weight_formulas",
    # 33-40: Pediatric Dosing Regimens & Liquid Suspensions
    "33_pediatric_single_dose_mg_per_kg",
    "34_daily_dose_divided_into_intervals",
    "35_suspension_volume_120mg_per_5ml",
    "36_suspension_volume_250mg_per_5ml",
    "37_maximum_safe_daily_dose_ceiling_check",
    "38_measuring_syringe_selection_and_increments",
    "39_doses_per_medicine_bottle_calculation",
    "40_bottles_needed_for_completed_antibiotic_course",
    # 41-46: Dosage Rules & Body Surface Area
    "41_clarks_rule_child_dose_kg",
    "42_clarks_rule_child_dose_pounds",
    "43_youngs_rule_child_dose_years",
    "44_frieds_rule_infant_dose_months",
    "45_bsa_dosage_calculation",
    "46_clarks_vs_youngs_weight_superiority",
    # 47-52: Clinical Dispensing, IV Flow Rates & Nutrition
    "47_iv_drip_rate_drops_per_minute",
    "48_iv_infusion_duration_total_hours",
    "49_powdered_suspension_reconstitution_dilution",
    "50_oral_rehydration_salts_mixing_ratio",
    "51_macronutrient_energy_kj_and_kcal",
    "52_pediatric_outpatient_clinic_quotation",
]

DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {
    i + 1: b for i, b in enumerate(BUILDERS)
}

# String key aliases
for i, b in enumerate(BUILDERS):
    DISPATCH_TABLE[f"gr12_bmi_{i+1:02d}"] = b
    DISPATCH_TABLE[f"gr12_bmi_subskill_{i+1:02d}"] = b
    DISPATCH_TABLE[SUBSKILLS[i]] = b

SUBSKILLS_METADATA = {
    f"gr12_bmi_{i+1:02d}": {
        "index": i + 1,
        "name": SUBSKILLS[i],
        "category": (
            "Adult BMI Calculations" if i < 8 else
            "Child Growth BMI Percentiles" if i < 16 else
            "Height & Weight Percentiles" if i < 24 else
            "BMR & Ideal Weight" if i < 32 else
            "Pediatric Dosing & Suspensions" if i < 40 else
            "Dosage Rules & BSA" if i < 46 else
            "Clinical Dispensing & IV Rates"
        ),
    }
    for i in range(len(SUBSKILLS))
}
