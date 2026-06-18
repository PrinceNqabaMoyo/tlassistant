# App.jsx Modularization Plan

## Goal

Reduce `src/App.jsx` into a smaller orchestration file without changing the current behavior of:

- splash-to-landing/auth/app routing
- browser history and back-button behavior
- student/teacher/admin role routing
- workspace question flow
- freeform chat and struggling-problem persistence
- subscription page navigation
- header, keypad, footer, and modal shell behavior

The safest outcome is for `App.jsx` to become a thin composition layer that wires together:

- app-level hooks
- top-level route decisions
- view renderers
- shell UI

## Current App.jsx Responsibilities

Based on the live file, `src/App.jsx` currently owns all of the following:

1. Firebase/auth service wiring from `useAuthentication`
2. Core app state wiring from multiple custom hooks
3. Top-level route and browser history synchronization
4. splash and landing/auth/subscription/app entry transitions
5. app session reset and logout cleanup
6. chat history and freeform thread management
7. struggling-problem save/continue/solve behavior
8. AI request orchestration via `getAgentResponse`
9. workspace answer submission and evaluation handlers
10. assignment start/submission behavior
11. student/teacher/admin render branching
12. app shell rendering for header, keypad, footer, and message modal

That is too much for one file and is the main reason the file is difficult to maintain safely.

## High-Risk Areas To Preserve During Modularization

These are the invariants that should not change while splitting the file:

- `landing`, `signin`, `signup`, `subscribe`, and `app` must continue to behave as guarded top-level pages.
- Signed-in users must not accidentally expose private app surfaces on public routes.
- Browser `popstate` handling must remain consistent with the current route/history rules.
- Student navigation state must still reset correctly on logout.
- `StudentView`, `Workspace`, `Header`, and `AuthScreen` must continue receiving the props they actually depend on.
- Freeform thread IDs, saved struggling problems, and solve/delete behavior must keep the same Firestore paths and semantics.
- Assignment and answer-submission flows must keep their current side effects and loading/message behavior.

## Files To Back Up Before Editing

These are the files most likely to be touched directly or indirectly during a proper modularization pass.

### Must back up

- `src/App.jsx`
- `src/main.jsx`
- `src/hooks/index.js`
- `src/hooks/useAuthentication.js`
- `src/hooks/useCoreState.js`
- `src/hooks/useCurriculumNavigation.js`
- `src/hooks/useWorkspaceUI.js`
- `src/hooks/useChatFunctionality.js`
- `src/hooks/useFreeformTopics.js`
- `src/hooks/useTeacherAdminViews.js`
- `src/hooks/useAssignmentsPractice.js`

### Very likely to be edited because of prop or render extraction

- `src/components/student/StudentView.jsx`
- `src/components/workspace/index.js`
- `src/components/workspace/Workspace.jsx` or the current workspace entry file
- `src/components/ui/Header.jsx`
- `src/components/auth/AuthScreen.jsx`
- `src/components/ui/LandingPage.jsx`
- `src/components/ui/SubscriptionPage.jsx`

### Useful reference backups if you want a wider rollback safety net

- `src/components/forms/StudentForms.jsx`
- `src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx`
- `src/components/curriculum/curriculum-helper/components/RepositoryModals.jsx`
- `src/constants/sourceDocuments.js`
- `src/utils/api.js`
- `src/utils/accountingValidation.js`
- `src/utils/curriculumHelpers.js`

## Recommended Backup Naming

Use timestamped copies before the first edit, for example:

- `src/App.20260525-1645.bak.jsx`
- `src/hooks/useCoreState.20260525-1645.bak.js`
- `src/components/student/StudentView.20260525-1645.bak.jsx`

If you prefer folder-based backups, create something like:

- `backups/app-modularization-phase-0/`

and place the copied files there.

## Recommended Target Structure

A safe modularization target would be to introduce an `src/app/` area and move App-specific orchestration there.

### Suggested structure

```text
src/
  app/
    constants/
      routes.js
    hooks/
      useTopLevelRouting.js
      useAppSessionReset.js
      useFreeformProblemFlow.js
      useWorkspaceSubmissionFlow.js
    render/
      renderRoleContent.jsx
      renderStudentContent.jsx
    shell/
      AppShell.jsx
    utils/
      subjectKeys.js
      navigationReset.js
```

You do not have to create all of these at once. The point is to split by responsibility, not by arbitrary line count.

## Modularization Strategy

The safest order is:

1. extract pure constants/helpers first
2. extract side-effect-heavy hooks second
3. extract render composition last

Do **not** start by moving everything into one huge `renderContent` helper file. That usually just relocates the complexity.

