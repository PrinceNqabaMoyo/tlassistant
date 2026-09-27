"""
Grade 10-12 Life Sciences - Genetics & Inheritance Generator
100% Deterministic Punnett Square and Monohybrid Cross generator producing infinite unique genetics problems.
"""

from __future__ import annotations

import random
from typing import Any, Dict, List, Optional


def _rng(seed: Optional[int] = None) -> random.Random:
    r = random.Random()
    if seed is not None:
        r.seed(int(seed))
    return r


TRAIT_BANK = [
    {
        "trait": "pea plant height",
        "dominant_allele": "T",
        "dominant_pheno": "tall",
        "recessive_allele": "t",
        "recessive_pheno": "short",
        "organism": "pea plant"
    },
    {
        "trait": "seed color",
        "dominant_allele": "Y",
        "dominant_pheno": "yellow",
        "recessive_allele": "y",
        "recessive_pheno": "green",
        "organism": "pea plant"
    },
    {
        "trait": "guinea pig fur color",
        "dominant_allele": "B",
        "dominant_pheno": "black",
        "recessive_allele": "b",
        "recessive_pheno": "white",
        "organism": "guinea pig"
    },
    {
        "trait": "fruit fly eye color",
        "dominant_allele": "R",
        "dominant_pheno": "red eyes",
        "recessive_allele": "r",
        "recessive_pheno": "white eyes",
        "organism": "fruit fly (Drosophila)"
    },
]


def generate_monohybrid_cross(r: random.Random, mode: str = "scaffold") -> Dict[str, Any]:
    """Generates a complete monohybrid genetic cross problem with Punnett square solution."""
    trait_info = r.choice(TRAIT_BANK)
    
    # Possible cross configurations
    crosses = [
        {"p1": "heterozygous", "p2": "heterozygous", "p1_geno": "Bb", "p2_geno": "Bb", "pheno_ratio": "3:1", "dom_pct": 75, "rec_pct": 25},
        {"p1": "heterozygous", "p2": "homozygous recessive", "p1_geno": "Bb", "p2_geno": "bb", "pheno_ratio": "1:1", "dom_pct": 50, "rec_pct": 50},
        {"p1": "homozygous dominant", "p2": "homozygous recessive", "p1_geno": "BB", "p2_geno": "bb", "pheno_ratio": "4:0 (100% dominant)", "dom_pct": 100, "rec_pct": 0},
    ]
    cross = r.choice(crosses)

    dom_let = trait_info["dominant_allele"]
    rec_let = trait_info["recessive_allele"]

    # Adapt letter to trait
    p1_geno = cross["p1_geno"].replace("B", dom_let).replace("b", rec_let)
    p2_geno = cross["p2_geno"].replace("B", dom_let).replace("b", rec_let)

    prompt = (
        f"In {trait_info['organism']}s, the allele for {trait_info['dominant_pheno']} ({dom_let}) is dominant "
        f"over the allele for {trait_info['recessive_pheno']} ({rec_let}). "
        f"A {cross['p1']} {trait_info['organism']} is crossed with a {cross['p2']} {trait_info['organism']}.\n\n"
        f"Use a genetic cross diagram (or Punnett square) to determine the phenotypic ratio and probability of producing a {trait_info['recessive_pheno']} offspring."
    )

    sample_answer = (
        f"P1 Phenotype: {trait_info['dominant_pheno']} × {trait_info['recessive_pheno'] if 'recessive' in cross['p2'] else trait_info['dominant_pheno']}\n"
        f"P1 Genotype: {p1_geno} × {p2_geno}\n"
        f"Meiosis / Gametes: ({p1_geno[0]}, {p1_geno[1]}) × ({p2_geno[0]}, {p2_geno[1]})\n"
        f"F1 Phenotypic Ratio: {cross['pheno_ratio']}\n"
        f"Probability of {trait_info['recessive_pheno']} offspring: {cross['rec_pct']}%"
    )

    return {
        "id": f"ls_genetics_{r.randint(100000, 999999)}",
        "topic": "Life Sciences Genetics",
        "subskill": "monohybrid_cross",
        "term": 1,
        "caps_weight_percent": 30,
        "suggested_duration_mins": 10,
        "prompt": prompt,
        "sample_answer": sample_answer,
        "ideal_answer": f"Phenotypic ratio: {cross['pheno_ratio']}; Probability: {cross['rec_pct']}%",
        "marks": 6,
        "misconception_tags": ["confuses_phenotype_genotype", "dominant_recessive_inversion", "incorrect_gamete_separation"],
        "marking_schema": {
            "total_marks": 6,
            "marking_points": [
                {"id": "mp_p1_pheno", "desc": "P1 phenotype and genotype stated correctly", "marks": 1, "editable": True},
                {"id": "mp_meiosis", "desc": "Meiosis indicated with separated gametes", "marks": 1, "editable": True},
                {"id": "mp_punnett", "desc": "Correct Punnett square / fertilization grid", "marks": 2, "editable": True},
                {"id": "mp_f1_ratio", "desc": f"F1 phenotypic ratio: {cross['pheno_ratio']}", "marks": 1, "editable": True},
                {"id": "mp_prob", "desc": f"Probability percentage: {cross['rec_pct']}%", "marks": 1, "editable": True}
            ],
            "deductions": [{"rule": "missing_meiosis_label", "penalty": -1}],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": f"Write down the parental genotypes: Heterozygous = {dom_let}{rec_let}, Homozygous = {dom_let}{dom_let} or {rec_let}{rec_let}.",
            "2_concept": "Separate the alleles during Meiosis into gametes before setting up the 2x2 Punnett square.",
            "3_breakdown": f"Cross {p1_geno} × {p2_geno}. The offspring genotypes yield a {cross['pheno_ratio']} ratio ({cross['rec_pct']}% {trait_info['recessive_pheno']})."
        }
    }


def generate(subskill: str = "monohybrid_cross", count: int = 1, mode: str = "scaffold", seed: Optional[int] = None, **kwargs) -> List[Dict[str, Any]]:
    r = _rng(seed)
    return [generate_monohybrid_cross(r, mode=mode) for _ in range(count)]
