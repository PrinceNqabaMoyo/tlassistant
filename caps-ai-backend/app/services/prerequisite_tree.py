"""
Prerequisite Tree Service — Cross-Grade Prerequisite Lineage & Adaptive Descent
==============================================================================
Defines the cross-grade dependency graph across grades 7–12 for Mathematics,
Commercial Sciences (EMS/Accounting), and Natural/Physical Sciences.

Enforces Vertical Slicing:
When a student in Grade 11 struggles on a compound topic (e.g. Quadratic Equations),
this service enables the adaptive progression engine to step down the grade ladder
(Grade 10 Trinomials -> Grade 9 Common Factors -> Grade 8 Directed Integers -> Grade 7 Number Bonds)
rather than endlessly drilling the failing compound question.
"""

from typing import Dict, Any, List, Optional

# Declarative Cross-Grade Dependency Graph
# Key: (subject_normalized, grade_str, topic_normalized)
PREREQUISITE_GRAPH: Dict[str, Dict[str, Any]] = {
    # ── Grade 12 Mathematics ──
    "mathematics:12:calculus": {
        "target_grade": "11",
        "target_topic": "Functions",
        "target_subskill": "parabola_hyperbola_exponential",
        "gap_title": "Function graphs & average gradient (Grade 11)",
        "explanation": "Calculus limits and first derivatives require solid fluency in algebraic function notation, tangents, and average gradients.",
        "micro_drill_title": "Grade 11 Function Gradient Micro-Drill",
        "route": "grade11_functions_practice",
    },
    "mathematics:12:differential calculus": {
        "target_grade": "11",
        "target_topic": "Functions",
        "target_subskill": "parabola_hyperbola_exponential",
        "gap_title": "Function graphs & average gradient (Grade 11)",
        "explanation": "Calculus limits and first derivatives require solid fluency in algebraic function notation, tangents, and average gradients.",
        "micro_drill_title": "Grade 11 Function Gradient Micro-Drill",
        "route": "grade11_functions_practice",
    },
    "mathematics:12:trigonometry": {
        "target_grade": "11",
        "target_topic": "Trigonometry",
        "target_subskill": "reduction_formulae",
        "gap_title": "Trig reduction formulae & identities (Grade 11)",
        "explanation": "Grade 12 compound and double-angle formulas expand on Grade 11 CAST diagram reduction and basic quotient/square identities.",
        "micro_drill_title": "Grade 11 Trig Reductions Micro-Drill",
        "route": "grade11_trigonometry_practice",
    },
    "mathematics:12:patterns, sequences and series": {
        "target_grade": "11",
        "target_topic": "Patterns and Sequences",
        "target_subskill": "quadratic_patterns",
        "gap_title": "Quadratic number patterns & second differences (Grade 11)",
        "explanation": "Arithmetic and Geometric series summation formulas require isolating common differences (d) and ratios (r) mastered in Grade 11.",
        "micro_drill_title": "Grade 11 Quadratic Patterns Micro-Drill",
        "route": "grade11_patterns_sequences_practice",
    },

    # ── Grade 11 Mathematics ──
    "mathematics:11:quadratic equations": {
        "target_grade": "10",
        "target_topic": "Algebraic Expressions",
        "target_subskill": "trinomial_factorisation",
        "gap_title": "Trinomial factorisation (Grade 10)",
        "explanation": "Solving quadratic equations by factorisation requires finding factors of ac that sum to b: ax² + bx + c = 0.",
        "micro_drill_title": "Grade 10 Trinomial Factorisation Micro-Drill",
        "route": "grade10_algebraic_expressions_practice",
    },
    "mathematics:11:equations and inequalities": {
        "target_grade": "10",
        "target_topic": "Algebraic Expressions",
        "target_subskill": "trinomial_factorisation",
        "gap_title": "Trinomial factorisation & difference of squares (Grade 10)",
        "explanation": "Grade 11 quadratic equations and inequalities depend on Grade 10 factorisation techniques.",
        "micro_drill_title": "Grade 10 Factorisation Micro-Drill",
        "route": "grade10_algebraic_expressions_practice",
    },
    "mathematics:11:exponents and surds": {
        "target_grade": "10",
        "target_topic": "Exponents",
        "target_subskill": "exponent_laws",
        "gap_title": "Index laws & rational exponents (Grade 10)",
        "explanation": "Surd simplification and exponential equations require integer exponent rules (xᵃ × xᵇ = xᵃ⁺ᵇ, (xᵃ)ᵇ = xᵃᵇ).",
        "micro_drill_title": "Grade 10 Exponent Laws Micro-Drill",
        "route": "grade10_exponents_practice",
    },
    "mathematics:11:analytical geometry": {
        "target_grade": "10",
        "target_topic": "Analytical Geometry",
        "target_subskill": "distance_midpoint_gradient",
        "gap_title": "Distance, midpoint & gradient formulas (Grade 10)",
        "explanation": "Inclination of a line and parallel/perpendicular slopes build on coordinate geometry fundamentals.",
        "micro_drill_title": "Grade 10 Coordinate Geometry Micro-Drill",
        "route": "grade10_analytical_geometry_practice",
    },
    "mathematics:11:trigonometry": {
        "target_grade": "10",
        "target_topic": "Trigonometry",
        "target_subskill": "soh_cah_toa",
        "gap_title": "Right-angled triangle trig definitions (Grade 10)",
        "explanation": "Working in Cartesian quadrants requires sin θ = y/r, cos θ = x/r, tan θ = y/x.",
        "micro_drill_title": "Grade 10 Trig Ratios Micro-Drill",
        "route": "grade10_trigonometry1_practice",
    },

    # ── Grade 10 Mathematics ──
    "mathematics:10:algebraic expressions": {
        "target_grade": "9",
        "target_topic": "Algebraic Expressions",
        "target_subskill": "common_factors_and_binomials",
        "gap_title": "Common monomial factor extraction (Grade 9)",
        "explanation": "Factoring quadratic expressions requires finding the highest common factor (HCF) and grouping terms.",
        "micro_drill_title": "Grade 9 Common Factors Micro-Drill",
        "route": "grade9_algebraic_expressions_practice",
    },
    "mathematics:10:equations and inequalities": {
        "target_grade": "9",
        "target_topic": "Algebraic Equations",
        "target_subskill": "linear_equations_with_brackets",
        "gap_title": "Linear equations with fractions & brackets (Grade 9)",
        "explanation": "Solving quadratic or simultaneous equations requires isolating variables and balancing operations across the equals sign.",
        "micro_drill_title": "Grade 9 Linear Equations Micro-Drill",
        "route": "grade9_algebraic_equations_practice",
    },
    "mathematics:10:exponents": {
        "target_grade": "9",
        "target_topic": "Exponents",
        "target_subskill": "laws_of_exponents",
        "gap_title": "Product & quotient exponent laws (Grade 9)",
        "explanation": "Handling algebraic powers with negative indices requires the Grade 9 exponent laws.",
        "micro_drill_title": "Grade 9 Exponent Laws Micro-Drill",
        "route": "grade9_exponents_practice",
    },
    "mathematics:10:trigonometry": {
        "target_grade": "9",
        "target_topic": "Geometry of 2D Shapes",
        "target_subskill": "pythagoras_theorem",
        "gap_title": "Theorem of Pythagoras (Grade 9)",
        "explanation": "Calculating hypotenuse, adjacent, and opposite sides in right-angled triangles relies on a² + b² = c².",
        "micro_drill_title": "Grade 9 Pythagoras Theorem Micro-Drill",
        "route": "grade9_geometry_2d_practice",
    },

    # ── Grade 9 Mathematics ──
    "mathematics:9:algebraic expressions": {
        "target_grade": "8",
        "target_topic": "Algebraic Expressions",
        "target_subskill": "like_terms_and_distributive_law",
        "gap_title": "Like terms & distributive law (Grade 8)",
        "explanation": "Expanding binomial products requires distributing terms across brackets: a(b + c) = ab + ac.",
        "micro_drill_title": "Grade 8 Distributive Law Micro-Drill",
        "route": "grade8_algebraic_expressions_practice",
    },
    "mathematics:9:algebraic equations": {
        "target_grade": "8",
        "target_topic": "Algebraic Equations",
        "target_subskill": "linear_equations_integers",
        "gap_title": "Solving linear equations with directed integers (Grade 8)",
        "explanation": "Balancing equations with inverse operations requires confidence in signed integer arithmetic.",
        "micro_drill_title": "Grade 8 Integer Equations Micro-Drill",
        "route": "grade8_algebraic_equations_practice",
    },
    "mathematics:9:exponents": {
        "target_grade": "8",
        "target_topic": "Exponents",
        "target_subskill": "repeated_multiplication_powers",
        "gap_title": "Repeated multiplication & power notation (Grade 8)",
        "explanation": "Understanding that 2⁴ = 2 × 2 × 2 × 2 is essential before combining indices.",
        "micro_drill_title": "Grade 8 Power Notation Micro-Drill",
        "route": "grade8_exponents_practice",
    },

    # ── Grade 8 Mathematics ──
    "mathematics:8:algebraic expressions": {
        "target_grade": "7",
        "target_topic": "Whole Numbers",
        "target_subskill": "order_of_operations_bodmas",
        "gap_title": "Order of operations / BODMAS (Grade 7)",
        "explanation": "Evaluating algebraic expressions requires strict order of operations: Brackets, Orders/Powers, Division, Multiplication, Addition, Subtraction.",
        "micro_drill_title": "Grade 7 BODMAS Micro-Drill",
        "route": "grade7_whole_numbers_practice",
    },
    "mathematics:8:integers": {
        "target_grade": "7",
        "target_topic": "Whole Numbers",
        "target_subskill": "number_bonds_addition_subtraction",
        "gap_title": "Number bonds & number line arithmetic (Grade 7)",
        "explanation": "Directed integer arithmetic (+ and - signs) builds on whole number distance and number line direction.",
        "micro_drill_title": "Grade 7 Number Bonds Micro-Drill",
        "route": "grade7_whole_numbers_practice",
    },
    "mathematics:8:exponents": {
        "target_grade": "7",
        "target_topic": "Exponents",
        "target_subskill": "squares_cubes_quickfacts",
        "gap_title": "Mental squares & cubes (Grade 7)",
        "explanation": "Fluency with exponents requires instant recall of perfect squares (1² to 15²) and perfect cubes (1³ to 6³).",
        "micro_drill_title": "Grade 7 Squares & Cubes Micro-Drill",
        "route": "grade7_exponents_practice",
    },

    # ── Commercial Sciences (EMS / Accounting) ──
    "accounting:11:partnerships": {
        "target_grade": "10",
        "target_topic": "Sole Trader",
        "target_subskill": "general_ledger_trading_profit_loss",
        "gap_title": "General Ledger & Profit Calculation (Grade 10)",
        "explanation": "Partnership accounting divides net profit calculated through sole trader ledger accounts.",
        "micro_drill_title": "Grade 10 Sole Trader Ledger Micro-Drill",
        "route": "grade10_accounting_sole_trader_practice",
    },
    "accounting:11:bank reconciliation": {
        "target_grade": "10",
        "target_topic": "Sole Trader",
        "target_subskill": "crj_cpj_bank_columns",
        "gap_title": "Cash Receipts & Payments Journals (Grade 10)",
        "explanation": "Bank reconciliation requires comparing the CRJ and CPJ bank columns with the monthly bank statement.",
        "micro_drill_title": "Grade 10 Cash Journals Micro-Drill",
        "route": "grade10_accounting_sole_trader_practice",
    },
    "accounting:10:sole trader": {
        "target_grade": "9",
        "target_topic": "EMS Financial Literacy",
        "target_subskill": "crj_cpj_debtors_creditors",
        "gap_title": "Subsidiary Journals & General Ledger (Grade 9 EMS)",
        "explanation": "Sole trader financial accounting requires classifying source documents into CRJ, CPJ, DJ, and CJ.",
        "micro_drill_title": "Grade 9 EMS Journals Micro-Drill",
        "route": "grade9_ems_practice",
    },
    "ems:9:financial literacy": {
        "target_grade": "8",
        "target_topic": "EMS Financial Literacy",
        "target_subskill": "accounting_equation_a_oe_l",
        "gap_title": "The Accounting Equation: A = OE + L (Grade 8 EMS)",
        "explanation": "Recording journal transactions requires understanding effect on Assets, Owner's Equity, and Liabilities.",
        "micro_drill_title": "Grade 8 Accounting Equation Micro-Drill",
        "route": "grade8_ems_practice",
    },
    "ems:8:financial literacy": {
        "target_grade": "7",
        "target_topic": "EMS Financial Literacy",
        "target_subskill": "personal_and_business_budgets",
        "gap_title": "Income, Expenses & Personal Budgets (Grade 7 EMS)",
        "explanation": "Understanding owner's capital and net profit starts with calculating income vs. operational expenditure.",
        "micro_drill_title": "Grade 7 EMS Budgets Micro-Drill",
        "route": "grade7_ems_practice",
    },

    # ── Sciences (Natural Sciences & Physical Sciences) ──
    "physical sciences:11:newton's laws": {
        "target_grade": "10",
        "target_topic": "Mechanics",
        "target_subskill": "vectors_and_scalars",
        "gap_title": "Vector resolution & free-body diagrams (Grade 10)",
        "explanation": "Newton's second law (F_net = ma) requires resolving force vectors into horizontal and vertical components.",
        "micro_drill_title": "Grade 10 Force Vectors Micro-Drill",
        "route": "grade10_physics_mechanics_practice",
    },
    "physical sciences:11:stoichiometry": {
        "target_grade": "10",
        "target_topic": "Chemical Change",
        "target_subskill": "mole_concept_molar_mass",
        "gap_title": "Mole concept & molar mass (Grade 10)",
        "explanation": "Limiting reagents and percentage yields rely directly on calculating molar mass (n = m/M).",
        "micro_drill_title": "Grade 10 Mole Concept Micro-Drill",
        "route": "grade10_chemistry_mole_practice",
    },
    "physical sciences:10:mechanics": {
        "target_grade": "9",
        "target_topic": "Forces and Motion",
        "target_subskill": "speed_velocity_acceleration",
        "gap_title": "Speed, velocity & acceleration basics (Grade 9 NS)",
        "explanation": "Kinematics equations of motion require intuitive understanding of change in position over time (v = Δx/Δt).",
        "micro_drill_title": "Grade 9 Forces & Motion Micro-Drill",
        "route": "grade9_ns_practice",
    },
}


