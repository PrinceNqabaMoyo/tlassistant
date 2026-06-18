---
description: Grade 11 Business Studies pilot enhancement plan
---

# BSGR11 Enhancement Plan

## Purpose

Stabilize the Grade 11 Business Studies pilot (`Influences on business environments`) into an acceptable, reusable workflow design before rolling the pattern out to other Business Studies grades and topics.

This plan starts with an audit of the current pilot's curriculum/content metadata and then defines:

1. A mastery-driven scaffold workflow
2. A future diagnostic-to-mastery workflow
3. A phased implementation sequence that can be reused across later BS topics

## Audit Scope

Audited implementation folder:

`C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_business_studies`

Audited curriculum source folder:

`C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\curriculum_docs\BusinessStudies_Gr11`

Files currently present:

- `__init__.py`
- `names.py`
- `term_1\__init__.py`
- `term_1\influences_on_business_environments_family_spec.md`
- `term_1\influences_on_business_environments_generator.py`

Curriculum documents reviewed for the pilot topic and paper-style scope:

- `Term 1\1 Influences on business environments.md`
- `Term 1\ControlledTest_Term1.md`
- `Mixed-1.md`
- `Mixed-2.md`

## Audit Findings

### 1. Current pilot content structure is clean but minimal

The pilot generator already separates content into three pools:

- `concepts`
- `application`
- `discussion`

This aligns well with the current Grade 11 scaffold stepper.

### 2. Useful teaching metadata already exists

The generator already exposes several good instructional fields that are reusable for mastery workflows:

- `hint_sections`
- `marking_points`
- `sample_answer`
- `ideal_answer`
- `guidelines`
- `teaching_note`
- `answer_part_hints` for typed items
- `keywords` for typed semantic marking
- `difficulties`

This is enough to support:

- richer feedback
- memo comparison
- progressive hints
- partial-credit semantic scoring

### 3. The main gap is identity metadata, not teaching metadata

The current pilot does **not** assign stable metadata such as:

- `concept_id`
- `concept_group`
- `subtopic_id`
- `scenario_family_id`
- `question_family_id`
- `learning_objective_id`
- `misconception_tags`
- `prerequisite_tags`
- `retry_variant`
- `diagnostic_tags`

Without those fields, the system cannot reliably do any of the following:

- retry the **same concept** after failure
- reword the same concept intentionally
- distinguish “same concept, new wording” from “new concept in same step”
- track user weakness at concept/family level
- start mastery at the learner’s weakest concept cluster

### 4. The current pilot can support subskill mastery, but not true concept mastery

At present, the pilot can say:

- the learner is in `concepts`
- the learner is in `application`
- the learner is in `discussion`

But it cannot say:

- this learner is weak on `internal vs external influences`
- this learner repeatedly misses `macro influence classification`
- this learner can name influences but cannot explain business effects in scenarios

### 5. Semantic marking is usable, but the progression threshold needs design tightening

The Grade 11 API marks typed answers using keyword coverage and length-based partial credit.

This is a good pilot marker, but for mastery progression the app should not treat every positive score as equivalent.

Current implication:

- a weak partial answer can still qualify as “move on” if the workflow only checks `score > 0`

That is too permissive for mastery-driven progression.

### 6. Separate curriculum docs do exist and should be treated as the source of truth

The generator folder contains implementation code only, but the actual curriculum notes, revision material and paper-style questions live under:

- `caps-ai-backend\curriculum_docs\BusinessStudies_Gr11`

These documents should be treated as the authoritative scope reference for the pilot.

The pilot topic document confirms that the implemented topic is expected to cover at least these learning objectives:

- name the components of the micro, market and macro environments
- explain why businesses have more control over micro, less over market and no control over macro
- identify challenges from scenarios and state the extent of control over each environment
- recommend ways businesses can be involved in the macro environment
- discuss the benefits of businesses being involved in the macro environment

The mixed and controlled-test docs also show the intended exam-style range for Grade 11 BS, including:

- MCQ recall/classification
- scenario quotation and classification tasks
- extent-of-control responses
- recommendation/advice questions
- explanation/discussion questions
- structured table-guided responses

### 7. The current pilot under-covers parts of the documented curriculum scope

Relative to the curriculum docs, the pilot already covers some core foundations well:

- internal vs external influence recognition
- stakeholder and macro influence classification
- scenario-based explanation
- broad discussion of why environmental understanding matters

