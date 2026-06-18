import random

NAMES = [
    "Karabo", "Aisha", "Bongani", "Chloe", "David", "Esethu", 
    "Faris", "Gugulethu", "Heinrich", "Imran"
]

AREAS = [
    "Soweto", "Sandton", "Khayelitsha", "Mitchells Plain", "Umlazi",
    "Chatsworth", "Mamelodi", "Centurion", "Mdantsane"
]

TUCKSHOP_ITEMS = [
    "chips", "cold drinks", "sweets", "bread", "milk", "vetkoek", "fruit"
]

NEEDS = [
    "food", "water", "shelter", "clothing", "basic healthcare"
]

WANTS = [
    "a new smartphone", "designer sneakers", "a gaming console", 
    "expensive jewelry", "a luxury vacation"
]

FINANCIAL_TERMS = [
    "capital", "assets", "liabilities", "income", "expenses", "profit", "loss"
]

def get_ems_scenario():
    """Generates a random dictionary of EMS dressing (often smaller scale than BS)."""
    return {
        "entrepreneur": random.choice(NAMES),
        "area": random.choice(AREAS),
        "item_sold": random.choice(TUCKSHOP_ITEMS),
    }

def get_random_need_and_want():
    return {
        "need": random.choice(NEEDS),
        "want": random.choice(WANTS)
    }
