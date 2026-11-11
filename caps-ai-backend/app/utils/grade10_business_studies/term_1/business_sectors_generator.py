"""Grade 10 Business Studies - Term 1 - Topic 5: Business sectors.

Deterministic generator (no LLM). Content hand-authored from the CAPS notes, the
'New words' glossary, Activities 6.1-6.3 and the informal-sector case study in
``curriculum_docs_auto/BusinessStudies_Gr10/Term 1/05. Business sectors.md``.

All six archetypes are covered:
    concepts    -> mcq (primary/secondary/tertiary, formal/informal, public/private)
    application -> scenario mcq + typed (classify a business, trace the economic chain)
    discussion  -> typed (explain relationships, differences and importance, with memos)
    word_bank   -> the CAPS 'New words' glossary definitions
    matching    -> sector to example, term to meaning
    crossword   -> sector vocabulary (GDP, SOE, PPP, parastatal, privatisation)
    essay       -> extended sector-analysis answers with model answers
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
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An INDUSTRY, as distinguished from a sector in this topic, refers to \u2026",
            options=[
                "a specific group of businesses that produce a particular kind of good or service in a particular field",
                "all businesses in the country that pay tax",
                "businesses owned by the government",
                "sole traders only",
            ],
            correct_index=0,
            explanation="Although 'sector' and 'industry' are used interchangeably, an industry is a specific group of businesses producing a particular good/service in a field \u2014 e.g. the tourism industry.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The secondary sector is often referred to as \u2026 because valuable products are created for consumers.",
            options=["the service industry", "manufacturing industries", "the primary industry", "the retail sector"],
            correct_index=1,
            explanation="The secondary sector is often called manufacturing industries because raw materials are converted into valuable products.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which sector is also known as the SERVICE industry?",
            options=["Primary", "Secondary", "Tertiary", "Informal"],
            correct_index=2,
            explanation="The tertiary sector offers services to businesses and consumers and is also known as the service industry.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses in the informal sector are mostly started by \u2026",
            options=[
                "unemployed people who need to earn an income to buy necessities",
                "multinational corporations",
                "state-owned enterprises",
                "banks and insurance companies",
            ],
            correct_index=0,
            explanation="The informal sector consists of small businesses started mainly by unemployed people who need an income to buy necessities such as water and electricity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses in the formal sector are required to register with \u2026 and be liable for tax with \u2026",
            options=[
                "the CIPC; SARS",
                "SARS; the CIPC only",
                "Eskom; Transnet",
                "the SABC; the IDB",
            ],
            correct_index=0,
            explanation="Formal-sector businesses register with the Companies and Intellectual Property Commission (CIPC) and register with the South African Revenue Service (SARS), paying tax on turnover and profits at the prescribed threshold.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A MIXED ECONOMY is an economy that \u2026",
            options=[
                "consists of both private and state-owned companies sharing control of owning, making, selling and exchanging goods",
                "has only government-owned businesses",
                "has no taxation",
                "relies only on the primary sector",
            ],
            correct_index=0,
            explanation="The glossary defines a mixed economy as one consisting of both private and state-owned companies that share control of owning, making, selling and exchanging goods.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A PARASTATAL is \u2026",
            options=[
                "a state-owned company/enterprise (SOC/SOE)",
                "a private company listed on the JSE",
                "a non-profit organisation",
                "a street-vending business",
            ],
            correct_index=0,
            explanation="The glossary defines a parastatal as a state-owned company or enterprise (SOC/SOE) owned and controlled by the government.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="PRIVATISATION means \u2026",
            options=[
                "the sale of state-owned businesses and assets to the private sector",
                "the government taking over a private company",
                "paying tax on profits",
                "registering a business with the CIPC",
            ],
            correct_index=0,
            explanation="The glossary defines privatisation as the sale of state-owned businesses and assets to the private sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A PUBLIC-PRIVATE PARTNERSHIP (PPP) is \u2026",
            options=[
                "a contract between a public-sector institution and the private sector, where the private sector performs a function usually provided by the public sector or uses state property",
                "a partnership between two sole traders",
                "an agreement between two unions",
                "a business owned entirely by foreign investors",
            ],
            correct_index=0,
            explanation="This is the glossary definition of a PPP.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="GROSS DOMESTIC PRODUCT (GDP) is \u2026",
            options=[
                "a measurement that captures a country's economic output",
                "the total taxes collected by SARS",
                "the value of a company's shares",
                "the number of people employed by government",
            ],
            correct_index=0,
            explanation="The glossary defines GDP as a measurement that captures a country's economic output.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Employees in the formal sector are protected by legislation such as \u2026",
            options=["BCEA, COIDA and UIF", "the CPA only", "municipal by-laws", "the Water Act"],
            correct_index=0,
            explanation="Formal-sector employees are protected by legislation such as the BCEA, COIDA and UIF; informal-sector employees are not protected and can easily be exploited.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which ONE is a given example of a business in the INFORMAL sector?",
            options=["A spaza shop", "A commercial bank", "Eskom", "A car-manufacturing factory"],
            correct_index=0,
            explanation="The CAPS examples of the informal sector are food and flea markets, street vendors and spaza shops. Banks, Eskom and factories are formal-sector businesses.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="CORPORATE SOCIAL RESPONSIBILITY (CSR) is a function MOST associated with \u2026",
            options=[
                "the private sector giving back by uplifting the community",
                "the public sector providing water and electricity",
                "sole traders avoiding tax",
                "the primary sector extracting minerals",
            ],
            correct_index=0,
            explanation="The private sector gives back by uplifting the community through CSR programmes; CSR relates to businesses taking responsibility for their impact on society and the environment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="According to the case study, the policy goal for the informal sector in the short to medium term should be to \u2026",
            options=[
                "shrink and eliminate it",
                "grow and strengthen it, creating more viable self-reliant enterprises",
                "register all spaza shops with SARS immediately",
                "replace it with state-owned enterprises",
            ],
            correct_index=1,
            explanation="The adapted case study states the goal should NOT be to shrink or eliminate the informal sector, but to grow and strengthen it into a larger, more dynamic sector with better-quality employment.",
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


def _application(r) -> List[Callable[[], Dict[str, Any]]]:
    """Classify real businesses into sectors and trace the economic chain of production."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Sasko Bakery processes wheat grains from a farm into flour and bakes bread. Sasko operates in the \u2026",
            options=["primary sector", "secondary sector", "tertiary sector", "informal sector"],
            correct_index=1,
            explanation="Sasko TRANSFORMS raw materials into products, which is the defining activity of the secondary (manufacturing) sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Shoprite buys baked bread from Sasko and sells it to consumers. Shoprite operates in the \u2026",
            options=["tertiary sector", "primary sector", "secondary sector", "public sector"],
            correct_index=0,
            explanation="Retailers sell goods and offer services to consumers, placing them in the tertiary (service) sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A fisherman in Port Nolloth catches fish that are later canned by a factory. The fisherman's business is in the \u2026",
            options=["primary sector", "secondary sector", "tertiary sector", "informal sector only"],
            correct_index=0,
            explanation="The primary sector extracts, collects or cultivates raw materials and natural resources; fishing is one of its four given examples (agriculture, fishing, forestry, mining).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Eskom supplies electricity to the country and is owned and controlled by the government. Eskom is part of the \u2026",
            options=[
                "private sector, tertiary sector",
                "public sector, and it is a state-owned enterprise (parastatal)",
                "informal sector",
                "primary sector",
            ],
            correct_index=1,
            explanation="Eskom is given as an example of the public sector \u2014 a state-owned company/enterprise (SOC/SOE) also called a parastatal.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Mama Nkosi runs an unregistered spaza shop from her house, works long hours and earns an irregular income. Her business belongs to the \u2026",
            options=["formal sector", "informal sector", "public sector", "secondary sector"],
            correct_index=1,
            explanation="Spaza shops are unregistered with the CIPC, pay no tax on profits and have long hours and irregular income \u2014 the CAPS characteristics of the informal sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "The government sells a loss-making state-owned logistics company to a private group of investors. "
                "This transaction is an example of \u2026"
            ),
            options=["a public-private partnership", "privatisation", "corporatisation", "a joint venture"],
            correct_index=1,
            explanation="Privatisation is the sale of state-owned businesses and assets to the private sector (glossary definition).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                "A mining company (primary) uses drilling machinery made in a factory (secondary) and insurance and "
                "transport services provided by firms in the tertiary sector. This BEST shows that \u2026"
            ),
            options=[
                "the relationship between the three sectors is not a linear one",
                "the primary sector has no need of the other sectors",
                "only the tertiary sector creates value",
                "sectors must be classified by the size of the business",
            ],
            correct_index=0,
            explanation="The CAPS document stresses that the relationship is NOT linear: the primary sector also depends on the secondary for machinery and on the tertiary for services such as insurance and transport.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt=(
                f"{biz} is registered with the CIPC, pays PAYE and VAT to SARS and its employees are covered by the BCEA. "
                "Which statement is TRUE about this business?"
            ),
            options=[
                "Its activities are recorded in the GDP of the country",
                "It operates in the informal sector",
                "Its employees are not protected by legislation",
                "Its contribution to the economy is difficult to calculate",
            ],
            correct_index=0,
            explanation="All contributions of formal-sector businesses are recorded in the GDP; they pay tax, are monitored by government and their employees are protected. The other options describe the informal sector.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which ONE of the following is a purpose of the PUBLIC sector rather than the private sector?",
            options=[
                "Ensuring an equal distribution of wealth among the rich and the poor",
                "Generating profit for shareholders",
                "Building wealth for business growth",
                "Meeting consumer demand for a wide variety of goods",
            ],
            correct_index=0,
            explanation="Improving the general standard of living and ensuring the equal distribution of wealth are given as purposes of the public sector; profit-making and wealth creation are private-sector purposes.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A private toll-road company builds and operates a highway on behalf of the government using state property. This arrangement is a \u2026",
            options=["parastatal", "public-private partnership (PPP)", "privatisation", "multinational corporation"],
            correct_index=1,
            explanation="A PPP is a contract between a public-sector institution and the private sector, where the private sector performs a function usually provided by the public sector and/or uses state property.",
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Trace the product BREAD through the three business sectors, from the farm to the consumer, "
                "and state the role of each sector. (6)"
            ),
            marking_points=[
                "PRIMARY sector: wheat needed for bread is grown on a farm (extraction/cultivation of raw materials).",
                "The farm sells the wheat grains to a bread company, for example Sasko Bakery.",
                "SECONDARY sector: Sasko processes the wheat into flour at a mill and uses the flour to produce bread (manufacturing/transforming).",
                "The bread is packaged and sold to retailers, for example Shoprite/Checkers and Pick 'n Pay.",
                "TERTIARY sector: the bread is transported to retailers who sell it to consumers (services supporting distribution and sale).",
                "State that the sectors work together to create an economic chain of production.",
            ],
            sample_answer=(
                "In the PRIMARY sector the wheat needed for bread is grown on a farm, and the farm sells the wheat grains "
                "to a bread company such as Sasko Bakery. In the SECONDARY sector Sasko Bakery processes the wheat into "
                "flour at the flour mill, and the flour is used to produce the bread, which is then packaged. In the "
                "TERTIARY sector the bread is transported to retailers such as Shoprite/Checkers and Pick 'n Pay, and the "
                "retailers sell the bread to consumers. Together the three sectors work as an economic chain of production, "
                "each depending on the others."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Classify EACH of the following businesses into the correct sector (primary, secondary or tertiary) "
                "AND into formal or informal. Give a reason for each. (8)\n"
                "(a) Merries Gold Mine  (b) a street vendor selling fruit in East London  "
                "(c) a vehicle-assembly factory in Pretoria  (d) a registered hair salon paying VAT to SARS"
            ),
            marking_points=[
                "(a) PRIMARY \u2014 it extracts a natural resource (gold).",
                "(a) FORMAL \u2014 a registered mine pays tax and is monitored by government.",
                "(b) TERTIARY (selling goods/services) \u2014 informal \u2014 street vendors are unregistered, do not pay tax and earn an irregular income.",
                "(c) SECONDARY \u2014 it transforms raw materials into finished products (manufacturing).",
                "(c) FORMAL \u2014 a factory is registered with the CIPC and SARS.",
                "(d) TERTIARY \u2014 a hair salon offers a service, not a manufactured good.",
                "(d) FORMAL \u2014 paying VAT to SARS shows registration and tax liability.",
                "Each answer must give BOTH the classification AND a reason.",
            ],
            sample_answer=(
                "(a) Merries Gold Mine is PRIMARY because it extracts a natural resource, and FORMAL because registered "
                "mines are given as formal-sector examples that pay tax. (b) The fruit street vendor is TERTIARY because "
                "the business sells goods and offers a service, and INFORMAL because street vendors are not registered "
                "with the CIPC, pay no tax on profits and earn an irregular income. (c) The vehicle-assembly factory is "
                "SECONDARY because it transforms raw materials into finished products, and FORMAL because it is registered "
                "with the CIPC and SARS. (d) The hair salon is TERTIARY because it provides a service rather than a "
                "manufactured good, and FORMAL because it is registered and pays VAT to SARS, so its employees are also "
                "protected by legislation."
            ),
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "The case study states that almost 80% of informal enterprises are one-person firms and that working "
                "hours are long while returns are very low. Despite this, advise the government why the informal "
                "sector should be GROWN and STRENGTHENED rather than eliminated. (6)"
            ),
            marking_points=[
                "It is a significant component of the economy providing employment, livelihoods and income for millions of workers and business owners.",
                "About one in six working South Africans (\u00b117% of total employment) works in the informal sector.",
                "The National Development Plan projects that the sector could generate almost two million new jobs by 2030.",
                "It absorbs unemployed people who need an income to buy necessities, reducing poverty.",
                "It offers paid jobs \u2014 the case study notes \u00b150 000 paid jobs, nearly double direct employment in formal mining.",
                "Recommendation: support rather than eliminate it, e.g. through skills development, access to finance, safe trading spaces and simplified registration so enterprises become viable and self-reliant.",
            ],
            sample_answer=(
                "The informal sector should be grown and strengthened rather than eliminated. It is a significant component "
                "of the economy that provides employment, livelihoods and income for millions of workers and business owners. "
                "About one in every six South Africans who work (roughly 17% of total employment) works in this sector, and in "
                "the National Development Plan it is projected to generate almost two million new jobs by 2030. It also absorbs "
                "people who are unemployed and who need an income to buy necessities such as water and electricity, so it "
                "reduces poverty. Although most enterprises are one-person firms with long hours, difficult conditions and very "
                "low returns, the sector still provided about 850 000 paid jobs \u2014 almost double the direct employment of the "
                "formal mining sector. Government should therefore help enterprises become more viable by providing skills "
                "training, affordable finance, safe trading spaces and a simple, low-cost route to registration so that "
                "informal businesses can grow, create better-quality employment and eventually move into the formal sector."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt=(
                "Explain how the PUBLIC and PRIVATE sectors depend on each other in South Africa's mixed economy. (6)"
            ),
            marking_points=[
                "South Africa has a MIXED economy: most businesses are privately owned and some are state-owned.",
                "The public sector provides infrastructure that supports private-sector development.",
                "The public sector provides public goods and services such as water and electricity to meet people's needs.",
                "The private sector provides jobs, a variety of goods and services and contributes to tax revenue.",
                "The private sector supports the public sector through public-private partnership (PPP) agreements.",
                "The private sector gives back through CSR, while the public sector improves living standards and distributes wealth.",
            ],
            sample_answer=(
                "South Africa has a mixed economy consisting of both private and state-owned companies that share control of "
                "owning, making, selling and exchanging goods. The two sectors depend on each other. The public sector provides "
                "public goods and services such as water and electricity, improves the general standard of living, ensures a "
                "more equal distribution of wealth and, importantly, provides the infrastructure (roads, ports, power) that "
                "supports private-sector development. The private sector in turn supplies a large variety of goods and services "
                "to consumers, creates jobs for skilled, semi-skilled and unskilled labour, creates wealth and contributes tax "
                "revenue that government uses to fund public services. The private sector also supports the public sector "
                "through public-private partnership agreements where it performs functions normally provided by the state, and "
                "it gives back to communities through corporate social responsibility programmes. Neither sector can meet "
                "people's needs on its own."
            ),
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _wordbank(r) -> List[Callable[[], Dict[str, Any]]]:
    """Definitions from the CAPS 'Key concepts' and 'New words' lists."""
    return [
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the definitions of the three business sectors using the word bank.",
            pool=["primary", "secondary", "tertiary", "manufacturing", "services", "raw materials"],
            blanks=["1", "2", "3"],
            correct_map={"1": "primary", "2": "secondary", "3": "tertiary"},
            text_parts=[
                "The ",
                " sector deals with the extraction of raw materials and natural resources, such as agriculture, fishing, forestry and mining.",
                "The ",
                " sector transforms raw materials into finished or semi-finished products and is often referred to as manufacturing industries.",
                "The ",
                " sector offers services to other businesses and consumers and is also known as the service industry.",
            ],
            explanation="Primary extracts raw materials; secondary manufactures/transforms them; tertiary provides services.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Complete the statements about the formal and informal sectors.",
            pool=["CIPC", "SARS", "registered", "tax", "irregular", "self-employed"],
            blanks=["1", "2", "3"],
            correct_map={"1": "registered", "2": "CIPC", "3": "tax"},
            text_parts=[
                "Businesses in the formal sector are ",
                " businesses that must register with the Companies and Intellectual Property Commission, known as the ",
                ", and register with SARS to pay ",
                " on their turnover and profits at a prescribed threshold.",
            ],
            explanation="Formal businesses are registered, must register with the CIPC and must pay tax to SARS at the prescribed threshold.",
            marks=3,
            visual_aid_key=VAID,
        ),
        lambda: make_wordbank(
            prefix=PREFIX,
            prompt="Use the glossary word bank to complete the sector terms.",
            pool=["parastatal", "privatisation", "mixed economy", "GDP", "PPP", "CSR"],
            blanks=["1", "2", "3"],
            correct_map={"1": "parastatal", "2": "privatisation", "3": "mixed economy"},
            text_parts=[
                "A ",
                " is a state-owned company or enterprise (SOC/SOE) owned and controlled by the government.",
                " ",
                " refers to the sale of state-owned businesses and assets to the private sector.",
                "A ",
                " consists of both private and state-owned companies that share control of owning, making, selling and exchanging goods in the country.",
            ],
            explanation="A parastatal is a state-owned enterprise; privatisation is selling state assets to the private sector; a mixed economy combines both.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _matching(r) -> List[Callable[[], Dict[str, Any]]]:
    """Match sectors, examples and glossary terms."""
    return [
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each business with the sector it operates in.",
            column_a=["A coal mine in Mpumalanga", "A bread factory in Durban", "A tourism agency in Cape Town", "A timber plantation in the Eastern Cape", "A commercial bank in Sandton"],
            column_b=[
                "Primary sector \u2014 extracts mineral raw materials from the earth",
                "Secondary sector \u2014 manufactures food products from raw materials",
                "Tertiary sector \u2014 provides hospitality and travel services",
                "Primary sector \u2014 cultivates natural resources (forestry)",
                "Tertiary sector \u2014 provides financial services to businesses and consumers",
            ],
            correct_pairs={
                "A coal mine in Mpumalanga": "Primary sector \u2014 extracts mineral raw materials from the earth",
                "A bread factory in Durban": "Secondary sector \u2014 manufactures food products from raw materials",
                "A tourism agency in Cape Town": "Tertiary sector \u2014 provides hospitality and travel services",
                "A timber plantation in the Eastern Cape": "Primary sector \u2014 cultivates natural resources (forestry)",
                "A commercial bank in Sandton": "Tertiary sector \u2014 provides financial services to businesses and consumers",
            },
            explanation="Mining and forestry are primary because they extract or cultivate natural resources; a bakery is secondary because it transforms raw materials; tourism and banking are tertiary because they offer services. A bank is a SERVICE business, so it is tertiary \u2014 learners often mis-classify it as secondary.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_matching(
            prefix=PREFIX,
            prompt="Match each description in Column A with the correct term in Column B.",
            column_a=["Informal sector", "Public sector", "Private sector", "Formal sector", "Corporate social responsibility"],
            column_b=[
                "Businesses owned, financed and run by private individuals, mainly aiming to make a profit",
                "Small businesses not registered with the CIPC that do not pay tax on profits",
                "Businesses that take responsibility for their impact on society and the environment",
                "Registered businesses that pay tax to SARS and are monitored by government",
                "Enterprises owned and managed by government, providing public goods and services",
            ],
            correct_pairs={
                "Informal sector": "Small businesses not registered with the CIPC that do not pay tax on profits",
                "Public sector": "Enterprises owned and managed by government, providing public goods and services",
                "Private sector": "Businesses owned, financed and run by private individuals, mainly aiming to make a profit",
                "Formal sector": "Registered businesses that pay tax to SARS and are monitored by government",
                "Corporate social responsibility": "Businesses that take responsibility for their impact on society and the environment",
            },
            explanation="These are the CAPS definitions of the formal/informal and public/private classifications.",
            marks=5,
            visual_aid_key=VAID,
        ),
    ]


def _crossword(r) -> List[Callable[[], Dict[str, Any]]]:
    """Crossword from the CAPS 'New words' glossary for this topic."""
    return [
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="Complete the crossword using the sector and economy terms of this topic.",
            words=["PRIMARY", "SECONDARY", "TERTIARY", "PARASTATAL", "PRIVATISATION", "INDUSTRY", "SELFEMPLOYED"],
            clues={
                "PRIMARY": "Sector that extracts or cultivates raw materials such as coal, fish and timber",
                "SECONDARY": "Sector that transforms raw materials into finished or semi-finished products",
                "TERTIARY": "Sector that offers services to businesses and consumers",
                "PARASTATAL": "A state-owned company or enterprise owned and controlled by government",
                "PRIVATISATION": "The sale of state-owned businesses and assets to the private sector",
                "INDUSTRY": "A specific group of businesses producing a particular kind of good or service",
                "SELFEMPLOYED": "People working for themselves \u2014 typical of the informal sector",
            },
            grid_size=15,
            explanation="These are the sector classifications and glossary terms of the topic; primary extracts, secondary manufactures, tertiary serves.",
            marks=7,
            visual_aid_key=VAID,
        ),
        lambda: make_crossword(
            prefix=PREFIX,
            prompt="This crossword covers the abbreviations and economic terms used in the business sectors.",
            words=["GDP", "CIPC", "SARS", "CSR", "PPP", "SOE", "MIXED"],
            clues={
                "GDP": "A measurement that captures a country's economic output (abbreviation)",
                "CIPC": "The body with which formal businesses must register (abbreviation)",
                "SARS": "The authority to which formal businesses pay tax (abbreviation)",
                "CSR": "Corporate social \u2026 \u2014 business responsibility for its impact on society",
                "PPP": "A contract between the public and private sectors (abbreviation)",
                "SOE": "State-owned \u2026 \u2014 an enterprise owned by government (abbreviation)",
                "MIXED": "The \u2026 economy of South Africa, combining private and state-owned companies",
            },
            grid_size=12,
            explanation="Formal businesses register with the CIPC and pay tax to SARS; their contribution is captured in the GDP. South Africa's economy is a mixed economy made up of SOEs and private firms.",
            marks=7,
            visual_aid_key=VAID,
        ),
    ]


