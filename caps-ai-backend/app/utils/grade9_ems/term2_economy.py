import random

def _rng(seed=None):
    if seed is not None:
        return random.Random(seed)
    return random.Random()

def _with_metadata(item, subskill, learning_objective_id, question_family_id, concept_id, concept_group, diagnostic_tags):
    item['subskill'] = subskill
    item['learning_objective_id'] = learning_objective_id
    item['question_family_id'] = question_family_id
    item['concept_id'] = concept_id
    item['concept_group'] = concept_group
    item['diagnostic_tags'] = diagnostic_tags
    return item

def _generate_price_theory(rng, mode, seed=None):
    questions = [
        {
            "prompt": "According to the law of demand, what happens to the quantity demanded of a product when its price increases?",
            "sample_answer": "It decreases.",
            "ideal_answer": "The quantity demanded decreases.",
            "hint_sections": {
                "1_nudge": "Think about your own behavior as a consumer. Do you buy more or less when things get expensive?",
                "2_concept": "There is an inverse relationship between price and quantity demanded.",
                "3_breakdown": "When price goes up, people buy less. It decreases."
            }
        },
        {
            "prompt": "According to the law of supply, how does a manufacturer respond when the market selling price of their product increases?",
            "sample_answer": "They increase the quantity supplied to maximize profit.",
            "ideal_answer": "The quantity supplied increases.",
            "hint_sections": {
                "1_nudge": "Think from the perspective of the seller. If prices are high, do they want to sell more or less?",
                "2_concept": "There is a direct relationship between price and quantity supplied.",
                "3_breakdown": "High prices incentivize businesses to supply more units."
            }
        },
        {
            "prompt": "In price theory, what is meant by the 'market equilibrium price'?",
            "sample_answer": "The price at which the quantity demanded by consumers exactly equals the quantity supplied by producers.",
            "ideal_answer": "The price where quantity demanded equals quantity supplied (where the demand and supply curves intersect).",
            "hint_sections": {
                "1_nudge": "Think of the point of balance where both buyers and sellers agree.",
                "2_concept": "Equilibrium means there is neither a shortage nor a surplus in the market.",
                "3_breakdown": "It is the market clearing price where demand matches supply."
            }
        },
        {
            "prompt": "What happens in a competitive market if the price of a product is set BELOW the equilibrium price?",
            "sample_answer": "A shortage (excess demand) occurs because consumers want to buy more than producers are willing to supply.",
            "ideal_answer": "A market shortage occurs because quantity demanded exceeds quantity supplied.",
            "hint_sections": {
                "1_nudge": "If goods are very cheap, will there be queues of buyers or piles of unsold stock?",
                "2_concept": "Low prices stimulate high demand but discourage supply, causing shortages.",
                "3_breakdown": "Excess demand creates a market shortage."
            }
        },
        {
            "prompt": "What happens in a competitive market if the price of a product is set ABOVE the equilibrium price?",
            "sample_answer": "A surplus (excess supply) occurs because producers make more goods than consumers are willing to buy at that high price.",
            "ideal_answer": "A market surplus occurs because quantity supplied exceeds quantity demanded.",
            "hint_sections": {
                "1_nudge": "If goods are too expensive, what happens to unsold inventory on shop shelves?",
                "2_concept": "High prices reduce consumer purchasing while encouraging producer supply.",
                "3_breakdown": "Excess supply results in a market surplus."
            }
        },
        {
            "prompt": "Which of the following would cause the entire DEMAND CURVE for winter jackets to shift to the right?",
            "sample_answer": "A sudden severe cold wave or increase in consumer income.",
            "ideal_answer": "An increase in consumer preference/fashion, a cold winter, or an increase in consumer disposable income.",
            "hint_sections": {
                "1_nudge": "A rightward shift means consumers want more jackets at every price level.",
                "2_concept": "Non-price determinants like weather, tastes, and income shift the entire curve.",
                "3_breakdown": "Colder weather increases demand for warm clothing."
            }
        },
        {
            "prompt": "How does an increase in the cost of raw materials (such as flour for a bakery) affect the SUPPLY of that product?",
            "sample_answer": "The cost of production rises, reducing profitability and causing the supply curve to shift to the left (supply decreases).",
            "ideal_answer": "Supply decreases (the supply curve shifts to the left) because producing each unit is more expensive.",
            "hint_sections": {
                "1_nudge": "If ingredients cost more, can the baker afford to make as many loaves at the same price?",
                "2_concept": "Higher input costs reduce producer margins and contract market supply.",
                "3_breakdown": "Supply shifts left / decreases."
            }
        },
        {
            "prompt": "Differentiate between a 'movement along a demand curve' and a 'shift of the demand curve'.",
            "sample_answer": "A movement along the curve is caused ONLY by a change in the product's own price. A shift of the curve is caused by non-price factors like consumer income, tastes, or weather.",
            "ideal_answer": "Price change causes movement along the curve (change in quantity demanded); non-price factors cause the entire curve to shift (change in demand).",
            "hint_sections": {
                "1_nudge": "Does the price of the item change, or does a background factor like popularity change?",
                "2_concept": "Movement = price change only. Shift = non-price determinants.",
                "3_breakdown": "Movement is along the line; shift creates a new line."
            }
        }
    ]
    
    if seed is not None:
        q = questions[int(seed) % len(questions)]
    else:
        q = rng.choice(questions)
    
    item = {
        "id": f"ems9_econ_{rng.randint(1000, 9999)}",
        "topic": "Price Theory & Market Equilibrium",
        "question_type": "standard",
        "prompt": q["prompt"],
        "marks": 2,
        "sample_answer": q["sample_answer"],
        "ideal_answer": q["ideal_answer"],
        "marking_points": ["Correct identification of the economic law, curve movement, or equilibrium condition."],
        "hint_sections": q["hint_sections"],
        "guidelines": ["Award full marks for clear conceptual understanding."],
        "teaching_note": "Ensure learners understand the difference between price changes and curve shifts."
    }
    return [_with_metadata(item, subskill='price_theory', learning_objective_id='lo_price_theory', question_family_id='econ_q', concept_id='price_theory', concept_group='economy', diagnostic_tags=['semantic', 'ems'])]

def generate(subskill="price_theory", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _generate_price_theory(rng, mode, seed=seed)
    selected = pool
    if count < len(selected):
        selected = rng.sample(selected, count)
    return selected
