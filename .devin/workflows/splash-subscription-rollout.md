---
description: Implement splash flow, trial gating, saved exact problems, student notifications, signup verification and lifecycle emails, admin POP notification emails, and EFT modal header updates
---
# Goal

Implement a coordinated user-flow upgrade for splash behavior, signup/login routing, subscription gating, saved exact problems, student notifications, verification and lifecycle emails, admin POP notification emails, and the EFT payment modal.

This workflow is intentionally written **before implementation** so the changes can be reviewed and backed up safely.

# Requested behavior summary

## 1. Splash and landing behavior

Desired behavior:

1. Every app/web visit should begin with the splash screen.
2. If the visitor is already authenticated, the splash should route directly to that user's dashboard.
3. If the visitor is not authenticated, the splash should route to the landing page.
4. A signed-in user should only see the landing page after they explicitly sign out.
5. Signing out should return the user to the splash, then to the landing page.

## 2. Splash visual behavior

Desired behavior:

1. Revert from the animated yellow-square drop effect.
2. Use the static graduation cap logo.
3. Restore the older Netflix-style text reveal for `fundile`.
4. Match the older timing and visual rhythm from the copy files. Ensure that the text and logo are centered.

## 3. One free question generation for signed-in users

Desired behavior:

1. Each signed-in user gets exactly one free generated question to try the app.
2. After that first free generation, they are not blocked from signing in or viewing the dashboard.
3. Any later attempt to select a locked subject or generate another question without an active subscription should show the existing subscribe popup.

## 4. Save exact struggled problems for subscribed users

Desired behavior:

1. Subscribed users should be able to save problems they struggle with.
2. The saved problem should be the exact generated question, not just the topic.
3. The save action should appear after `Compare/Memo` or `Check`.
4. Start with Accounting Grade 10 and Grade 11.

## 5. Improve student notifications

Desired behavior:

1. Remove the feeling that notifications always show the same default assignments.
2. After signup, the first notification should welcome the user by name and encourage subscription.
3. After subscription approval, the next important notification should congratulate the user on subscribing.

## 6. Improve signup email security and onboarding

Desired behavior:

1. A new user must receive an email verification email after signup.
2. The app should treat verification as a security step, not just an optional extra.
3. The verification email should be polite and excited, and should encourage the learner to try their one-time free question generation trial.
4. The verification/onboarding email flow should encourage subscription in a warm, non-pushy way.
5. Where technically supported, user emails should include the learner's signup name.
6. After successful verification, the user should receive a second welcome email.

## 7. Add subscription lifecycle email notifications

Desired behavior:

1. When a learner uploads a POP, all configured super admin / owner recipient emails should receive an email telling them to check the system.
2. The POP notification email should include enough context to identify the learner quickly, such as learner name, email, requested grade, plan, and reference used.
3. When a POP is approved, the learner should receive a congratulations email.
4. The approval email should be warm, encouraging, and personalized with the learner's signup name.
5. The approval email should wish the learner well and direct them back to the app to begin learning.

## 8. Update the EFT payment modal header and banking details

Desired behavior:

1. The blue ribbon header should show the graduation cap logo and `fundile` branding.
2. The modal header should clearly show:
   - `SUBSCRIPTION`
   - `EFT payment step`
3. Banking details should be updated to:
   - Bank: `Access Bank`
   - Account number: `51622451787`
   - Branch code: `410506`

# Backup checklist before implementation

Create backups for these files before making code changes.

## Core navigation, splash, and auth flow

- `src/App.jsx`
- `src/hooks/useCoreState.js`
- `src/hooks/useAuthentication.js`
- `src/components/ui/SplashScreen.jsx`
- `src/components/ui/GraduationCapSplash.jsx`
- `src/components/ui/CapRainAnimation.jsx`
- `src/components/auth/AuthScreen.jsx`
- `src/components/ui/LandingPage.jsx`
- `src/components/ui/Header.jsx`