## Step-by-Step Plan

## Phase 0: Freeze a Baseline

### Purpose

Create a rollback point before changing behavior.

### Actions

- Back up the files listed above.
- Confirm the current `App.jsx` line count and note the current route behavior.
- Record current working flows:
  - splash -> landing for signed-out user
  - `/signin`
  - `/signup`
  - `/subscribe`
  - signed-in route to app
  - logout back to landing flow

### Success criteria

- You can restore the current app shell quickly if any extraction breaks routing.

## Phase 1: Remove Pure Static Pieces From App.jsx First

### Purpose

Shrink the file without touching runtime behavior.

### Extract first

- route constants and path resolvers
- subject key helpers
- navigation reset helpers
- any small pure utility currently defined inside `App.jsx`

### Candidate extractions

- `routePathMap`
- `getRequestedRouteFromPath`
- `resolveRoutePage`
- the duplicated `getSubjectKey` logic should become a single shared helper

### Suggested files

- `src/app/constants/routes.js`
- `src/app/utils/subjectKeys.js`
- `src/app/utils/navigationReset.js`

### Why first

These changes are low-risk and remove clutter before touching hooks or render flow.

## Phase 2: Extract Top-Level Routing and History Into a Dedicated Hook

### Purpose

Move splash/landing/auth/subscription/app orchestration out of `App.jsx`.

### Move into one hook

Create something like `useTopLevelRouting` that owns:

- `routePage`
- `topLevelPage`
- `authMode`
- splash-complete transition logic
- `popstate` listener logic
- history `pushState` / `replaceState` synchronization
- public navigation callbacks:
  - `navigateHome`
  - `navigateSignIn`
  - `navigateSignUp`
  - `navigateSubscribe`
  - `navigateApp`

### Inputs

- `authLoading`
- `showSplash`
- `effectiveCurrentUser`
- `setShowLandingPage`
- `setShowSplash`

### Outputs

- `topLevelPage`
- `authMode`
- `shouldRenderStandaloneLandingPage`
- navigation callbacks
- `handleSplashComplete`

### Why this matters

This is one of the most self-contained high-value extractions in the file.

## Phase 3: Extract App Session Reset / Logout Cleanup

### Purpose

Separate “sign out” from “reset every app state bucket manually inside App.jsx”.

### Move into one helper or hook

Create a dedicated reset unit that owns:

- logout call
- error handling on logout failure
- reset of selected curriculum/grade/subject/topic
- reset of assignments/practice/freeform state
- reset of navigation stack
- reset of route and splash state
- reset of route-history refs if needed

### Suggested file

- `src/app/hooks/useAppSessionReset.js`

### Reason

This block is long, stateful, and easy to break when edited inline.

## Phase 4: Extract Freeform Problem Persistence Flow

### Purpose

Move the saved/struggling problem lifecycle into a dedicated module.

### Move together as one concern

These functions should stay near each other in the same extracted unit because they are tightly related:

- `saveSuccessfulProblem`
- `saveStrugglingProblem`
- `handleMarkStrugglingProblemSolved`
- `addQuestionToChat`
- `updateAnswerInChat`
- `handleStrugglingProblem`
- `handleSendFreeformQuery`
- `handleContinueProblem`

### Suggested file

- `src/app/hooks/useFreeformProblemFlow.js`

### Inputs

- current user
- db service
- selected curriculum/grade/subject/topic
- message setters
- chat history setters
- thread ID setters
- `getAgentResponse`

### Output

A single object with the freeform/chat handlers consumed by `Workspace`, `StudentView`, and `MySavedProblemsView`.

### Why this should be one phase

This area has shared state and Firestore side effects. Splitting it into tiny pieces too early increases risk.

## Phase 5: Extract Workspace Question and Assignment Submission Logic

### Purpose

Reduce the density of App-owned handler logic used by `Workspace`.

### Candidate group

Move these together:

- `handleToggleMathStructure`
- `handleAttempt`
- `handleAnswerInput`
- `handleSubmit`
- `handleMathInput`
- `handleStartAssignment`
- `handleAssignmentSubmit`

### Suggested file

- `src/app/hooks/useWorkspaceSubmissionFlow.js`

### Important caution

Keep deterministic evaluation and AI-assisted evaluation behavior unchanged. This extraction is about ownership, not rewriting logic.

## Phase 6: Extract Student/Role Render Composition

### Purpose

Shrink the giant render branch and prop wall.

### Split render responsibilities

Create render-focused modules for:

- role-level rendering
- student-specific rendering
- app shell rendering

### Suggested files

