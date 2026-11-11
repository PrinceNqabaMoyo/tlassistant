import random
from typing import Any, Dict, List, Optional

# Expand NAMES to 65+ diverse South African names across all cultural groups
NAMES: List[str] = [
    "Karabo", "Aisha", "Bongani", "Naledi", "David", "Esethu", "Faris", "Gugulethu",
    "Heinrich", "Tariq", "Samangele", "Sthembiso", "Mbalenhle", "Latita", "Nqaba",
    "Nqoba", "Lameck", "Sukoluhle", "Dumisani", "Ayanda", "Siyanda", "Luyanda",
    "Loyiso", "Nanziwe", "Lubelihle", "Nqobizitha", "Ndabezinhle", "Amanda",
    "Aluwani", "Ambani", "Dakalo", "Dzuvha", "Elelwani", "Hangwani", "Khuthandzo",
    "Palesa", "Tshepo", "Lerato", "Andziso", "Fanisa", "Hlori", "Annelie", "Elize",
    "Petronella", "Adriaan", "Gert", "Johan", "Pieter", "Mariska", "Noah", "Oliver",
    "James", "Elizabeth", "Amelia", "Sofia", "Maya", "Salim", "Zain", "Malik",
    "Ashwin", "Aravind", "Kamal", "Jayesh", "Yatika", "Neha", "Inaya", "Vanshika",
    "Thabo", "Zanele", "Sipho", "Nomsa", "Kagiso", "Rethabile", "Lunga", "Mpho",
]

# Expand AREAS to 36 urban, township, and rural communities across all 9 South African provinces
AREAS: List[str] = [
    # Gauteng (Urban & Township)
    "Soweto (Gauteng)", "Sandton (Gauteng)", "Mamelodi (Gauteng)", "Centurion (Gauteng)",
    "Tembisa (Gauteng)", "Alexandra (Gauteng)",
    # Western Cape (Urban, Township & Winelands)
    "Khayelitsha (Western Cape)", "Athlone (Western Cape)", "Paarl (Western Cape)",
    "George (Western Cape)", "Langa (Western Cape)", "Beaufort West (Karoo, Western Cape)",
    # KwaZulu-Natal (Urban, Township & Rural)
    "Umlazi (KwaZulu-Natal)", "Chatsworth (KwaZulu-Natal)", "KwaMashu (KwaZulu-Natal)",
    "Pietermaritzburg (KwaZulu-Natal)", "Nongoma (Rural KwaZulu-Natal)", "Ixopo (Rural KwaZulu-Natal)",
    # Eastern Cape (Urban, Township & Rural)
    "Mdantsane (Eastern Cape)", "Gqeberha (Eastern Cape)", "Lusikisiki (Rural Eastern Cape)",
    "Mthatha (Eastern Cape)", "Qunu (Rural Eastern Cape)", "Makhanda (Eastern Cape)",
    # Limpopo (Urban & Rural)
    "Polokwane (Limpopo)", "Thohoyandou (Rural Limpopo)", "Tzaneen (Limpopo)", "Giyani (Rural Limpopo)",
    # Mpumalanga, North West, Free State, Northern Cape
    "Mbombela (Mpumalanga)", "Bushbuckridge (Rural Mpumalanga)",
    "Mahikeng (North West)", "Rustenburg (North West)",
    "Mangaung (Free State)", "QwaQwa (Rural Free State)",
    "Kimberley (Northern Cape)", "Upington (Northern Cape)",
]

RURAL_AREAS: List[str] = [
    "Lusikisiki (Rural Eastern Cape)",
    "Nongoma (Rural KwaZulu-Natal)",
    "Thohoyandou (Rural Limpopo)",
    "Giyani (Rural Limpopo)",
    "Bushbuckridge (Rural Mpumalanga)",
    "QwaQwa (Rural Free State)",
    "Ixopo (Rural KwaZulu-Natal)",
    "Qunu (Rural Eastern Cape)",
]

URBAN_AREAS: List[str] = [
    "Soweto (Gauteng)",
    "Sandton (Gauteng)",
    "Khayelitsha (Western Cape)",
    "Umlazi (KwaZulu-Natal)",
    "Gqeberha (Eastern Cape)",
    "Polokwane (Limpopo)",
    "Mbombela (Mpumalanga)",
    "Mangaung (Free State)",
]

TUCKSHOP_ITEMS: List[str] = [
    "chips", "cold drinks", "sweets", "freshly baked bread", "milk", "vetkoek",
    "seasonal fruit", "stationery packs", "airtime vouchers", "samosas", "boerewors rolls"
]

