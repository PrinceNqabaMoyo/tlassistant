I’ll map the exact implementation-touch files by phase and turn that into a backup checklist. I’m starting with a targeted codebase search so the list is anchored to the current structure, not just the older plan assumptions.
Fast Context failed, so I’m falling back to direct file discovery and targeted searches. I’ll map the current files for each rollout area, then I’ll give you a backup list phase by phase.
I’ve confirmed the current core shell files. I’m now locating the student-facing surfaces that are most likely to change in later phases: subject selection, saved problems, assignments, and any data/config files behind grade or subject availability.

The text searches were sparse, which usually means those labels are assembled indirectly. I’m reading the student render layer next, since that’s the most likely place where dashboard cards and entry points are currently defined.

I’ve confirmed two high-value targets already: [renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0) still exposes the thumbnail/integration/geometry test surfaces, and [Workspace.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/workspace/Workspace.jsx:0:0-0:0) still contains the component repositories and live class-assignment UI. I’m checking the student shell next so the backup list includes the dashboard cards and entry points themselves, not just the lower-level handlers.

I found the assignment screen and confirmed there are duplicate/copy files in `components/student`, which matters for backups because we need to protect the live file and avoid confusing it with stale copies. I’m checking the live `StudentView` and export index so the phase backup list points to the real entry files.
I’ve got enough to outline most phases, but I want to make the auth backup list precise. I’m checking the authentication hook and the header, because those are likely Phase 1 touchpoints for verification, logout, and notification/back-button behavior.
I already have enough for most phases. I’m doing one last quick pass on the auth/header/form entry files so the backup list includes the exact live files, not guesses.

I’ve mapped the primary live entry files. I’m doing one last confirmation read on the student form/dashboard file so I can mark the subject/grade gating backup list as confirmed rather than speculative.

I have the frontend phase files. I’m doing one last lookup for Firebase rule/config files because Phase 4 POP hardening may need backups there too.

I’ve mapped the live files and I also confirmed there are many stale `copy`/`backup` files in the repo. I’m saving one memory from this: you want a **phase-by-phase backup list before implementation**, and the live routing shell is centered on [useTopLevelRouting.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useTopLevelRouting.js:0:0-0:0) plus the extracted render/shell files.

# Phase-by-Phase Backup List

I used the routing-shell memory and the backup-preference memory to shape this list.

## First rule

Back up the **live imported files**, not the stale duplicates.

I found many repo duplicates like:

- `src/components/student/StudentView copy.jsx`
- `src/components/student/EftUploadModal copy.jsx`
- `src/hooks/useAuthentication copy.js`
- `src/hooks/useAssignmentsPractice copy.js`
- `src/components/forms/StudentForms copy.jsx`

Unless you explicitly want archival copies of those too, **do not treat them as the source of truth**.

---

# Phase 0: Base snapshot before any rollout work

Create one master backup bundle first.

## Back up

- [src/App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0)
- [src/app/constants/routes.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/constants/routes.js:0:0-0:0)
- [src/app/hooks/useTopLevelRouting.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useTopLevelRouting.js:0:0-0:0)
- [src/app/hooks/useAppSessionReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useAppSessionReset.js:0:0-0:0)
- [src/app/utils/navigationReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/utils/navigationReset.js:0:0-0:0)
- [src/app/render/renderRoleContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderRoleContent.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/app/shell/AppShell.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/shell/AppShell.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/ui/LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/components/ui/Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0)
- [src/components/student/EftUploadModal.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/EftUploadModal.jsx:0:0-0:0)
- [src/components/student/ClassworkView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/ClassworkView.jsx:0:0-0:0)
- [src/components/workspace/Workspace.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/workspace/Workspace.jsx:0:0-0:0)
- [src/components/curriculum/CurriculumHelper.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/CurriculumHelper.jsx:0:0-0:0)
- [src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx:0:0-0:0)
- [src/curriculumData.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/curriculumData.js:0:0-0:0)
- [firebase.json](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/firebase.json:0:0-0:0)
- `dev to production plan.md`

