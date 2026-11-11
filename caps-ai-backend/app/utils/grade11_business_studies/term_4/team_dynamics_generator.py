"""Grade 11 Business Studies - Term 4 - Topic 19: Team dynamics and conflict management.

Deterministic generator (seeded RNG + curated CAPS content banks). Grounded in
``curriculum_docs_auto/BusinessStudies_Gr11/Term 4/01. Team dynamics & conflict
management.md``. The word_bank / matching / crossword / essay archetypes are
authored below where a curated bank adds value, and are otherwise derived from
the concept / discussion banks by ``make_generate``.
"""
from __future__ import annotations

import random
from typing import Any, Dict, List

from .._g11_common import TopicMeta, hint_sections, make_generate, with_metadata

META = TopicMeta(
    topic_id='grade11_business_studies',
    subtopic_id='team_dynamics',
    curriculum_reference='Term 4 > Team dynamics and conflict management',
    id_prefix='g11_bs_teamdyn',
)

LO_TEAM = 'lo_team_work_and_development'
LO_THEORY = 'lo_team_dynamic_theories'
LO_CONFLICT = 'lo_conflict_management'


def _concept_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Team',
            'prompt': 'A group of people organised to work together is called a …',
            'options': ['team', 'department', 'hierarchy', 'workforce'],
            'correct_index': 0,
            'explanation': 'A team is a group of people organised to work together towards a common goal.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections('Recall the CAPS definition of a team.', 'A team works together towards a shared goal.', 'Teamwork is the joint action of the group.'),
            'guidelines': ['Define team as a group working together.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='team_definition', concept_id='team', concept_group='teamwork', misconception_tags=['confuse_team_with_department'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Team dynamics',
            'prompt': 'The forces that influence how a team behaves, performs or responds are known as …',
            'options': ['team dynamics', 'team hierarchy', 'groupthink', 'workplace forums'],
            'correct_index': 0,
            'explanation': 'Team dynamics are the behavioural and emotional forces that influence how a team behaves, performs or responds.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Identify the term for the forces within a team.', 'Forces influencing behaviour and performance = team dynamics.', 'These theories guide how teams are managed.'),
            'guidelines': ['Link forces within a team to team dynamics.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='team_dynamics_definition', concept_id='team_dynamics', concept_group='teamwork', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Forming stage',
            'prompt': 'The FIRST stage of team development, when members first meet each other, is the … stage.',
            'options': ['forming', 'storming', 'norming', 'performing'],
            'correct_index': 0,
            'explanation': 'Forming is the first stage of Tuckman\'s model; it begins when the team first meets and members get to know each other.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections('Order the stages of team development.', 'The first stage, when members meet, is forming.', 'Sequence: forming, storming, norming, performing, mourning.'),
            'guidelines': ['Match "first stage / meeting" to forming.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_forming', concept_id='forming', concept_group='team_development', misconception_tags=['confuse_stage_order'], diagnostic_tags=['stages_of_development']),
        with_metadata({
            'title': 'Storming stage',
            'prompt': 'The stage of team development that is often characterised by conflict and power struggles is the … stage.',
            'options': ['storming', 'forming', 'norming', 'adjourning'],
            'correct_index': 0,
            'explanation': 'Storming is the second stage; it is characterised by conflict, confrontation of ideas and power struggles over leadership.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Which stage involves conflict?', 'Conflict and power struggles = storming.', 'Storming is the second stage.'),
            'guidelines': ['Conflict / power struggle points to storming.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_storming', concept_id='storming', concept_group='team_development', misconception_tags=['confuse_stage_order'], diagnostic_tags=['stages_of_development']),
        with_metadata({
            'title': 'Norming stage',
            'prompt': 'Team members reach consensus and roles become clear and accepted during the … stage.',
            'options': ['norming', 'storming', 'forming', 'mourning'],
            'correct_index': 0,
            'explanation': 'Norming (settling/reconciliation) is the third stage where the team reaches consensus and accepts roles and responsibilities.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Which stage brings agreement?', 'Consensus and accepted roles = norming.', 'Norming follows storming.'),
            'guidelines': ['Consensus / accepted roles points to norming.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_norming', concept_id='norming', concept_group='team_development', misconception_tags=['confuse_stage_order'], diagnostic_tags=['stages_of_development']),
        with_metadata({
            'title': 'Performing stage',
            'prompt': 'The stage at which the team functions at a high level and members make decisions without supervision is the … stage.',
            'options': ['performing', 'norming', 'storming', 'forming'],
            'correct_index': 0,
            'explanation': 'Performing is the fourth stage; the team functions at a high level and members handle decision-making without supervision.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Which stage is peak performance?', 'High performance, self-managing = performing.', 'Performing is the fourth stage.'),
            'guidelines': ['Peak functioning points to performing.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_performing', concept_id='performing', concept_group='team_development', misconception_tags=['confuse_stage_order'], diagnostic_tags=['stages_of_development']),
        with_metadata({
            'title': 'Mourning / adjourning stage',
            'prompt': 'The FINAL stage of team development, when the project ends and the team dissolves, is called the … stage.',
            'options': ['mourning/adjourning', 'performing', 'norming', 'storming'],
            'correct_index': 0,
            'explanation': 'Mourning (adjourning) is the fifth stage; it occurs when the project is completed and the team breaks up.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Which stage ends the team?', 'Project completion / break up = mourning/adjourning.', 'It is the fifth stage.'),
            'guidelines': ['Ending / dissolving points to mourning or adjourning.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_mourning', concept_id='adjourning', concept_group='team_development', misconception_tags=['confuse_stage_order'], diagnostic_tags=['stages_of_development']),
        with_metadata({
            'title': 'Tuckman model',
            'prompt': 'The five stages of team development were created by … in 1965.',
            'options': ['Bruce Tuckman', 'Meredith Belbin', 'Carl Jung', 'Charles Handy'],
            'correct_index': 0,
            'explanation': 'Bruce Tuckman created the five-stage model of team development (forming, storming, norming, performing, mourning) in 1965.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Attribute the stage model to its author.', 'The stage model is Tuckman\'s.', 'Belbin did roles; Jung did personality types.'),
            'guidelines': ['Link the stage model to Bruce Tuckman.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='tuckman_author', concept_id='tuckman', concept_group='team_development', misconception_tags=['confuse_theory_authors'], diagnostic_tags=['attribution']),
        with_metadata({
            'title': 'Belbin roles',
            'prompt': 'According to the Belbin Role Theory, how many key roles exist in a balanced team?',
            'options': ['nine', 'five', 'eight', 'four'],
            'correct_index': 0,
            'explanation': 'Belbin identified nine key roles, grouped into action-oriented, cerebral-oriented and people-oriented categories.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Recall the number of Belbin roles.', 'Belbin = nine roles in three groups.', 'MTR-I has eight roles; Tuckman has five stages.'),
            'guidelines': ['Belbin has nine roles.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='belbin_count', concept_id='belbin', concept_group='theories', misconception_tags=['confuse_theory_details'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Belbin Planter',
            'prompt': 'In the Belbin Role Theory, the cerebral role of the creative innovator and problem-solver is the …',
            'options': ['planter', 'implementer', 'shaper', 'completer-finisher'],
            'correct_index': 0,
            'explanation': 'Planters are the creative innovators and good problem-solvers (a cerebral-oriented role in Belbin\'s theory).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Match the behaviour to a Belbin role.', 'Creative innovator = planter.', 'Implementer is disciplined; shaper is energetic.'),
            'guidelines': ['Creativity/innovation points to the planter role.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='belbin_roles', concept_id='belbin_planter', concept_group='theories', misconception_tags=['confuse_belbin_roles'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Belbin implementer',
            'prompt': 'The Belbin role described as disciplined, dependable, well-organised and able to turn an idea into practice is the …',
            'options': ['implementer', 'planter', 'resource-investigator', 'team worker'],
            'correct_index': 0,
            'explanation': 'Implementers are disciplined, dependable and well-organised; they turn ideas into practical action (an action-oriented role).',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Match the behaviour to a Belbin role.', 'Dependable and practical = implementer.', 'Planters generate the ideas implementers carry out.'),
            'guidelines': ['Practical follow-through points to the implementer.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='belbin_roles', concept_id='belbin_implementer', concept_group='theories', misconception_tags=['confuse_belbin_roles'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Jungian extrovert',
            'prompt': 'According to the Jungian Theory, personality types that focus their energy on the outer world of people and events are …',
            'options': ['extroverts', 'introverts', 'sensing types', 'thinkers'],
            'correct_index': 0,
            'explanation': 'Extroverts focus energy outward on people and events, enjoy meeting new people and are energised by outside factors.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Distinguish the two Jungian attitudes.', 'Energy directed outward = extrovert.', 'Energy directed inward = introvert.'),
            'guidelines': ['Outward focus points to extroverts.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='jungian_types', concept_id='extrovert', concept_group='theories', misconception_tags=['confuse_intro_extro'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'MTR-I origin',
            'prompt': 'The MTR-I (Management Team Role Indicator) approach was based on the personality theory of …',
            'options': ['Carl Jung', 'Bruce Tuckman', 'Meredith Belbin', 'Maslow'],
            'correct_index': 0,
            'explanation': 'Myers developed the MTR-I approach in 1990, basing it on Carl Jung\'s theory of personality; it identifies eight team roles.',
            'difficulties': ['hard'],
            'hint_sections': hint_sections('Attribute the MTR-I to its theoretical base.', 'MTR-I is built on Jung\'s personality theory.', 'It lists eight roles (Coach, Conductor, Crusader, etc.).'),
            'guidelines': ['MTR-I derives from Jung\'s theory.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='mtr_i_origin', concept_id='mtr_i', concept_group='theories', misconception_tags=['confuse_theory_authors'], diagnostic_tags=['attribution']),
        with_metadata({
            'title': 'Margerison-McCann',
            'prompt': 'The Margerison-McCann Team Management Systems theory is built on the idea that people …',
            'options': ['do better at the things they enjoy doing', 'must be strictly supervised', 'work best in isolation', 'should avoid conflict at all costs'],
            'correct_index': 0,
            'explanation': 'Margerison and McCann held that people do better at the things they enjoy, so a team succeeds when members\' role preferences complement and balance one another.',
            'difficulties': ['hard'],
            'hint_sections': hint_sections('Recall the core idea of the M-M profiles.', 'M-M focuses on role preferences/enjoyment.', 'Balance and complementarity drive success.'),
            'guidelines': ['Link enjoyment/preferences to Margerison-McCann.'],
        }, subskill='concepts', learning_objective_id=LO_THEORY, question_family_id='margerison_mccann', concept_id='margerison_mccann', concept_group='theories', diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Conflict',
            'prompt': 'A difference, disagreement or clash between persons is called …',
            'options': ['conflict', 'consensus', 'grievance', 'cooperation'],
            'correct_index': 0,
            'explanation': 'Conflict is the difference, disagreement, disharmony or clash between persons.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections('Define the disagreement between people.', 'Disagreement/clash = conflict.', 'Consensus is the opposite - agreement.'),
            'guidelines': ['Disagreement/clash points to conflict.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='conflict_definition', concept_id='conflict', concept_group='conflict', misconception_tags=['confuse_conflict_grievance'], diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Contemporary conflict theory',
            'prompt': 'Which conflict management theory holds that conflict is unavoidable and can be beneficial if managed correctly?',
            'options': ['contemporary theory', 'traditional theory', 'behavioural theory', 'classical theory'],
            'correct_index': 0,
            'explanation': 'The contemporary theory sees conflict as a natural, unavoidable result of change that can benefit the business if managed correctly.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Contrast the two conflict theories.', 'Conflict useful/unavoidable = contemporary.', 'Conflict always bad/to be avoided = traditional.'),
            'guidelines': ['Conflict being natural/beneficial points to the contemporary view.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='conflict_theories', concept_id='contemporary_conflict', concept_group='conflict', misconception_tags=['confuse_conflict_theories'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Traditional conflict theory',
            'prompt': 'The conflict management theory that views ALL conflict as harmful and something to be avoided is the … theory.',
            'options': ['traditional', 'contemporary', 'human relations', 'systems'],
            'correct_index': 0,
            'explanation': 'The traditional theory views conflict as negative and destructive and believes it should be avoided or eliminated.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Contrast the two conflict theories.', 'Conflict = always bad = traditional.', 'Conflict = natural/possibly good = contemporary.'),
            'guidelines': ['Conflict as harmful points to the traditional view.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='conflict_theories', concept_id='traditional_conflict', concept_group='conflict', misconception_tags=['confuse_conflict_theories'], diagnostic_tags=['theory_detail']),
        with_metadata({
            'title': 'Grievance',
            'prompt': 'A concern or complaint at work, such as discrimination or excessive workload, is called a …',
            'options': ['grievance', 'consensus', 'negotiation', 'arbitration'],
            'correct_index': 0,
            'explanation': 'A grievance is a concern or complaint raised at work, for example about discrimination or workload.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Recall the term for a workplace complaint.', 'A complaint/concern = grievance.', 'Consensus is group agreement.'),
            'guidelines': ['Workplace complaint points to grievance.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='grievance_definition', concept_id='grievance', concept_group='conflict', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Consensus',
            'prompt': 'The process by which a group agrees by discussing the facts and making the best decision for the group is called …',
            'options': ['consensus', 'conflict', 'grievance', 'headhunting'],
            'correct_index': 0,
            'explanation': 'Consensus is the process used by a group to agree by discussing the facts and making the best decision for the group.',
            'difficulties': ['easy', 'medium'],
            'hint_sections': hint_sections('Recall the term for group agreement.', 'Group agreement after discussion = consensus.', 'It is reached in the norming stage.'),
            'guidelines': ['Group agreement points to consensus.'],
        }, subskill='concepts', learning_objective_id=LO_TEAM, question_family_id='consensus_definition', concept_id='consensus', concept_group='teamwork', diagnostic_tags=['definition']),
        with_metadata({
            'title': 'Workplace forums',
            'prompt': 'A key function of workplace forums is to …',
            'options': ['give employees a voice in decision-making on workplace issues', 'set the national minimum wage', 'register new companies', 'audit financial statements'],
            'correct_index': 0,
            'explanation': 'Workplace forums consult with employees on matters such as restructuring, discipline and the work environment, giving employees a collective voice.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Recall what workplace forums do.', 'Forums consult employees on workplace issues.', 'Trade unions bargain over pay; forums consult on the work environment.'),
            'guidelines': ['Consultation on workplace issues = function of forums.'],
        }, subskill='concepts', learning_objective_id=LO_CONFLICT, question_family_id='workplace_forums', concept_id='workplace_forum', concept_group='conflict', misconception_tags=['confuse_forum_union'], diagnostic_tags=['definition']),
    ]


def _application_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Identify the stage',
            'prompt': 'A newly appointed project team is polite, still getting to know one another and planning roles and work. Identify the stage of team development and motivate your answer. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The team is in the forming stage (first stage).',
                'Members have just met and are getting to know each other.',
                'They show good behaviour because they are new to the group.',
                'They are planning their work and new roles - motivation for forming.',
            ],
            'sample_answer': 'The team is in the forming stage, the first stage of Tuckman\'s model. This is clear because the members have just met, are still polite and aware of themselves, and are busy planning their work and new roles.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Match the behaviour to a stage.', 'First meeting / planning = forming.', 'Quote the scenario facts as motivation.'),
            'answer_part_hints': ['Name the stage.', 'Motivate with two facts.'],
            'guidelines': ['Motivation must quote scenario evidence.'],
            'teaching_note': 'Award the stage plus correct motivating facts.',
            'keywords': ['forming', 'first stage', 'get to know', 'planning'],
        }, subskill='application', learning_objective_id=LO_TEAM, question_family_id='tuckman_scenario', concept_id='forming', concept_group='team_development', scenario_family_id='new_project_team', diagnostic_tags=['scenario_analysis'], answer_structure_tags=['identify', 'motivate'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Belbin role analysis',
            'prompt': 'Thandi is the creative problem-solver of her team; she is full of new ideas but ignores small details. Identify the Belbin role and explain how the business can use Belbin\'s theory. (4 marks)',
            'marks': 4,
            'marking_points': [
                'Thandi plays the Planter role (creative innovator / problem-solver).',
                'Belbin identified nine roles in a balanced team.',
                'The theory is used to create a balanced team before a project starts.',
                'It also helps to allocate tasks according to members\' strengths and manage interpersonal differences.',
            ],
            'sample_answer': 'Thandi is a Planter - the creative, idea-generating problem-solver in Belbin\'s theory. A business can use Belbin\'s Role Theory to build a balanced team (all nine roles) before a project, allocate tasks to match each member\'s role and manage interpersonal differences.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Match the behaviour to a Belbin role.', 'Creativity/innovation = planter.', 'Belbin is used to balance the team and allocate tasks.'),
            'answer_part_hints': ['Name the Belbin role.', 'Explain a use of the theory.'],
            'guidelines': ['Explain a practical business use of Belbin.'],
            'teaching_note': 'Reward correct role plus a valid application of the theory.',
            'keywords': ['planter', 'creative', 'nine roles', 'balanced team'],
        }, subskill='application', learning_objective_id=LO_THEORY, question_family_id='belbin_scenario', concept_id='belbin_planter', concept_group='theories', scenario_family_id='thandi_creative', diagnostic_tags=['scenario_analysis', 'theory_application'], answer_structure_tags=['identify', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Conflict theory choice',
            'prompt': 'A manager believes all conflict is destructive and must be eliminated. Name this view and argue why the contemporary theory may serve the business better. (4 marks)',
            'marks': 4,
            'marking_points': [
                'The manager holds the traditional view of conflict.',
                'The contemporary theory sees conflict as natural and unavoidable.',
                'Managed correctly, conflict can surface problems and lead to better decisions/innovation.',
                'Suppressing all conflict may hide issues that later grow into grievances.',
            ],
            'sample_answer': 'The manager follows the traditional theory, which sees all conflict as harmful. The contemporary theory is more useful because conflict is a natural result of change; managed properly it exposes problems early, encourages discussion and can improve decisions, whereas eliminating it hides grievances that may escalate.',
            'difficulties': ['hard'],
            'hint_sections': hint_sections('Name the theory, then argue the alternative.', 'Conflict = all bad = traditional.', 'Contemporary: conflict natural and can be beneficial.'),
            'answer_part_hints': ['Name the current view.', 'Justify the contemporary theory.'],
            'guidelines': ['Justification must give a benefit of managed conflict.'],
            'teaching_note': 'Reward correct naming plus a reasoned justification.',
            'keywords': ['traditional', 'contemporary', 'natural', 'beneficial'],
        }, subskill='application', learning_objective_id=LO_CONFLICT, question_family_id='conflict_theory_justify', concept_id='contemporary_conflict', concept_group='conflict', scenario_family_id='conflict_philosophy_case', diagnostic_tags=['scenario_analysis', 'justification'], answer_structure_tags=['identify', 'justify'], minimum_mastery_score=0.6),
    ]


def _discussion_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        with_metadata({
            'title': 'Importance of teamwork',
            'prompt': 'Explain the importance of teamwork in a business. (6 marks)',
            'marks': 6,
            'marking_points': [
                'Teamwork creates a sense of unity and shared responsibility.',
                'It increases productivity and output quality.',
                'It improves job satisfaction and reduces stress.',
                'It empowers employees and uses a wider range of skills.',
                'It improves organisational effectiveness towards common goals.',
                'Members support one another and solve problems faster.',
            ],
            'sample_answer': 'Teamwork is important because it creates unity and shared responsibility, raises productivity and quality, and improves job satisfaction while reducing stress. It empowers employees, draws on a wider range of skills, and makes the organisation more effective in achieving common goals.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Explain why teamwork matters.', 'Focus on productivity, satisfaction, effectiveness.', 'Give benefits such as empowerment and quality.'),
            'answer_part_hints': ['Give benefits of teamwork.', 'Explain each benefit.'],
            'guidelines': ['Explain rather than only list.'],
            'teaching_note': 'Reward explained benefits, not bare lists.',
            'keywords': ['unity', 'productivity', 'job satisfaction', 'effectiveness', 'empowerment'],
        }, subskill='discussion', learning_objective_id=LO_TEAM, question_family_id='importance_of_teamwork', concept_id='teamwork', concept_group='teamwork', diagnostic_tags=['discussion'], answer_structure_tags=['explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Team dynamic theories',
            'prompt': 'Discuss FOUR team dynamic theories and explain why businesses use team dynamic theories. (8 marks)',
            'marks': 8,
            'marking_points': [
                'Belbin Role Theory - nine roles in action, cerebral and people groups.',
                'Insights based on Jungian Theory - extrovert/introvert personality types.',
                'The MTR-I approach - eight team roles based on Jung\'s theory.',
                'Margerison-McCann profiles - role preferences that complement one another.',
                'Businesses use these theories to explain how people function by personality type.',
                'To select the right people and create a balanced team.',
                'To allocate tasks according to members\' abilities and skills.',
                'To maximise performance and minimise conflict in the team.',
            ],
            'sample_answer': 'Four team dynamic theories are Belbin\'s Role Theory (nine roles grouped as action, cerebral and people oriented), the Jungian-based insights (extrovert and introvert types), the MTR-I approach (eight roles derived from Jung) and the Margerison-McCann profiles (complementary role preferences). Businesses use these theories to understand how people function by personality type, select the right people, allocate tasks according to ability, maximise performance and minimise conflict.',
            'difficulties': ['hard'],
            'hint_sections': hint_sections('Name four theories, then give reasons for using them.', 'Theories: Belbin, Jungian, MTR-I, Margerison-McCann.', 'Reasons: select people, allocate tasks, maximise performance, reduce conflict.'),
            'answer_part_hints': ['Describe four theories.', 'Explain why they are used.'],
            'guidelines': ['Both the theories AND the reasons must be addressed.'],
            'teaching_note': 'Split marks between the four theories and the reasons for using them.',
            'keywords': ['Belbin', 'Jungian', 'MTR-I', 'Margerison', 'personality', 'allocate tasks'],
        }, subskill='discussion', learning_objective_id=LO_THEORY, question_family_id='team_dynamic_theories_discussion', concept_id='theories', concept_group='theories', diagnostic_tags=['discussion'], answer_structure_tags=['describe', 'explain'], minimum_mastery_score=0.6),
        with_metadata({
            'title': 'Trade unions vs workplace forums',
            'prompt': 'Explain the difference between a trade union and a workplace forum. (6 marks)',
            'marks': 6,
            'marking_points': [
                'A trade union is an association of employees that bargaining over pay and conditions.',
                'A workplace forum is a structure that consults employees on workplace change.',
                'Unions represent members of a particular union; forums represent all employees.',
                'Forums deal with matters such as restructuring, discipline and the work environment.',
                'Unions may declare strikes; forums consult and make recommendations.',
                'Both aim to protect employee interests but through different mechanisms.',
            ],
            'sample_answer': 'A trade union is an employee association that negotiates (collectively bargains) over wages and conditions and may strike. A workplace forum is a structure that consults with all employees on workplace issues such as restructuring and discipline and makes recommendations. Unions represent their members and bargain, while forums represent the whole workforce and consult.',
            'difficulties': ['medium', 'hard'],
            'hint_sections': hint_sections('Contrast purpose and representation.', 'Union = bargain over pay; forum = consult on change.', 'Union = members; forum = all employees.'),
            'answer_part_hints': ['Define each.', 'Contrast their functions.'],
            'guidelines': ['Present clear differences, not similarities only.'],
            'teaching_note': 'Reward distinct, correctly matched differences.',
            'keywords': ['trade union', 'workplace forum', 'bargain', 'consult'],
        }, subskill='discussion', learning_objective_id=LO_CONFLICT, question_family_id='union_vs_forum', concept_id='workplace_forum', concept_group='conflict', diagnostic_tags=['discussion', 'comparison'], answer_structure_tags=['differentiate'], minimum_mastery_score=0.6),
    ]


# --- curated richer archetypes (grounded in the topic's official activities) ---

def _matching_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        {
            'title': 'Tuckman stages',
            'prompt': 'Match each team-development stage in Column A with its correct description in Column B.',
            'column_a': ['Forming', 'Storming', 'Norming', 'Performing', 'Mourning/adjourning'],
            'column_b': [
                'Members first meet, are polite and plan their roles and work',
                'Conflict and power struggles over leadership arise',
                'The team reaches consensus and roles are accepted',
                'The team performs at a high level and self-manages',
                'The project ends and the team breaks up',
            ],
            'correct_pairs': {
                'Forming': 'Members first meet, are polite and plan their roles and work',
                'Storming': 'Conflict and power struggles over leadership arise',
                'Norming': 'The team reaches consensus and roles are accepted',
                'Performing': 'The team performs at a high level and self-manages',
                'Mourning/adjourning': 'The project ends and the team breaks up',
            },
            'explanation': 'These are the five stages of Tuckman\'s (1965) model of team development in their correct order.',
            'marks': 5,
        },
    ]


def _crossword_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        {
            'title': 'Team dynamics crossword',
            'prompt': 'Complete the crossword using the key terms of team dynamics and conflict management.',
            'words': ['FORMING', 'STORMING', 'NORMING', 'PERFORMING', 'CONFLICT', 'CONSENSUS', 'GRIEVANCE', 'BELBIN'],
            'clues': {
                'FORMING': 'First stage of team development when members meet',
                'STORMING': 'Stage characterised by conflict and power struggles',
                'NORMING': 'Stage when the team reaches agreement and accepts roles',
                'PERFORMING': 'Stage of high performance and self-management',
                'CONFLICT': 'A disagreement or clash between persons',
                'CONSENSUS': 'Group agreement reached by discussing the facts',
                'GRIEVANCE': 'A complaint or concern raised at work',
                'BELBIN': 'Theorist of the nine team roles',
            },
            'grid_size': 12,
            'explanation': 'Answers are the Tuckman stages, conflict terms and a theorist of this topic.',
            'marks': 8,
        },
    ]


def _essay_pool(r: random.Random) -> List[Dict[str, Any]]:
    return [
        {
            'title': 'Team dynamics essay',
            'prompt': 'Write an essay on team dynamics and conflict management in which you: (a) outline the five stages of team development; (b) explain why businesses use team dynamic theories; (c) define conflict and distinguish between the traditional and contemporary conflict management theories; and (d) explain the function of workplace forums.',
            'rubric': [
                {'criterion': 'Stages of team development', 'description': 'Explains forming, storming, norming, performing and mourning/adjourning in order with a feature of each.', 'marks': 10},
                {'criterion': 'Reasons for using theories', 'description': 'Explains that theories help understand personalities, select people, allocate tasks, maximise performance and minimise conflict.', 'marks': 8},
                {'criterion': 'Conflict and its theories', 'description': 'Defines conflict and contrasts the traditional (avoid all conflict) with the contemporary (natural, can be beneficial) theory.', 'marks': 12},
                {'criterion': 'Workplace forums', 'description': 'Explains the consultative function of workplace forums on workplace change and issues.', 'marks': 6},
                {'criterion': 'Structure and expression', 'description': 'Clear introduction, logical paragraphs, conclusion and business terminology.', 'marks': 4},
            ],
            'sample_answer': 'Teams develop through five Tuckman stages: forming (meeting and planning), storming (conflict and power struggles), norming (consensus and accepted roles), performing (high, self-managing performance) and mourning/adjourning (the project ends and the team breaks up). Businesses apply team dynamic theories (Belbin, Jungian insights, MTR-I, Margerison-McCann) to understand how people function by personality, select the right people, allocate tasks to ability, maximise performance and minimise conflict. Conflict is a disagreement or clash between persons; the traditional theory treats all conflict as harmful and to be avoided, whereas the contemporary theory sees it as a natural, unavoidable result of change that can be beneficial if managed correctly. Finally, workplace forums consult employees on matters such as restructuring, discipline and the work environment, giving the workforce a collective voice distinct from the bargaining role of trade unions.',
            'marks': 40,
            'min_words': 350,
            'max_words': 700,
            'keywords': ['forming', 'storming', 'norming', 'performing', 'conflict', 'contemporary', 'forum'],
        },
    ]


generate = make_generate(
    META, _concept_pool, _application_pool, _discussion_pool,
    matching_pool=_matching_pool,
    crossword_pool=_crossword_pool,
    essay_pool=_essay_pool,
)
