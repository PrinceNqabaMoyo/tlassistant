"""Grade 10 Business Studies - Term 3 - Topic 13: Business opportunities and
related factors.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_bizopp"
VAID = "business_opportunities"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An idea for a person to start a business so they can generate an income is a …",
            options=["business opportunity", "research protocol", "SWOT analysis", "questionnaire"],
            correct_index=0,
            explanation="A business opportunity is an idea for starting a business to generate income.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A strategic planning technique used to find strengths, weaknesses, opportunities and threats is a …",
            options=["SWOT analysis", "Force Field Analysis", "research protocol", "mind map"],
            correct_index=0,
            explanation="A SWOT analysis identifies strengths, weaknesses, opportunities and threats.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In a SWOT analysis, Strengths and Weaknesses relate to … factors.",
            options=["internal", "external", "political", "global"],
            correct_index=0,
            explanation="Strengths and weaknesses are internal factors under the control of the business.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="In a SWOT analysis, Opportunities and Threats relate to … factors.",
            options=["internal", "external", "financial", "personal"],
            correct_index=1,
            explanation="Opportunities and threats are external factors over which the business has little or no control.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A research instrument consisting of a set of questions to collect information from a respondent is a …",
            options=["questionnaire", "SWOT analysis", "protocol", "prospectus"],
            correct_index=0,
            explanation="A questionnaire is a research instrument made up of a set of questions for respondents.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A person who takes part in research is called a …",
            options=["respondent", "director", "supplier", "shareholder"],
            correct_index=0,
            explanation="A respondent is a person who takes part in research.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The systematic gathering, recording and analysing of data about marketing of goods and services is …",
            options=["market research", "auditing", "budgeting", "SWOT analysis"],
            correct_index=0,
            explanation="Market research is the systematic gathering, recording and analysing of marketing data.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Market research conducted by a person within the company is … market research.",
            options=["internal", "external", "primary", "secondary"],
            correct_index=0,
            explanation="Internal market research is usually conducted by a person within the company.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Market research conducted by an outside specialist is … market research.",
            options=["internal", "external", "informal", "casual"],
            correct_index=1,
            explanation="External market research is usually conducted by an outside specialist.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A plan with detailed guidelines that explain the rules of the research is a research …",
            options=["protocol", "instrument", "sample", "respondent"],
            correct_index=0,
            explanation="A research protocol is a plan with detailed guidelines explaining the rules of the research.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which is an advantage of internal market research?",
            options=["Lower research costs", "Zero bias", "Niche expertise", "Objective results"],
            correct_index=0,
            explanation="Internal market research has lower research costs and a high response rate.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which is an advantage of external market research?",
            options=["Lower costs", "Zero bias / objective results", "High response rate", "Shared internal information"],
            correct_index=1,
            explanation="External market research offers zero bias and objective results from specialists.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Something that is feasible, logical or sensible is described as …",
            options=["viable", "ethical", "internal", "confidential"],
            correct_index=0,
            explanation="Viable means something that is feasible, logical or sensible.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of a business opportunity. (4)",
            marking_points=[
                "An idea for a person to start a business so they can generate an income.",
                "A chance to improve current operations and contribute to greater profitability.",
                "Entrepreneurs constantly look for new business opportunities to remain competitive.",
                "Often arises when there is a gap in the market.",
            ],
            sample_answer="A business opportunity is an idea for a person to start a business to generate income. It is a chance to improve current operations and increase profitability, often arising when there is a gap in the market. Entrepreneurs constantly look for new opportunities to stay competitive.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the importance of assessing needs and desires in identifying a business opportunity. (4)",
            marking_points=[
                "Needs and desires are the keys to successful business opportunities.",
                "Success depends on awareness and fulfilment of the target market's needs.",
                "Every need and desire is a possible business opportunity / guaranteed market.",
                "Businesses can create a desire through well-designed advertising and marketing.",
            ],
            sample_answer="Assessing needs and desires is important because they are the keys to successful business opportunities. Success depends on being aware of and fulfilling the target market's needs, every unmet need is a guaranteed market, and businesses can create desire through well-designed advertising and marketing campaigns.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the importance of market research for a business. (6)",
            marking_points=[
                "Assesses the needs and desires of customers.",
                "Provides information about industry trends and competitors' actions.",
                "Helps develop and enhance the product.",
                "Minimises risks and identifies gaps in customer expectations.",
            ],
            sample_answer="Market research assesses customers' needs and desires, gives information about industry trends and competitors, helps develop and enhance the product, minimises risks and identifies gaps in customer expectations, and keeps the business informed about constantly changing tastes and behaviours.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between internal and external market research. (4)",
            marking_points=[
                "Internal is conducted by a person within the company; external by an outside specialist.",
                "Internal uses company resources and focuses on factors within the business.",
                "External obtains feedback from customers, potential customers and suppliers.",
                "External focuses on the interaction between the business and the customers.",
            ],
            sample_answer="Internal market research is conducted by a person within the company, using company resources and focusing on factors within the business. External market research is conducted by an outside specialist, obtaining feedback from customers and suppliers and focusing on the interaction between the business and its customers.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages and disadvantages of internal market research. (6)",
            marking_points=[
                "Advantages: lower research costs and shared information across the company.",
                "Advantages: high response rate and good insight into competitors' positions.",
                "Disadvantages: lack of anonymity.",
                "Disadvantages: not as formalised as external market research.",
            ],
            sample_answer="Internal market research has lower research costs, shares information across the company, has a high response rate and gives insight into competitors. However, it has disadvantages such as a lack of anonymity and being less formalised than external market research.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the protocol/ethical issues to be adhered to when conducting research. (6)",
            marking_points=[
                "Research must be conducted with the willing cooperation of participants.",
                "Research within an organisation must be approved/obtain clearance first.",
                "The researcher should not try to influence participants' opinions.",
                "Information must be kept confidential and findings must be accurate and not misleading.",
            ],
            sample_answer="When conducting research, it must be done with the willing cooperation of participants, be approved if conducted within an organisation, and the researcher must not influence participants' opinions. Consent should be obtained, information kept confidential, and findings reported accurately without being misleading; research may not disadvantage, exploit or be inhumane to anyone.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the SWOT analysis as a tool to determine a viable business venture. (6)",
            marking_points=[
                "SWOT stands for Strengths, Weaknesses, Opportunities and Threats.",
                "Strengths and weaknesses are internal factors under the business's control.",
                "Opportunities and threats are external factors with little or no control.",
                "The goal is to enhance strengths, reduce weaknesses, expand opportunities and avoid threats.",
            ],
            sample_answer="A SWOT analysis summarises data into Strengths, Weaknesses, Opportunities and Threats. Strengths and weaknesses are internal factors under the business's control, while opportunities and threats are external factors with little or no control. The goal is to enhance strengths, reduce weaknesses, expand opportunities and avoid threats to determine a viable venture.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="List the requirements of a good questionnaire / research instrument. (4)",
            marking_points=[
                "States the goal of the research.",
                "Uses clear, simple and unambiguous questions.",
                "Is short and takes little time to complete.",
                "Starts in a friendly, non-intimidating way and respects the respondent.",
            ],
            sample_answer="A good questionnaire states the goal of the research, uses clear and unambiguous questions, is short and quick to complete, and starts in a friendly, non-intimidating way that respects the respondent.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_business_opportunities = build_generate(_pools)
