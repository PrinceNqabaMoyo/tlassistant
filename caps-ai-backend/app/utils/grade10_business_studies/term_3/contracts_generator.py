"""Grade 10 Business Studies - Term 3 - Topic 15: Contracts.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_contracts"
VAID = "contracts"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An agreement enforceable by law between two or more parties is a …",
            options=["contract", "prospectus", "questionnaire", "memorandum"],
            correct_index=0,
            explanation="A contract is an agreement enforceable by law between two or more parties.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A legal agreement between an employer and an employee setting out terms of work is a/an …",
            options=["insurance contract", "employment contract", "lease contract", "hire purchase contract"],
            correct_index=1,
            explanation="An employment contract is a legal agreement between an employer and employee on terms of employment.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An agreement where the insured pays premiums to be compensated when a specified event happens is a/an …",
            options=["insurance contract", "lease contract", "rental agreement", "employment contract"],
            correct_index=0,
            explanation="An insurance contract transfers risk to the insurer in exchange for premiums.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The person who owns an asset and makes it available to another to use is the …",
            options=["lessee", "lessor", "tenant", "insured"],
            correct_index=1,
            explanation="The lessor owns the asset and makes it available to the lessee for an agreed amount.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The person who pays to use another person's asset for an agreed period is the …",
            options=["lessor", "lessee", "landlord", "insurer"],
            correct_index=1,
            explanation="The lessee pays to use another person's asset for an agreed period.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A person who rents out land, a building or accommodation is the …",
            options=["tenant", "landlord", "lessee", "insured"],
            correct_index=1,
            explanation="A landlord rents out land, a building or accommodation to a tenant.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A person who occupies land or property rented from a landlord is the …",
            options=["tenant", "lessor", "insurer", "employer"],
            correct_index=0,
            explanation="A tenant occupies land or property rented from a landlord.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="An individual or business that pays premiums to be covered for a specific risk is the …",
            options=["insurer", "insured", "lessor", "landlord"],
            correct_index=1,
            explanation="The insured pays premiums to an insurance company to be covered for a specific risk.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which Act provides the minimum acceptable standard for an employment contract?",
            options=["Companies Act", "Basic Conditions of Employment Act (BCEA)", "Consumer Protection Act", "Income Tax Act"],
            correct_index=1,
            explanation="The Basic Conditions of Employment Act (BCEA) provides minimum standards for employment contracts.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which of the following is a type of contract studied in this topic?",
            options=["Hire purchase contract", "Prospectus", "SWOT analysis", "Mind map"],
            correct_index=0,
            explanation="Employment, insurance, hire purchase, lease and rental are the types of contracts studied.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="For a contract to be valid it must be entered into …",
            options=["under threat", "voluntarily, without force", "by one party only", "verbally only"],
            correct_index=1,
            explanation="A contract must be entered into voluntarily, without threat or force, by parties legally able to do so.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A written or oral agreement that can be imposed in a court of law is described as …",
            options=["enforceable", "voluntary", "informal", "negotiable"],
            correct_index=0,
            explanation="Enforceable means an agreement that can be imposed in a court of law.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the meaning of a contract. (4)",
            marking_points=[
                "A contract is an agreement enforceable by law between two or more parties.",
                "Parties promise to fulfil certain obligations.",
                "It is a legally binding agreement.",
                "Parties are bound to perform/not perform a task or give goods/services in return for something.",
            ],
            sample_answer="A contract is an agreement enforceable by law between two or more parties in which they promise to fulfil certain obligations. It is a legally binding agreement that binds the parties to perform or not perform a certain task, or give goods or services in return for something.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the details/content/aspects of a contract. (6)",
            marking_points=[
                "Information of the parties and the terms and conditions of the agreement.",
                "A proposal by one party and acceptance by the other party.",
                "Payment arrangements, duration and the date the agreement comes into effect.",
                "Both parties must be legally able to enter into it and do so voluntarily.",
            ],
            sample_answer="A contract should stipulate the information of the parties and the terms and conditions, include a proposal by one party and acceptance by the other, and cover payment arrangements, duration and the effective date. Both parties must be legally able to enter into the contract and must do so voluntarily, without threat or force.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Name FIVE types of contracts that entrepreneurs enter into. (5)",
            marking_points=[
                "Employment contracts.",
                "Insurance contracts.",
                "Hire purchase contracts.",
                "Lease contracts and rental agreements.",
            ],
            sample_answer="Five types of contracts are employment contracts, insurance contracts, hire purchase contracts, lease contracts and rental agreements.",
            marks=5,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the aspects that an employment contract should contain. (6)",
            marking_points=[
                "Details of the employer and details of the employee.",
                "Wages/salary package, job title and job description.",
                "Working hours, days of work, overtime, meal breaks and benefits.",
                "Details of leave and termination of employment.",
            ],
            sample_answer="An employment contract should contain details of the employer and employee, the wages/salary package, job title and job description, working hours and days of work, overtime and meal breaks, details of benefits and leave, and details about termination of employment.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the rights and responsibilities of an employer in an employment contract. (4)",
            marking_points=[
                "Provide fair remuneration to the employee.",
                "Provide a reasonably safe working environment.",
                "Grant vocational, family responsibility and sick leave (LRA and BCEA).",
                "Comply with labour laws.",
            ],
            sample_answer="An employer must provide fair remuneration, a reasonably safe working environment, and grant vocational leave, family responsibility leave and sick leave in line with the Labour Relations Act and Basic Conditions of Employment Act, complying with labour laws.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the rights and responsibilities of an employee in an employment contract. (4)",
            marking_points=[
                "Make services available to the employer within the agreed period.",
                "Act in accordance with the skills for which they were hired.",
                "Act in the best interests of the business; no misconduct or dishonesty.",
                "Obey the employer's lawful and morally sound commands.",
            ],
            sample_answer="An employee must make their services available to the employer within the agreed period, act according to the skills for which they were hired, act in the best interests of the business (avoiding misconduct and dishonesty), and obey the employer's lawful and morally sound commands.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain what an insurance contract is and how it works. (4)",
            marking_points=[
                "An agreement between the insurer (insurance company) and the insured (policyholder).",
                "The insured pays an agreed amount (premiums) to the insurer.",
                "The insured receives compensation when a specified event happens.",
                "Insurance transfers risk from the individual/business to the insurance company.",
            ],
            sample_answer="An insurance contract is an agreement between the insurer (insurance company) and the insured (policyholder) in which the insured pays agreed premiums and receives compensation when a specified event happens. It transfers risk from the individual or business to the insurance company in exchange for premiums.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the legal implications of contracts for the parties involved. (4)",
            marking_points=[
                "A contract is legally binding and enforceable in a court of law.",
                "Parties have obligations they must carry out.",
                "Breaching a contract can result in the court instructing a party to fulfil obligations.",
                "Contracts prevent future misunderstanding and must comply with the constitution/law.",
            ],
            sample_answer="A contract is legally binding and enforceable in a court of law, so parties have obligations they must carry out. Breaching a contract can lead to a court instructing the party to fulfil its responsibilities. Contracts prevent future misunderstandings and their contents must comply with the law/constitution.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_contracts = build_generate(_pools)
