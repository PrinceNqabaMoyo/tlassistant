"""Grade 12 Life Sciences — Dihybrid Crosses & Pedigree Chart Analysis (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 2 — 25 to 30 marks):
- Dihybrid Genetic Cross (Mendel's Law of Independent Assortment, Punnett square, phenotypic ratios).
- Multi-generation Pedigree Chart analysis with Claim-Evidence-Reasoning (CER) proving autosomal recessive/dominant traits.
Supports full compound exam questions and atomic elementary sub-drills for adaptive deconstruction.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


DIHYBRID_TRAITS = [
    {
        "organism": "pea plant",
        "trait1": "seed shape",
        "t1_dom_allele": "R",
        "t1_dom_name": "Round",
        "t1_rec_allele": "r",
        "t1_rec_name": "wrinkled",
        "trait2": "seed colour",
        "t2_dom_allele": "Y",
        "t2_dom_name": "Yellow",
        "t2_rec_allele": "y",
        "t2_rec_name": "green",
    },
    {
        "organism": "guinea pig",
        "trait1": "fur colour",
        "t1_dom_allele": "B",
        "t1_dom_name": "Black",
        "t1_rec_allele": "b",
        "t1_rec_name": "brown",
        "trait2": "fur texture",
        "t2_dom_allele": "S",
        "t2_dom_name": "Short hair",
        "t2_rec_allele": "s",
        "t2_rec_name": "long hair",
    },
    {
        "organism": "fruit fly (Drosophila)",
        "trait1": "body colour",
        "t1_dom_allele": "G",
        "t1_dom_name": "Grey body",
        "t1_rec_allele": "g",
        "t1_rec_name": "ebony body",
        "trait2": "wing shape",
        "t2_dom_allele": "N",
        "t2_dom_name": "Normal wings",
        "t2_rec_allele": "n",
        "t2_rec_name": "vestigial wings",
    },
    {
        "organism": "tomato plant",
        "trait1": "stem height",
        "t1_dom_allele": "T",
        "t1_dom_name": "Tall stem",
        "t1_rec_allele": "t",
        "t1_rec_name": "dwarf stem",
        "trait2": "fruit shape",
        "t2_dom_allele": "R",
        "t2_dom_name": "Round fruit",
        "t2_rec_allele": "r",
        "t2_rec_name": "pear-shaped fruit",
    },
    {
        "organism": "corn (Zea mays)",
        "trait1": "kernel texture",
        "t1_dom_allele": "S",
        "t1_dom_name": "Starchy kernel",
        "t1_rec_allele": "s",
        "t1_rec_name": "sweet kernel",
        "trait2": "kernel colour",
        "t2_dom_allele": "P",
        "t2_dom_name": "Purple kernel",
        "t2_rec_allele": "p",
        "t2_rec_name": "yellow kernel",
    },
    {
        "organism": "rabbit",
        "trait1": "coat colour",
        "t1_dom_allele": "A",
        "t1_dom_name": "Agouti coat",
        "t1_rec_allele": "a",
        "t1_rec_name": "albino coat",
        "trait2": "ear length",
        "t2_dom_allele": "L",
        "t2_dom_name": "Long ears",
        "t2_rec_allele": "l",
        "t2_rec_name": "short ears",
    },
    {
        "organism": "house mouse (Mus musculus)",
        "trait1": "coat pigmentation",
        "t1_dom_allele": "B",
        "t1_dom_name": "Black fur",
        "t1_rec_allele": "b",
        "t1_rec_name": "brown fur",
        "trait2": "running behaviour",
        "t2_dom_allele": "R",
        "t2_dom_name": "Running normally",
        "t2_rec_allele": "r",
        "t2_rec_name": "waltzing behaviour",
    },
    {
        "organism": "sweet pea (Lathyrus)",
        "trait1": "flower colour",
        "t1_dom_allele": "P",
        "t1_dom_name": "Purple flowers",
        "t1_rec_allele": "p",
        "t1_rec_name": "red flowers",
        "trait2": "pollen shape",
        "t2_dom_allele": "L",
        "t2_dom_name": "Long pollen grains",
        "t2_rec_allele": "l",
        "t2_rec_name": "round pollen grains",
    },
    {
        "organism": "bell pepper (Capsicum)",
        "trait1": "fruit colour",
        "t1_dom_allele": "R",
        "t1_dom_name": "Red fruit",
        "t1_rec_allele": "r",
        "t1_rec_name": "yellow fruit",
        "trait2": "pungency",
        "t2_dom_allele": "H",
        "t2_dom_name": "Hot (pungent)",
        "t2_rec_allele": "h",
        "t2_rec_name": "sweet (mild)",
    },
    {
        "organism": "domestic cat",
        "trait1": "hair length",
        "t1_dom_allele": "S",
        "t1_dom_name": "Short hair",
        "t1_rec_allele": "s",
        "t1_rec_name": "long hair",
        "trait2": "tail presence",
        "t2_dom_allele": "T",
        "t2_dom_name": "Normal tail",
        "t2_rec_allele": "t",
        "t2_rec_name": "tailless (Manx)",
    },
    {
        "organism": "summer squash (Cucurbita)",
        "trait1": "fruit shape",
        "t1_dom_allele": "D",
        "t1_dom_name": "Disc-shaped fruit",
        "t1_rec_allele": "d",
        "t1_rec_name": "sphere-shaped fruit",
        "trait2": "fruit colour",
        "t2_dom_allele": "W",
        "t2_dom_name": "White fruit",
        "t2_rec_allele": "w",
        "t2_rec_name": "yellow fruit",
    },
    {
        "organism": "domestic fowl (chicken)",
        "trait1": "comb type",
        "t1_dom_allele": "R",
        "t1_dom_name": "Rose comb",
        "t1_rec_allele": "r",
        "t1_rec_name": "single comb",
        "trait2": "feather morphology",
        "t2_dom_allele": "F",
        "t2_dom_name": "Frizzled feathers",
        "t2_rec_allele": "f",
        "t2_rec_name": "plain feathers",
    },
    {
        "organism": "barley plant (Hordeum)",
        "trait1": "head awn type",
        "t1_dom_allele": "A",
        "t1_dom_name": "Awned spikes",
        "t1_rec_allele": "a",
        "t1_rec_name": "hooded spikes",
        "trait2": "row number",
        "t2_dom_allele": "V",
        "t2_dom_name": "Two-rowed",
        "t2_rec_allele": "v",
        "t2_rec_name": "six-rowed",
    },
    {
        "organism": "snapdragon (Antirrhinum)",
        "trait1": "flower morphology",
        "t1_dom_allele": "B",
        "t1_dom_name": "Broad petals",
        "t1_rec_allele": "b",
        "t1_rec_name": "narrow petals",
        "trait2": "plant habit",
        "t2_dom_allele": "H",
        "t2_dom_name": "Tall habit",
        "t2_rec_allele": "h",
        "t2_rec_name": "bushy habit",
    },
    {
        "organism": "shepherd's purse (Capsella)",
        "trait1": "capsule shape",
        "t1_dom_allele": "T",
        "t1_dom_name": "Triangular capsule",
        "t1_rec_allele": "t",
        "t1_rec_name": "ovoid capsule",
        "trait2": "flower size",
        "t2_dom_allele": "L",
        "t2_dom_name": "Large petals",
        "t2_rec_allele": "l",
        "t2_rec_name": "small petals",
    },
    {
        "organism": "sunflower (Helianthus annuus)",
        "trait1": "disc flower colour",
        "t1_dom_allele": "B",
        "t1_dom_name": "Brown centre",
        "t1_rec_allele": "b",
        "t1_rec_name": "yellow centre",
        "trait2": "ray floret colour",
        "t2_dom_allele": "Y",
        "t2_dom_name": "Deep yellow",
        "t2_rec_allele": "y",
        "t2_rec_name": "pale primrose",
    },
    {
        "organism": "garden pea (Pisum sativum)",
        "trait1": "pod shape",
        "t1_dom_allele": "I",
        "t1_dom_name": "Inflated pod",
        "t1_rec_allele": "i",
        "t1_rec_name": "constricted pod",
        "trait2": "pod colour",
        "t2_dom_allele": "G",
        "t2_dom_name": "Green pod",
        "t2_rec_allele": "g",
        "t2_rec_name": "yellow pod",
    },
]

PEDIGREE_CONDITIONS = [
    {"name": "albinism", "allele_rec": "a", "allele_dom": "A", "type": "autosomal recessive", "affected_trait": "albinism (aa)", "normal_trait": "normal pigmentation"},
    {"name": "cystic fibrosis", "allele_rec": "f", "allele_dom": "F", "type": "autosomal recessive", "affected_trait": "cystic fibrosis (ff)", "normal_trait": "unaffected"},
    {"name": "sickle cell anaemia", "allele_rec": "s", "allele_dom": "S", "type": "autosomal recessive", "affected_trait": "sickle cell anaemia (ss)", "normal_trait": "normal red blood cells"},
    {"name": "Tay-Sachs disease", "allele_rec": "t", "allele_dom": "T", "type": "autosomal recessive", "affected_trait": "Tay-Sachs (tt)", "normal_trait": "unaffected"},
    {"name": "Huntington's disease", "allele_rec": "h", "allele_dom": "H", "type": "autosomal dominant", "affected_trait": "Huntington's disease (Hh or HH)", "normal_trait": "unaffected (hh)"},
]


def _get_gametes(geno: str) -> List[str]:
    """Derives unique or all 4 gametes from a 4-letter dihybrid genotype (e.g. RrYy)."""
    t1_1, t1_2, t2_1, t2_2 = geno[0], geno[1], geno[2], geno[3]
    return [
        f"{t1_1}{t2_1}",
        f"{t1_1}{t2_2}",
        f"{t1_2}{t2_1}",
        f"{t1_2}{t2_2}",
    ]


# --------------------------------------------------------------------------- #
# Sub-Drill: Dihybrid Gamete Formation
# --------------------------------------------------------------------------- #
def _build_gamete_drill(r: random.Random) -> Dict[str, Any]:
    t = r.choice(DIHYBRID_TRAITS)
    combos = [
        ("heterozygous for both traits", f"{t['t1_dom_allele']}{t['t1_rec_allele']}{t['t2_dom_allele']}{t['t2_rec_allele']}"),
        ("homozygous dominant for trait 1 and heterozygous for trait 2", f"{t['t1_dom_allele']}{t['t1_dom_allele']}{t['t2_dom_allele']}{t['t2_rec_allele']}"),
        ("heterozygous for trait 1 and homozygous recessive for trait 2", f"{t['t1_dom_allele']}{t['t1_rec_allele']}{t['t2_rec_allele']}{t['t2_rec_allele']}"),
        ("homozygous recessive for both traits", f"{t['t1_rec_allele']}{t['t1_rec_allele']}{t['t2_rec_allele']}{t['t2_rec_allele']}"),
    ]
    desc, geno = r.choice(combos)
    raw_gametes = _get_gametes(geno)
    distinct_gametes = sorted(list(set(raw_gametes)))
    gamete_str = ", ".join(distinct_gametes)

    prompt = (
        f"In {t['organism']}s, consider the following alleles:\n"
        f"• {t['t1_dom_allele']}: {t['t1_dom_name']} (dominant) | {t['t1_rec_allele']}: {t['t1_rec_name']} (recessive)\n"
        f"• {t['t2_dom_allele']}: {t['t2_dom_name']} (dominant) | {t['t2_rec_allele']}: {t['t2_rec_name']} (recessive)\n\n"
        f"State all the possible distinct gametes that can be produced by an individual with genotype **{geno}** ({desc}) "
        f"according to Mendel's Law of Independent Assortment."
    )

    return {
        "id": f"life_gametes_{r.randint(100000, 999999)}",
        "topic": "Genetics & Inheritance",
        "subskill": "elementary_dihybrid_gametes",
        "mode": "elementary_dihybrid_gametes",
        "term": 2,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 4,
        "prompt": prompt,
        "ideal_answer": gamete_str,
        "sample_answer": f"Gametes: {gamete_str}",
        "marks": 3,
        "misconception_tags": ["paired_alleles_in_gametes", "omitted_gamete_combinations"],
        "marking_schema": {
            "total_marks": 3,
            "marking_points": [
                {"id": "mp1", "desc": "Each gamete contains only ONE allele for each gene", "marks": 1, "editable": True},
                {"id": "mp2", "desc": f"All distinct gametes listed correctly: {gamete_str}", "marks": 2, "editable": True}
            ],
            "deductions": [{"rule": "diploid_gamete_error", "penalty": -1}],
            "carry_forward_rule": "strict"
        },
        "hints": {
            "1_nudge": "Use the FOIL method (First, Outside, Inside, Last) to pair one allele from the first gene with one allele from the second gene.",
            "2_concept": "Mendel's Law of Independent Assortment: alleles for separate traits segregate independently during meiosis.",
            "3_breakdown": f"From {geno}, the possible distinct combinations are: {gamete_str}."
        }
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Pedigree Genotype Deduction
# --------------------------------------------------------------------------- #
def _build_pedigree_drill(r: random.Random) -> Dict[str, Any]:
    cond = r.choice(PEDIGREE_CONDITIONS)
    p1_idx = r.choice([1, 3, 5])
    p2_idx = p1_idx + 1
    child_idx = p2_idx + r.choice([2, 3, 4])

    if "recessive" in cond["type"]:
        dom = cond["allele_dom"]
        rec = cond["allele_rec"]
        prompt = (
            f"In a pedigree chart tracing {cond['name']} ({cond['type']} condition caused by allele '{rec}'):\n\n"
            f"Two unaffected parents (Individual {p1_idx} and Individual {p2_idx}) have a child (Individual {child_idx}) with {cond['name']} (genotype '{rec}{rec}').\n\n"
            f"1. Write down the genotypes of Individual {p1_idx} and Individual {p2_idx}.\n"
            f"2. Explain how you deduced their genotypes from the pedigree chart using Claim-Evidence-Reasoning."
        )
        sample = (
            f"1. Genotype of Individual {p1_idx}: {dom}{rec} | Genotype of Individual {p2_idx}: {dom}{rec}\n"
            f"2. Explanation: Because child {child_idx} has {cond['name']} ({rec}{rec}), they must have inherited one recessive allele ({rec}) from each parent. "
            f"Since both parents are unaffected, each parent must also possess a dominant allele ({dom}). Therefore, both parents are heterozygous carriers ({dom}{rec})."
        )
        ideal = f"Parents are heterozygous carriers ({dom}{rec})."
        p_geno = f"{dom}{rec}"
    else:
        dom = cond["allele_dom"]
        rec = cond["allele_rec"]
        prompt = (
            f"In a pedigree chart tracing {cond['name']} ({cond['type']} condition caused by allele '{dom}'):\n\n"
            f"An affected parent (Individual {p1_idx}) and an unaffected parent (Individual {p2_idx}, genotype '{rec}{rec}') have an unaffected child (Individual {child_idx}, genotype '{rec}{rec}').\n\n"
            f"1. State the genotype of Individual {p1_idx}.\n"
            f"2. Explain why Individual {p1_idx} cannot be homozygous dominant ({dom}{dom})."
        )
        sample = (
            f"1. Genotype of Individual {p1_idx}: {dom}{rec}\n"
            f"2. Explanation: Child {child_idx} is unaffected ({rec}{rec}) and received one '{rec}' from Individual {p2_idx} and one '{rec}' from Individual {p1_idx}. "
            f"If Individual {p1_idx} were homozygous dominant ({dom}{dom}), all offspring would inherit '{dom}' and be affected."
        )
        ideal = f"Individual {p1_idx} is heterozygous ({dom}{rec})."
        p_geno = f"{dom}{rec}"

    return {
        "id": f"life_ped_deduct_{r.randint(100000, 999999)}",
        "topic": "Genetics & Inheritance",
        "subskill": "elementary_pedigree_genotype_deduction",
        "mode": "elementary_pedigree_genotype_deduction",
        "term": 2,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": ideal,
        "sample_answer": sample,
        "marks": 4,
        "misconception_tags": ["assumed_parent_homozygous_dominant", "omitted_carrier_reasoning"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": f"Correct parent genotype: {p_geno}", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Offspring phenotype evidence correctly linked to allele segregation", "marks": 2, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": f"Inspect the genotype of child {child_idx}. Each parent contributed exactly one allele to this child.",
            "2_concept": "Recessive traits require two recessive alleles. If unaffected parents have an affected child, both parents must carry the hidden recessive allele.",
            "3_breakdown": f"The child inherits one recessive allele from each parent. Genotype must be {p_geno}."
        }
    }


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Complete Dihybrid Cross with Punnett Square
# --------------------------------------------------------------------------- #
def _build_compound_dihybrid_cross(r: random.Random) -> Dict[str, Any]:
    t = r.choice(DIHYBRID_TRAITS)
    cross_types = [
        "dihybrid_hetero",
        "testcross",
        "reciprocal_testcross",
        "hetero_homo_t2",
        "hetero_homo_t1",
        "hetero_homo_dominant"
    ]
    cross_type = r.choice(cross_types)

    t1_D, t1_d = t["t1_dom_allele"], t["t1_rec_allele"]
    t2_D, t2_d = t["t2_dom_allele"], t["t2_rec_allele"]

    sample_counts = [160, 240, 320, 480, 640, 800, 960, 1120, 1280, 1600]
    n_offspring = r.choice(sample_counts)

    trial_code = f"TR-{r.randint(101, 899)}"
    contexts = [
        f"In breeding trial {trial_code} with {t['organism']}s",
        f"During an agricultural genetics experiment (Trial {trial_code}) investigating {t['organism']}s",
        f"A biological research team investigating trait inheritance (Series {trial_code}) in {t['organism']}s",
        f"Learners conducting an empirical study (Investigation {trial_code}) on {t['organism']} phenotypes",
        f"In an experiment ({trial_code}) testing Mendel's Law of Independent Assortment in {t['organism']}s",
        f"A researcher studying dihybrid inheritance patterns (Project {trial_code}) in {t['organism']}s",
    ]
    ctx = r.choice(contexts)

    if cross_type == "dihybrid_hetero":
        p1_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p2_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p1_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        p2_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        ratio_str = f"9 {t['t1_dom_name']} {t['t2_dom_name']} : 3 {t['t1_dom_name']} {t['t2_rec_name']} : 3 {t['t1_rec_name']} {t['t2_dom_name']} : 1 {t['t1_rec_name']} {t['t2_rec_name']}"
        ratio_summary = "9 : 3 : 3 : 1"
        target_prob = "1/16"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = int(n_offspring * (1 / 16))
    elif cross_type == "testcross":
        p1_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p2_geno = f"{t1_d}{t1_d}{t2_d}{t2_d}"
        p1_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        p2_pheno = f"{t['t1_rec_name']}, {t['t2_rec_name']}"
        ratio_str = f"1 {t['t1_dom_name']} {t['t2_dom_name']} : 1 {t['t1_dom_name']} {t['t2_rec_name']} : 1 {t['t1_rec_name']} {t['t2_dom_name']} : 1 {t['t1_rec_name']} {t['t2_rec_name']}"
        ratio_summary = "1 : 1 : 1 : 1"
        target_prob = "1/4 (25%)"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = int(n_offspring * (1 / 4))
    elif cross_type == "reciprocal_testcross":
        p1_geno = f"{t1_d}{t1_d}{t2_d}{t2_d}"
        p2_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p1_pheno = f"{t['t1_rec_name']}, {t['t2_rec_name']}"
        p2_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        ratio_str = f"1 {t['t1_dom_name']} {t['t2_dom_name']} : 1 {t['t1_dom_name']} {t['t2_rec_name']} : 1 {t['t1_rec_name']} {t['t2_dom_name']} : 1 {t['t1_rec_name']} {t['t2_rec_name']}"
        ratio_summary = "1 : 1 : 1 : 1"
        target_prob = "1/4 (25%)"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = int(n_offspring * (1 / 4))
    elif cross_type == "hetero_homo_t2":
        p1_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p2_geno = f"{t1_D}{t1_d}{t2_d}{t2_d}"
        p1_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        p2_pheno = f"{t['t1_dom_name']}, {t['t2_rec_name']}"
        ratio_str = f"3 {t['t1_dom_name']} {t['t2_dom_name']} : 3 {t['t1_dom_name']} {t['t2_rec_name']} : 1 {t['t1_rec_name']} {t['t2_dom_name']} : 1 {t['t1_rec_name']} {t['t2_rec_name']}"
        ratio_summary = "3 : 3 : 1 : 1"
        target_prob = "1/8 (12,5%)"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = int(n_offspring * (1 / 8))
    elif cross_type == "hetero_homo_t1":
        p1_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p2_geno = f"{t1_d}{t1_d}{t2_D}{t2_d}"
        p1_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        p2_pheno = f"{t['t1_rec_name']}, {t['t2_dom_name']}"
        ratio_str = f"3 {t['t1_dom_name']} {t['t2_dom_name']} : 1 {t['t1_dom_name']} {t['t2_rec_name']} : 3 {t['t1_rec_name']} {t['t2_dom_name']} : 1 {t['t1_rec_name']} {t['t2_rec_name']}"
        ratio_summary = "3 : 1 : 3 : 1"
        target_prob = "1/8 (12,5%)"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = int(n_offspring * (1 / 8))
    else: # hetero_homo_dominant
        p1_geno = f"{t1_D}{t1_d}{t2_D}{t2_d}"
        p2_geno = f"{t1_D}{t1_D}{t2_D}{t2_d}"
        p1_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        p2_pheno = f"{t['t1_dom_name']}, {t['t2_dom_name']}"
        ratio_str = f"3 {t['t1_dom_name']} {t['t2_dom_name']} : 1 {t['t1_dom_name']} {t['t2_rec_name']}"
        ratio_summary = "3 : 1"
        target_prob = "0/16 (0%)"
        target_trait_name = f"{t['t1_rec_name']} and {t['t2_rec_name']}"
        expected_count = 0

    p1_gametes = _get_gametes(p1_geno)
    p2_gametes = _get_gametes(p2_geno)

    p1_gametes_str = ", ".join(sorted(list(set(p1_gametes))))
    p2_gametes_str = ", ".join(sorted(list(set(p2_gametes))))

    prompt = (
        f"{ctx}, consider the inheritance of two traits:\n"
        f"• {t['trait1'].capitalize()}: {t1_D} ({t['t1_dom_name']}, dominant) is dominant over {t1_d} ({t['t1_rec_name']}, recessive).\n"
        f"• {t['trait2'].capitalize()}: {t2_D} ({t['t2_dom_name']}, dominant) is dominant over {t2_d} ({t['t2_rec_name']}, recessive).\n\n"
        f"A parent with genotype **{p1_geno}** ({p1_pheno}) is crossed with a parent of genotype **{p2_geno}** ({p2_pheno}). "
        f"A total of {n_offspring} offspring are produced in the F1 generation.\n\n"
        f"1. State the phenotype of both parent organisms (P1). (2 marks)\n"
        f"2. Write down all the possible gametes produced by each parent. (2 marks)\n"
        f"3. Use a Punnett square to determine the possible genotypes and phenotypes of the offspring (F1). (4 marks)\n"
        f"4. State the expected **phenotypic ratio** of the offspring. (2 marks)\n"
        f"5. Calculate the expected number of offspring that will display {target_trait_name}. (2 marks)"
    )

    sample_answer = (
        f"**1. P1 Phenotypes:**\n"
        f"• Parent 1: {p1_pheno}\n"
        f"• Parent 2: {p2_pheno}\n\n"
        f"**2. Gametes:**\n"
        f"• Parent 1 ({p1_geno}): {p1_gametes_str}\n"
        f"• Parent 2 ({p2_geno}): {p2_gametes_str}\n\n"
        f"**3. Offspring Genotypes & Phenotypes:** Determined via Punnett square combining gametes from P1 and P2.\n\n"
        f"**4. Expected Phenotypic Ratio:**\n"
        f"{ratio_str} ({ratio_summary}).\n\n"
        f"**5. Expected Number of Offspring ({target_trait_name}):**\n"
        f"Probability = {target_prob}\n"
        f"Expected count = {target_prob} × {n_offspring} = {expected_count} offspring."
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            {"id": "mp_p1_pheno", "desc": f"Correct P1 phenotypes ({p1_pheno} and {p2_pheno})", "marks": 2, "editable": True},
            {"id": "mp_gametes", "desc": f"Correct gametes for both parents ({p1_gametes_str} | {p2_gametes_str})", "marks": 2, "editable": True},
            {"id": "mp_punnett", "desc": "Punnett square correctly constructed and populated with genotypes", "marks": 4, "editable": True},
            {"id": "mp_ratio", "desc": f"Correct phenotypic ratio: {ratio_summary}", "marks": 2, "editable": True}
        ],
        "deductions": [{"rule": "omitted_phenotypes_in_ratio", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy"
    }

    return {
        "id": f"life_dihybrid_{t['organism'][:3]}_{r.randint(100000, 999999)}",
        "topic": "Genetics & Inheritance",
        "subskill": "dihybrid_cross_compound",
        "mode": "compound",
        "difficulty": "hard",
        "term": 2,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 14,
        "prompt": prompt,
        "ideal_answer": f"Phenotypic ratio: {ratio_summary} ({ratio_str})",
        "sample_answer": sample_answer,
        "marks": 10,
        "misconception_tags": ["confused_monohybrid_dihybrid_ratio", "incorrect_gametes_in_punnett", "omitted_phenotypes_in_ratio"],
        "marking_schema": marking_schema,
        "hints": {
            "1_nudge": f"Write down all possible gametes produced by Parent 1 ({p1_geno}) and Parent 2 ({p2_geno}). Then cross them in a grid.",
            "2_concept": "Mendel's Law of Independent Assortment: alleles for separate gene pairs segregate into gametes independently.",
            "3_breakdown": f"Parent 1 gametes: {p1_gametes_str}. Parent 2 gametes: {p2_gametes_str}. Resulting phenotypic ratio: {ratio_summary}."
        }
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_dihybrid_cross,
    "dihybrid": _build_compound_dihybrid_cross,
    "dihybrid_cross_compound": _build_compound_dihybrid_cross,
    "elementary_dihybrid_gametes": _build_gamete_drill,
    "elementary_pedigree_genotype_deduction": _build_pedigree_drill,
    "pedigree": _build_pedigree_drill,
}


def generate(
    subskill: Optional[str] = None,
    difficulty: str = "hard",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    **kwargs: Any,
) -> Dict[str, Any]:
    """Generates deterministic Grade 12 Life Sciences Dihybrid and Pedigree questions."""
    base_seed = 42 if seed is None else int(seed)
    chosen_mode = mode if mode in BUILDERS else ("compound" if subskill is None else subskill)
    builder = BUILDERS.get(chosen_mode, _build_compound_dihybrid_cross)

    questions = []
    for i in range(max(1, count)):
        r = _rng(base_seed * 1000 + i)
        q = builder(r)
        q["seed"] = base_seed * 1000 + i
        questions.append(q)

    return {"questions": questions}
