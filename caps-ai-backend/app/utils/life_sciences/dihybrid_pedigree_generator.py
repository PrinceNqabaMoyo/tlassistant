"""Grade 12 Life Sciences — Dihybrid Crosses & Pedigree Chart Analysis (Deterministic 6-Pillar Generator).
Covers official CAPS Examination standards (Paper 2 — 25 to 30 marks):
- Dihybrid Genetic Cross (Mendel's Law of Independent Assortment, 16-cell Punnett square, 9:3:3:1 phenotypic ratio).
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
    }
]


# --------------------------------------------------------------------------- #
# Sub-Drill: Dihybrid Gamete Formation
# --------------------------------------------------------------------------- #
def _build_gamete_drill(r: random.Random) -> Dict[str, Any]:
    t = r.choice(DIHYBRID_TRAITS)
    # Pick a genotype: RrYy, RRYy, RrYY, etc.
    genos = [
        ("heterozygous for both traits", f"{t['t1_dom_allele']}{t['t1_rec_allele']}{t['t2_dom_allele']}{t['t2_rec_allele']}", [
            f"{t['t1_dom_allele']}{t['t2_dom_allele']}",
            f"{t['t1_dom_allele']}{t['t2_rec_allele']}",
            f"{t['t1_rec_allele']}{t['t2_dom_allele']}",
            f"{t['t1_rec_allele']}{t['t2_rec_allele']}"
        ]),
        ("homozygous dominant for trait 1 and heterozygous for trait 2", f"{t['t1_dom_allele']}{t['t1_dom_allele']}{t['t2_dom_allele']}{t['t2_rec_allele']}", [
            f"{t['t1_dom_allele']}{t['t2_dom_allele']}",
            f"{t['t1_dom_allele']}{t['t2_rec_allele']}"
        ]),
    ]

    desc, geno, gametes = r.choice(genos)
    gamete_str = ", ".join(gametes)

    prompt = (
        f"In {t['organism']}s, consider the following alleles:\n"
        f"• {t['t1_dom_allele']}: {t['t1_dom_name']} (dominant) | {t['t1_rec_allele']}: {t['t1_rec_name']} (recessive)\n"
        f"• {t['t2_dom_allele']}: {t['t2_dom_name']} (dominant) | {t['t2_rec_allele']}: {t['t2_rec_name']} (recessive)\n\n"
        f"State all the possible gametes that can be produced by an individual with genotype **{geno}** ({desc}) "
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
            "1_nudge": "Use the FOIL method (First, Outside, Inside, Last) to combine one allele from the first gene with one allele from the second gene.",
            "2_concept": "Mendel's Law of Independent Assortment: alleles for separate traits segregate independently into gametes.",
            "3_breakdown": f"From {geno}, the possible combinations are: {gamete_str}."
        }
    }


# --------------------------------------------------------------------------- #
# Sub-Drill: Pedigree Genotype Deduction
# --------------------------------------------------------------------------- #
def _build_pedigree_drill(r: random.Random) -> Dict[str, Any]:
    prompt = (
        "In a pedigree chart tracing albinism (an autosomal recessive condition caused by allele 'a'):\n\n"
        "Two unaffected parents (Individuals 1 and 2) have an albino child (Individual 5, genotype 'aa').\n\n"
        "1. Write down the genotype of Individual 1 and Individual 2.\n"
        "2. Explain how you deduced their genotypes from the pedigree chart."
    )

    sample = (
        "1. Genotype of Individual 1: Aa | Genotype of Individual 2: Aa\n"
        "2. Explanation: Because child 5 has albinism (aa), she must have inherited one recessive allele (a) from each parent. "
        "Since both parents are unaffected, each parent must also possess a dominant normal allele (A). Therefore, both parents are heterozygous carriers (Aa)."
    )

    return {
        "id": f"life_ped_deduct_{r.randint(100000, 999999)}",
        "topic": "Genetics & Inheritance",
        "subskill": "elementary_pedigree_genotype_deduction",
        "mode": "elementary_pedigree_genotype_deduction",
        "term": 2,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 5,
        "prompt": prompt,
        "ideal_answer": "Parents are heterozygous carriers (Aa).",
        "sample_answer": sample,
        "marks": 4,
        "misconception_tags": ["assumed_parent_homozygous_dominant", "omitted_carrier_reasoning"],
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Genotype of Individual 1: Aa", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Genotype of Individual 2: Aa", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Child 5 inherits one 'a' allele from each parent", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Both parents are unaffected hence must carry dominant 'A'", "marks": 1, "editable": True}
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy"
        },
        "hints": {
            "1_nudge": "The affected child has genotype 'aa'. Where did each 'a' allele come from?",
            "2_concept": "Each parent contributes one allele. If unaffected parents have an affected child, both parents MUST be heterozygous carriers.",
            "3_breakdown": "Child is aa. Father contributes 'a' and Mother contributes 'a'. Since both look normal, each has 'A'. Genotypes: Aa and Aa."
        }
    }


# --------------------------------------------------------------------------- #
# Compound Level 3 & 4 Exam Question: Complete Dihybrid Cross with Punnett Square
# --------------------------------------------------------------------------- #
def _build_compound_dihybrid_cross(r: random.Random) -> Dict[str, Any]:
    t = DIHYBRID_TRAITS[0] # Pea plant: RrYy
    
    prompt = (
        f"In pea plants, the allele for round seeds ({t['t1_dom_allele']}) is dominant over wrinkled seeds ({t['t1_rec_allele']}), "
        f"and the allele for yellow seeds ({t['t2_dom_allele']}) is dominant over green seeds ({t['t2_rec_allele']}).\n\n"
        f"A plant that is **heterozygous for both seed shape and seed colour** is crossed with another plant of the same genotype.\n\n"
        f"1. State the phenotype of the parent plants (P1).\n"
        f"2. Write down the genotypes of the gametes produced by each parent.\n"
        f"3. Use a 16-cell Punnett square to determine the possible genotypes of the offspring (F1).\n"
        f"4. State the expected **phenotypic ratio** of the offspring."
    )

    punnett_table = (
        r"\begin{array}{|c|c|c|c|c|}"
        r"\hline"
        r"\text{Gametes} & \text{RY} & \text{Ry} & \text{rY} & \text{ry} \\ \hline"
        r"\text{RY} & \text{RRYY} & \text{RRYy} & \text{RrYY} & \text{RrYy} \\ \hline"
        r"\text{Ry} & \text{RRYy} & \text{RRyy} & \text{RrYy} & \text{Rryy} \\ \hline"
        r"\text{rY} & \text{RrYY} & \text{RrYy} & \text{rrYY} & \text{rrYy} \\ \hline"
        r"\text{ry} & \text{RrYy} & \text{Rryy} & \text{rrYy} & \text{rryy} \\ \hline"
        r"\end{array}"
    )

    sample_answer = (
        f"**1. P1 Phenotype:** Round yellow seeds x Round yellow seeds\n\n"
        f"**2. Gametes:** RY, Ry, rY, ry\n\n"
        f"**3. Punnett Square:**\n\n{punnett_table}\n\n"
        f"**4. Phenotypic Ratio (9:3:3:1):**\n"
        f"• 9 Round, Yellow\n"
        f"• 3 Round, green\n"
        f"• 3 wrinkled, Yellow\n"
        f"• 1 wrinkled, green"
    )

    marking_schema = {
        "total_marks": 10,
        "marking_points": [
            {"id": "mp_p1", "desc": "P1 phenotype: Round yellow seeds", "marks": 1, "editable": True},
            {"id": "mp_p1_geno", "desc": "P1 genotypes: RrYy x RrYy", "marks": 1, "editable": True},
            {"id": "mp_gametes", "desc": "Correct 4 gametes for each parent: RY, Ry, rY, ry", "marks": 2, "editable": True},
            {"id": "mp_punnett_grid", "desc": "16-cell Punnett square correctly populated", "marks": 4, "editable": True},
            {"id": "mp_ratio", "desc": "Correct phenotypic ratio: 9 Round Yellow : 3 Round green : 3 wrinkled Yellow : 1 wrinkled green", "marks": 2, "editable": True}
        ],
        "deductions": [{"rule": "omitted_phenotypes_in_ratio", "penalty": -1}],
        "carry_forward_rule": "consequential_accuracy"
    }

    return {
        "id": f"life_dihybrid_compound_{r.randint(100000, 999999)}",
        "topic": "Genetics & Inheritance",
        "subskill": "dihybrid_cross_compound",
        "mode": "compound",
        "difficulty": "hard",
        "term": 2,
        "caps_weight_percent": 25,
        "suggested_duration_mins": 14,
        "prompt": prompt,
        "ideal_answer": "9 Round Yellow : 3 Round green : 3 wrinkled Yellow : 1 wrinkled green (9:3:3:1)",
        "sample_answer": sample_answer,
        "marks": 10,
        "misconception_tags": ["confused_monohybrid_dihybrid_ratio", "incorrect_gametes_in_punnett", "omitted_phenotypes_in_ratio"],
        "marking_schema": marking_schema,
        "hints": {
            "1_nudge": "Each heterozygous parent produces 4 distinct gametes (RY, Ry, rY, ry). Set up a 4x4 Punnett square.",
            "2_concept": "Mendel's dihybrid F1 self-cross always yields a canonical 9:3:3:1 phenotypic ratio.",
            "3_breakdown": "Offspring summary: 9/16 Round Yellow, 3/16 Round green, 3/16 wrinkled Yellow, 1/16 wrinkled green."
        }
    }


# --------------------------------------------------------------------------- #
# Public Dispatcher
# --------------------------------------------------------------------------- #
BUILDERS = {
    "compound": _build_compound_dihybrid_cross,
    "elementary_dihybrid_gametes": _build_gamete_drill,
    "elementary_pedigree_genotype_deduction": _build_pedigree_drill,
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
