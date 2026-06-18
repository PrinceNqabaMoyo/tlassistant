from __future__ import annotations

import random
from typing import Dict, List, Tuple

AFRICAN_FIRST_NAMES: List[str] = [
    "Samangele",
    "Ben",
    "Erica",
    "Lance",
    "Sthembiso",
    "Mbalenhle",
    "Latita",
    "Nqaba",
    "Nqoba",
    "Lameck",
    "Sukoluhle",
    "Prince",
    "Dumisani",
    "Ayanda",
    "Siyanda",
    "Luyanda",
    "Loyiso",
    "Nanziwe",
    "Lubelihle",
    "Nqobizitha",
    "Ndabezinhle",
    "Amanda",
    "Aluwani",
    "Ambani",
    "Bono",
    "Dakalo",
    "Dzuvha",
    "Elelwani",
    "Hangwani",
    "Khuthandzo",
    "Palesa",
    "Tshepo",
    "Lerato",
    "Andziso",
    "Fanisa",
    "Hlori",
]

AFRICAN_SURNAMES: List[str] = [
    "Mlotshwa",
    "Nyathi",
    "Mazibuko",
    "Manzi",
    "Khumalo",
    "Nxumalo",
    "Kunene",
    "Ramavhona",
    "Nkhumeleni",
    "Mudau",
    "Mbeki",
    "Bukhali",
    "Langa",
    "Madlingozi",
    "Mahambehlala",
    "Mathanzima",
    "Madida",
    "Mpofu",
    "Ngwenya",
    "Kekana",
    "Tau",
    "Roka",
    "Ntwane",
    "Chauke",
]

AFRIKAANS_FIRST_NAMES: List[str] = [
    "Annelie",
    "Elize",
    "Petronella",
    "Magriet",
    "Adriaan",
    "Gert",
    "Johan",
]

AFRIKAANS_SURNAMES: List[str] = [
    "Van de Merwe",
    "Botha",
    "Coetzee",
    "Du Toit",
    "De Cock",
    "Van Wyk",
    "Van Heerden",
    "Van Niekerk",
]

ENGLISH_FIRST_NAMES: List[str] = [
    "Noah",
    "Oliver",
    "James",
    "William",
    "Elizabeth",
    "Amelia",
    "Arthur",
    "Sofia",
    "Cindy",
]

ENGLISH_SURNAMES: List[str] = [
    "Taylor",
    "Brown",
    "Williams",
    "Smith",
    "Johnson",
    "Cooper",
    "Baker",
    "Fletcher",
]

INDIAN_FIRST_NAMES: List[str] = [
    "Erica",
    "Justin",
    "Maya",
    "Salim",
    "Zain",
    "Malik",
    "Ashwin",
    "Aravind",
    "Kamal",
    "Jayesh",
    "Yatika",
    "Simran",
    "Inaya",
    "Vanshika",
    "Amaira",
    "Shivanya",
    "Adrija",
]

INDIAN_SURNAMES: List[str] = [
    "Pillay",
    "Badoo",
    "Badul",
    "Govender",
    "Reddy",
    "Chetty",
    "Moodley",
    "Naicker",
    "Patel",
    "Naidoo",
    "Benny",
    "Khan",
    "Singh",
]

NAME_BANKS: Dict[str, Dict[str, List[str]]] = {
    "african": {"first": AFRICAN_FIRST_NAMES, "surname": AFRICAN_SURNAMES},
    "english": {"first": ENGLISH_FIRST_NAMES, "surname": ENGLISH_SURNAMES},
    "afrikaans": {"first": AFRIKAANS_FIRST_NAMES, "surname": AFRIKAANS_SURNAMES},
    "indian": {"first": INDIAN_FIRST_NAMES, "surname": INDIAN_SURNAMES},
}

NAME_GROUP_WEIGHTS: Tuple[Tuple[str, float], ...] = (
    ("african", 0.70),
    ("afrikaans", 0.10),
    ("english", 0.10),
    ("indian", 0.10),
)


def pick_name_group(*, r: random.Random) -> str:
    roll = r.random()
    cumulative = 0.0
    for key, weight in NAME_GROUP_WEIGHTS:
        cumulative += float(weight)
        if roll < cumulative:
            return key
    return NAME_GROUP_WEIGHTS[-1][0]



def pick_person_name(*, r: random.Random) -> str:
    group = pick_name_group(r=r)
    bank = NAME_BANKS[group]
    first = r.choice(bank["first"])
    surname = r.choice(bank["surname"])
    return f"{first} {surname}"


def pick_surname(*, r: random.Random) -> str:
    group = pick_name_group(r=r)
    bank = NAME_BANKS[group]
    return r.choice(bank["surname"])


def pick_business_name(*, r: random.Random) -> str:
    surname = pick_surname(r=r)
    suffix = r.choice(["Traders", "Enterprise", "Stores", "Suppliers", "Wholesalers", "Distributors"])
    return f"{surname} {suffix}"


def pick_business_names(*, r: random.Random, k: int, unique_surnames: bool = False) -> List[str]:
    target = max(0, int(k))
    out: List[str] = []
    seen = set()
    seen_surnames = set()
    max_attempts = max(20, target * 20)
    attempts = 0
    while len(out) < target and attempts < max_attempts:
        attempts += 1
        if unique_surnames:
            surname = pick_surname(r=r)
            if surname in seen_surnames:
                continue
            suffix = r.choice(["Traders", "Enterprise", "Stores", "Suppliers", "Wholesalers", "Distributors"])
            name = f"{surname} {suffix}"
        else:
            surname = ""
            name = pick_business_name(r=r)
        if name in seen:
            continue
        out.append(name)
        seen.add(name)
        if unique_surnames:
            seen_surnames.add(surname)
    while len(out) < target:
        out.append(pick_business_name(r=r))
    return out


def pick_person_names(*, r: random.Random, k: int) -> List[str]:
    target = max(0, int(k))
    out: List[str] = []
    seen = set()
    max_attempts = max(20, target * 20)
    attempts = 0
    while len(out) < target and attempts < max_attempts:
        attempts += 1
        name = pick_person_name(r=r)
        if name in seen:
            continue
        out.append(name)
        seen.add(name)
    while len(out) < target:
        out.append(pick_person_name(r=r))
    return out
