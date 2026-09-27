import random

NAMES = [
    "Sipho", "Thabo", "Lerato", "Zanele", "Kagiso", "Dineo", 
    "Johan", "Mary", "Lwazi", "Naledi", "Fatima", "Priya"
]

CITIES = [
    "Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth",
    "Bloemfontein", "Polokwane", "Nelspruit", "Kimberley", "Rustenburg"
]

BUSINESS_NAMES = [
    "TechCorp", "Mzanzi Traders", "Sunrise Logistics", "Blue Ocean Retail",
    "Loxion Foods", "Apex Manufacturing", "Pioneer Services", "Global Imports"
]

BUSINESS_TYPES = [
    "sole trader", "partnership", "private company", "public company",
    "state-owned company", "non-profit company"
]

PRODUCTS = [
    "smartphones", "organic vegetables", "clothing", "furniture",
    "stationary", "software subscriptions", "automotive parts", "baked goods"
]

MACRO_ISSUES = [
    "an increase in the repo rate by the Reserve Bank",
    "new strict environmental legislation",
    "a nationwide power outage affecting production",
    "a sudden drop in the exchange rate (ZAR depreciation)",
    "high inflation reducing consumer purchasing power"
]

MARKET_ISSUES = [
    "a new competitor opening a store across the street",
    "suppliers raising the cost of raw materials by 15%",
    "a change in consumer trends towards eco-friendly alternatives",
    "a key supplier going bankrupt",
    "trade unions demanding higher wages for the industry"
]

MICRO_ISSUES = [
    "a high staff turnover rate in the sales department",
    "outdated machinery breaking down frequently",
    "poor cash flow management by the financial director",
    "a lack of vision and leadership from management",
    "a strike by the company's own workers"
]

try:
    from .sa_naming_engine import generate_sa_enterprise, generate_sa_person
except ImportError:
    from app.utils.sa_naming_engine import generate_sa_enterprise, generate_sa_person


def get_random_scenario(r: random.Random = None):
    """Generates a random dictionary of business dressing."""
    ent = generate_sa_enterprise(r)
    return {
        "owner_name": ent["founder"],
        "city": ent["town"],
        "business_name": ent["business_name"],
        "business_type": ent["form"].lower(),
        "product": ent["product"],
        "province": ent["province"],
        "industry": ent["industry"],
    }

def get_random_issue(environment: str):
    """Returns a random issue from a specific business environment."""
    if environment.lower() == "macro":
        return random.choice(MACRO_ISSUES)
    elif environment.lower() == "market":
        return random.choice(MARKET_ISSUES)
    elif environment.lower() == "micro":
        return random.choice(MICRO_ISSUES)
    return "an unexpected business challenge"
