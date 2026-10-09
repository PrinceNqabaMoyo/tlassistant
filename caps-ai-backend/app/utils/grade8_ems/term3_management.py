import random
from app.utils.ems_namelist import NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade8_ems'
SUBTOPIC_ID = 'term3_management'
CURRICULUM_REFERENCE = 'Term 3 > Entrepreneurship: Levels and Functions of Management'

def _with_metadata(
    item,
    *,
    subskill,
    learning_objective_id,
    question_family_id,
    concept_id=None,
    concept_group="management",
    scenario_family_id=None,
    retry_variant='core',
    curriculum_reference=CURRICULUM_REFERENCE,
    misconception_tags=None,
    diagnostic_tags=None,
    answer_structure_tags=None,
    minimum_mastery_score=None,
):
    enriched = dict(item)
    enriched.update({
        'topic_id': TOPIC_ID,
        'subtopic_id': SUBTOPIC_ID,
        'subskill': subskill,
        'learning_objective_id': learning_objective_id,
        'concept_id': concept_id,
        'concept_group': concept_group,
        'question_family_id': question_family_id,
        'scenario_family_id': scenario_family_id,
        'retry_variant': retry_variant,
        'difficulty_band': item.get('difficulties', ['easy', 'medium', 'hard']),
        'curriculum_reference': curriculum_reference,
        'misconception_tags': misconception_tags or [],
        'diagnostic_tags': diagnostic_tags or [],
        'answer_structure_tags': answer_structure_tags or [],
        'term': 3,
        'caps_weight_percent': 20,
        'suggested_duration_mins': 15,
    })
    if minimum_mastery_score is not None:
        enriched['minimum_mastery_score'] = minimum_mastery_score
    return enriched

def _mcq_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    correct_option = item['options'][item['correct_index']]
    question = {
        'id': f"g8_ems_mgmt_mcq_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Levels and Functions of Management'),
        'question_type': 'mcq',
        'prompt': item['prompt'],
        'options': item['options'],
        'correct_index': str(item['correct_index']),
        'explanation': item['explanation'],
        'marks': item.get('marks', 2),
        'sample_answer': correct_option,
        'ideal_answer': correct_option,
        'marking_points': [correct_option],
        'term': 3,
        'caps_weight_percent': 20,
        'suggested_duration_mins': 12,
        'marking_schema': {
            'total_marks': item.get('marks', 2),
            'marking_points': [
                {'id': 'mp_1', 'desc': f"Correct option selection: {correct_option}", 'marks': item.get('marks', 2), 'editable': True}
            ]
        },
        **{k: v for k, v in item.items() if k not in ['prompt', 'options', 'correct_index', 'explanation', 'title', 'marks', 'hint_sections', 'guidelines', 'teaching_note', 'hints']}
    }
    
    if 'hints' in item:
        question['hints'] = item['hints']
    elif 'hint_sections' in item:
        question['hints'] = {
            'tier_1': item['hint_sections'][0]['text'] if len(item['hint_sections']) > 0 else "Focus on management hierarchy and core tasks.",
            'tier_2': item['hint_sections'][1]['text'] if len(item['hint_sections']) > 1 else "Recall POLC: Planning, Organising, Leading, and Controlling.",
            'tier_3': f"The correct answer is: {correct_option}"
        }
    else:
        question['hints'] = {
            'tier_1': "Identify the level of authority and specific management function.",
            'tier_2': "Top = strategic vision, Middle = departmental coordination, Lower = direct team supervision.",
            'tier_3': f"The correct answer is: {correct_option}"
        }

    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', item['explanation'])
    return question

