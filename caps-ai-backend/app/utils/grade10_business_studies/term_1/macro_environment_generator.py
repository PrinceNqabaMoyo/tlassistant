"""Grade 10 Business Studies - Term 1 - Topic 3: The macro environment.

Deterministic generator (no LLM). Content hand-authored from the CAPS notes,
activities, PESTLE table, official crossword key and consolidation questions in
``curriculum_docs_auto/BusinessStudies_Gr10/Term 1/03. The macro environment.md``.

All six archetypes are covered:
    concepts    -> mcq (meaning, PESTLE, ten components, examples)
    application -> scenario mcq + typed (identify the component and MOTIVATE from a quote)
    discussion  -> typed (explain why each component is a challenge, with memos)
    word_bank   -> fill-in definitions from a term bank
    matching    -> match component / Act to its description
    crossword   -> the ten macro-environment components
    essay       -> extended PESTLE analysis with a model answer

Common misconception targeted (snake_case taxonomy): macro_vs_market_confusion \u2014
learners confuse the influenceable market environment with the uncontrollable macro environment.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import (
    build_generate,
    make_mcq,
    make_typed,
    make_wordbank,
    make_matching,
    make_crossword,
    make_essay,
    pick_scenario,
)

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
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In the acronym PESTLE, the letter 'E' that stands for 'rules that businesses must adhere to' is \u2026",
            options=["Economic", "Environmental", "Legal (legislation)", "Ethical"],
            correct_index=2,
            explanation="PESTLE covers Political, Economic, Social, Technological, Legal and Environmental. The legal environment refers to the rules businesses must adhere to.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="PESTLE is used by businesses MAINLY to \u2026",
            options=[
                "calculate the salaries of employees",
                "identify and evaluate factors in the external environment that affect the business",
                "prepare the annual financial statements",
                "design the organisational structure",
            ],
            correct_index=1,
            explanation="PESTLE gives a business a better understanding of the external environment and the industry in which it competes.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which macro-environment component includes religion, customs and traditions that influence actions and decisions?",
            options=["Cultural environment", "Legal environment", "Economic environment", "Political environment"],
            correct_index=0,
            explanation="The cultural environment includes religion, customs and traditions; under PESTLE it is grouped with the social environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses use the \u2026 environment to identify the product preferences and purchasing behaviour of customers.",
            options=["technological", "demographic", "international", "physical"],
            correct_index=1,
            explanation="The demographic environment is the socio-economic characteristics of a population, used to identify customer preferences and purchasing behaviour.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which component of the macro environment changes the FASTEST?",
            options=["The legal environment", "The cultural environment", "The technological environment", "The political environment"],
            correct_index=2,
            explanation="The technological environment shows the fastest changes in the macro environment; new technologies started the Fourth Industrial Revolution (4IR).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The Fourth Industrial Revolution (4IR) is associated with developments in the \u2026 environment.",
            options=["technological", "physical", "social", "institutional"],
            correct_index=0,
            explanation="New and innovative technology and inventions drive the 4IR, which is part of the technological environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="SUSTAINABILITY, as used in the physical/natural environment, means \u2026",
            options=[
                "making a profit every year",
                "using natural products and energy in a way that does not harm the environment",
                "expanding into foreign markets",
                "retaining all employees for ten years",
            ],
            correct_index=1,
            explanation="The CAPS definition: sustainability is the use of natural products and energy in a way that does not harm the environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A large corporation incorporated in one country that produces or sells goods and services in various countries is a \u2026",
            options=["franchise", "joint venture", "multinational corporation", "co-operative"],
            correct_index=2,
            explanation="A multinational corporation is incorporated in one country but produces/sells goods or services in various countries; its exploitative nature is a challenge in the global environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In business studies, an IMPACT is defined as \u2026",
            options=[
                "the effect or influence of a decision or activity on the business, community or employees",
                "a sudden increase in the price of shares",
                "the movement of goods across a border",
                "a formal complaint lodged by a union",
            ],
            correct_index=0,
            explanation="Impact is the effect or influence of a decision or activity on the business, community or employees.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How many official languages does the South African Constitution recognise, and which macro-environment component does this relate to?",
            options=[
                "Eleven \u2013 social/cultural environment",
                "Nine \u2013 legal environment",
                "Eleven \u2013 political environment",
                "Twelve \u2013 institutional environment",
            ],
            correct_index=0,
            explanation="The constitution recognises eleven official languages, which is a language factor within the social (including cultural) environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which statement about the ten macro-environment components is CORRECT?",
            options=[
                "They are completely separate and a change in one never affects another",
                "A change in one environment can affect any of the other environments and thereby impact businesses",
                "Only the economic environment affects businesses",
                "Businesses can control them if they plan well enough",
            ],
            correct_index=1,
            explanation="The CAPS document explains that a change in one of the macro environments can affect the others, which then impacts businesses (e.g. COVID-19 affected both the social and economic environments).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which ONE of the following is NOT part of the ECONOMIC environment?",
            options=["Inflation", "Exchange rates", "Poverty and unemployment", "Conditions of credit"],
            correct_index=2,
            explanation="Poverty, unemployment and crime are SOCIAL issues. The economic environment covers inflation, petrol price, interest rates, conditions of credit, exchange rates and economic growth. (Misconception: macro_vs_market_confusion / component mis-classification.)",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The Skills Development Act (SDA), Broad-Based Black Economic Empowerment (BBBEE) and the Employment Equity Act (EEA) form part of the \u2026 environment.",
            options=["legal", "technological", "cultural", "physical"],
            correct_index=0,
            explanation="These are business law within the legal environment, which refers to the laws passed by government that affect businesses.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A business MUST apply for a \u2026 before it is able to legally trade in a municipality.",
            options=["patent", "trading licence", "tax clearance only", "BBBEE certificate"],
            correct_index=1,
            explanation="Municipal by-laws (zoning ordinances, business hours, permits and licences) require a business to apply for a trading licence before it may legally trade.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which law requires a business to provide information about the INGREDIENTS of a product to consumers?",
            options=["Consumer Protection Act (CPA)", "Compensation for Occupational Injuries and Diseases Act (COIDA)", "Labour Relations Act (LRA)", "Municipal by-laws"],
            correct_index=0,
            explanation="Under consumer law the CPA requires the business to give information on the ingredients of the product, while the NCA requires background checks on credit clients.",
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


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    """Apply knowledge to scenarios: identify the macro-environment component and MOTIVATE.

    Uses the official CAPS case study 'Dukaan Bicycle Repairs' (Term 1 Topic 3,
    consolidation Question 3.3) plus additional authored scenarios.
    """
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Read the scenario: KAYVAAN DUKAAN owns a bicycle repair shop in Ritzfontein where "
                "the UNEMPLOYMENT LEVEL is quite high. Which component of the macro environment "
                "does the unemployment level represent?"
            ),
            options=["The economic environment", "The social environment", "The legal environment", "The technological environment"],
            correct_index=1,
            explanation="Unemployment, poverty and crime are SOCIAL issues within the social environment. (Misconception to avoid: macro_vs_market_confusion \u2014 the social environment is a macro, not a market, component.)",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "In the same scenario, RESIDENTS are always PROTESTING against poor service delivery. "
                "Identify the component and MOTIVATE your answer."
            ),
            options=[
                "Political environment \u2013 because strikes/protests cause political instability and delay productivity",
                "Social environment \u2013 because protests change consumer tastes",
                "Legal environment \u2013 because protesting is prohibited by law",
                "Economic environment \u2013 because protests raise inflation",
            ],
            correct_index=0,
            explanation="The CAPS answer key classifies protesting residents under the POLITICAL environment, motivated by the quote 'residents in the area are always protesting against poor service delivery'; protests cause political instability and delays in productivity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Also in the scenario, SOME BUSINESSES DUMP WASTE MATERIAL on the nearby field. "
                "Which macro-environment component does this illustrate?"
            ),
            options=["The environmental/physical-natural environment", "The cultural environment", "The institutional environment", "The international environment"],
            correct_index=0,
            explanation="Dumping waste is a pollution factor within the environmental (physical/natural) environment, which also covers weather, climate and depletion of non-renewable resources.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                f"{biz} finds that its transport and production costs are rising because of a jump "
                "in the petrol price. This is a factor in the \u2026 environment."
            ),
            options=["economic", "demographic", "political", "technological"],
            correct_index=0,
            explanation="The economic environment consists of external factors such as inflation, petrol price, interest rates, conditions of credit and exchange rates that influence buying habits.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "A clothing retailer's point-of-sale system is hacked and customer data is stolen. "
                "Which macro-environment component and challenge does this show?"
            ),
            options=[
                "Legal environment \u2013 municipal by-laws",
                "Technological environment \u2013 risk of cyberattacks in cryptography security",
                "Social environment \u2013 low levels of literacy",
                "Political environment \u2013 corruption",
            ],
            correct_index=1,
            explanation="The CAPS table lists 'security in cryptography' under the technological environment: IT systems may be hacked by fraudsters, exposing confidential information.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "The rand weakens sharply against the US dollar, making it much more expensive for a "
                "South African importer to buy overseas stock. This challenge arises from the \u2026 environment."
            ),
            options=["technological", "cultural", "economic", "institutional"],
            correct_index=2,
            explanation="Exchange rates (the price of the rand in terms of another currency) are an economic factor; fluctuations in foreign currency may restrict imports.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "A food manufacturer must now print full ingredient information on all its packaging "
                "and carry out background checks on customers buying on credit. Which macro-environment "
                "component forces this change?"
            ),
            options=["The legal environment", "The political environment", "The technological environment", "The demographic environment"],
            correct_index=0,
            explanation="Consumer law within the legal environment: the CPA requires ingredient information and the NCA requires background checks on credit clients.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "A lockdown prevents a furniture exporter from shipping goods overseas and stops raw "
                "materials from arriving. According to the CAPS document this challenge belongs to the \u2026"
            ),
            options=["international/global environment", "physical environment only", "cultural environment", "demographic environment"],
            correct_index=0,
            explanation="Health issues such as the COVID-19 pandemic are listed under the international/global environment: businesses cannot import and export during lockdown, and many face liquidation.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Which ONE of the following is NOT one of the six grouped factors of the acronym PESTLE?"
            ),
            options=["Political", "Technological", "Demographic", "Environmental"],
            correct_index=2,
            explanation="PESTLE = Political, Economic, Social, Technological, Legal, Environmental. Demographic and cultural factors are grouped INSIDE 'S' (social), not given their own letter.",
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Read the scenario and answer the question that follows.\n"
                "KAYVAAN DUKAAN owns a bicycle repair shop in Ritzfontein where the unemployment level "
                "is quite high. Residents in the area are always protesting against poor service delivery. "
                "Some businesses in the area dump waste material on the nearby field.\n\n"
                "Identify THREE components/features of the macro environment applicable to the scenario "
                "and MOTIVATE each answer by QUOTING from the scenario. (9)"
            ),
            marking_points=[
                "Social environment \u2013 motivated by: 'the unemployment level is quite high'.",
                "Political environment \u2013 motivated by: 'residents in the area are always protesting against poor service delivery'.",
                "Environmental (physical/natural) environment \u2013 motivated by: 'some businesses in the area dump waste material on the nearby field'.",
                "Each answer must pair the component WITH a direct quotation from the scenario to earn both marks.",
            ],
            sample_answer=(
                "(1) SOCIAL ENVIRONMENT \u2013 because 'the unemployment level is quite high'; unemployment is a "
                "social issue that reduces consumer spending. (2) POLITICAL ENVIRONMENT \u2013 because 'residents in "
                "the area are always protesting against poor service delivery'; protests cause political instability "
                "and delays in productivity. (3) ENVIRONMENTAL / PHYSICAL-NATURAL ENVIRONMENT \u2013 because 'some "
                "businesses in the area dump waste material on the nearby field'; pollution threatens the sustainability "
                "of businesses and waste disposal is expensive."
            ),
            marks=9,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Explain why the ECONOMIC environment poses a challenge to businesses. (4)"
            ),
            marking_points=[
                "Rising costs due to inflation/petrol price could affect business sales and profitability.",
                "High interest rates mean that loans become more expensive.",
                "The price of credit impacts the willingness and ability of banks to lend money.",
                "Fluctuations in foreign currency may restrict imports / a recession restricts businesses from continuing to operate.",
            ],
            sample_answer=(
                "Inflation and rising petrol prices increase costs and reduce sales and profitability. High interest "
                "rates make loans more expensive, while the price of credit affects the willingness and ability of "
                "banks to lend. Fluctuations in the exchange rate can restrict imports, and a recession removes the "
                "support businesses need to keep operating."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Explain why the TECHNOLOGICAL environment poses a challenge to businesses. (4)"
            ),
            marking_points=[
                "Businesses may not be able to keep up with, or be aware of, the latest technology.",
                "Employees may not be skilled to operate or maintain new technology/equipment.",
                "Staying up to date with the latest technology is expensive to buy and to maintain.",
                "Systems failure can paralyse operations, and IT systems may be hacked, exposing confidential information.",
            ],
            sample_answer=(
                "Technology changes faster than any other macro-environment component, so businesses may struggle to "
                "keep up. Employees may lack the skills to operate or maintain new equipment, and buying and maintaining "
                "current technology is expensive. Dependence on technology means systems failure can paralyse operations "
                "and cause loss of capital, while cyberattacks can steal, erase or change confidential data."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                f"Choose TWO components of the macro environment and explain how each could specifically "
                f"challenge {biz}. Support each point with a practical example. (6)"
            ),
            marking_points=[
                "Name and define the first chosen component.",
                "Explain a specific challenge it creates for the business with an example.",
                "Name and define the second chosen component.",
                "Explain a specific challenge it creates for the business with an example.",
                "Link the challenge to the fact that the business has NO control over the macro environment.",
                "Conclude with a strategy the business could use to respond.",
            ],
            sample_answer=(
                "The economic environment refers to the external economic factors that influence the buying habits of "
                "consumers and businesses. If inflation rises, the cost of stock and fuel increases, customers buy less, "
                "and the business's profit margin falls; the business should renegotiate supplier contracts and review "
                "its pricing. The legal environment refers to the laws passed by government that businesses must adhere "
                "to. If the CPA tightens labelling requirements or the NCA forces costly background checks on credit "
                "customers, compliance becomes time-consuming and expensive and the business could be liable for fines. "
                "Because a business has no control at all over the macro environment, it must monitor these components "
                "constantly (for example by using PESTLE) and plan contingencies rather than assume conditions will hold."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Definitions lifted directly from the CAPS 'Key concepts' list."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete each definition of a macro-environment component using the word bank.",
            pool=["Demographic", "Technological", "Institutional", "Cultural", "Global", "Physical"],
            blanks=["1", "2", "3"],
            correct_map={"1": "Demographic", "2": "Technological", "3": "Institutional"},
            text_parts=[
                "The ",
                " environment refers to the socio-economic characteristics of a population used to identify customer preferences and purchasing behaviour.",
                "The ",
                " environment refers to developments, new inventions and improvements in techniques that affect businesses.",
                "The ",
                " environment refers to the three levels of government in South Africa that put laws and rules in place to regulate how businesses operate.",
            ],
            explanation="Demographic = population characteristics; Technological = inventions and techniques; Institutional = the three levels of government.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Fill in the economic terms that are missing from the sentences below.",
            pool=["inflation", "interest rates", "exchange rates", "recession", "credit", "petrol price"],
            blanks=["1", "2", "3"],
            correct_map={"1": "inflation", "2": "interest rates", "3": "exchange rates"},
            text_parts=[
                " ",
                " decreases the value of money and raises costs such as the price of fuel.",
                "High ",
                " mean that loans become more expensive for a business.",
                "The ",
                " is the price of the rand in terms of another currency and it affects imports and exports.",
            ],
            explanation="Inflation reduces the value of money; high interest rates make borrowing expensive; the exchange rate is the price of the rand against another currency.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Choose the correct term from the word bank to complete each statement.",
            pool=["sustainability", "multinational corporation", "acronym", "productivity", "impact", "by-laws"],
            blanks=["1", "2", "3"],
            correct_map={"1": "sustainability", "2": "multinational corporation", "3": "acronym"},
            text_parts=[
                " ",
                " is the use of natural products and energy in a way that does not harm the environment.",
                "A ",
                " is a large corporation incorporated in one country which produces or sells goods or services in various countries.",
                "PESTLE is an ",
                " \u2014 an abbreviation formed from the initial letters of other words and pronounced as a word.",
            ],
            explanation="Sustainability protects the environment; a multinational corporation operates in many countries; an acronym is formed from initial letters (as the CAPS document defines it).",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Match each macro-environment component or Act to the CAPS definition."
    """
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each macro-environment component with its correct CAPS definition.",
            column_a=["Demographic environment", "Technological environment", "Institutional environment", "Cultural environment", "Global environment", "Physical environment"],
            column_b=[
                "The uncontrollable local and international interactions that influence how businesses operate",
                "Natural and man-made variables that surround businesses",
                "The socio-economic characteristics of a population used to identify customer behaviour",
                "The three levels of government in South Africa that put laws and rules in place",
                "Religion, customs and traditions that influence actions and decisions",
                "Development in technology with new inventions and improvements in techniques",
            ],
            correct_pairs={
                "Demographic environment": "The socio-economic characteristics of a population used to identify customer behaviour",
                "Technological environment": "Development in technology with new inventions and improvements in techniques",
                "Institutional environment": "The three levels of government in South Africa that put laws and rules in place",
                "Cultural environment": "Religion, customs and traditions that influence actions and decisions",
                "Global environment": "The uncontrollable local and international interactions that influence how businesses operate",
                "Physical environment": "Natural and man-made variables that surround businesses",
            },
            explanation="These are the exact definitions given in the CAPS 'Key concepts' list for this topic. Note that 'institutional' refers to the three levels of government, while 'political' refers to government actions and stakeholders.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each South African law or body with what it requires of a business (legal environment).",
            column_a=["Consumer Protection Act (CPA)", "National Credit Act (NCA)", "Basic Conditions of Employment Act (BCEA)", "COIDA", "Municipal by-laws"],
            column_b=[
                "Dictates how employees should be treated, including working conditions",
                "Requires the business to give information on the ingredients of the product",
                "Requires the business to apply for a trading licence before trading legally",
                "Requires background checks on clients, which may be costly and time-consuming",
                "Provides compensation for occupational injuries and diseases",
            ],
            correct_pairs={
                "Consumer Protection Act (CPA)": "Requires the business to give information on the ingredients of the product",
                "National Credit Act (NCA)": "Requires background checks on clients, which may be costly and time-consuming",
                "Basic Conditions of Employment Act (BCEA)": "Dictates how employees should be treated, including working conditions",
                "COIDA": "Provides compensation for occupational injuries and diseases",
                "Municipal by-laws": "Requires the business to apply for a trading licence before trading legally",
            },
            explanation="The CAPS legal-environment table groups the CPA and NCA under consumer law, the LRA/BCEA/COIDA under labour law, and zoning, business hours and licences under municipal by-laws. (Misconception to avoid: omitted_legislation_impact.)",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """CAPS Activity 4.2 crossword (components of the three environments) plus a challenge-vocabulary grid."
    """
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt=(
                "Activity 4.2 \u2013 Components of the environments. Read each clue and complete the "
                "crossword with the correct macro-environment component."
            ),
            words=["ECONOMIC", "POLITICAL", "CULTURAL", "DEMOGRAPHIC", "TECHNOLOGICAL", "GLOBAL", "INSTITUTIONAL", "PHYSICAL", "SOCIAL"],
            clues={
                "ECONOMIC": "Refers to all the external economic factors that influence the buying habits of consumers and businesses",
                "POLITICAL": "The government and its institutions, and the public and private stakeholders that influence businesses",
                "CULTURAL": "Includes religion, customs and traditions that influence actions and decisions",
                "DEMOGRAPHIC": "The socio-economic characteristics of a population used to identify product preferences and purchasing behaviour",
                "TECHNOLOGICAL": "Development in the field of technology with new inventions and improvements in techniques",
                "GLOBAL": "The uncontrollable local and international interactions that influence how businesses operate",
                "INSTITUTIONAL": "Refers to the three levels of government in South Africa that put laws and rules in place",
                "PHYSICAL": "Refers to natural and man-made variables that surround businesses",
                "SOCIAL": "Refers to the immediate physical and social setting in which people live",
            },
            grid_size=15,
            explanation="This is the official CAPS Activity 4.2 crossword. Down: Institutional, Physical, Social. Across: Economic, Political, Cultural, Demographic, Technological, Global.",
            marks=9,
            visual_aid_key=VAID,
        ),
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="This crossword covers the CHALLENGES of the macro environment described in the CAPS table.",
            words=["INFLATION", "RECESSION", "CORRUPTION", "POLLUTION", "CYBERATTACK", "LICENCE", "STRIKE", "PATENT"],
            clues={
                "INFLATION": "A general increase in prices and a decrease in the purchasing power of money",
                "RECESSION": "A downswing of the business cycle that restricts businesses from continuing to operate",
                "CORRUPTION": "Impacts the implementation of the rule of law and makes investors lose trust in a business",
                "POLLUTION": "Air, water and noise waste that threatens the sustainability of a business",
                "CYBERATTACK": "Fraudsters hacking IT systems to steal, erase or change data",
                "LICENCE": "A business must apply for a trading \u2026 before it may legally trade",
                "STRIKE": "Workers refusing to work until their demands are met",
                "PATENT": "A legal right granted for a new invention, part of the technological/legal environment",
            },
            grid_size=14,
            explanation="Each answer is a named example of a macro-environment challenge: economic (inflation, recession), political (corruption), physical (pollution), technological (cyberattack), legal (licence, patent) and social/political (strike).",
            marks=8,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Extended PESTLE writing tasks with rubrics and full model answers."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                " 'A business has no control whatsoever over the macro environment, yet it must respond "
                "to it constantly.' Carry out a PESTLE analysis of the macro environment of a South "
                f"African small business such as {biz}, explaining ONE challenge and ONE opportunity per "
                "PESTLE factor, and recommend how the business should respond. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Define the macro environment, state that it is the external environment over which the business has no control, and explain what PESTLE stands for."},
                {"criterion": "Political and Economic analysis", "marks": 4, "description": "Give a challenge and an opportunity for both the political (incl. institutional) and economic environments with examples."},
                {"criterion": "Social and Technological analysis", "marks": 4, "description": "Give a challenge and an opportunity for both the social (incl. cultural/demographic) and technological environments with examples."},
                {"criterion": "Legal and Environmental analysis", "marks": 4, "description": "Give a challenge and an opportunity for both the legal and environmental (physical/global) environments with examples."},
                {"criterion": "Recommendations", "marks": 5, "description": "Practical responses the business can make, recognising that a change in one environment affects the others."},
            ],
            sample_answer=(
                "The macro environment is the external environment; it refers to the interaction of businesses with forces "
                "outside of themselves. It presents both opportunities and threats, is always changing and developing, and "
                "businesses have no control over it. PESTLE groups its ten components into Political (including institutional), "
                "Economic, Social (including cultural and demographic), Technological, Legal and Environmental (including physical "
                "and global). POLITICALLY, a challenge is that protests and strikes cause political instability and delays in "
                "productivity, and tax changes act like cost increases; an opportunity is government policy that supports small "
                "businesses in townships. ECONOMICALLY, inflation and rising petrol prices reduce sales and profitability and high "
                "interest rates make loans expensive; but a decline in interest rates or favourable tax changes are opportunities, "
                "so the business should time its borrowing. SOCIALLY, poverty, unemployment, crime, HIV/AIDS and low literacy "
                "reduce consumer spending and employee productivity; however South Africa's eleven official languages and cultural "
                "diversity are an opportunity to design inclusive marketing. TECHNOLOGICALLY, the fastest-changing component means "
                "the business may not keep up, staff may lack skills, equipment is costly to maintain, systems failure can paralyse "
                "operations and cyberattacks can expose data; the opportunity is reaching customers through smartphones and wireless "
                "services. LEGALLY, the CPA, NCA, LRA, BCEA, COIDA, BBBEE, EEA and municipal by-laws make compliance time-consuming "
                "and non-adherence can lead to fines; a well-run compliance regime is itself an opportunity because it builds "
                "consumer trust. ENVIRONMENTALLY, unpredictable weather, scarce and expensive non-renewable resources, and the cost "
                "of waste disposal are challenges, while global markets offer new customers and international competition encourages "
                "efficiency. The business should respond by conducting regular PESTLE scans, budgeting for compliance, backing up "
                "and securing its systems, training employees, diversifying suppliers to reduce exposure to exchange rates, and "
                "adopting sustainable energy to lower cost and pollution. Because a change in one environment affects the others \u2014 "
                "as the corona virus showed by hitting both the social and economic environments simultaneously \u2014 no single response "
                "is enough. In conclusion, although the business cannot control the macro environment, disciplined monitoring and "
                "contingency planning convert its threats into opportunities."
            ),
            marks=20,
            min_words=250,
            max_words=450,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                "Using the Dukaan Bicycle Repairs scenario in Ritzfontein \u2014 high unemployment, residents "
                "protesting against poor service delivery, and businesses dumping waste on a nearby field \u2014 "
                "discuss the macro-environment challenges facing the business and evaluate the extent to which "
                "Kayvaan can overcome them. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "State the meaning of the macro environment and outline the situation of Dukaan Bicycle Repairs."},
                {"criterion": "Identification of components", "marks": 5, "description": "Correctly identify the social, political and environmental components with direct quotations from the scenario."},
                {"criterion": "Analysis of each challenge", "marks": 6, "description": "Explain the impact of each factor on demand, operations and costs."},
                {"criterion": "Evaluation of control", "marks": 4, "description": "Evaluate honestly what Kayvaan cannot control and what he can influence, with practical strategies."},
                {"criterion": "Conclusion", "marks": 2, "description": "A reasoned final judgement on the extent to which the challenges can be overcome."},
            ],
            sample_answer=(
                "The macro environment consists of forces outside the business over which the business has no control. "
                "Dukaan Bicycle Repairs (DBR) in Ritzfontein faces three clear macro-environment components. Firstly the "
                "SOCIAL environment: 'the unemployment level is quite high'. Unemployment is a social issue that directly "
                "reduces consumer spending, so fewer residents can afford bicycle repairs, and DBR's market shrinks. "
                "Secondly the POLITICAL environment: 'residents in the area are always protesting against poor service "
                "delivery'. Protests and strikes cause political instability and delays in productivity; roads may be "
                "blocked, customers and staff may not reach the shop, and unrest discourages investment in the area. "
                "Thirdly the ENVIRONMENTAL (physical/natural) environment: 'some businesses in the area dump waste material "
                "on the nearby field'. Pollution threatens the sustainability of the business, and responsible disposal of "
                "DBR's own hazardous waste \u2014 old tyres, chains and oil \u2014 may be expensive. Kayvaan cannot control any of "
                "these factors, which is exactly why the macro environment is a challenge. He can, however, influence their "
                "effects. Against high unemployment he can offer payment arrangements, repair-and-refurbish options at lower "
                "price points, and market to delivery companies and schools whose bicycles must stay working, so his income "
                "does not depend only on disposable household income. Against unrest he can keep stock on hand for busy "
                "periods, offer a collection-and-return service when roads are blocked, and remain open on days when protests "
                "are announced. Against pollution he can separate and recycle tyres and metal, which lowers disposal cost and "
                "improves his public image, and he can partner with local CBOs running clean-up campaigns. The extent to which "
                "he can overcome these challenges is therefore limited but real: he cannot lift employment or stop protests, "
                "but he can make DBR resilient to them. In conclusion, the smart response to the macro environment is not "
                "control but adaptation \u2014 monitoring the environment, planning contingencies and turning emerging threats "
                "into opportunities before competitors do."
            ),
            marks=20,
            min_words=250,
            max_words=450,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "application": _application(r),
        "discussion": _discussion(r),
        "word_bank": _wordbank(r),
        "matching": _matching(r),
        "crossword": _crossword(r),
        "essay": _essay(r),
    }


generate_macro_environment = build_generate(_pools)
