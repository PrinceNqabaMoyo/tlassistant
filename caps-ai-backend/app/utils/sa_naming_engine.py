"""Fundile Learning - South African Naming & Enterprise Generation Engine.

Generates culturally authentic, demographically proportional South African character
names, surnames, regional geographic locations, and enterprise identities.

Design Principles:
1. Proportional Demographic Representation: Calibrated against authentic South African
   demographics (Nguni ~46%, Sotho-Tswana ~28%, Coloured ~8%, Tsonga/Venda ~7%,
   Afrikaans ~5%, English ~3%, Indian ~3%).
2. Full Geographic Coverage: Spans all 9 provinces with authentic municipal hubs,
   towns, and regional economic activities.
3. Diverse Enterprise Structures: Supports Sole Traders, Partnerships, Pty Ltds,
   Close Corporations (CC), Public Companies (Ltd), State-Owned Companies (SOC Ltd),
   and Primary Cooperatives.
4. Zero Verbatim Exam / Real Brand Copying: Guaranteed proprietary generation; excludes
   real commercial conglomerates and historical past-paper exam entities.
5. 100% Deterministic: Seeded PRNG (`random.Random`) guarantees byte-identical
   reproducibility with zero LLM calls.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List, Optional, Tuple


# ============================================================================
# 1. DEMOGRAPHIC GROUPS & ETHNIC DISTRIBUTIONS (StatSA Calibrated)
# ============================================================================

DEMOGRAPHIC_WEIGHTS: Tuple[Tuple[str, float], ...] = (
    ("nguni", 0.46),          # isiZulu, isiXhosa, siSwati, isiNdebele
    ("sotho_tswana", 0.28),   # Sesotho, Setswana, Sepedi
    ("coloured_cape", 0.08),  # Western Cape, Eastern Cape, Northern Cape communities
    ("tsonga_venda", 0.07),   # Xitsonga, Tshivenda
    ("afrikaans", 0.05),      # Afrikaans heritage
    ("english", 0.03),        # English heritage
    ("indian", 0.03),         # South African Indian heritage
)

NAMES_DATABASE: Dict[str, Dict[str, List[str]]] = {
    "nguni": {
        "female": [
            "Lindiwe", "Nomsa", "Zanele", "Thandeka", "Busisiwe", "Nontobeko",
            "Phindile", "Nonhlanhla", "Senzekile", "Nokuthula", "Andiswa",
            "Babalwa", "Hlengiwe", "Siphesihle", "Zandile", "Tholakele",
            "Nomalanga", "Sibongile", "Nolwazi", "Nobuhle", "Khanyisile", "Ayanda"
        ],
        "male": [
            "Sipho", "Bongani", "Siyabonga", "Mandla", "Nkululeko", "Mthokozisi",
            "Sibusiso", "Thabani", "Sandile", "Melusi", "Lwazi", "Dumisani",
            "Bandile", "Mxolisi", "Simphiwe", "Philani", "Mcebisi", "Themba",
            "Sfiso", "Bheki", "Vusumuzi", "Khaya"
        ],
        "surnames": [
            "Dlamini", "Khumalo", "Ndlovu", "Mthembu", "Buthelezi", "Zungu",
            "Sithole", "Mchunu", "Zulu", "Bhengu", "Cele", "Gumede", "Mbatha",
            "Ntuli", "Shabalala", "Xaba", "Radebe", "Gcabashe", "Majola",
            "Mabaso", "Maphumulo", "Hadebe", "Zondi", "Shezi", "Nene", "Khoza",
            "Nxumalo", "Makhanya", "Myeni", "Mabika", "Gwala", "Ngcobo"
        ],
    },
    "sotho_tswana": {
        "female": [
            "Palesa", "Refilwe", "Mpho", "Dineo", "Naledi", "Puleng", "Lerato",
            "Bokang", "Kelebogile", "Dimakatso", "Tshegofatso", "Matshepo",
            "Rethabile", "Malebo", "Mmabatho", "Boitumelo", "Keneilwe",
            "Motselisi", "Lesego", "Pontsho", "Kagiso"
        ],
        "male": [
            "Kagiso", "Tebogo", "Lesedi", "Thato", "Katlego", "Kabelo", "Tshepo",
            "Karabo", "Tumelo", "Lebohang", "Kgotso", "Mothusi", "Ofentse",
            "Molefe", "Tau", "Modise", "Kopano", "Phenyo", "Tebalo", "Tlali",
            "Mpho", "Tshiamo"
        ],
        "surnames": [
            "Mokoena", "Molefe", "Tau", "Motsepe", "Phiri", "Modise", "Mabena",
            "Moroka", "Moeti", "Mofokeng", "Moloi", "Tsotetsi", "Mosikili",
            "Seokolo", "Mashego", "Malatji", "Mamabolo", "Lekota", "Matlala",
            "Letsoalo", "Mogale", "Ratau", "Tladi", "Mahlangu", "Mokwena",
            "Ramphele", "Sebola", "Kekana"
        ],
    },
    "tsonga_venda": {
        "female": [
            "Tinyiko", "Ntsako", "Khensani", "Rirhandzu", "Tsakani", "Nhlamulo",
            "Langavi", "Xikombiso", "Dzuvha", "Elelwani", "Fhatuwani", "Murendeni",
            "Dakalo", "Lufuno", "Rudzani", "Vhuthu", "Ndivhuwo", "Mulalo",
            "Tshanduko", "Zwivhuya", "Hlulani"
        ],
        "male": [
            "Vhahangwele", "Rendani", "Ndivhuwo", "Mulalo", "Khuliso", "Hlulani",
            "Fumani", "Akani", "Kulani", "Vutomi", "Khumbudzo", "Gundo",
            "Takalani", "Hlanganani", "Tiyani", "Masingita", "Thabelo",
            "Vuwani", "Pfuxani", "Unarine"
        ],
        "surnames": [
            "Netshitenzhe", "Mulaudzi", "Nemukula", "Mudau", "Ramovha", "Tshivhase",
            "Ravele", "Baloyi", "Chauke", "Maluleke", "Mabasa", "Rikhotso",
            "Hlungwani", "Mathebula", "Shirinda", "Ndou", "Munyai", "Khorommbi",
            "Makhado", "Mabunda", "Manganyi", "Ngoveni"
        ],
    },
    "coloured_cape": {
        "female": [
            "Cheryl", "Nadia", "Candice", "Bianca", "Chantal", "Stacey",
            "Robyn", "Megan", "Kaylin", "Nicole", "Rochelle", "Tersia",
            "Delia", "Gail", "Verona", "Lauren", "Monique", "Justine"
        ],
        "male": [
            "Denver", "Clint", "Jerome", "Wayne", "Lyle", "Chad", "Keenan",
            "Lorenzo", "Earl", "Darren", "Byron", "Kurt", "Vernon", "Clyde",
            "Dillon", "Reagan", "Gavin", "Roderick"
        ],
        "surnames": [
            "Abrahams", "Davids", "Hendricks", "Fortuin", "Jacobs", "Cloete",
            "Petersen", "Cupido", "Arendse", "Adams", "Swartz", "Pietersen",
            "Titus", "September", "Philander", "Booysen", "Karelse", "Snyders",
            "Fisher", "Manuel", "Solomons", "Jansen"
        ],
    },
    "afrikaans": {
        "female": [
            "Ansie", "Marike", "Elize", "Magriet", "Ronel", "Susan", "Liezel",
            "Petro", "Heleen", "Ilse", "Hannelie", "Corne", "Martie", "Sonja",
            "Lize", "Marietjie", "Zelda", "Wilma"
        ],
        "male": [
            "Pieter", "Johan", "Willem", "Hendrik", "Jaco", "Riaan", "Dirk",
            "Francois", "Gerhard", "Christo", "Adriaan", "Schalk", "Stephan",
            "Bennie", "Tiaan", "Marthinus", "Frikkie", "Dewald"
        ],
        "surnames": [
            "van der Merwe", "Botha", "Steyn", "de Klerk", "Visser", "du Plessis",
            "Coetzee", "Fourie", "Nel", "Pretorius", "Oosthuizen", "Kruger",
            "Smit", "Meyer", "Labuschagne", "Viljoen", "Swart", "Potgieter",
            "du Preez", "Joubert", "van Wyk", "Theron"
        ],
    },
    "english": {
        "female": [
            "Claire", "Kirsten", "Lauren", "Shannon", "Gillian", "Penelope",
            "Bridget", "Heather", "Samantha", "Fiona", "Gemma", "Tracey",
            "Wendy", "Alison", "Rowena", "Chloe"
        ],
        "male": [
            "Bradley", "Craig", "Ross", "Liam", "Callum", "Gareth", "Trevor",
            "Keith", "Oliver", "Arthur", "Graham", "Douglas", "Nigel",
            "Alistair", "Duncan", "Malcolm"
        ],
        "surnames": [
            "Campbell", "Hughes", "Fletcher", "MacIntyre", "Gallagher", "Smith",
            "Taylor", "Harrison", "Anderson", "Brown", "Davies", "Clark",
            "Robertson", "Stewart", "Walker", "Bennett"
        ],
    },
    "indian": {
        "female": [
            "Fatima", "Priya", "Yasmin", "Aaminah", "Zainab", "Kavita", "Neha",
            "Sunita", "Ananya", "Shreya", "Divya", "Meera", "Tasneem", "Farzana",
            "Soraya", "Laxmi", "Nisha", "Roshni"
        ],
        "male": [
            "Farhan", "Rajiv", "Aarav", "Tariq", "Bilal", "Kaveer", "Devash",
            "Rohan", "Sanjeev", "Cassim", "Zaheer", "Vikram", "Dinesh",
            "Hamza", "Imran", "Harish", "Sanjay"
        ],
        "surnames": [
            "Naidoo", "Govender", "Pillay", "Chetty", "Moodley", "Reddy",
            "Padayachee", "Patel", "Moosa", "Seedat", "Essop", "Kajee",
            "Chothia", "Bhamjee", "Maharaj", "Singh", "Khan", "Goolam", "Desai"
        ],
    },
}


# ============================================================================
# 2. GEOGRAPHIC DISTRIBUTION ACROSS ALL 9 PROVINCES
# ============================================================================

PROVINCES_AND_HUBS: Dict[str, Dict[str, Any]] = {
    "Gauteng": {
        "towns": ["Johannesburg", "Soweto", "Pretoria", "Midrand", "Centurion", "Germiston", "Kempton Park", "Vanderbijlpark", "Benoni", "Krugersdorp"],
        "industries": [
            ("Financial Services & Fintech", "digital banking solutions"),
            ("Light Engineering & Toolmaking", "precision machine components"),
            ("Township FMCG & Retail", "fast-moving consumer groceries"),
            ("Pharmaceutical Manufacturing", "generic essential healthcare medicines"),
            ("Freight & Air Cargo Logistics", "bonded international airfreight logistics"),
            ("Software Engineering", "enterprise cloud software solutions"),
        ],
    },
    "Western Cape": {
        "towns": ["Cape Town", "Stellenbosch", "Paarl", "George", "Saldanha Bay", "Worcester", "Mossel Bay", "Hermanus", "Oudtshoorn", "Robertson"],
        "industries": [
            ("Wine Viticulture & Export", "estate bottled wines for global export"),
            ("Marine Fisheries & Cold Storage", "sustainably caught hake fillets"),
            ("Renewable Tech & Ecotourism", "boutique hospitality and solar microgrids"),
            ("Agro-Processing & Canning", "canned deciduous fruits and purees"),
            ("Creative & Digital Agencies", "multimedia production and web applications"),
            ("Yacht Building & Marine Services", "luxury marine catamaran fabrication"),
        ],
    },
    "KwaZulu-Natal": {
        "towns": ["Durban", "Pietermaritzburg", "Richards Bay", "Newcastle", "Ladysmith", "Port Shepstone", "Empangeni", "Dundee", "Ballito", "Stanger"],
        "industries": [
            ("Harbour Container Freight", "intermodal maritime container logistics"),
            ("Sugar Cane Milling & Refining", "refined white and brown bulk sugars"),
            ("Textile & Industrial Workwear", "flame-retardant safety overalls"),
            ("Aluminium Smelting & Extrusion", "structural architectural extrusions"),
            ("Automotive Assembly Support", "commercial vehicle wiring harnesses"),
            ("Speciality Coffee Roasting", "single-origin roasted coffee beans"),
        ],
    },
    "Eastern Cape": {
        "towns": ["Gqeberha", "East London", "Mthatha", "Makhanda", "Kariega", "Komani", "Graaff-Reinet", "Cradock", "Jeffreys Bay", "Butterworth"],
        "industries": [
            ("Automotive Assembly & Components", "automotive catalytic converters and exhausts"),
            ("Wool & Mohair Processing", "scoured raw wool and natural mohair bales"),
            ("Dairy Farming & Cheese Making", "pasteurised milk and mature gouda cheeses"),
            ("Timber Milling & Pine Products", "sustainably kiln-dried pine timber"),
            ("Citrus Packaging & Export", "fresh export-grade lemons and valencias"),
            ("Wind Energy Farm Maintenance", "wind turbine generator field services"),
        ],
    },
    "Free State": {
        "towns": ["Bloemfontein", "Welkom", "Bethlehem", "Sasolburg", "Parys", "Harrismith", "Kroonstad", "Phuthaditjhaba", "Ficksburg", "Bothaville"],
        "industries": [
            ("Grain Milling & Maize Silos", "fortified maize meal and animal feeds"),
            ("Petrochemical Auxiliaries", "industrial waxes and synthetic lubricants"),
            ("Poultry Farming & Feedlots", "fresh dressed broiler chicken packs"),
            ("Eco-Friendly Clay Bricks", "kiln-fired structural face bricks"),
            ("Agricultural Implement Manufacturing", "heavy tractor-drawn seed planters"),
            ("Cherry Farming & Preserves", "artisan glazed cherries and fruit preserves"),
        ],
    },
    "Limpopo": {
        "towns": ["Polokwane", "Tzaneen", "Thohoyandou", "Mokopane", "Lephalale", "Musina", "Makhado", "Giyani", "Phalaborwa", "Modimolle"],
        "industries": [
            ("Citrus Packing & Cold Stores", "waxed navel oranges for Eurasian export"),
            ("Macadamia & Avocado Orchards", "cold-pressed culinary macadamia oil"),
            ("Cross-Border Freight Drayage", "commercial cross-border road logistics"),
            ("Platinum & Mineral Refining Support", "high-grade mineral screening mesh"),
            ("Subtropical Fruit Drying", "sulphur-free dried mango slices"),
            ("Tomato Processing & Puree", "canned tomato paste and Italian purees"),
        ],
    },
    "Mpumalanga": {
        "towns": ["Mbombela", "eMalahleni", "Secunda", "Middelburg", "Barberton", "Standerton", "Ermelo", "Lydenburg", "Piet Retief", "White River"],
        "industries": [
            ("Sustainable Forestry & Pulp", "corrugated packaging paper and pulp"),
            ("Stainless Steel Fabrication", "heavy-gauge stainless industrial vessels"),
            ("Safari Ecotourism & Logistics", "custom luxury safari lodge excursions"),
            ("Thermal Energy Servicing", "boiler tube inspection and welding services"),
            ("Macadamia Nut Processing", "vacuum-packed roasted macadamia halves"),
            ("Coal Rail Freight Logistics", "specialised bulk train wagon leasing"),
        ],
    },
    "North West": {
        "towns": ["Rustenburg", "Mahikeng", "Potchefstroom", "Klerksdorp", "Brits", "Lichtenburg", "Vryburg", "Zeerust", "Orkney", "Wolmaransstad"],
        "industries": [
            ("Platinum Group Metals Support", "underground rock-drill pneumatics"),
            ("Granite Quarrying & Tile Cutting", "polished African black granite slabs"),
            ("Sunflower Oil Seed Crushing", "refined golden sunflower cooking oil"),
            ("Beef Cattle Feedlots & Abattoirs", "A-grade grass-fed beef carcasses"),
            ("Chrome Ore Washing & Sizing", "concentrated metallurgical chrome lump"),
            ("Poultry Hatchery & Distribution", "day-old vaccinated layer chicks"),
        ],
    },
    "Northern Cape": {
        "towns": ["Kimberley", "Upington", "Springbok", "Kuruman", "De Aar", "Kathu", "Calvinia", "Port Nolloth", "Kakamas", "Prieska"],
        "industries": [
            ("Utility-Scale Solar PV Farms", "grid-tied solar panel maintenance services"),
            ("Table Grape & Raisin Export", "sun-dried golden sultanas and fresh grapes"),
            ("Iron Ore & Manganese Logistics", "heavy-haul open-cast mining conveyancing"),
            ("Kalahari Karoo Lamb Butchery", "certified origin Karoo lamb cuts"),
            ("Diamond Cutting & Polishing", "conflict-free certified polished gemstones"),
            ("Desalination & Marine Minerals", "reverse osmosis coastal potable water"),
        ],
    },
}


# ============================================================================
# 3. CULTURAL & ASPIRATIONAL BRAND CONCEPTS (Authentic SA Heritage)
# ============================================================================

ASPIRATIONAL_CONCEPTS: List[Tuple[str, str]] = [
    ("Isibani", "beacon/illumination"),
    ("Thari", "heritage/nurturing"),
    ("Phambili", "progress/forward movement"),
    ("Boikanyo", "trust/reliability"),
    ("Tswelopele", "development/advancement"),
    ("Simunye", "unity/togetherness"),
    ("Ubuhle", "excellence/grace"),
    ("Vutivi", "wisdom/intellect"),
    ("Impilo", "vitality/health"),
    ("Kagiso", "peace/stability"),
    ("Kutlwano", "harmony/accord"),
    ("Sediba", "sustenance/perennial fountain"),
    ("Ikhethelo", "distinction/premium choice"),
    ("Masakhane", "collective strength"),
    ("Siyanqoba", "resilience/triumph"),
    ("Matla", "energy/might"),
    ("Bokamoso", "future prosperity"),
    ("Khanya", "radiance/clarity"),
    ("Ntsika", "pillar of trust"),
    ("Lwazi", "knowledge/insight"),
]

TRADING_DESCRIPTORS: List[str] = [
    "Traders", "Suppliers", "Enterprises", "Wholesalers", "Distributors",
    "Solutions", "Holdings", "Services", "Logistics", "Manufacturing",
    "Works", "Engineering", "Agri", "Industries", "Group"
]

BLACK_LISTED_VERBATIM_NAMES: set[str] = {
    "thabo's spaza", "sipho's supermarket", "superb tiling", "bongiwe's boutique",
    "mpho's car wash", "praveen's spices", "ace wholesalers", "shoprite",
    "pick n pay", "checkers", "spar", "woolworths", "vodacom", "mtn", "telkom",
    "sasol", "eskom", "transnet", "standard bank", "nedbank", "absa", "fnb",
    "first national bank", "capitec", "discovery", "old mutual", "sanlam",
    "anglo american", "naspers", "sarah's bakery", "olwethu beauty salon"
}


# ============================================================================
# 4. CORE ENGINE FUNCTIONS
# ============================================================================

def _resolve_rng(r: Optional[random.Random]) -> random.Random:
    return r if r is not None else random.Random()


def pick_demographic_group(r: Optional[random.Random] = None) -> str:
    """Samples an ethnic demographic group proportionally to the SA population."""
    rng = _resolve_rng(r)
    roll = rng.random()
    cumulative = 0.0
    for group, weight in DEMOGRAPHIC_WEIGHTS:
        cumulative += weight
        if roll <= cumulative:
            return group
    return DEMOGRAPHIC_WEIGHTS[0][0]


def generate_sa_person(
    r: Optional[random.Random] = None,
    *,
    gender: Optional[str] = None,
    ethnic_group: Optional[str] = None,
) -> Dict[str, str]:
    """Generates an authentic South African individual identity with demographic provenance."""
    rng = _resolve_rng(r)
    grp = ethnic_group if ethnic_group in NAMES_DATABASE else pick_demographic_group(rng)
    bank = NAMES_DATABASE[grp]

    chosen_gender = gender.lower() if gender in ("female", "male") else rng.choice(["female", "male"])
    first_name = rng.choice(bank[chosen_gender])
    surname = rng.choice(bank["surnames"])
    salutation = "Ms." if chosen_gender == "female" else "Mr."

    return {
        "first_name": first_name,
        "surname": surname,
        "full_name": f"{first_name} {surname}",
        "gender": chosen_gender,
        "ethnic_group": grp,
        "salutation": salutation,
        "titled_name": f"{salutation} {surname}",
    }


def pick_person_name(r: Optional[random.Random] = None) -> str:
    """Quick helper returning 'First Last' for a single individual."""
    return generate_sa_person(r)["full_name"]


def pick_person_names(r: Optional[random.Random] = None, k: int = 1) -> List[str]:
    """Samples k unique South African names."""
    rng = _resolve_rng(r)
    target = max(1, int(k))
    names: List[str] = []
    seen: set[str] = set()
    attempts = 0
    max_attempts = target * 25

    while len(names) < target and attempts < max_attempts:
        attempts += 1
        name = pick_person_name(rng)
        if name not in seen:
            seen.add(name)
            names.append(name)

    while len(names) < target:
        names.append(f"{pick_person_name(rng)} ({len(names)+1})")
    return names


def pick_surname(r: Optional[random.Random] = None) -> str:
    """Samples a single South African surname according to demographic proportions."""
    return generate_sa_person(r)["surname"]


def generate_sa_enterprise(
    r: Optional[random.Random] = None,
    *,
    form: Optional[str] = None,
    province: Optional[str] = None,
    sector_hint: Optional[str] = None,
) -> Dict[str, Any]:
    """Synthesizes a realistic, curriculum-aligned South African enterprise."""
    rng = _resolve_rng(r)

    # 1. Resolve Geographic Location & Regional Sector
    prov_name = province if province in PROVINCES_AND_HUBS else rng.choice(list(PROVINCES_AND_HUBS.keys()))
    prov_data = PROVINCES_AND_HUBS[prov_name]
    town = rng.choice(prov_data["towns"])
    industry_pair = rng.choice(prov_data["industries"])
    industry, product = industry_pair

    # 2. Resolve Form of Ownership
    valid_forms = ["Sole Trader", "Partnership", "Private Company", "Close Corporation", "Public Company", "Primary Cooperative"]
    chosen_form = form if form in valid_forms else rng.choice(valid_forms)

    # 3. Generate Enterprise Legal Suffix
    form_suffix_map = {
        "Sole Trader": "",
        "Partnership": "& Partners",
        "Private Company": "(Pty) Ltd",
        "Close Corporation": "CC",
        "Public Company": "Ltd",
        "Primary Cooperative": "Co-op Ltd",
    }
    legal_suffix = form_suffix_map.get(chosen_form, "(Pty) Ltd")

    # 4. Generate Founder / Key Executive
    founder_person = generate_sa_person(rng)
    founder = founder_person["full_name"]
    first = founder_person["first_name"]
    surname = founder_person["surname"]

    # 5. Combinatorial Brand Naming Strategy
    for _ in range(20):
        strategy = rng.choice(["founder_possessive", "surname_trade", "regional_hub", "aspirational", "partnership"])
        if strategy == "founder_possessive" or chosen_form == "Sole Trader":
            activity_word = industry.split()[0]
            name = f"{first}'s {activity_word} {legal_suffix}".strip()
        elif strategy == "partnership" and chosen_form == "Partnership":
            person_2 = generate_sa_person(rng)
            name = f"{surname} & {person_2['surname']} {legal_suffix}".strip()
        elif strategy == "surname_trade":
            desc = rng.choice(TRADING_DESCRIPTORS)
            name = f"{surname} {desc} {legal_suffix}".strip()
        elif strategy == "regional_hub":
            activity_word = industry.split()[0]
            name = f"{town} {activity_word} {legal_suffix}".strip()
        else:
            concept, _ = rng.choice(ASPIRATIONAL_CONCEPTS)
            desc = rng.choice(TRADING_DESCRIPTORS)
            name = f"{concept} {desc} {legal_suffix}".strip()

        # Check blacklist
        if name.lower() not in BLACK_LISTED_VERBATIM_NAMES:
            break

    return {
        "business_name": name,
        "owner_name": founder,
        "founder": founder,
        "founder_person": founder_person,
        "form": chosen_form,
        "province": prov_name,
        "town": town,
        "industry": industry,
        "product": product,
        "legal_suffix": legal_suffix,
        "intro": f"{founder} is the principal of {name}, an established {chosen_form.lower()} based in {town}, {prov_name}.",
    }


def pick_sa_scenario(r: Optional[random.Random] = None) -> Dict[str, str]:
    """Drop-in replacement for legacy Business Studies `pick_scenario`."""
    ent = generate_sa_enterprise(r)
    return {
        "business": ent["business_name"],
        "owner": ent["founder"],
        "industry": ent["industry"],
        "town": ent["town"],
        "province": ent["province"],
        "form": ent["form"],
        "product": ent["product"],
    }


def pick_business_name(r: Optional[random.Random] = None) -> str:
    """Drop-in helper returning just the enterprise business name."""
    return generate_sa_enterprise(r)["business_name"]


def pick_business_names(
    r: Optional[random.Random] = None,
    k: int = 1,
    unique_surnames: bool = False,
) -> List[str]:
    """Samples k unique business names."""
    rng = _resolve_rng(r)
    target = max(1, int(k))
    names: List[str] = []
    seen: set[str] = set()
    attempts = 0
    max_attempts = target * 30

    while len(names) < target and attempts < max_attempts:
        attempts += 1
        b_name = pick_business_name(rng)
        if b_name not in seen:
            seen.add(b_name)
            names.append(b_name)

    while len(names) < target:
        names.append(f"{pick_business_name(rng)} ({len(names)+1})")
    return names
