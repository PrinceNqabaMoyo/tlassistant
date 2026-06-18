---
description: Modularize CurriculumHelper.jsx safely while preserving current routing, topic selection behavior, and UI behavior, with each resulting file kept comfortably small.
---

# Curriculum Helper Modularization Workflow

## Goal

Modularize `src/components/curriculum/CurriculumHelper.jsx` so it becomes safer to edit, easier to review, and less likely to break unrelated subjects or topic-routing logic.

The final state should keep `src/components/curriculum/CurriculumHelper.jsx` as the stable public entrypoint, but move most of the current responsibilities into a dedicated folder:

- `src/components/curriculum/curriculum-helper/`

This refactor must preserve existing runtime behavior, especially the fragile direct-to-workspace routing and topic-specific conditional rendering paths.

## Why this file needs special care

`CurriculumHelper.jsx` currently mixes several very different responsibilities in one file:

- React view state and modal state
- subject and grade detection
- topic normalization and topic-matcher helpers
- scaffold-route resolution
- topic numbering, term, and display-name metadata
- large subject/topic-specific card rendering branches
- topic overview and subtopic actions
- repository launch buttons and overlay wiring
- workspace navigation handoff

Because those concerns are interleaved, small edits can easily damage unrelated JSX or route logic.

## Hard constraints

1. Preserve the existing import path for callers: `src/components/curriculum/CurriculumHelper.jsx`.
2. Do not change prop names or the external component API during modularization.
3. Do not change topic-routing behavior while refactoring.
4. Do not change UI copy, topic labels, numbering, or card availability unless explicitly required by a bug fix.
5. Do not refactor this as one giant patch.
6. Verify after each extraction phase.
7. Keep each resulting file comfortably small. Target `<= 900` lines per file, and prefer much smaller where practical.
8. Prefer pure-function extraction first, then presentational JSX extraction, and only then deeper state/orchestration extraction.

## Non-obvious fragile areas to preserve

These are high-risk and must be treated as invariants during the refactor:

- route resolution order matters for some topics
- Grade 11 and Grade 12 Accounting use numbered-topic overrides
- direct workspace navigation in `handleTopicSelect` must keep working
- `navigateToWorkspaceWithMode` must preserve navigation stack behavior
- Grade 10 Business Studies and Grade 11 Business Studies routes must still resolve correctly
- implemented Math, Accounting, and Business Studies topic cards must keep rendering as before
- repository buttons, visual aids, and overlay wiring must continue to open the same UI
- topic overview and subtopic actions must continue to work for non-direct-routed topics

## Target folder structure

Use a responsibility-based structure inside:

- `src/components/curriculum/curriculum-helper/`

### Target files

- `CurriculumHelper.jsx`
  - thin facade / stable entrypoint
  - imports and renders the modularized helper container
  - minimal orchestration only

- `curriculum-helper/constants.js`
  - static arrays and simple constants
  - icon pools
  - color pools
  - small static configuration values

- `curriculum-helper/topicMatchers.js`
  - pure topic matcher helpers only
  - grade/subject-specific topic predicate functions
  - topic normalization helpers

- `curriculum-helper/topicMetadata.js`
  - topic display names
  - numbering logic
  - term labels
  - any metadata maps that are currently embedded in helper logic

- `curriculum-helper/topicRouting.js`
  - scaffold route resolution
  - direct-to-workspace topic mapping logic
  - logic that determines whether a topic should jump straight into workspace mode

- `curriculum-helper/repositories.js`
  - repository availability helpers
  - repository metadata builders
  - any pure helper logic for repository launch cards

- `curriculum-helper/components/TopicCardsSection.jsx`
  - the large topic-card rendering block
  - receives already-prepared flags, handlers, and labels via props
  - should stay presentational where possible

- `curriculum-helper/components/TopicOverviewSection.jsx`
  - topic summary
  - subtopic grid
  - topic-level action buttons

- `curriculum-helper/components/TopicListSection.jsx`
  - topics list/grid selection UI
  - icon and color presentation

- `curriculum-helper/components/RepositoryModals.jsx`
  - repository modals
  - mathematical visual aids modal wiring
  - component overlay wiring
  - EFT modal rendering if keeping it out of the main component reduces noise

- `curriculum-helper/useCurriculumHelperState.js` if still needed
  - optional later extraction
  - only if the main container still holds too much state/orchestration after the pure/helper and JSX moves

## Architecture rules for the refactor

1. Keep pure logic out of JSX files where possible.
2. Do not let extracted presentational components decide routes on their own unless that logic is intentionally passed in.
3. Keep route mapping and topic metadata centralized so future topic additions touch fewer files.
4. Avoid circular imports between metadata, matchers, and routing modules.
5. Pass down precomputed flags and handlers instead of recreating the same subject/topic checks in many child components.
6. Prefer extraction by responsibility, not by arbitrary line-count slicing.

## Execution order

Follow these phases in order.

### Phase 1: Freeze the baseline

1. Record the current known-sensitive behaviors.
2. Identify representative manual test paths before moving code.
3. Confirm the current file is the source of truth before extracting anything.

### Baseline test paths

Use these as the minimum regression set during the refactor:

- Grade 7 Math topic card flow
- Grade 10 Accounting direct-to-workspace flow
- Grade 10 Business Studies direct-to-workspace flow
- Grade 11 Business Studies card flow
- Grade 11 Accounting numbered-topic flow
- Grade 12 Accounting numbered-topic flow
- Grade 11 Math flow
- Grade 12 Math flow
- repository modal opening
- topic summary and subtopic action behavior for non-direct-routed topics