def _typed_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    question = {
        'id': f"g8_ems_mgmt_typed_{rng.randint(1000, 999999)}",
        'title': item.get('title', 'Management Analysis'),
        'question_type': 'typed',
        'prompt': item['prompt'],
        'marks': item['marks'],
        'marking_points': item['marking_points'],
        'sample_answer': item['sample_answer'],
        'ideal_answer': item.get('ideal_answer', item['sample_answer']),
        'term': 3,
        'caps_weight_percent': 20,
        'suggested_duration_mins': 15,
        'marking_schema': {
            'total_marks': item['marks'],
            'marking_points': [
                {'id': f'mp_{i+1}', 'desc': pt, 'marks': 1, 'editable': True} for i, pt in enumerate(item['marking_points'])
            ]
        },
        'hints': item.get('hints', {
            'tier_1': "Review the four management tasks (POLC) or leadership styles.",
            'tier_2': "Structure your answer with clear definitions and business examples.",
            'tier_3': item['sample_answer']
        }),
        **{k: v for k, v in item.items() if k not in ['prompt', 'marks', 'marking_points', 'sample_answer', 'ideal_answer', 'hint_sections', 'guidelines', 'teaching_note', 'title', 'hints']}
    }
    if mode_norm == "scaffold":
        if 'hint_sections' in item: question['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: question['guidelines'] = item['guidelines']
        if 'teaching_note' in item: question['teaching_note'] = item.get('teaching_note', '')
    return question

def _build_levels_questions(rng):
    name = rng.choice(NAMES)
    area = rng.choice(AREAS)
    
    scenarios = [
        {
            "role": f"Managing Director (Chief Executive Officer)",
            "task": "sets 5-year strategic expansion targets and formulates major company policies",
            "level": "Top level management",
            "wrong": ["Middle level management", "Lower / First-line management", "Non-managerial operations"]
        },
        {
            "role": f"Regional Marketing and Sales Manager",
            "task": "coordinates the promotional campaign between branch stores and ensures advertising targets are met",
            "level": "Middle level management",
            "wrong": ["Top level management", "Lower / First-line management", "Executive board level"]
        },
        {
            "role": f"Factory Floor Shift Supervisor",
            "task": "oversees daily assembly shifts, ensures workers wear safety gear, and monitors hourly output quotas",
            "level": "Lower / First-line management",
            "wrong": ["Top level management", "Middle level management", "Executive committee level"]
        }
    ]
    sc = rng.choice(scenarios)
    options = [sc['level']] + sc['wrong']
    rng.shuffle(options)
    correct_idx = options.index(sc['level'])

    return [
        _with_metadata({
            'title': 'Identifying Levels of Management',
            'prompt': (
                f"At a nationwide retail enterprise in {area}, {name} serves as the {sc['role']}. "
                f"In this role, {name} {sc['task']}. Which level of management does this position represent?"
            ),
            'options': options,
            'correct_index': correct_idx,
            'explanation': (
                f"{sc['role']} is part of {sc['level']} because the responsibilities involve {sc['task']}."
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Identify whether this role makes company-wide strategic decisions, manages a department, or supervises daily work.",
                'tier_2': "Top = overall business direction. Middle = departmental managers. Lower/first-line = direct supervisors of workers.",
                'tier_3': f"A {sc['role']} belongs to {sc['level']}."
            },
            'misconception_tags': ['top_vs_middle_confusion', 'middle_vs_lower_confusion']
        }, subskill='elementary_levels', learning_objective_id='lo_ems_mgmt_levels', question_family_id='level_id', concept_id='hierarchy')
    ]

def _build_tasks_questions(rng):
    name = rng.choice(NAMES)
    
    tasks = [
        {
            "task_name": "Planning",
            "action": f"{name} drafts the annual financial budget, establishes sales targets, and sets the schedule for product launches for the upcoming year.",
            "desc": "Setting goals ahead of time and determining the actions needed to achieve them."
        },
        {
            "task_name": "Organising",
            "action": f"{name} allocates staff into four specialized project teams, purchases new packaging equipment, and assigns specific responsibilities to each team leader.",
            "desc": "Arranging and allocating resources, equipment, and people so that planned work can be carried out efficiently."
        },
        {
            "task_name": "Leading",
            "action": f"{name} holds weekly team briefings to inspire staff, resolves interpersonal disputes between workers, and motivates employees to exceed performance quotas.",
            "desc": "Guiding, motivating, directing, and inspiring employees to work towards business goals."
        },
        {
            "task_name": "Controlling",
            "action": f"{name} inspects finished products for defects, compares actual monthly sales figures against projected targets, and implements corrective procedures for variances.",
            "desc": "Monitoring actual performance, checking against set standards, and correcting deviations."
        }
    ]
    t = rng.choice(tasks)
    all_names = ["Planning", "Organising", "Leading", "Controlling"]
    rng.shuffle(all_names)
    correct_idx = all_names.index(t['task_name'])

    return [
        _with_metadata({
            'title': 'Management Tasks (POLC)',
            'prompt': (
                f"Consider the following management scenario:\n\n"
                f"\"{t['action']}\"\n\n"
                f"Which of the four core management tasks is being performed here?"
            ),
            'options': all_names,
            'correct_index': correct_idx,
            'explanation': (
                f"This activity describes {t['task_name']}, which involves: {t['desc']}"
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Recall the 4 management tasks: Planning, Organising, Leading, and Controlling (POLC).",
                'tier_2': f"Is the manager setting future targets (Planning), assigning resources (Organising), motivating people (Leading), or checking results (Controlling)?",
                'tier_3': f"The correct task is {t['task_name']}."
            },
            'misconception_tags': ['planning_vs_controlling_confusion', 'organising_vs_leading_confusion']
        }, subskill='elementary_tasks', learning_objective_id='lo_ems_mgmt_polc', question_family_id='polc_task_id', concept_id='management_functions'),

        _with_metadata({
            'title': 'Explaining the Four Core Management Tasks',
            'prompt': (
                "Name the FOUR main management tasks and briefly explain what each task entails. (4 marks)"
            ),
            'marks': 4,
            'marking_points': [
                "Planning: Deciding ahead of time what to do and setting goals and action steps.",
                "Organising: Allocating resources, staff, and assigning responsibilities.",
                "Leading: Guiding, motivating, and directing employees to achieve goals.",
                "Controlling: Checking actual performance against targets and taking corrective action."
            ],
            'sample_answer': (
                "The four core management tasks are:\n"
                "1. Planning: Setting business goals and outlining the steps to achieve them.\n"
                "2. Organising: Grouping activities, allocating resources, and assigning tasks to workers.\n"
                "3. Leading: Motivating, directing, and guiding employees to perform effectively.\n"
                "4. Controlling: Measuring actual performance against targets and taking corrective action."
            ),
            'difficulties': ['medium', 'hard'],
            'hints': {
                'tier_1': "Use the POLC acronym: P - Planning, O - Organising, L - Leading, C - Controlling.",
                'tier_2': "Provide a clear 1-sentence definition for each of the four components.",
                'tier_3': "Planning (setting goals), Organising (allocating tasks), Leading (motivating people), Controlling (monitoring results)."
            },
            'misconception_tags': ['incomplete_polc_explanation']
        }, subskill='elementary_tasks', learning_objective_id='lo_ems_mgmt_tasks_essay', question_family_id='polc_essay', concept_id='polc_complete')
    ]

def _build_styles_questions(rng):
    name = rng.choice(NAMES)
    
    styles = [
        {
            "name": "Autocratic management style",
            "scenario": f"{name} makes all business decisions alone without asking employees for input, issues strict commands, and closely supervises workers without allowing questions.",
            "desc": "A dictating style where the manager makes all decisions unilaterally and requires strict compliance."
        },
        {
            "name": "Democratic / Participatory management style",
            "scenario": f"{name} regularly consults employees during staff meetings, encourages team members to propose innovative solutions, and takes group feedback into account before finalizing decisions.",
            "desc": "A participatory style where managers consult the team, encourage open discussion, and involve workers in decision-making."
        },
        {
            "name": "Laissez-faire / Permissive management style",
            "scenario": f"{name} delegates broad project objectives to highly skilled graphic designers, granting them complete freedom to choose their working hours and methods without micromanagement.",
            "desc": "A free-rein style where managers delegate authority and give experienced staff freedom to decide how to complete work."
        }
    ]
    st = rng.choice(styles)
    all_styles = [
        "Autocratic management style",
        "Democratic / Participatory management style",
        "Laissez-faire / Permissive management style",
        "Bureaucratic government style"
    ]
    rng.shuffle(all_styles)
    correct_idx = all_styles.index(st['name'])

    return [
        _with_metadata({
            'title': 'Management and Leadership Styles',
            'prompt': (
                f"Evaluate the following management approach:\n\n"
                f"\"{st['scenario']}\"\n\n"
                f"Which management style does {name} practice?"
            ),
            'options': all_styles,
            'correct_index': correct_idx,
            'explanation': (
                f"{st['name']} is demonstrated here because: {st['desc']}"
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Observe whether decisions are dictated (autocratic), made through teamwork (democratic), or left to employees (laissez-faire).",
                'tier_2': "Autocratic = boss dictates; Democratic = team participates; Laissez-faire = complete freedom/delegation.",
                'tier_3': f"The described style is {st['name']}."
            },
            'misconception_tags': ['autocratic_vs_democratic_confusion', 'laissez_faire_misunderstanding']
        }, subskill='elementary_styles', learning_objective_id='lo_ems_mgmt_styles', question_family_id='mgmt_style_id', concept_id='leadership_styles'),

        _with_metadata({
            'title': 'Comparing Autocratic and Democratic Management Styles',
            'prompt': (
                "Contrast the AUTOCRATIC management style with the DEMOCRATIC management style. "
                "In your answer, identify one situation where an autocratic style is appropriate. (4 marks)"
            ),
            'marks': 4,
            'marking_points': [
                "Autocratic: Manager dictates decisions without consulting employees and demands strict obedience.",
                "Democratic: Manager encourages participation, consults the team, and values worker feedback.",
                "Difference in worker morale: Democratic fosters higher morale and creativity, while autocratic can lower job satisfaction.",
                "Appropriate situation: Autocratic is necessary in crises, emergencies, or strictly timed safety procedures where immediate action is required."
            ],
            'sample_answer': (
                "In an autocratic style, the manager makes all decisions alone and dictates tasks without consultation. "
                "In a democratic style, the manager involves employees and encourages shared decision-making. "
                "An autocratic style is appropriate during an emergency or crisis (e.g. a fire evacuation or strict factory safety compliance) "
                "where urgent, decisive leadership is required without time for team debate."
            ),
            'difficulties': ['medium', 'hard'],
            'hints': {
                'tier_1': "Define how decisions are made in each style and provide a crisis example for autocratic management.",
                'tier_2': "Autocratic = no consultation; Democratic = shared consultation. Crises or safety emergencies require autocratic commands.",
                'tier_3': "Point 1: Autocratic dictates. Point 2: Democratic consults. Point 3: Autocratic is suitable in emergencies."
            },
            'misconception_tags': ['autocratic_vs_democratic_confusion']
        }, subskill='elementary_styles', learning_objective_id='lo_ems_mgmt_comparison', question_family_id='mgmt_comparison', concept_id='style_comparison')
    ]

def _build_characteristics_questions(rng):
    return [
        _with_metadata({
            'title': 'Characteristics of a Good Manager',
            'prompt': (
                "Which combination of traits best represents the qualities of an effective and trustworthy business manager?"
            ),
            'options': [
                "Possesses strong interpersonal people skills, demonstrates integrity, and organizes resources efficiently",
                "Dictates all orders without listening, works in isolation, and ignores worker grievances",
                "Leaves all decisions entirely to unguided junior workers and refuses to take responsibility for business failures",
                "Prioritizes short-term personal profits over worker safety and ethical business standards"
            ],
            'correct_index': 0,
            'explanation': (
                "Effective managers demonstrate strong people skills, ethical trustworthiness, organizational competence, "
                "and responsibility for their team's performance."
            ),
            'difficulties': ['easy', 'medium'],
            'marks': 2,
            'hints': {
                'tier_1': "Identify positive leadership qualities that build a productive and motivated workforce.",
                'tier_2': "Good managers communicate well, take responsibility, maintain integrity, and organize resources.",
                'tier_3': "Strong interpersonal skills, integrity, and efficient organization are the core qualities."
            },
            'misconception_tags': ['bad_leadership_assumptions']
        }, subskill='elementary_characteristics', learning_objective_id='lo_ems_good_manager_traits', question_family_id='manager_traits', concept_id='manager_qualities')
    ]

def generate(subskill="compound", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    subskill_str = str(subskill or "compound").strip().lower()
    
    if subskill_str == "elementary_levels":
        pool = _build_levels_questions(rng)
    elif subskill_str == "elementary_tasks":
        pool = _build_tasks_questions(rng)
    elif subskill_str == "elementary_styles":
        pool = _build_styles_questions(rng)
    elif subskill_str == "elementary_characteristics":
        pool = _build_characteristics_questions(rng)
    else:
        # Compound
        pool = (
            _build_levels_questions(rng) +
            _build_tasks_questions(rng) +
            _build_styles_questions(rng) +
            _build_characteristics_questions(rng)
        )
        
    selected = [q for q in pool if difficulty in q['difficulty_band']]
    if not selected:
        selected = pool
    chosen = rng.sample(selected, min(count, len(selected)))
    
    results = []
    for item in chosen:
        if 'options' in item:
            results.append(_mcq_question(rng, item, mode=mode))
        else:
            results.append(_typed_question(rng, item, mode=mode))
            
    if count == 1 and len(results) == 1:
        return results[0]
    return results