But the pilot is still thin or missing in several curriculum-backed areas:

- explicit naming of components across micro, market and macro environments
- systematic “extent of control” questions across the three environments
- challenge-identification tables from scenario evidence
- recommendation/suggestion items on how businesses can be involved in the macro environment
- benefits/advantages of business involvement in the macro environment
- strategic responses such as lobbying, networking, bargaining and adaptation strategies
- more paper-like direct/indirect question forms drawn from controlled-test style prompts

This means the pilot is not only missing mastery metadata; it is also still missing some curriculum breadth and question-form breadth.

## Conclusion of Audit

The pilot is **strong enough to evolve**, but it is not yet a true mastery engine.

The most important missing layer is:

- stable curriculum/objective metadata
- retry-family metadata
- weakness-tracking metadata
- fuller curriculum coverage aligned to the Grade 11 notes and test documents

These should be added before the pilot workflow is generalized to other topics.

## Implementation status update

Since the audit, the pilot has moved materially closer to the target model:

- stable metadata has been added to the Grade 11 BS generator via a shared metadata helper
- typed families now carry `minimum_mastery_score` values aligned to mastery gating
- the backend and scaffold now support same-family retry routing by metadata rather than random same-subskill retries
- authored retry variants now exist across key concept, application and discussion family lines
- a Grade 11 BS `names.py` helper now provides controlled scenario-surface variance for business and supplier names while preserving stable family metadata

This means the remaining work is no longer “introduce metadata from scratch,” but rather:

- extend the same pattern across future BS topics
- keep the family inventory and retry ladders curriculum-aligned
- document the reusable generator contract clearly enough for rollout

# Target Workflow Design

## Phase A target: mastery-driven scaffold

The Grade 11 pilot should become a genuine mastery scaffold with the following behavior:

### Mastery progression principles

- The learner should **not** move to a new step just because they attempted a question.
- The learner should progress when they meet a meaningful threshold for that step.
- Failure should trigger **same-concept remediation**, not random movement within the same broad subskill.
- The system should distinguish:
  - same exact question
  - same concept, reworded
  - same concept, easier variant
  - same concept, transfer variant

### Recommended progression by step

#### Concepts (MCQ)

Progress threshold:

- require `is_correct === true`

If learner is wrong:

- retry the same `concept_id`
- first retry should use the same concept with clearer distractor logic or stronger hints
- second retry should use a different wording of the same concept
- after repeated failure, show memo + explanation and keep the learner inside the same concept family

#### Application / Scenario Analysis

Progress threshold:

- require at least **60% to 70%** of marks, not merely `score > 0`

If learner is below threshold:

- give a new scenario from the same `scenario_family_id`
- preserve the same target learning objective
- optionally reduce difficulty or increase scaffolding

Suggested retry ladder:

- Attempt 1: standard scenario
- Attempt 2: same concept family, simpler evidence cues
- Attempt 3: same concept family, guided structure prompt + answer-part hints

#### Discussion

Progress threshold:

- require at least **70%** or a “full-coverage band” threshold

If learner is below threshold:

- ask another question from the same `question_family_id` or `learning_objective_id`
- tighten structure support via answer-part hints and memo comparison

After learner achieves discussion threshold:

- mark scaffold sequence complete
- show completion summary
- recommend either:
  - another challenge at the same topic
  - a mixed mastery check
  - a diagnostic/practice handoff

## Phase B target: diagnostic-to-mastery flow

Once the mastery scaffold is stable, add a separate diagnostic mode.

### Diagnostic mode principles

- free progression
- broad topic coverage
- no hard gating
- optimized for weakness detection, not mastery proof

### Diagnostic mode structure

Recommended first version:

- 2 concept items
- 2 application/scenario items
- 1 discussion item

Track performance by:

- `subskill`
- `concept_id`
- `learning_objective_id`
- `question_family_id`
- score band
- attempt count

### Diagnostic outcome

At the end of diagnostic mode, generate a weakness profile such as:

- strong in classification concepts
- weak in scenario explanation
- weak in linking influence to business effect
- weak in extended discussion structure

Then route the learner into mastery mode starting at:

- weakest subskill first
- then weakest concept family within that subskill

# Required Data Model Upgrades

## 1. Add stable content metadata to every question archetype

Each item in the pilot generator should gain fields like:

