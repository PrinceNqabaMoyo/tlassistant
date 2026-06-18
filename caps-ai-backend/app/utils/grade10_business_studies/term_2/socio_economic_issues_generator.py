"""Grade 10 Business Studies - Term 2 - Topic 7: Contemporary socio-economic
issues.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_socioecon"
VAID = "socio_economic_issues"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Aspects that have a negative effect on individuals, communities and businesses are called …",
            options=["social responsibility", "profitability", "socio-economic issues", "employment"],
            correct_index=2,
            explanation="Socio-economic issues are societal and economic factors in the macro environment that affect people and businesses negatively.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The difference in income levels and wealth between groups of people is called …",
            options=["poverty", "inequality", "inclusivity", "discrimination"],
            correct_index=1,
            explanation="Inequality is the difference in income levels and wealth between groups of people.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The lack of resources to meet basic human needs is defined as …",
            options=["inequality", "poverty", "unemployment", "crime"],
            correct_index=1,
            explanation="Poverty is the lack of resources to meet basic human needs.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Everyone having access to equal opportunities irrespective of race, gender, religion or disability describes …",
            options=["inclusivity", "productivity", "a pyramid scheme", "discrimination"],
            correct_index=0,
            explanation="Inclusivity means everyone has access to equal opportunities regardless of race, gender, religion or disability.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Employees who are always absent because of medical appointments are most likely affected by …",
            options=["inequality", "HIV/AIDS", "unemployment", "poverty"],
            correct_index=1,
            explanation="Employees affected by HIV/AIDS are often absent for medical appointments, reducing productivity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A risk people take by placing bets with money in the hope of winning more money or a prize is …",
            options=["piracy", "gambling", "bootlegging", "counterfeiting"],
            correct_index=1,
            explanation="Gambling is a risk people take by betting money in the hope of winning more.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A scheme where only the individuals at the top receive large sums while others keep investing is a …",
            options=["pyramid scheme", "trademark", "patent", "copyright"],
            correct_index=0,
            explanation="In a pyramid scheme, only those at the top of the pyramid receive large sums of money.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The process of investing unlawful profits from crime into valid businesses to hide their source is called …",
            options=["money laundering", "bootlegging", "piracy", "gambling"],
            correct_index=0,
            explanation="Money laundering disguises the source of unlawful profits by investing them in legitimate businesses.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The illegal copying or reproduction of someone's product, music or software is called …",
            options=["piracy", "inclusivity", "inequality", "a strike"],
            correct_index=0,
            explanation="Piracy is the illegal copying or reproduction of a product, music, video or software.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Legal protection given to the original inventor of an idea so it cannot be reproduced without permission is a …",
            options=["trademark", "copyright", "patent", "licence"],
            correct_index=1,
            explanation="Copyright is legal protection given to the original inventor/creator of a work.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A right granted to an inventor preventing others from making the invention for 20 years is a …",
            options=["patent", "copyright", "trademark", "warranty"],
            correct_index=0,
            explanation="A patent prevents others from producing, using or importing an invention for a limited period of twenty years.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A name, representation or design used by a company for its products, registered with CIPC, is a …",
            options=["patent", "copyright", "trademark", "logo licence"],
            correct_index=2,
            explanation="A trademark is a name/design used for a company's products and registered with CIPC.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The illegal production of counterfeit goods for sale is known as …",
            options=["bootlegging", "inclusivity", "lockout", "go-slow"],
            correct_index=0,
            explanation="Bootlegging is the illegal production of counterfeit goods for sale.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A form of industrial action where workers refuse to work is a …",
            options=["lockout", "go-slow", "strike", "boycott"],
            correct_index=2,
            explanation="A strike is a form of industrial action where workers refuse to work.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="When business owners prevent workers from entering the workplace, this is a …",
            options=["strike", "go-slow", "lockout", "protest"],
            correct_index=2,
            explanation="A lockout is when owners do not allow workers to work and prevent them from entering the workplace.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A registered trademark stays protected forever provided it is renewed every …",
            options=["five years", "ten years", "twenty years", "year"],
            correct_index=1,
            explanation="A registered trademark is protected indefinitely provided it is renewed every ten years.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Define socio-economic issues and explain why they pose a challenge to businesses. (6)",
            marking_points=[
                "Socio-economic issues are societal and economic factors that negatively affect individuals, communities and businesses.",
                "Customers may have limited disposable income, so businesses are poorly supported.",
                "Absenteeism (e.g. HIV/AIDS) decreases productivity.",
                "Counterfeiting, bootlegging and crime lead to loss of profit; CSR pressure raises costs.",
            ],
            sample_answer="Socio-economic issues are societal and economic factors in the macro environment that negatively affect individuals, communities and businesses. They challenge businesses because customers have limited disposable income, absenteeism reduces productivity, crime and counterfeiting cause losses, and businesses feel pressured to fund CSR projects, raising costs.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Evaluate the negative impact of HIV/AIDS on businesses. (8)",
            marking_points=[
                "Reduced productivity of affected employees.",
                "Increased absenteeism due to medical appointments and funerals.",
                "Higher staff turnover as experienced employees die, raising hiring/training costs.",
                "Low morale of colleagues and possible discrimination/stigmatisation, decreasing productivity and profits.",
            ],
            sample_answer="HIV/AIDS reduces the productivity of affected employees and increases absenteeism for medical appointments and funerals. Experienced employees may die, raising staff turnover and hiring/training costs. Remaining staff suffer low morale and increased workloads, and affected employees may face stigmatisation, all of which decrease productivity and profits.",
            marks=8,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the impact of inequality and poverty on businesses. (6)",
            marking_points=[
                "Customers have less or no money to spend, reducing business profitability.",
                "Limited customer spending means lower sales figures.",
                "Businesses may not grow because of reduced sales.",
                "Poverty raises crime and pressures businesses to invest in poor communities.",
            ],
            sample_answer="Inequality and poverty mean customers have little disposable income, so they spend less, reducing sales and profitability. Businesses record lower sales and may not grow. Poverty also increases crime and creates media pressure on businesses to invest in poor communities.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning and purpose of inclusivity in the workplace. (6)",
            marking_points=[
                "Inclusivity means everyone has access to equal opportunities regardless of race, gender, religion or disability.",
                "It aims to address past imbalances and discrimination.",
                "Its purpose is to ensure fair labour practices and redress past inequalities.",
                "It ensures the workforce is representative and accommodates people with disabilities.",
            ],
            sample_answer="Inclusivity means everyone has access to equal opportunities regardless of race, gender, religion or disability, addressing past imbalances and discrimination. Its purpose is to ensure fair labour practices, redress past inequalities, create a representative workforce and accommodate people with disabilities.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the impact of gambling on businesses. (6)",
            marking_points=[
                "Employees in financial difficulty from gambling may be absent regularly.",
                "Compulsive gamblers may be unwilling to work overtime.",
                "Absenteeism and unproductive staff disrupt the work setting.",
                "Lower morale, depression and money laundering promote corruption.",
            ],
            sample_answer="Gambling causes employees in financial difficulty to be absent regularly and unwilling to work overtime. This absenteeism and unproductivity disrupt the workplace, while lower morale and depression reduce focus, and gambling such as money laundering promotes corruption in businesses.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Define piracy and discuss its negative impact on businesses. (6)",
            marking_points=[
                "Piracy is the illegal copying/reproduction of a product, music, video or software.",
                "Businesses experience a decline in sales due to copied/imitation products.",
                "Businesses may be forced to adjust prices to reduce the impact on sales.",
                "Businesses spend money taking legal action against people who copy their products.",
            ],
            sample_answer="Piracy is the illegal copying or reproduction of someone's product, music or software. It causes a decline in sales due to imitation products, forces businesses to adjust prices to protect sales, and costs money when businesses take legal action against those who copy their products.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Recommend and explain THREE methods businesses can use to deal with piracy. (6)",
            marking_points=[
                "Copyright: legal protection so a work cannot be reproduced without permission.",
                "Patent: a right preventing others from producing an invention for twenty years.",
                "Trademark: a registered name/design that may not be used by anyone else.",
            ],
            sample_answer="To deal with piracy, businesses can use copyright, which legally protects a work from being reproduced without permission; patents, which prevent others from producing an invention for twenty years; and trademarks, registered names or designs that may not be used by anyone else.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of counterfeiting and bootlegging. (4)",
            marking_points=[
                "Counterfeiting is fraudulently manufacturing/altering/distributing a product of lesser value than the original.",
                "Counterfeit goods imitate the original product.",
                "Bootlegging is the illegal production of counterfeit goods for sale.",
                "Both reduce sales and profits of the original business.",
            ],
            sample_answer="Counterfeiting is the fraudulent manufacture, alteration or distribution of a product of lesser value that imitates the original. Bootlegging is the illegal production of these counterfeit goods for sale. Both reduce the sales and profits of the original business.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_socio_economic_issues = build_generate(_pools)
