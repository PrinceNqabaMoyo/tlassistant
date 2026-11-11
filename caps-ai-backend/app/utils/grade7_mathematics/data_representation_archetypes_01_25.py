"""
Grade 7 Mathematics - Represent Data Generator (Archetypes 01 to 25).
100% CAPS-aligned deterministic question generator.
Adheres strictly to the 6-Pillar Generator Contract and Zero-Meta-Curriculum Invariant.
Grounded in curriculum_docs_auto/Mathematics_Gr7/Term 1/02. Represent data.md.
"""
from __future__ import annotations
import random
from typing import Any, Dict, List, Optional


# ==============================================================================
# CLUSTER 1: Single Bar Graph Reading & Interpretation (01 - 08)
# ==============================================================================

def arch_01_read_bar_height_single_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Soccer", "Netball", "Cricket", "Rugby", "Athletics"]
    counts = [rng.randint(15, 45) for _ in categories]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    target_val = counts[target_idx]

    spec = {
        "kind": "bar_graph",
        "title": "Favourite Sports in Grade 7",
        "x_label": "Sport",
        "y_label": "Number of Learners",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the bar graph showing favourite sports of Grade 7 learners.\n\n"
        f"How many learners chose **{target_cat}** as their favourite sport?"
    )
    sol = (
        f"**Step 1:** Locate the **{target_cat}** bar on the horizontal axis [1 Mark: Method].\n\n"
        f"**Step 2:** Read the height of the bar on the vertical axis: "
        f"$$\\mathbf{{{target_val}}} \\text{{ learners}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_01_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "01_read_bar_height_single_category",
        "hints": {
            "tier_1": f"Find '{target_cat}' on the horizontal axis and trace up to the top of the bar.",
            "tier_2": "Look horizontally across to the vertical axis to read the value.",
            "tier_3": f"{target_val} learners."
        }
    }


def arch_02_identify_modal_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Bus", "Walk", "Bicycle", "Car", "Taxi"]
    # Ensure distinct max and min
    counts = rng.sample(range(10, 60), len(categories))
    max_idx = counts.index(max(counts))
    modal_cat = categories[max_idx]
    max_val = counts[max_idx]

    spec = {
        "kind": "bar_graph",
        "title": "Method of Transport to School",
        "x_label": "Transport Mode",
        "y_label": "Frequency",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"The bar graph displays the transport methods used by Grade 7 learners.\n\n"
        f"1. Which method of transport is the **mode** (most common)?\n"
        f"2. State its frequency."
    )
    sol = (
        f"**Step 1:** The mode is the category represented by the tallest bar: "
        f"**{modal_cat}** [1 Mark: Method].\n\n"
        f"**Step 2:** Height of the tallest bar is: "
        f"$$\\mathbf{{{max_val}}} \\text{{ learners}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_02_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{modal_cat}; {max_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "02_identify_modal_category",
        "hints": {
            "tier_1": "The mode corresponds to the tallest bar in the graph.",
            "tier_2": f"The tallest bar is {modal_cat}.",
            "tier_3": f"{modal_cat} with {max_val} learners."
        }
    }


def arch_03_total_frequency_across_all_bars(rng: random.Random) -> Dict[str, Any]:
    categories = ["isiZulu", "English", "Afrikaans", "Sesotho", "isiXhosa"]
    counts = [rng.randint(8, 25) for _ in categories]
    total = sum(counts)
    sum_str = " + ".join(str(c) for c in counts)

    spec = {
        "kind": "bar_graph",
        "title": "Home Languages Spoken in Class",
        "x_label": "Language",
        "y_label": "Number of Learners",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"The bar graph illustrates home languages spoken by learners in a Grade 7 class.\n\n"
        f"Calculate the **total number of learners** surveyed in this class."
    )
    sol = (
        f"**Step 1:** Read the frequency of each bar:\n"
        + "".join([f"- {cat}: {cnt}\n" for cat, cnt in zip(categories, counts)])
        + f"[1 Mark: Method].\n\n"
        f"**Step 2:** Sum all frequencies:\n"
        f"$$\\text{{Total}} = {sum_str} = \\mathbf{{{total}}} \\text{{ learners [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_03_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "03_total_frequency_across_all_bars",
        "hints": {
            "tier_1": "Read each bar height and add them all together.",
            "tier_2": f"Add: {sum_str}.",
            "tier_3": f"{total} learners."
        }
    }


