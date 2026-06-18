# The Challenges of the Business Environments Family Spec

## Purpose

This document externalizes the Grade 11 Business Studies topic specification for `The challenges of the business environments` so topic coverage can be audited without reading generator code only.

Generator source:

`caps-ai-backend/app/utils/grade11_business_studies/term_1/the_challenges_of_the_business_environments_generator.py`

## Topic identity

- `topic_id`: `grade11_business_studies`
- `subtopic_id`: `challenges_of_the_business_environments`
- `curriculum_reference`: `Term 1 > The challenges of the business environments`

## Curriculum sources

- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Term 1/2 The challenges of the business environments.md`
- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Term 1/ControlledTest_Term1.md`
- `caps-ai-backend/curriculum_docs/BusinessStudies_Gr11/Mixed-1.md`

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

This helper currently varies:

- business names for competition-response cases

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
| `lo_challenges_of_micro_environment` | Identify and explain challenges that arise within the micro environment |
| `lo_challenges_of_market_environment` | Identify and discuss challenges found in the market environment |
| `lo_challenges_of_macro_environment` | Identify and explain challenges in the macro environment |
| `lo_overcome_competition_in_market_environment` | Recommend ways businesses can overcome competition in the market |
| `lo_examples_of_contemporary_legislation` | Recall examples of contemporary legislation affecting business operations |
| `lo_identify_challenges_from_scenarios` | Extract and classify challenges from integrated scenarios |

## Family inventory by subskill

### Concepts

| Question family ID | Concept ID | Concept group | Retry variants | Notes |
| --- | --- | --- | --- | --- |
| `micro_challenge_classification` | `micro_environment_challenges` | `challenge_classification` | `core` | Classify internal employee-related challenges as micro |
| `market_challenge_classification` | `market_environment_challenges` | `challenge_classification` | `core` | Classify supplier-related challenges as market |
| `macro_challenge_classification` | `macro_environment_challenges` | `challenge_classification` | `core` | Classify legal or labour-related challenges as macro |
| `consumer_behaviour_identification` | `consumer_behaviour_challenges` | `market_challenges` | `core` | Identify consumer-behaviour challenges from descriptions |
| `competition_response_reasoning` | `competition_response_strategies` | `adaptation_and_response` | `core` | Recognize suitable responses to competition |
| `contemporary_legislation_example` | `contemporary_legislation_examples` | `macro_challenges` | `core` | Distinguish legislation examples from internal tools or activities |

### Application

| Question family ID | Concept ID | Concept group | Scenario family ID | Retry variants | Notes |
| --- | --- | --- | --- | --- | --- |
| `micro_challenge_identification_from_statements` | `micro_environment_challenges` | `challenge_classification` | `temba_micro_challenges_case` | `core` | Identify common micro-environment challenges from four statements |
| `challenge_identification_from_scenario` | `challenge_extraction` | `scenario_reasoning` | `steyn_three_environment_challenges` | `core`, `guided`, `reworded`, `transfer` | Extract employee, crime, and supplier challenges from one case line |
| `challenge_classification_from_scenario` | `environment_challenge_classification` | `scenario_reasoning` | `steyn_three_environment_challenges` | `core`, `guided`, `reworded`, `transfer` | Classify Steyn scenario evidence into micro, market, and macro environments |
| `competition_overcome_recommendations` | `competition_response_strategies` | `adaptation_and_response` | `competition_response_advice` | `core`, `guided`, `reworded`, `transfer` | Recommend practical ways to overcome competition |
| `macro_challenge_identification_with_motivation` | `macro_environment_challenges` | `scenario_reasoning` | `maureen_lodge_macro_case` | `core` | Identify macro challenges and motivate with scenario quotes |
| `contemporary_legislation_listing` | `contemporary_legislation_examples` | `macro_challenges` |  | `core` | List examples of legislation affecting business operations |

### Discussion

| Question family ID | Concept ID | Concept group | Retry variants | Notes |
| --- | --- | --- | --- | --- |
| `market_environment_challenges_discussion` | `market_environment_challenges` | `discussion_reasoning` | `core`, `guided`, `reworded` | Discuss supplier, consumer-behaviour, and demographic or psychographic challenges |
| `macro_environment_challenges_discussion` | `macro_environment_challenges` | `discussion_reasoning` | `core`, `guided`, `reworded` | Explain broad macro-environment challenges and their effects on businesses |

## Scenario family map

| Scenario family ID | Used by families | Core purpose |
| --- | --- | --- |
| `temba_micro_challenges_case` | `micro_challenge_identification_from_statements` | Identify common micro-environment challenges from fixed activity statements |
| `steyn_three_environment_challenges` | `challenge_identification_from_scenario`, `challenge_classification_from_scenario` | Shared mastery line for extracting and classifying employee, crime, and supplier challenges |
| `competition_response_advice` | `competition_overcome_recommendations` | Recommend competition-response strategies in a business case context |
| `maureen_lodge_macro_case` | `macro_challenge_identification_with_motivation` | Identify macro challenges from legislation and socio-economic evidence |

## Discussion objective map

| Discussion family | Expected reasoning shape |
| --- | --- |
| `market_environment_challenges_discussion` | explain how supply, customer behaviour, and customer-profile shifts affect business performance |
| `macro_environment_challenges_discussion` | explain broad external challenges and link them to demand, compliance, cost, risk, or competition |

## Misconception focus areas

- confusing micro and market challenges
- treating suppliers as internal rather than market-environment actors
- confusing market and macro pressures
- naming scenario details without classifying them
- discussing competition responses without practical action verbs
- listing legislation incorrectly as internal business tools
- discussing broad challenges without linking them to business impact

## Current rollout notes

This topic now supports:

- metadata-driven retry selection
- same-family mastery progression
- stable scenario-family routing
- authored retry ladders across key application and discussion lines
- a minimum viable coverage slice for micro, market, and macro challenge classification
- curriculum-backed scenario lines for Steyn Manufacturers, Maureen B&B Lodge, and competition-response advice

## Next extension points

- add more concept families for detailed micro, market, and macro challenge coverage
- add more scenario lines for socio-economic issues, labour restrictions, and globalisation
- add explicit extent-of-control families if this topic is later blended with cross-topic environment reasoning
- externalize a reusable Business Studies metadata contract once Topic 2 confirms the same rollout pattern