---

# Phase 1: Routing, auth, verification, sign-in path, grade restriction

These are the files most likely to move in Phase 1.

## Required backups

- [src/App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0)
- [src/app/constants/routes.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/constants/routes.js:0:0-0:0)
- [src/app/hooks/useTopLevelRouting.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useTopLevelRouting.js:0:0-0:0)
- [src/app/hooks/useAppSessionReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useAppSessionReset.js:0:0-0:0)
- [src/app/utils/navigationReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/utils/navigationReset.js:0:0-0:0)
- [src/app/render/renderRoleContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderRoleContent.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/app/shell/AppShell.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/shell/AppShell.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- [src/components/ui/LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)

## Why these matter

- **Routing shell**: [routes.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/constants/routes.js:0:0-0:0), [useTopLevelRouting.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useTopLevelRouting.js:0:0-0:0), [App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0), [renderRoleContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderRoleContent.jsx:0:0-0:0), [AppShell.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/shell/AppShell.jsx:0:0-0:0)
- **Verification and grade lock**: [AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0), [useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- **Returning-user path**: [LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0), [SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- **Student dashboard entry behavior**: [StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0), [StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)

---

# Phase 2: MVP scope lockdown and student-surface cleanup

This phase touches the visible student product the most.

## Required backups

- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/components/student/ClassworkView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/ClassworkView.jsx:0:0-0:0)
- [src/components/workspace/Workspace.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/workspace/Workspace.jsx:0:0-0:0)
- [src/components/ui/Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0)
- [src/hooks/useAssignmentsPractice.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAssignmentsPractice.js:0:0-0:0)
- [src/curriculumData.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/curriculumData.js:0:0-0:0)
- [src/components/curriculum/CurriculumHelper.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/CurriculumHelper.jsx:0:0-0:0)
- [src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx:0:0-0:0)

## Likely additional backups if helper/topic cards are touched

- `src/components/curriculum/curriculum-helper/components/TopicListSection.jsx`
- `src/components/curriculum/curriculum-helper/components/TopicOverviewSection.jsx`
- `src/components/curriculum/curriculum-helper/repositories.js`

## Why these matter

I confirmed:

- [Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0) still contains the **thumbnail test** button
- [renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0) still exposes:
  - `thumbnail_test`
  - `integration_demo`
  - `geometry_backend_test`
- [Workspace.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/workspace/Workspace.jsx:0:0-0:0) still exposes **component repositories** and live **class assignment** workspace behavior
- [StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0) currently renders:
  - **Subjects**
  - **My Saved Problems**
  - **Class Assignments**
  - **Learning Tools & Components**

This is the main phase where those student-visible surfaces get locked down.

---

# Phase 3: User messaging, welcome notification, demand capture

This phase is lighter, but still touches important public and student-facing files.

## Required backups

- [src/components/ui/LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/ui/Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)

## Optional backups if notification wiring moves upward

- [src/App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)

## Why these matter

- **Public availability messaging**: [LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0), [SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- **Welcome notification / bell behavior**: [Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0), [Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- **User bootstrap state**: [useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- **Dashboard copy / prompts / upsell copy**: [StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)

---

# Phase 4: POP hardening and subscription operations

This is the most payment-sensitive phase.

## Required backups

- [src/components/student/EftUploadModal.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/EftUploadModal.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- [firebase.json](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/firebase.json:0:0-0:0)

## Optional backups if top-level payment gating changes

- [src/App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)

## External/non-repo backups to remember

I did **not** find local copies of:

- `firestore.rules`
- `storage.rules`

So if those live outside this repo, back them up separately before Phase 4.

## Why these matter

- [EftUploadModal.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/EftUploadModal.jsx:0:0-0:0) is the core POP flow
- [useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0) holds subscription/payment normalization fields
- [StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0) already renders subscription status and manage-subscription prompts
- [SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0) is the user’s entry point into the POP process

---

# Phase 5: QA, staging, and cutover

Before release, make one release-candidate backup bundle of every file actually changed in Phases 1 to 4.

## Minimum release bundle

- all edited files from Phase 1
- all edited files from Phase 2
- all edited files from Phase 3
- all edited files from Phase 4
- [firebase.json](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/firebase.json:0:0-0:0)
- `dev to production plan.md`

## If Firebase rules are managed outside repo

Also back up:

- Firestore rules
- Storage rules
- any Firebase console-side indexes or config relevant to POP/payment flows

---

# My recommended backup sets

If you want the shortest practical list, use these:

## Set A: Before Phase 1

- [src/App.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/App.jsx:0:0-0:0)
- [src/app/constants/routes.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/constants/routes.js:0:0-0:0)
- [src/app/hooks/useTopLevelRouting.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useTopLevelRouting.js:0:0-0:0)
- [src/app/hooks/useAppSessionReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/hooks/useAppSessionReset.js:0:0-0:0)
- [src/app/utils/navigationReset.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/utils/navigationReset.js:0:0-0:0)
- [src/app/render/renderRoleContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderRoleContent.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/app/shell/AppShell.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/shell/AppShell.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- [src/components/ui/LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)

## Set B: Before Phase 2

- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/app/render/renderStudentContent.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/app/render/renderStudentContent.jsx:0:0-0:0)
- [src/components/student/StudentView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/StudentView.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/components/student/ClassworkView.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/ClassworkView.jsx:0:0-0:0)
- [src/components/workspace/Workspace.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/workspace/Workspace.jsx:0:0-0:0)
- [src/components/ui/Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0)
- [src/hooks/useAssignmentsPractice.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAssignmentsPractice.js:0:0-0:0)
- [src/curriculumData.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/curriculumData.js:0:0-0:0)
- [src/components/curriculum/CurriculumHelper.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/CurriculumHelper.jsx:0:0-0:0)
- [src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/curriculum/curriculum-helper/CurriculumHelperContainer.jsx:0:0-0:0)

## Set C: Before Phase 3

- [src/components/ui/LandingPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/LandingPage.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/ui/Notifications.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Notifications.jsx:0:0-0:0)
- [src/components/ui/Header.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/Header.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/components/auth/AuthScreen.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/auth/AuthScreen.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)

## Set D: Before Phase 4

- [src/components/student/EftUploadModal.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/student/EftUploadModal.jsx:0:0-0:0)
- [src/components/ui/SubscriptionPage.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/ui/SubscriptionPage.jsx:0:0-0:0)
- [src/components/forms/StudentForms.jsx](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/components/forms/StudentForms.jsx:0:0-0:0)
- [src/hooks/useAuthentication.js](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/src/hooks/useAuthentication.js:0:0-0:0)
- [firebase.json](cci:7://file:///C:/Users/princ/fundile-tlassistant-vite/firebase.json:0:0-0:0)
- external Firebase rules/config if stored outside repo

---

# Suggested naming

Use one folder per phase, for example:

- `backups/phase-1-routing-auth/`
- `backups/phase-2-mvp-scope/`
- `backups/phase-3-messaging/`
- `backups/phase-4-pop/`

---

# Best next step

If you want, I can now do one of these:

- **Option 1**
  Turn this into a **copy-paste backup checklist** inside `dev to production plan.md`

- **Option 2**
  Turn this into a **Windows command list** for making the backup folders and copying the files

- **Option 3**
  Start the actual **Phase 1 file audit** and identify which of those files are definitely first-touch vs just precautionary backups

# Status

- **Live implementation files mapped by phase:** complete
- **Backup list before each phase:** complete
- **Ready to move into Phase 1 execution prep:** ready