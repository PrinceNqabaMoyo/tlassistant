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


try:
    from ..sa_naming_engine import (
        pick_person_name as _sa_pick_person_name,
        pick_person_names as _sa_pick_person_names,
        pick_surname as _sa_pick_surname,
        pick_business_name as _sa_pick_business_name,
        pick_business_names as _sa_pick_business_names,
    )
except ImportError:
    from app.utils.sa_naming_engine import (
        pick_person_name as _sa_pick_person_name,
        pick_person_names as _sa_pick_person_names,
        pick_surname as _sa_pick_surname,
        pick_business_name as _sa_pick_business_name,
        pick_business_names as _sa_pick_business_names,
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
    return _sa_pick_person_name(r)


def pick_surname(*, r: random.Random) -> str:
    return _sa_pick_surname(r)


def pick_business_name(*, r: random.Random) -> str:
    return _sa_pick_business_name(r)


def pick_business_names(*, r: random.Random, k: int, unique_surnames: bool = False) -> List[str]:
    return _sa_pick_business_names(r, k=k, unique_surnames=unique_surnames)


def pick_person_names(*, r: random.Random, k: int) -> List[str]:
    return _sa_pick_person_names(r, k=k)