def arch_04_difference_between_two_bars(rng: random.Random) -> Dict[str, Any]:
    categories = ["Apples", "Bananas", "Oranges", "Pears"]
    counts = rng.sample(range(12, 40), len(categories))
    i, j = rng.sample(range(len(categories)), 2)
    cat_a, cat_b = categories[i], categories[j]
    val_a, val_b = counts[i], counts[j]
    diff = abs(val_a - val_b)
    higher = cat_a if val_a > val_b else cat_b
    lower = cat_b if val_a > val_b else cat_a

    spec = {
        "kind": "bar_graph",
        "title": "Fruit Sold at Tuckshop",
        "x_label": "Fruit Type",
        "y_label": "Quantity Sold",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the bar graph showing fruit sales at a school tuckshop.\n\n"
        f"How many more **{higher}** were sold than **{lower}**?"
    )
    sol = (
        f"**Step 1:** Identify bar heights: {higher} = {max(val_a, val_b)} and {lower} = {min(val_a, val_b)} [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract: "
        f"$${max(val_a, val_b)} - {min(val_a, val_b)} = \\mathbf{{{diff}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_04_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "04_difference_between_two_bars",
        "hints": {
            "tier_1": f"Find heights for {higher} and {lower}, then subtract.",
            "tier_2": f"{max(val_a, val_b)} - {min(val_a, val_b)}.",
            "tier_3": f"{diff}."
        }
    }


def arch_05_fraction_or_percentage_of_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Fiction", "Non-Fiction", "Comics", "Poetry"]
    c0 = rng.choice([20, 25, 30])
    counts = [c0, 40 - c0, 35, 25]  # total = 100
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    target_val = counts[target_idx]
    pct = target_val  # since sum is 100

    spec = {
        "kind": "bar_graph",
        "title": "Library Books Borrowed by Genre",
        "x_label": "Genre",
        "y_label": "Number of Books",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"The bar graph shows the number of books borrowed from the library by genre.\n\n"
        f"What **percentage** of the total books borrowed were **{target_cat}**?"
    )
    sol = (
        f"**Step 1:** Calculate total books: ${counts[0]} + {counts[1]} + 35 + 25 = 100$ [1 Mark: Method].\n\n"
        f"**Step 2:** Form percentage for {target_cat}: "
        f"$$\\frac{{{target_val}}}{{100}} \\times 100\\% = \\mathbf{{{pct}\\%}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_05_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{pct}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "05_fraction_or_percentage_of_category",
        "hints": {
            "tier_1": "Find total books first, then divide category count by total and multiply by 100.",
            "tier_2": f"{target_val} out of 100.",
            "tier_3": f"{pct}%."
        }
    }


def arch_06_horizontal_bar_graph_interpretation(rng: random.Random) -> Dict[str, Any]:
    categories = ["Drama", "Art", "Chess", "Choir", "Robotics"]
    counts = [rng.randint(12, 38) for _ in categories]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    target_val = counts[target_idx]

    spec = {
        "kind": "bar_graph",
        "title": "After-School Club Memberships",
        "x_label": "Number of Learners",
        "y_label": "Clubs",
        "categories": categories,
        "values": counts,
        "orientation": "horizontal",
        "diagram_role": "context"
    }

    prompt = (
        f"The horizontal bar graph shows learner enrollments in after-school clubs.\n\n"
        f"Read the horizontal length of the bar to determine the number of learners enrolled in **{target_cat}**."
    )
    sol = (
        f"**Step 1:** Locate **{target_cat}** on the vertical axis [1 Mark: Method].\n\n"
        f"**Step 2:** Trace the bar horizontally to the horizontal scale: "
        f"$$\\mathbf{{{target_val}}} \\text{{ learners}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_06_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "06_horizontal_bar_graph_interpretation",
        "hints": {
            "tier_1": f"Find {target_cat} on the vertical axis and read across to the bottom axis.",
            "tier_2": f"The bar ends at {target_val}.",
            "tier_3": f"{target_val} learners."
        }
    }


