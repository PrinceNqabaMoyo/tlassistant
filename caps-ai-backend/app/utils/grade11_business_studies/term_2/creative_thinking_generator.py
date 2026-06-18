"""Grade 11 Business Studies - Term 2 - Topic 8: Creative thinking and problem
solving.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='creative_thinking',
    curriculum_reference='Term 2 > Creative thinking and problem solving',
    id_prefix='g11_bs_creative',
)

LO_CREATIVE = 'lo_creative_thinking'
LO_PROBLEM = 'lo_problem_solving'
LO_TECHNIQUES = 'lo_problem_solving_techniques'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Creative thinking',
            'prompt': 'The ability to think of original, diverse or new ideas that can be applied to situations requiring solutions is …',
            'options': ['routine thinking', 'creative thinking', 'problem-solving', 'brainstorming'],
            'correct_index': 1,
            'explanation': 'Creative thinking is the ability to think of original, diverse or new ideas that can be applied to situations requiring solutions.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the source of new ideas.',
                'Creative thinking generates original, new ideas.',
                'Routine thinking repeats the same steps each time.',
            ),
            'guidelines': ['Link "original/new ideas" to creative thinking.'],
        }, subskill='concepts', learning_objective_id=LO_CREATIVE, question_family_id='creative_thinking_definition', concept_id='creative_thinking', concept_group='creative_thinking', misconception_tags=['confuses_creative_with_routine'], diagnostic_tags=['definition', 'creativity']),
        with_metadata({
            'title': 'Routine thinking',
            'prompt': 'A series of steps of doing things in the same way each time is called …',
            'options': ['creative thinking', 'routine thinking', 'lateral thinking', 'mind mapping'],
            'correct_index': 1,
            'explanation': 'Routine thinking is a series of steps of doing things in the same way.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify repeating the same approach.',
                'Routine thinking follows the same steps each time.',
                'It is the opposite of creative thinking.',
            ),
            'guidelines': ['Link "same way each time" to routine thinking.'],
        }, subskill='concepts', learning_objective_id=LO_CREATIVE, question_family_id='routine_thinking_definition', concept_id='routine_thinking', concept_group='creative_thinking', misconception_tags=['confuses_routine_with_creative'], diagnostic_tags=['definition', 'creativity']),
        with_metadata({
            'title': 'Conventional vs non-conventional',
            'prompt': 'Solutions obtained through using creative thinking (rather than the expected response) are called …',
            'options': ['conventional solutions', 'non-conventional solutions', 'routine solutions', 'standard solutions'],
            'correct_index': 1,
            'explanation': 'Non-conventional solutions are solutions obtained through using creative thinking, unlike conventional (expected) solutions.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish expected from creative solutions.',
                'Non-conventional solutions come from creative thinking.',
                'Conventional solutions are the expected responses.',
            ),
            'guidelines': ['Creative = non-conventional.'],
        }, subskill='concepts', learning_objective_id=LO_CREATIVE, question_family_id='nonconventional_definition', concept_id='non_conventional_solutions', concept_group='creative_thinking', misconception_tags=['confuses_conventional_with_nonconventional'], diagnostic_tags=['definition', 'creativity']),
        with_metadata({
            'title': 'Force Field Analysis',
            'prompt': 'A framework based on the assumption that there are forces for and against that influence a situation is called …',
            'options': ['Delphi Technique', 'Force Field Analysis', 'brainstorming', 'mind mapping'],
            'correct_index': 1,
            'explanation': 'Force Field Analysis is a framework based on the assumption that there are forces for and against that influence a situation.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the technique weighing forces.',
                'Force Field Analysis weighs driving vs restraining forces.',
                'The Delphi Technique uses expert questionnaires instead.',
            ),
            'guidelines': ['Forces for/against = Force Field Analysis.'],
        }, subskill='concepts', learning_objective_id=LO_TECHNIQUES, question_family_id='force_field_definition', concept_id='force_field_analysis', concept_group='techniques', misconception_tags=['confuses_force_field_with_delphi'], diagnostic_tags=['definition', 'techniques']),
        with_metadata({
            'title': 'Delphi Technique',
            'prompt': 'A problem-solving technique that gathers and refines the opinions of experts using questionnaires is the …',
            'options': ['Force Field Analysis', 'Delphi Technique', 'SWOT analysis', 'mind mapping'],
            'correct_index': 1,
            'explanation': 'The Delphi Technique gathers and refines the opinions of a panel of experts (often anonymously) using questionnaires until consensus is reached.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the technique using experts.',
                'The Delphi Technique relies on expert questionnaires.',
                'Force Field Analysis weighs forces instead.',
            ),
            'guidelines': ['Expert questionnaires = Delphi Technique.'],
        }, subskill='concepts', learning_objective_id=LO_TECHNIQUES, question_family_id='delphi_definition', concept_id='delphi_technique', concept_group='techniques', misconception_tags=['confuses_delphi_with_force_field'], diagnostic_tags=['definition', 'techniques']),
        with_metadata({
            'title': 'Problem-solving',
            'prompt': 'The skills and abilities that individuals use to solve problems within a given time frame are called …',
            'options': ['creative thinking', 'problem-solving skills', 'routine thinking', 'risk bearing'],
            'correct_index': 1,
            'explanation': 'Problem-solving skills are the skills and abilities that individuals use to solve problems within a given time frame.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the skill set for solving problems.',
                'Problem-solving applies skills to reach a solution in time.',
                'Creative thinking generates the ideas behind solutions.',
            ),
            'guidelines': ['Link "solve problems in a time frame" to problem-solving.'],
        }, subskill='concepts', learning_objective_id=LO_PROBLEM, question_family_id='problem_solving_definition', concept_id='problem_solving', concept_group='problem_solving', misconception_tags=['confuses_problem_solving_with_creativity'], diagnostic_tags=['definition', 'problem_solving']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply a problem-solving technique',
            'prompt': 'A business must decide whether to introduce a new shift system. There are clear pressures for and against the change. Recommend a suitable problem-solving technique and explain how it would be applied. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend Force Field Analysis.',
                'List the driving forces (for the change).',
                'List the restraining forces (against the change).',
                'Compare/weigh the forces to decide whether to proceed.',
            ],
            'sample_answer': 'The business should use Force Field Analysis. It would list the driving forces for the new shift system and the restraining forces against it, then weigh the two sets of forces to decide whether the change should go ahead.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the situation to a technique.',
                'Forces for and against signal Force Field Analysis.',
                'Application means listing and weighing the forces.',
            ),
            'answer_part_hints': ['Name the technique.', 'Explain how to apply it.'],
            'guidelines': ['Apply, do not just define.'],
            'teaching_note': 'Reward naming Force Field Analysis AND applying it.',
            'keywords': ['force field analysis', 'driving forces', 'restraining forces', 'weigh', 'decide'],
        }, subskill='application', learning_objective_id=LO_TECHNIQUES, question_family_id='apply_technique_scenario', concept_id='force_field_analysis', concept_group='techniques', scenario_family_id='shift_system_change', diagnostic_tags=['scenario_analysis', 'techniques'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Identify the type of solution',
            'prompt': 'Instead of advertising in the usual way, a small bakery sells "mystery boxes" of surplus stock through a social media auction. Identify whether this is a conventional or non-conventional solution and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is a non-conventional solution.',
                'It uses creative thinking rather than the expected response.',
                'It is original/new (mystery boxes via social media auction).',
                'It solves the surplus-stock problem in an unexpected way.',
            ],
            'sample_answer': 'This is a non-conventional solution because it uses creative thinking instead of the expected advertising response. Selling surplus stock as mystery boxes through a social media auction is an original, unexpected way to solve the problem.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Decide if the idea is expected or creative.',
                'Unexpected, original ideas are non-conventional.',
                'Conventional solutions are the predictable responses.',
            ),
            'answer_part_hints': ['Classify the solution.', 'Motivate your choice.'],
            'guidelines': ['Use scenario evidence.'],
            'teaching_note': 'Reward correct classification plus motivation.',
            'keywords': ['non-conventional', 'creative', 'original', 'unexpected', 'social media'],
        }, subskill='application', learning_objective_id=LO_CREATIVE, question_family_id='classify_solution_scenario', concept_id='non_conventional_solutions', concept_group='creative_thinking', scenario_family_id='bakery_mystery_box', diagnostic_tags=['scenario_analysis', 'creativity'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Benefits of creative thinking',
            'prompt': 'Explain the benefits of creative thinking in the workplace. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Generates new ideas, products and improvements (innovation).',
                'Gives the business a competitive advantage.',
                'Solves problems in non-conventional, effective ways.',
                'Improves efficiency and motivates/engages employees.',
            ],
            'sample_answer': 'Creative thinking generates new ideas, products and improvements, giving the business a competitive advantage. It allows problems to be solved in non-conventional, effective ways, improves efficiency, and motivates and engages employees who feel their ideas are valued.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List benefits of creativity at work.',
                'Think innovation, competitiveness and problem-solving.',
                'Creativity also boosts efficiency and morale.',
            ),
            'answer_part_hints': ['Give several benefits.', 'Explain each.'],
            'guidelines': ['Provide at least three benefits.'],
            'teaching_note': 'Reward distinct, workplace-linked benefits.',
            'keywords': ['creative thinking', 'innovation', 'competitive advantage', 'problem-solving', 'efficiency', 'motivation'],
        }, subskill='discussion', learning_objective_id=LO_CREATIVE, question_family_id='benefits_creative_thinking_discussion', concept_id='creative_thinking', concept_group='creative_thinking', diagnostic_tags=['discussion', 'creativity'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Advantages of solving problems with others',
            'prompt': 'Explain the advantages of working with others (collaboration) to solve business problems. (6 marks)',
            'marks': 6,
            'marking_points': [
                'A wider range of ideas, skills and perspectives is available.',
                'Better-quality decisions through shared knowledge.',
                'Shared workload and responsibility for the solution.',
                'Greater buy-in/commitment to implementing the solution.',
            ],
            'sample_answer': 'Working with others to solve problems brings a wider range of ideas, skills and perspectives, which leads to better-quality decisions through shared knowledge. It shares the workload and responsibility, and creates greater buy-in and commitment to implementing the chosen solution.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List benefits of collaboration.',
                'More people = more ideas and skills.',
                'Collaboration also builds buy-in for the solution.',
            ),
            'answer_part_hints': ['Give several advantages.', 'Explain each.'],
            'guidelines': ['Provide at least three advantages.'],
            'teaching_note': 'Reward distinct advantages of group problem-solving.',
            'keywords': ['collaboration', 'ideas', 'skills', 'perspectives', 'decisions', 'buy-in'],
        }, subskill='discussion', learning_objective_id=LO_PROBLEM, question_family_id='collaboration_advantages_discussion', concept_id='problem_solving', concept_group='problem_solving', diagnostic_tags=['discussion', 'problem_solving'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
