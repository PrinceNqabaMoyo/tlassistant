from __future__ import annotations

import random
from typing import Iterable, List, Sequence

from ..sole_trader.names import pick_person_name as _pick_person_name
from ..sole_trader.names import pick_surname as _pick_surname

GENERAL_BUSINESS_SUFFIXES: Sequence[str] = (
    'Traders',
    'Retailers',
    'Suppliers',
    'Services',
    'Solutions',
    'Fashions',
    'Manufacturers',
)

MANUFACTURING_SUFFIXES: Sequence[str] = (
    'Manufacturers',
    'Foods',
    'Processors',
    'Textiles',
    'Works',
    'Producers',
)

SUPPLIER_SUFFIXES: Sequence[str] = (
    'Suppliers',
    'Wholesalers',
    'Distributors',
    'Materials',
    'Inputs',
)

RETAIL_AND_LIFESTYLE_SUFFIXES: Sequence[str] = (
    'Retailers',
    'Fashions',
    'Sportswear',
    'Apparel',
    'Boutique',
    'Activewear',
)

INDUSTRY_SPECIFIC_SUFFIXES = {
    'manufacturing': MANUFACTURING_SUFFIXES,
    'supplier': SUPPLIER_SUFFIXES,
    'retail_lifestyle': RETAIL_AND_LIFESTYLE_SUFFIXES,
    'general': GENERAL_BUSINESS_SUFFIXES,
}


def _pick_suffix(*, r: random.Random, suffixes: Iterable[str] | None = None) -> str:
    bank = list(suffixes or GENERAL_BUSINESS_SUFFIXES)
    return r.choice(bank)



def pick_owner_name(*, r: random.Random) -> str:
    return _pick_person_name(r=r)



def pick_business_name(*, r: random.Random, suffixes: Iterable[str] | None = None) -> str:
    surname = _pick_surname(r=r)
    suffix = _pick_suffix(r=r, suffixes=suffixes)
    return f"{surname} {suffix}"



def pick_supplier_name(*, r: random.Random) -> str:
    return pick_business_name(r=r, suffixes=SUPPLIER_SUFFIXES)



def pick_distinct_business_names(*, r: random.Random, k: int, suffixes: Iterable[str] | None = None) -> List[str]:
    target = max(0, int(k))
    out: List[str] = []
    seen = set()
    attempts = 0
    max_attempts = max(20, target * 20)
    while len(out) < target and attempts < max_attempts:
        attempts += 1
        name = pick_business_name(r=r, suffixes=suffixes)
        if name in seen:
            continue
        out.append(name)
        seen.add(name)
    while len(out) < target:
        out.append(pick_business_name(r=r, suffixes=suffixes))
    return out
