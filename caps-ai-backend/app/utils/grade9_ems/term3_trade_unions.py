import random
from app.utils.ems_namelist import get_ems_scenario, NAMES, AREAS

def _rng(seed=None):
    return random.Random(seed)

TOPIC_ID = 'grade9_ems'
SUBTOPIC_ID = 'term3_trade_unions'
CURRICULUM_REFERENCE = 'Term 3 > Trade Unions'

def _with_metadata(item, *, subskill, learning_objective_id, question_family_id, concept_id=None, concept_group=None, curriculum_reference=CURRICULUM_REFERENCE, misconception_tags=None, diagnostic_tags=None):
    enriched = dict(item)
    enriched.update({'topic_id': TOPIC_ID, 'subtopic_id': SUBTOPIC_ID, 'subskill': subskill, 'learning_objective_id': learning_objective_id, 'concept_id': concept_id, 'concept_group': concept_group, 'question_family_id': question_family_id, 'difficulty_band': item.get('difficulties', ['easy','medium','hard']), 'curriculum_reference': curriculum_reference, 'misconception_tags': misconception_tags or [], 'diagnostic_tags': diagnostic_tags or []})
    return enriched

def _mcq_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    correct_option = item['options'][item['correct_index']]
    q = {'id': f"g9_ems_mcq_{rng.randint(1000,999999)}", 'title': item.get('title','Concept check'), 'question_type': 'mcq', 'prompt': item['prompt'], 'options': item['options'], 'correct_index': str(item['correct_index']), 'explanation': item['explanation'], 'marks': item.get('marks',1), 'sample_answer': correct_option, 'ideal_answer': correct_option, 'marking_points': [correct_option]}
    q.update({k:v for k,v in item.items() if k not in ['prompt','options','correct_index','explanation','title','marks','hint_sections','guidelines','teaching_note']})
    if mode_norm == "scaffold":
        if 'hint_sections' in item: q['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: q['guidelines'] = item['guidelines']
    return q

def _typed_question(rng, item, mode="scaffold"):
    mode_norm = str(mode or "").strip().lower()
    q = {'id': f"g9_ems_typed_{rng.randint(1000,999999)}", 'title': item.get('title','Written response'), 'question_type': 'typed', 'prompt': item['prompt'], 'marks': item['marks'], 'marking_points': item['marking_points'], 'sample_answer': item['sample_answer'], 'ideal_answer': item.get('ideal_answer',item['sample_answer'])}
    q.update({k:v for k,v in item.items() if k not in ['prompt','marks','marking_points','sample_answer','ideal_answer','hint_sections','guidelines','teaching_note','title']})
    if mode_norm == "scaffold":
        if 'hint_sections' in item: q['hint_sections'] = item['hint_sections']
        if 'guidelines' in item: q['guidelines'] = item['guidelines']
    return q

def _concept_pool(rng):
    return [
        _with_metadata({'title': 'Trade Union Definition', 'prompt': 'What is the main purpose of a trade union?', 'options': ['To make profits for business owners','To protect and promote the interests of workers','To replace government in labour regulation','To prevent businesses from hiring new employees'], 'correct_index': 1, 'explanation': 'A trade union is an organisation formed by workers to protect and promote their interests, including negotiating better wages and working conditions.', 'difficulties': ['easy','medium'], 'marks': 2, 'hint_sections': [{'title':'What is being tested?','text':'Understanding the fundamental purpose of trade unions.'}], 'guidelines': ['Select the option about protecting workers.']}, subskill='concepts', learning_objective_id='lo_trade_union_purpose', question_family_id='trade_union_definition', concept_id='trade_union', concept_group='trade_unions'),
        _with_metadata({'title': 'COSATU', 'prompt': 'COSATU stands for:', 'options': ['Congress of South African Trade Unions','Council of South African Trade Unions','Committee of South African Trade Unions','Coalition of South African Trade Unions'], 'correct_index': 0, 'explanation': 'COSATU is the Congress of South African Trade Unions, the largest trade union federation in South Africa.', 'difficulties': ['easy','medium'], 'marks': 2, 'hint_sections': [{'title':'What is being tested?','text':'Knowledge of major South African trade union federations.'}], 'guidelines': ['Select the correct full name.']}, subskill='concepts', learning_objective_id='lo_cosatu', question_family_id='cosatu_name', concept_id='cosatu', concept_group='trade_unions'),
        _with_metadata({'title': 'Collective Bargaining', 'prompt': 'Collective bargaining refers to:', 'options': ['Individual workers negotiating their own salaries','Trade unions negotiating wages and conditions on behalf of workers','Government setting wages for all industries','Business owners deciding pay without worker input'], 'correct_index': 1, 'explanation': 'Collective bargaining is the process where trade unions negotiate wages, working hours, and conditions of employment on behalf of their members.', 'difficulties': ['easy','medium'], 'marks': 2, 'hint_sections': [{'title':'What is being tested?','text':'Understanding collective bargaining.'}], 'guidelines': ['Select the option about union negotiation.']}, subskill='concepts', learning_objective_id='lo_collective_bargaining', question_family_id='collective_bargaining', concept_id='collective_bargaining', concept_group='trade_unions'),
        _with_metadata({'title': 'Strike Action', 'prompt': 'When trade unions call a strike, what is the primary goal?', 'options': ['To close the business permanently','To force employers to address worker demands','To increase government taxes','To recruit new union members'], 'correct_index': 1, 'explanation': 'A strike is a form of industrial action where workers withdraw their labour to pressure employers into meeting their demands, such as better pay or safer conditions.', 'difficulties': ['medium'], 'marks': 2, 'hint_sections': [{'title':'What is being tested?','text':'Understanding the purpose of strikes.'}], 'guidelines': ['Select the option about addressing worker demands.']}, subskill='concepts', learning_objective_id='lo_strike', question_family_id='strike_purpose', concept_id='strike', concept_group='trade_unions'),
    ]

def _discussion_pool(rng):
    return [
        _with_metadata({'title': 'Roles of Trade Unions', 'prompt': 'Discuss three roles and responsibilities of trade unions in South Africa. (6 marks)', 'marks': 6, 'marking_points': ['Protecting workers\' rights and interests.','Negotiating wages and working conditions through collective bargaining.','Providing support to workers during disputes or disciplinary hearings.','Promoting skills development and training for members.','Engaging in socio-economic policy discussions.'], 'sample_answer': 'Trade unions in South Africa protect workers\' rights and interests, ensuring fair treatment in the workplace. They engage in collective bargaining to negotiate better wages and working conditions on behalf of their members. Unions also provide support during disputes, promote skills development, and participate in national policy discussions affecting workers.', 'difficulties': ['medium','hard'], 'hint_sections': [{'title':'What is being tested?','text':'Comprehensive knowledge of trade union roles.'}], 'guidelines': ['Accept any three valid roles with brief explanation.']}, subskill='discussion', learning_objective_id='lo_union_roles', question_family_id='union_roles_essay', concept_id='union_roles', concept_group='trade_unions'),
        _with_metadata({'title': 'Effect on Businesses', 'prompt': 'Explain two positive and two negative effects that trade unions can have on businesses in South Africa. (6 marks)', 'marks': 6, 'marking_points': ['Positive: improved worker morale and productivity.','Positive: reduced staff turnover through fair treatment.','Positive: structured wage negotiations prevent arbitrary decisions.','Negative: strikes can disrupt production and cause financial losses.','Negative: high wage demands may increase business costs.'], 'sample_answer': 'Trade unions can positively affect businesses by improving worker morale and productivity, and by reducing staff turnover through fair treatment and structured wage negotiations. However, strikes can disrupt production and cause financial losses, and unions may demand wages that increase business operating costs.', 'difficulties': ['medium'], 'hint_sections': [{'title':'What is being tested?','text':'Balanced analysis of trade union impact on businesses.'}], 'guidelines': ['Require at least two positive and two negative points.']}, subskill='discussion', learning_objective_id='lo_union_business_effect', question_family_id='union_business_effect', concept_id='union_business_impact', concept_group='trade_unions'),
    ]

def generate(subskill="concepts", difficulty="medium", count=1, mode="scaffold", seed=None, **kwargs):
    rng = _rng(seed)
    pool = _discussion_pool(rng) if subskill == "discussion" else _concept_pool(rng)
    selected = [q for q in pool if difficulty in q['difficulties']]
    if not selected: selected = pool
    chosen = rng.sample(selected, min(count, len(selected)))
    builder = _typed_question if subskill == "discussion" else _mcq_question
    return [builder(rng, item, mode=mode) for item in chosen]
