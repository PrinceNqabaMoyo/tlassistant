"""Grade 10 Business Studies - Term 3 - Topic 17: Understanding business plans
and implications.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_bizplan"
VAID = "business_plans"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A document setting out a business's future objectives and strategies for achieving them is a …",
            options=["business plan", "prospectus", "questionnaire", "marketing mix"],
            correct_index=0,
            explanation="A business plan sets out a business's future objectives and the strategies to achieve them.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A short section that summarises the entire business plan is the …",
            options=["executive summary", "cover page", "SWOT analysis", "financial plan"],
            correct_index=0,
            explanation="The executive summary summarises the entire business plan and appears at the beginning.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The statement describing the purpose of the business and why it exists is the …",
            options=["vision statement", "mission statement", "executive summary", "marketing plan"],
            correct_index=1,
            explanation="The mission statement describes the purpose of the business and why it exists.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The statement describing the long-term goal of how entrepreneurs see their business in the future is the …",
            options=["vision statement", "mission statement", "budget", "SWOT analysis"],
            correct_index=0,
            explanation="The vision statement is the long-term goal of how entrepreneurs see their business in the future.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The 7Ps refer to the elements of the …",
            options=["marketing mix", "financial plan", "SWOT analysis", "PESTLE analysis"],
            correct_index=0,
            explanation="The 7Ps (Product, Price, Place, Promotion, People, Physical environment, Process) form the marketing mix.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In the marketing mix, the location of the business refers to which 'P'?",
            options=["Place", "Price", "Product", "Promotion"],
            correct_index=0,
            explanation="'Place' in the marketing mix refers to the location of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In the marketing mix, methods used to advertise the product refer to which 'P'?",
            options=["Promotion", "Place", "People", "Process"],
            correct_index=0,
            explanation="'Promotion' refers to the methods used to advertise the product.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The PESTLE analysis is used to analyse the challenges of the … environment.",
            options=["micro", "market", "macro", "internal"],
            correct_index=2,
            explanation="PESTLE analyses the external macro environment (Political, Economic, Social, Technological, Legal, Environmental).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The authorisation issued by local government to start a business is a …",
            options=["trading licence", "patent", "copyright", "credit facility"],
            correct_index=0,
            explanation="A trading licence is the authorisation issued by local government to start a business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An exclusive right granted for an invention is a …",
            options=["patent", "copyright", "trademark", "trading licence"],
            correct_index=0,
            explanation="A patent is an exclusive right granted for an invention (a new product or process).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An estimation of revenue and expenses over a specified future period is a …",
            options=["budget", "cash flow statement", "SWOT analysis", "mission statement"],
            correct_index=0,
            explanation="A budget is an estimation of revenue and expenses over a specified future period.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Rivalry between two or more businesses selling the same goods or service is called …",
            options=["competition", "collaboration", "promotion", "the marketing mix"],
            correct_index=0,
            explanation="Competition is the rivalry between two or more businesses selling the same goods or service.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which is a strategy a business can use to overcome competition?",
            options=["Sell poor quality products", "Charge reasonable prices", "Avoid marketing", "Copy competitor logos"],
            correct_index=1,
            explanation="Charging reasonable prices (along with quality products and good service) helps overcome competition.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the importance of a business plan. (6)",
            marking_points=[
                "Helps entrepreneurs to set goals and objectives.",
                "Can be used to attract investors and prospective employees.",
                "Guides the entrepreneur on the viability of the business idea.",
                "Helps identify problems and is essential when applying for financial assistance.",
            ],
            sample_answer="A business plan helps entrepreneurs set goals and objectives, attract investors and prospective employees, and assess the viability of the business idea. It helps identify problems and take steps to avoid them, improves processes, evaluates success, gives direction, and is essential when applying for financial assistance.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Name the components of a business plan. (6)",
            marking_points=[
                "Cover page, contents page/index and executive summary.",
                "Description/overview of the business and SWOT analysis.",
                "Legal requirements, marketing plan and operational plan.",
                "Financial plan, management plan and competitor analysis.",
            ],
            sample_answer="The components of a business plan are: cover page, contents page/index, executive summary, description/overview of the business, SWOT analysis, legal requirements, marketing plan, operational plan, financial plan, management plan and competitor analysis.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the purpose of an executive summary. (4)",
            marking_points=[
                "Gives the reader an overview of the entire document.",
                "Summarises the entire business plan.",
                "Written after the plan is completed but appears at the beginning.",
                "Gives readers an idea of what is contained in the business plan.",
            ],
            sample_answer="The executive summary gives the reader an overview of the entire document, summarising the whole business plan. It is written after the plan is completed but appears at the beginning, giving readers an idea of what is contained in the business plan.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Distinguish between a vision statement and a mission statement. (4)",
            marking_points=[
                "The vision statement is the long-term goal of how entrepreneurs see the business in future.",
                "The vision describes how the business will achieve its purpose and grow.",
                "The mission statement describes the purpose of the business and why it exists.",
                "The mission addresses how entrepreneurs hope to achieve their vision.",
            ],
            sample_answer="A vision statement is the long-term goal of how entrepreneurs see their business in the future and how they want to grow, describing how the business will achieve its purpose. A mission statement describes the purpose of the business and why it exists, and addresses how entrepreneurs hope to achieve their vision.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of the marketing mix with reference to the 7Ps. (7)",
            marking_points=[
                "The marketing mix is a set of actions used to promote the brand, explained by 7Ps.",
                "Product (object made for sale), Price (amount required as payment), Place (location).",
                "Promotion (methods to advertise) and People (employees and target market).",
                "Physical environment (environment around the business) and Process (system to deliver).",
            ],
            sample_answer="The marketing mix is a set of actions a business uses to promote its brand, explained by the 7Ps: Product (object made for sale), Price (amount required as payment), Place (location of the business), Promotion (methods to advertise), People (employees and the target market), Physical environment (the environment around the business) and Process (the system used to deliver the product/service).",
            marks=7,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss strategies a business can use to overcome competition in the market. (6)",
            marking_points=[
                "Sell quality products and services and offer after-sales services.",
                "Charge reasonable prices.",
                "Conduct intensive marketing campaigns and use creative advertising slogans.",
                "Make unique products and provide attractive product displays.",
            ],
            sample_answer="To overcome competition, a business can sell quality products and services, offer after-sales services, charge reasonable prices, conduct intensive marketing campaigns, use creative advertising slogans, make unique products, and provide attractive product displays.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how a PESTLE analysis helps a business deal with the macro environment. (4)",
            marking_points=[
                "PESTLE analyses the external elements of the macro environment.",
                "It covers Political, Economic, Social, Technological, Legal and Environmental factors.",
                "Businesses have no control over these factors but can scan them.",
                "It enables a business to identify challenges posed by these external factors.",
            ],
            sample_answer="A PESTLE analysis scans the external macro environment by examining Political, Economic, Social, Technological, Legal and Environmental factors. Although businesses have no control over these factors, the analysis enables them to identify the challenges posed by these external factors and plan to deal with them.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain what a financial plan should include and its purpose. (6)",
            marking_points=[
                "Explains the entrepreneur's financial contribution and funding requirements.",
                "Indicates how much capital is needed and how it will be raised.",
                "Includes a budget and projected cash flow statements (usually over three years).",
                "Aims to project profitability and how long before the business shows a profit.",
            ],
            sample_answer="A financial plan explains the entrepreneur's financial contribution and funding requirements, indicating how much capital is needed and how it will be raised. It includes a budget and projected statements of profit, loss and cash flow (usually over three years), aiming to project the profitability of the business and how long it will take before it shows a profit.",
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_business_plans = build_generate(_pools)