## Student gating, dashboard, notifications, and saving problems

- `src/components/student/StudentView.jsx`
- `src/components/forms/StudentForms.jsx`
- `src/components/student/EftUploadModal.jsx`

## Optional but strongly recommended backup targets

- `src/index.html`
- `firebase.json`
- `package.json`

## New backend/service files likely needed

There is currently no obvious project-level `functions/` directory in this app root. If email sending, POP admin notifications, approval mail, or post-verification welcome mail is implemented via Firebase Functions or another server-side path, back up any newly created backend mailer/config files as soon as they are introduced.

# Current code touchpoints already identified

## Splash, landing, and top-level flow

- `src/App.jsx`
- `src/hooks/useCoreState.js`
- `src/components/ui/SplashScreen.jsx`
- `src/components/ui/GraduationCapSplash.jsx`
- `src/components/ui/CapRainAnimation.jsx`

## Signup and auth state

- `src/components/auth/AuthScreen.jsx`
- `src/hooks/useAuthentication.js`
- any future email action handler page or custom auth action route if verification is branded/customized

## Student dashboard, subject gating, and saved problems

- `src/components/student/StudentView.jsx`
- `src/components/forms/StudentForms.jsx`
- `src/App.jsx`

## Header notifications

- `src/components/ui/Header.jsx`
- `src/App.jsx`

## POP upload and approval lifecycle

- `src/components/student/EftUploadModal.jsx`
- `src/components/forms/AdminForms.jsx`
- `src/components/admin/AdminView.jsx`

## Mailer/backend integration

- new backend mailer/functions files
- provider configuration files for SendGrid, Resend, Mailgun, or equivalent if introduced
- possibly `firebase.json` if functions are added to this repo structure later

## EFT payment modal

- `src/components/student/EftUploadModal.jsx`

# Recommended implementation order

## Phase 1. Lock down the desired auth and splash state machine

Define the top-level rules first, because every other flow depends on this.

Implementation goals:

1. On page load, always show splash first.
2. After splash completes:
   - if authenticated: route to the correct dashboard
   - if not authenticated: route to landing
3. On logout:
   - clear user session through Firebase auth
   - reset app navigation state
   - show splash again
   - then show landing
4. Prevent landing from appearing in front of authenticated users unless they explicitly sign out.

Recommended files:

- `src/App.jsx`
- `src/hooks/useCoreState.js`
- `src/hooks/useAuthentication.js`

Acceptance check:

- Refresh while signed out -> splash -> landing
- Refresh while signed in -> splash -> dashboard
- Logout -> splash -> landing

## Phase 2. Revert splash visuals to the older static-cap version

The current falling-square animation should be removed from the main splash experience.

Recommended approach:

1. Use the older static cap presentation from the copy files as the visual baseline.
2. Restore the typing/reveal behavior for the `fundile` wordmark.
3. Restore the older timing rhythm.
4. Remove the square-drop animation from the user-facing splash path.
5. Keep `CapRainAnimation.jsx` only if you still want it for experiments; otherwise remove it from the splash entry path.

Recommended files:

- `src/components/ui/SplashScreen.jsx`
- `src/components/ui/GraduationCapSplash.jsx`
- `src/components/ui/CapRainAnimation.jsx`

Acceptance check:

- Splash shows a static graduation cap
- `fundile` reveals in the older Netflix-style motion
- no falling-square merge animation is visible

## Phase 3. Add one free generation for signed-in but unsubscribed users

This should be implemented as a clear entitlement rule, not as scattered UI exceptions.

## Recommended entitlement design

Add explicit usage tracking to the user profile.

Recommended user fields:

- `freeGenerationAllowance: 1`
- `freeGenerationUsedCount: 0`
- `hasConsumedFreeGeneration: false`
- `subscriptionStatus` or continue using the current approved subscription fields already in use

Recommended rule:

