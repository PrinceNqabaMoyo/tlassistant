"""Grade 12 Business Studies - Term 1 - Creative thinking and problem-solving.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='creative_thinking_problem_solving',
    curriculum_reference='Term 1 > Creative thinking and problem-solving',
    id_prefix='g12_bs_creative',
)

LO_PROBLEM = 'lo_problem_solving'
LO_TECHNIQUES = 'lo_problem_solving_techniques'
LO_CREATIVE = 'lo_creative_thinking'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Problem-solving',
            'prompt': 'The process of gathering the facts necessary to overcome a specific challenge is called …',
            'options': ['decision-making', 'problem-solving', 'brainstorming', 'delegation'],
            'correct_index': 1,
            'explanation': 'Problem-solving is the process of gathering the facts that are necessary to overcome a specific challenge.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on gathering facts to overcome a challenge.',
                'Working through a problem with facts = problem-solving.',
                'Decision-making is choosing between alternatives.',
            ),
            'guidelines': ['Gathering facts to overcome a challenge = problem-solving.'],
        }, subskill='concepts', learning_objective_id=LO_PROBLEM, question_family_id='problem_solving_definition', concept_id='problem_solving', concept_group='problem', misconception_tags=['confuses_problem_solving_with_decision_making'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Decision-making',
            'prompt': 'Considering various alternatives before choosing the best one — often done by one person/senior management — describes …',
            'options': ['problem-solving', 'decision-making', 'creative thinking', 'forecasting'],
            'correct_index': 1,
            'explanation': 'Decision-making considers various alternatives before deciding on the best one and is often more authoritative (done by one person/senior management).',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on choosing between alternatives.',
                'Selecting the best alternative = decision-making.',
                'Problem-solving is more inclusive/group-based.',
            ),
            'guidelines': ['Choosing the best alternative = decision-making.'],
        }, subskill='concepts', learning_objective_id=LO_PROBLEM, question_family_id='decision_making_definition', concept_id='decision_making', concept_group='problem', misconception_tags=['confuses_decision_making_with_problem_solving'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Delphi Technique',
            'prompt': 'A panel of experts is consulted individually through questionnaires until consensus is reached. This problem-solving technique is the …',
            'options': ['Nominal Group Technique', 'Delphi Technique', 'Force Field Analysis', 'Brainstorming'],
            'correct_index': 1,
            'explanation': 'The Delphi Technique consults a panel of experts (often individually via questionnaires) until consensus is reached.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on a panel of experts and questionnaires.',
                'Experts consulted until consensus = Delphi Technique.',
                'Force Field Analysis weighs forces for and against.',
            ),
            'guidelines': ['Panel of experts to consensus = Delphi Technique.'],
        }, subskill='concepts', learning_objective_id=LO_TECHNIQUES, question_family_id='delphi_definition', concept_id='delphi_technique', concept_group='techniques', misconception_tags=['confuses_delphi_with_nominal_group'], diagnostic_tags=['definition', 'techniques']),
        with_metadata({
            'title': 'Force Field Analysis',
            'prompt': 'A technique that identifies the forces driving and resisting a change before making a decision is …',
            'options': ['Force Field Analysis', 'Brainstorming', 'Delphi Technique', 'SWOT analysis'],
            'correct_index': 0,
            'explanation': 'Force Field Analysis identifies and weighs the driving forces (for) against the restraining forces (against) a change.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on forces for and against a change.',
                'Weighing driving vs restraining forces = Force Field Analysis.',
                'Brainstorming just generates many ideas quickly.',
            ),
            'guidelines': ['Forces for vs against = Force Field Analysis.'],
        }, subskill='concepts', learning_objective_id=LO_TECHNIQUES, question_family_id='force_field_definition', concept_id='force_field_analysis', concept_group='techniques', misconception_tags=['confuses_force_field_with_brainstorming'], diagnostic_tags=['definition', 'techniques']),
        with_metadata({
            'title': 'Nominal Group Technique',
            'prompt': 'Group members independently write down ideas, which are then shared, discussed and ranked. This technique is the …',
            'options': ['Brainstorming', 'Nominal Group Technique', 'Delphi Technique', 'Force Field Analysis'],
            'correct_index': 1,
            'explanation': 'The Nominal Group Technique has members generate ideas independently, then share, discuss and rank them to reach a decision.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on individual ideas that are then ranked.',
                'Independent ideas shared then ranked = Nominal Group Technique.',
                'Delphi keeps experts anonymous via questionnaires.',
            ),
            'guidelines': ['Independent ideas then ranked = Nominal Group Technique.'],
        }, subskill='concepts', learning_objective_id=LO_TECHNIQUES, question_family_id='nominal_group_definition', concept_id='nominal_group_technique', concept_group='techniques', misconception_tags=['confuses_nominal_group_with_brainstorming'], diagnostic_tags=['definition', 'techniques']),
        with_metadata({
            'title': 'Creative thinking',
            'prompt': 'The ability to look at the same challenge and come up with original, new, innovative ideas is …',
            'options': ['routine thinking', 'creative thinking', 'critical analysis', 'decision-making'],
            'correct_index': 1,
            'explanation': 'Creative thinking is the ability to look at the same scenario/challenge and come up with original, new, innovative ideas/solutions.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on original and innovative ideas.',
                'New, original ideas for the same problem = creative thinking.',
                'Routine thinking repeats the usual steps.',
            ),
            'guidelines': ['Original/innovative ideas = creative thinking.'],
        }, subskill='concepts', learning_objective_id=LO_CREATIVE, question_family_id='creative_thinking_definition', concept_id='creative_thinking', concept_group='creative', misconception_tags=['confuses_creative_with_routine'], diagnostic_tags=['definition', 'creative']),
        with_metadata({
            'title': 'First step in problem-solving',
            'prompt': 'Which is the FIRST step in the problem-solving process?',
            'options': ['Implement the solution', 'Identify the problem', 'Evaluate the outcome', 'Generate alternatives'],
            'correct_index': 1,
            'explanation': 'The first step is to identify the problem — acknowledge that a problem exists before it can be solved.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Think about what must happen before solving.',
                'You must first recognise the problem exists.',
                'Implementation and evaluation come later.',
            ),
            'guidelines': ['Identify the problem is the first step.'],
        }, subskill='concepts', learning_objective_id=LO_PROBLEM, question_family_id='problem_solving_steps', concept_id='problem_solving', concept_group='problem', diagnostic_tags=['process']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify and apply a technique',
            'prompt': 'BizCo gathers anonymous written opinions from a panel of industry experts over several rounds until they agree on a forecast. Name the problem-solving technique and explain how BizCo applies it. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The technique is the Delphi Technique.',
                'A panel of experts is consulted (often anonymously).',
                'Opinions are gathered through several rounds of questionnaires.',
                'The process continues until the experts reach consensus.',
            ],
            'sample_answer': 'BizCo is using the Delphi Technique. It consults a panel of industry experts anonymously through several rounds of questionnaires, refining the responses each round until the experts reach consensus on the forecast.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the scenario clues to a technique.',
                'Anonymous experts + rounds + consensus = Delphi Technique.',
                'Describe how the rounds reach consensus.',
            ),
            'answer_part_hints': ['Name the technique.', 'Explain the application.'],
            'guidelines': ['Identify Delphi and explain the rounds to consensus.'],
            'teaching_note': 'Reward naming Delphi plus the consensus-by-rounds process.',
            'keywords': ['delphi', 'experts', 'questionnaire', 'rounds', 'consensus'],
        }, subskill='application', learning_objective_id=LO_TECHNIQUES, question_family_id='identify_technique_scenario', concept_id='delphi_technique', concept_group='techniques', scenario_family_id='forecast_panel', diagnostic_tags=['scenario_analysis', 'techniques'], answer_structure_tags=['identify', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Apply the problem-solving steps',
            'prompt': 'Staff morale at a factory has dropped sharply. Apply the problem-solving steps the manager should follow to address this. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Identify and define the problem (low morale) and its causes.',
                'Gather relevant information from affected staff.',
                'Generate and evaluate possible solutions/alternatives.',
                'Choose, implement and then evaluate the chosen solution.',
            ],
            'sample_answer': 'The manager should first identify and define the problem of low morale and gather information from staff about its causes. They should then generate possible solutions, evaluate the alternatives, choose and implement the best one, and finally evaluate whether morale has improved.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Walk through the problem-solving cycle.',
                'Identify, gather info, generate/evaluate options, implement, review.',
                'End by checking whether the problem is solved.',
            ),
            'answer_part_hints': ['List the steps in order.', 'Tie them to the morale problem.'],
            'guidelines': ['Apply the steps to the morale scenario.'],
            'teaching_note': 'Reward correctly ordered steps applied to the scenario.',
            'keywords': ['identify', 'gather information', 'alternatives', 'implement', 'evaluate'],
        }, subskill='application', learning_objective_id=LO_PROBLEM, question_family_id='apply_steps_scenario', concept_id='problem_solving', concept_group='problem', scenario_family_id='low_morale', diagnostic_tags=['scenario_analysis', 'process'], answer_structure_tags=['apply', 'sequence'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Impact of problem-solving techniques',
            'prompt': 'Discuss the positives and negatives of using the Nominal Group Technique to solve complex business problems. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Positive: all members contribute, reducing the dominance of one person.',
                'Positive: ideas are ranked, so the best ideas are prioritised.',
                'Positive: it limits conflict because ideas are first generated independently.',
                'Negative: it is time-consuming to gather and rank all ideas.',
                'Negative: it requires a skilled facilitator to run effectively.',
            ],
            'sample_answer': 'The Nominal Group Technique lets every member contribute ideas independently, reducing the dominance of strong personalities and limiting conflict, and ranking ensures the best ideas are prioritised. However, it can be time-consuming to gather and rank all the ideas and needs a skilled facilitator to run effectively.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Give both positives and negatives.',
                'Think participation/ranking (positives) vs time/facilitation (negatives).',
                'Balance the discussion across both sides.',
            ),
            'answer_part_hints': ['Give positives.', 'Give negatives.'],
            'guidelines': ['Provide both positives and negatives.'],
            'teaching_note': 'Reward a balanced discussion of positives and negatives.',
            'keywords': ['participation', 'ranked', 'conflict', 'time-consuming', 'facilitator'],
        }, subskill='discussion', learning_objective_id=LO_TECHNIQUES, question_family_id='technique_impact_discussion', concept_id='nominal_group_technique', concept_group='techniques', diagnostic_tags=['discussion', 'evaluation'], answer_structure_tags=['positives', 'negatives'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Promote creative thinking',
            'prompt': 'Recommend ways in which a business can create an environment that promotes creative thinking in the workplace. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Encourage and reward new ideas without fear of criticism.',
                'Allow employees freedom and time to experiment.',
                'Use brainstorming and other techniques to generate ideas.',
                'Create a diverse team that brings different perspectives.',
                'Provide resources and training that support innovation.',
            ],
            'sample_answer': 'A business can promote creative thinking by encouraging and rewarding new ideas without fear of criticism, allowing employees freedom and time to experiment, and using techniques such as brainstorming. Building diverse teams and providing supporting resources and training also helps generate innovative solutions.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Think about culture, freedom and rewards.',
                'A safe, rewarding, diverse environment fosters creativity.',
                'Techniques and resources support idea generation.',
            ),
            'answer_part_hints': ['Give several ways.', 'Explain each briefly.'],
            'guidelines': ['Provide at least four recommendations.'],
            'teaching_note': 'Reward practical ways to foster creativity.',
            'keywords': ['reward ideas', 'freedom', 'brainstorming', 'diverse', 'training'],
        }, subskill='discussion', learning_objective_id=LO_CREATIVE, question_family_id='promote_creativity_discussion', concept_id='creative_thinking', concept_group='creative', diagnostic_tags=['discussion', 'recommendation'], answer_structure_tags=['recommend', 'list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
