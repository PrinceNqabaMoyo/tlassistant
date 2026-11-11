"""
South African EMS Case Studies Bank (Grades 7–9)
100% Aligned with South African National Curriculum Standards.

Provides 20 rich, self-contained South African case studies spanning all 9 provinces,
urban, peri-urban, township, and rural economic contexts for Economic and Management Sciences.
"""
from typing import Any, Dict, List
import random

SA_EMS_CASE_STUDIES: List[Dict[str, Any]] = [
    {
        "id": "cs_01",
        "business_name": "Zululand Solar & Spaza Co-op",
        "owner": "Nokuthula Zulu",
        "location": "Empangeni, KwaZulu-Natal",
        "sector": "Tertiary / Retail & Renewable Energy",
        "ownership_form": "Co-operative",
        "narrative": (
            "Nokuthula Zulu and four local women in Empangeni pooled R45 000 in personal savings to establish "
            "Zululand Solar & Spaza Co-op. The business sells essential household groceries (maize meal, cooking oil, "
            "and fresh vegetables) alongside affordable solar lanterns and phone-charging services. During load-shedding, "
            "demand for solar lanterns increased by 65%, allowing the co-operative to hire two youth assistants."
        ),
        "monthly_revenue": 38500,
        "monthly_expenses": 24200,
        "assets": {"Solar Charging Kiosk": 28000, "Trading Inventory": 14500, "Cash in Bank": 19800},
        "liabilities": {"Trade Creditors (Wholesalers)": 6400},
    },
    {
        "id": "cs_02",
        "business_name": "Karoo Rooibos & Honey Apiary",
        "owner": "Pieter van der Merwe",
        "location": "Clanwilliam, Western Cape",
        "sector": "Primary & Secondary (Agro-processing)",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Pieter van der Merwe harvests organic fynbos honey and wild rooibos in Clanwilliam. Instead of selling "
            "raw bulk honey at low farm-gate prices, he invested R60 000 in a bottling and labelling unit to package "
            "infused honey jars for supermarkets across the Western Cape."
        ),
        "monthly_revenue": 52000,
        "monthly_expenses": 31500,
        "assets": {"Bottling Equipment": 60000, "Delivery Bakkie": 145000, "Packaging Stock": 8200},
        "liabilities": {"Agri-Equipment Loan": 42000},
    },
    {
        "id": "cs_03",
        "business_name": "Polokwane Fresh Produce Market",
        "owner": "kabelo Mokoena",
        "location": "Polokwane, Limpopo",
        "sector": "Primary / Agriculture & Distribution",
        "ownership_form": "Close Corporation / Partnership",
        "narrative": (
            "Kabelo Mokoena operates a drip-irrigated tomato and spinach farm outside Polokwane. By using water-saving "
            "drip lines, the farm reduced water expenses by 35% while supplying fresh crates daily to hawkers and "
            "school nutrition programmes across Capricorn District."
        ),
        "monthly_revenue": 64000,
        "monthly_expenses": 41000,
        "assets": {"Drip Irrigation System": 75000, "Cold Storage Room": 55000, "Debtors Control": 12400},
        "liabilities": {"Land Bank Facility": 38000, "Creditors Control": 9100},
    },
    {
        "id": "cs_04",
        "business_name": "Soweto Kasi Tech Repairs",
        "owner": "Thabo Molefe",
        "location": "Soweto, Gauteng",
        "sector": "Tertiary / Technical Services",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Thabo Molefe trained in micro-soldering and opened Soweto Kasi Tech Repairs near Bara Taxi Rank. "
            "He repairs smartphones, laptops, and POS terminals for local commuters and small businesses, issuing "
            "digital receipts via EFT and mobile speedpoint."
        ),
        "monthly_revenue": 29400,
        "monthly_expenses": 15800,
        "assets": {"Diagnostic & Soldering Station": 22000, "Spare Screens Inventory": 11500, "Bank": 16200},
        "liabilities": {"Supplier Account (TechParts SA)": 4800},
    },
    {
        "id": "cs_05",
        "business_name": "Algoa Bay Marine Logistics (Pty) Ltd",
        "owner": "Sipho Ndlovu & Partners",
        "location": "Gqeberha, Eastern Cape",
        "sector": "Tertiary / Transport & Logistics",
        "ownership_form": "Private Company",
        "narrative": (
            "Algoa Bay Marine Logistics transports automotive components and citrus exports between local factories "
            "and the Port of Ngqura in Gqeberha. Rising diesel prices required the management team to optimise route "
            "scheduling and preventative fleet maintenance."
        ),
        "monthly_revenue": 185000,
        "monthly_expenses": 132000,
        "assets": {"Fleet Vehicles": 680000, "Office Computers": 34000, "Bank": 92000},
        "liabilities": {"WesBank Vehicle Finance": 290000, "Creditors Control": 28500},
    },
    {
        "id": "cs_06",
        "business_name": "Mangaung Artisanal Bakery",
        "owner": "Lerato Mokoena",
        "location": "Bloemfontein, Free State",
        "sector": "Secondary / Food Manufacturing",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Lerato Mokoena runs Mangaung Artisanal Bakery in Bloemfontein, baking wholewheat loaves, vetkoek, and "
            "scones using locally milled Free State wheat flour. She supplies three nearby boarding schools on 30-day "
            "credit terms and sells directly to walk-in cash customers."
        ),
        "monthly_revenue": 46800,
        "monthly_expenses": 29900,
        "assets": {"Rotary Convection Ovens": 85000, "Flour & Ingredients Stock": 11200, "Debtors": 9600},
        "liabilities": {"Oven Finance Loan": 31000, "Millers Creditors": 7400},
    },
    {
        "id": "cs_07",
        "business_name": "Lowveld Macadamia & Citrus Processors",
        "owner": "Bongani Sithole",
        "location": "Mbombela, Mpumalanga",
        "sector": "Secondary / Agro-Processing",
        "ownership_form": "Partnership",
        "narrative": (
            "In Mbombela, Bongani Sithole and his partner crack, dry, and vacuum-pack macadamia nuts sourced from "
            "emerging smallholder farmers. By grading nuts to export quality, the business earns foreign exchange "
            "and pays fair farm-gate prices."
        ),
        "monthly_revenue": 112000,
        "monthly_expenses": 78400,
        "assets": {"Nut Cracking & Drying Plant": 210000, "Packing Material": 16000, "Bank": 48000},
        "liabilities": {"Industrial Development Loan": 85000},
    },
    {
        "id": "cs_08",
        "business_name": "Kimberley Diamond Solar Wash",
        "owner": "Rethabile Modise",
        "location": "Kimberley, Northern Cape",
        "sector": "Tertiary / Eco-Services",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Operating in water-scarce Kimberley, Rethabile Modise started an eco-friendly mobile car and fleet wash "
            "that uses greywater filtration and high-pressure steam cleaners, cutting water usage per vehicle from "
            "120 litres to 18 litres."
        ),
        "monthly_revenue": 24500,
        "monthly_expenses": 13200,
        "assets": {"Steam Cleaning Trailer": 38000, "Water Recycling Unit": 19000, "Cash Float": 2500},
        "liabilities": {"Small Enterprise Finance Loan": 14000},
    },
    {
        "id": "cs_09",
        "business_name": "Rustenburg Platinum Workwear Stitchers",
        "owner": "Mpho Khumalo",
        "location": "Rustenburg, North West",
        "sector": "Secondary / Textile Manufacturing",
        "ownership_form": "Close Corporation",
        "narrative": (
            "Mpho Khumalo's workshop in Rustenburg manufactures flame-retardant overalls and reflective vests for "
            "surrounding platinum mines and contractors. Bulk fabric is purchased on credit from Durban textile mills, "
            "cut and sewn locally by 12 skilled machinists."
        ),
        "monthly_revenue": 94000,
        "monthly_expenses": 66500,
        "assets": {"Industrial Sewing Machines": 96000, "Fabric Rolls Inventory": 27000, "Debtors": 31000},
        "liabilities": {"Textile Mill Creditors": 22500},
    },
    {
        "id": "cs_10",
        "business_name": "uMlazi Green Recycling & Upcycling",
        "owner": "Sibusiso Dlamini",
        "location": "Durban, KwaZulu-Natal",
        "sector": "Secondary & Tertiary / Circular Economy",
        "ownership_form": "Co-operative",
        "narrative": (
            "Sibusiso Dlamini coordinates a network of 30 community waste pickers in uMlazi who collect PET plastic, "
            "cardboard, and aluminium cans. The co-operative bales and sells sorted recyclables to pelletising mills, "
            "cleaning streets while generating steady weekly income."
        ),
        "monthly_revenue": 41200,
        "monthly_expenses": 26800,
        "assets": {"Hydraulic Baling Press": 64000, "Weighing Scales": 8500, "Bank": 21400},
        "liabilities": {"Equipment Payable": 15000},
    },
    {
        "id": "cs_11",
        "business_name": "Mthatha Rural Timber & Furniture",
        "owner": "Lindiwe Ndamase",
        "location": "Mthatha, Eastern Cape",
        "sector": "Secondary / Woodwork & Carpentry",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Lindiwe Ndamase sources sustainable pine timber from Eastern Cape plantations and crafts school desks, "
            "bookshelves, and household wardrobes in Mthatha. Her workshop combines artisanal carpentry with strict "
            "cost control over timber offcuts, varnish, and hardware."
        ),
        "monthly_revenue": 53500,
        "monthly_expenses": 34800,
        "assets": {"Woodworking Lathes & Saws": 72000, "Timber Inventory": 18400, "Bank": 15600},
        "liabilities": {"Sawmill Creditors": 11200},
    },
    {
        "id": "cs_12",
        "business_name": "Tshwane Coding & Robotics Academy",
        "owner": "Amahle Nkosi",
        "location": "Pretoria, Gauteng",
        "sector": "Tertiary / Education & Training",
        "ownership_form": "Private Company",
        "narrative": (
            "Amahle Nkosi runs an after-school Coding & Robotics Academy in Pretoria, teaching Grade 7–9 learners "
            "Python programming and microcontroller electronics. Parents pay monthly tuition via debit order and EFT."
        ),
        "monthly_revenue": 58000,
        "monthly_expenses": 33400,
        "assets": {"Laptops & Robotics Kits": 115000, "Classroom Furniture": 24000, "Bank": 37500},
        "liabilities": {"Tech Lease Liability": 29000},
    },
    {
        "id": "cs_13",
        "business_name": "Drakensberg Eco-Trail & Guest Rondavels",
        "owner": "Zanele Gumede",
        "location": "Bergville, KwaZulu-Natal",
        "sector": "Tertiary / Hospitality & Eco-Tourism",
        "ownership_form": "Partnership",
        "narrative": (
            "Zanele Gumede operates solar-powered guest rondavels and guided mountain hikes in Bergville. "
            "Seasonal peak bookings in April and December generate strong cash surpluses that must be budgeted "
            "carefully to cover quieter winter months."
        ),
        "monthly_revenue": 69000,
        "monthly_expenses": 42500,
        "assets": {"Guest Rondavels & Solar Array": 420000, "Linen & Equipment": 32000, "Bank": 44000},
        "liabilities": {"Mortgage Bond": 165000},
    },
    {
        "id": "cs_14",
        "business_name": "Vhembe Subtropical Dried Fruit",
        "owner": "Ndivhuwo Tshivhase",
        "location": "Thohoyandou, Limpopo",
        "sector": "Secondary / Food Dehydration",
        "ownership_form": "Co-operative",
        "narrative": (
            "To prevent post-harvest spoilage of mangoes and bananas in Vhembe, Ndivhuwo Tshivhase's co-operative "
            "installed solar-assisted dehydrators. Surplus summer fruit is sliced, dried, and sealed into preservative-free "
            "snack packs with a 12-month shelf life."
        ),
        "monthly_revenue": 44600,
        "monthly_expenses": 28100,
        "assets": {"Solar Dehydrator Tunnels": 58000, "Packaging Pouches": 7900, "Bank": 18300},
        "liabilities": {"Fruit Growers Creditors": 8600},
    },
    {
        "id": "cs_15",
        "business_name": "Cape Flats Community Pharmacy & Clinic",
        "owner": "Tariq Abrahams",
        "location": "Athlone, Western Cape",
        "sector": "Tertiary / Healthcare & Retail Pharmacy",
        "ownership_form": "Private Company",
        "narrative": (
            "Tariq Abrahams manages an independent community pharmacy in Athlone providing chronic medication, "
            "blood-pressure screening, and wellness consultations. Strict stock rotation prevents medicine expiry "
            "and maintains healthy cash flow."
        ),
        "monthly_revenue": 148000,
        "monthly_expenses": 109000,
        "assets": {"Medical Cold-Chain Fridges": 68000, "Pharmaceutical Stock": 94000, "Bank": 51000},
        "liabilities": {"Pharmaceutical Wholesalers": 46000},
    },
    {
        "id": "cs_16",
        "business_name": "Highveld Poultry & Egg Layers",
        "owner": "Jabu Mahlangu",
        "location": "Standerton, Mpumalanga",
        "sector": "Primary / Poultry Farming",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Jabu Mahlangu manages 1 500 laying hens in Standerton, producing graded trays of 30 eggs for local "
            "spaza shops, bakeries, and households. Feed accounts for 65% of operating expenses, making bulk feed "
            "discounts critical for profitability."
        ),
        "monthly_revenue": 61500,
        "monthly_expenses": 43200,
        "assets": {"Poultry Houses & Feeders": 110000, "Layer Feed Stock": 14800, "Bank": 22900},
        "liabilities": {"Feed Mill Creditors": 12500},
    },
    {
        "id": "cs_17",
        "business_name": "Vaal Triangle Engineering & Welding",
        "owner": "Johan Steyn & Mandla Sithole",
        "location": "Vanderbijlpark, Gauteng",
        "sector": "Secondary / Metal Fabrication",
        "ownership_form": "Partnership",
        "narrative": (
            "Johan Steyn and Mandla Sithole fabricate steel security gates, burglar bars, and trailer frames in "
            "Vanderbijlpark. Every custom job requires a 50% cash deposit before steel is cut, with the balance "
            "paid upon installation."
        ),
        "monthly_revenue": 78000,
        "monthly_expenses": 51400,
        "assets": {"MIG/TIG Welding Plant": 88000, "Steel Tubing Stock": 23500, "Debtors": 14200},
        "liabilities": {"Steel Merchant Creditors": 17800},
    },
    {
        "id": "cs_18",
        "business_name": "Namaqualand Succulent & Indigenous Nursery",
        "owner": "Annelize Cloete",
        "location": "Springbok, Northern Cape",
        "sector": "Primary & Tertiary / Horticulture",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Annelize Cloete propagates water-wise indigenous succulents and aloes in Springbok for landscaping "
            "projects and guesthouses. Using rainwater harvesting tanks, her nursery thrives even during dry seasons."
        ),
        "monthly_revenue": 27800,
        "monthly_expenses": 14900,
        "assets": {"Shade-Cloth Greenhouses": 42000, "Rainwater JoJo Tanks": 18500, "Bank": 13400},
        "liabilities": {"Nursery Supplies Account": 3900},
    },
    {
        "id": "cs_19",
        "business_name": "Richards Bay Harbour Catering Services",
        "owner": "Nomusa Mthethwa",
        "location": "Richards Bay, KwaZulu-Natal",
        "sector": "Tertiary / Industrial Catering",
        "ownership_form": "Close Corporation",
        "narrative": (
            "Nomusa Mthethwa's industrial kitchen prepares 400 balanced shift meals daily for stevedores and port "
            "workers in Richards Bay. Hygiene compliance, portion costing, and punctual delivery are core operational goals."
        ),
        "monthly_revenue": 124000,
        "monthly_expenses": 88600,
        "assets": {"Commercial Kitchen & Bain-Maries": 135000, "Insulated Delivery Van": 160000, "Bank": 49000},
        "liabilities": {"Vehicle Finance": 74000, "Food Wholesalers": 19200},
    },
    {
        "id": "cs_20",
        "business_name": "Stellenbosch Winelands Cycle Tours",
        "owner": "Lukas Davids",
        "location": "Stellenbosch, Western Cape",
        "sector": "Tertiary / Tourism & Recreation",
        "ownership_form": "Sole Trader",
        "narrative": (
            "Lukas Davids operates guided mountain-bike and e-bike tours through Stellenbosch farms and nature trails. "
            "He tracks bicycle maintenance, helmet replacements, and tour guide wages in a monthly Cash Payments Journal."
        ),
        "monthly_revenue": 54000,
        "monthly_expenses": 31200,
        "assets": {"Fleet of 20 Mountain & E-Bikes": 190000, "Workshop Tools": 16500, "Bank": 33800},
        "liabilities": {"Equipment Loan": 48000},
    },
]


def get_case_study(seed: int = 42, index: int = 0) -> Dict[str, Any]:
    """Deterministically returns a South African EMS case study dictionary."""
    rng = random.Random((seed or 42) + index * 13)
    return rng.choice(SA_EMS_CASE_STUDIES)