NEEDS: List[str] = [
    "nutritious food", "clean drinking water", "safe shelter", "warm clothing", "basic primary healthcare"
]

WANTS: List[str] = [
    "a latest-model smartphone", "designer sneakers", "a gaming console",
    "fashion jewellery", "a luxury holiday trip", "branded headphones"
]

FINANCIAL_TERMS: List[str] = [
    "capital", "assets", "liabilities", "income", "expenses", "profit", "loss", "savings", "budget"
]

BUSINESS_TYPES: List[str] = [
    "Eco-Friendly Car Wash", "Hair & Braiding Salon", "Solar & Plumbing Services",
    "Bicycle & Scooter Repairs", "Community Bakery & Catering", "Mobile Laundry Services",
    "Fresh Produce Market Stall", "School Stationery & Printing Kiosk"
]

SUPPLIERS: List[str] = [
    "Waltons", "Office National", "Makro", "Metro Cash & Carry",
    "Game Stores", "Builders Warehouse", "Freshmark Wholesalers", "Boxer Superstores"
]

# Self-contained 3-to-4 sentence South African urban & rural case studies (EMS #8, #9)
CASE_STUDIES: List[Dict[str, str]] = [
    {
        "setting": "rural",
        "title": "Agricultural Co-operative in Rural Limpopo",
        "text": (
            "{entrepreneur} lives in {area}, where many households rely on seasonal farming and municipal water tankers. "
            "After noticing that villagers travelled 35 km to buy fresh vegetables and seedlings, {entrepreneur} started a small "
            "community nursery and fresh-produce stall near the local clinic using R1 500 in personal savings. "
            "The business employs two local youth and supplies spinach, tomatoes, and maize meal to nearby families."
        ),
    },
    {
        "setting": "urban",
        "title": "Township Micro-Enterprise in Gauteng",
        "text": (
            "{entrepreneur} operates a busy {business_type} near the main taxi rank in {area}. "
            "Every morning, commuters and learners pass the stall to buy {item_sold} before boarding taxis to school and work. "
            "Although customer demand is high at month-end, {entrepreneur} must carefully manage rising electricity tariffs, stock transport costs from {supplier}, and competition from nearby informal traders."
        ),
    },
    {
        "setting": "rural",
        "title": "Solar & Mobile Charging Kiosk in the Eastern Cape",
        "text": (
            "In the rural village of {area}, grid electricity is often interrupted during stormy weather. "
            "{entrepreneur} invested in two solar panels and a battery bank to open a small kiosk offering phone charging, cold water, and {item_sold}. "
            "Local pensioners and learners now save taxi fare because they no longer have to travel to town for basic services."
        ),
    },
    {
        "setting": "urban",
        "title": "School Entrepreneur's Day Venture",
        "text": (
            "Learners at a high school in {area} organised an Entrepreneur's Day market on the school sports field. "
            "{entrepreneur}'s team conducted a quick survey of 60 learners, borrowed a portable gas stove from home, and purchased bulk ingredients from {supplier} to sell warm {item_sold}. "
            "They recorded every cash sale and expense in a notebook to calculate their net profit at the end of the afternoon."
        ),
    },
]


def get_ems_scenario(rng=None) -> Dict[str, Any]:
    """Generates a rich South African EMS scenario with both urban and rural context."""
    chooser = rng.choice if rng else random.choice
    entrepreneur = chooser(NAMES)
    area = chooser(AREAS)
    item_sold = chooser(TUCKSHOP_ITEMS)
    business_type = chooser(BUSINESS_TYPES)
    supplier = chooser(SUPPLIERS)
    competitor = chooser([s for s in SUPPLIERS if s != supplier] or SUPPLIERS)
    case_template = chooser(CASE_STUDIES)
    case_study_text = case_template["text"].format(
        entrepreneur=entrepreneur,
        area=area,
        item_sold=item_sold,
        business_type=business_type,
        supplier=supplier,
    )
    return {
        "entrepreneur": entrepreneur,
        "area": area,
        "rural_area": chooser(RURAL_AREAS),
        "urban_area": chooser(URBAN_AREAS),
        "item_sold": item_sold,
        "business_type": business_type,
        "competitor": competitor,
        "supplier": supplier,
        "case_study_title": case_template["title"],
        "case_study_text": case_study_text,
    }


def get_random_need_and_want(rng=None) -> Dict[str, str]:
    chooser = rng.choice if rng else random.choice
    return {
        "need": chooser(NEEDS),
        "want": chooser(WANTS),
    }