1. If user has active subscription -> allow generation normally.
2. If user has no active subscription and `hasConsumedFreeGeneration` is `false` -> allow one generation and immediately mark it consumed.
3. If user has no active subscription and the free generation is already used -> show subscribe popup on locked subject click or generation attempt.

## Important implementation note

The free trial should be enforced at the same point where question generation is actually triggered, not only at subject selection UI level. Otherwise the user could bypass the rule via alternate flows.

Recommended files:

- `src/components/forms/StudentForms.jsx`
- `src/components/student/StudentView.jsx`
- `src/App.jsx`
- `src/hooks/useAuthentication.js`

Acceptance check:

- new signed-in unsubscribed user can generate exactly one question
- second attempt shows subscribe popup
- subscribed users are unaffected

## Phase 4. Save exact struggled generated problems for subscribed users

This is best implemented as a dedicated persisted problem snapshot, not just a topic/thread pointer.

## Why the current struggling-problem flow is not enough

The existing struggling-problem path in `App.jsx` stores thread history for freeform struggle flows. That is useful, but it is not yet a robust exact-question snapshot system for deterministic generated accounting questions.

## Recommended data model

Create a saved problem snapshot document that stores the exact generated question payload at the time the learner saves it.

Recommended collection strategy:

- keep using a user-scoped collection under the existing artifacts pattern, or
- create a dedicated saved problems collection if you want simpler querying later

Recommended saved problem fields:

- `userId`
- `curriculum`
- `grade`
- `subject`
- `topic`
- `subtopic` if available
- `questionType`
- `questionPrompt`
- `questionData` or full rendered generator payload
- `memoData`
- `markingGuide`
- `studentAnswerSnapshot` if available
- `savedAt`
- `sourceMode` such as scaffold/practice
- `generatorMetadata` such as seed, family, difficulty, variant, concept identifiers where available

## Recommended UI behavior

1. Show `Save Problem` only for subscribed users.
2. Show it after `Compare/Memo` or `Check`, because that is when the learner knows this is a problem worth revisiting.
3. Save the full exact question payload, not just a regenerated version.
4. The saved problems dashboard should reopen the exact saved question first.
5. Start with Accounting Grade 10 and Grade 11 only.

## Recommended rollout strategy

### Stage 1

Support exact snapshot saving for Grade 10 and Grade 11 Accounting only.

### Stage 2

Normalize a common saved-question schema for future subjects.

### Stage 3

Optionally allow teachers/admins to inspect commonly saved struggle patterns.

Recommended files:

- `src/App.jsx`
- `src/components/forms/StudentForms.jsx`
- `src/components/student/StudentView.jsx`
- any grade 10/11 accounting workspace or question-rendering files that own the generated payload shape

Acceptance check:

- learner can save a generated accounting question after compare/check
- reopening the saved item shows the same exact question and memo content
- the question does not drift because of a new regeneration

# Best-practice recommendation for exact-problem saving

For accounting, the safest design is:

1. Save the exact rendered payload shown to the student.
2. Also save generator metadata if available.
3. On reopen, render from the saved snapshot first.
4. Only fall back to generator regeneration if a migration is needed later.

This avoids mismatch caused by deterministic-but-variable generation rules.

## Phase 5. Replace static-feeling notifications with lifecycle notifications

The student notification bell should be driven by real notification records, not just a short assignment list.

## Recommended notification model

Create a lightweight notification collection per user or under a central collection keyed by `uid`.

Recommended notification fields:

- `userId`
- `type`
- `title`
- `body`
- `ctaLabel`
- `ctaTarget`
- `isRead`
- `createdAt`
- `priority`

## Initial notification types to implement

1. `welcome_after_signup`
   - personalized with learner name
   - encourages subscription
2. `subscription_approved`
   - congratulates user
   - points them back to dashboard/subjects
3. keep assignments as a separate notification type rather than hard-coded bell content

## Recommended behavior

