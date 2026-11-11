"""Grade 10 Business Studies - Term 1 - Topic 2: The market environment.

Deterministic generator (no LLM). Content hand-authored from the CAPS notes,
activities and consolidation questions in
``curriculum_docs_auto/BusinessStudies_Gr10/Term 1/02. The market environment.md``.

All six archetypes are covered so that every question format the Business
Studies UI can render is available for this topic:
    concepts    -> mcq (recall / understanding of market-environment components)
    application -> scenario-based mcq + typed (identify & motivate from scenarios)
    discussion  -> typed (outline / explain / discuss, with memos)
    word_bank   -> fill-in definitions from a term bank
    matching    -> match component to its description
    crossword   -> key vocabulary from the topic
    essay       -> long-form rubric-marked answer with a model answer
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

PREFIX = "g10bs_market"
VAID = "market_environment"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The market environment of a business is best described as the …",
            options=[
                "internal environment over which the business has full control",
                "immediate external environment that the business can influence but not fully control",
                "macro environment over which the business has no control",
                "physical resources owned by the business",
            ],
            correct_index=1,
            explanation="The market environment is the immediate external environment; the business has limited control but can influence it.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Individuals or businesses that provide a business with inputs/raw materials are called …",
            options=["consumers", "suppliers", "intermediaries", "competitors"],
            correct_index=1,
            explanation="Suppliers provide the inputs/resources a business needs to produce its goods and services.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Agents or businesses that distribute and sell the goods of other businesses, linking producer and consumer, are …",
            options=["intermediaries", "regulators", "unions", "competitors"],
            correct_index=0,
            explanation="Intermediaries (wholesalers, retailers, agents, brokers) bridge the gap between producers and consumers.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that sell more or less the same goods/services are known as …",
            options=["suppliers", "intermediaries", "competitors", "strategic allies"],
            correct_index=2,
            explanation="Competitors sell more or less the same goods/services, forcing businesses to compete on quality and price.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Government bodies that make rules and regulations to monitor businesses (e.g. SABS, ACSA) are called …",
            options=["unions", "regulators", "CBOs", "intermediaries"],
            correct_index=1,
            explanation="Regulators are government bodies that make rules and regulations to control business activities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An organised group of workers that protects the interests of its members is a/an …",
            options=["union", "NGO", "CBO", "strategic ally"],
            correct_index=0,
            explanation="A union is an organised group of workers that protects members' interests and negotiates wages and conditions.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Non-profit organisations that operate separately from government to meet community needs are …",
            options=["regulators", "NGOs", "competitors", "intermediaries"],
            correct_index=1,
            explanation="NGOs are non-governmental, non-profit organisations established to fulfil community needs.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses that combine their resources to undertake a project that benefits all of them are …",
            options=["competitors", "strategic allies", "regulators", "unions"],
            correct_index=1,
            explanation="Strategic allies combine resources and share expertise to benefit all members of the alliance.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is an OPPORTUNITY in the external environment?",
            options=[
                "Increase in taxes",
                "New businesses entering the market",
                "Decline in interest rates",
                "Industrial action (strikes)",
            ],
            correct_index=2,
            explanation="A decline in interest rates is an opportunity; increased taxes, new entrants and strikes are threats.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is a THREAT in the external environment?",
            options=[
                "Decrease in taxes",
                "Closing down of a competitor",
                "Increase in interest rates",
                "Favourable government legislation",
            ],
            correct_index=2,
            explanation="An increase in interest rates is a threat; the others are opportunities.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A business identifies opportunities and threats in its environment by conducting a …",
            options=["SWOT analysis", "PESTLE forecast", "balance sheet", "cash budget"],
            correct_index=0,
            explanation="A SWOT analysis identifies strengths, weaknesses, opportunities and threats.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=f"{biz} buys its raw materials from another business at fixed prices via a long-term contract. That other business is its …",
            options=["competitor", "supplier", "regulator", "intermediary"],
            correct_index=1,
            explanation="The business providing inputs/raw materials is the supplier; long-term contracts build good supplier relationships.",
            visual_aid_key=VAID,
        ),
        # --- Additional CAPS-grounded recall questions ---
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A MARKET, in business terms, is best described as …",
            options=[
                "a physical place where goods are stored",
                "any transaction that brings buyers and sellers together to exchange goods or services for money",
                "the group of employees working for a business",
                "a government body that controls prices",
            ],
            correct_index=1,
            explanation="A market is any transaction that brings buyers and sellers together to exchange goods/services for money.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which ONE of the following is a component of the market environment?",
            options=["Organisational culture", "Intermediaries", "Production function", "Mission statement"],
            correct_index=1,
            explanation="Intermediaries are part of the immediate external (market) environment; culture, functions and the mission statement are internal (micro).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Wholesalers, retailers, agents and brokers are examples of …",
            options=["regulators", "competitors", "intermediaries", "CBOs"],
            correct_index=2,
            explanation="Intermediaries include wholesalers, retailers, agents, brokers and transportation services; they bridge the gap between producers and consumers.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which intermediary sells the products of OTHER businesses on their behalf, for a commission?",
            options=["An agent", "A wholesaler", "A retailer", "A regulator"],
            correct_index=0,
            explanation="Agents are individuals or businesses that sell the products of other businesses for a commission.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which intermediary buys goods in BULK from producers and resells them in SMALLER quantities to retailers?",
            options=["Retailers", "Wholesalers", "Brokers", "Agents"],
            correct_index=1,
            explanation="Wholesalers buy in bulk from producers and sell in smaller quantities to retailers; retailers then sell to consumers.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Community-based organisations (CBOs) form part of the market environment because they …",
            options=[
                "make rules and regulations for businesses",
                "provide essential goods and services to members of the community",
                "compete with the business for the same customers",
                "negotiate wages on behalf of workers",
            ],
            correct_index=1,
            explanation="CBOs are community-based organisations that provide certain essential goods and services to members of the community.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The South African Bureau of Standards (SABS) and Airports Company South Africa (ACSA) are examples of …",
            options=["NGOs", "unions", "regulators", "strategic allies"],
            correct_index=2,
            explanation="Regulators are government bodies/institutions that make rules and regulations to monitor the operations of businesses; SABS and ACSA are given examples.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A worker who refuses to report for duty so that the employer meets the workers' demands is taking part in a …",
            options=["go-slow", "strike", "lock-out", " disciplinary hearing"],
            correct_index=1,
            explanation="A strike is a situation whereby workers refuse to work in order for their demands to be met.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Workers report for duty but DELIBERATELY work at a slower pace. This form of industrial action is called a …",
            options=["strike", "go-slow", "picket", "shutdown"],
            correct_index=1,
            explanation="A go-slow is when workers go to work but deliberately work at a slower pace.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Inflation, which threatens a business, is BEST defined as …",
            options=[
                "a general increase in prices and a decrease in the purchasing power of money",
                "an increase in the value of the rand against the dollar",
                "a decrease in the country's total production",
                "government spending more than it collects in taxes",
            ],
            correct_index=0,
            explanation="Inflation is a general increase in prices and a decrease in the purchasing power of money.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="TAXES, as they affect a business, are …",
            options=[
                "voluntary donations made by businesses to charity",
                "a compulsory contribution to state revenue deducted from income",
                "the fees charged by intermediaries",
                "interest paid on a bank overdraft",
            ],
            correct_index=1,
            explanation="Taxes are a compulsory contribution to state revenue made by businesses and individuals from their income.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="LEGISLATION, in a business context, refers to …",
            options=["the laws passed by parliament", "the process of making laws of the country", "company rules and codes of conduct", "municipal by-laws only"],
            correct_index=1,
            explanation="The CAPS definition given for this topic is that legislation is the process of making laws of the country.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Why must businesses constantly monitor the changing preferences and tastes of their consumers?",
            options=[
                "Because consumers who are unhappy will turn to a competitor",
                "Because regulators require annual customer reports",
                "Because unions negotiate prices with customers",
                "Because suppliers set the retail prices",
            ],
            correct_index=0,
            explanation="Customer preferences and tastes change over time; if customers are not happy with the products or services of a business, they will turn to a competitor.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is NOT one of the forces that influence competition in a market?",
            options=[
                "Power of consumers",
                "Threat of substitute products or services",
                "The colour of the business's logo",
                "Competitive rivalry",
            ],
            correct_index=2,
            explanation="The forces influencing competition are the power of consumers, power of suppliers, threat of substitutes, new entrants and competitive rivalry. Logo colour is irrelevant.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Competition is beneficial to customers MAINLY because it …",
            options=["keeps prices down", "removes the need for suppliers", "guarantees profit for business", "is controlled by unions"],
            correct_index=0,
            explanation="Competition is beneficial to customers because it keeps prices down and forces businesses to offer better quality.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A business that combines its resources with other businesses to undertake a project that benefits ALL of them is acting as a …",
            options=["regulator", "strategic ally", "wholesaler", "non-governmental organisation"],
            correct_index=1,
            explanation="Strategic allies join their resources together to undertake a project that will benefit all the members in the alliance.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which FOUR socio-economic issues do CBOs in communities most often focus on?",
            options=[
                "HIV/AIDS, unemployment, crime and illiteracy",
                "inflation, interest rates, taxes and exchange rates",
                "merging, acquisition, privatisation and globalisation",
                "supply, demand, price and competition",
            ],
            correct_index=0,
            explanation="The CAPS activity answer names HIV/AIDS, unemployment, crime and illiteracy as the socio-economic issues CBOs focus on.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of the market environment. (2)",
            marking_points=[
                "It is the immediate external environment of the business.",
                "The business has limited/little control over it but can influence it.",
            ],
            sample_answer="The market environment is the immediate external environment of the business. The business has limited control over it but is able to influence its components to some extent.",
            marks=2,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between CBOs and NGOs. (8)",
            marking_points=[
                "CBOs assist the community with job creation, socio-economic development and self-sufficiency.",
                "CBOs are local organisations providing social services aimed at social upliftment.",
                "NGOs are non-profit organisations that operate separately from government.",
                "NGOs are established to fulfil important community needs by addressing socio-economic issues.",
            ],
            sample_answer="CBOs are local community-based organisations that assist with job creation and socio-economic development, aiming at social upliftment. NGOs are non-profit organisations operating separately from government, established to address socio-economic issues and meet important community needs.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Describe intermediaries as a component of the market environment. (4)",
            marking_points=[
                "Individuals or businesses that distribute and sell the products/services of a business.",
                "They bridge the gap between producers and consumers.",
                "Include wholesalers, retailers, agents, brokers and transport services.",
                "Some assist businesses with packaging and advertising.",
            ],
            sample_answer="Intermediaries are individuals or businesses that distribute and sell the products of other businesses, bridging the gap between producers and consumers. They include wholesalers, retailers, agents and brokers, and some also help with packaging and advertising.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of 'opportunities' and give TWO practical examples. (4)",
            marking_points=[
                "Opportunities are external factors that contribute to the success of the business.",
                "Example: decrease in taxes / decline in interest rates.",
                "Example: closing down of a competitor / favourable legislation.",
            ],
            sample_answer="Opportunities are factors in the external environment that contribute, or are already contributing, to the success of the business. Examples include a decline in interest rates and the closing down of a competitor.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of 'threats' and give TWO practical examples. (4)",
            marking_points=[
                "Threats are external factors that prevent the business from achieving its goals.",
                "Example: increase in taxes / increase in interest rates.",
                "Example: new businesses entering the market / industrial action.",
            ],
            sample_answer="Threats are factors in the external environment that stand in the way of the business achieving its goals. Examples include an increase in taxes and new businesses entering the market.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the role of unions in the market environment. (4)",
            marking_points=[
                "Unions protect the interests of workers.",
                "They negotiate for better wages, salaries and working conditions.",
                "They may call for industrial action such as strikes or go-slows.",
                "They safeguard members against unfair dismissal and represent them at disciplinary hearings.",
            ],
            sample_answer="Unions are established bodies that protect workers' interests. They negotiate for better wages and working conditions, may call for industrial action like strikes, and safeguard members against unfair dismissal, representing them at disciplinary hearings.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain why NGOs and CBOs form part of the market environment. (4)",
            marking_points=[
                "They supply consumer goods and services.",
                "They are concerned about the welfare of others.",
                "They are local organisations providing social services aimed at social upliftment.",
            ],
            sample_answer="NGOs and CBOs form part of the market environment because they supply consumer goods and services and are concerned about the welfare of others, operating locally to provide social services aimed at social upliftment.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss strategic allies as a component of the market environment. (4)",
            marking_points=[
                "Strategic allies are businesses that combine their resources to undertake a project.",
                "The project benefits all members of the alliance.",
                "They share expertise and information.",
                "Alliances help explore new markets and gain competitive advantage.",
            ],
            sample_answer="Strategic allies are businesses that combine their resources to undertake a project that benefits all of them. They share expertise and information, which helps them explore new markets and gain a competitive advantage.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    """Scenario-based application: identify components/opportunities/threats and MOTIVATE.

    Mirrors the CAPS learning objective: 'identify the components of the market
    environment from a given scenario/statements/case study and motivate your answer'.
    Uses the two CAPS case studies: Sipho's Gardening Services and Mazzars Suppliers.
    """
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Sipho's Gardening Services (SGS) buys gardening materials from Jan Garden "
                "Accessories (JGA) at a reasonable price. Which component of the market "
                "environment does JGA represent for SGS?"
            ),
            options=["A competitor", "A supplier", "An intermediary", "A regulator"],
            correct_index=1,
            explanation="JGA provides SGS with the inputs (gardening materials) it needs to deliver its services, so JGA is a supplier.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Zane opens a gardening service in the SAME area as SGS and charges much lower "
                "prices. Zane's business is an example of a/an \u2026 for SGS."
            ),
            options=["opportunity", "supplier", "competitor", "strategic ally"],
            correct_index=2,
            explanation="Zane sells more or less the same service in the same area at lower prices, so Zane is a competitor \u2014 and a threat \u2014 to SGS.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Mazzars Suppliers (MS) in Orange Farm specialises in generators and identified "
                "the NEED for generators because of load shedding. In a SWOT analysis this is a/an \u2026"
            ),
            options=["strength", "weakness", "opportunity", "threat"],
            correct_index=2,
            explanation="Load shedding creating demand for generators is an EXTERNAL factor contributing to MS's success, so it is an opportunity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "MS discovers that Kay Electronics ALSO supplies generators in Orange Farm. "
                "How should MS classify Kay Electronics?"
            ),
            options=["An internal weakness", "A competitor and a threat", "A supplier", "A regulator"],
            correct_index=1,
            explanation="Kay Electronics sells the same product in the same market, so it is a competitor, which is an external threat to MS.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "MS is situated in an area with a HIGH CRIME RATE. Within a SWOT analysis this is a/an \u2026"
            ),
            options=["opportunity", "strength", "threat", "weakness"],
            correct_index=2,
            explanation="A high crime rate is an EXTERNAL negative factor standing in the way of MS reaching its goals, so it is a threat (not a weakness, which would be internal).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Which ONE of the following statements about the market environment of "
                f"{biz} is CORRECT?"
            ),
            options=[
                "It is the internal environment that the business fully controls",
                "It is the immediate external environment that the business can influence but not fully control",
                "It consists only of government laws the business cannot influence at all",
                "It is the same as the macro environment",
            ],
            correct_index=1,
            explanation="The market environment is the immediate EXTERNAL environment; the business has limited control but can influence it. The macro environment (Topic 3) is the one the business cannot control.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Classify the following SWOT items: (i) a reliable supply of raw materials, "
                "(ii) well-trained and skilled employees, (iii) a new competitor entering the "
                "market, (iv) very high production costs."
            ),
            options=[
                "(i) opportunity (ii) strength (iii) threat (iv) weakness",
                "(i) strength (ii) opportunity (iii) weakness (iv) threat",
                "(i) threat (ii) weakness (iii) opportunity (iv) strength",
                "(i) opportunity (ii) threat (iii) strength (iv) weakness",
            ],
            correct_index=0,
            explanation="Suppliers are external, so reliable suppliers are an OPPORTUNITY. Employees are internal, so skilled staff are a STRENGTH; high production costs are an internal WEAKNESS. A new entrant is an external THREAT.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Workers of a factory deliberately work at a slower pace, reducing output. "
                "For that business this is an example of a/an \u2026"
            ),
            options=["internal strength", "external opportunity", "external threat", "internal opportunity"],
            correct_index=2,
            explanation="Industrial action such as a go-slow originates outside the business's own control (it comes from organised labour/the market environment), and it hinders the business, so it is a threat.",
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Read the scenario and answer the questions that follow.\n"
                "MAZZARS SUPPLIERS (MS) specialises in supplying generators in Orange Farm. MS "
                "identified the need for generators because of load shedding. MS also discovered "
                "that Kay Electronics supplies generators in Orange Farm. MS has identified a need "
                "for its generators in other townships of Johannesburg. MS is situated in an area "
                "with a high crime rate.\n\n"
                "Identify TWO opportunities and TWO threats for MS. (4)"
            ),
            marking_points=[
                "Opportunity: MS identified the need for generators because of load shedding.",
                "Opportunity: MS identified a need for its generators in other townships of Johannesburg (new markets).",
                "Threat: Kay Electronics also supplies generators in Orange Farm (competition).",
                "Threat: MS is situated in an area with a high crime rate.",
            ],
            sample_answer=(
                "OPPORTUNITIES: (1) MS identified the need for generators because of load shedding. "
                "(2) MS has identified a need for its generators in other townships of Johannesburg, "
                "opening up new markets. THREATS: (1) Kay Electronics also supplies generators in "
                "Orange Farm, so MS faces direct competition. (2) MS is situated in an area with a "
                "high crime rate, which can disrupt its operations."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Read the scenario and answer the questions that follow.\n"
                "SIPHO, the owner of Sipho's Gardening Services (SGS), provides goods and services "
                "to clients in his hometown. Sipho buys gardening materials from Jan Garden "
                "Accessories (JGA) at a reasonable price. Zane has opened a gardening service in the "
                "same area as Sipho at very low prices.\n\n"
                "Name the component of the market environment that JGA and Zane each represent for "
                "SGS, and MOTIVATE each answer. (4)"
            ),
            marking_points=[
                "JGA is a SUPPLIER.",
                "Motivate: JGA provides SGS with the inputs/gardening materials it needs to produce its services.",
                "Zane is a COMPETITOR.",
                "Motivate: Zane sells more or less the same service in the same area, so SGS may lose customers to him.",
            ],
            sample_answer=(
                "JGA is a supplier of SGS, because JGA provides SGS with the inputs (gardening "
                "materials) it needs in order to produce/deliver its services. Zane is a competitor "
                "of SGS, because Zane offers more or less the same gardening service in the same "
                "area at very low prices, which means SGS could lose customers to him."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "A clothing retailer in Ladysmith notices that a nearby competitor has closed down "
                "and that the municipality has introduced favourable zoning legislation. "
                "Recommend TWO strategies the retailer can use to turn these opportunities into "
                "a competitive advantage. (4)"
            ),
            marking_points=[
                "Absorb the closed competitor's former customers by advertising/market research to target that market.",
                "Expand product range or open a new outlet in the vacated area/market segment.",
                "Use the favourable zoning legislation to expand or relocate at lower cost.",
                "Monitor the remaining competitors and keep prices and quality attractive so the gains are retained.",
            ],
            sample_answer=(
                "The retailer should first conduct market research and advertise to attract the former "
                "customers of the closed competitor, possibly widening the product range or opening an "
                "outlet in the area the competitor vacated. Secondly, the retailer should use the "
                "favourable zoning legislation to expand or relocate at a lower cost, while continuing "
                "to monitor remaining competitors on price and quality so that the new advantage is sustained."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                f"{biz} relies on a single supplier for its raw materials and has just been told "
                "that the supplier will raise prices by 15%. Suggest how the business should "
                "respond to this threat. (4)"
            ),
            marking_points=[
                "Identify/develop alternative reliable suppliers so it is not dependent on one.",
                "Negotiate or sign long-term contracts at fixed prices to limit future increases.",
                "Review its own cost structure and consider passing part of the increase to consumers carefully.",
                "Conduct a SWOT/monitoring exercise so emerging threats are detected early.",
            ],
            sample_answer=(
                "The business should reduce its dependence on a single supplier by identifying and "
                "qualifying alternative reliable suppliers. It should negotiate, and where possible sign "
                "long-term contracts at fixed prices, to protect itself from future increases. It must also "
                "review its own costs before deciding how much of the increase can be passed on to consumers, "
                "and continuously scan the market environment so that threats are identified and turned into "
                "opportunities early."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Word-bank items built from the 'Key concepts' list of the CAPS topic document."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Choose the correct term from the word bank to complete each definition of a market-environment component.",
            pool=["Suppliers", "Intermediaries", "Competitors", "Regulators", "Unions", "Consumers"],
            blanks=["1", "2", "3"],
            correct_map={"1": "Suppliers", "2": "Intermediaries", "3": "Competitors"},
            text_parts=[
                "Individuals or businesses that provide a business with the inputs or raw materials it needs are called ",
                ".",
                " Agents or businesses that distribute and sell the goods of other businesses, bridging the gap between producer and consumer, are ",
                ".",
                " Businesses that sell more or less the same goods and services are ",
                ".",
            ],
            explanation="Suppliers provide inputs; intermediaries bridge producer and consumer; competitors sell similar goods/services.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the statements about organisations in the market environment.",
            pool=["NGOs", "CBOs", "Strategic allies", "government", "profit", "community"],
            blanks=["1", "2", "3"],
            correct_map={"1": "CBOs", "2": "NGOs", "3": "Strategic allies"},
            text_parts=[
                " ",
                " are community-based organisations that provide essential goods and services to the members of the community.",
                " ",
                " are non-profit organisations that operate separately from the government and address socio-economic needs.",
                " ",
                " are businesses that combine their resources to undertake a project that benefits all of them.",
            ],
            explanation="CBOs serve the community directly; NGOs operate separately from government; strategic allies pool resources for mutual benefit.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Fill in each blank with the correct business term from the word bank.",
            pool=["strike", "go-slow", "inflation", "taxes", "legislation", "SWOT", "market research"],
            blanks=["1", "2", "3"],
            correct_map={"1": "strike", "2": "go-slow", "3": "inflation"},
            text_parts=[
                "When workers refuse to work in order for their demands to be met, they are on a ",
                ".",
                "When workers attend work but deliberately work at a slower pace, this is called a ",
                ".",
                "A general increase in prices together with a decrease in the purchasing power of money is ",
                ".",
            ],
            explanation="A strike = refusing to work; a go-slow = working deliberately slowly; inflation = general rise in prices and fall in purchasing power.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Match CAPS terminology to its defining description."""
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each component of the market environment with its correct description.",
            column_a=["Suppliers", "Intermediaries", "Competitors", "Regulators", "Unions", "Strategic allies"],
            column_b=[
                "Businesses that combine their resources to undertake a project that benefits all of them",
                "Individuals or businesses that provide the inputs/raw materials a business needs",
                "Organised groups of workers that protect the interests of their members",
                "Agents or businesses that distribute and sell the goods of other businesses",
                "Government bodies that make rules and regulations to monitor businesses",
                "Businesses that sell more or less the same goods and services",
            ],
            correct_pairs={
                "Suppliers": "Individuals or businesses that provide the inputs/raw materials a business needs",
                "Intermediaries": "Agents or businesses that distribute and sell the goods of other businesses",
                "Competitors": "Businesses that sell more or less the same goods and services",
                "Regulators": "Government bodies that make rules and regulations to monitor businesses",
                "Unions": "Organised groups of workers that protect the interests of their members",
                "Strategic allies": "Businesses that combine their resources to undertake a project that benefits all of them",
            },
            explanation="These are the CAPS definitions of the market-environment components; look for the defining keywords (inputs, distribute, same goods, rules, workers, combine resources).",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each term in Column A with the correct description in Column B.",
            column_a=["Agents", "Wholesalers", "Retailers", "Strike", "Go-slow"],
            column_b=[
                "Buy goods in bulk from producers and sell in smaller quantities to retailers",
                "Workers refuse to work until their demands are met",
                "Sell the products of other businesses for a commission",
                "Workers attend work but deliberately work at a slower pace",
                "Buy stock from wholesalers and sell it to the final consumers",
            ],
            correct_pairs={
                "Agents": "Sell the products of other businesses for a commission",
                "Wholesalers": "Buy goods in bulk from producers and sell in smaller quantities to retailers",
                "Retailers": "Buy stock from wholesalers and sell it to the final consumers",
                "Strike": "Workers refuse to work until their demands are met",
                "Go-slow": "Workers attend work but deliberately work at a slower pace",
            },
            explanation="Agents sell for a commission; wholesalers buy in bulk; retailers sell to consumers; a strike is refusal to work; a go-slow is deliberately slow work.",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """Crossword using the key vocabulary of the topic (acronym expansions included)."""
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="Read each clue and complete the crossword with the correct market-environment term.",
            words=["SUPPLIERS", "INTERMEDIARIES", "COMPETITORS", "REGULATORS", "UNIONS", "CONSUMERS", "ALLIES", "STRIKE"],
            clues={
                "SUPPLIERS": "Businesses that provide a business with the inputs it needs to produce",
                "INTERMEDIARIES": "They bridge the gap between producers and consumers",
                "COMPETITORS": "Businesses that sell more or less the same goods and services",
                "REGULATORS": "Government bodies such as SABS and ACSA that monitor business behaviour",
                "UNIONS": "Organised groups of workers protecting their members' interests",
                "CONSUMERS": "The final users of a product or service",
                "ALLIES": "Strategic \u2026\u2026: businesses that combine resources for a mutual project",
                "STRIKE": "Industrial action in which workers refuse to work",
            },
            grid_size=15,
            explanation="These eight terms are the key vocabulary of the market environment as defined in the CAPS topic document.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="This crossword covers the abbreviations and concepts used in the market environment.",
            words=["SABS", "NGO", "CBO", "SWOT", "INFLATION", "TAXES"],
            clues={
                "SABS": "Abbreviation for the South African Bureau of Standards",
                "NGO": "Non-governmental organisation that serves the community without aiming at profit",
                "CBO": "Abbreviation for a community-based organisation",
                "SWOT": "Analysis used to identify strengths, weaknesses, opportunities and threats",
                "INFLATION": "General increase in prices and decrease in purchasing power",
                "TAXES": "Compulsory contributions to state revenue deducted from income",
            },
            grid_size=12,
            explanation="SABS is a regulator; NGO and CBO are civil-society organisations; SWOT is the tool used to spot opportunities and threats; inflation and taxes are typical external threats.",
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Rubric-marked extended writing tasks tied to the topic's learning objectives."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                " 'The survival of a business depends on how well it manages its relationship with "
                "the components of its market environment.' Discuss the THREE most important "
                "components of the market environment for a retail business such as "
                f"{biz}, and explain how the business should manage each relationship. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 4, "description": "Define the market environment and state that the business has limited control but can influence it; name the components chosen."},
                {"criterion": "Component 1 \u2013 meaning and role", "marks": 4, "description": "Define and describe the first component accurately with a retail example."},
                {"criterion": "Component 2 \u2013 meaning and role", "marks": 4, "description": "Define and describe the second component accurately with a retail example."},
                {"criterion": "Component 3 \u2013 meaning and role", "marks": 4, "description": "Define and describe the third component accurately with a retail example."},
                {"criterion": "Relationship management strategies", "marks": 4, "description": "Explain practical strategies (long-term contracts at fixed prices, market research, monitoring competitors, service recovery)."},
            ],
            sample_answer=(
                "The market environment is the immediate external environment of a business; it consists of the "
                "components that directly affect the business's ability to operate. The business has limited control "
                "over these components but can influence them. Three vital components for a retail business are "
                "consumers, suppliers and competitors. Consumers are the individuals or other businesses that buy the "
                "retailer's goods and are the final users of the product; because their tastes change over time, the "
                "retailer must conduct ongoing market research, because unhappy customers simply turn to a competitor. "
                "Suppliers provide the retailer with the stock it needs; if inputs are late, poor quality or overpriced "
                "the retailer cannot meet its objectives, so it should identify reliable suppliers and sign long-term "
                "contracts at fixed prices. Competitors are businesses selling more or less the same goods; the retailer "
                "must monitor their activities and offer better quality at the lowest possible price. Intermediaries such "
                "as wholesalers and retailers, regulators such as the SABS, unions and NGOs/CBOs also form part of this "
                "environment. To manage these relationships the business should build partnerships with suppliers, invest "
                "in customer service and loyalty programmes, benchmark itself against competitors, and comply with the "
                "rules set by regulators. In conclusion, a retail business that actively influences its market environment "
                "and converts threats into opportunities through tools such as a SWOT analysis is far more likely to "
                "survive and grow than one that ignores these components."
            ),
            marks=20,
            min_words=200,
            max_words=400,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                "Using Mazzars Suppliers (MS) \u2014 a generator supplier in Orange Farm that identified demand "
                "during load shedding, competes with Kay Electronics, wants to expand to other Johannesburg "
                "townships, and operates in a high-crime area \u2014 conduct a SWOT analysis of the opportunities "
                "and threats in MS's external environment and recommend how MS should respond. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Define opportunities and threats and explain that a SWOT analysis separates internal (S/W) from external (O/T) factors."},
                {"criterion": "Opportunities identified", "marks": 4, "description": "Load-shedding demand; unmet need in other Johannesburg townships; limited competition in the area."},
                {"criterion": "Threats identified", "marks": 4, "description": "Competition from Kay Electronics; high crime rate; dependence on load shedding continuing; possible new entrants."},
                {"criterion": "Recommendations", "marks": 5, "description": "Practical strategies to exploit opportunities and neutralise threats, applied to MS."},
                {"criterion": "Conclusion", "marks": 4, "description": "Summarise why continuous scanning of the market environment keeps MS competitive."},
            ],
            sample_answer=(
                "Opportunities are external factors that contribute, or can contribute, to the success of a business, "
                "while threats are external factors that stand in the way of the business achieving its goals. A SWOT "
                "analysis separates internal strengths and weaknesses from external opportunities and threats. For "
                "Mazzars Suppliers the opportunities are: the clear need for generators created by load shedding; the "
                "identified demand in other townships of Johannesburg, which is an opportunity to expand into new markets; "
                "and the fact that only one other supplier (Kay Electronics) currently operates in Orange Farm, meaning the "
                "market is not saturated. The threats are: Kay Electronics competing directly in the same area; the high "
                "crime rate where MS is situated, which risks stock loss and employee safety; the possibility of new entrants "
                "into the generator market; and the risk that improved electricity supply (for example more stable supply or "
                "solar adoption) would reduce dependence on generators. MS should respond by securing long-term contracts at "
                "fixed prices with reliable suppliers so it can price competitively against Kay Electronics, differentiate "
                "through after-sales service and installation support, and expand deliberately into the townships where demand "
                "has been confirmed rather than spreading too thin. To manage the crime threat it should invest in security, "
                "insurance and stock control, and consider partnering with local CBOs and NGOs that understand the community. "
                "Finally, MS should not rely on load shedding alone: diversifying into solar and backup-power products would "
                "turn a potential threat into a new opportunity. In conclusion, because businesses have no complete control "
                "over the market environment, MS must monitor it continuously and convert threats into opportunities if it "
                "wants to remain successful."
            ),
            marks=20,
            min_words=200,
            max_words=400,
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


generate_market_environment = build_generate(_pools)