### Phase 2: Extract pure constants and normalization helpers

Start with the safest, least stateful logic.

#### First extraction candidates

- icon arrays
- color arrays
- simple normalization helpers
- small constant maps

#### Phase 2 exit criteria

- no UI behavior changes
- imports remain clean
- main file becomes slightly smaller without moving route logic yet

### Phase 3: Extract topic matchers

Move pure topic predicate functions into `topicMatchers.js`.

#### Include

- grade/subject checks that can be made pure
- topic predicate helpers like `isWholeNumbersTopic`, `isGrade10BSMicroEnvironment`, and similar matchers
- shared normalization helpers used by those matchers

#### Important rule

If some matchers currently depend on component-local booleans, convert them into pure helpers that accept the needed inputs explicitly.

#### Phase 3 exit criteria

- all matcher helpers are imported from one place
- matcher behavior is unchanged
- no subject loses topic recognition

### Phase 4: Extract metadata and labeling logic

Move display-oriented topic metadata into `topicMetadata.js`.

#### Include

- display-name resolution
- topic numbering resolution
- term-label logic
- any label normalization used for topic cards or subtitles

#### Phase 4 exit criteria

- card titles still render the same
- numbering stays stable
- term labels stay stable
- subtitle and topic display behavior stay unchanged

### Phase 5: Extract route resolution and direct-navigation logic

Move route-resolution logic into `topicRouting.js`.

#### Include

- `getScaffoldRouteForTopic`
- helpers that map topic names to workspace modes
- route decision helpers used by `handleTopicSelect`

#### Important rule

Preserve matching order exactly where order matters.

#### Phase 5 exit criteria

- direct-to-workspace topics still open the correct workspace mode
- non-implemented topics still fall back correctly
- navigation labels and stack behavior remain intact

### Phase 6: Extract repository availability helpers

Move repository-related helper logic into `repositories.js`.

#### Include

- available repository calculation
- repository metadata objects that can be built outside JSX
- any reusable helper logic for repository launch buttons

#### Phase 6 exit criteria

- repository buttons still appear under the same conditions
- repository launch behavior is unchanged

### Phase 7: Extract large presentational sections

Now move the big JSX branches into focused components.

#### Recommended order

1. `TopicListSection.jsx`
2. `TopicOverviewSection.jsx`
3. `TopicCardsSection.jsx`
4. `RepositoryModals.jsx`

#### Important rule

Do not migrate business logic into these components unnecessarily. Pass in:

- resolved labels
- booleans
- callbacks
- already-filtered data

#### Phase 7 exit criteria

- the main file is dramatically smaller
- extracted components are mostly presentational
- JSX nesting in the main file is reduced enough that edits become local and safer

### Phase 8: Slim the main container

After the helper and JSX extractions, reduce `CurriculumHelper.jsx` to:

- prop intake
- core state
- top-level effect wiring
- handler composition
- render orchestration

If it is still too large, introduce `useCurriculumHelperState.js` for grouped state/handlers.

#### Phase 8 exit criteria

- `CurriculumHelper.jsx` becomes a readable facade/container
- future edits to cards, routes, or metadata can happen in separate modules
- no child component requires hidden knowledge of unrelated helper internals

### Phase 9: Final cleanup and verification

1. Remove duplicate helpers that remained after extraction.
2. Standardize imports.
3. Ensure no resulting file exceeds the size target.
4. Re-run the regression paths.
5. Check for circular imports.
6. Check for dead code and stale local helpers.

## Testing cadence during modularization

After each extraction phase:

1. verify imports compile cleanly in the IDE
2. test at least one representative topic path affected by that phase
3. confirm no route changed unexpectedly
4. confirm no JSX block disappeared or shifted to the wrong branch
5. stop and fix regressions before continuing

Do not stack several extraction phases without checking behavior in between.

## Suggested test matrix

At minimum, manually verify:

- one Grade 7 Math topic
- one Grade 10 Accounting topic
- one Grade 10 Business Studies topic
- one Grade 11 Business Studies topic
- one Grade 11 Accounting topic
- one Grade 12 Accounting topic
- one Grade 11 Math topic
- one Grade 12 Math topic
- repository modal launch
- topic summary toggle
- subtopic action buttons

## Non-negotiable safety rules

- Do not rename the public `CurriculumHelper.jsx` entrypoint casually.
- Do not change route keys during refactoring.
- Do not combine route metadata and rendered JSX in the same new module if that makes future edits harder.
- Do not split one fragile logic area across too many files.
- Do not move everything into hooks if the result hides simple rendering logic.
- Do not rewrite working topic cards while modularizing.
- Do not use a giant replace-all refactor across the whole file.

## Definition of done

The modularization is complete only when all of the following are true:

- `CurriculumHelper.jsx` is no longer the main place for topic matchers, metadata, route mapping, and giant JSX blocks
- the public import path remains stable
- route behavior is unchanged
- representative topics across Math, Accounting, and Business Studies still work
- repository and overlay flows still work
- each resulting file is within the target size limit
- future edits to topic cards or route mapping can happen in isolated files instead of a 3000-line component

## Follow-up after completion

Once modularization is complete and verified:

1. use the new structure as the baseline for future Curriculum Helper edits
2. document where new topic metadata, route mappings, and card JSX should be added
3. only then continue with larger Curriculum Helper feature work or new topic implementations