def normalize_key(subject: str, grade: str, topic: str) -> str:
    """Normalize subject, grade, and topic into lookup key."""
    norm_subj = str(subject or '').strip().lower()
    if 'math' in norm_subj and 'lit' not in norm_subj and 'tech' not in norm_subj:
        norm_subj = 'mathematics'
    elif 'account' in norm_subj:
        norm_subj = 'accounting'
    elif 'ems' in norm_subj:
        norm_subj = 'ems'
    elif 'physic' in norm_subj:
        norm_subj = 'physical sciences'

    norm_grade = str(grade or '').strip()
    norm_topic = str(topic or '').strip().lower()

    # Match aliases
    if 'quadratic' in norm_topic or 'inequal' in norm_topic or 'equation' in norm_topic:
        if norm_grade == '11':
            norm_topic = 'quadratic equations'
        elif norm_grade == '10':
            norm_topic = 'equations and inequalities'
    elif 'exponent' in norm_topic or 'surd' in norm_topic or 'power' in norm_topic:
        if norm_grade == '11':
            norm_topic = 'exponents and surds'
        else:
            norm_topic = 'exponents'
    elif 'trig' in norm_topic:
        norm_topic = 'trigonometry'
    elif 'calculus' in norm_topic:
        norm_topic = 'calculus'
    elif 'sole trader' in norm_topic or 'ledger' in norm_topic:
        norm_topic = 'sole trader'
    elif 'partner' in norm_topic:
        norm_topic = 'partnerships'
    elif 'reconcil' in norm_topic:
        norm_topic = 'bank reconciliation'
    elif 'financial lit' in norm_topic:
        norm_topic = 'financial literacy'
    elif 'whole' in norm_topic or 'number' in norm_topic:
        norm_topic = 'whole numbers'

    return f"{norm_subj}:{norm_grade}:{norm_topic}"