- `topic_id`
- `subtopic_id`
- `subskill`
- `learning_objective_id`
- `concept_id`
- `concept_group`
- `question_family_id`
- `scenario_family_id` for application items
- `difficulty_band`
- `retry_variant`
- `misconception_tags`
- `diagnostic_tags`
- `curriculum_reference`

## 2. Separate content identity from runtime question id

Keep random runtime `id` values for rendering, but also add a stable identity layer:

- runtime `id`: unique per generated question instance
- stable content IDs: used for weakness tracking and mastery routing

## 3. Add mastery feedback metadata

Recommended optional fields:

- `minimum_mastery_score`
- `mastery_rule`
- `recommended_followup_family`
- `fallback_family`
- `supports_reteach_prompt`

## 4. Add controlled scenario-surface variance

Scenario-based Business Studies families should support light contextual variation without changing the learning target.

Recommended pattern:

- use a subject-specific helper such as `grade11_business_studies/names.py`
- allow variation in business names, supplier names, product types and export destinations where appropriate
- keep `question_family_id`, `scenario_family_id`, `learning_objective_id`, marking points and mastery thresholds stable
- treat contextual names as prompt-surface variance only, not as part of the marking contract

Success check:

- retries feel less repetitive while the system still recognises them as the same mastery family line

# Step-by-Step Implementation Plan

## Step 1. Expand pilot content metadata in the generator

Update `influences_on_business_environments_generator.py` so every pool item includes stable curriculum and family metadata.

Deliverables:

- Add `concept_id` / `learning_objective_id` / `question_family_id`
- Add `scenario_family_id` for application items
- Add `retry_variant` labels such as `core`, `reworded`, `guided`, `transfer`
- Add `misconception_tags` where applicable

Success check:

- Every generated question can be linked back to a stable concept family

## Step 1A. Align the pilot generator with the documented Grade 11 topic scope

Expand the pilot question families so the implemented topic covers the major curriculum objectives and common paper-style prompts evidenced in the Grade 11 docs.

Deliverables:

- add question families for micro/market/macro component naming
- add scenario families for challenge identification and environment classification
- add “extent of control” response families
- add recommendation families for business involvement in the macro environment
- add discussion families for advantages/benefits of business involvement in the macro environment
- add strategic response items such as lobbying, networking, collective influence and adaptation strategies
- add more paper-like direct/indirect question forms drawn from controlled-test style prompts

Success check:

- the pilot topic can visibly trace its generator families back to the curriculum notes and controlled-test style prompts

## Step 1B. Add controlled scenario variance to scenario families

Add a Grade 11 BS-specific scenario helper so repeated attempts can vary names and surface context without changing the mastery target.

Deliverables:

- add `grade11_business_studies/names.py`
- reuse the existing accounting name bank where helpful, but expose BS-friendly business suffix groups
- apply the helper to scenario-based application families only
- keep semantic marking and mastery metadata independent from the randomized names

Success check:

- the same family line can produce slightly different scenario surfaces while remaining traceable to one stable `scenario_family_id`

## Step 2. Normalize semantic mastery thresholds

Update the Grade 11 marking and/or frontend progression rules so typed answers use mastery thresholds that vary by step.

Recommended threshold policy:

- `concepts`: exact correctness
- `application`: at least 60% of marks
- `discussion`: at least 70% of marks

Success check:

- progression decisions are based on explicit mastery thresholds, not `score > 0`

## Step 3. Replace random same-subskill retries with same-family retries

Update the scaffold fetch flow so failed answers do not request an arbitrary question from the same broad subskill.

Instead, request:

- same `concept_id` or `question_family_id`
- next `retry_variant`
- reduced or guided difficulty where needed

Success check:

- a learner who fails a scenario-analysis item stays on the same targeted concept family

## Step 4. Tighten scaffold navigation

Frontend scaffold changes for the Grade 11 pilot:

- hide or disable shell-level free `Next Question` in mastery mode
- prevent manual step jumping to locked future steps
- show mastery progress within a step
- show retry state such as:
  - Attempt 1 of 3
  - Same concept, guided retry
  - Same concept, transfer retry

Success check:

- learners cannot bypass mastery via open shell navigation

## Step 5. Add scaffold completion behavior

After discussion mastery is achieved:

- show topic completion card
- summarize strengths and weak points
- offer:
  - another challenge set
  - move to practice
  - start mixed mastery check

Success check:

- scaffold no longer ends with an endless “try another discussion question” loop