def arch_07_estimating_intermediate_scale_values(rng: random.Random) -> Dict[str, Any]:
    categories = ["Term 1", "Term 2", "Term 3", "Term 4"]
    # Step scale is 10, intermediate values are multiples of 5
    counts = [rng.choice([25, 35, 45, 55]) for _ in categories]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    target_val = counts[target_idx]

    spec = {
        "kind": "bar_graph",
        "title": "Recycling Paper Collected (kg)",
        "x_label": "Term",
        "y_label": "Mass (kg) [Scale in 10s]",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"The bar graph has vertical axis grid lines spaced every 10 kg.\n\n"
        f"In **{target_cat}**, the bar reaches halfway between {target_val - 5} kg and {target_val + 5} kg.\n"
        f"What is the exact mass of paper collected in {target_cat}?"
    )
    sol = (
        f"**Step 1:** Since grid lines are spaced in intervals of 10 kg, halfway represents $5\\text{{ kg}}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Value is ${target_val - 5} + 5 = \\mathbf{{{target_val}\\text{{ kg}}}}$ [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_07_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_val} kg",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "07_estimating_intermediate_scale_values",
        "hints": {
            "tier_1": f"Find the number halfway between {target_val - 5} and {target_val + 5}.",
            "tier_2": f"{target_val - 5} + 5 = {target_val}.",
            "tier_3": f"{target_val} kg."
        }
    }


def arch_08_categories_exceeding_threshold(rng: random.Random) -> Dict[str, Any]:
    categories = ["Grade 4", "Grade 5", "Grade 6", "Grade 7"]
    counts = [rng.randint(20, 60) for _ in categories]
    threshold = rng.choice([30, 40, 45])
    qualifying = [cat for cat, val in zip(categories, counts) if val > threshold]
    k = len(qualifying)
    qual_str = ", ".join(qualifying) if qualifying else "None"

    spec = {
        "kind": "bar_graph",
        "title": "Merit Certificates Awarded",
        "x_label": "Grade",
        "y_label": "Certificates",
        "categories": categories,
        "values": counts,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the bar graph of merit certificates awarded.\n\n"
        f"How many grades had **more than {threshold}** certificates awarded?"
    )
    sol = (
        f"**Step 1:** Compare each bar height to the threshold line at {threshold}:\n"
        + "".join([f"- {cat}: {val} ({'Exceeds' if val > threshold else 'Does not exceed'})\n" for cat, val in zip(categories, counts)])
        + f"[1 Mark: Method].\n\n"
        f"**Step 2:** Total qualifying grades: **{k}** ({qual_str}) [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_08_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{k}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "08_categories_exceeding_threshold",
        "hints": {
            "tier_1": f"Draw an imaginary horizontal line at {threshold} and count bars higher than it.",
            "tier_2": f"Qualifying grades are: {qual_str}.",
            "tier_3": f"{k} grades."
        }
    }


# ==============================================================================
# CLUSTER 2: Double Bar Graph Comparison (09 - 16)
# ==============================================================================

