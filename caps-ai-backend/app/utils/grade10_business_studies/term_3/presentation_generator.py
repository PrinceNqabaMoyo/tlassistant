"""Grade 10 Business Studies - Term 3 - Topic 16: Presentation of business
information.

Deterministic generator (no LLM). Content hand-authored from CAPS notes and
activities. Subskills: concepts (mcq), discussion (typed), mixed.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .._bs_common import build_generate, make_mcq, make_typed

PREFIX = "g10bs_present"
VAID = "presentation"


def _concepts(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A presentation delivered through speech or orally is a … presentation.",
            options=["verbal", "non-verbal", "written", "graphic"],
            correct_index=0,
            explanation="A verbal presentation is delivered through speech or orally.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="The transfer of information through business reports, handouts, charts and posters is a … presentation.",
            options=["verbal", "non-verbal", "oral", "spoken"],
            correct_index=1,
            explanation="A non-verbal presentation transfers information through reports, handouts, charts and posters.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A key communication tool that provides an evaluation of a particular business issue is a …",
            options=["business report", "poster", "slide", "handout"],
            correct_index=0,
            explanation="A business report is a key communication tool that evaluates a particular business issue.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A written summary of information dealt with in a presentation is a …",
            options=["handout", "transparency", "graph", "poster"],
            correct_index=0,
            explanation="A handout is a written summary of information dealt with in a presentation.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A data structure that organises information into rows and columns is a …",
            options=["table", "graph", "diagram", "poster"],
            correct_index=0,
            explanation="A table organises information into rows and columns.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Diagrams that show the relationship between two or more data sets or values are …",
            options=["graphs", "handouts", "posters", "tables"],
            correct_index=0,
            explanation="Graphs are diagrams that show the relationship between two or more data sets or values.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Devices that make use of both sound and sight are called …",
            options=["audio-visual aids", "handouts", "transparencies", "posters"],
            correct_index=0,
            explanation="Audio-visual aids make use of both sound (audio) and sight (visual).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A device used to project computer output onto a screen is a …",
            options=["data projector", "whiteboard", "poster", "handout"],
            correct_index=0,
            explanation="A data projector projects/displays computer output onto a screen.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A simple drawing showing the processes for each stage of a project is best presented as a …",
            options=["flowchart/diagram", "bar graph", "illustration", "table"],
            correct_index=0,
            explanation="A flowchart/diagram is a simplified drawing that shows processes for each stage.",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="A set of sales figures shown in a series of rectangles is presented as a …",
            options=["bar graph", "flowchart", "illustration", "poster"],
            correct_index=0,
            explanation="A bar graph presents figures in a series of rectangles (bars).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Online technology allowing users in different locations to hold face-to-face meetings is …",
            options=["video conferencing", "a data projector", "a transparency", "a handout"],
            correct_index=0,
            explanation="Video conferencing allows users in different locations to hold face-to-face meetings (e.g. Zoom).",
            visual_aid_key=VAID,
        ),
        lambda: make_mcq(
            prefix=PREFIX,
            prompt="Which is a disadvantage of using graphs/diagrams in a presentation?",
            options=[
                "They display a lot of information in an easy format",
                "Too many can confuse the audience",
                "They help identify trends",
                "They require little explanation",
            ],
            correct_index=1,
            explanation="Too many diagrams and graphs can be confusing to the audience - a key disadvantage.",
            visual_aid_key=VAID,
        ),
    ]


def _discussion(r) -> List[Callable[[], Dict[str, Any]]]:
    return [
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline the importance of business reports. (4)",
            marking_points=[
                "Provide a critical analysis of how the business is performing.",
                "Used to guide decision-making in the business.",
                "Allow owners/senior management to investigate and solve identified issues.",
                "Provide timely and factual information and inform management of each department's work.",
            ],
            sample_answer="Business reports provide a critical analysis of how the business is performing, guide decision-making, and allow owners and senior management to investigate and solve identified issues. They provide timely and factual information and inform management of what each department is doing.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Outline guidelines for writing an effective business report. (6)",
            marking_points=[
                "Determine the scope, target audience and how the report should be presented.",
                "Collect the necessary information and prepare an overview.",
                "Write concisely using simple language and clear, short sentences.",
                "Use accurate visual aids and revise/correct the report; ask someone to review it.",
            ],
            sample_answer="To write an effective business report, determine the scope, target audience and presentation method, collect the necessary information and prepare an overview. Write concisely using simple language and short clear sentences, use accurate visual aids, and revise the report for errors before asking someone to review it.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the advantages of using graphs/diagrams (visual aids) in a presentation. (6)",
            marking_points=[
                "Help with understanding and identifying patterns and trends in data.",
                "Enable quick analysis of large amounts of data and support predictions/decisions.",
                "Display a lot of information in an easy-to-understand format.",
                "Graphs require little explanation and simplify complex information.",
            ],
            sample_answer="Graphs and diagrams help with understanding and identifying patterns and trends, enable quick analysis of large amounts of data to support predictions and decisions, display a lot of information in an easy-to-understand format, require little explanation, and simplify complex information.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss the disadvantages of using graphs/diagrams in a presentation. (4)",
            marking_points=[
                "Too many diagrams and graphs can be confusing to the audience.",
                "Information can easily be manipulated, causing false interpretations.",
                "They may distract the audience from the speech.",
                "Preparation of graphs and diagrams is time-consuming.",
            ],
            sample_answer="Disadvantages of graphs and diagrams include that too many can confuse the audience, information can be manipulated to cause false interpretations, they may distract the audience from the speech, and their preparation is time-consuming.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss factors that must be considered when preparing a verbal presentation. (6)",
            marking_points=[
                "Identify the purpose and main points and capture the main aim in the introduction.",
                "Present relevant, accurate information and be fully conversant with the content.",
                "Know the background of the audience to choose appropriate visual aids.",
                "Prepare a draft (introduction, body, conclusion), practise, time it and anticipate questions.",
            ],
            sample_answer="When preparing a verbal presentation, identify the purpose and main points and capture the aim in the introduction, present relevant and accurate information while being fully conversant with the content, know the audience's background to choose appropriate visual aids, and prepare a draft with introduction, body and conclusion - practising it, timing it, checking the venue and equipment, and anticipating questions.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Discuss factors that must be considered when designing a presentation. (6)",
            marking_points=[
                "Start with text and headings and use a legible font and font size.",
                "Select a suitable, non-distracting background and use bright colours for visibility.",
                "Choose simple, relevant images and graphics related to the content.",
                "Structure information logically, limit information per slide and check for errors.",
            ],
            sample_answer="When designing a presentation, start with text and headings, use a legible font and size, and select a suitable non-distracting background with bright colours for visibility. Choose simple relevant images and graphics related to the content, structure information in a logical sequence, limit information on each slide, and check for grammatical and spelling errors.",
            marks=6,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Explain the purpose of audio-visual aids in a presentation. (4)",
            marking_points=[
                "They help the speaker present information more effectively.",
                "They appeal to the audience's sight and hearing.",
                "They solidify and reinforce the message.",
                "Examples: data projector, interactive whiteboard, video conferencing.",
            ],
            sample_answer="Audio-visual aids help the speaker present business information more effectively by appealing to the audience's sight and hearing, thereby solidifying and reinforcing the message. Examples include a data projector, interactive whiteboard/smartboard and video conferencing.",
            marks=4,
            visual_aid_key=VAID,
        ),
        lambda: make_typed(
            prefix=PREFIX,
            prompt="Distinguish between verbal and non-verbal presentations. (4)",
            marking_points=[
                "A verbal presentation is delivered through speech or orally.",
                "It involves what you say, how you say it and what the audience sees.",
                "A non-verbal presentation transfers information through reports, handouts, charts and posters.",
                "Non-verbal presentations use the support of visual aids.",
            ],
            sample_answer="A verbal presentation is delivered through speech or orally and involves what you say, how you say it with your voice, and everything the audience can see. A non-verbal presentation transfers information through business reports, handouts, charts and posters, with the support of visual aids.",
            marks=4,
            visual_aid_key=VAID,
        ),
    ]


def _pools(r):
    return {
        "concepts": _concepts(r),
        "discussion": _discussion(r),
    }


generate_presentation = build_generate(_pools)
