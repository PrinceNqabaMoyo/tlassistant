"""Grade 12 Business Studies - Term 3 - Presentation and data responses.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='presentation_data_responses',
    curriculum_reference='Term 3 > Presentation and data responses',
    id_prefix='g12_bs_presentation',
)

LO_PREPARE = 'lo_prepare_presentation'
LO_FEEDBACK = 'lo_handle_feedback'
LO_VISUAL = 'lo_visual_aids'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Verbal vs non-verbal presentation',
            'prompt': 'A written report and a pie chart are examples of … presentations.',
            'options': ['verbal', 'non-verbal', 'spoken', 'interactive'],
            'correct_index': 1,
            'explanation': 'Non-verbal presentations convey information without spoken words, e.g. written reports, graphs, pictures and photographs.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on information without spoken words.',
                'Reports and charts = non-verbal presentations.',
                'A spoken talk is a verbal presentation.',
            ),
            'guidelines': ['Reports/charts = non-verbal presentation.'],
        }, subskill='concepts', learning_objective_id=LO_PREPARE, question_family_id='non_verbal_identify', concept_id='non_verbal', concept_group='types', misconception_tags=['confuses_verbal_with_non_verbal'], diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Preparation factor',
            'prompt': 'Which factor should be considered BEFORE a presentation?',
            'options': [
                'Maintain eye contact with the audience',
                'Research the audience and prepare the content',
                'Speak slowly and use pauses',
                'Answer questions calmly',
            ],
            'correct_index': 1,
            'explanation': 'Before a presentation, the presenter should research the audience, prepare and organise the content, and rehearse.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on what happens before presenting.',
                'Researching the audience/preparing content = before.',
                'Eye contact and pauses happen during.',
            ),
            'guidelines': ['Researching/preparing = before the presentation.'],
        }, subskill='concepts', learning_objective_id=LO_PREPARE, question_family_id='before_factor_identify', concept_id='preparation', concept_group='prepare', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'During the presentation',
            'prompt': 'Which factor should the presenter focus on DURING the presentation?',
            'options': [
                'Prepare the venue',
                'Research the audience',
                'Maintain eye contact and not speak too fast',
                'Design the slides',
            ],
            'correct_index': 2,
            'explanation': 'During the presentation the presenter should maintain eye contact, use visual aids effectively, use pauses and not speak too fast.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on delivery while presenting.',
                'Eye contact/pacing = during the presentation.',
                'Designing slides happens before.',
            ),
            'guidelines': ['Eye contact/pacing = during the presentation.'],
        }, subskill='concepts', learning_objective_id=LO_PREPARE, question_family_id='during_factor_identify', concept_id='delivery', concept_group='prepare', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Visual aid: data projector',
            'prompt': 'A PowerPoint slideshow displayed with a data projector is most suited to …',
            'options': [
                'a small one-on-one meeting only',
                'presenting visual information to a large audience',
                'recording financial transactions',
                'conducting an interview',
            ],
            'correct_index': 1,
            'explanation': 'A PowerPoint/data projector is well suited to presenting visual information to a large audience clearly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a large audience and visuals.',
                'PowerPoint/projector suits large audiences.',
                'It is not for recording transactions.',
            ),
            'guidelines': ['PowerPoint/projector = large audience visuals.'],
        }, subskill='concepts', learning_objective_id=LO_VISUAL, question_family_id='projector_identify', concept_id='data_projector', concept_group='visual', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Handling questions',
            'prompt': 'When responding to a hostile question after a presentation, the presenter should …',
            'options': [
                'argue back aggressively',
                'remain calm and answer professionally',
                'ignore the question',
                'end the presentation immediately',
            ],
            'correct_index': 1,
            'explanation': 'The presenter should remain calm and answer questions in a non-aggressive, professional manner.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on staying professional.',
                'Calm, professional response is correct.',
                'Arguing or ignoring is unprofessional.',
            ),
            'guidelines': ['Stay calm and professional.'],
        }, subskill='concepts', learning_objective_id=LO_FEEDBACK, question_family_id='questions_identify', concept_id='handle_questions', concept_group='feedback', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Multimedia presentation',
            'prompt': 'A presentation that combines sound, video and text is a … presentation.',
            'options': ['verbal', 'multimedia', 'printed', 'telephonic'],
            'correct_index': 1,
            'explanation': 'A multimedia presentation infuses sound and video into a presentation alongside text and images.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on combining several media.',
                'Sound + video + text = multimedia.',
                'A printed report is non-verbal only.',
            ),
            'guidelines': ['Sound + video + text = multimedia.'],
        }, subskill='concepts', learning_objective_id=LO_VISUAL, question_family_id='multimedia_identify', concept_id='multimedia', concept_group='visual', diagnostic_tags=['identification']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Prepare for a presentation',
            'prompt': 'A manager must present quarterly results to the board next week. Recommend the factors they should consider when preparing for the presentation. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Research the audience (the board) and their expectations.',
                'Prepare, organise and structure the content logically.',
                'Prepare clear visual aids such as graphs and slides.',
                'Rehearse the presentation and prepare for likely questions.',
            ],
            'sample_answer': 'The manager should research the board and their expectations, prepare and organise the content logically, and prepare clear visual aids such as graphs and slides. They should also rehearse the presentation and anticipate likely questions so they can respond confidently.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on preparation factors.',
                'Audience, content, visual aids, rehearsal.',
                'Tie each to the board presentation.',
            ),
            'answer_part_hints': ['List preparation factors.', 'Explain each.'],
            'guidelines': ['Provide preparation factors.'],
            'teaching_note': 'Reward preparation factors applied to the scenario.',
            'keywords': ['research audience', 'prepare content', 'visual aids', 'rehearse', 'questions'],
        }, subskill='application', learning_objective_id=LO_PREPARE, question_family_id='prepare_scenario', concept_id='preparation', concept_group='prepare', scenario_family_id='board_results', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['recommend'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Handle feedback professionally',
            'prompt': 'During a presentation an audience member aggressively challenges the presenter\u2019s figures. Recommend how the presenter should handle this feedback in a non-aggressive, professional manner. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Remain calm and listen to the full question without interrupting.',
                'Acknowledge the concern and respond politely.',
                'Provide a clear, factual answer or offer to verify and follow up.',
                'Do not take it personally or become defensive.',
            ],
            'sample_answer': 'The presenter should remain calm and listen to the full question without interrupting, acknowledge the concern and respond politely. They should give a clear, factual answer or offer to verify the figures and follow up, without becoming defensive or taking the challenge personally.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a calm, professional response.',
                'Listen, acknowledge, answer factually, stay calm.',
                'Offer to follow up if unsure.',
            ),
            'answer_part_hints': ['List the steps.', 'Keep it professional.'],
            'guidelines': ['Provide professional feedback-handling steps.'],
            'teaching_note': 'Reward calm, professional handling steps.',
            'keywords': ['calm', 'listen', 'acknowledge', 'factual', 'follow up'],
        }, subskill='application', learning_objective_id=LO_FEEDBACK, question_family_id='handle_feedback_scenario', concept_id='handle_questions', concept_group='feedback', scenario_family_id='hostile_question', diagnostic_tags=['scenario_analysis', 'feedback'], answer_structure_tags=['recommend'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of visual aids',
            'prompt': 'Discuss the impact of using visual aids such as a data projector and handouts in a presentation. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Data projector: displays visuals clearly to a large audience and keeps attention.',
                'It makes complex data easier to understand through graphs and images.',
                'Handouts: give the audience a record to refer to afterwards.',
                'Handouts allow note-taking and reinforce the key points.',
                'Poorly designed visual aids can distract or confuse the audience.',
            ],
            'sample_answer': 'A data projector displays visuals clearly to a large audience, keeps their attention and makes complex data easier to understand through graphs and images. Handouts give the audience a record to refer to afterwards, allow note-taking and reinforce the key points. However, if visual aids are poorly designed or overloaded, they can distract or confuse the audience.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Discuss the impact of each visual aid.',
                'Projector (clarity/attention) and handouts (record/notes).',
                'Mention a drawback of poor design.',
            ),
            'answer_part_hints': ['Discuss the projector.', 'Discuss handouts.'],
            'guidelines': ['Cover impact of at least two visual aids.'],
            'teaching_note': 'Reward impact of each visual aid plus a drawback.',
            'keywords': ['projector', 'large audience', 'handouts', 'record', 'distract'],
        }, subskill='discussion', learning_objective_id=LO_VISUAL, question_family_id='visual_aids_discussion', concept_id='data_projector', concept_group='visual', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['explain', 'evaluate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Areas of improvement',
            'prompt': 'After a weak presentation, recommend areas the presenter could improve for the next presentation. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Prepare and rehearse more thoroughly beforehand.',
                'Improve the design and clarity of visual aids.',
                'Manage time better and keep to the point.',
                'Improve delivery: eye contact, pacing and confidence.',
                'Prepare better for audience questions and feedback.',
            ],
            'sample_answer': 'For the next presentation the presenter should prepare and rehearse more thoroughly, improve the design and clarity of the visual aids, and manage time better by keeping to the point. They should also improve delivery through eye contact, pacing and confidence, and prepare better for audience questions and feedback.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on areas to improve.',
                'Preparation, visuals, time, delivery, questions.',
                'Explain each improvement.',
            ),
            'answer_part_hints': ['List areas.', 'Explain each.'],
            'guidelines': ['Provide several improvement areas.'],
            'teaching_note': 'Reward practical improvement areas.',
            'keywords': ['rehearse', 'visual aids', 'time', 'delivery', 'questions'],
        }, subskill='discussion', learning_objective_id=LO_FEEDBACK, question_family_id='improvement_discussion', concept_id='preparation', concept_group='prepare', diagnostic_tags=['discussion', 'recommendation'], answer_structure_tags=['recommend', 'list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
