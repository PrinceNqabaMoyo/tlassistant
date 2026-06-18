"""Grade 11 Business Studies - Term 3 - Topic 15: Transformation of a business
plan into an action plan.

Deterministic generator (seeded RNG + curated CAPS content banks).
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='business_plan_transformation',
    curriculum_reference='Term 3 > Transformation of a business plan into an action plan',
    id_prefix='g11_bs_actionplan',
)

LO_PLANS = 'lo_business_and_action_plans'
LO_TOOLS = 'lo_planning_tools'
LO_STEPS = 'lo_action_plan_steps'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Business plan',
            'prompt': 'A formal written document describing the goals of a business and the methods of how to achieve them is a …',
            'options': ['action plan', 'business plan', 'Gantt chart', 'timeline'],
            'correct_index': 1,
            'explanation': 'A business plan is a formal written document describing the goals of a business and the methods of how to achieve those goals.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish the strategic document.',
                'A business plan sets out goals and how to achieve them.',
                'An action plan is the checklist of tasks to do it.',
            ),
            'guidelines': ['Goals + methods document = business plan.'],
        }, subskill='concepts', learning_objective_id=LO_PLANS, question_family_id='business_plan_definition', concept_id='business_plan', concept_group='plans', misconception_tags=['confuses_business_plan_with_action_plan'], diagnostic_tags=['definition', 'plans']),
        with_metadata({
            'title': 'Action plan',
            'prompt': 'A checklist of the steps or tasks you need to complete to achieve your set goals is a(n) …',
            'options': ['business plan', 'action plan', 'prospectus', 'WBS'],
            'correct_index': 1,
            'explanation': 'An action plan is a checklist of the steps or tasks you need to complete to achieve the goals you have set.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Distinguish the task checklist.',
                'An action plan lists the tasks to reach the goals.',
                'A business plan is the broader strategic document.',
            ),
            'guidelines': ['Checklist of tasks = action plan.'],
        }, subskill='concepts', learning_objective_id=LO_PLANS, question_family_id='action_plan_definition', concept_id='action_plan', concept_group='plans', misconception_tags=['confuses_action_plan_with_business_plan'], diagnostic_tags=['definition', 'plans']),
        with_metadata({
            'title': 'Gantt chart',
            'prompt': 'A bar chart that provides a visual timeline of how tasks are scheduled is a …',
            'options': ['pie chart', 'Gantt chart', 'flowchart', 'histogram'],
            'correct_index': 1,
            'explanation': 'A Gantt chart is a bar chart that provides a visual timeline of how tasks are scheduled.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the scheduling bar chart.',
                'A Gantt chart shows tasks against time as bars.',
                'A WBS breaks the plan into smaller stages.',
            ),
            'guidelines': ['Bar chart of scheduled tasks = Gantt chart.'],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='gantt_chart_definition', concept_id='gantt_chart', concept_group='tools', misconception_tags=['confuses_gantt_with_wbs'], diagnostic_tags=['definition', 'tools']),
        with_metadata({
            'title': 'Work breakdown structure',
            'prompt': 'A tool that divides the business plan into smaller project stages and shows exactly what must be done is a …',
            'options': ['timeline', 'work breakdown structure (WBS)', 'Gantt chart', 'budget'],
            'correct_index': 1,
            'explanation': 'A work breakdown structure (WBS) divides the business plan into smaller project stages and shows exactly what must be done.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the breakdown tool.',
                'A WBS breaks work into smaller stages/tasks.',
                'A Gantt chart schedules those tasks over time.',
            ),
            'guidelines': ['Breaks plan into stages = WBS.'],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='wbs_definition', concept_id='wbs', concept_group='tools', misconception_tags=['confuses_wbs_with_gantt'], diagnostic_tags=['definition', 'tools']),
        with_metadata({
            'title': 'Timelines',
            'prompt': 'A sequence of related events arranged in chronological order along a line to track activities is a …',
            'options': ['timeline', 'Gantt chart', 'WBS', 'budget'],
            'correct_index': 0,
            'explanation': 'A timeline is a sequence of related events arranged in chronological order and displayed along a line to keep track of activities.',
            'difficulties': ['easy', 'medium', 'hard'],
            'hint_sections': hint_sections(
                'Identify the chronological tool.',
                'A timeline shows events in chronological order.',
                'A Gantt chart adds task durations as bars.',
            ),
            'guidelines': ['Chronological line of events = timeline.'],
        }, subskill='concepts', learning_objective_id=LO_TOOLS, question_family_id='timeline_definition', concept_id='timeline', concept_group='tools', misconception_tags=['confuses_timeline_with_gantt'], diagnostic_tags=['definition', 'tools']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Choose the planning tool',
            'prompt': 'A project manager wants to see, at a glance, which tasks overlap and how long each task will take across the next three months. Recommend the BEST planning tool and motivate. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Recommend a Gantt chart.',
                'It shows tasks as bars against a time axis.',
                'Overlapping bars show which tasks run at the same time.',
                'The length of each bar shows how long each task takes.',
            ],
            'sample_answer': 'A Gantt chart is best because it shows each task as a bar against a time axis, so the manager can see at a glance which tasks overlap and how long each task will take over the three months.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Match the need to the tool.',
                'Seeing durations and overlaps over time = Gantt chart.',
                'A WBS only breaks work into stages, not a schedule.',
            ),
            'answer_part_hints': ['Name the tool.', 'Motivate your choice.'],
            'guidelines': ['Tie the tool to the manager\'s need.'],
            'teaching_note': 'Reward a Gantt chart with a motivation about time/overlap.',
            'keywords': ['Gantt chart', 'tasks', 'time', 'overlap', 'duration', 'schedule'],
        }, subskill='application', learning_objective_id=LO_TOOLS, question_family_id='choose_tool_scenario', concept_id='gantt_chart', concept_group='tools', scenario_family_id='project_schedule', diagnostic_tags=['recommendation', 'tools'], answer_structure_tags=['recommend', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Transform plan into action',
            'prompt': 'A business plan states the goal "open a second branch within 12 months". Convert this into TWO action-plan tasks with a sense of timing. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Action tasks are specific steps with timing.',
                'Example: secure premises and finance by month 4.',
                'Example: recruit and train staff by month 9.',
                'Example: stock the branch and launch by month 12.',
            ],
            'sample_answer': 'Two action-plan tasks could be: (1) secure premises and finance for the branch by month 4, and (2) recruit and train staff by month 9, so that the branch can be stocked and launched by month 12.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Turn a goal into timed tasks.',
                'Action tasks are specific and have deadlines.',
                'Break the 12-month goal into smaller dated steps.',
            ),
            'answer_part_hints': ['Give two tasks.', 'Add timing to each.'],
            'guidelines': ['Tasks must be specific with timing.'],
            'teaching_note': 'Reward specific, timed action tasks derived from the goal.',
            'keywords': ['action plan', 'tasks', 'premises', 'finance', 'staff', 'deadline', 'months'],
        }, subskill='application', learning_objective_id=LO_STEPS, question_family_id='transform_plan_scenario', concept_id='action_plan', concept_group='plans', scenario_family_id='second_branch', diagnostic_tags=['scenario_analysis', 'plans'], answer_structure_tags=['apply', 'convert'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Importance of an action plan',
            'prompt': 'Discuss the importance of an action plan for a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Breaks goals into clear, manageable tasks.',
                'Assigns responsibility and deadlines for each task.',
                'Helps monitor progress and stay on schedule.',
                'Improves use of resources and the chance of achieving goals.',
            ],
            'sample_answer': 'An action plan is important because it breaks the business\'s goals into clear, manageable tasks, assigns responsibility and deadlines for each, and helps the business monitor progress and stay on schedule. This improves the use of resources and increases the chance of actually achieving the goals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain why action plans matter.',
                'Think tasks, responsibility, deadlines and monitoring.',
                'Action plans turn goals into achievable steps.',
            ),
            'answer_part_hints': ['Give several points.', 'Explain each.'],
            'guidelines': ['Provide at least three points.'],
            'teaching_note': 'Reward distinct reasons an action plan helps execution.',
            'keywords': ['action plan', 'tasks', 'responsibility', 'deadlines', 'monitor', 'goals'],
        }, subskill='discussion', learning_objective_id=LO_STEPS, question_family_id='importance_action_plan_discussion', concept_id='action_plan', concept_group='plans', diagnostic_tags=['discussion', 'plans'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Importance of Gantt charts and timelines',
            'prompt': 'Discuss the importance of timelines and Gantt charts/WBS in project planning. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Provide a visual schedule of tasks and deadlines.',
                'Show how tasks depend on or overlap with each other.',
                'Help allocate resources and track progress.',
                'Make it easier to identify delays and stay on schedule.',
            ],
            'sample_answer': 'Timelines and Gantt charts/WBS provide a visual schedule of tasks and deadlines, show how tasks overlap or depend on one another, and help the business allocate resources and track progress. This makes it easier to spot delays early and keep the project on schedule.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections(
                'Explain why these tools help planning.',
                'They visualise schedules, dependencies and progress.',
                'They help spot delays and manage resources.',
            ),
            'answer_part_hints': ['Give several points.', 'Explain each.'],
            'guidelines': ['Provide at least three points.'],
            'teaching_note': 'Reward distinct benefits of visual planning tools.',
            'keywords': ['Gantt chart', 'timeline', 'WBS', 'schedule', 'progress', 'deadlines'],
        }, subskill='discussion', learning_objective_id=LO_TOOLS, question_family_id='importance_tools_discussion', concept_id='gantt_chart', concept_group='tools', diagnostic_tags=['discussion', 'tools'], answer_structure_tags=['list', 'explain'], minimum_mastery_score=0.6),
    ]


generate = make_generate(META, _concept_pool, _application_pool, _discussion_pool)
