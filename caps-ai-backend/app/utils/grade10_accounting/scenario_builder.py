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
    owner = r.choice(OWNER_NAMES)
    business = r.choice(BUSINESS_NAMES)
    industry = r.choice(INDUSTRY_TYPES)
    
    return {
        "owner": owner,
        "business": business,
        "industry": industry,
        "intro": f"{owner} owns and operates {business}, a local {industry}. "
    }
