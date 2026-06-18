"""Grade 11 Business Studies - Term 3 - Topic 17: Presentation of business
information.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='presentation_of_information',
    curriculum_reference='Term 3 > Presentation of business information',
    id_prefix='g11_bs_present',
)

LO_TYPES = 'lo_presentation_types'
LO_VISUAL = 'lo_visual_aids'
LO_WRITTEN = 'lo_written_information'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Verbal presentation',
            'prompt': 'The use of speech by a presenter to convey a message to an audience is a … presentation.',
            'options': ['non-verbal', 'verbal', 'written', 'visual'],
            'correct_index': 1,
            'explanation': 'A verbal presentation is the use of speech by a presenter to convey a message to stakeholders/audiences.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on the use of speech.',
                'Spoken words to an audience = verbal presentation.',
                'Non-verbal presentations use no spoken words.',
            ),
            'guidelines': ['Use of speech = verbal presentation.'],
        }, subskill='concepts', learning_objective_id=LO_TYPES, question_family_id='verbal_definition', concept_id='verbal_presentation', concept_group='types', misconception_tags=['confuses_verbal_with_nonverbal'], diagnostic_tags=['definition', 'types']),
        with_metadata({
            'title': 'Non-verbal presentation',
            'prompt': 'Presenting information to an audience without using spoken words is a … presentation.',
            'options': ['verbal', 'non-verbal', 'oral', 'spoken'],
            'correct_index': 1,
            'explanation': 'A non-verbal presentation is the presentation of information to an audience without using spoken words (e.g. posters, handouts).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on the absence of speech.',
                'No spoken words = non-verbal presentation.',
                'Verbal presentations rely on speech.',
            ),
            'guidelines': ['No spoken words = non-verbal presentation.'],
        }, subskill='concepts', learning_objective_id=LO_TYPES, question_family_id='nonverbal_definition', concept_id='non_verbal_presentation', concept_group='types', misconception_tags=['confuses_nonverbal_with_verbal'], diagnostic_tags=['definition', 'types']),
        with_metadata({
            'title': 'Visual aids',
            'prompt': 'Charts, pictures or images that help to clarify a point or enhance a presentation are called …',
            'options': ['handouts', 'visual aids', 'reports', 'flyers'],
            'correct_index': 1,
            'explanation': 'Visual aids are charts/pictures/images that help to clarify a point or enhance a presentation.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify what enhances a presentation visually.',
                'Charts/pictures that clarify a point = visual aids.',
                'A report is a written document, not a visual aid.',
            ),
            'guidelines': ['Visuals that clarify a point = visual aids.'],
        }, subskill='concepts', learning_objective_id=LO_VISUAL, question_family_id='visual_aids_definition', concept_id='visual_aids', concept_group='visual', misconception_tags=['confuses_visual_aid_with_report'], diagnostic_tags=['definition', 'visual']),
        with_metadata({
            'title': 'Handouts',
            'prompt': 'Printed information provided to the audience to accompany a presentation is called …',
            'options': ['posters', 'handouts', 'transparencies', 'graphs'],
            'correct_index': 1,
            'explanation': 'Handouts are printed information provided to the audience to accompany a presentation.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify printed take-aways for the audience.',
                'Printed material given to the audience = handouts.',
                'Posters are displayed; handouts are given out.',
            ),
            'guidelines': ['Printed material for the audience = handouts.'],
        }, subskill='concepts', learning_objective_id=LO_VISUAL, question_family_id='handouts_definition', concept_id='handouts', concept_group='visual', misconception_tags=['confuses_handouts_with_posters'], diagnostic_tags=['definition', 'visual']),
        with_metadata({
            'title': 'Business report',
            'prompt': 'A formal written document outlining facts and findings about a business matter is a …',
            'options': ['flyer', 'business report', 'poster', 'transparency'],
            'correct_index': 1,
            'explanation': 'A business report is a formal written document outlining facts and findings about a business matter.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the formal written document.',
                'Facts and findings in a formal document = business report.',
                'A flyer is a short promotional handout.',
            ),
            'guidelines': ['Formal facts/findings document = business report.'],
        }, subskill='concepts', learning_objective_id=LO_WRITTEN, question_family_id='business_report_definition', concept_id='business_report', concept_group='written', misconception_tags=['confuses_report_with_flyer'], diagnostic_tags=['definition', 'written']),
        with_metadata({
            'title': 'Graphs vs tables',
            'prompt': 'A set of facts and figures arranged in columns and rows is a …',
            'options': ['graph', 'table', 'diagram', 'poster'],
            'correct_index': 1,
            'explanation': 'A table is a set of facts and figures arranged in columns and rows (a graph shows relationships between sets of numbers).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on rows and columns.',
                'Columns and rows of figures = a table.',
                'A graph shows relationships visually.',
            ),
            'guidelines': ['Rows and columns = table.'],
        }, subskill='concepts', learning_objective_id=LO_VISUAL, question_family_id='table_definition', concept_id='tables', concept_group='visual', misconception_tags=['confuses_table_with_graph'], diagnostic_tags=['definition', 'visual']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Choose a visual aid',
            'prompt': 'A presenter wants the audience to compare sales figures across four years at a glance. Recommend a suitable visual aid and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend a graph (e.g. bar or line graph).',
                'A graph shows the relationship between sets of numbers visually.',
                'It lets the audience compare the four years at a glance.',
                'It is clearer than a table for spotting trends.',
            ],
            'sample_answer': 'A graph, such as a bar or line graph, is best because it shows the relationship between sets of numbers visually, letting the audience compare the four years\' sales at a glance and spot the trend more easily than a table would.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the goal to a visual aid.',
                'Comparing figures/trends at a glance favours a graph.',
                'Tables are better for exact figures than trends.',
            ),
            'answer_part_hints': ['Name the aid.', 'Motivate your choice.'],
            'guidelines': ['Tie the aid to the comparison goal.'],
            'teaching_note': 'Reward a graph with a motivation about comparison/trends.',
            'keywords': ['graph', 'compare', 'trend', 'figures', 'at a glance'],
        }, subskill='application', learning_objective_id=LO_VISUAL, question_family_id='choose_visual_aid_scenario', concept_id='visual_aids', concept_group='visual', scenario_family_id='sales_comparison', diagnostic_tags=['recommendation', 'visual'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Handle questions professionally',
            'prompt': 'After a presentation an audience member aggressively criticises the data. Recommend how the presenter should respond in a non-aggressive, professional manner. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Stay calm and listen to the full question without interrupting.',
                'Acknowledge the point respectfully; do not become defensive.',
                'Answer factually using evidence/data, or offer to follow up.',
                'Thank the person and keep the tone professional.',
            ],
            'sample_answer': 'The presenter should stay calm, listen to the full criticism without interrupting, and acknowledge the point respectfully rather than becoming defensive. They should answer factually using the data, or offer to follow up if needed, and thank the person, keeping the tone professional throughout.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on professional feedback handling.',
                'Stay calm, listen, acknowledge, respond with facts.',
                'Avoid being defensive or aggressive.',
            ),
            'answer_part_hints': ['Give the recommended behaviours.', 'Keep them professional.'],
            'guidelines': ['Recommendations must be non-aggressive and professional.'],
            'teaching_note': 'Reward calm, respectful, fact-based responses.',
            'keywords': ['calm', 'listen', 'acknowledge', 'facts', 'professional', 'not defensive'],
        }, subskill='application', learning_objective_id=LO_TYPES, question_family_id='handle_questions_scenario', concept_id='verbal_presentation', concept_group='types', scenario_family_id='aggressive_question', diagnostic_tags=['scenario_analysis', 'types'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Factors when preparing a presentation',
            'prompt': 'Discuss the factors a presenter must consider when preparing a presentation. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Know the audience and the purpose of the presentation.',
                'Plan and organise the content logically.',
                'Prepare suitable visual aids (slides, posters, handouts).',
                'Consider the venue, time and equipment available.',
                'Practise delivery, timing and how to handle questions.',
            ],
            'sample_answer': 'When preparing a presentation the presenter must know the audience and the purpose, plan and organise the content logically, and prepare suitable visual aids such as slides, posters and handouts. They should also consider the venue, time and equipment, and practise their delivery, timing and how to handle questions.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List preparation factors.',
                'Think audience, content, visual aids and venue.',
                'Practising delivery and Q&A also matters.',
            ),
            'answer_part_hints': ['Give several factors.', 'Explain each.'],
            'guidelines': ['Provide at least four factors.'],
            'teaching_note': 'Reward breadth across preparation factors.',
            'keywords': ['audience', 'purpose', 'content', 'visual aids', 'venue', 'practise'],
        }, subskill='discussion', learning_objective_id=LO_TYPES, question_family_id='preparation_factors_discussion', concept_id='verbal_presentation', concept_group='types', diagnostic_tags=['discussion', 'types'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Steps in report writing',
            'prompt': 'Outline the steps a business should follow in report writing. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Plan: define the purpose, scope and audience of the report.',
                'Gather and analyse the relevant information/data.',
                'Structure the report (introduction, body, findings, recommendations).',
                'Write clearly, then review/edit for accuracy and clarity.',
            ],
            'sample_answer': 'In report writing the business should first plan by defining the purpose, scope and audience, then gather and analyse the relevant information. Next it structures the report with an introduction, body, findings and recommendations, writes it clearly, and finally reviews and edits it for accuracy and clarity.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the report-writing steps in order.',
                'Plan, gather, structure, write, review.',
                'A report ends with findings and recommendations.',
            ),
            'answer_part_hints': ['Name each step.', 'Keep them in order.'],
            'guidelines': ['Provide the steps in a logical order.'],
            'teaching_note': 'Reward correct steps; order strengthens the answer.',
            'keywords': ['plan', 'purpose', 'gather', 'structure', 'write', 'review', 'recommendations'],
        }, subskill='discussion', learning_objective_id=LO_WRITTEN, question_family_id='report_writing_steps_discussion', concept_id='business_report', concept_group='written', diagnostic_tags=['discussion', 'written'], answer_structure_tags=['list', 'sequence'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
