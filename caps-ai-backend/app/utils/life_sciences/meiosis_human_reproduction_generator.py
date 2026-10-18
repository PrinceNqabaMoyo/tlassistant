"""Grade 12 Life Sciences — Meiosis & Human Reproduction (Deterministic 6-Pillar Generator).
Grounding:
- curriculum_docs_auto/LifeSciences_Gr12/Term 1/03. Meiosis.md (Term 1)
- curriculum_docs_auto/LifeSciences_Gr12/Term 2/01. Human Reproduction.md (Term 2)

Complies strictly with the 6-Pillar Generator Contract:
1. Term & Calendar Metadata: Declares term=1 (Meiosis) or term=2 (Human Reproduction), caps_weight_percent, suggested_duration_mins.
2. Deconstructibility: Compound exam scenarios and atomic elementary sub-drills (elementary_meiosis_phases, elementary_chromosome_counts, elementary_menstrual_hormones, elementary_gametogenesis).
3. Standardized Misconceptions: anaphase1_vs_anaphase2_confusion, mitosis_vs_meiosis_ploidy, lh_vs_fsh_inversion, progesterone_maintenance_confusion, non_disjunction_mechanism.
4. Teacher-Editable Marking Schema: explicit marking points with marks and carry_forward_rule.
5. Deterministic 3-Tier Pre-Baked Hints: Tier 1 (nudge), Tier 2 (directional rule), Tier 3 (worked step).
6. Modality: Scientific inquiry, MCQ and structured short analytical answers with South African decimal conventions.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

TOPIC = "life_sciences_meiosis_human_reproduction"

ORGANISMS_CYTOGENETICS = [
    {"name": "human (Homo sapiens)", "diploid": 46, "haploid": 23, "autosome_pairs": 22, "gonosomes": "XX (female) or XY (male)"},
    {"name": "fruit fly (Drosophila melanogaster)", "diploid": 8, "haploid": 4, "autosome_pairs": 3, "gonosomes": "XX (female) or XY (male)"},
    {"name": "garden pea (Pisum sativum)", "diploid": 14, "haploid": 7, "autosome_pairs": 6, "gonosomes": "homomorphic"},
    {"name": "chimpanzee (Pan troglodytes)", "diploid": 48, "haploid": 24, "autosome_pairs": 23, "gonosomes": "XX or XY"},
    {"name": "domestic dog (Canis lupus familiaris)", "diploid": 78, "haploid": 39, "autosome_pairs": 38, "gonosomes": "XX or XY"},
    {"name": "house mouse (Mus musculus)", "diploid": 40, "haploid": 20, "autosome_pairs": 19, "gonosomes": "XX or XY"},
]

HORMONES_DB = [
    {
        "name": "Follicle Stimulating Hormone (FSH)",
        "gland": "Hypophysis (Anterior Pituitary)",
        "target": "Ovary (Graafian follicle)",
        "function": "Stimulates the development of a primary follicle into a mature Graafian follicle and stimulates secretion of oestrogen.",
        "cycle_phase": "Follicular phase (Days 1–13)"
    },
    {
        "name": "Luteinizing Hormone (LH)",
        "gland": "Hypophysis (Anterior Pituitary)",
        "target": "Ovary (Mature follicle)",
        "function": "A sudden surge in LH triggers ovulation (release of ovum) around Day 14 and stimulates formation of the corpus luteum.",
        "cycle_phase": "Ovulatory phase (Day 14)"
    },
    {
        "name": "Oestrogen",
        "gland": "Developing Graafian follicle in ovary",
        "target": "Endometrium of the uterus",
        "function": "Repairs and thickens the endometrium lining after menstruation, and inhibits FSH secretion via negative feedback.",
        "cycle_phase": "Proliferative phase (Days 6–13)"
    },
    {
        "name": "Progesterone",
        "gland": "Corpus luteum in ovary (and later placenta)",
        "target": "Endometrium of the uterus",
        "function": "Maintains the thickened, vascular, glandular endometrium for implantation and inhibits FSH and LH secretion.",
        "cycle_phase": "Luteal / Secretory phase (Days 15–28)"
    }
]

PROMPT_LEAD_HOOKS_MEIOSIS = [
    "During an investigation of gametogenesis in a secondary school Life Sciences laboratory,",
    "A cytogeneticist examines stained micrographs of dividing testicular germ cells,",
    "An exam question paper provides a schematic diagram of a diploid cell undergoing reduction division,",
    "In a study examining sources of genetic variation in sexually reproducing organisms,",
    "A clinical cytogenetics lab analyzes a karyotype prepared from an amniocentesis fluid sample,"
]

PROMPT_LEAD_HOOKS_REPRO = [
    "A clinical endocrinologist monitors the circulating ovarian hormone concentrations in a patient,",
    "In an examination of human reproductive biology,",
    "A health science study assesses the physiological interactions between pituitary and ovarian hormones,",
    "During a medical diagnostic ultrasound of the female pelvic organs on day 14 of the cycle,",
    "A reproductive physiologist analyzes the process of gametogenesis and fertilisation in humans,"
]


def _make_id(prefix: str, seed: Optional[int], idx: int) -> str:
    s_val = seed if seed is not None else random.randint(1000, 9999)
    return f"{prefix}_{s_val}_{idx}"


def _generate_meiosis_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Generates CAPS Term 1 Meiosis question (6-pillar contract)."""
    org = r.choice(ORGANISMS_CYTOGENETICS)
    hook = r.choice(PROMPT_LEAD_HOOKS_MEIOSIS)
    qid = _make_id("ls12_meiosis", seed, idx)

    archetype = r.choice(["phases_crossing_over", "chromosome_arithmetic", "non_disjunction", "anaphase_distinction"])
    if mode == "elementary_meiosis_phases":
        archetype = "phases_crossing_over"
    elif mode == "elementary_chromosome_counts":
        archetype = "chromosome_arithmetic"

    if archetype == "phases_crossing_over":
        prompt = (
            f"{hook} the cytological process of meiotic division is analyzed in {org['name']} somatic and germinal cells.\n\n"
            f"1. State the specific phase of Meiosis during which crossing over occurs.\n"
            f"2. Name the point of contact where non-sister chromatids overlap and exchange genetic segments.\n"
            f"3. Explain the biological significance of crossing over for sexually reproducing populations.\n"
            f"4. State whether the daughter cells produced at the completion of Telophase II are diploid or haploid."
        )
        ans_str = "1. Prophase I; 2. Chiasma (plural: chiasmata); 3. Generates genetic variation; 4. Haploid"
        memo = (
            "1. Prophase I. [1]\n"
            "2. Chiasma / chiasmata. [1]\n"
            "3. Crossing over results in exchange of DNA segments between homologous maternal and paternal chromosomes, "
            "producing recombinant chromatids with novel allele combinations, increasing genetic variation. [2]\n"
            "4. Haploid (n). [1]"
        )
        hints = {
            "tier_1": "Crossing over happens in the first meiotic prophase. Gametes have half the chromosomes of somatic cells.",
            "tier_2": "Prophase I is characterized by bivalent pairing and chiasmata formation. It introduces new allele combinations (genetic variation).",
            "tier_3": "1. Prophase I. 2. Chiasma. 3. Recombinant chromatids create genetic variation. 4. Haploid.",
        }
        marks = 5
        misconceptions = ["anaphase1_vs_anaphase2_confusion", "mitosis_vs_meiosis_ploidy"]

    elif archetype == "chromosome_arithmetic":
        diploid = org["diploid"]
        haploid = org["haploid"]
        autosomes = org["autosome_pairs"] * 2
        prompt = (
            f"{hook} the chromosome complement of {org['name']} is documented as 2n = {diploid}.\n\n"
            f"1. How many autosomes are present in a normal somatic cell of this organism?\n"
            f"2. How many chromosomes are present in a mature gamete (sperm cell or ovum)?\n"
            f"3. State the number of chromosome pairs aligned on the equatorial plate during Metaphase I.\n"
            f"4. How many individual chromatids are present in a single cell during Metaphase II?"
        )
        ans_str = f"1. {autosomes}; 2. {haploid}; 3. {haploid} homologous pairs; 4. {diploid} chromatids"
        memo = (
            f"1. {autosomes} autosomes ({org['autosome_pairs']} pairs, excluding 2 sex chromosomes). [1]\n"
            f"2. {haploid} chromosomes (haploid n = {diploid}/2). [1]\n"
            f"3. {haploid} bivalent homologous pairs. [1]\n"
            f"4. {diploid} chromatids ({haploid} replicated chromosomes each with 2 chromatids = {diploid}). [2]"
        )
        hints = {
            "tier_1": "Somatic cells have 2n chromosomes (autosomes + 2 sex chromosomes). Gametes have n.",
            "tier_2": "Autosomes = 2n - 2. Metaphase I has n pairs. In Metaphase II, each of the n chromosomes still has 2 sister chromatids.",
            "tier_3": f"1. {autosomes}. 2. {haploid}. 3. {haploid} pairs. 4. {diploid} chromatids.",
        }
        marks = 5
        misconceptions = ["mitosis_vs_meiosis_ploidy", "anaphase1_vs_anaphase2_confusion"]

    elif archetype == "non_disjunction":
        prompt = (
            f"{hook} an abnormality occurs during Anaphase I of human meiosis where homologous chromosome pair 21 fails to separate.\n\n"
            "1. Name this cytological failure of chromosomes or chromatids to separate during anaphase.\n"
            "2. State the number of chromosomes present in a gamete resulting from this non-disjunction event.\n"
            "3. Name the genetic disorder that results when an abnormal gamete with 24 chromosomes is fertilised by a normal sperm cell (23 chromosomes).\n"
            "4. Differentiate between autosomes and gonosomes in a human karyotype."
        )
        ans_str = "1. Non-disjunction; 2. 24 or 22 chromosomes; 3. Down syndrome (Trisomy 21); 4. Autosomes (pairs 1-22) control general body traits; gonosomes (pair 23) determine biological sex."
        memo = (
            "1. Non-disjunction. [1]\n"
            "2. 24 chromosomes (n + 1) or 22 chromosomes (n - 1). [2]\n"
            "3. Down syndrome / Trisomy 21 (resulting zygote has 47 chromosomes). [1]\n"
            "4. Autosomes are the first 22 pairs of homologous chromosomes that control somatic body traits [1]; gonosomes are the 23rd pair (XX or XY) that determines sex [1]."
        )
        hints = {
            "tier_1": "Failure to separate is non-disjunction. Trisomy 21 causes Down syndrome.",
            "tier_2": "Non-disjunction produces n+1 (24) or n-1 (22) gametes. Autosomes are pairs 1-22, gonosomes are XX/XY.",
            "tier_3": "1. Non-disjunction. 2. 24 or 22. 3. Down syndrome. 4. Autosomes = pairs 1-22; gonosomes = pair 23.",
        }
        marks = 6
        misconceptions = ["non_disjunction_mechanism", "mitosis_vs_meiosis_ploidy"]

    else:
        # anaphase_distinction
        prompt = (
            f"{hook} the mechanical differences between Meiosis I and Meiosis II are examined.\n\n"
            "1. What structures separate and move to opposite poles during Anaphase I?\n"
            "2. What structures separate and move to opposite poles during Anaphase II?\n"
            "3. State whether centromeres divide during Anaphase I or Anaphase II.\n"
            "4. Explain why Meiosis I is termed a 'reduction division' whereas Meiosis II is an 'equational division'."
        )
        ans_str = "1. Homologous chromosome pairs; 2. Sister chromatids; 3. Anaphase II; 4. Meiosis I halves chromosome number from diploid (2n) to haploid (n); Meiosis II maintains haploid count while separating chromatids."
        memo = (
            "1. Homologous chromosomes / chromosome pairs separate in Anaphase I. [1]\n"
            "2. Sister chromatids separate in Anaphase II. [1]\n"
            "3. Centromeres divide in Anaphase II (they do not divide in Anaphase I). [1]\n"
            "4. In Meiosis I, the diploid (2n) number is reduced to haploid (n) [1]; in Meiosis II, the number of chromosomes remains haploid (n), resembling mitosis [1]."
        )
        hints = {
            "tier_1": "In Meiosis I, pairs separate. In Meiosis II, individual chromatids separate.",
            "tier_2": "Anaphase I pulls whole replicated chromosomes apart without splitting centromeres. Anaphase II splits centromeres and separates sister chromatids.",
            "tier_3": "1. Homologous chromosomes. 2. Sister chromatids. 3. Anaphase II. 4. 2n -> n in Meiosis I.",
        }
        marks = 5
        misconceptions = ["anaphase1_vs_anaphase2_confusion"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 1,
        "caps_weight_percent": 14,
        "suggested_duration_mins": 10,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Phase / terminology identification", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Cytological mechanism description", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Biological significance / reasoning", "marks": marks - 4, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def _generate_human_reproduction_question(r: random.Random, seed: Optional[int], idx: int, mode: str) -> Dict[str, Any]:
    """Generates CAPS Term 2 Human Reproduction question (6-pillar contract)."""
    hook = r.choice(PROMPT_LEAD_HOOKS_REPRO)
    qid = _make_id("ls12_human_repro", seed, idx)

    archetype = r.choice(["hormonal_menstrual_cycle", "gametogenesis_comparison", "fertilisation_implantation"])
    if mode == "elementary_menstrual_hormones":
        archetype = "hormonal_menstrual_cycle"
    elif mode == "elementary_gametogenesis":
        archetype = "gametogenesis_comparison"

    if archetype == "hormonal_menstrual_cycle":
        target_hormone = r.choice(HORMONES_DB)
        day_ovulation = 14
        prompt = (
            f"{hook} the hormonal regulation of the 28-day human female menstrual cycle is analyzed.\n\n"
            f"1. Identify the endocrine gland that secretes {target_hormone['name']}.\n"
            f"2. State the primary physiological target and function of {target_hormone['name']}.\n"
            f"3. Name the hormone whose sharp surge directly triggers ovulation on approximately Day {day_ovulation}.\n"
            f"4. Describe what happens to the level of progesterone if fertilisation does NOT occur after ovulation, and state the uterine consequence."
        )
        ans_str = f"1. {target_hormone['gland']}; 2. {target_hormone['function']}; 3. Luteinizing Hormone (LH); 4. Progesterone levels drop, corpus luteum degenerates, endometrium breaks down causing menstruation."
        memo = (
            f"1. {target_hormone['gland']}. [1]\n"
            f"2. Target: {target_hormone['target']} [1]; Function: {target_hormone['function']} [1].\n"
            f"3. Luteinizing Hormone (LH). [1]\n"
            "4. The corpus luteum degenerates, causing progesterone levels to decrease sharply [1]; without progesterone, the endometrium cannot be maintained and sloughs off, resulting in menstruation [1]."
        )
        hints = {
            "tier_1": "Pituitary hormones are FSH and LH. Ovarian hormones are oestrogen and progesterone.",
            "tier_2": "LH surge triggers ovulation. High progesterone maintains the endometrium; when it drops, menstruation begins.",
            "tier_3": f"1. {target_hormone['gland']}. 2. {target_hormone['target']}. 3. LH surge triggers ovulation. 4. Progesterone falls -> menstruation.",
        }
        marks = 6
        misconceptions = ["lh_vs_fsh_inversion", "progesterone_maintenance_confusion"]

    elif archetype == "gametogenesis_comparison":
        prompt = (
            f"{hook} the cytological processes of spermatogenesis and oogenesis are compared.\n\n"
            "1. Name the specific anatomical site where spermatogenesis takes place in the male body.\n"
            "2. State the number of functional gametes produced from one primary spermatocyte versus one primary oocyte.\n"
            "3. State the ploidy of a secondary spermatocyte.\n"
            "4. Explain why unequal division of cytoplasm during cytokinesis in oogenesis is biologically advantageous."
        )
        ans_str = "1. Seminiferous tubules of the testes; 2. 4 functional sperm vs 1 functional ovum (and 3 polar bodies); 3. Haploid (n); 4. Concentrates food/nutrient reserves in the single ovum to nourish the early embryo before implantation."
        memo = (
            "1. Seminiferous tubules (in the testes). [1]\n"
            "2. Spermatogenesis produces 4 functional sperm cells [1]; oogenesis produces 1 functional ovum and 3 non-functional polar bodies [1].\n"
            "3. Haploid (n). [1]\n"
            "4. Unequal cytokinesis ensures that the single ovum receives almost all the cytoplasm, yolk, and nutrients necessary to support cell division and sustain the zygote until implantation [2]."
        )
        hints = {
            "tier_1": "Sperm develop in the testes' tubules. Eggs need enough cytoplasm to feed the zygote.",
            "tier_2": "Spermatogenesis produces 4 equal sperm. Oogenesis yields 1 large egg and small polar bodies so the ovum has rich food stores.",
            "tier_3": "1. Seminiferous tubules. 2. 4 sperm vs 1 ovum. 3. Haploid. 4. Provides nutrients for early embryonic development.",
        }
        marks = 6
        misconceptions = ["mitosis_vs_meiosis_ploidy"]

    else:
        # fertilisation_implantation
        prompt = (
            f"{hook} the sequence of events from ovulation to early embryonic gestation is tracked.\n\n"
            "1. In which specific part of the female reproductive tract does fertilisation normally occur?\n"
            "2. Name the hollow ball of cells formed by mitotic cleavage of the zygote before implantation.\n"
            "3. Name the hormone secreted by the developing placenta that maintains the corpus luteum during early pregnancy.\n"
            "4. Define the term 'implantation'."
        )
        ans_str = "1. Fallopian tube (oviduct); 2. Blastocyst; 3. Human Chorionic Gonadotropin (hCG); 4. The attachment of the blastocyst to the thickened endometrium lining of the uterus."
        memo = (
            "1. Fallopian tube / oviduct. [1]\n"
            "2. Blastocyst / blastula. [1]\n"
            "3. Human Chorionic Gonadotropin (hCG) (or progesterone). [1]\n"
            "4. Implantation is the process where the blastocyst attaches to and embeds into the vascular endometrium wall of the uterus [2]."
        )
        hints = {
            "tier_1": "Fertilisation happens in the tubes. The embryo embeds into the uterine wall.",
            "tier_2": "Fertilisation occurs in the Fallopian tube. Cleavage creates a blastocyst which implants in the endometrium.",
            "tier_3": "1. Fallopian tube. 2. Blastocyst. 3. hCG. 4. Blastocyst embedding into endometrium.",
        }
        marks = 5
        misconceptions = ["progesterone_maintenance_confusion"]

    return {
        "id": qid,
        "question_id": qid,
        "term": 2,
        "caps_weight_percent": 18,
        "suggested_duration_mins": 10,
        "mode": mode,
        "topic": TOPIC,
        "question_type": "short_answer",
        "question": prompt,
        "correct_answer": ans_str,
        "sample_answer": ans_str,
        "worked_solution": memo,
        "explanation": memo,
        "marks": marks,
        "hints": hints,
        "misconception_tags": misconceptions,
        "marking_schema": {
            "total_marks": marks,
            "marking_points": [
                {"id": "mp_1", "desc": "Anatomical site and hormone identification", "marks": 2, "editable": True},
                {"id": "mp_2", "desc": "Physiological feedback / cycle mechanism", "marks": 2, "editable": True},
                {"id": "mp_3", "desc": "Developmental sequence / adaptations", "marks": marks - 4, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
    }


def generate(
    subskill: str = "mixed",
    difficulty: str = "medium",
    count: int = 1,
    seed: Optional[int] = None,
    mode: str = "compound",
    grade: str = "12",
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    """Master generator for Grade 12 Life Sciences Meiosis & Human Reproduction."""
    r = random.Random(seed) if seed is not None else random.Random()
    questions: List[Dict[str, Any]] = []

    for i in range(count):
        sub_seed = r.randint(1, 1_000_000_000)
        sub_r = random.Random(sub_seed)

        if subskill in ("meiosis", "crossing_over", "karyotype", "non_disjunction") or mode in ("elementary_meiosis_phases", "elementary_chromosome_counts"):
            q = _generate_meiosis_question(sub_r, sub_seed, i, mode)
        elif subskill in ("human_reproduction", "menstrual_cycle", "gametogenesis", "fertilisation") or mode in ("elementary_menstrual_hormones", "elementary_gametogenesis"):
            q = _generate_human_reproduction_question(sub_r, sub_seed, i, mode)
        else:
            # 50/50 distribution between Term 1 Meiosis and Term 2 Human Reproduction
            chosen = sub_r.choice(["meiosis", "repro"])
            if chosen == "meiosis":
                q = _generate_meiosis_question(sub_r, sub_seed, i, mode)
            else:
                q = _generate_human_reproduction_question(sub_r, sub_seed, i, mode)

        questions.append(q)

    return questions
