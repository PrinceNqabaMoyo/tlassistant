"""Grade 11 Business Studies - Term 2 - Topic 11: The production function.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='production_function',
    curriculum_reference='Term 2 > The production function',
    id_prefix='g11_bs_production',
)

LO_METHODS = 'lo_production_methods'
LO_PLANNING = 'lo_production_planning_control'
LO_SAFETY = 'lo_workplace_safety'
LO_QUALITY = 'lo_quality_control'
LO_COSTS = 'lo_production_costs'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Mass production',
            'prompt': 'Producing large quantities of identical/standardised products continuously is called …',
            'options': ['job production', 'batch production', 'mass production', 'custom production'],
            'correct_index': 2,
            'explanation': 'Mass production is the continuous production of large quantities of identical/standardised products.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the description to a method.',
                'Large quantities of identical products = mass production.',
                'Job production makes one unique item at a time.',
            ),
            'guidelines': ['Large, identical quantities = mass production.'],
        }, subskill='concepts', learning_objective_id=LO_METHODS, question_family_id='mass_production_definition', concept_id='mass_production', concept_group='methods', misconception_tags=['confuses_mass_with_batch'], diagnostic_tags=['definition', 'production_methods']),
        with_metadata({
            'title': 'Job production',
            'prompt': 'Producing a single, unique product to a customer\'s specific requirements (e.g. a tailored wedding dress) is called …',
            'options': ['mass production', 'job production', 'batch production', 'flow production'],
            'correct_index': 1,
            'explanation': 'Job production is making a single, unique product to a customer\'s specific requirements.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the description to a method.',
                'One unique, customised item = job production.',
                'Batch production makes groups of identical items.',
            ),
            'guidelines': ['One unique item = job production.'],
        }, subskill='concepts', learning_objective_id=LO_METHODS, question_family_id='job_production_definition', concept_id='job_production', concept_group='methods', misconception_tags=['confuses_job_with_mass'], diagnostic_tags=['definition', 'production_methods']),
        with_metadata({
            'title': 'Production planning',
            'prompt': 'The plan used in the production process that decreases cost and time and increases output is called …',
            'options': ['production control', 'production planning', 'quality control', 'scheduling'],
            'correct_index': 1,
            'explanation': 'Production planning is the plan used in the production process to decrease cost and time and increase output.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish planning from control.',
                'Planning sets out how to reduce cost/time and raise output.',
                'Control manages each task while production happens.',
            ),
            'guidelines': ['The upfront plan = production planning.'],
        }, subskill='concepts', learning_objective_id=LO_PLANNING, question_family_id='production_planning_definition', concept_id='production_planning', concept_group='planning_control', misconception_tags=['confuses_planning_with_control'], diagnostic_tags=['definition', 'planning']),
        with_metadata({
            'title': 'Occupational Health and Safety Act',
            'prompt': 'Which Act outlines the health and safety roles and responsibilities of all stakeholders in the workplace?',
            'options': [
                'Labour Relations Act (No. 66 of 1995)',
                'Occupational Health and Safety Act (No. 85 of 1993)',
                'Companies Act (No. 71 of 2008)',
                'Consumer Protection Act',
            ],
            'correct_index': 1,
            'explanation': 'The Occupational Health and Safety Act (No. 85 of 1993) outlines the health and safety roles and responsibilities of all stakeholders.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match safety to the correct Act.',
                'Workplace safety is governed by the OHSA (No. 85 of 1993).',
                'The LRA governs industrial relations instead.',
            ),
            'guidelines': ['Workplace safety = OHSA.'],
        }, subskill='concepts', learning_objective_id=LO_SAFETY, question_family_id='ohsa_identification', concept_id='ohsa', concept_group='safety', misconception_tags=['confuses_ohsa_with_lra'], diagnostic_tags=['legislation', 'safety']),
        with_metadata({
            'title': 'Quality control',
            'prompt': 'The inspection of the final product to ensure that it meets the required standards is called …',
            'options': ['quality control', 'production planning', 'scheduling', 'dispatching'],
            'correct_index': 0,
            'explanation': 'Quality control includes the inspection of the final product to ensure that it meets the required standards.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify inspecting the final product.',
                'Quality control inspects the finished product.',
                'TQM is a broader system covering all processes.',
            ),
            'guidelines': ['Inspecting the final product = quality control.'],
        }, subskill='concepts', learning_objective_id=LO_QUALITY, question_family_id='quality_control_definition', concept_id='quality_control', concept_group='quality', misconception_tags=['confuses_quality_control_with_tqm'], diagnostic_tags=['definition', 'quality']),
        with_metadata({
            'title': 'SABS',
            'prompt': 'The body that promotes and maintains standards in South Africa is the …',
            'options': ['SARS', 'SABS', 'CIPC', 'JSE'],
            'correct_index': 1,
            'explanation': 'The South African Bureau of Standards (SABS) promotes and maintains standards in South Africa.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the standards body.',
                'SABS = South African Bureau of Standards.',
                'SARS handles tax; CIPC handles company registration.',
            ),
            'guidelines': ['Standards body = SABS.'],
        }, subskill='concepts', learning_objective_id=LO_QUALITY, question_family_id='sabs_identification', concept_id='sabs', concept_group='quality', misconception_tags=['confuses_sabs_with_sars'], diagnostic_tags=['recall', 'quality']),
        with_metadata({
            'title': 'Fixed costs',
            'prompt': 'Costs that stay the same regardless of the level of output (e.g. rent) are called …',
            'options': ['variable costs', 'fixed costs', 'unit costs', 'primary costs'],
            'correct_index': 1,
            'explanation': 'Fixed costs remain the same regardless of the level of output, for example rent and salaries.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Decide if the cost changes with output.',
                'Costs unchanged by output = fixed costs.',
                'Variable costs rise and fall with output.',
            ),
            'guidelines': ['Unchanged by output = fixed costs.'],
        }, subskill='concepts', learning_objective_id=LO_COSTS, question_family_id='fixed_costs_definition', concept_id='fixed_costs', concept_group='costs', misconception_tags=['confuses_fixed_with_variable'], diagnostic_tags=['definition', 'costs']),
        with_metadata({
            'title': 'Break-even point',
            'prompt': 'The level of output at which total revenue equals total costs (no profit or loss) is the …',
            'options': ['mark-up point', 'break-even point', 'profit margin', 'turning point'],
            'correct_index': 1,
            'explanation': 'The break-even point is the level of output at which total revenue equals total costs, so the business makes neither a profit nor a loss.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify where revenue equals costs.',
                'No profit and no loss = break-even point.',
                'Above break-even the business makes a profit.',
            ),
            'guidelines': ['Revenue = costs at the break-even point.'],
        }, subskill='concepts', learning_objective_id=LO_COSTS, question_family_id='break_even_definition', concept_id='break_even_point', concept_group='costs', misconception_tags=['confuses_break_even_with_profit'], diagnostic_tags=['definition', 'costs']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the production method',
            'prompt': 'A factory produces 5 000 identical loaves of bread every day on a continuous production line. Identify the production method and motivate your answer. (4 marks)',
            'marks': 4,
            'marking_points': [
                'This is mass production.',
                'Large quantities are produced (5 000 loaves).',
                'The products are identical/standardised.',
                'Production is continuous on a production line.',
            ],
            'sample_answer': 'This is mass production because the factory produces large quantities (5 000 loaves) of identical, standardised products continuously on a production line.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the scenario to a method.',
                'Large quantities of identical goods = mass production.',
                'Use the scenario figures as evidence.',
            ),
            'answer_part_hints': ['Name the method.', 'Motivate with evidence.'],
            'guidelines': ['Use scenario evidence.'],
            'teaching_note': 'Reward correct method plus motivation.',
            'keywords': ['mass production', 'identical', 'large quantities', 'continuous', 'production line'],
        }, subskill='application', learning_objective_id=LO_METHODS, question_family_id='identify_method_scenario', concept_id='mass_production', concept_group='methods', scenario_family_id='bread_factory', diagnostic_tags=['scenario_analysis', 'production_methods'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Calculate break-even',
            'prompt': 'A business has fixed costs of R20 000. It sells a product for R50 with a variable cost of R30 per unit. Calculate the break-even quantity and show your working. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Contribution per unit = selling price - variable cost = R50 - R30 = R20.',
                'Break-even quantity = fixed costs / contribution per unit.',
                '= R20 000 / R20.',
                '= 1 000 units.',
            ],
            'sample_answer': 'Contribution per unit = R50 - R30 = R20. Break-even quantity = fixed costs / contribution per unit = R20 000 / R20 = 1 000 units.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Recall the break-even formula.',
                'Break-even = fixed costs / (price - variable cost).',
                'First find the contribution per unit.',
            ),
            'answer_part_hints': ['Find contribution per unit.', 'Divide fixed costs by it.'],
            'guidelines': ['Show the working, not just the answer.'],
            'teaching_note': 'Reward correct method and the answer of 1 000 units.',
            'keywords': ['contribution', 'break-even', 'fixed costs', '1 000', 'units'],
        }, subskill='application', learning_objective_id=LO_COSTS, question_family_id='break_even_calculation', concept_id='break_even_point', concept_group='costs', scenario_family_id='break_even_R20000', diagnostic_tags=['calculation', 'costs'], answer_structure_tags=['calculate', 'show_working'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Requirements for a safe environment',
            'prompt': 'Discuss the requirements for a safe working environment and why businesses must manage safety. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Provide safety equipment/protective clothing and clear procedures.',
                'Keep machinery maintained and the workplace clean/hazard-free.',
                'Train employees on safe practices and emergency procedures.',
                'Comply with the Occupational Health and Safety Act.',
                'Why: protects employees, avoids legal liability and lost productivity.',
            ],
            'sample_answer': 'A safe environment requires protective equipment and clear safety procedures, well-maintained machinery, a clean hazard-free workplace, and training on safe practices and emergencies, all in compliance with the OHSA. Businesses must manage safety to protect employees, avoid legal liability and penalties, and prevent the lost productivity and costs that come from accidents.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Cover requirements AND reasons.',
                'Think equipment, maintenance, training and compliance.',
                'Reasons link to people, law and productivity.',
            ),
            'answer_part_hints': ['Give safety requirements.', 'Explain why safety matters.'],
            'guidelines': ['Address both requirements and reasons.'],
            'teaching_note': 'Reward requirements plus reasons for managing safety.',
            'keywords': ['safety', 'protective equipment', 'training', 'OHSA', 'maintenance', 'liability'],
        }, subskill='discussion', learning_objective_id=LO_SAFETY, question_family_id='safe_environment_discussion', concept_id='safety_management', concept_group='safety', diagnostic_tags=['discussion', 'safety'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Advantages of production planning',
            'prompt': 'Explain the advantages of production planning for a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Decreases production cost and time; increases output.',
                'Ensures resources/materials are available when needed.',
                'Reduces waste and bottlenecks in the process.',
                'Helps meet deadlines and customer demand reliably.',
            ],
            'sample_answer': 'Production planning decreases production cost and time while increasing output. It ensures that resources and materials are available when needed, reduces waste and bottlenecks, and helps the business meet deadlines and customer demand reliably.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'List benefits of planning ahead.',
                'Think cost, time, output and resource availability.',
                'Planning also reduces waste and meets demand.',
            ),
            'answer_part_hints': ['Give several advantages.', 'Explain each.'],
            'guidelines': ['Provide at least three advantages.'],
            'teaching_note': 'Reward distinct, production-linked advantages.',
            'keywords': ['production planning', 'cost', 'time', 'output', 'waste', 'deadlines'],
        }, subskill='discussion', learning_objective_id=LO_PLANNING, question_family_id='planning_advantages_discussion', concept_id='production_planning', concept_group='planning_control', diagnostic_tags=['discussion', 'planning'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Total Quality Management',
            'prompt': 'Explain Total Quality Management (TQM) as part of the quality management system. (6 marks)',
            'marks': 6,
            'marking_points': [
                'TQM is a continuous, business-wide approach to improving quality.',
                'Involves all employees and all processes (not just final inspection).',
                'Focuses on meeting/exceeding customer expectations.',
                'Aims to prevent defects and continuously improve.',
            ],
            'sample_answer': 'Total Quality Management is a continuous, business-wide approach to improving quality that involves all employees and all processes, not just final inspection. It focuses on meeting and exceeding customer expectations, preventing defects rather than just detecting them, and continuously improving every part of the business.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain the breadth of TQM.',
                'TQM covers everyone and every process continuously.',
                'It is broader than quality control (final inspection).',
            ),
            'answer_part_hints': ['Define TQM.', 'Explain its key features.'],
            'guidelines': ['Show TQM is business-wide and continuous.'],
            'teaching_note': 'Reward the whole-business, continuous nature of TQM.',
            'keywords': ['TQM', 'continuous', 'all employees', 'processes', 'customer', 'prevent defects'],
        }, subskill='discussion', learning_objective_id=LO_QUALITY, question_family_id='tqm_discussion', concept_id='tqm', concept_group='quality', diagnostic_tags=['discussion', 'quality'], answer_structure_tags=['define', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
