"""Grade 10 Business Studies - Term 1 - Topic 4: The macro environment.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_macro"
VAID = "macro_environment"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How much control does a business have over the macro environment?",
            options=["Full control", "Limited/some control", "No control at all", "Control through suppliers"],
            correct_index=2,
            explanation="Businesses have no control over the macro (external) environment; they can only respond to it.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The acronym used to identify and evaluate macro-environment factors is …",
            options=["SWOT", "PESTLE", "SMART", "PDCA"],
            correct_index=1,
            explanation="PESTLE (Political, Economic, Social, Technological, Legal, Environmental) is used to scan the macro environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Inflation, interest rates, petrol price and exchange rates are part of the … environment.",
            options=["social", "economic", "legal", "physical"],
            correct_index=1,
            explanation="These external factors that influence buying habits form part of the economic environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Religion, customs and traditions that influence business decisions belong to the … environment.",
            options=["cultural", "political", "technological", "legal"],
            correct_index=0,
            explanation="The cultural environment includes religion, customs and traditions that influence actions and decisions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The socio-economic characteristics of a population used to identify customer behaviour describe the … environment.",
            options=["social", "demographic", "economic", "institutional"],
            correct_index=1,
            explanation="The demographic environment refers to the socio-economic characteristics of a population.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The three levels of government in South Africa that put laws and rules in place describe the … environment.",
            options=["political", "institutional", "legal", "global"],
            correct_index=1,
            explanation="The institutional environment refers to the three levels of government that regulate how businesses operate.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The … environment refers to the immediate physical and social setting in which people live and businesses operate.",
            options=["cultural", "economic", "natural", "social"],
            correct_index=3,
            explanation="The social environment refers to the immediate physical and social setting in which people live.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which Act requires a business to give information about the ingredients of a product?",
            options=[
                "National Credit Act",
                "Consumer Protection Act",
                "Broad-Based Black Economic Empowerment",
                "Compensation for Occupational Injuries and Diseases Act",
            ],
            correct_index=1,
            explanation="The Consumer Protection Act (CPA) requires businesses to provide information on a product's ingredients.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which component of the macro environment shows the fastest changes?",
            options=["Legal environment", "Technological environment", "Physical environment", "Political environment"],
            correct_index=1,
            explanation="The technological environment shows the fastest changes (e.g. the Fourth Industrial Revolution).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Globalisation, international trade and multinational corporations form part of the … environment.",
            options=["international/global", "institutional", "economic", "social"],
            correct_index=0,
            explanation="The international/global environment covers international interactions, trade and multinational corporations.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Air, water and noise pollution and the depletion of non-renewable resources relate to the … environment.",
            options=["physical/natural", "economic", "legal", "demographic"],
            correct_index=0,
            explanation="The physical/natural environment includes pollution, ecological aspects and non-renewable resources.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The Labour Relations Act (LRA) and Basic Conditions of Employment Act (BCEA) are examples of factors in the … environment.",
            options=["legal", "political", "social", "economic"],
            correct_index=0,
            explanation="Laws such as the LRA and BCEA form part of the legal environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The government and its institutions plus public and private stakeholders that influence businesses describe the … environment.",
            options=["institutional", "political", "legal", "global"],
            correct_index=1,
            explanation="The political environment is the government, its institutions and public/private stakeholders that influence businesses.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How many features/components does the macro environment have?",
            options=["Six", "Eight", "Ten", "Twelve"],
            correct_index=2,
            explanation="The macro environment has ten features/components (often grouped using PESTLE).",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Define the meaning of the macro environment. (4)",
            marking_points=[
                "It refers to the interaction of businesses with forces outside of themselves.",
                "It is also known as the external environment.",
                "It presents both opportunities and threats and is always changing.",
                "Businesses have no control over this environment.",
            ],
            sample_answer="The macro environment refers to the interaction of businesses with forces outside of themselves. It is also known as the external environment, presents both opportunities and threats, is always changing, and businesses have no control over it.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Briefly explain TWO reasons why the macro environment can be challenging for businesses. (4)",
            marking_points=[
                "It cannot be controlled by a business at all.",
                "It is always changing, which leads to challenges.",
                "A change in one macro environment can affect the others and impact businesses.",
            ],
            sample_answer="The macro environment is challenging because a business cannot control it at all, and it is always changing. A change in one part of the macro environment can affect the others, which then impacts the business.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain what PESTLE stands for. (6)",
            marking_points=[
                "Political (including institutional) environment.",
                "Economic environment.",
                "Social (including cultural and demographic) environment.",
                "Technological environment.",
                "Legal environment.",
                "Environmental (physical/natural and international/global).",
            ],
            sample_answer="PESTLE stands for Political, Economic, Social, Technological, Legal and Environmental factors. It is used to identify and evaluate the external factors that affect a business.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the economic environment and give an example of how it challenges businesses. (4)",
            marking_points=[
                "Refers to external economic factors influencing buying habits of consumers and businesses.",
                "Includes inflation, interest rates, petrol price and exchange rates.",
                "Example: high interest rates make loans more expensive.",
                "Example: inflation raises costs and reduces sales/profitability.",
            ],
            sample_answer="The economic environment refers to external factors such as inflation, interest rates and exchange rates that influence buying habits. For example, high interest rates make loans more expensive, while inflation raises costs and can reduce sales and profitability.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the technological environment as a component of the macro environment. (4)",
            marking_points=[
                "Refers to new and innovative knowledge, inventions and improvements in techniques.",
                "Shows the fastest changes in the macro environment (e.g. 4IR).",
                "Challenge: businesses may not keep up with the latest technology.",
                "Challenge: high cost to buy and maintain new technology / cyberattack risk.",
            ],
            sample_answer="The technological environment refers to new knowledge, inventions and improvements in techniques, and shows the fastest changes in the macro environment. A challenge is that businesses may struggle to keep up with the latest technology, which is also expensive to buy and maintain, and carries cyberattack risks.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the legal environment and give TWO examples of relevant laws. (4)",
            marking_points=[
                "Refers to laws passed by government that affect businesses.",
                "Example: Labour Relations Act / Basic Conditions of Employment Act.",
                "Example: Consumer Protection Act / National Credit Act.",
                "Businesses may pay fines for non-adherence to laws.",
            ],
            sample_answer="The legal environment refers to laws passed by government that businesses must obey. Examples include the Labour Relations Act and the Consumer Protection Act. Businesses may be fined for not adhering to these laws.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the physical/natural environment as a component of the macro environment. (4)",
            marking_points=[
                "Refers to natural and man-made variables surrounding businesses.",
                "Includes availability and sustainability of natural resources.",
                "Challenge: unpredictable weather/climate disrupts businesses.",
                "Challenge: pollution and depletion of non-renewable resources.",
            ],
            sample_answer="The physical/natural environment refers to natural and man-made variables surrounding businesses, including the availability and sustainability of resources. Challenges include unpredictable weather that disrupts operations and pollution or depletion of non-renewable resources.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the international/global environment and a challenge it poses. (4)",
            marking_points=[
                "Refers to uncontrollable local and international interactions affecting businesses.",
                "Increases competition in domestic markets and opens foreign markets.",
                "Encourages businesses to be more innovative and efficient.",
                "Challenge: pandemics/civil wars disrupt imports and exports.",
            ],
            sample_answer="The international/global environment refers to uncontrollable local and international interactions. It increases competition and opens foreign markets, encouraging innovation and efficiency. A challenge is that events such as pandemics or civil wars disrupt the ability to import and export goods.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_macro_environment = build_generate(_pools)
