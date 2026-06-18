"""Grade 12 Business Studies - Term 2 - Quality of performance.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g12_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade12_business_studies',
    subtopic_id='quality_of_performance',
    curriculum_reference='Term 2 > Quality of performance',
    id_prefix='g12_bs_quality',
)

LO_CONCEPTS = 'lo_quality_concepts'
LO_TQM = 'lo_tqm_elements'
LO_FUNCTIONS = 'lo_quality_functions'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Quality control',
            'prompt': 'Inspecting the final product to ensure it meets the required standards is …',
            'options': ['quality assurance', 'quality control', 'quality management', 'TQM'],
            'correct_index': 1,
            'explanation': 'Quality control ensures the desired quality is met by inspecting the final product against the required standards.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on inspecting the final product.',
                'Checking the finished product = quality control.',
                'Checks during the process = quality assurance.',
            ),
            'guidelines': ['Inspecting the final product = quality control.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='quality_control_definition', concept_id='quality_control', concept_group='concepts', misconception_tags=['confuses_control_with_assurance'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Quality assurance',
            'prompt': 'Checks carried out during and after the production process to prevent defects describe …',
            'options': ['quality control', 'quality assurance', 'quality performance', 'quality circle'],
            'correct_index': 1,
            'explanation': 'Quality assurance refers to checks carried out during and after the production process to prevent defects.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on preventing defects during production.',
                'Checks during the process = quality assurance.',
                'Inspecting the final product = quality control.',
            ),
            'guidelines': ['Checks during production = quality assurance.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='quality_assurance_definition', concept_id='quality_assurance', concept_group='concepts', misconception_tags=['confuses_assurance_with_control'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Total Quality Management',
            'prompt': 'An integrated, organisation-wide approach to consistently deliver quality products and services is …',
            'options': ['quality control', 'Total Quality Management (TQM)', 'a quality circle', 'benchmarking'],
            'correct_index': 1,
            'explanation': 'TQM is an integrated system applied throughout the organisation to design, produce and provide quality products and services to customers.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections(
                'Focus on the whole organisation.',
                'Organisation-wide quality approach = TQM.',
                'Quality control is just final inspection.',
            ),
            'guidelines': ['Organisation-wide quality system = TQM.'],
        }, subskill='concepts', learning_objective_id=LO_TQM, question_family_id='tqm_definition', concept_id='tqm', concept_group='tqm', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'TQM element',
            'prompt': 'Which of the following is a key element of TQM?',
            'options': ['Total client/customer satisfaction', 'Vertical integration', 'Market penetration', 'Affirmative action'],
            'correct_index': 0,
            'explanation': 'Total client/customer satisfaction is a key TQM element, along with continuous improvement, training, adequate financing and monitoring.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the TQM elements.',
                'Customer satisfaction is central to TQM.',
                'Integration/penetration are growth strategies.',
            ),
            'guidelines': ['Customer satisfaction = a TQM element.'],
        }, subskill='concepts', learning_objective_id=LO_TQM, question_family_id='tqm_element_identify', concept_id='tqm_elements', concept_group='tqm', diagnostic_tags=['identification']),
        with_metadata({
            'title': 'Quality circle',
            'prompt': 'A small group of employees who meet regularly to identify and solve quality problems is a …',
            'options': ['quality circle', 'bargaining council', 'board of directors', 'focus group'],
            'correct_index': 0,
            'explanation': 'A quality circle is a small group of employees who meet regularly to identify and solve quality-related problems as part of continuous improvement.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on employees solving quality problems together.',
                'Group solving quality problems = quality circle.',
                'A bargaining council deals with labour disputes.',
            ),
            'guidelines': ['Employee quality problem-solving group = quality circle.'],
        }, subskill='concepts', learning_objective_id=LO_TQM, question_family_id='quality_circle_definition', concept_id='quality_circle', concept_group='tqm', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Quality management',
            'prompt': 'The process of managing all activities needed to ensure consistently high standards is …',
            'options': ['quality performance', 'quality management', 'quality control', 'quality circle'],
            'correct_index': 1,
            'explanation': 'Quality management is the process of managing all activities needed to ensure a business produces products/services of consistently high standards.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on managing all quality activities.',
                'Managing all activities for high standards = quality management.',
                'Quality performance is measured output vs standards.',
            ),
            'guidelines': ['Managing all quality activities = quality management.'],
        }, subskill='concepts', learning_objective_id=LO_CONCEPTS, question_family_id='quality_management_definition', concept_id='quality_management', concept_group='concepts', misconception_tags=['confuses_management_with_performance'], diagnostic_tags=['definition']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Apply TQM elements',
            'prompt': 'A large manufacturer keeps losing customers because of defective products. Recommend how it could apply TQM elements to improve quality. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Continuous skills development: train employees to reduce errors.',
                'Total client/customer satisfaction: focus on meeting customer needs.',
                'Continuous improvement to processes and systems: refine production methods.',
                'Monitoring and evaluation: regularly check quality and adequate financing/capacity.',
            ],
            'sample_answer': 'The manufacturer should apply TQM by investing in continuous skills development to reduce errors, focusing on total customer satisfaction, continuously improving its processes and systems, and ensuring adequate financing and capacity while monitoring and evaluating quality regularly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Apply the TQM elements to defects.',
                'Training, customer focus, continuous improvement, monitoring.',
                'Tie each to reducing defects.',
            ),
            'answer_part_hints': ['Name the elements.', 'Apply each to the scenario.'],
            'guidelines': ['Apply TQM elements with actions.'],
            'teaching_note': 'Reward TQM elements applied to the defect problem.',
            'keywords': ['skills development', 'customer satisfaction', 'continuous improvement', 'monitoring', 'financing'],
        }, subskill='application', learning_objective_id=LO_TQM, question_family_id='apply_tqm_scenario', concept_id='tqm_elements', concept_group='tqm', scenario_family_id='defective_products', diagnostic_tags=['scenario_analysis', 'tqm'], answer_structure_tags=['recommend', 'apply'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Quality indicators for a function',
            'prompt': 'Explain how good quality in the marketing function could contribute to the success of a business. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Effective market research identifies customer needs accurately.',
                'Good advertising and promotion build a strong brand image.',
                'Reliable distribution gets products to customers on time.',
                'Strong after-sales service increases customer loyalty and repeat sales.',
            ],
            'sample_answer': 'Good quality in marketing means effective market research that identifies customer needs, advertising and promotion that build a strong brand image, reliable distribution that delivers on time, and strong after-sales service. Together these increase customer satisfaction, loyalty and repeat sales, contributing to business success.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on quality in marketing activities.',
                'Research, promotion, distribution, after-sales service.',
                'Link to customer satisfaction and success.',
            ),
            'answer_part_hints': ['Give quality indicators.', 'Link to success.'],
            'guidelines': ['Link marketing quality to success.'],
            'teaching_note': 'Reward marketing quality indicators linked to success.',
            'keywords': ['market research', 'advertising', 'distribution', 'after-sales', 'loyalty'],
        }, subskill='application', learning_objective_id=LO_FUNCTIONS, question_family_id='quality_function_scenario', concept_id='quality_performance', concept_group='functions', scenario_family_id='marketing_quality', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Benefits of a good quality management system',
            'prompt': 'Discuss the advantages of a good quality management system for a business. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Improves product/service quality and customer satisfaction.',
                'Reduces waste, defects and the cost of quality.',
                'Builds a strong reputation and competitive advantage.',
                'Increases productivity and employee involvement.',
                'Leads to greater profitability and long-term sustainability.',
            ],
            'sample_answer': 'A good quality management system improves product and service quality and customer satisfaction, reduces waste, defects and the cost of quality, and builds a strong reputation and competitive advantage. It also increases productivity and employee involvement, leading to greater profitability and long-term sustainability.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List the benefits.',
                'Think quality, cost, reputation, productivity, profit.',
                'Explain each briefly.',
            ),
            'answer_part_hints': ['List benefits.', 'Explain each.'],
            'guidelines': ['Provide several advantages.'],
            'teaching_note': 'Reward a range of advantages.',
            'keywords': ['customer satisfaction', 'reduce waste', 'reputation', 'productivity', 'profitability'],
        }, subskill='discussion', learning_objective_id=LO_CONCEPTS, question_family_id='qms_benefits_discussion', concept_id='quality_management', concept_group='concepts', diagnostic_tags=['discussion'], answer_structure_tags=['list', 'advantages'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Reduce the cost of quality',
            'prompt': 'Recommend ways in which a business can reduce the cost of quality. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Get things right the first time to avoid rework and waste.',
                'Train employees so they produce fewer defects.',
                'Use quality assurance to prevent defects during production.',
                'Maintain machinery to avoid breakdowns and defective output.',
                'Use quality circles and continuous improvement to refine processes.',
            ],
            'sample_answer': 'A business can reduce the cost of quality by getting things right the first time to avoid rework and waste, training employees to reduce defects, and using quality assurance to prevent defects during production. Maintaining machinery and using quality circles and continuous improvement to refine processes also lowers the overall cost of quality.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Focus on prevention over correction.',
                'Right first time, training, assurance, maintenance.',
                'Prevention reduces the cost of quality.',
            ),
            'answer_part_hints': ['Give recommendations.', 'Explain each.'],
            'guidelines': ['Provide several ways to reduce cost of quality.'],
            'teaching_note': 'Reward prevention-focused recommendations.',
            'keywords': ['right first time', 'training', 'assurance', 'maintenance', 'continuous improvement'],
        }, subskill='discussion', learning_objective_id=LO_TQM, question_family_id='cost_of_quality_discussion', concept_id='tqm', concept_group='tqm', diagnostic_tags=['discussion', 'recommendation'], answer_structure_tags=['recommend', 'list'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