- `src/app/render/renderRoleContent.jsx`
- `src/app/render/renderStudentContent.jsx`
- `src/app/shell/AppShell.jsx`

### Expected responsibilities

#### `renderRoleContent.jsx`

Chooses between:

- unauthenticated auth screen
- admin view
- teacher view
- student branch

#### `renderStudentContent.jsx`

Chooses between:

- saved problems
- workspace
- thumbnail/integration/geometry test routes
- default `StudentView`

#### `AppShell.jsx`

Owns shared shell UI:

- `BackButton`
- `Header`
- `<main>` wrapper
- `EnhancedMathKeypad`
- footer
- `MessageModal`
- `AdminTokenUsageDisplay`

### Why late in the process

Render extraction is safer after the underlying handlers are already grouped cleanly.

## Phase 7: Reduce Prop Surface Where It Is Obviously Safe

### Purpose

Avoid replacing one big file with many files that all require enormous prop lists.

### Safe reductions

- Group navigation callbacks into one object.
- Group freeform/workspace handlers into one object.
- Group shell props into one object.
- Group student render props into one object.

### Caution

Do **not** introduce global context unless the prop drilling remains unmanageable after the first refactor pass. Context is not automatically simpler.

## Phase 8: Remove Dead Code and Duplicate Logic

### Purpose

Finish the modularization cleanly.

### Things to check

- duplicated `getSubjectKey`
- outdated helper comments that no longer match the file
- imports no longer needed in `App.jsx`
- stale experimental/test-only imports that can be relocated closer to their render boundary

### Desired end state for App.jsx

`App.jsx` should ideally contain only:

- imported hooks
- imported render helpers
- high-level composition
- a very small amount of app-specific glue code

A realistic target is roughly **250-500 lines**, not necessarily under 100 lines.

## Phase 9: Verification After Each Extraction

After every phase, verify these flows before continuing:

### Public/top-level flows

- `/`
- `/signin`
- `/signup`
- `/subscribe`
- browser back button across landing/auth/app

### Auth and session flows

- signed-out splash behavior
- signed-in splash behavior
- logout reset behavior

### Student flows

- curriculum selection
- locked student subject landing
- workspace opening
- freeform query submission
- continue struggling problem
- mark struggling problem solved
- subscription redirect from locked flows

### Teacher/admin flows

- teacher route render
- admin route render
- super-admin mode switching

## Recommended Editing Sequence

If you want the lowest-risk actual implementation order, use this exact sequence:

1. create `src/app/constants/routes.js`
2. create `src/app/utils/subjectKeys.js`
3. create `src/app/utils/navigationReset.js`
4. extract `useTopLevelRouting`
5. extract `useAppSessionReset`
6. extract `useFreeformProblemFlow`
7. extract `useWorkspaceSubmissionFlow`
8. extract `renderStudentContent.jsx`
9. extract `renderRoleContent.jsx`
10. extract `AppShell.jsx`
11. clean imports and remove dead code
12. run full manual verification

## Files Likely To Be Created During Modularization

A realistic first-pass creation list is:

- `src/app/constants/routes.js`
- `src/app/utils/subjectKeys.js`
- `src/app/utils/navigationReset.js`
- `src/app/hooks/useTopLevelRouting.js`
- `src/app/hooks/useAppSessionReset.js`
- `src/app/hooks/useFreeformProblemFlow.js`
- `src/app/hooks/useWorkspaceSubmissionFlow.js`
- `src/app/render/renderStudentContent.jsx`
- `src/app/render/renderRoleContent.jsx`
- `src/app/shell/AppShell.jsx`

## Anti-Patterns To Avoid During This Refactor

- Moving hundreds of lines without verification between steps
- Changing behavior while extracting ownership
- Introducing new global state just to avoid passing props
- Duplicating business logic in both `App.jsx` and a new extracted hook
- Mixing public route logic with student workspace render logic in the same new file
- Refactoring comments or naming everywhere at the same time as the structural split

## Definition of Done

The modularization is complete when:

- `App.jsx` is primarily orchestration and composition
- route/history logic lives outside `App.jsx`
- freeform problem flow lives outside `App.jsx`
- workspace submission flow lives outside `App.jsx`
- render branching is split into focused modules
- no observable app behavior has regressed
- the backed-up files are no longer needed for rollback

## Recommended First Implementation Cut

If you want the smallest safe first pass, stop after these extractions:

- routes/constants/helpers
- `useTopLevelRouting`
- `useAppSessionReset`
- `renderStudentContent`

That alone should remove a meaningful amount of weight from `App.jsx` without forcing a full deep rewrite in one session.
