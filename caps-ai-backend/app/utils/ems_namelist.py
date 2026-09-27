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

BUSINESS_TYPES = [
    "Cleaners", "Salon", "Plumbing Services", "Auto Repairs", "Deliveries", "Consulting", "Catering"
]

SUPPLIERS = [
    "Waltons", "Office National", "Makro", "Metro Stores", "Game Stores", "Builders Warehouse"
]

def get_ems_scenario(rng=None):
    """Generates a random dictionary of EMS dressing (often smaller scale than BS)."""
    chooser = rng.choice if rng else random.choice
    return {
        "entrepreneur": chooser(NAMES),
        "area": chooser(AREAS),
        "item_sold": chooser(TUCKSHOP_ITEMS),
        "business_type": chooser(BUSINESS_TYPES),
        "competitor": chooser(SUPPLIERS),
        "supplier": chooser(SUPPLIERS),
    }

def get_random_need_and_want(rng=None):
    chooser = rng.choice if rng else random.choice
    return {
        "need": chooser(NEEDS),
        "want": chooser(WANTS)
    }