1. On signup, create a welcome notification record.
2. On subscription approval, create a congratulations notification record.
3. The bell should read notification records, not fake defaults.
4. If assignments exist, show them in the same stream as a different type.

Recommended files:

- `src/components/ui/Header.jsx`
- `src/App.jsx`
- admin approval flow files that mark subscriptions approved

Acceptance check:

- new signup sees welcome notification by name
- approved subscriber sees congratulations notification
- bell content is data-driven

## Phase 6. Strengthen signup verification and welcome email flow

The current `AuthScreen.jsx` already calls `sendEmailVerification(user)`, which is good, but the overall onboarding flow still needs strengthening.

## Recommended email flow

### Email 1: verification/security email

Purpose:

- confirm the person who signed up controls the email address
- start the onboarding journey with warm, confident messaging
- mention the learner's one-time free question generation trial
- encourage subscription without sounding aggressive

Current state:

- Firebase Auth verification email is already triggered in `AuthScreen.jsx`

Recommended improvements:

1. Block privileged onboarding steps until the account is verified where appropriate.
2. On login, reload the auth user and check `emailVerified`.
3. If not verified, show a clear message and provide a resend option.
4. Consider preventing unverified users from fully entering protected learning flows until verification is complete.
5. Decide whether Firebase's built-in email template is sufficient or whether a custom server-side branded verification flow is needed.
6. If built-in Firebase verification is retained, update the Firebase Auth email template in the console to use warm, polished copy.
7. If the learner's signup name must appear in the email body, plan for a custom backend-driven mail flow because Firebase's default template system is limited.

### Email 2: welcome email after verification

Purpose:

- send a branded welcome after the security step is complete

Recommended implementation path:

1. Detect the transition from `emailVerified = false` to `true`.
2. Trigger a server-side welcome email exactly once.
3. Store a user flag such as:
   - `welcomeEmailSent: true`
   - `verifiedAt`
4. Personalize the message with the learner's signup name.
5. Mention the one-time free question generation trial if it has not yet been used.
6. Encourage subscription in a warm, motivating tone.

### Email 3: POP uploaded -> admin notification email

Purpose:

- notify super admin / owner recipients that a learner has submitted proof of payment and the system should be checked

Recommended implementation path:

1. Trigger a server-side email when a new `pending_payments` record is created.
2. Send the message to all configured owner/super-admin recipient addresses.
3. Include at least:
   - learner name
   - learner email
   - requested grade
   - selected plan
   - reference used
   - submission timestamp
4. Store mail status fields if needed, such as:
   - `adminPopNotificationSentAt`
   - `adminPopNotificationRecipients`

### Email 4: POP approved -> learner congratulations email

Purpose:

- celebrate successful subscription approval and encourage the learner to begin using the platform

Recommended implementation path:

1. Trigger a server-side email when a pending payment is approved.
2. Personalize the message with the learner's signup name.
3. Use a congratulatory tone with encouragement and best wishes.
4. Direct the learner back to the app to start using their subscribed access.
5. Store a user/payment flag such as:
   - `subscriptionApprovalEmailSentAt`
   - `lastApprovalEmailPaymentId`

## Important architecture note

Do not send lifecycle emails directly from insecure client-side code.

Recommended options:

1. Firebase Cloud Functions triggered from user document state changes
2. Firebase Auth / Firestore driven backend worker
3. Third-party mail provider such as SendGrid, Mailgun, Resend, or similar from server-side code

## Recommended user document fields

- `emailVerifiedAt`
- `welcomeEmailSent`
- `verificationReminderCount` if needed later
- `adminPopNotificationSentAt`
- `subscriptionApprovalEmailSentAt`
- `lastApprovalEmailPaymentId`

Recommended files:

- `src/components/auth/AuthScreen.jsx`
- `src/hooks/useAuthentication.js`
- `src/components/student/EftUploadModal.jsx`
- `src/components/forms/AdminForms.jsx`
- new backend mailer/functions files
- possibly `firebase.json` if functions are added to this repo structure later

