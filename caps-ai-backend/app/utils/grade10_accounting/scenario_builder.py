import random
from typing import Dict, Optional, Tuple, List

BUSINESS_NAMES = [
    "Khumalo Traders",
    "Mokoena Stores",
    "Dlamini Spares",
    "Mashoke Traders",
    "Lucia Traders",
    "Sunshine Traders",
    "Mngadi Deliveries",
    "Sizwe Wholesale",
    "Rainbow Furnishers",
    "Irma Traders",
]

OWNER_NAMES = [
    "A. Khumalo",
    "B. Maseko",
    "C. Naidoo",
    "Moses Mngadi",
    "Sizwe Ntakumba",
    "Ray Ndlovu",
    "Irma Swart",
    "Ernst Rhinehart",
    "Melt Masuku",
]

INDUSTRY_TYPES = [
    "gift shop",
    "grocery store",
    "delivery service",
    "furniture retail store",
    "hardware shop",
    "clothing boutique",
]

try:
    from ..sa_naming_engine import generate_sa_enterprise, generate_sa_person
except ImportError:
    from app.utils.sa_naming_engine import generate_sa_enterprise, generate_sa_person

def _rng(seed: Optional[int]) -> random.Random:
    r = random.Random()
    if seed is None:
        r.seed()
    else:
        r.seed(int(seed))
    return r

def build_scenario(*, seed: Optional[int] = None) -> Dict[str, str]:
    """Generates a random business scenario to be used as context in theoretical questions."""
    r = _rng(seed)
    ent = generate_sa_enterprise(r, form="Sole Trader")
    owner = ent["founder"]
    business = ent["business_name"]
    industry = ent["industry"]
    town = ent["town"]
    province = ent["province"]

    return {
        "owner": owner,
        "business": business,
        "industry": industry,
        "town": town,
        "province": province,
        "intro": f"{owner} owns and operates {business}, a local {industry} based in {town}, {province}. "
    }
