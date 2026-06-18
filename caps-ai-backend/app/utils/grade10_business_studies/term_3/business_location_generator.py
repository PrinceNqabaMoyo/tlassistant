"""Grade 10 Business Studies - Term 3 - Topic 14: Business location decisions.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_location"
VAID = "business_location"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The availability of transport, water, electricity and communication networks is called …",
            options=["infrastructure", "labour market", "potential market", "raw materials"],
            correct_index=0,
            explanation="Infrastructure refers to the availability of transport, water, electricity and communication networks.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The people who may be interested in the product/service sold by a business is the …",
            options=["labour market", "potential market", "supplier base", "competition"],
            correct_index=1,
            explanation="The potential market refers to people who may be interested in the business's product/service.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="People who are employed by businesses and available to work make up the …",
            options=["potential market", "labour market", "raw materials", "infrastructure"],
            correct_index=1,
            explanation="The labour market refers to people who are employed and available to work.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Rules governing working hours, minimum wage and discrimination are … regulations.",
            options=["environmental", "labour", "tax", "transport"],
            correct_index=1,
            explanation="Labour regulations govern working hours, minimum wage, breaks and discrimination.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A mine that relies on rail transport should be located close to the …",
            options=["railway", "airport", "harbour", "highway"],
            correct_index=0,
            explanation="The nature of transport varies; mines relying on rail should be located close to the railway.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An amount by which SARS reduces the actual taxes owing is a …",
            options=["tax rebate", "dividend", "subsidy", "debenture"],
            correct_index=0,
            explanation="A tax rebate is an amount by which SARS reduces the actual taxes owing.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that use heavy raw materials such as iron should locate close to the …",
            options=["source of raw materials", "potential market", "airport", "competitors"],
            correct_index=0,
            explanation="Heavy raw materials affect transport and price, so businesses should locate close to the source.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Agricultural and tourism industries are most directly dependent on …",
            options=["climate conditions", "labour regulations", "tax rebates", "competition"],
            correct_index=0,
            explanation="Agricultural and tourism industries depend on particular climate conditions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="If the minimum wage in an area is high, the cost of labour is …",
            options=["lower", "expensive", "unaffected", "free"],
            correct_index=1,
            explanation="High minimum wage makes labour expensive, which can raise the price of products.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Strict pollution and dumping laws in an area are an example of a/an … factor affecting location.",
            options=["environmental", "geographical", "economic", "transport"],
            correct_index=0,
            explanation="Strict pollution and dumping laws are environmental factors that may discourage businesses.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which statement about the importance of business location is correct?",
            options=[
                "Location has no impact on establishment costs",
                "Location plays a role in attracting and retaining the best employees",
                "Location does not affect access to resources",
                "Location only affects income, never expenses",
            ],
            correct_index=1,
            explanation="Location plays a huge role in attracting and retaining the best employees and affects costs and resources.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A location far away from transport routes is generally …",
            options=["more desirable", "less desirable", "tax exempt", "cheaper to staff"],
            correct_index=1,
            explanation="Locations far away from transport routes are less desirable for businesses.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the importance of business location. (6)",
            marking_points=[
                "Location plays a huge role in attracting and retaining the best employees.",
                "It has a significant impact on the establishment costs of the business.",
                "It affects access to capital, resources and infrastructure.",
                "A good location decision can boost long-term performance and affects income, expenses and legalities.",
            ],
            sample_answer="Business location is important because it plays a huge role in attracting and retaining the best employees, has a significant impact on establishment costs, and affects access to capital, resources and infrastructure. A good location decision can boost long-term performance and affects the income, expenses and legalities of the business.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss how labour regulations and the labour market impact the location of a business. (6)",
            marking_points=[
                "Labour regulations increase the cost of labour (working hours, minimum wage).",
                "Strict labour regulations make a location less desirable.",
                "Scarcity of labour in a location means labour will be expensive.",
                "Businesses should locate where labour is available and affordable with the right skills.",
            ],
            sample_answer="Labour regulations increase the cost of labour through working hours and minimum wage requirements, and strict regulations make a location less desirable. The labour market matters because scarcity of labour makes it expensive, so businesses should locate where labour is available, affordable and has the right skills.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss how transport and infrastructure impact the location of a business. (6)",
            marking_points=[
                "Transport affects employees getting to work and the delivery of supplies.",
                "Locations far from transport routes are less desirable.",
                "Infrastructure is the availability of transport, water, electricity and communication.",
                "An entrepreneur must check whether infrastructure will be upgraded and water is sufficient.",
            ],
            sample_answer="Transport affects how employees get to work and how supplies are delivered, and locations far from transport routes are less desirable. Infrastructure - the availability of transport, water, electricity and communication - is also vital, so an entrepreneur must check whether it will be upgraded and whether there is sufficient suitable water.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss how the potential market and raw materials impact the location of a business. (6)",
            marking_points=[
                "The potential market is the people who may be interested in the product/service.",
                "Businesses must locate close to their potential market to be accessible to consumers.",
                "The proximity of raw materials affects transport, price and availability.",
                "Businesses must locate close to the source of raw materials, especially heavy ones.",
            ],
            sample_answer="The potential market is the people who may be interested in the product, so a business must locate close to them to remain accessible. Raw materials also matter because their proximity affects transport, price and availability, so businesses should locate close to the source, especially for heavy materials like iron.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss how environmental factors and climate conditions impact the location of a business. (6)",
            marking_points=[
                "Environmental factors such as depletion of natural resources can affect operations.",
                "Some areas restrict noisy or polluting machines, affecting location.",
                "Strict pollution and dumping laws may discourage businesses.",
                "Agricultural and tourism industries depend on particular climate conditions.",
            ],
            sample_answer="Environmental factors such as depletion of natural resources can affect operations, and some areas restrict noisy or polluting machines or have strict pollution and dumping laws that discourage businesses. Climate conditions matter too, since agricultural and tourism industries depend on particular climates, and changes in rainfall or temperature can affect raw materials.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Name SIX factors that impact the location of a business. (6)",
            marking_points=[
                "Labour regulations and the labour market.",
                "Transport and infrastructure.",
                "Potential markets (customers) and raw materials.",
                "Environmental factors, climate, government regulations/taxes, crime and competition.",
            ],
            sample_answer="Factors that impact business location include labour regulations, the labour market, transport, infrastructure, potential markets, raw materials, environmental factors, climate conditions, government regulations and taxes, crime, competition, and economic and geographical factors.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how government/local regulations and taxes can impact a business location. (4)",
            marking_points=[
                "Government and local regulations and taxes differ between areas.",
                "Tax rebates can reduce the taxes owing and attract businesses to an area.",
                "High taxes or strict regulations make a location less attractive.",
                "Regulations affect the legalities, income and expenses of the business.",
            ],
            sample_answer="Government and local regulations and taxes differ between areas, so tax rebates can attract businesses by reducing taxes owing, while high taxes or strict regulations make a location less attractive. These regulations affect the legalities, income and expenses of the business.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how crime and competition can impact a business location. (4)",
            marking_points=[
                "High crime areas increase security costs and risk to stock and staff.",
                "Crime makes a location less desirable for customers and employees.",
                "Locating near strong competition can reduce market share.",
                "Businesses must weigh competition against access to the potential market.",
            ],
            sample_answer="High crime areas increase security costs and risk to stock and staff, making the location less desirable for customers and employees. Strong competition in an area can reduce market share, so businesses must weigh competition against access to the potential market when choosing a location.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_business_location = build_generate(_pools)