## Step 6. Add diagnostic mode specification

Define a separate Grade 11 BS diagnostic route and controller behavior.

Diagnostic should:

- allow free progression
- collect structured results by concept family
- produce a weakness profile

Success check:

- the app can recommend a mastery starting point after diagnostic completion

## Step 7. Add learner state model for weakness tracking

Introduce a learner progress structure in frontend state first, then later persist if needed.

Recommended tracked fields:

- `question_family_id`
- `concept_id`
- attempt history
- recent score band
- mastery achieved boolean
- hint dependency level
- memo usage frequency

Success check:

- the scaffold can adapt based on the learner’s prior failures

## Step 8. Externalize curriculum notes/specification

Create topic-specific curriculum support docs under the Grade 11 Business Studies backend area.

Recommended docs:

- topic scope and boundaries
- concept inventory
- question family map
- scenario family map
- discussion objectives
- misconceptions map

Success check:

- topic coverage can be audited without reading generator code only

# Recommended Implementation Order

## Wave 1: make the pilot mastery-safe

1. Add stable metadata
2. Align generator families to the documented curriculum scope
3. Tighten thresholds
4. Implement same-family retry routing
5. Lock scaffold navigation
6. Add scaffold completion state

## Wave 2: make the pilot diagnostically intelligent

7. Design diagnostic mode
8. Add weakness profiling
9. Route diagnostic results into mastery start points

## Wave 3: prepare for rollout to other BS topics and grades

10. Externalize curriculum specs
11. Create a reusable BS generator metadata contract
12. Create reusable mastery hooks/components
13. Apply the pattern to the next Grade 11 BS topic, then Grade 10 BS topics

# Coverage Matrix: Influences on business environments

## Curriculum objective and family coverage

| Curriculum objective / family | Evidence in Grade 11 docs | Current pilot coverage | Gap level | Recommended generator families | Recommended mastery metadata |
| --- | --- | --- | --- | --- | --- |
| Name the components of the micro environment | Topic notes list vision, mission, goals, structure, resources, culture, leadership, business functions | Partially implied by internal-vs-external MCQ only | High | `micro_components_naming`, `micro_components_recognition`, `micro_component_examples` | `learning_objective_id`, `concept_id`, `question_family_id`, `retry_variant`, `curriculum_reference` |
| Name the components of the market environment | Topic notes and Activity 2 ask for market environment components | Supplier-focused item only | High | `market_components_naming`, `market_components_mcq`, `market_component_from_scenario` | `learning_objective_id`, `concept_id`, `question_family_id`, `misconception_tags`, `curriculum_reference` |
| Name the components of the macro environment | Topic notes list social, political, legal, economic, technological, physical, global | Macro classification appears, but not systematic component coverage | Medium | `macro_components_naming`, `macro_component_classification`, `macro_component_examples` | `learning_objective_id`, `concept_id`, `question_family_id`, `retry_variant`, `curriculum_reference` |
| Explain why control differs across micro, market and macro | Learning objective explicitly states more control over micro, less over market, no control over macro | Partially covered through scattered explanation items | High | `control_extent_reasoning`, `why_micro_more_control`, `why_market_limited_control`, `why_macro_no_control` | `learning_objective_id`, `concept_group`, `question_family_id`, `difficulty_band`, `curriculum_reference` |
| Identify challenges in each environment from scenario evidence | Topic notes, revision, mixed papers and controlled test use scenario extraction tasks | Partially covered by broad application items | High | `challenge_quote_from_scenario`, `challenge_environment_mapping`, `three_environment_scenario_set` | `learning_objective_id`, `scenario_family_id`, `question_family_id`, `diagnostic_tags`, `curriculum_reference` |
| State the extent of control for each environment in scenario context | Topic notes and controlled test explicitly ask for extent of control per environment | Not explicitly implemented as a family | High | `extent_of_control_by_environment`, `scenario_control_statement`, `table_guided_control_response` | `learning_objective_id`, `concept_id`, `question_family_id`, `scenario_family_id`, `retry_variant` |
| Recommend ways businesses can be involved in the macro environment | Topic notes include a dedicated section and revision question on this | Not currently represented | High | `macro_involvement_recommendations`, `macro_involvement_from_scenario`, `recommend_other_ways` | `learning_objective_id`, `question_family_id`, `scenario_family_id`, `curriculum_reference`, `answer_structure_tags` |
| Discuss benefits of business involvement in the macro environment | Topic notes include benefits/advantages section and revision discussion prompt | Not currently represented | High | `macro_involvement_benefits_discussion`, `advantages_of_macro_involvement`, `benefit_explanation_short_form` | `learning_objective_id`, `question_family_id`, `keywords`, `mark_band_threshold`, `curriculum_reference` |
| Explain strategic responses such as lobbying, networking, alliances and adaptation | Topic notes and controlled test include lobbying, strategic responses and adaptation ideas | Only lightly implied | High | `strategic_responses_to_environment`, `lobbying_reasons`, `adaptation_advice`, `collective_influence_examples` | `learning_objective_id`, `concept_group`, `question_family_id`, `misconception_tags`, `curriculum_reference` |
| Discuss why understanding influences matters for managerial decisions | Current discussion family aligns well with topic notes | Already covered well | Low | Keep `importance_of_environmental_awareness` family and add retry variants | `learning_objective_id`, `question_family_id`, `retry_variant`, `mark_band_threshold` |
| Differentiate internal and external influences and explain why both matter | Current discussion family aligns well | Already covered well | Low | Keep `internal_vs_external_balance` family and add variants | `learning_objective_id`, `concept_id`, `question_family_id`, `retry_variant` |
| Explain consequences of ignoring environmental influences | Current discussion family aligns reasonably | Covered, but narrow | Medium | Keep `ignoring_influences_consequences` and add scenario-linked variants | `learning_objective_id`, `question_family_id`, `scenario_family_id`, `retry_variant` |

