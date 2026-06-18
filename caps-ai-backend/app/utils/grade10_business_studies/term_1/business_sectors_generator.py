"""Grade 10 Business Studies - Topic 6: Business sectors.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_sectors"
VAID = "business_sectors"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which sector deals with the extraction/collection of raw materials and natural resources?",
            options=["Primary sector", "Secondary sector", "Tertiary sector", "Informal sector"],
            correct_index=0,
            explanation="The primary sector extracts/collects/cultivates raw materials such as livestock, fish, timber, coal and gold.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which sector transforms raw materials into finished or semi-finished products?",
            options=["Primary sector", "Secondary sector", "Tertiary sector", "Public sector"],
            correct_index=1,
            explanation="The secondary (manufacturing) sector converts raw materials into new products.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which sector offers services and is also known as the service industry?",
            options=["Primary sector", "Secondary sector", "Tertiary sector", "Formal sector"],
            correct_index=2,
            explanation="The tertiary sector offers services to businesses and consumers and is known as the service industry.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Mining, fishing, forestry and agriculture are examples of which sector?",
            options=["Tertiary", "Secondary", "Primary", "Public"],
            correct_index=2,
            explanation="Agriculture, fishing, forestry and mining are primary-sector activities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Retailing, tourism, transport and financing are examples of which sector?",
            options=["Primary", "Secondary", "Tertiary", "Informal"],
            correct_index=2,
            explanation="Financing, hospitality, retail, storage, tourism and transport are tertiary-sector activities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that are registered with CIPC and pay tax to SARS belong to the …",
            options=["informal sector", "formal sector", "primary sector", "public sector"],
            correct_index=1,
            explanation="Formal-sector businesses are registered with CIPC and pay tax to SARS.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Spaza shops, street vendors and car-wash services are typically part of the …",
            options=["formal sector", "informal sector", "public sector", "secondary sector"],
            correct_index=1,
            explanation="These small, unregistered home-based operations form part of the informal sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="State-owned companies (SOCs/SOEs) owned and controlled by the government form part of the …",
            options=["private sector", "public sector", "informal sector", "primary sector"],
            correct_index=1,
            explanation="The public sector comprises enterprises owned and managed by the government.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses owned, financed and run by private individuals to make a profit form part of the …",
            options=["public sector", "private sector", "primary sector", "tertiary sector"],
            correct_index=1,
            explanation="The private sector consists of business activity owned, financed and run by private individuals seeking profit.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An economy that consists of both private and state-owned companies is called a …",
            options=["command economy", "mixed economy", "free-market economy", "traditional economy"],
            correct_index=1,
            explanation="South Africa has a mixed economy with both private and state-owned companies.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The sale of state-owned businesses and assets to the private sector is called …",
            options=["nationalisation", "privatisation", "globalisation", "urbanisation"],
            correct_index=1,
            explanation="Privatisation is the sale of state-owned businesses and assets to the private sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which sector's contribution is difficult to calculate and is not monitored by government?",
            options=["Formal sector", "Informal sector", "Public sector", "Secondary sector"],
            correct_index=1,
            explanation="The informal sector is unregistered and unmonitored, so its contribution to GDP is hard to calculate.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="State the THREE business sectors. (3)",
            marking_points=["Primary sector", "Secondary sector", "Tertiary sector"],
            sample_answer="The three business sectors are the primary sector, the secondary sector and the tertiary sector.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the relationship between the three business sectors. (6)",
            marking_points=[
                "The primary sector extracts raw materials and supplies them to the secondary sector.",
                "The secondary sector transforms raw materials into final products.",
                "The secondary sector sells products to retailers in the tertiary sector.",
                "The tertiary sector sells the products/services to the consumer and supports the other sectors.",
            ],
            sample_answer="The primary sector extracts raw materials and supplies them to the secondary sector, which transforms them into final products. The secondary sector sells these to retailers in the tertiary sector, which sells the products to consumers and supports the activities of the other two sectors.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Differentiate between the formal and informal sectors. (8)",
            marking_points=[
                "Formal: registered with CIPC and pays tax to SARS; informal: not registered and pays no profit tax.",
                "Formal: monitored and controlled by government laws; informal: not monitored by government.",
                "Formal: regular weekly/monthly income and set hours; informal: irregular income and long hours.",
                "Formal: employees protected by legislation (BCEA, COIDA, UIF); informal: employees not protected.",
            ],
            sample_answer="Formal-sector businesses are registered with CIPC and pay tax to SARS, are monitored by government and protect employees through legislation such as BCEA and UIF, with regular income and set hours. Informal-sector businesses are unregistered, pay no profit tax, are not monitored, offer irregular income and long hours, and do not protect employees.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Advise businesses on the importance of the formal sector. (4)",
            marking_points=[
                "Business activities are included in the GDP figures of the country.",
                "Companies pay tax on profits and employees pay personal income tax.",
                "Provides employment to skilled, semi-skilled and unskilled labour.",
                "Provides a large variety of goods and services to satisfy consumers.",
            ],
            sample_answer="The formal sector is important because its activities are included in the country's GDP, companies and employees pay tax, it provides employment to a range of skill levels, and it offers a wide variety of goods and services to consumers.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the importance of the informal sector. (4)",
            marking_points=[
                "Encourages entrepreneurship and self-employment.",
                "Provides employment and contributes to poverty alleviation.",
                "People gain work experience to apply for formal-sector jobs.",
                "Easy to enter and serves the needs of individuals.",
            ],
            sample_answer="The informal sector is important because it encourages entrepreneurship and self-employment, provides employment that alleviates poverty, lets people gain work experience for formal jobs, and is easy to enter while serving individuals' needs.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of the public sector. (4)",
            marking_points=[
                "Comprises business enterprises owned and managed by the government.",
                "Composed of all levels of government and government-controlled enterprises (SOCs/SOEs).",
                "Provides public goods and services such as water and electricity.",
                "Does not include private companies, voluntary organisations or households.",
            ],
            sample_answer="The public sector comprises enterprises owned and managed by the government at all levels, including state-owned companies. It provides public goods and services such as water and electricity and excludes private companies, voluntary organisations and households.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning and main aim of the private sector. (4)",
            marking_points=[
                "Consists of business activity owned, financed and run by private individuals.",
                "Businesses are owned by sole traders, partnerships, close corporations or companies.",
                "Their main aim is to make a profit.",
                "Some exist in the formal or informal sectors.",
            ],
            sample_answer="The private sector consists of business activity that is owned, financed and run by private individuals such as sole traders, partnerships and companies. Their main aim is to make a profit, and some operate in the formal or informal sectors.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Using bread as an example, describe how a product moves through the three sectors. (6)",
            marking_points=[
                "Primary: wheat is grown on a farm and sold to a bread company.",
                "Secondary: the bread company processes wheat into flour and produces bread.",
                "Tertiary: the bread is transported to and sold by retailers to consumers.",
            ],
            sample_answer="In the primary sector, wheat is grown on a farm and sold to a bread company. In the secondary sector, the company processes the wheat into flour and bakes bread. In the tertiary sector, the bread is transported to retailers who sell it to consumers.",
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_business_sectors = build_generate(_pools)