Acceptance check:

- verification email is always sent on signup
- login flow clearly handles unverified users
- welcome email is sent once after verification
- super admin recipients get an email when a POP is uploaded
- approved learner gets a congratulations email by name

## Phase 7. Update the EFT modal branding and banking details

This is a straightforward UI/content update, but it should align with the wider subscription flow.

## Requested header content

Header ribbon should show:

1. graduation cap logo + `fundile`
2. title: `SUBSCRIPTION`
3. subtitle: `EFT payment step`

## Requested banking details

- Bank: `Access Bank`
- Account number: `51622451787`
- Branch code: `410506`

## Recommended extra updates while touching this modal

1. Replace the email-based reference with the shorter bank-safe Fundile reference if that work is approved for implementation.
2. Ensure learner `name` uses the stored profile name instead of falling back to a generic value where possible.
3. Make the modal header visually consistent with the splash/auth branding.

Recommended files:

- `src/components/student/EftUploadModal.jsx`
- optionally `src/components/ui/Header.jsx` or shared logo components if a reusable brand header is extracted

Acceptance check:

- modal header shows the requested brand content
- banking details match the values above
- modal still uploads successfully

# Dependencies and sequencing notes

## High-priority dependency chain

1. Splash/auth routing should be finalized first.
2. Splash visual rollback can be done next.
3. Free-question gating should be implemented before notification wording is finalized, because trial/subscription state affects messaging.
4. Exact-problem saving should be scoped to Grade 10 and 11 Accounting first.
5. Verification + lifecycle emails require backend/server-side planning before implementation.
6. EFT modal branding can be implemented independently once subscription wording is confirmed.

# Risks and design cautions

## 1. Free-question tracking must be server-backed

Do not rely only on local component state for the one-free-question rule.

Reason:

- refreshes or alternate flows would bypass it

## 2. Exact saved questions should not depend on regeneration

Do not save only topic/subtopic and then regenerate later.

Reason:

- the learner may receive a different accounting question later

## 3. Welcome email should be idempotent

Ensure the welcome email is sent only once after verification.

## 4. POP admin and approval emails must be event-safe and idempotent

Ensure duplicate writes or retries do not send duplicate admin POP or approval emails.

## 5. Notification bell should not mix placeholder content with real events

Once data-driven notifications are introduced, remove any default hard-coded notification items.

## 6. Logout should reset top-level state cleanly

Signing out should clear dashboard-specific state before routing through splash and landing.

# Suggested verification checklist after implementation

## Splash and routing

- signed-out refresh -> splash -> landing
- signed-in refresh -> splash -> dashboard
- logout -> splash -> landing
- signed-in user does not randomly land on marketing page during normal authenticated flow

## Splash visuals

- static cap is shown
- old-style `fundile` reveal is restored
- timing feels like the copy version

## Free-question gating

- first unsubscribed generation works once
- second attempt shows subscribe popup
- subscribed users can continue normally

## Saved exact problems

- save button appears only after compare/check
- saved question reopens exactly as seen
- Grade 10 and 11 Accounting work first

## Notifications

- welcome notification appears after signup
- congratulations notification appears after subscription approval
- no fake default assignment list remains

## Email flow

- verification email is sent on signup
- unverified user handling is clear
- welcome email is sent once after verification
- POP upload sends an email to configured super admin recipients
- approval sends a congratulations email to the learner by signup name

## EFT modal

- header branding is correct
- banking details are correct
- POP upload still reaches `pending_payments`

# Suggested first implementation batch

To reduce risk, implement in this order:

1. Splash routing rules
2. Splash visual rollback
3. One-free-question subscription gating
4. EFT modal content update
5. Data-driven notifications
6. Exact saved accounting questions
7. Verification enforcement + lifecycle emails

This order keeps the highest-visibility user experience fixes first while reserving the email/backend work for a more deliberate pass.
