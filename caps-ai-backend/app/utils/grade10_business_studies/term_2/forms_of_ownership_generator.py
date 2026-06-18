"""Grade 10 Business Studies - Term 2 - Topic 10: Forms of ownership.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_ownership"
VAID = "forms_of_ownership"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The legal position of a business and the way it is owned is called the …",
            options=["form of ownership", "memorandum", "prospectus", "audit"],
            correct_index=0,
            explanation="A form of ownership refers to the legal position of a business and the way it is owned.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A business owned and managed by one person is a …",
            options=["partnership", "sole trader", "private company", "co-operative"],
            correct_index=1,
            explanation="A sole trader/proprietor is a business owned and managed by one person.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Where business owners are responsible for ALL the business debts, they have …",
            options=["limited liability", "unlimited liability", "no liability", "shared liability"],
            correct_index=1,
            explanation="Unlimited liability means owners are personally responsible for all the business debts.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A legal status where a person's financial liability is limited to the amount invested is …",
            options=["unlimited liability", "limited liability", "double taxation", "continuity"],
            correct_index=1,
            explanation="Limited liability limits a person's financial liability to the amount they invested.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The name of a private company must end with …",
            options=["Ltd", "(Pty) Ltd", "Inc", "SOC Ltd"],
            correct_index=1,
            explanation="A private company's name ends with '(Proprietary) Limited' or '(Pty) Ltd'.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A company whose shares are traded freely on the JSE and whose name ends in 'Ltd' is a …",
            options=["private company", "public company", "close corporation", "sole trader"],
            correct_index=1,
            explanation="A public company trades shares freely on the stock exchange and ends with 'Ltd'.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A minimum of how many members is required to start a co-operative?",
            options=["Two", "Three", "Five", "Ten"],
            correct_index=2,
            explanation="A minimum of five members is required to start a co-operative.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A close corporation (CC) can have a maximum of how many members?",
            options=["Five", "Seven", "Ten", "Twenty"],
            correct_index=2,
            explanation="A CC can have a minimum of one and a maximum of ten members.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A document inviting the public to buy securities/shares is a …",
            options=["prospectus", "MOI", "debenture", "dividend"],
            correct_index=0,
            explanation="A prospectus is a document inviting the public to buy securities/shares.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A company incorporated for public benefit, reflected as NPC, is a …",
            options=["public company", "non-profit company", "private company", "state-owned company"],
            correct_index=1,
            explanation="A non-profit company (NPC) is incorporated for public benefit, not for gain.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A state-owned company is reflected by the letters …",
            options=["Ltd", "(Pty) Ltd", "SOC Ltd", "NPC"],
            correct_index=2,
            explanation="State-owned companies are reflected as SOC Ltd.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The ability of a business to continue to exist even if an owner dies or retires is called …",
            options=["liability", "continuity", "solvency", "liquidity"],
            correct_index=1,
            explanation="Continuity is the ability of a business to continue to exist despite a change of ownership.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A document that sets out the rights, duties and responsibilities of shareholders and directors is the …",
            options=["prospectus", "Memorandum of Incorporation (MOI)", "audit report", "partnership agreement"],
            correct_index=1,
            explanation="The Memorandum of Incorporation (MOI) sets out the rights, duties and responsibilities of stakeholders.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The form of ownership mainly used by associations of lawyers and accountants, ending in 'Inc', is a …",
            options=["public company", "personal liability company", "co-operative", "sole trader"],
            correct_index=1,
            explanation="A personal liability company (Inc) is mainly used by associations such as lawyers and accountants.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A minimum number of directors required to start a public company is …",
            options=["one", "two", "three", "five"],
            correct_index=2,
            explanation="A public company requires three or more directors and three or more shareholders.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between profit and non-profit companies. (4)",
            marking_points=[
                "A profit company is formed with the aim of making a profit; a non-profit for charity/social purposes.",
                "A profit company is incorporated for financial gain for shareholders; an NPC is incorporated not for gain.",
                "Profit organisations pay taxes based on their profit.",
                "Non-profit organisations are not required to pay taxes on net income.",
            ],
            sample_answer="A profit company is formed to make a profit and is incorporated for financial gain for its shareholders, paying tax on its profit. A non-profit company is formed for charity or social and cultural purposes, incorporated not for gain, and is not required to pay tax on net income.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages of a sole trader/proprietorship. (6)",
            marking_points=[
                "Easy and quick to form as less capital is needed.",
                "The owner can take quick decisions and has full control.",
                "The owner takes all the profits and owns all assets.",
                "There is personal contact and a personalised approach to customers.",
            ],
            sample_answer="A sole trader is easy and quick to form because less capital is needed, and the owner has full control to make quick decisions. The owner takes all the profits and owns all the assets, and offers personal contact and a personalised approach to customers.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the disadvantages of a sole trader/proprietorship. (6)",
            marking_points=[
                "The business is limited to the management abilities of the owner.",
                "The owner has unlimited liability for the debts of the business.",
                "Limited capital makes expansion and raising funds difficult.",
                "Lacks continuity, especially in the event of death or illness.",
            ],
            sample_answer="A sole trader is limited by the management abilities of the owner and has unlimited liability for the business's debts. Limited capital makes it difficult to expand or raise funds, and the business lacks continuity, especially if the owner dies or becomes ill.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages of a partnership. (6)",
            marking_points=[
                "Each partner brings knowledge, skills, experience and contacts.",
                "Workload and responsibility are shared, and each can focus on strengths.",
                "Partners invest new capital to finance expansion.",
                "Partners are taxed in their personal capacities, possibly lowering tax; not compelled to audit statements.",
            ],
            sample_answer="In a partnership each partner brings knowledge, skills, experience and contacts, giving the business a better chance to succeed. The workload and responsibility are shared so each can focus on strengths, partners invest new capital to expand, they are taxed in their personal capacities (possibly lower tax), and they are not compelled to audit their statements.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the disadvantages of a partnership. (6)",
            marking_points=[
                "Partners are jointly and severally liable for the actions of other partners.",
                "Partnership has unlimited liability - partners risk losing personal possessions.",
                "Different personalities and opinions can lead to conflict.",
                "Lacks continuity - dissolves if a partner dies or retires.",
            ],
            sample_answer="In a partnership, partners are jointly and severally liable for each other's actions and have unlimited liability, risking their personal possessions. Different personalities can cause conflict, decision-making can be slow, and the partnership lacks continuity because it dissolves if a partner dies or retires.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages of a private company. (6)",
            marking_points=[
                "Continues to trade even if a shareholder dies or resigns (continuity).",
                "Shareholders have limited liability restricted to the shares they own.",
                "Large amounts of capital can be raised as there is no limit on shareholders.",
                "Has its own legal identity and can buy assets in its name; capable directors are appointed.",
            ],
            sample_answer="A private company has continuity, trading on even if a shareholder dies or resigns. Shareholders have limited liability restricted to their shares, large amounts of capital can be raised because there is no limit on shareholders, and the company has its own legal identity, can own assets and appoint capable directors.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the disadvantages of a public company. (6)",
            marking_points=[
                "Vulnerable to increased scrutiny from government and the public.",
                "Difficult and expensive to establish due to many legal requirements.",
                "Auditing of financial statements is compulsory, raising costs.",
                "Large management structure slows down decision-making.",
            ],
            sample_answer="A public company is vulnerable to increased scrutiny from government and the public and is difficult and expensive to establish due to many legal requirements. Auditing of financial statements is compulsory, raising costs, and the large management structure slows down decision-making.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the characteristics of a co-operative. (6)",
            marking_points=[
                "A minimum of five members is required; name ends with 'Co-operative Limited'.",
                "Democratic structure with each member having one vote.",
                "Motivated by service rather than profit; members share equally in profits.",
                "A legal entity that must register with the Registrar of Co-operative Societies.",
            ],
            sample_answer="A co-operative needs a minimum of five members and its name ends with 'Co-operative Limited'. It has a democratic structure where each member has one vote, is motivated by service rather than profit, shares profits equally among members, and is a legal entity that must register with the Registrar of Co-operative Societies.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the differences between a private company and a public company. (6)",
            marking_points=[
                "A private company may not offer shares to the public; a public company trades shares on the JSE.",
                "Private shares are not freely transferable; public shares are freely transferable.",
                "A private company needs a minimum of one director; a public company needs three.",
                "A private company's name ends in (Pty) Ltd; a public company's in Ltd, and must publish a prospectus.",
            ],
            sample_answer="A private company may not offer shares to the public and its shares are not freely transferable, it needs at least one director, and its name ends in (Pty) Ltd. A public company trades its shares freely on the JSE, needs at least three directors, ends in Ltd, must publish a prospectus and audit its statements.",
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_forms_of_ownership = build_generate(_pools)
