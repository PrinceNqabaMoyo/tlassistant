"""Grade 10 Business Studies - Term 1 - Topic 4: Interrelationship of the micro,
market and macro environments.

Deterministic generator (no LLM). Content hand-authored from the CAPS notes, 'New
Words' glossary, Activities 5.1/5.2 and the consolidation questions in
``curriculum_docs_auto/BusinessStudies_Gr10/Term 1/04. The interrelationship of the
micro market & macro environments.md``.

All six archetypes are covered:
    concepts    -> mcq (who depends on whom, New Words glossary, TEBO Ltd identification)
    application -> scenario mcq + typed (chain-reaction reasoning, motivate with quotes)
    discussion  -> typed (explain the interrelationships, with memos)
    word_bank   -> the CAPS 'New Words' glossary
    matching    -> functions / departments / chain reactions
    crossword   -> topic vocabulary
    essay       -> extended evaluation with a model answer
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

PREFIX = "g10bs_interrel"
VAID = "interrelationship"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which environment has the biggest control and influence over the other two?",
            options=["Micro environment", "Market environment", "Macro environment", "They are equal"],
            correct_index=2,
            explanation="The macro environment has the biggest influence; the micro and market environments can only adapt to it.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'TEBO Ltd uses the services of Malo Distributors to supply products to customers.' This shows a relationship with …",
            options=["suppliers", "intermediaries", "competitors", "consumers"],
            correct_index=1,
            explanation="A business that distributes/sells goods to customers is an intermediary.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'A supermarket discovers another grocery store has opened nearby.' The new store is a …",
            options=["supplier", "intermediary", "competitor", "regulator"],
            correct_index=2,
            explanation="A business selling more or less the same goods/services is a competitor.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'A business purchases raw materials in bulk from Birchwood Ltd.' Birchwood Ltd is a …",
            options=["supplier", "competitor", "consumer", "intermediary"],
            correct_index=0,
            explanation="A business that provides raw materials/inputs is a supplier.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An increase in the interest rate (macro) raises production costs (micro), which raises prices and lowers consumer demand (market). This best illustrates …",
            options=[
                "that the three environments are independent",
                "the interrelationship between the three environments",
                "that the micro environment controls the macro environment",
                "that the market environment is the most powerful",
            ],
            correct_index=1,
            explanation="A change in one environment flows through to the others — this is their interrelationship.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which function coordinates all the other functions to achieve the vision and mission of the business?",
            options=["Marketing function", "General management function", "Purchasing function", "Administration function"],
            correct_index=1,
            explanation="General management coordinates the other functions and seeks information/advice from departmental heads.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Reliable suppliers are those that deliver raw materials at the right quality, quantity, price and …",
            options=["colour", "time", "weight", "brand"],
            correct_index=1,
            explanation="Reliable suppliers deliver the right quality, quantity, price and at the right time.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An individual or business that sells the goods of another business for a commission is a/an …",
            options=["agent", "regulator", "union", "consumer"],
            correct_index=0,
            explanation="An agent distributes and sells the goods/services of another business for a commission.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which environment has the BIGGEST influence and control over both the market and micro environments?",
            options=["The micro environment", "The market environment", "The macro environment", "They all have equal control"],
            correct_index=2,
            explanation="The CAPS document states that the macro environment has the biggest control and influence over both the market and micro environments.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How much control do the market and micro environments have OVER the macro environment?",
            options=[
                "Very little control, but they can adapt to its challenges",
                "Complete control, because they are closer to the business",
                "The same control the macro has over them",
                "Control only through the media",
            ],
            correct_index=0,
            explanation="The market and micro environments have very little control over the macro environment, but they can ADAPT to its challenges.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A SINGLE business has no control over government legislation, BUT a group of businesses CAN influence it by \u2026",
            options=["reducing their prices", "forming a strategic alliance", "hiring more employees", "closing down"],
            correct_index=1,
            explanation="The CAPS example: if businesses come together to form a strategic alliance, they could influence certain aspects of government legislation \u2014 something a single business cannot do.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In the micro environment, which function does GENERAL MANAGEMENT consult to obtain the information it needs to run the affairs of the business?",
            options=["The administration function", "The production function", "The marketing function", "The purchasing function"],
            correct_index=0,
            explanation="The general management function consults the administration function to obtain the relevant information required to run the affairs of the business and develop strategies.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which department must tell the PURCHASING department the type, quality and quantity of resources it needs?",
            options=["The production department", "The public relations department", "The financial department", "The administration department"],
            correct_index=0,
            explanation="The production department informs purchasing about the type, quality and quantity of resources to be ordered so that the required goods/services can be produced.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Customer feedback that allows production to make goods meeting consumer expectations comes from the \u2026 department.",
            options=["marketing", "financial", "purchasing", "administration"],
            correct_index=0,
            explanation="The marketing department provides production with feedback from customers so that goods and services can be produced to meet consumers' expectations.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Before RECRUITING employees, the human resources department must consult other departments to determine the \u2026",
            options=[
                "salaries the company can afford",
                "type of skills and experience those departments need",
                "advertising budget",
                "number of competitors in the market",
            ],
            correct_index=1,
            explanation="Human resources consults the other departments to determine the type of skills and experience required in each department before recruiting.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In a car-manufacturing company, different departments produce the parts that are later combined into a complete car. This illustrates \u2026",
            options=[
                "the interrelationship between departments",
                "the macro environment",
                "the relationship with regulators",
                "external competitive rivalry",
            ],
            correct_index=0,
            explanation="The CAPS example of the interrelationship between DEPARTMENTS: some departments depend on others for resources and to complete the final product.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="REMUNERATE, as used in this topic, means \u2026",
            options=["to dismiss a worker", "payment a worker receives for performing a job", "to promote a worker", "to train a worker"],
            correct_index=1,
            explanation="The 'New Words' glossary defines remunerate as the payment a worker receives for performing a job for the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="To CONSULT means \u2026",
            options=[
                "to seek information or input from other departments",
                "to sell goods in large quantities",
                "to punish employees",
                "to end a contract",
            ],
            correct_index=0,
            explanation="The glossary defines consult as to seek information or input from other departments.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which term means 'achieving maximum productivity with minimum wasted effort or expense'?",
            options=["Efficient", "Reliable", "Accessible", "Interrelated"],
            correct_index=0,
            explanation="The glossary defines efficient as achieving maximum productivity with minimum wasted effort or expense.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A SUPPLY SHORTAGE is a situation whereby businesses find it difficult to \u2026",
            options=[
                "identify suppliers who offer raw material in the right quality, quantity and place",
                "advertise their products on social media",
                "recruit seasonal employees",
                "obtain a trading licence from the municipality",
            ],
            correct_index=0,
            explanation="The glossary defines supply shortage as businesses finding it difficult to identify suppliers offering raw material in the right quality, right quantities and in the right place.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="MARKET RESEARCH is best defined as the activity of \u2026",
            options=[
                "gathering information about customers' needs and preferences",
                "setting the prices of products",
                "hiring marketing employees",
                "registering a business with CIPRO",
            ],
            correct_index=0,
            explanation="The glossary defines market research as the action or activity of gathering information about customers' needs and preferences.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="ACCESSIBILITY, in this topic, means that a product or location is \u2026",
            options=["easily reached", "very expensive", "legally protected", "mass-produced"],
            correct_index=0,
            explanation="The glossary defines accessibility as easily reached \u2014 for example a delivery agent seeking help where accessibility to a destination is restricted.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An ALLIANCE is \u2026",
            options=[
                "two or more businesses that work together in a joint venture",
                "a worker refusing to work",
                "a tax levied on imported goods",
                "a written agreement with a supplier",
            ],
            correct_index=0,
            explanation="The glossary defines an alliance as two or more businesses that work together in a joint venture.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="'Interrelated' means that \u2026",
            options=[
                "a connection or relationship exists between the components",
                "components operate completely independently",
                "one component has bought another",
                "components compete with each other",
            ],
            correct_index=0,
            explanation="The glossary defines interrelated as: there is a connection or relationship between the components.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="GOODS, as defined in this topic, are things that are \u2026",
            options=[
                "produced, bought or sold, then finally consumed",
                "work done by businesses that is not tangible",
                "materials that have not yet been processed",
                "imported from other countries",
            ],
            correct_index=0,
            explanation="The glossary distinguishes goods (produced, bought or sold then finally consumed) from services (work done, not tangible) and raw materials (unprocessed).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is NOT given as a reason why competition poses a challenge to businesses?",
            options=[
                "It is not within the control of the business",
                "Consumers will buy where they get the most value for money",
                "It guarantees higher profits for every business in the market",
                "New entrants with better products divide the market further",
            ],
            correct_index=2,
            explanation="Competition REDUCES prices and profits; it does not guarantee higher profits. The other three are given in the CAPS answer as reasons competition is a challenge.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Evaluate the interrelationships that exist WITHIN the micro environment. (6)",
            marking_points=[
                "Interrelationship between business functions: the eight functions depend on each other.",
                "Interrelationship between departments: e.g. production informs purchasing of the resources needed.",
                "Interrelationship between employer and employee: employees perform duties; employers remunerate and consult them.",
            ],
            sample_answer="Within the micro environment the eight business functions depend on one another, for example general management consults administration for information. Departments also depend on each other, such as production informing purchasing of the resources required. Finally, employers and employees are interrelated: employees perform duties and are remunerated and consulted by employers.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the reasons why competition poses a challenge to businesses. (6)",
            marking_points=[
                "Competition is not within the control of the business.",
                "Consumers buy where they get the most value for money and may choose a competitor.",
                "A business may be unable to make sufficient profit when demand is not high enough.",
                "It is hard to differentiate from competitors to gain a competitive advantage.",
                "New entrants with better products can divide the market and reduce market share.",
            ],
            sample_answer="Competition is challenging because it is outside the business's control. Consumers buy where they get the most value and may choose a competitor, so a business may struggle to make sufficient profit. It is also hard to differentiate from rivals, and new entrants with better products can reduce the business's market share.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between businesses and their consumers. (6)",
            marking_points=[
                "Consumers depend on businesses for goods/services; businesses depend on consumers for income.",
                "Without consumers a business cannot survive, so it must produce consistently high-quality goods.",
                "Public relations must maintain a positive image so customers stay loyal.",
                "Marketing must conduct market research to satisfy changing consumer needs.",
            ],
            sample_answer="Consumers depend on businesses for goods and services, while businesses depend on consumers for income. Because a business cannot survive without consumers, it must produce consistently high-quality goods, maintain a positive image through public relations, and conduct market research to satisfy changing consumer needs.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between a business and its suppliers. (6)",
            marking_points=[
                "Businesses depend on suppliers for raw materials and inputs.",
                "Without raw materials a business cannot produce its goods/services.",
                "Businesses must identify reliable suppliers (right quality, quantity, price, time).",
                "Good relationships are maintained by paying on time and signing long-term contracts.",
            ],
            sample_answer="Businesses depend on suppliers for raw materials and inputs, without which they cannot produce. They must identify reliable suppliers who deliver the right quality, quantity and price at the right time, and maintain good relationships by paying on time and signing long-term contracts at fixed prices.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how a change in the macro environment can affect the micro and market environments. (4)",
            marking_points=[
                "Changes in the macro environment may affect the micro environment, then the market environment.",
                "Example: an increase in interest rates raises production costs.",
                "Higher production costs raise the prices of goods/services.",
                "Higher prices decrease consumer spending/demand.",
            ],
            sample_answer="A change in the macro environment flows through to the micro and then the market environment. For example, an increase in interest rates raises production costs in the micro environment, which increases prices, and this in turn decreases consumer spending in the market environment.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the interrelationship between a business and its intermediaries. (4)",
            marking_points=[
                "Intermediaries distribute and sell the goods of the business; they link business and consumers.",
                "Businesses must maintain good relationships and monitor intermediaries' activities.",
                "Intermediaries must be reliable and efficient as they affect quality and price.",
                "Intermediaries are also customers of the business and should be treated with care.",
            ],
            sample_answer="Intermediaries distribute and sell a business's goods, linking it to consumers. The business must monitor and maintain good relationships with them because their reliability and efficiency affect the quality and price of goods. Intermediaries are also customers, so they should be treated with care.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    """Scenario application: identify the market component (Activity 5.1 TEBO Ltd) and
    reason about the macro → micro → market chain reaction (CAPS Question 2.1 Zipho)."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "TEBO Ltd uses the services of Malo Distributors to supply products to customers. "
                "Which component of the market environment is Malo Distributors?"
            ),
            options=["A supplier", "An intermediary", "A regulator", "A strategic ally"],
            correct_index=1,
            explanation="Malo Distributors distributes and sells products on to customers, so it is an intermediary (the CAPS Activity 5.2 answer is 'Intermediaries').",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="TEBO Ltd's customers buy products from Zane Ltd, which recently opened next door. Zane Ltd is a/an \u2026 of TEBO Ltd.",
            options=["competitor", "supplier", "agent", "union"],
            correct_index=0,
            explanation="Zane Ltd sells more or less the same products in the same area, so it is a competitor (CAPS Activity answer: 'Competitor').",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="TEBO Ltd makes use of individuals to sell its goods for a commission. These individuals are \u2026",
            options=["brokers", "wholesalers", "agents", "regulators"],
            correct_index=2,
            explanation="Agents are individuals or businesses that sell the goods/services of another business for a commission.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="TEBO Ltd purchases raw materials in bulk from Birchwood Ltd. Birchwood Ltd is a/an \u2026 of TEBO Ltd.",
            options=["supplier", "competitor", "intermediary", "consumer"],
            correct_index=0,
            explanation="Birchwood provides the unprocessed raw materials TEBO needs for production, so it is a supplier.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "ZIPHO owns a large industrial window-cleaning company. He buys his machines in the USA "
                "and will now only be able to afford ONE machine because the South African currency has "
                "depreciated dramatically. Which ECONOMIC factor of the macro environment is affecting Zipho?"
            ),
            options=["Inflation", "The exchange rate", "The interest rate", "Conditions of credit"],
            correct_index=1,
            explanation="The CAPS answer is the EXCHANGE RATE \u2014 the price of the rand in terms of another currency \u2014 motivated by 'he buys his machines in the USA and will only be able to buy one machine as the South African currency has depreciated dramatically'.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "An increase in the interest rate raises Zipho's production costs, so he raises his prices "
                "and fewer customers can afford his service. The correct chain of influence is \u2026"
            ),
            options=[
                "MACRO (interest rate) \u2192 MICRO (production cost) \u2192 MARKET (consumer demand)",
                "MARKET (consumer demand) \u2192 MACRO (interest rate) \u2192 MICRO (production cost)",
                "MICRO (production cost) \u2192 MACRO (interest rate) \u2192 MARKET (consumer demand)",
                "MACRO (interest rate) \u2192 MARKET (production cost) \u2192 MICRO (consumer demand)",
            ],
            correct_index=0,
            explanation="The CAPS chain-reaction diagram: an increase in the interest rate is a MACRO change that increases production costs in the MICRO environment, which reduces consumer demand in the MARKET environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "Two years after opening, TEBO Ltd finds that new businesses selling better products have "
                "entered its market and its market share has fallen. This is an example of \u2026"
            ),
            options=[
                "a market-environment change affecting the micro environment of TEBO Ltd",
                "a macro-environment change TEBO Ltd can fully control",
                "an internal micro-environment weakness TEBO Ltd created itself",
                "a change in TEBO Ltd's mission statement",
            ],
            correct_index=0,
            explanation="New competitors entering the market is a MARKET-environment change that affects the micro environment \u2014 the CAPS document states such changes might force businesses to decrease their prices.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                f"A fuel price increase (macro) raises {biz}'s transport costs (micro), which makes its "
                "products dearer than rivals'. What is the MOST likely market-environment result?"
            ),
            options=[
                "Loyal customers will buy even more from the business",
                "Customers may switch to competitors, reducing the business's customer base",
                "Suppliers will stop delivering raw materials",
                "Regulators will remove all legislation",
            ],
            correct_index=1,
            explanation="Higher prices reduce consumer spending; consumers buy where they get the most value for money and could therefore choose a competitor, shrinking the business's customer base.",
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Read the scenario and answer the question that follows.\n"
                "ZIPHO owns a large industrial window-cleaning company. He buys his machines in the USA and "
                "will only be able to buy ONE machine, because the South African currency has depreciated "
                "dramatically.\n\n"
                "Identify the economic factor of the macro environment that has a direct influence on "
                "Zipho's business AND motivate your answer by quoting from the scenario. (4)"
            ),
            marking_points=[
                "The economic factor is the EXCHANGE RATE (1)",
                "Motivation, quoted from the scenario: 'He buys his machines in the USA' (1)",
                "Motivation, quoted: 'will only be able to buy one machine as the South African currency has depreciated dramatically' (1)",
                "Link: the weakened rand makes imported machinery more expensive, so the macro change reduces Zipho's capital equipment (micro) (1)",
            ],
            sample_answer=(
                "The economic factor is the EXCHANGE RATE \u2014 the price of the rand in terms of another currency. "
                "This is motivated by the statements that 'he buys his machines in the USA' and that 'he will only "
                "be able to buy one machine as the South African currency has depreciated dramatically'. Because the "
                "rand has weakened against the US dollar, each imported machine costs far more rands, so a macro-"
                "environment change directly reduces the capital equipment (a micro-environment resource) Zipho can "
                "acquire, which in turn limits how many jobs his company can service."
            ),
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Explain THREE reasons why competition poses a challenge to businesses. (6)"
            ),
            marking_points=[
                "Competition is a component of the market environment and is NOT within the control of the business.",
                "Consumers will buy from the business that gives the most value for money and could choose the competitor.",
                "A business may be unable to make sufficient profit when demand is not high enough.",
                "It is hard to differentiate the business from competitors to gain a competitive advantage.",
                "New entrants with better products divide the market further, decreasing the business's market share.",
                "Each reason must be explained, not merely listed, to earn the second mark.",
            ],
            sample_answer=(
                "Firstly, competition is part of the market environment, so it is outside the control of the business \u2014 "
                "the business cannot stop rivals from entering. Secondly, consumers will buy from the business that "
                "gives them the most value for money and they could therefore choose the competitor, and increased "
                "competition drives prices and profits down. Thirdly, new entrants with better products divide the "
                "market even further, reducing the business's market share, while it struggles to differentiate itself "
                "to gain a competitive advantage."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Briefly explain the interrelationship between the micro (internal), market and macro environments. (6)"
            ),
            marking_points=[
                "Businesses (the micro environment) are in constant interaction with components of the market and macro environments.",
                "The business is challenged by changes in the market and macro environments that it cannot control.",
                "Changes in the macro environment may affect the micro environment, which may then affect the market environment.",
                "Example: an increase in the interest rate raises production costs, raises prices and decreases consumer spending.",
                "Changes in the market environment may affect the micro environment, e.g. new competitors force price decreases.",
                "Businesses must ADAPT to macro challenges by formulating strategies to cope.",
            ],
            sample_answer=(
                "The three environments do not exist in isolation; businesses in the micro environment are in constant "
                "interaction with the market and macro environments and are challenged by changes they cannot control. "
                "A change in the macro environment may affect the micro environment, which in turn affects the market "
                "environment \u2014 for example an increase in the interest rate increases production costs, which raises "
                "the prices of goods and services and finally decreases consumer spending. A change in the market "
                "environment can also affect the micro environment, for instance new competitors entering the market "
                "may force the business to lower its prices. Because the macro environment has the biggest influence, "
                "businesses must adapt to its challenges by formulating strategies to cope."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Discuss the interrelationship between a business and its SUPPLIERS, and state how the business can "
                "maintain a good supplier relationship. (6)"
            ),
            marking_points=[
                "Businesses depend on suppliers for their raw materials and other inputs.",
                "Without raw materials from suppliers a business cannot produce its goods or services.",
                "Businesses must identify RELIABLE suppliers \u2014 right quality, right quantity, right price, delivered at the right time.",
                "A supply shortage is a market-environment challenge that can stop production.",
                "Maintain the relationship by paying suppliers on time / honouring commitments.",
                "Maintain the relationship by signing long-term contracts at fixed prices or buying in bulk for discounts.",
            ],
            sample_answer=(
                "A business depends on its suppliers for raw materials and other inputs, and without those inputs it "
                "simply cannot produce its goods or services. Suppliers must therefore be reliable \u2014 offering the "
                "right quality, right quantity and right price and delivering on time \u2014 because a supply shortage is "
                "a challenge in the market environment that halts production. The business maintains this relationship "
                "by honouring its commitments and paying for supplies on time, and by signing long-term contracts for "
                "raw materials at fixed prices or buying in bulk to obtain discounts."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                f"Explain how a change in the MACRO environment could specifically affect {biz} and, through it, "
                "its relationships with suppliers, competitors and consumers. (8)"
            ),
            marking_points=[
                "Identify a macro change (e.g. interest rate, exchange rate, legislation, technology, load shedding) (1)",
                "Explain the effect on the micro environment \u2014 costs, resources, functions or pricing (2)",
                "Effect on SUPPLIERS: costs rise, orders change, payment terms are strained or bulk buying increases (1)",
                "Effect on COMPETITORS: prices and market share shift; competitors hit by the same change may exit or enter (1)",
                "Effect on CONSUMERS: demand and spending fall or change; unhappy customers turn to competitors (1)",
                "State that the business cannot control the macro environment but can adapt through strategy (1)",
                "Give a practical coping strategy, e.g. PESTLE monitoring, renegotiating contracts, market research (1)",
            ],
            sample_answer=(
                "Suppose the macro environment changes because the reserve bank raises interest rates. The business "
                "cannot control this, but its micro environment is affected immediately: the cost of its overdraft and "
                "vehicle finance rises and production costs increase, so the administration and financial functions must "
                "rebudget and prices may have to rise. This ripples through the market environment. Suppliers are "
                "affected because the business may order less stock, delay payments or try to lock in long-term "
                "contracts at fixed prices to protect itself. Competitors are affected because those who can absorb the "
                "increase may keep prices low and win market share, while weaker competitors may close \u2014 which is "
                "itself an opportunity. Consumers reduce their spending because credit is more expensive and prices are "
                "higher, and unhappy or unable customers turn to a competitor, shrinking the customer base. Since the "
                "macro environment has the greatest influence and cannot be controlled, the business should scan it "
                "continuously (PESTLE), renegotiate terms with reliable suppliers, differentiate on quality rather than "
                "price alone, and use market research to stay close to changing consumer needs \u2014 thereby adapting to "
                "the challenge instead of being defeated by it."
            ),
            marks=8,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Built from the CAPS 'New Words' glossary for this topic."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Use the glossary word bank to complete the CAPS 'New Words' definitions.",
            pool=["remunerate", "consult", "devising", "legislation"],
            blanks=["1", "2", "3"],
            correct_map={"1": "remunerate", "2": "consult", "3": "devising"},
            text_parts=[
                "To ",
                " means to pay a worker what that worker receives for performing a job for the business.",
                "To ",
                " means to seek information or input from other departments.",
                "Devising", # placeholder replaced below
                " means to plan or come up with a procedure or system \u2014 for example employers consult staff when ",
                "strategies to achieve the goals of the business.",
            ],
            explanation="remunerate = to pay for a job; consult = to seek input from other departments; devising = to plan or come up with procedures/systems.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the glossary definitions with the correct terms from the word bank.",
            pool=["accessibility", "alliance", "efficient", "reliable", "bulk", "interrelated"],
            blanks=["1", "2", "3"],
            correct_map={"1": "interrelated", "2": "efficient", "3": "accessibility"},
            text_parts=[
                " ",
                " means there is a connection or relationship between the components of an environment.",
                " ",
                " means achieving maximum productivity with minimum wasted effort or expense.",
                " ",
                " means that a place or product is easily reached.",
            ],
            explanation="interrelated = a connection exists between components; efficient = maximum productivity with minimum waste; accessibility = easily reached.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the definitions of the market terms used in this topic.",
            pool=["raw materials", "goods", "services", "market research", "customer base", "supply shortage"],
            blanks=["1", "2", "3"],
            correct_map={"1": "raw materials", "2": "services", "3": "market research"},
            text_parts=[
                " ",
                " are materials that have not yet been processed by the business.",
                " ",
                " are work done by businesses which is not tangible.",
                " ",
                " is the activity of gathering information about customers' needs and preferences.",
            ],
            explanation="raw materials = unprocessed inputs; services = intangible work done by business; market research = gathering information on customer needs and preferences.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Match functions, departments and chain-reaction links (Sections 5.1\u20135.3)."""
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each micro-environment relationship with the example the CAPS document uses for it.",
            column_a=[
                "General management \u2192 administration",
                "Production \u2192 purchasing",
                "Marketing \u2192 production",
                "Human resources \u2192 other departments",
                "Employer \u2192 employee",
            ],
            column_b=[
                "Consults to obtain the information needed to run the affairs of the business",
                "Must be told the type, quality and quantity of resources to purchase",
                "Supplies feedback from customers so goods can meet consumer expectations",
                "Are consulted to determine what skills and experience are needed before recruiting",
                "Depends on workers to perform duties, and remunerates them for their services",
            ],
            correct_pairs={
                "General management \u2192 administration": "Consults to obtain the information needed to run the affairs of the business",
                "Production \u2192 purchasing": "Must be told the type, quality and quantity of resources to purchase",
                "Marketing \u2192 production": "Supplies feedback from customers so goods can meet consumer expectations",
                "Human resources \u2192 other departments": "Are consulted to determine what skills and experience are needed before recruiting",
                "Employer \u2192 employee": "Depends on workers to perform duties, and remunerates them for their services",
            },
            explanation="Section 5.1 gives these exact examples of how the functions, departments and role-players inside the micro environment depend on one another.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each chain-reaction description (Column A) with the environment relationship it shows (Column B).",
            column_a=[
                "An increase in the interest rate raises production costs",
                "New competitors entering the market force prices down",
                "Businesses form a strategic alliance to influence government legislation",
                "The public relations department keeps a positive image so customers stay loyal",
                "The marketing department conducts research to follow changing tastes",
            ],
            column_b=[
                "Macro \u2192 micro influence",
                "Market \u2192 micro influence",
                "Micro/market \u2192 macro influence (only as a group)",
                "Micro function \u2192 market consumer relationship",
                "Micro function \u2192 market consumer needs",
            ],
            correct_pairs={
                "An increase in the interest rate raises production costs": "Macro \u2192 micro influence",
                "New competitors entering the market force prices down": "Market \u2192 micro influence",
                "Businesses form a strategic alliance to influence government legislation": "Micro/market \u2192 macro influence (only as a group)",
                "The public relations department keeps a positive image so customers stay loyal": "Micro function \u2192 market consumer relationship",
                "The marketing department conducts research to follow changing tastes": "Micro function \u2192 market consumer needs",
            },
            explanation="Interest rates are macro and costs are micro; competitors are market and pricing is a micro response. A single business cannot influence legislation but an alliance can \u2014 showing the market acting back on the macro environment.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each type of intermediary or market role-player with how the business depends on it.",
            column_a=["Wholesalers", "Retailers", "Agents", "Other agents (networking)", "Public relations department"],
            column_b=[
                "Buy in bulk from the producer and sell on to retailers",
                "Sell the business's goods to the final consumers",
                "Sell the business's goods for a commission",
                "A delivery agent seeks a local agent where accessibility is restricted",
                "Maintains a positive image so that customers remain loyal",
            ],
            correct_pairs={
                "Wholesalers": "Buy in bulk from the producer and sell on to retailers",
                "Retailers": "Sell the business's goods to the final consumers",
                "Agents": "Sell the business's goods for a commission",
                "Other agents (networking)": "A delivery agent seeks a local agent where accessibility is restricted",
                "Public relations department": "Maintains a positive image so that customers remain loyal",
            },
            explanation="Section 5.2 explains that intermediaries are the link between the business and consumers, that agents network and depend on other agents, and that the PR function keeps the customer base loyal.",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """Crossword drawn from the CAPS 'New Words' glossary for this topic."""
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="Complete the crossword using the 'New Words' of this topic.",
            words=["INTERRELATED", "LEGISLATION", "CONSULT", "REMUNERATE", "DEVISING", "EFFICIENT", "RELIABLE", "ALLIANCE"],
            clues={
                "INTERRELATED": "Describes components between which a connection or relationship exists",
                "LEGISLATION": "Laws enacted or passed by the government",
                "CONSULT": "To seek information or input from other departments",
                "REMUNERATE": "To pay a worker for performing a job",
                "DEVISING": "Planning or coming up with procedures or systems",
                "EFFICIENT": "Achieving maximum productivity with minimum wasted effort",
                "RELIABLE": "Something that can be trusted or depended upon",
                "ALLIANCE": "Two or more businesses working together in a joint venture",
            },
            grid_size=15,
            explanation="All eight answers come straight from the 'New Words' glossary of the interrelationship topic.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="This crossword covers the market-environment vocabulary used in the activities.",
            words=["BULK", "SHORTAGE", "ACCESSIBILITY", "COMMISSION", "CUSTOMERBASE", "MARKETRESEARCH", "PRICINGSTRATEGIES"],
            clues={
                "BULK": "Buying raw materials in large quantities, often for a discount",
                "SHORTAGE": "A supply \u2026 is when businesses cannot find suppliers offering the right quality, quantity and place",
                "ACCESSIBILITY": "The quality of being easily reached",
                "COMMISSION": "An agent sells the goods of another business for a \u2026",
                "CUSTOMERBASE": "The group of customers a business has in the market",
                "MARKETRESEARCH": "Gathering information about customers' needs and preferences",
                "PRICINGSTRATEGIES": "Methods a business uses to set the prices of its products",
            },
            grid_size=18,
            explanation="These terms appear in the 'New Words' list and in Section 5.2 on the relationship between the business and its market components.",
            marks=7,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Extended evaluation tasks based on Activities 5.1 and Section 5.3."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                " 'All the components of the micro environment are interrelated. A change in one "
                "feature will influence all the other components.' In view of this statement, evaluate "
                f"the interrelationships within the micro environment of a business such as {biz}, and "
                "show how those internal relationships connect the business to its market environment. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Define interrelated and state that the micro, market and macro environments do not exist in isolation."},
                {"criterion": "Relationship between the functions", "marks": 4, "description": "Explain how the eight functions depend on each other, e.g. general management consults administration for information."},
                {"criterion": "Relationship between departments", "marks": 4, "description": "Use the production-purchasing and marketing-production examples, or the car-manufacturing example."},
                {"criterion": "Relationship employer-employee", "marks": 3, "description": "Explain mutual dependence, remuneration, consultation on strategy and training."},
                {"criterion": "Link to the market environment", "marks": 4, "description": "Explain the micro-market links: suppliers/inputs, intermediaries, competitors, consumers."},
                {"criterion": "Conclusion", "marks": 2, "description": "A reasoned summary stating that internal harmony is needed to respond to external change."},
            ],
            sample_answer=(
                "Interrelated means that a connection or relationship exists between components. The micro, market and macro "
                "environments do not exist in isolation, and within the micro environment the components depend on and "
                "influence one another, so a change in one feature influences all the others. The eight business functions "
                "are the first clear example. General management coordinates all the other functions efficiently and effectively "
                "to achieve the vision and mission, and it constantly seeks information and advice from departmental heads. It "
                "consults the administration function, which collects and stores the information needed to run the affairs of the "
                "business and to develop strategies. The second example is the relationship between DEPARTMENTS. The production "
                "department must inform purchasing about the type, quality and quantity of resources required, otherwise it cannot "
                "produce the goods or services. In turn, marketing feeds customer feedback back to production so that what is made "
                "meets consumer expectations. Human resources must consult the other departments to establish which skills and "
                "experience are needed before recruiting. In a car-manufacturing company, different departments produce the "
                "components that are later combined into the complete car \u2014 proof that departments depend on one another for "
                "resources and to complete the final product. The third example is the EMPLOYER-EMPLOYEE relationship. The employer "
                "depends on employees to perform duties and responsibilities and must remunerate them for their services, while "
                "employees depend on the employer for income. Employers also consult employees when devising strategies to achieve "
                "the goals of the business, and some provide education and training to improve staff skills. These internal "
                "relationships then connect the business outward to its MARKET environment. The purchasing function depends on "
                "suppliers for raw materials \u2014 without them production stops \u2014 so the business must identify reliable suppliers "
                "and maintain the relationship by paying on time and signing long-term contracts at fixed prices. Intermediaries "
                "act as the link to consumers, competitors force the business to study pricing strategies, and the marketing and "
                "public relations functions must conduct market research and protect the image of the business so that the customer "
                "base remains loyal. In conclusion, because the internal components are so interdependent, poor performance by one "
                "department spreads through the whole business and weakens its position in the market. A business that keeps its "
                "micro environment harmonised is far better placed to absorb the changes that come from the market and macro "
                "environments, which it cannot control but must adapt to."
            ),
            marks=20,
            min_words=250,
            max_words=450,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                " 'Businesses have very little control over the macro environment, but the macro environment has the "
                "biggest influence over them.' Discuss, with reference to the relationship between the micro, market "
                "and macro environments, and evaluate the strategies a business can use to respond. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "State that the macro environment has the biggest control and influence over the market and micro environments and that a single business has no control over it."},
                {"criterion": "The chain reaction", "marks": 5, "description": "Explain and illustrate the macro \u2192 micro \u2192 market chain (interest rate \u2192 production cost \u2192 consumer demand)."},
                {"criterion": "Market \u2192 micro influence", "marks": 4, "description": "Explain the reverse influence, e.g. new competitors forcing price decreases."},
                {"criterion": "Influence BACK on the macro environment", "marks": 4, "description": "A single business cannot change legislation, but a strategic alliance of businesses can influence it."},
                {"criterion": "Strategies and conclusion", "marks": 4, "description": "Practical responses (environmental scanning/PESTLE, adapting pricing, market research, alliances) with a reasoned judgement."},
            ],
            sample_answer=(
                "The micro, market and macro environments are interrelated, but they are not equally powerful. The CAPS document "
                "states that the macro environment has the biggest control and influence over both the market and micro "
                "environments, while the market and micro environments have very little control over the macro environment and "
                "can only adapt to its challenges. The chain reaction is the clearest illustration. An increase in the rate of "
                "interest is a macro-environment change. Because loans and vehicle finance become more expensive, the cost of "
                "production in the micro environment rises. The business then raises the price of its goods or services, which "
                "reduces consumer demand in the market environment \u2014 exactly the sequence shown in the CAPS diagram of "
                "'increase in interest rate \u2192 increase in production costs \u2192 decrease in customers' demand'. The same logic "
                "applies to the exchange rate: when the rand depreciates, a business that buys machinery in the USA, like Zipho's "
                "window-cleaning company, can afford only one machine instead of several, which limits its capacity to service jobs. "
                "Influence also runs from the market into the micro environment. New competitors entering the market might force a "
                "business to decrease its prices, which reduces revenue and therefore constrains the purchasing, production and human "
                "resources functions. Increased competition lowers prices and profits, so businesses that offer the best quality at "
                "the right price attract and keep loyal customers. There is, however, one route by which businesses can act back on "
                "the macro environment: collective action. A single business has no control over government legislation, but if "
                "businesses come together to form a strategic alliance, combining resources and sharing expertise, they can "
                "influence certain aspects of that legislation. Because intermediaries are also customers, and because agents depend "
                "on other agents where accessibility is restricted, maintaining these relationships is itself a defence. To respond, "
                "the business should continuously scan the environment using tools such as PESTLE and SWOT, so that macro changes are "
                "foreseen rather than reacted to late. It should lock in reliable suppliers through long-term contracts at fixed "
                "prices, budget for higher interest costs, differentiate on quality instead of competing on price alone, conduct "
                "market research so changing consumer needs are met, and use the public relations function to protect customer "
                "loyalty. In conclusion, the statement is valid: the macro environment dominates and cannot be controlled by an "
                "individual business. But the business is not helpless \u2014 because the environments are interrelated, adapting "
                "quickly in the micro environment converts many macro threats into manageable change, and acting collectively "
                "gives business at least some influence over the macro environment it otherwise cannot touch."
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


generate_interrelationship = build_generate(_pools)
