"""Grade 8 EMS — The Markets (Deterministic 6-Pillar Generator).
Grounded strictly in: curriculum_docs_auto/EMS_Gr8/Term 4/02. The markets.md

Covers CAPS subskills:
  1. definition_and_types_of_markets: Market concept (physical vs virtual exchange).
  2. goods_and_services_market: Wholesale, retail, flea/farmers/craft markets, and intangible services markets.
  3. factor_market_structure: Differentiating factor market (buying/selling production resources) from goods market.
  4. financial_markets: Capital market (shares, dividends, JSE) vs money market (bank loans, trade credit, overdrafts).
  5. labour_market: Employers and employees, monthly salaries vs hourly/weekly wages.

Zero-LLM, 100% deterministic, authentic South African context.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional
from app.utils.ems_namelist import get_ems_scenario, AREAS

SUBSKILLS = [
    "definition_and_types_of_markets",
    "goods_and_services_market",
    "factor_market_structure",
    "financial_markets",
    "labour_market",
]

TOPIC_KEY = "grade8_ems_markets"
LO = "g8_ems_markets"


def _rng(seed: Optional[int] = None) -> random.Random:
    return random.Random(seed) if seed is not None else random.Random()


def _gen_def_markets(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "In Economics, what is the authentic definition of a **market**?"
    )
    options = [
        "Any physical or virtual arrangement where buyers and sellers communicate to exchange goods, services, and resources.",
        "A specific brick-and-mortar municipal grocery store building located in a city centre.",
        "An exclusive government agency that dictates the prices of all private goods and services.",
        "A warehouse where manufacturers store unsold products before they are discarded.",
    ]
    ans = "A. Any physical or virtual arrangement where buyers and sellers communicate to exchange goods, services, and resources."
    sol = (
        "**A. Any physical or virtual arrangement where buyers and sellers communicate to exchange goods, services, and resources.** [2 marks]\n\n"
        "**Explanation:** In modern economics, a market is not restricted to a physical building; it includes websites, exchanges (like the JSE), "
        "and any mechanism where buyers and sellers interact to determine prices and exchange goods, services, or factors of production."
    )
    return {
        "id": f"g8_mkt_def_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The Markets",
        "subskill": "definition_and_types_of_markets",
        "learning_objective_id": f"{LO}_def",
        "archetype": "market_definition_check",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": "0",
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Markets can be physical or online/virtual.",
            "tier_2": "It involves buyers and sellers agreeing on price and exchange.",
            "tier_3": "Correct answer is option A.",
        },
        "misconception_tags": ["restricting_market_to_physical_shops"],
    }


def _gen_goods_services(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    cases = [
        (
            f"A large enterprise purchases hundreds of crates of cleaning supplies directly from factories, breaks the bulk into smaller packs, and sells them to spaza shops and retailers in {scenario['area']}.",
            "Wholesale market",
            ["Wholesale market", "Retail market", "Labour market", "Capital market"],
            "Wholesalers buy in bulk from producers and sell smaller quantities to retailers.",
        ),
        (
            f"Consumers walk into a supermarket in {scenario['area']} to buy bread, milk, and stationery for their daily household use.",
            "Retail market",
            ["Retail market", "Wholesale market", "Money market", "Factor market"],
            "Retailers sell directly to the final consumer in individual quantities.",
        ),
        (
            f"An electrician, lawyer, or doctor provides specialized professional expertise to a client in {scenario['area']}.",
            "Services market (intangible)",
            ["Services market (intangible)", "Capital market", "Commodity market", "Foreign exchange market"],
            "A service is an intangible activity where expertise, knowledge, or labour is sold.",
        ),
    ]
    stmt, correct_type, options, expl = rng.choice(cases)
    rng.shuffle(options)
    c_idx = options.index(correct_type)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"Consider the following business activity in {scenario['area']}:\n\n"
        f"\"{stmt}\"\n\n"
        f"Which type of goods and services market does this transaction represent?"
    )
    ans = f"{correct_letter}. {correct_type}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {expl}"
    )
    return {
        "id": f"g8_mkt_gs_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The Markets",
        "subskill": "goods_and_services_market",
        "learning_objective_id": f"{LO}_goods_services",
        "archetype": "goods_services_market_classification",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Consider whether this is bulk to retailers (wholesale) or final consumer (retail) or intangible (service).",
            "tier_2": f"Explanation hint: {expl}",
            "tier_3": f"Answer is {correct_type}.",
        },
        "misconception_tags": ["confuses_wholesale_with_retail"],
    }


def _gen_factor_vs_goods(rng: random.Random) -> Dict[str, Any]:
    prompt = (
        "Differentiate clearly between the **Goods and Services Market** and the **Factor Market**.\n\n"
        "1. What is bought and sold in the Goods and Services Market, and who are the primary buyers?\n"
        "2. What is bought and sold in the Factor Market, and who are the primary buyers?"
    )
    ans = (
        "1. Final goods and services (e.g. food, clothing, transport); primary buyers are households and consumers.\n"
        "2. Factors of production (labour, land, capital, entrepreneurship); primary buyers are businesses and firms."
    )
    sol = (
        "**Model Answer** [4 marks]:\n\n"
        "1. **Goods and Services Market** [2 marks]:\n"
        "   - What is traded: Finished consumer goods and services [1 mark].\n"
        "   - Primary buyers: Households/consumers purchase to satisfy needs and wants [1 mark].\n\n"
        "2. **Factor Market** [2 marks]:\n"
        "   - What is traded: The factors of production (natural resources, labour, capital, entrepreneurship) [1 mark].\n"
        "   - Primary buyers: Businesses/firms purchase these resources to produce goods and services [1 mark]."
    )
    return {
        "id": f"g8_mkt_fac_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "The Markets",
        "subskill": "factor_market_structure",
        "learning_objective_id": f"{LO}_factor_vs_goods",
        "archetype": "market_structural_comparison",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Goods market: finished goods/services bought by households/consumers", "marks": 2, "editable": True},
                {"id": "mp2", "desc": "Factor market: factors of production bought by businesses/firms", "marks": 2, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Households buy final goods. Businesses buy factors of production to make those goods.",
            "tier_2": "Goods market = food, cars, haircuts. Factor market = workers, land, investment funds.",
            "tier_3": "1. Goods: products/services bought by households. 2. Factors: labour/land/capital bought by businesses.",
        },
        "misconception_tags": ["inverting_buyers_in_factor_and_goods_markets"],
    }


def _gen_financial_markets(rng: random.Random) -> Dict[str, Any]:
    scenarios = [
        (
            "A public company issues shares to the public on the Johannesburg Stock Exchange (JSE) to raise long-term capital for business expansion. Shareholders receive dividends from profits.",
            "Capital Market",
            ["Capital Market", "Money Market", "Labour Market", "Foreign Exchange Market"],
            "The capital market deals with long-term finance, shares, and equities traded on stock exchanges like the JSE.",
        ),
        (
            "A small business owner obtains a 30-day trade credit from a supplier or uses a temporary bank overdraft to pay urgent monthly operating costs.",
            "Money Market",
            ["Money Market", "Capital Market", "Real Estate Market", "Factor Market"],
            "The money market deals with short-term credit, bank loans, overdrafts, and trade credit.",
        ),
    ]
    story, market_name, options, why = rng.choice(scenarios)
    rng.shuffle(options)
    c_idx = options.index(market_name)
    correct_letter = chr(65 + c_idx)

    prompt = (
        f"Consider the following financial arrangement:\n\n"
        f"\"{story}\"\n\n"
        f"Which division of the financial market does this transaction belong to?"
    )
    ans = f"{correct_letter}. {market_name}"
    sol = (
        f"**{ans}** [2 marks]\n\n"
        f"**Explanation:** {why}"
    )
    return {
        "id": f"g8_mkt_fin_{rng.randint(100000, 999999)}",
        "question_type": "mcq",
        "topic": "The Markets",
        "subskill": "financial_markets",
        "learning_objective_id": f"{LO}_financial",
        "archetype": "financial_market_division",
        "prompt": prompt,
        "question": prompt,
        "options": options,
        "correct_index": str(c_idx),
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 2,
        "hints": {
            "tier_1": "Long-term shares and JSE stocks belong to the Capital Market.",
            "tier_2": "Short-term bank loans, overdrafts, and trade credit belong to the Money Market.",
            "tier_3": f"Answer is {market_name}.",
        },
        "misconception_tags": ["confuses_money_market_with_capital_market"],
    }


def _gen_labour_market(rng: random.Random) -> Dict[str, Any]:
    scenario = get_ems_scenario(rng)
    prompt = (
        f"In the labour market in {scenario['area']}, workers exchange their time and skills for financial compensation.\n\n"
        f"1. Explain the difference between a **salary** and a **wage**.\n"
        f"2. Who are the suppliers of labour in this market, and who are the buyers?"
    )
    ans = (
        "1. A salary is a fixed monthly payment for skilled/professional work; a wage is an hourly or weekly rate paid based on hours worked;\n"
        "2. Households (individuals/workers) are the suppliers of labour; businesses and the government are the buyers."
    )
    sol = (
        "**Model Answer** [4 marks]:\n\n"
        "1. **Salary vs Wage** [2 marks]:\n"
        "   - **Salary:** A fixed amount of money paid at the end of each month, typical for administrative, managerial, and professional staff [1 mark].\n"
        "   - **Wage:** Calculated at an hourly rate and paid weekly or fortnightly according to the exact number of hours worked, typical for manual and semi-skilled workers [1 mark].\n\n"
        "2. **Suppliers and Buyers** [2 marks]:\n"
        "   - **Suppliers of Labour:** Households / individual workers supply their mental and physical labour [1 mark].\n"
        "   - **Buyers of Labour:** Businesses, entrepreneurs, and the government hire (buy) labour [1 mark]."
    )
    return {
        "id": f"g8_mkt_lab_{rng.randint(100000, 999999)}",
        "question_type": "paragraph",
        "topic": "The Markets",
        "subskill": "labour_market",
        "learning_objective_id": f"{LO}_labour_market",
        "archetype": "labour_market_mechanisms",
        "prompt": prompt,
        "question": prompt,
        "correct_answer": ans,
        "sample_answer": ans,
        "worked_solution": sol,
        "explanation": sol,
        "canonical_solution": sol,
        "marks": 4,
        "marking_schema": {
            "total_marks": 4,
            "marking_points": [
                {"id": "mp1", "desc": "Salary explained as fixed monthly rate for professional staff", "marks": 1, "editable": True},
                {"id": "mp2", "desc": "Wage explained as hourly/weekly rate based on time worked", "marks": 1, "editable": True},
                {"id": "mp3", "desc": "Households identified as suppliers of labour", "marks": 1, "editable": True},
                {"id": "mp4", "desc": "Businesses/Government identified as buyers of labour", "marks": 1, "editable": True},
            ],
            "deductions": [],
            "carry_forward_rule": "consequential_accuracy",
        },
        "hints": {
            "tier_1": "Salary is monthly; wages are hourly/weekly.",
            "tier_2": "Workers sell their labour (supply); businesses buy their labour (demand).",
            "tier_3": "1. Salary = monthly fixed, Wage = hourly/weekly. 2. Suppliers = households, Buyers = businesses/state.",
        },
        "misconception_tags": ["confuses_supplier_and_buyer_in_labour_market"],
    }


def generate(
    subskill: str = "mixed",
    seed: Optional[int] = None,
    count: int = 1,
    **kwargs: Any,
) -> List[Dict[str, Any]]:
    rng = _rng(seed)
    generators = {
        "definition_and_types_of_markets": _gen_def_markets,
        "goods_and_services_market": _gen_goods_services,
        "factor_market_structure": _gen_factor_vs_goods,
        "financial_markets": _gen_financial_markets,
        "labour_market": _gen_labour_market,
    }

    results: List[Dict[str, Any]] = []
    if subskill in generators:
        for _ in range(count):
            results.append(generators[subskill](rng))
        return results

    keys = list(generators.keys())
    for i in range(count):
        chosen = keys[i % len(keys)]
        results.append(generators[chosen](rng))
    return results
