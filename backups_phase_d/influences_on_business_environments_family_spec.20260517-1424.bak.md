# Influences on Business Environments Family Spec

## Purpose

This document externalizes the Grade 11 Business Studies topic specification for `Influences on business environments` so topic coverage can be audited without reading generator code only.

Generator source:

`caps-ai-backend/app/utils/grade11_business_studies/term_1/influences_on_business_environments_generator.py`

## Topic identity

- `topic_id`: `grade11_business_studies`
- `subtopic_id`: `influences_on_business_environments`
- `curriculum_reference`: `Term 1 > Influences on business environments`

## Curriculum sources

- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Term 1/1 Influences on business environments.md`
- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Term 1/ControlledTest_Term1.md`
- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Mixed-1.md`
- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Mixed-2.md`

## Metadata contract

Each generated family line should preserve the following stable fields:

- `topic_id`
- `subtopic_id`
- `subskill`
- `learning_objective_id`
- `concept_id`
- `concept_group`
- `question_family_id`
- `scenario_family_id` where applicable
- `retry_variant`
- `curriculum_reference`
- `diagnostic_tags`
- `answer_structure_tags`
- `minimum_mastery_score` for typed items

Runtime question `id` values remain instance-specific and are not part of the stable family identity.

## Mastery thresholds

- `concepts`: `1.0`
- `application`: `0.6`
- `discussion`: `0.7`

## Retry-variant policy

### Concepts

- `core`
- `guided`
- `reworded`

### Application

- `core`
- `guided`
- `reworded`
- `transfer`

### Discussion

- `core`
- `guided`
- `reworded`

## Scenario-variance rule

Scenario-based variance uses:

`caps-ai-backend/app/utils/grade11_business_studies/names.py`

This helper may vary:

- business names
- supplier names
- product types
- export destinations

This variation is surface-only.

The following must remain stable across retries in the same mastery line:

- `learning_objective_id`
- `question_family_id`
- `scenario_family_id`
- `marking_points`
- `minimum_mastery_score`

## Learning objective map

| Learning objective ID | Description |
| --- | --- |
| `lo_components_of_business_environments` | Identify and differentiate components of business environments |
| `lo_control_over_business_environments` | Explain why control differs across micro, market and macro environments |
| `lo_identify_challenges_and_control_from_scenarios` | Identify scenario challenges, classify environments, and state extent of control |
| `lo_recommend_macro_environment_involvement` | Recommend ways businesses can be involved in the macro environment |
| `lo_adapt_to_business_environment_challenges` | Explain or advise on strategic responses and adaptation |
| `lo_importance_of_understanding_influences` | Explain why understanding influences matters and what happens when they are ignored |
| `lo_benefits_of_macro_environment_involvement` | Discuss the benefits of business involvement in the macro environment |

## Family inventory by subskill

### Concepts

| Question family ID | Concept ID | Concept group | Retry variants | Notes |
| --- | --- | --- | --- | --- |
| `internal_vs_external_influence` | `internal_vs_external_influences` | `environment_components` | `core` | Foundational internal vs external recognition |
| `macro_influence_classification` | `macro_environment_classification` | `environment_components` | `core` | Broad external classification |
| `control_over_influences` | `monitoring_legal_influences` | `extent_of_control` | `core` | Legal influence reasoning |
| `stakeholder_influence` | `market_environment_suppliers` | `market_environment_components` | `core` | Supplier influence on inputs and costs |
| `technological_influence` | `macro_environment_technology` | `macro_environment_components` | `core` | Technology as macro influence |
| `micro_market_macro_components_naming` | `micro_environment_components` / `market_environment_components` / `macro_environment_components` | `environment_components` | `core`, `guided`, `reworded` | Three linked component-recognition lines |
| `control_extent_reasoning` | `extent_of_control_levels` | `extent_of_control` | `core`, `guided`, `reworded` | Why control differs across environments |

### Application