## Paper-style question form coverage

| Paper-style form seen in docs | Current pilot state | Needed upgrade |
| --- | --- | --- |
| MCQ recall/classification | Present | Broaden to full micro/market/macro component coverage and control concepts |
| Scenario quotation of challenge evidence | Weak | Add explicit extract-and-classify families |
| Table-guided environment/control responses | Missing | Add structured response families that preserve row-by-row reasoning |
| Direct short explanation questions | Partial | Add tighter objective-linked short-form items |
| Advice / recommendation questions | Missing | Add recommendation families for macro involvement and strategic responses |
| Extended discussion questions | Present | Add stronger family identity and mastery thresholds |

## Pilot family inventory snapshot

### Already implemented families in the pilot

- `internal_vs_external_influence`
- `macro_influence_classification`
- `micro_market_macro_components_naming`
- `control_over_influences`
- `control_extent_reasoning`
- `stakeholder_influence`
- `technological_influence`
- `scenario_analysis_general`
- `influence_classification_written`
- `technology_opportunity_and_risk`
- `challenge_identification_from_scenario`
- `environment_classification_from_scenario`
- `extent_of_control_from_scenario`
- `macro_environment_involvement_recommendations`
- `benefits_of_macro_environment_involvement`
- `strategic_responses_lobbying_networking_adaptation`
- `table_guided_three_environment_response`
- `importance_of_environmental_awareness`
- `internal_vs_external_balance`
- `ignoring_influences_consequences`

### Missing high-priority families to add next

- add more scenario families drawn from additional curriculum-backed case lines, not only the current Bavi/Majeed/Vincent-style cases
- generalize the same external family/spec map pattern to the next Grade 11 BS topic
- externalize a reusable Business Studies metadata contract once a second topic follows the same pattern

## Metadata contract recommended for every new family

Every newly added or upgraded family should carry at minimum:

- `topic_id`
- `subtopic_id`
- `subskill`
- `learning_objective_id`
- `concept_id`
- `concept_group`
- `question_family_id`
- `scenario_family_id` for application items
- `difficulty_band`
- `retry_variant`
- `misconception_tags`
- `diagnostic_tags`
- `curriculum_reference`
- `minimum_mastery_score` for typed families

## Generator implementation checklist

### Checklist A: metadata foundation

- [x] Add a shared metadata helper so all generated questions return stable curriculum identity fields.
- [x] Keep random runtime `id` values separate from stable family metadata.
- [x] Ensure all existing pilot families emit `learning_objective_id`, `concept_id` or `concept_group`, `question_family_id`, `retry_variant`, and `curriculum_reference`.
- [x] Ensure typed families emit `minimum_mastery_score`.
- [x] Ensure scenario-based families emit `scenario_family_id`.

### Checklist B: first generator families to implement

