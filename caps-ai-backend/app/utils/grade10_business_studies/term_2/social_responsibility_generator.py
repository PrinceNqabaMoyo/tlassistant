"""Grade 10 Business Studies - Term 2 - Topic 8: Social responsibility.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_socialresp"
VAID = "social_responsibility"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A duty to act in the best interests of one's environment and society as a whole is called …",
            options=["profitability", "social responsibility", "inequality", "productivity"],
            correct_index=1,
            explanation="Social responsibility means each person has a duty to act in the best interests of their environment and society.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A company's commitment to manage the social, environmental and economic effects of its operations responsibly is …",
            options=["CSR", "GDP", "SWOT", "CIPC"],
            correct_index=0,
            explanation="Corporate Social Responsibility (CSR) is a company's commitment to manage its impact responsibly.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is a common example of social responsibility?",
            options=["Increasing prices", "Reducing carbon footprints", "Avoiding tax", "Cutting wages"],
            correct_index=1,
            explanation="Reducing carbon footprints, donating to charity and volunteering are common examples of social responsibility.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="How much carbon dioxide a person or company emits through its activities is its …",
            options=["carbon footprint", "carbon credit", "carbon tax", "carbon market"],
            correct_index=0,
            explanation="A carbon footprint refers to how much carbon dioxide a person or company emits.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Donating money or food parcels to local NGOs is an initiative to address …",
            options=["piracy", "inequality and poverty", "counterfeiting", "load shedding"],
            correct_index=1,
            explanation="Donating money or food to NGOs helps address inequality and poverty.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Offering voluntary HIV/AIDS testing, counselling and ARV treatment programmes addresses …",
            options=["gambling", "HIV/AIDS", "piracy", "crime"],
            correct_index=1,
            explanation="Voluntary testing, counselling and ARV programmes are initiatives that address HIV/AIDS.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Educating managers on the benefits of diversity and creating mentorship programmes addresses …",
            options=["inclusivity", "piracy", "gambling", "strikes"],
            correct_index=0,
            explanation="Promoting diversity and mentorship in the workplace addresses inclusivity.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Referring employees to Gamblers Anonymous and offering financial literacy education addresses …",
            options=["crime", "gambling", "violence", "piracy"],
            correct_index=1,
            explanation="Awareness programmes, financial literacy and referrals to Gamblers Anonymous address gambling.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Using software product keys, watermarks and tamper-proof software addresses …",
            options=["piracy", "poverty", "inclusivity", "strikes"],
            correct_index=0,
            explanation="Product keys, watermarks and tamper-proof software are initiatives to address piracy.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Encouraging employees to join community policing forums and sponsoring community events addresses …",
            options=["crime", "gambling", "piracy", "HIV/AIDS"],
            correct_index=0,
            explanation="Community policing forums and community involvement are initiatives that address crime.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Offering an Employee Assistance Programme (EAP) and counselling facilities addresses …",
            options=["violence", "piracy", "inflation", "gambling"],
            correct_index=0,
            explanation="An EAP and counselling facilities help employees and address violence.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Businesses are referred to as corporate … because they have responsibilities to their community.",
            options=["traders", "citizens", "regulators", "rivals"],
            correct_index=1,
            explanation="Businesses are corporate citizens with social, cultural and environmental responsibilities.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of social responsibility. (4)",
            marking_points=[
                "Each person has a duty to act in the best interests of their environment and society.",
                "Individuals are responsible for the effects of their behaviour and lifestyle on others.",
                "Every individual and organisation should contribute to the well-being of the community.",
                "It includes acting morally and ethically in everyday life and business practices.",
            ],
            sample_answer="Social responsibility means each person has a duty to act in the best interests of their environment and society. Individuals are responsible for the effects of their behaviour on others, and every individual and organisation should contribute to the community's well-being by behaving morally and ethically.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of Corporate Social Responsibility (CSR). (4)",
            marking_points=[
                "Businesses take responsibility for their impact on society and the environment.",
                "It includes managing social, cultural and environmental responsibilities to the community.",
                "It is how a business conducts operations ethically and morally.",
                "It covers how the business uses its human, physical and financial resources.",
            ],
            sample_answer="CSR means businesses take responsibility for their impact on society and the environment. It includes their social, cultural and environmental responsibilities to the community, and the ethical, moral way they conduct operations and use their human, physical and financial resources.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Recommend initiatives businesses can take to address inequality and poverty. (6)",
            marking_points=[
                "Support government poverty alleviation programmes.",
                "Donate money or food parcels to local NGOs.",
                "Invest in young startups and encourage entrepreneurial programmes.",
                "Provide bursaries, learnerships or apprenticeships and upskill employees.",
            ],
            sample_answer="To address inequality and poverty, businesses can support government poverty alleviation programmes, donate money or food parcels to local NGOs, invest in young startups, encourage entrepreneurial programmes, and provide bursaries or learnerships while upskilling their employees.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Suggest initiatives businesses can take to address HIV/AIDS. (6)",
            marking_points=[
                "Conduct regular workshops/information sessions on HIV/AIDS.",
                "Develop counselling programmes for infected/affected employees.",
                "Develop strategies to deal with stigma and discrimination.",
                "Offer voluntary testing and support ARV treatment programmes.",
            ],
            sample_answer="To address HIV/AIDS, businesses can run regular workshops, develop counselling programmes for affected employees, create strategies to deal with stigma and discrimination, offer voluntary testing and counselling, and support antiretroviral treatment programmes.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Recommend initiatives businesses can take to address inclusivity in the workplace. (6)",
            marking_points=[
                "Educate managers and employees on the benefits of diversity.",
                "Create or amend policies from recruitment to promotion.",
                "Value individual differences and make employees feel welcome.",
                "Design a non-segregating workplace and create mentorship programmes.",
            ],
            sample_answer="To address inclusivity, businesses can educate managers and employees about diversity, create or amend policies from recruitment to promotion, value individual differences so employees feel welcome, design a workplace that does not segregate staff, and create mentorship programmes for advancement.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Suggest initiatives businesses can take to address piracy and counterfeiting. (6)",
            marking_points=[
                "Raise awareness of piracy and counterfeiting.",
                "Protect intellectual property through copyright, patents and trademarks.",
                "Use software product keys, watermarks and tamper-proof software.",
                "Use technology (holograms, smart cards) and prosecute counterfeiters.",
            ],
            sample_answer="To address piracy and counterfeiting, businesses can raise awareness, protect their intellectual property through copyright, patents and trademarks, use software product keys, watermarks and tamper-proof software, and apply technology such as holograms while tracking down and prosecuting counterfeiters.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Recommend initiatives businesses can take to address crime. (4)",
            marking_points=[
                "Encourage employees to participate in community policing forums.",
                "Become involved in sustainable projects within the local community.",
                "Sponsor special sports or community events.",
                "Use in-house security teams to reduce crime.",
            ],
            sample_answer="To address crime, businesses can encourage employees to join community policing forums, get involved in sustainable local community projects, sponsor community or sports events, and use in-house security teams to deter and detect crime.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Give THREE practical examples of social responsibility by individuals. (3)",
            marking_points=[
                "Reducing carbon footprints.",
                "Donations to charities.",
                "Volunteering in the community.",
            ],
            sample_answer="Three examples of social responsibility are reducing carbon footprints, donating to charities, and volunteering in the community.",
            marks=3,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_social_responsibility = build_generate(_pools)