| Question family ID | Concept ID | Concept group | Scenario family ID | Retry variants | Notes |
| --- | --- | --- | --- | --- | --- |
| `scenario_analysis_general` | `scenario_influence_identification` | `scenario_reasoning` | `brightpath_internal_macro_mix` | `core` | Internal plus macro influence explanation |
| `influence_classification_written` | `multiple_external_influences` | `scenario_reasoning` | `retailer_multi_influence_case` | `core` | Multi-influence written explanation |
| `technology_opportunity_and_risk` | `technology_opportunities_and_challenges` | `adaptation_and_response` | `technology_change_response` | `core` | Opportunity plus challenge explanation |
| `challenge_identification_from_scenario` | `challenge_extraction` | `scenario_reasoning` | `bavi_three_environment_challenges` | `core`, `guided`, `reworded`, `transfer` | Extract three challenges from one case line |
| `challenge_identification_from_scenario` | `challenge_extraction` | `scenario_reasoning` | `joes_supermarket_three_environment_challenges` | `core` | Alternative curriculum-backed three-environment challenge extraction line |
| `environment_classification_from_scenario` | `environment_classification` | `scenario_reasoning` | `bavi_three_environment_challenges` | `core`, `guided`, `reworded`, `transfer` | Classify challenges into micro, market, macro |
| `environment_classification_from_scenario` | `environment_classification` | `scenario_reasoning` | `joes_supermarket_three_environment_challenges` | `core` | Alternative curriculum-backed classification line using Joe's Supermarket |
| `extent_of_control_from_scenario` | `extent_of_control_levels` | `extent_of_control` | `bavi_three_environment_challenges` | `core`, `guided`, `reworded`, `transfer` | Apply full-limited-none control ladder |
| `extent_of_control_from_scenario` | `extent_of_control_levels` | `extent_of_control` | `joes_supermarket_three_environment_challenges` | `core` | Alternative curriculum-backed control line using Joe's Supermarket |
| `macro_environment_involvement_recommendations` | `macro_environment_involvement` | `macro_involvement` | `majeed_tiles_macro_involvement` | `core`, `guided`, `reworded`, `transfer` | Recommend practical macro involvement actions |
| `strategic_responses_lobbying_networking_adaptation` | `strategic_responses` | `adaptation_and_response` | `strategic_response_advice` | `core`, `guided`, `reworded`, `transfer` | Strategic-response and adaptation advice |
| `table_guided_three_environment_response` | `three_environment_table_response` | `scenario_reasoning` | `vincent_sportswear_table_case` | `transfer` | Structured challenge plus control response |
| `table_guided_three_environment_response` | `three_environment_table_response` | `scenario_reasoning` | `joes_supermarket_table_case` | `core` | Structured curriculum-note table-style challenge plus control response |

### Discussion

| Question family ID | Concept ID | Concept group | Retry variants | Notes |
| --- | --- | --- | --- | --- |
| `importance_of_environmental_awareness` | `importance_of_environmental_awareness` | `discussion_reasoning` | `core`, `guided`, `reworded` | Why environmental understanding matters for decision-making |
| `internal_vs_external_balance` | `internal_vs_external_influences` | `discussion_reasoning` | `core`, `guided`, `reworded` | Differentiate internal and external influences and explain significance |
| `ignoring_influences_consequences` | `ignoring_influences_consequences` | `discussion_reasoning` | `core`, `guided`, `reworded` | Long-term consequences of ignoring influences |
| `benefits_of_macro_environment_involvement` | `macro_environment_involvement_benefits` | `macro_involvement` | `core`, `guided`, `reworded` | Advantages of positive macro-environment involvement |

## Scenario family map

| Scenario family ID | Used by families | Core purpose |
| --- | --- | --- |
| `brightpath_internal_macro_mix` | `scenario_analysis_general` | Mix internal leadership/goals with macro pressures |
| `retailer_multi_influence_case` | `influence_classification_written` | Explain multiple external influences in one retailer case |
| `technology_change_response` | `technology_opportunity_and_risk` | Explain technology as both opportunity and challenge |
| `bavi_three_environment_challenges` | `challenge_identification_from_scenario`, `environment_classification_from_scenario`, `extent_of_control_from_scenario` | One shared mastery line for challenge extraction, classification and control |
| `joes_supermarket_three_environment_challenges` | `challenge_identification_from_scenario`, `environment_classification_from_scenario`, `extent_of_control_from_scenario` | Alternative note-backed mastery line using management, competitor, and legislation/wage pressures |
| `majeed_tiles_macro_involvement` | `macro_environment_involvement_recommendations` | Recommend wider macro-environment involvement actions |
| `strategic_response_advice` | `strategic_responses_lobbying_networking_adaptation` | Strategic responses to environmental challenges |
| `vincent_sportswear_table_case` | `table_guided_three_environment_response` | Structured row-by-row challenge and control response |
| `joes_supermarket_table_case` | `table_guided_three_environment_response` | Structured row-by-row challenge and control response using Joe's Supermarket |

## Discussion objective map

| Discussion family | Expected reasoning shape |
| --- | --- |
| `importance_of_environmental_awareness` | importance discussion with reasons and consequences |
| `internal_vs_external_balance` | differentiate plus explain significance |
| `ignoring_influences_consequences` | consequence explanation linked to long-term survival |
| `benefits_of_macro_environment_involvement` | advantages discussion across reputation, people, and long-term opportunity |

## Misconception focus areas

- confusing internal and external influences
- treating market-environment actors as fully controllable
- confusing market and macro examples
- naming scenario details without classifying or explaining them
- giving vague macro-involvement suggestions without practical action verbs
- discussing strategic responses without linking them to adaptation
- listing discussion points without explaining why they matter

## Current rollout notes

This topic now supports:

- metadata-driven retry selection
- same-family mastery progression
- stable scenario-family routing
- authored retry ladders across key concept, application, and discussion lines
- controlled scenario-surface variation through the BS names helper
- more than one curriculum-backed three-environment scenario line for challenge/classification/control work

## Next extension points

- add additional curriculum-backed scenario lines beyond the current Bavi, Joe's, Majeed, BrightPath, retailer, and Vincent cases
- add more concept families for broader micro, market and macro component coverage
- externalize a reusable Business Studies metadata contract once the next topic follows the same pattern