- [x] `micro_market_macro_components_naming`
- [x] `control_extent_reasoning`
- [x] `challenge_identification_from_scenario`
- [x] `environment_classification_from_scenario`
- [x] `extent_of_control_from_scenario`

### Checklist C: second wave families

- [x] `macro_environment_involvement_recommendations`
- [x] `benefits_of_macro_environment_involvement`
- [x] `strategic_responses_lobbying_networking_adaptation`
- [x] `table_guided_three_environment_response`

### Checklist D: scenario variance and retry-ladder quality

- [x] Add a Grade 11 BS names helper for scenario-surface variation.
- [x] Keep names/context variation separate from marking rules and mastery metadata.
- [x] Add authored retry variants across the first-wave mastery families.
- [x] Extend authored retry variants to the remaining discussion families where only core wording exists.

### Checklist E: external topic specification

- [x] Create a topic-local external family/spec map for `Influences on business environments`.
- [ ] Reuse the same document structure for the next Grade 11 BS topic.

### Checklist F: question quality checks per family

- [ ] Prompt clearly matches one curriculum objective.
- [ ] Marking points map directly to the objective wording.
- [ ] Keyword list is broad enough for semantic marking but specific enough to avoid false mastery.
- [ ] Hints move from recognition to explanation, not straight to the memo.

## Exact mastery retry rules

### Rule set 1: concepts (MCQ)

- **Mastery threshold**: learner must answer correctly.
- **Fail on first attempt**: serve same `question_family_id` with `retry_variant = guided` and stronger hinting or clearer distractors.
- **Fail on second attempt**: serve same `question_family_id` with `retry_variant = reworded`.
- **Fail on third attempt**: show explanation/memo support, mark the family as needing further review, and keep the learner inside the same concept family until one correct response is achieved.
- **Pass rule**: after one correct response, move to the next planned family in the same scaffold step.

### Rule set 2: application / scenario analysis

- **Mastery threshold**: learner must achieve at least `minimum_mastery_score`, recommended default `0.6` of total marks.
- **Fail below threshold on first attempt**: serve same `scenario_family_id` with `retry_variant = guided` and stronger evidence cues.
- **Fail below threshold on second attempt**: serve same `scenario_family_id` with `retry_variant = reworded` and a cleaner scenario surface form.
- **Fail below threshold on third attempt**: serve same target objective with `retry_variant = transfer` or a reduced-complexity scenario, plus answer-part hints.
- **Pass rule**: only move on when the learner reaches threshold on the same family line, not merely the same subskill.

### Rule set 3: discussion

- **Mastery threshold**: learner must achieve at least `minimum_mastery_score`, recommended default `0.7` of total marks.
- **Fail on first attempt**: keep the same `question_family_id` and add structure cues for the expected paragraphs or points.
- **Fail on second attempt**: keep the same `learning_objective_id`, but swap to a reworded prompt from the same family.
- **Fail on third attempt**: provide memo comparison support, then require one more same-family response before completion.
- **Pass rule**: after threshold is met, mark the discussion family complete and allow scaffold completion or handoff.

### Rule set 4: diagnostic mode versus mastery mode

- **Diagnostic mode**: no gating, free progression, all attempts recorded by family metadata.
- **Mastery mode**: gating enforced by the thresholds above.
- **Diagnostic handoff rule**: start mastery at the weakest `question_family_id` cluster, then expand to adjacent families in the same `concept_group`.

### Rule set 5: stop conditions and escalation

- **Maximum consecutive failures in one family**: 3 before stronger support is forced.
- **Maximum forced retries before temporary progression**: 4, only if the app stores the family as unresolved and schedules it for return.
- **Completion rule**: a scaffold step is complete only when all scheduled families for that step meet mastery or are explicitly parked for later return after support.

# Immediate Next Actions

## First coding slice recommended

The next implementation slice should be:
 
  - add more curriculum-backed scenario family lines beyond the current cases so retry coverage does not over-concentrate on one scenario set
  - reuse the new family/spec map pattern for the next Grade 11 BS topic
  - draft a reusable BS metadata contract after the second topic confirms the pattern

This keeps the pilot documented, auditable and ready for reuse in the next Business Studies rollout.

# Final Recommendation

Use the Grade 11 pilot as the canonical Business Studies workflow model, but upgrade it from:

- guided subskill progression

to:

- metadata-driven mastery progression

Only after that is stable should the system introduce:

- diagnostic mode
- cross-topic rollout
- cross-grade rollout
