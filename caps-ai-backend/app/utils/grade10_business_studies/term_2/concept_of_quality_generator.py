"""Grade 10 Business Studies - Term 2 - Topic 11: The concept of quality.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_quality"
VAID = "concept_of_quality"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How well goods/services satisfy the specific needs of customers refers to …",
            options=["quantity", "quality", "productivity", "profitability"],
            correct_index=1,
            explanation="Quality refers to how well goods/services satisfy the specific needs of customers.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A system to maintain standards by inspecting the final product against specifications is …",
            options=["quality assurance", "quality control", "quality management", "accreditation"],
            correct_index=1,
            explanation="Quality control inspects the final product to ensure it meets the required standards.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Inspection carried out DURING and AFTER production to get it right the first time is …",
            options=["quality control", "quality assurance", "quality grading", "sampling"],
            correct_index=1,
            explanation="Quality assurance inspects during and after production to prevent mistakes and get it right first time.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The act of overseeing all activities and tasks needed to maintain a desired level of excellence is …",
            options=["quality management", "quality control", "auditing", "benchmarking"],
            correct_index=0,
            explanation="Quality management is overseeing all activities and tasks to maintain a desired level of excellence.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which body approves the commercial standards of products in South Africa?",
            options=["CIPC", "SABS", "JSE", "SARS"],
            correct_index=1,
            explanation="The South African Bureau of Standards (SABS) approves the commercial standards of products.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of these is a method used to indicate quality in products?",
            options=["Debentures", "Trademarks", "Dividends", "Prospectus"],
            correct_index=1,
            explanation="Trademarks, samples, grades and commercial standards are methods used to indicate quality.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Following a fair selection process and offering market-related salaries are quality indicators of the … function.",
            options=["financial", "human resources", "production", "marketing"],
            correct_index=1,
            explanation="A fair selection process and market-related salaries are quality indicators of the HR function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Drawing up an accurate budget and investing surplus funds are quality indicators of the … function.",
            options=["financial", "administration", "purchasing", "public relations"],
            correct_index=0,
            explanation="Budgeting and investing surplus funds are quality indicators of the financial function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Buying raw materials in bulk and choosing reliable suppliers are quality indicators of the … function.",
            options=["marketing", "purchasing", "production", "financial"],
            correct_index=1,
            explanation="Bulk buying and choosing reliable suppliers are quality indicators of the purchasing function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Dealing quickly with negative publicity and running CSI projects are quality indicators of the … function.",
            options=["public relations", "marketing", "human resources", "administration"],
            correct_index=0,
            explanation="Handling negative publicity and CSI projects are quality indicators of the public relations function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Keeping documentation neat, accurate and available for quick decisions is a quality indicator of the … function.",
            options=["production", "administration", "financial", "marketing"],
            correct_index=1,
            explanation="Neat, accurate, available records are quality indicators of the administration function.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Differentiating products and using effective pricing techniques are quality indicators of the … function.",
            options=["marketing", "purchasing", "financial", "general management"],
            correct_index=0,
            explanation="Product differentiation and pricing techniques are quality indicators of the marketing function.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of quality. (4)",
            marking_points=[
                "Quality is the ability of goods/services to satisfy customers' needs.",
                "It refers to the characteristics of a product/service that meet customer requirements.",
                "It is the ability to meet customers' expectations on a continuous basis.",
                "It is the degree of excellence to which a product/service meets customers' needs.",
            ],
            sample_answer="Quality is the ability of goods or services to satisfy customers' needs. It refers to the characteristics of a product or service that meet customer requirements, the ability to meet expectations on a continuous basis, and the degree of excellence to which a product or service meets customers' needs.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the difference between quality control and quality assurance. (4)",
            marking_points=[
                "Quality control inspects the final product to ensure it meets required standards.",
                "Quality control sets targets, measures performance and takes corrective measures.",
                "Quality assurance inspects during and after production to meet standards at every stage.",
                "Quality assurance ensures the product is right the first time and prevents repeat mistakes.",
            ],
            sample_answer="Quality control inspects the final product to ensure it meets required standards, by setting targets, measuring performance and taking corrective measures. Quality assurance inspects during and after production so standards are met at every stage, ensuring the product is right the first time and preventing repeat mistakes.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the importance of quality for a business. (4)",
            marking_points=[
                "Quality gives the business a good reputation and promotes brand awareness.",
                "Consumers associate the image of the business with the quality of the product.",
                "Quality products increase sales, profits, growth and attract investors.",
                "The business gains goodwill and support from the community.",
            ],
            sample_answer="Quality gives a business a good reputation and promotes brand awareness, and consumers associate the business's image with product quality. Quality products increase sales, profits, growth and attract prospective investors, and the business gains goodwill and community support.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the quality indicators of the human resources function. (6)",
            marking_points=[
                "The recruitment policy should attract the best candidates.",
                "HR should follow a fair and equitable selection process.",
                "Maintain a low staff turnover and a healthy employer-employee relationship.",
                "Offer market-related salaries and performance incentives to increase productivity.",
            ],
            sample_answer="Quality indicators of the HR function include a recruitment policy that attracts the best candidates, a fair and equitable selection process, a low staff turnover with healthy employer-employee relationships, and market-related salaries with performance incentives to boost productivity.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the quality indicators of the financial function. (6)",
            marking_points=[
                "Obtain capital from the most suitable sources.",
                "Negotiate lower interest rates to keep financial costs low.",
                "Draw a budget to allocate cash and prevent wastage.",
                "Keep accurate, up-to-date records and invest surplus funds.",
            ],
            sample_answer="Quality indicators of the financial function include obtaining capital from the most suitable sources, negotiating lower interest rates to reduce costs, drawing a budget to allocate cash and prevent wastage, keeping accurate up-to-date records for tax compliance, and investing surplus funds for future growth.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the quality indicators of the general management function. (6)",
            marking_points=[
                "Develop and monitor effective strategic plans.",
                "Continuously learn and understand changes in the business environment.",
                "Set direction, prioritise responsibilities and communicate the vision and values.",
                "Set an example of ethics and professionalism and allocate resources effectively.",
            ],
            sample_answer="Quality indicators of general management include developing and monitoring effective strategic plans, continuously understanding changes in the business environment, setting direction and communicating the vision and values, setting an example of ethics and professionalism, and allocating resources effectively.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the quality indicators of the purchasing function. (6)",
            marking_points=[
                "Buy raw materials in bulk and negotiate discounts to reduce costs.",
                "Choose reliable suppliers offering quality goods at reasonable prices.",
                "Place orders timeously and follow up to ensure on-time delivery.",
                "Implement good stock control and maintain average stock levels.",
            ],
            sample_answer="Quality indicators of the purchasing function include buying raw materials in bulk and negotiating discounts, choosing reliable suppliers of quality goods at reasonable prices, placing orders timeously with follow-ups for on-time delivery, and implementing good stock control while maintaining average stock levels.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the correlation between management and the success of a business. (4)",
            marking_points=[
                "Management plays an important role in making correct decisions and motivating employees.",
                "Poor management results in ineffective employees and loss of productivity.",
                "Businesses require ongoing decision-making and problem-solving.",
                "Unsolved problems and poor decisions decrease productivity.",
            ],
            sample_answer="Management plays an important role in making correct decisions and motivating employees to be productive. Poor management leads to ineffective employees and loss of productivity. Because businesses require ongoing decision-making and problem-solving, unsolved problems and poor decisions decrease productivity.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_concept_of_quality = build_generate(_pools)