def get_prerequisite(subject: str, grade: str, topic: str, subskill: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Look up direct prerequisite for the given subject, grade, and topic.
    Returns dictionary with target_grade, target_topic, target_subskill, gap_title, explanation, route.
    """
    key = normalize_key(subject, grade, topic)
    if key in PREREQUISITE_GRAPH:
        return dict(PREREQUISITE_GRAPH[key])

    # Fallback fuzzy scan by subject and grade
    norm_topic = str(topic or '').lower()
    for graph_key, data in PREREQUISITE_GRAPH.items():
        k_subj, k_grade, k_topic = graph_key.split(':', 2)
        if str(grade) == k_grade and k_subj in str(subject).lower():
            if k_topic in norm_topic or norm_topic in k_topic:
                return dict(data)

    return None


def get_full_lineage(subject: str, grade: str, topic: str) -> List[Dict[str, Any]]:
    """Returns the full ancestral prerequisite path down to the foundational root (e.g. Grade 7)."""
    lineage = []
    curr_subj = subject
    curr_grade = str(grade)
    curr_topic = topic

    visited = set()
    while True:
        key = normalize_key(curr_subj, curr_grade, curr_topic)
        if key in visited:
            break
        visited.add(key)

        prereq = get_prerequisite(curr_subj, curr_grade, curr_topic)
        if not prereq:
            break

        lineage.append({
            "from_grade": curr_grade,
            "from_topic": curr_topic,
            "target_grade": prereq["target_grade"],
            "target_topic": prereq["target_topic"],
            "target_subskill": prereq["target_subskill"],
            "gap_title": prereq["gap_title"],
            "explanation": prereq["explanation"],
            "route": prereq.get("route", ""),
        })

        curr_grade = prereq["target_grade"]
        curr_topic = prereq["target_topic"]

    return lineage