def _essay(r) -> List[Callable[[], Dict[str, Any]]]:
    """Extended responses on the relationship and importance of the sectors."""
    s = pick_scenario(r)
    biz = s["business"]
    return [
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                " 'The three business sectors do not work in isolation; they form an economic chain of "
                "production, but their relationship is not a linear one.' Discuss the meaning of each "
                "sector, trace a product through the chain, and evaluate how the sectors depend on each "
                "other. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "Explain that businesses are grouped into primary, secondary and tertiary sectors according to the nature of their product, and state the purpose of the classification."},
                {"criterion": "Meaning and examples of each sector", "marks": 6, "description": "Define primary, secondary and tertiary and give correct examples of each."},
                {"criterion": "The chain of production", "marks": 5, "description": "Trace a product (e.g. bread, or iron ore to steel) through the three sectors."},
                {"criterion": "Non-linear dependence", "marks": 4, "description": "Show how the primary sector also needs machinery from the secondary and services from the tertiary."},
                {"criterion": "Conclusion", "marks": 2, "description": "A reasoned summary of the contribution of the sectors to the economy."},
            ],
            sample_answer=(
                f"Business sectors consist of businesses that are grouped together and classified into primary, secondary or "
                "tertiary sectors according to the nature of their product or service. The purpose of the classification is to "
                "determine the contribution of each sector and industry to the South African economy. The PRIMARY sector deals "
                "with the extraction, collection or cultivation of raw materials and natural resources such as livestock, fish, "
                "timber, coal and gold; examples are agriculture, fishing, forestry and mining. The SECONDARY sector transforms "
                "those raw materials into finished or semi-finished products, which is why it is often called manufacturing "
                "industries; examples are construction, factories, manufacturing and electricity generation. It plays a critical "
                "role because not all resources are useful in their natural state and require further processing. The TERTIARY "
                "sector offers services to other businesses and consumers and is therefore also called the service industry; "
                "examples are financing, hospitality, retailers and wholesalers, storage, tourism and transportation. These "
                "sectors work together in an economic chain of production. Bread illustrates this clearly: in the primary sector "
                "wheat is grown on a farm, which sells the wheat grains to a bread company such as Sasko Bakery; in the secondary "
                "sector Sasko processes the wheat into flour at a flour mill and uses the flour to produce bread, which is then "
                "packaged; in the tertiary sector the bread is transported to retailers such as Shoprite/Checkers and Pick 'n Pay "
                "and sold to consumers. The same pattern applies to iron ore: the primary sector extracts the ore and supplies the "
                "secondary sector, which transforms it into steel and sells it to retailers in the tertiary sector, who sell it to "
                "the consumer. However, the relationship is NOT linear. The primary sector depends on the secondary sector for "
                "manufactured goods such as the drilling machinery used in mining, and both the primary and secondary sectors "
                "depend on the tertiary sector for services such as insurance and transport. This means that if one sector is "
                "disrupted, the whole chain suffers \u2014 a decline in mining reduces factory output and transport demand. In "
                "conclusion, the three sectors are interdependent and together determine the country's gross domestic product. "
                f"A business such as {biz} must therefore understand where it sits in the chain, because its suppliers, "
                "its customers and its service providers are spread across all three sectors."
            ),
            marks=20,
            min_words=250,
            max_words=450,
            visual_aid_key=VAID,
        ),
        lambda: make_essay(
            prefix=PREFIX,
            prompt=(
                "Distinguish between the formal and the informal sector, and between the public and the private "
                "sector. Then advise the government why the informal sector should be taken seriously and "
                "supported rather than eliminated. (20)"
            ),
            rubric=[
                {"criterion": "Introduction", "marks": 3, "description": "State that South African businesses are classified by registration/tax status and by ownership, and outline the four categories."},
                {"criterion": "Formal versus informal", "marks": 5, "description": "At least four clear differences: CIPC/SARS registration, tax, monitoring, protection of employees, GDP recording, examples."},
                {"criterion": "Public versus private", "marks": 5, "description": "Distinguish ownership, control, purpose and give examples of each (Eskom/Transnet; banks/hotels/retailers)."},
                {"criterion": "Importance of the informal sector", "marks": 5, "description": "Use the case study: employment, livelihoods, \u00b17% of employment, NDP projection, paid jobs compared with formal mining."},
                {"criterion": "Recommendations and conclusion", "marks": 2, "description": "Practical support measures and a reasoned final judgement."},
            ],
            sample_answer=(
                "Businesses operating in South Africa are divided into the formal and informal sectors, and separately into the "
                "public and private sectors. The FORMAL sector consists of registered businesses that pay taxes to the government. "
                "They must register with the Companies and Intellectual Property Commission (CIPC) and with the South African "
                "Revenue Service (SARS), and are liable to pay tax on turnover and profits at a prescribed threshold. Formal-sector "
                "activities are monitored by government, controlled by laws and regulations, and all their contributions are "
                "recorded in the GDP. Employees are protected by legislation such as the BCEA, COIDA and UIF, and they earn a "
                "regular weekly or monthly income. It consists of small, micro, medium and large businesses such as mines, farms, "
                "manufacturers, construction firms, retailers, banks and insurance companies. The INFORMAL sector, by contrast, "
                "consists of businesses that are NOT registered with the CIPC and do NOT pay tax on their profits. Government laws "
                "and regulations relating to businesses do not apply to them, they are not monitored, and their contribution to GDP "
                "is difficult to calculate. They are generally small, home-based operations with long working hours, difficult "
                "working conditions and irregular income, and their employees are not protected and can easily be exploited. "
                "Examples are spaza shops, street vendors, food and flea markets, hairdressers, gardening services and car washes. "
                "The PUBLIC/PRIVATE classification is different: it is about OWNERSHIP. The public sector comprises businesses "
                "owned, managed and controlled by government at all three levels \u2014 state-owned companies or enterprises (SOCs/SOEs), "
                "also called parastatals, such as Eskom, Denel, the SABC, South African Airways and Transnet. Its purpose is not "
                "profit but to provide public goods and services such as water and electricity, improve the general standard of "
                "living, ensure a more equal distribution of wealth, provide infrastructure that supports private-sector "
                "development and create job opportunities. The private sector consists of businesses owned, financed and run by "
                "private individuals \u2014 sole traders, partnerships, close corporations and profit companies \u2014 whose main aim is to "
                "make a profit. Some private businesses operate in the formal sector and some in the informal sector. Examples are "
                "banks, hotels, insurance companies, restaurants and retailers. The private sector creates wealth, offers a wide "
                "variety of goods and services, provides jobs, contributes tax revenue, supports the public sector through "
                "public-private partnership (PPP) agreements and gives back through corporate social responsibility (CSR). "
                "Although these distinctions exist, the informal sector should be taken seriously rather than eliminated. It is a "
                "significant component of the economy providing employment, livelihoods and income for millions of workers and "
                "owners. About 17% of total employment \u2014 roughly one in every six South Africans who work \u2014 is in the informal "
                "sector, and the National Development Plan projects that the sector, together with domestic work, could generate "
                "almost two million new jobs by 2030. Almost 80% of the \u00b71,4 million informal enterprises are one-person firms, yet "
                "about 1,1 million people work in enterprises that have employees, and in 2013 these firms provided about 850 000 "
                "paid jobs \u2014 almost double the \u00b7450 000 direct jobs in formal mining. Most employing enterprises are in "
                "construction, retail trade and services. With unemployment remaining high, the policy goal in the short to medium "
                "term should not be to shrink or eliminate the sector but to grow and strengthen it, so that it becomes larger and "
                "more dynamic with more viable, self-reliant enterprises and better-quality employment. Government can do this by "
                "providing training and business skills, affordable finance and savings schemes, safe serviced trading spaces, "
                "local procurement opportunities, and a simplified, low-cost registration route that gives an incentive to move "
                "into the formal sector rather than punishing those who cannot afford to. In conclusion, the four classifications "
                "answer different questions \u2014 formal/informal asks about registration and tax, public/private asks about ownership "
                "\u2014 and a realistic economic policy recognises that all four contribute to the country's output and employment."
            ),
            marks=20,
            min_words=300,
            max_words=500,
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


generate_business_sectors = build_generate(_pools)
