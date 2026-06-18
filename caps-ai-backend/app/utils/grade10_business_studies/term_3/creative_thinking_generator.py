"""Grade 10 Business Studies - Term 3 - Topic 12: Creative thinking and problem
solving.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_creative"
VAID = "creative_thinking"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The process of generating innovative and imaginative ideas is called …",
            options=["problem-solving", "creative thinking", "decision-making", "benchmarking"],
            correct_index=1,
            explanation="Creative thinking is the process of generating innovative and imaginative ideas.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The process of finding solutions to difficult or complex issues is called …",
            options=["problem-solving", "creative thinking", "brainstorming", "forecasting"],
            correct_index=0,
            explanation="Problem-solving is the process of finding solutions to difficult or complex issues.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Diagrams that represent ideas connected to a central theme are called …",
            options=["force field analysis", "mind mapping", "SCAMPER", "Delphi technique"],
            correct_index=1,
            explanation="Mind mapping uses diagrams that represent ideas connected to a central theme.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A group activity to find a solution by gathering a list of ideas spontaneously is …",
            options=["brainstorming", "the empty chair technique", "the Delphi technique", "forced combinations"],
            correct_index=0,
            explanation="Brainstorming is a group activity to find a solution by gathering ideas spontaneously.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A technique used to determine the forces that are for and against a decision is …",
            options=["Force Field Analysis", "SCAMPER", "mind mapping", "the empty chair technique"],
            correct_index=0,
            explanation="Force Field Analysis determines the driving and restraining forces for and against a decision.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A method that relies on a panel of experts using questionnaires to solve a problem is the …",
            options=["Delphi Technique", "Nominal Group Technique", "empty chair technique", "brainstorming"],
            correct_index=0,
            explanation="The Delphi Technique relies on a panel of experts who respond to a series of questionnaires.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A role-play exercise where a person imagines someone sitting opposite them is the …",
            options=["empty chair technique", "Delphi technique", "SCAMPER", "force field analysis"],
            correct_index=0,
            explanation="The empty chair technique is a role-play exercise placing a person across from an empty chair.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A structured method where each member silently brainstorms ideas and then votes is the …",
            options=["Nominal Group Technique", "brainstorming", "Delphi technique", "forced combinations"],
            correct_index=0,
            explanation="The Nominal Group Technique has each member silently generate ideas, then rank/vote on them.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="SCAMPER is an acronym that helps teams explore ideas from how many different perspectives?",
            options=["Five", "Six", "Seven", "Eight"],
            correct_index=2,
            explanation="SCAMPER helps teams explore ideas from seven different perspectives using lateral thinking.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Combining new ideas that do not appear to be related in any way is the technique of …",
            options=["forced combinations", "mind mapping", "brainstorming", "Delphi technique"],
            correct_index=0,
            explanation="Forced combinations involves combining new ideas that do not appear to be related.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The process of choosing from several alternatives is best described as …",
            options=["decision-making", "problem-solving", "creative thinking", "monitoring"],
            correct_index=0,
            explanation="Decision-making is the process of choosing from several alternatives.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Local knowledge that is unique to a given culture or society is called …",
            options=["non-conventional thinking", "indigenous knowledge", "lateral thinking", "data"],
            correct_index=1,
            explanation="Indigenous knowledge is the local knowledge unique to a given culture or society.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="What is the FIRST step in the problem-solving cycle?",
            options=["Implement the strategy", "Identify the problem", "Evaluate the process", "Allocate resources"],
            correct_index=1,
            explanation="The problem-solving cycle begins with identifying the exact problem.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Thinking differently and looking at something in a new way is called …",
            options=["non-conventional thinking", "indigenous knowledge", "decision-making", "monitoring"],
            correct_index=0,
            explanation="Non-conventional thinking refers to thinking differently and looking at something in a new way.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of creative thinking. (4)",
            marking_points=[
                "Creative thinking is the process of generating innovative and imaginative ideas.",
                "It is the ability to see something in a new way.",
                "It is about thinking of unique ideas or new approaches to solve problems.",
                "It can have a positive impact and help solve business problems successfully.",
            ],
            sample_answer="Creative thinking is the process of generating innovative and imaginative ideas. It is the ability to see something in a new way and to think of unique ideas or new approaches to solve problems, having a positive impact and helping solve business problems successfully.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages/benefits of creative thinking in the workplace. (6)",
            marking_points=[
                "New, innovative and better ideas and solutions are generated.",
                "Creativity helps stay one step ahead of competitors.",
                "Complex business problems may be solved and productivity increases.",
                "It improves motivation and leads to more positive attitudes among staff.",
            ],
            sample_answer="Creative thinking generates new, innovative and better ideas and solutions, helps the business stay ahead of competitors, solves complex problems and increases productivity. It improves staff motivation and creates more positive attitudes, and may lead to new inventions and keeping up with technology.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain ways in which businesses can use creative thinking to generate entrepreneurial opportunities. (6)",
            marking_points=[
                "Design environments that stimulate creative thinking and encourage new ideas.",
                "Make time for brainstorming sessions and hold regular workshops.",
                "Place suggestion boxes and keep communication channels open.",
                "Train staff in innovative techniques and regard indigenous knowledge as valuable.",
            ],
            sample_answer="Businesses can design environments that stimulate creativity, encourage staff to suggest new ideas, make time for brainstorming sessions and workshops, place suggestion boxes and keep communication open, train staff in innovative techniques, and regard indigenous knowledge as a valuable resource.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Elaborate on the meaning of problem-solving. (4)",
            marking_points=[
                "Problem-solving is the process of finding solutions to difficult or complex issues.",
                "It is a process that requires creative thinking.",
                "Alternative solutions are identified and critically evaluated.",
                "Effective problem-solving results in good decision-making.",
            ],
            sample_answer="Problem-solving is the process of finding solutions to difficult or complex issues. It requires creative thinking, identifies and critically evaluates alternative solutions, and effective problem-solving results in good decision-making. It can be done by a group or an individual.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the steps of the problem-solving cycle. (7)",
            marking_points=[
                "Identify the problem and develop a detailed problem statement.",
                "Define the problem and its causes.",
                "Formulate a strategy by identifying possible solutions.",
                "Implement the strategy, allocate resources, monitor and evaluate the process.",
            ],
            sample_answer="The problem-solving cycle is: identify the problem and write a problem statement; define the problem and its causes; formulate a strategy by identifying possible solutions; implement the strategy; allocate resources; monitor the solution by gathering feedback; and evaluate the whole process to see if the problem was solved.",
            marks=7,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Distinguish between decision-making and problem-solving. (4)",
            marking_points=[
                "Decision-making is choosing from several alternatives; problem-solving is finding a solution to a problem.",
                "In decision-making various alternatives are considered; in problem-solving solutions are identified and evaluated.",
                "Decision-making is part of the problem-solving process where a solution is chosen.",
                "Decisions are usually made by one person; problem-solving usually involves a group.",
            ],
            sample_answer="Decision-making is the process of choosing from several alternatives, usually by one person, and is part of the problem-solving process where a solution is chosen. Problem-solving is the process of finding a solution to a problem by identifying and evaluating solutions, and usually involves a group or team.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how the Delphi Technique can be applied to solve a business problem. (6)",
            marking_points=[
                "Invite a panel of experts who do not have to be in one place.",
                "Design and distribute a questionnaire on how to solve the problem.",
                "Summarise responses and send feedback with further questionnaires.",
                "Repeat the cycle and choose the best solution after reaching consensus.",
            ],
            sample_answer="With the Delphi Technique, a business invites a panel of experts (who need not be in one place), designs and distributes a questionnaire on solving the problem, summarises their responses in a feedback report, sends further questionnaires based on the feedback over several rounds, and chooses the best solution after reaching consensus.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain how the Force Field Analysis technique is applied. (6)",
            marking_points=[
                "Describe the current situation/problem and the desired situation.",
                "List all the driving forces and restraining forces.",
                "Allocate a score to each force on a scale where 1 is weak and 5 is strong.",
                "Weigh up the totals and decide if the project is viable, then develop an action plan.",
            ],
            sample_answer="To apply Force Field Analysis, describe the current problem and the desired situation, list all driving and restraining forces, allocate each a score from 1 (weak) to 5 (strong), weigh up the totals to decide if the project is viable, and if so increase the forces for change and develop an action plan.",
            marks=6,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_creative_thinking = build_generate(_pools)