def arch_09_read_double_bar_single_subgroup(rng: random.Random) -> Dict[str, Any]:
    categories = ["Soccer", "Hockey", "Netball", "Cricket"]
    boys = [rng.randint(15, 40) for _ in categories]
    girls = [rng.randint(15, 40) for _ in categories]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    target_group = rng.choice(["Boys", "Girls"])
    target_val = boys[target_idx] if target_group == "Boys" else girls[target_idx]

    spec = {
        "kind": "double_bar_graph",
        "title": "Sports Participation by Gender",
        "x_label": "Sport",
        "y_label": "Number of Learners",
        "categories": categories,
        "series": [
            {"name": "Boys", "values": boys, "color": "#2563eb"},
            {"name": "Girls", "values": girls, "color": "#ec4899"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the double bar graph comparing sports participation by gender.\n\n"
        f"How many **{target_group}** participate in **{target_cat}**?"
    )
    sol = (
        f"**Step 1:** Locate the **{target_cat}** section on the horizontal axis and find the bar corresponding to **{target_group}** in the legend [1 Mark: Method].\n\n"
        f"**Step 2:** Read the height of the bar on the vertical scale: "
        f"$$\\mathbf{{{target_val}}} \\text{{ {target_group.lower()}}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_09_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_val}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "09_read_double_bar_single_subgroup",
        "hints": {
            "tier_1": f"Check the legend for {target_group}, find {target_cat}, and read the bar height.",
            "tier_2": f"The {target_group} bar for {target_cat} reaches {target_val}.",
            "tier_3": f"{target_val}."
        }
    }


def arch_10_compare_two_subgroups_within_category(rng: random.Random) -> Dict[str, Any]:
    categories = ["Term 1", "Term 2", "Term 3", "Term 4"]
    b_vals = [rng.randint(18, 42) for _ in categories]
    g_vals = [rng.randint(18, 42) for _ in categories]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    b = b_vals[target_idx]
    g = g_vals[target_idx]
    diff = abs(b - g)
    leader = "Boys" if b > g else "Girls"

    spec = {
        "kind": "double_bar_graph",
        "title": "Attendance at Chess Club",
        "x_label": "Term",
        "y_label": "Learners Attending",
        "categories": categories,
        "series": [
            {"name": "Boys", "values": b_vals, "color": "#3b82f6"},
            {"name": "Girls", "values": g_vals, "color": "#f43f5e"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the double bar graph for Chess Club attendance.\n\n"
        f"In **{target_cat}**, which group had higher attendance, and by how many learners?"
    )
    sol = (
        f"**Step 1:** In {target_cat}, Boys = {b} and Girls = {g} [1 Mark: Method].\n\n"
        f"**Step 2:** **{leader}** had higher attendance by: "
        f"$${max(b, g)} - {min(b, g)} = \\mathbf{{{diff}}} \\text{{ learners [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_10_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{leader} by {diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "10_compare_two_subgroups_within_category",
        "hints": {
            "tier_1": f"Look at {target_cat} and compare the heights of both bars.",
            "tier_2": f"Subtract {min(b, g)} from {max(b, g)}.",
            "tier_3": f"{leader} by {diff} learners."
        }
    }


def arch_11_category_with_greatest_difference(rng: random.Random) -> Dict[str, Any]:
    categories = ["Mathematics", "English", "Natural Sciences", "EMS"]
    p_schools = [rng.randint(50, 150) for _ in categories]
    s_schools = [p + rng.choice([10, -15, 35, -40]) for p in p_schools]
    diffs = [abs(p - s) for p, s in zip(p_schools, s_schools)]
    max_idx = diffs.index(max(diffs))
    max_cat = categories[max_idx]
    max_diff = diffs[max_idx]

    spec = {
        "kind": "double_bar_graph",
        "title": "Olympiad Participation by School Type",
        "x_label": "Subject",
        "y_label": "Schools Participating",
        "categories": categories,
        "series": [
            {"name": "Primary Schools", "values": p_schools, "color": "#0ea5e9"},
            {"name": "Secondary Schools", "values": s_schools, "color": "#8b5cf6"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"The double bar graph shows schools participating in subject Olympiads.\n\n"
        f"1. In which subject was the difference between primary and secondary schools the **greatest**?\n"
        f"2. Calculate this greatest difference."
    )
    sol = (
        f"**Step 1:** Calculate absolute difference for each subject:\n"
        + "".join([f"- {cat}: |{p} - {s}| = {d}\n" for cat, p, s, d in zip(categories, p_schools, s_schools, diffs)])
        + f"[1 Mark: Method].\n\n"
        f"**Step 2:** Greatest difference is in **{max_cat}** with a difference of **{max_diff}** schools [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_11_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{max_cat}; {max_diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "11_category_with_greatest_difference",
        "hints": {
            "tier_1": "Look for the pair of bars with the biggest height difference.",
            "tier_2": f"The biggest gap is in {max_cat}.",
            "tier_3": f"{max_cat} with difference {max_diff}."
        }
    }


def arch_12_identify_subgroup_exceeding_another(rng: random.Random) -> Dict[str, Any]:
    categories = ["Soccer", "Tennis", "Swimming", "Chess"]
    girls = [rng.randint(25, 34), rng.randint(22, 30), rng.randint(40, 48), 15]
    boys = [40, 15, 30, 25]
    qualifying = [cat for cat, g, b in zip(categories, girls, boys) if g > b]
    qual_str = ", ".join(qualifying)

    spec = {
        "kind": "double_bar_graph",
        "title": "Club Participation",
        "x_label": "Club",
        "y_label": "Learners",
        "categories": categories,
        "series": [
            {"name": "Girls", "values": girls, "color": "#ec4899"},
            {"name": "Boys", "values": boys, "color": "#3b82f6"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the double bar graph of club participation.\n\n"
        f"Name all clubs in which the number of **Girls** exceeded the number of **Boys**."
    )
    sol = (
        f"**Step 1:** Compare Girls (pink) to Boys (blue) in each club:\n"
        + "".join([f"- {c}: Girls ({g}) vs Boys ({b}) $\\rightarrow$ {'Girls higher' if g > b else 'Boys higher'}\n" for c, g, b in zip(categories, girls, boys)])
        + f"[1 Mark: Method].\n\n"
        f"**Step 2:** Clubs where Girls exceeded Boys: **{qual_str}** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_12_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": qual_str,
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "12_identify_subgroup_exceeding_another",
        "hints": {
            "tier_1": "Find categories where the Girls bar is taller than the Boys bar.",
            "tier_2": f"Check each sport: {qual_str}.",
            "tier_3": f"{qual_str}."
        }
    }


def arch_13_overall_subgroup_total(rng: random.Random) -> Dict[str, Any]:
    categories = ["Grade 4", "Grade 5", "Grade 6", "Grade 7"]
    series_name = rng.choice(["Boys", "Girls"])
    counts = [rng.randint(20, 45) for _ in categories]
    other_counts = [rng.randint(20, 45) for _ in categories]
    total = sum(counts)
    sum_str = " + ".join(str(c) for c in counts)

    spec = {
        "kind": "double_bar_graph",
        "title": "Cross-Country Runners",
        "x_label": "Grade",
        "y_label": "Number of Runners",
        "categories": categories,
        "series": [
            {"name": series_name, "values": counts, "color": "#10b981"},
            {"name": "Others", "values": other_counts, "color": "#6366f1"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"The double bar graph displays cross-country runners by grade.\n\n"
        f"Calculate the **total number of {series_name}** running cross-country across all four grades."
    )
    sol = (
        f"**Step 1:** Read {series_name} bar heights: {', '.join(str(c) for c in counts)} [1 Mark: Method].\n\n"
        f"**Step 2:** Add them together:\n"
        f"$$\\text{{Total}} = {sum_str} = \\mathbf{{{total}}} \\text{{ {series_name.lower()} [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_13_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "13_overall_subgroup_total",
        "hints": {
            "tier_1": f"Sum only the bars representing {series_name}.",
            "tier_2": f"Add {sum_str}.",
            "tier_3": f"{total}."
        }
    }


def arch_14_compare_overall_totals_two_subgroups(rng: random.Random) -> Dict[str, Any]:
    categories = ["Term 1", "Term 2", "Term 3"]
    t1 = [rng.randint(30, 60) for _ in categories]
    t2 = [rng.randint(30, 60) for _ in categories]
    tot1 = sum(t1)
    tot2 = sum(t2)
    diff = abs(tot1 - tot2)
    leader = "Team Alpha" if tot1 > tot2 else "Team Beta"

    spec = {
        "kind": "double_bar_graph",
        "title": "House Points Earned",
        "x_label": "Term",
        "y_label": "Points",
        "categories": categories,
        "series": [
            {"name": "Team Alpha", "values": t1, "color": "#f59e0b"},
            {"name": "Team Beta", "values": t2, "color": "#3b82f6"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"The double bar graph shows house points earned across three terms.\n\n"
        f"Which team won the overall competition across all three terms, and by how many points?"
    )
    sol = (
        f"**Step 1:** Calculate overall totals:\n"
        f"- Team Alpha: ${' + '.join(str(x) for x in t1)} = {tot1}$\n"
        f"- Team Beta: ${' + '.join(str(x) for x in t2)} = {tot2}$ [1 Mark: Method].\n\n"
        f"**Step 2:** Compare: **{leader}** won by: "
        f"$${max(tot1, tot2)} - {min(tot1, tot2)} = \\mathbf{{{diff}}} \\text{{ points [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_14_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{leader} by {diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "14_compare_overall_totals_two_subgroups",
        "hints": {
            "tier_1": "Sum the points for Team Alpha, then sum for Team Beta, then subtract.",
            "tier_2": f"Alpha = {tot1}, Beta = {tot2}.",
            "tier_3": f"{leader} by {diff} points."
        }
    }


def arch_15_percentage_double_bar_graph(rng: random.Random) -> Dict[str, Any]:
    categories = ["Electricity", "Water", "Computers", "Library"]
    prov_a = [rng.randint(70, 85), 68, 60, 42]
    prov_b = [50, 45, 25, 30]
    target_idx = rng.randint(0, len(categories) - 1)
    target_cat = categories[target_idx]
    diff = prov_a[target_idx] - prov_b[target_idx]

    spec = {
        "kind": "double_bar_graph",
        "title": "School Facilities: Province A vs Province B",
        "x_label": "Facility",
        "y_label": "Percentage of Schools (%)",
        "categories": categories,
        "series": [
            {"name": "Province A", "values": prov_a, "color": "#059669"},
            {"name": "Province B", "values": prov_b, "color": "#d97706"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"The double bar graph shows the percentage of schools with basic facilities.\n\n"
        f"In **{target_cat}**, what is the difference in percentage points between Province A and Province B?"
    )
    sol = (
        f"**Step 1:** Read percentages for {target_cat}: Province A = {prov_a[target_idx]}% and Province B = {prov_b[target_idx]}% [1 Mark: Method].\n\n"
        f"**Step 2:** Calculate difference: "
        f"$${prov_a[target_idx]}\\% - {prov_b[target_idx]}\\% = \\mathbf{{{diff}\\%}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_15_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "15_percentage_double_bar_graph",
        "hints": {
            "tier_1": f"Read the percentage bars for {target_cat} in Province A and Province B.",
            "tier_2": f"{prov_a[target_idx]}% - {prov_b[target_idx]}%.",
            "tier_3": f"{diff}%."
        }
    }


def arch_16_equal_representation_in_double_bar(rng: random.Random) -> Dict[str, Any]:
    categories = ["Rugby", "Debating", "Science Club", "Choir"]
    eq_v = rng.randint(20, 29)
    boys = [40, eq_v, 30, 20]
    girls = [10, eq_v, 35, 45]
    equal_cat = "Debating"

    spec = {
        "kind": "double_bar_graph",
        "title": "Extramural Activities",
        "x_label": "Activity",
        "y_label": "Participants",
        "categories": categories,
        "series": [
            {"name": "Boys", "values": boys, "color": "#2563eb"},
            {"name": "Girls", "values": girls, "color": "#db2777"}
        ],
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the double bar graph of extramural activities.\n\n"
        f"1. In which activity is participation between Boys and Girls **equal**?\n"
        f"2. How many participants of each gender are in this activity?"
    )
    sol = (
        f"**Step 1:** Look for the activity where both bars have the exact same height: "
        f"**{equal_cat}** [1 Mark: Method].\n\n"
        f"**Step 2:** Both bars have a height of **{eq_v}** participants [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_16_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{equal_cat}; {eq_v}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "16_equal_representation_in_double_bar",
        "hints": {
            "tier_1": "Find the sport where the two bars are level with each other.",
            "tier_2": f"Both bars are at {eq_v} in {equal_cat}.",
            "tier_3": f"{equal_cat} with {eq_v} participants each."
        }
    }


# ==============================================================================
# CLUSTER 3: Histograms & Grouped Frequency (17 - 25)
# ==============================================================================

def arch_17_distinguish_histogram_from_bar_graph(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"Explain two visual differences between a **bar graph** and a **histogram**."
    )
    sol = (
        f"**Step 1 (Bar Graph):** Used for discrete or categorical data; bars have **spaces (gaps)** between them [1 Mark].\n\n"
        f"**Step 2 (Histogram):** Used for continuous grouped intervals; bars **touch each other (no gaps)** to represent a continuous scale [1 Mark]."
    )
    return {
        "id": f"g7_dat_17_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "Histogram bars touch (continuous); bar graph bars have spaces (discrete)",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "17_distinguish_histogram_from_bar_graph",
        "hints": {
            "tier_1": "Think about spaces between the bars and the type of data (discrete vs continuous).",
            "tier_2": "In a histogram, bars touch because data is in continuous intervals.",
            "tier_3": "Histogram bars touch (continuous); bar graph bars have spaces (discrete)."
        }
    }


def arch_18_read_histogram_interval_frequency(rng: random.Random) -> Dict[str, Any]:
    intervals = ["40 - 49", "50 - 59", "60 - 69", "70 - 79", "80 - 89"]
    freqs = [rng.randint(4, 18) for _ in intervals]
    target_idx = rng.randint(0, len(intervals) - 1)
    target_int = intervals[target_idx]
    target_f = freqs[target_idx]

    spec = {
        "kind": "histogram",
        "title": "Mathematics Test Marks (%)",
        "x_label": "Mark Interval (%)",
        "y_label": "Number of Learners",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    prompt = (
        f"The histogram shows marks obtained in a Mathematics test.\n\n"
        f"How many learners scored in the interval **{target_int}%**?"
    )
    sol = (
        f"**Step 1:** Locate the interval **{target_int}** on the horizontal axis [1 Mark: Method].\n\n"
        f"**Step 2:** Read the height of the touching bar on the vertical scale: "
        f"$$\\mathbf{{{target_f}}} \\text{{ learners}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_18_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{target_f}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "18_read_histogram_interval_frequency",
        "hints": {
            "tier_1": f"Find {target_int} on the horizontal axis and trace up to the bar height.",
            "tier_2": f"The bar has a height of {target_f}.",
            "tier_3": f"{target_f} learners."
        }
    }


def arch_19_identify_modal_class_histogram(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0 - 9", "10 - 19", "20 - 29", "30 - 39", "40 - 49"]
    freqs = rng.sample(range(5, 30), len(intervals))
    max_idx = freqs.index(max(freqs))
    modal_int = intervals[max_idx]
    max_f = freqs[max_idx]

    spec = {
        "kind": "histogram",
        "title": "Time Spent on Homework Daily (minutes)",
        "x_label": "Time Interval (min)",
        "y_label": "Frequency",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    prompt = (
        f"The histogram displays time spent on daily homework.\n\n"
        f"1. Identify the **modal class interval**.\n"
        f"2. State the frequency of this modal interval."
    )
    sol = (
        f"**Step 1:** The modal class corresponds to the tallest bar in the histogram: "
        f"**{modal_int} minutes** [1 Mark: Method].\n\n"
        f"**Step 2:** Frequency of this interval is **{max_f} learners** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_19_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{modal_int}; {max_f}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "19_identify_modal_class_histogram",
        "hints": {
            "tier_1": "Find the tallest bar in the histogram.",
            "tier_2": f"The tallest bar covers the range {modal_int}.",
            "tier_3": f"{modal_int} with {max_f} learners."
        }
    }


def arch_20_total_sample_size_from_histogram(rng: random.Random) -> Dict[str, Any]:
    intervals = ["30 - 39", "40 - 49", "50 - 59", "60 - 69"]
    freqs = [rng.randint(5, 15) for _ in intervals]
    total = sum(freqs)
    sum_str = " + ".join(str(f) for f in freqs)

    spec = {
        "kind": "histogram",
        "title": "Mass of Grade 7 Learners (kg)",
        "x_label": "Mass (kg)",
        "y_label": "Learners",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    prompt = (
        f"Refer to the histogram of learner body masses.\n\n"
        f"Calculate the **total number of learners** included in this survey."
    )
    sol = (
        f"**Step 1:** Read the frequency of each interval: {', '.join(str(f) for f in freqs)} [1 Mark: Method].\n\n"
        f"**Step 2:** Sum all frequencies:\n"
        f"$$\\text{{Total}} = {sum_str} = \\mathbf{{{total}}} \\text{{ learners [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_20_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "20_total_sample_size_from_histogram",
        "hints": {
            "tier_1": "Add the heights of all the bars together.",
            "tier_2": f"{sum_str}.",
            "tier_3": f"{total} learners."
        }
    }


def arch_21_observations_above_or_below_threshold_histogram(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0 - 19", "20 - 39", "40 - 59", "60 - 79", "80 - 100"]
    f2 = rng.randint(12, 18)
    f3 = rng.randint(8, 13)
    freqs = [4, 8, f2, f3, 6]

    spec = {
        "kind": "histogram",
        "title": "Science Quiz Results",
        "x_label": "Marks (%)",
        "y_label": "Number of Learners",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    # Pass mark is 40%
    pass_freqs = freqs[2:]  # 40-59, 60-79, 80-100
    pass_total = sum(pass_freqs)
    pass_str = " + ".join(str(f) for f in pass_freqs)

    prompt = (
        f"The histogram displays marks on a science quiz where the pass mark is 40%.\n\n"
        f"How many learners passed the quiz (achieved **40% or more**)?"
    )
    sol = (
        f"**Step 1:** Identify intervals that meet or exceed 40%:\n"
        f"- 40 - 59%: {f2} learners\n"
        f"- 60 - 79%: {f3} learners\n"
        f"- 80 - 100%: 6 learners [1 Mark: Method].\n\n"
        f"**Step 2:** Sum: $${pass_str} = \\mathbf{{{pass_total}}} \\text{{ learners [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_21_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{pass_total}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "21_observations_above_or_below_threshold_histogram",
        "hints": {
            "tier_1": "Add the bars from 40% upwards (40-59, 60-79, and 80-100).",
            "tier_2": f"{f2} + {f3} + 6.",
            "tier_3": f"{pass_total} learners."
        }
    }


def arch_22_interval_width_and_boundaries(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        f"A histogram has intervals: $10 \\le x < 20$, $20 \\le x < 30$, $30 \\le x < 40$.\n\n"
        f"1. What is the **class width** (interval size) of each class?\n"
        f"2. Into which interval would a measurement of exactly $20$ fall?"
    )
    sol = (
        f"**Step 1:** The class width is the difference between upper and lower limits: "
        f"$$20 - 10 = \\mathbf{{10}} \\text{{ [1 Mark: Method]}}$$\n\n"
        f"**Step 2:** Because the inequality is $20 \\le x < 30$ ($x$ is greater than or equal to 20), a value of 20 falls into **$20 \\le x < 30$** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_22_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "10; 20 <= x < 30",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "subskill": "22_interval_width_and_boundaries",
        "hints": {
            "tier_1": "Subtract lower bound from upper bound for width.",
            "tier_2": "Look at the '<=' sign to see which interval includes 20.",
            "tier_3": "Width is 10; interval is 20 <= x < 30."
        }
    }


def arch_23_percentage_of_learners_in_interval(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0 - 19", "20 - 39", "40 - 59", "60 - 79"]
    f0 = rng.choice([8, 10, 12, 14])
    freqs = [f0, 25 - f0, 15, 10]  # total = 50
    target_idx = rng.randint(0, len(intervals) - 1)
    target_int = intervals[target_idx]
    target_f = freqs[target_idx]
    pct = int((target_f / 50) * 100)

    spec = {
        "kind": "histogram",
        "title": "Mathematics Speed Test (Total = 50 learners)",
        "x_label": "Score",
        "y_label": "Frequency",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    prompt = (
        f"In a sample of 50 learners, the histogram shows scores on a speed test.\n\n"
        f"Calculate the **percentage** of learners who scored in the interval **{target_int}**."
    )
    sol = (
        f"**Step 1:** Identify frequency: {target_f} learners out of a total of 50 [1 Mark: Method].\n\n"
        f"**Step 2:** Compute percentage: "
        f"$$\\frac{{{target_f}}}{{50}} \\times 100\\% = \\mathbf{{{pct}\\%}} \\text{{ [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_23_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{pct}%",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "23_percentage_of_learners_in_interval",
        "hints": {
            "tier_1": f"Divide {target_f} by 50 and multiply by 100.",
            "tier_2": f"({target_f} / 50) * 100.",
            "tier_3": f"{pct}%."
        }
    }


def arch_24_comparing_non_adjacent_intervals(rng: random.Random) -> Dict[str, Any]:
    intervals = ["10 - 19", "20 - 29", "30 - 39", "40 - 49", "50 - 59"]
    f1 = rng.randint(10, 14)
    f3 = rng.randint(16, 21)
    freqs = [6, f1, 22, f3, 4]

    spec = {
        "kind": "histogram",
        "title": "Ages of Visitors to Science Expo",
        "x_label": "Age Group",
        "y_label": "Number of Visitors",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    diff = abs(freqs[1] - freqs[3])

    prompt = (
        f"Refer to the histogram of visitor ages.\n\n"
        f"How many more visitors were in the **40 - 49** age group than in the **20 - 29** age group?"
    )
    sol = (
        f"**Step 1:** Frequency of 40 - 49 = {freqs[3]}; Frequency of 20 - 29 = {freqs[1]} [1 Mark: Method].\n\n"
        f"**Step 2:** Subtract: $${freqs[3]} - {freqs[1]} = \\mathbf{{{diff}}} \\text{{ visitors [1 Mark: Accuracy]}}$$"
    )
    return {
        "id": f"g7_dat_24_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": f"{diff}",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "24_comparing_non_adjacent_intervals",
        "hints": {
            "tier_1": f"Read heights for 40-49 and 20-29: {freqs[3]} and {freqs[1]}.",
            "tier_2": f"{freqs[3]} - {freqs[1]}.",
            "tier_3": f"{diff}."
        }
    }


def arch_25_identifying_zero_frequency_intervals(rng: random.Random) -> Dict[str, Any]:
    intervals = ["0 - 4", "5 - 9", "10 - 14", "15 - 19"]
    freqs = [rng.randint(6, 12), 0, rng.randint(13, 18), 6]

    spec = {
        "kind": "histogram",
        "title": "Books Read Over the Holidays",
        "x_label": "Books Read",
        "y_label": "Learners",
        "categories": intervals,
        "values": freqs,
        "diagram_role": "context"
    }

    prompt = (
        f"The histogram shows holiday reading counts.\n\n"
        f"Which interval had a frequency of **zero** (no bar shown)?"
    )
    sol = (
        f"**Step 1:** Scan the horizontal axis for the interval where the bar height is flat at zero [1 Mark: Method].\n\n"
        f"**Step 2:** Interval with 0 frequency: **5 - 9 books** [1 Mark: Accuracy]."
    )
    return {
        "id": f"g7_dat_25_{rng.randint(10000, 99999)}",
        "question_text": prompt,
        "correct_answer": "5 - 9",
        "canonical_solution": sol,
        "explanation": sol,
        "marks": 2,
        "term": 1,
        "diagram_spec": spec,
        "subskill": "25_identifying_zero_frequency_intervals",
        "hints": {
            "tier_1": "Look for the interval where there is no bar drawn.",
            "tier_2": "The flat space is between 5 and 9.",
            "tier_3": "5 - 9."
        }
    }
