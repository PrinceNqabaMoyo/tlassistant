"""Grade 10 Mathematics curriculum metadata (scaffold sections + subskills).

Drives the frontend topic registry and the scaffold step ordering. Mirrors the
role of ``_bs_curriculum.py`` for Business Studies but is hand-defined here
(maths scaffolds are subskill-ordered rather than format-pool driven).
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional

TOPICS: Dict[str, Dict[str, Any]] = {
    "grade10_math_algebraic_expressions": {
        "title": "Algebraic Expressions",
        "term": 1,
        "subskills": [
            {"key": "real_numbers", "title": "The real number system"},
            {"key": "rounding", "title": "Rounding off"},
            {"key": "products", "title": "Products (expanding)"},
            {"key": "factorise_common", "title": "Common factors"},
            {"key": "factorise_diff_squares", "title": "Difference of two squares"},
            {"key": "factorise_trinomial", "title": "Quadratic trinomials"},
            {"key": "simplify_fractions", "title": "Simplifying algebraic fractions"},
        ],
        "sections": [
            {"key": "real_numbers", "title": "The real number system", "formats": ["real_numbers"]},
            {"key": "rounding", "title": "Rounding off", "formats": ["rounding"]},
            {"key": "products", "title": "Products", "formats": ["products"]},
            {"key": "factorisation", "title": "Factorisation", "formats": ["factorise_common", "factorise_diff_squares", "factorise_trinomial"]},
            {"key": "fractions", "title": "Algebraic fractions", "formats": ["simplify_fractions"]},
        ],
    },
    "grade10_math_trigonometry": {
        "title": "Trigonometry",
        "term": 1,
        "subskills": [
            {"key": "identify_sides", "title": "Opposite, adjacent & hypotenuse"},
            {"key": "ratio_from_triangle", "title": "Trig ratios from a triangle"},
            {"key": "calculator_value", "title": "Using a calculator"},
            {"key": "special_angles", "title": "Special angles (no calculator)"},
            {"key": "find_length", "title": "Finding a side length"},
            {"key": "find_angle", "title": "Finding an angle"},
            {"key": "solve_equation", "title": "Solving trig equations"},
        ],
        "sections": [
            {"key": "identify_sides", "title": "Opposite, adjacent & hypotenuse", "formats": ["identify_sides"]},
            {"key": "ratios", "title": "Trig ratios (SohCahToa)", "formats": ["ratio_from_triangle"]},
            {"key": "calculator", "title": "Calculator skills", "formats": ["calculator_value"]},
            {"key": "special_angles", "title": "Special angles", "formats": ["special_angles"]},
            {"key": "find_length", "title": "Finding a side length", "formats": ["find_length"]},
            {"key": "find_angle", "title": "Finding an angle", "formats": ["find_angle"]},
            {"key": "solve_equation", "title": "Solving trig equations", "formats": ["solve_equation"]},
        ],
    },
    "grade10_math_exponents": {
        "title": "Exponents",
        "term": 1,
        "subskills": [
            {"key": "zero_negative_exponents", "title": "Zero and negative exponents"},
            {"key": "laws_monomial", "title": "Exponent laws on monomials"},
            {"key": "laws_with_brackets", "title": "Brackets and nested powers"},
            {"key": "prime_base_simplify", "title": "Prime bases and simplifying"},
            {"key": "common_factor_exponents", "title": "Common factor with exponents"},
            {"key": "difference_of_squares_exp", "title": "Difference of squares with exponents"},
            {"key": "rational_exponents", "title": "Rational (fractional) exponents"},
            {"key": "exponential_equations", "title": "Exponential equations"},
        ],
        "sections": [
            {"key": "zero_negative", "title": "Zero and negative exponents", "formats": ["zero_negative_exponents"]},
            {"key": "laws_monomial", "title": "Exponent laws on monomials", "formats": ["laws_monomial"]},
            {"key": "laws_with_brackets", "title": "Brackets and nested powers", "formats": ["laws_with_brackets"]},
            {"key": "prime_base_simplify", "title": "Prime bases and simplifying", "formats": ["prime_base_simplify"]},
            {"key": "common_factor_exponents", "title": "Common factor with exponents", "formats": ["common_factor_exponents"]},
            {"key": "difference_of_squares_exp", "title": "Difference of squares with exponents", "formats": ["difference_of_squares_exp"]},
            {"key": "rational_exponents", "title": "Rational (fractional) exponents", "formats": ["rational_exponents"]},
            {"key": "exponential_equations", "title": "Exponential equations", "formats": ["exponential_equations"]},
        ],
    },
    "grade10_math_equations_inequalities": {
        "title": "Equations & Inequalities",
        "term": 1,
        "subskills": [
            {"key": "linear_equations", "title": "Linear equations"},
            {"key": "quadratic_by_factorising", "title": "Quadratic equations by factorising"},
            {"key": "quadratic_restrictions", "title": "Quadratic equations with restrictions"},
            {"key": "simultaneous_substitution", "title": "Simultaneous equations (substitution)"},
            {"key": "simultaneous_elimination", "title": "Simultaneous equations (elimination)"},
            {"key": "word_problems", "title": "Word problems"},
            {"key": "literal_equations", "title": "Literal equations"},
            {"key": "linear_inequalities", "title": "Linear inequalities"},
        ],
        "sections": [
            {"key": "linear_equations", "title": "Linear equations", "formats": ["linear_equations"]},
            {"key": "quadratic_by_factorising", "title": "Quadratic equations by factorising", "formats": ["quadratic_by_factorising"]},
            {"key": "quadratic_restrictions", "title": "Quadratic equations with restrictions", "formats": ["quadratic_restrictions"]},
            {"key": "simultaneous_substitution", "title": "Simultaneous equations (substitution)", "formats": ["simultaneous_substitution"]},
            {"key": "simultaneous_elimination", "title": "Simultaneous equations (elimination)", "formats": ["simultaneous_elimination"]},
            {"key": "word_problems", "title": "Word problems", "formats": ["word_problems"]},
            {"key": "literal_equations", "title": "Literal equations", "formats": ["literal_equations"]},
            {"key": "linear_inequalities", "title": "Linear inequalities", "formats": ["linear_inequalities"]},
        ],
    },
    "grade10_math_functions": {
        "title": "Functions",
        "term": 1,
        "subskills": [
            {"key": "function_notation_eval", "title": "Function notation: evaluate f(x)"},
            {"key": "function_notation_solve", "title": "Function notation: find the input"},
            {"key": "domain_range", "title": "Domain and range"},
            {"key": "representation_convert", "title": "Representations (table/words/formula)"},
            {"key": "linear_gradient_intercept", "title": "Linear: gradient and y-intercept"},
            {"key": "linear_intercepts", "title": "Linear: intercepts"},
            {"key": "linear_find_equation", "title": "Linear: find the equation"},
            {"key": "quadratic_effect", "title": "Quadratic: effect of a and q"},
            {"key": "quadratic_features", "title": "Quadratic: turning point & symmetry"},
            {"key": "hyperbola_features", "title": "Hyperbola: asymptotes"},
            {"key": "exponential_features", "title": "Exponential: growth, decay & asymptote"},
            {"key": "trig_graph_features", "title": "Trig graphs: amplitude & range"},
            {"key": "interpret_graph", "title": "Interpreting graphs"},
            {"key": "match_equation_graph", "title": "Match equation to graph"},
            {"key": "parameter_manipulation", "title": "Manipulate parameters (grapher)"},
        ],
        "sections": [
            {"key": "function_notation", "title": "Function notation", "formats": ["function_notation_eval", "function_notation_solve"]},
            {"key": "domain_range", "title": "Domain and range", "formats": ["domain_range"]},
            {"key": "representations", "title": "Representations", "formats": ["representation_convert"]},
            {"key": "linear", "title": "Linear functions", "formats": ["linear_gradient_intercept", "linear_intercepts", "linear_find_equation"]},
            {"key": "quadratic", "title": "Quadratic functions", "formats": ["quadratic_effect", "quadratic_features"]},
            {"key": "hyperbola", "title": "Hyperbolic functions", "formats": ["hyperbola_features"]},
            {"key": "exponential", "title": "Exponential functions", "formats": ["exponential_features"]},
            {"key": "trig_graphs", "title": "Trigonometric functions", "formats": ["trig_graph_features"]},
            {"key": "interpretation", "title": "Interpreting graphs", "formats": ["interpret_graph", "match_equation_graph"]},
            {"key": "grapher", "title": "Manipulate parameters", "formats": ["parameter_manipulation"]},
        ],
    },
    "grade10_math_patterns_sequences": {
        "title": "Patterns & Sequences",
        "term": 1,
        "subskills": [
            {"key": "next_terms", "title": "Next terms"},
            {"key": "common_difference", "title": "Common difference"},
            {"key": "general_term", "title": "General term"},
            {"key": "term_from_n", "title": "Term from position"},
            {"key": "n_from_term", "title": "Position from term"},
            {"key": "missing_terms", "title": "Missing terms"},
            {"key": "diagram_pattern", "title": "Diagram patterns"},
            {"key": "letter_sequence", "title": "Letter sequences"},
            {"key": "linear_param", "title": "Linear parameter"},
            {"key": "word_problem", "title": "Word problems"},
        ],
        "sections": [
            {"key": "next_terms", "title": "Next terms", "formats": ["next_terms"]},
            {"key": "common_difference", "title": "Common difference", "formats": ["common_difference"]},
            {"key": "general_term", "title": "General term", "formats": ["general_term"]},
            {"key": "term_from_n", "title": "Term from position", "formats": ["term_from_n"]},
            {"key": "n_from_term", "title": "Position from term", "formats": ["n_from_term"]},
            {"key": "missing_terms", "title": "Missing terms", "formats": ["missing_terms"]},
            {"key": "diagram_pattern", "title": "Diagram patterns", "formats": ["diagram_pattern"]},
            {"key": "letter_sequence", "title": "Letter sequences", "formats": ["letter_sequence"]},
            {"key": "linear_param", "title": "Linear parameter", "formats": ["linear_param"]},
            {"key": "word_problem", "title": "Word problems", "formats": ["word_problem"]},
        ],
    },
}


def get_topic_meta(topic: str) -> Optional[Dict[str, Any]]:
    return TOPICS.get(topic)


def get_topic_sections(topic: str) -> List[Dict[str, Any]]:
    meta = TOPICS.get(topic)
    return list(meta["sections"]) if meta else []


def get_section_for_topic(topic: str, key: str) -> Optional[Dict[str, Any]]:
    for sec in get_topic_sections(topic):
        if sec["key"] == key:
            return sec
    return None


def list_topics() -> List[Dict[str, Any]]:
    return [
        {
            "topic": key,
            "title": meta["title"],
            "term": meta["term"],
            "subskills": meta["subskills"],
        }
        for key, meta in TOPICS.items()
    ]
