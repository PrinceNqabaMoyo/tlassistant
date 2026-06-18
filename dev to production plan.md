# Dev to Production Plan

## Goal

Ship a stable MVP to production that is honest about current availability, easy to navigate, safe for real users, and commercially usable for Grade 10 and Grade 11 Accounting.

The current production objective should be:

- Limit the live offer to **CAPS Grade 10 and Grade 11 Accounting**
- Ensure authentication, routing, and subscription flows behave predictably
- Remove legacy/test UI that weakens trust
- Make subscription and proof-of-payment flows reliable enough for paying customers
- Present clear messaging about what is available now versus what is coming soon

## Execution framing

This plan should now be treated as an **execution plan**, not only a strategy note.

That means each section should help answer four questions:

- What decision is being locked for MVP?
- What code areas are most likely to change?
- What must be true before we move to the next phase?
- What can be deliberately deferred until after launch?

For this launch, the main discipline is **scope protection**. Any feature that weakens trust, introduces routing instability, or exposes unfinished subject coverage should be blocked, simplified, or deferred.

---

## Core Product Decision Before Implementation

### Issue 1: Should we create pages like `gradeX/dashboard/subject`?

### Recommendation

**Do not build a large route tree for every grade/subject before MVP launch.**

For this production push, the better approach is:

- Keep a **small canonical route set**
- Add a clear **`/dashboard`** route for signed-in users
- Keep the detailed subject/grade state inside the app until the catalog is broader and more stable
- Only introduce deeper subject routes later if they materially improve SEO, sharing, or support workflows

### Decision lock for execution

For the MVP, the route architecture should be locked to:

- a small top-level public route set
- one stable authenticated dashboard entry point
- one active workspace route
- no grade-specific or subject-specific browser routes yet

This decision should remain fixed unless a production blocker is discovered. It should not be reopened during cleanup work, because reopening route structure late in the cycle is likely to create regressions in auth, history behavior, and page transitions.

### Recommended MVP route map

- `/` - landing page
- `/signin` - sign in
- `/signup` - sign up
- `/subscribe` - subscription page
- `/dashboard` - signed-in home/dashboard
- `/app` - active workspace/question flow
- `/verify-email` - optional dedicated verification status/resend page

### Why this is better for MVP

- Less routing complexity
- Less browser history breakage
- Faster production launch
- Easier to maintain while content is still limited
- Keeps focus on payments, access, and retention instead of route expansion

### Explicit deferrals

The following items should be deferred until after MVP launch unless they become essential:

- deep-linkable grade routes
- deep-linkable subject routes
- SEO-oriented per-subject pages
- shareable assignment or workspace URLs
- route-level restructuring for future catalog expansion

---

## Recommended Delivery Order

### Phase 1: Routing, auth, and access foundation

Covers issues **1, 2, 3, 4, 5, 13**

### Phase 2: MVP scope lockdown and trust cleanup

Covers issues **6, 7, 9, 10, 11, 12**

### Phase 3: User communication and demand capture

Covers issues **8, 14**

### Phase 4: Payment operations hardening

Covers issue **15**

### Phase 5: QA, staging, and production release

Covers end-to-end verification before launch

## Phase readiness rule

Do not advance from one phase to the next only because coding has started. Move phases only when the previous phase is stable enough not to poison the rest of the rollout.

### Minimum exit rule for each phase

- The primary user path for that phase works end to end
- The main regression risks for that phase are manually checked
- The user-facing copy for that phase is production-safe
- The next phase does not depend on unresolved behavior from the previous one

### Practical meaning for this rollout

- Do not start UI gating cleanup before routing/auth behavior is stable
- Do not widen notifications or demand-capture work before MVP scope is locked
- Do not rely on EFT monetization before POP upload reliability is verified
- Do not cut over to production until signup, login, access gating, and POP submission all pass a real-user test flow

---

# Detailed Plan By Issue

## Issue 1: Routing architecture decision

### Objective

Avoid overbuilding route complexity before MVP.

### Plan

- Keep top-level navigation simple
- Introduce `/dashboard` as the canonical post-login page instead of using only `/app`
- Keep grade and subject selection in app state for now
- Revisit per-grade or per-subject routes only after more grades and subjects are live

### Execution steps

1. Update the route map and route resolver to support the final MVP route set.
2. Separate the meaning of `/dashboard` and `/app` clearly in code.
3. Confirm which signed-in views belong to dashboard versus workspace.
4. Remove any accidental dependence on implicit route fallbacks.
5. Manually test refresh behavior on every top-level route.

### Dependencies

- This work should be completed before browser-history fixes are finalized.
- This work should be completed before dashboard cleanup starts, because later UI changes depend on a stable route model.

### Likely files

- `src/app/constants/routes.js`
- `src/app/hooks/useTopLevelRouting.js`
- `src/App.jsx`

### Acceptance criteria

- A signed-in user lands on a stable dashboard URL
- No grade-specific routes are required for launch
- Top-level routes are human-readable and production-ready

---

## Issue 2: Signed-in users should always go directly to `/dashboard`

### Objective

Ensure login reliably sends students to the signed-in dashboard.

### Plan

- Add `/dashboard` to route resolution and history mapping
- On successful sign-in, route authenticated users to `/dashboard`
- Keep `/app` for active workspaces only
- If a signed-in user manually visits `/signin` or `/signup`, redirect them to `/dashboard`

### Execution steps

1. Decide whether `/app` remains a secondary authenticated route or becomes purely internal.
2. Make successful auth resolve to `/dashboard` consistently for both fresh sign-in and page refresh.
3. Ensure direct visits to public auth routes while authenticated are normalized to `/dashboard`.
4. Confirm logout clears the authenticated route state correctly.

### Go-live check

- New sign-in lands on `/dashboard`
- Refresh on `/dashboard` stays on dashboard
- Typing `/signin` while authenticated redirects cleanly
- Logout does not leave the browser on a misleading authenticated URL

### Likely files

- `src/app/constants/routes.js`
- `src/app/hooks/useTopLevelRouting.js`
- `src/components/auth/AuthScreen.jsx`
- `src/App.jsx`

### Acceptance criteria

- Sign-in always ends on `/dashboard`
- Refreshing `/dashboard` preserves the dashboard view
- Visiting `/signin` while authenticated redirects to `/dashboard`

---

## Issue 3: Missing verification security layer

### Current observation

The app already sends a verification email during sign-up in `AuthScreen.jsx`, but the flow is incomplete for production because it does not yet fully enforce verification or guide the user cleanly.

### Objective

Turn verification from a partial mechanism into an enforced production flow.

### Plan

- Keep `sendEmailVerification` on signup
- Add a clear post-signup verification screen or message state
- Prevent unverified users from accessing the dashboard/workspace until verified
- Add a resend verification action
- Add a friendly explanation for spam-folder checks and retry timing
- Ensure owner/admin accounts have a deliberate bypass only if truly necessary

### Execution steps

1. Audit the current signup flow and identify exactly where verification is sent and where it is ignored.
2. Add verified-email enforcement in the authenticated entry flow.
3. Add a lightweight verification waiting screen or route.
4. Add resend verification capability.
5. Decide whether internal owner/admin bypass exists, and if it does, document it explicitly.

### Go-live check

- Sign-up sends the email
- Unverified users cannot enter the product
- Verified users can proceed normally
- The verification failure state is understandable to a non-technical user

### Likely files

- `src/components/auth/AuthScreen.jsx`
- `src/App.jsx`
- `src/hooks/useAuthentication.js`
- possibly a new lightweight verification status component/page

### Acceptance criteria

- Newly registered users receive a verification email
- Unverified users cannot proceed into the main product
- Verified users can sign in normally
- Resend verification is available

---

## Issue 4: Add a clearer sign-in entry point

### Objective

Make sign-in obvious for returning users after logout or on future visits.

### Plan

- Add a dedicated **Sign in** CTA on the landing page header and/or hero area
- Keep **Get Started** for new users, but separate the returning-user path
- Ensure logout returns the user to a state where **Sign in** is immediately visible
- Keep `onNavigateSignIn` available from all public surfaces

### Execution steps

1. Add a persistent sign-in CTA on landing.
2. Review the subscription page and any public headers for the same returning-user path.
3. Confirm sign-out lands in a place where re-entry is obvious.
4. Remove any user journey that implies sign-up is the only way back in.

### Go-live check

- Returning users can get to sign-in in one action from the landing page
- No public page traps returning users in a sign-up-first flow

### Likely files

- `src/components/ui/LandingPage.jsx`
- `src/components/ui/SubscriptionPage.jsx`
- `src/app/hooks/useTopLevelRouting.js`

### Acceptance criteria

- Returning users can reach sign-in in one click from landing
- Logging out does not force a confusing sign-up-first journey

---

## Issue 5: Browser back button changes URL but not the actual view

### Current observation

Top-level history is already managed in `useTopLevelRouting.js`, but the internal app view state does not appear to stay synchronized with browser navigation.

### Objective

Make browser history and visible UI match.

### Plan

- Decide a strict MVP navigation model:
  - Top-level pages use browser history
  - Internal dashboard/workspace panes either:
    - also get route/history support, or
    - do not mutate browser history at all
- For MVP, the safest option is:
  - keep browser history only for top-level pages
  - make dashboard internal navigation explicit and state-driven
  - prevent stale URL changes that do not update the visible view
- Review logout/history reset behavior together with `useAppSessionReset.js`

### Execution steps

1. Audit which transitions currently push browser history.
2. Stop internal pane switches from pretending to be top-level page changes unless they are fully route-backed.
3. Normalize popstate handling so route and visible page always resolve from the same source of truth.
4. Retest logout, browser back, browser forward, and direct URL entry as one combined flow.

### High-risk area

This section is likely to produce regressions if routing changes and internal view-state changes are edited separately. It should be tested immediately after each routing change, not left for the end.

### Likely files

- `src/app/hooks/useTopLevelRouting.js`
- `src/app/hooks/useAppSessionReset.js`
- `src/App.jsx`
- render/shell modules handling dashboard and workspace transitions

### Acceptance criteria

- Clicking browser back changes both URL and visible page consistently
- No case exists where URL says one page while the screen shows another
- Logout/back flow is predictable

---

## Issue 6: Remove the test thumbnails button

### Objective

Remove visible dev/test affordances before production.

### Plan

- Find and remove the legacy thumbnails button from the static ribbon/header
- Confirm no dead navigation points remain
- Remove any related temporary labels or dormant UI entry points still visible to end users

### Execution steps

1. Locate every visible entry point for the thumbnails/test surface.
2. Remove the user-facing control, not only the first visible button.
3. Verify no hidden route, modal trigger, or fallback navigation still exposes the same surface.
4. Smoke-test the header or ribbon area after removal so layout and spacing remain clean.

### Go-live check

- No student-facing or public-facing page exposes a thumbnails test entry point
- Removing the control does not leave dead spacing or broken navigation

### Likely files

- `src/App.jsx`
- `src/components/ui/Header.jsx`
- any remaining references to thumbnail test surfaces

### Acceptance criteria

- No test thumbnails control is visible in production UI

---

## Issue 7: Student notifications should not load with old assignment data

### Objective

Ensure a new student does not see fake or stale assignment notifications.

### Current observation

`Notifications.jsx` currently presents pending assignments, so the production problem is likely seeded or leftover assignment state rather than a notification system built for real students.

### Plan

- Remove hardcoded or seeded assignment notifications from student state
- Ensure a new student starts with zero pending assignments unless real data exists
- Separate student notification data from teacher testing data
- Add defensive empty-state handling across the bell/notification trigger

### Execution steps

1. Trace the current notification source for newly created or newly loaded student accounts.
2. Remove any seeded pending assignment data from bootstrap or local defaults.
3. Ensure notification UI can render a true empty state without fallback test content.
4. Validate the behavior with a fresh account and with an existing account that has no real assignments.

### Dependency note

This cleanup should happen before the welcome-notification feature is added, otherwise the new notification work can end up layered on top of noisy or fake baseline data.

### Likely files

- `src/components/ui/Notifications.jsx`
- `src/App.jsx`
- `src/hooks/useAssignmentsPractice.js`
- any seed/mock assignment initialization

### Acceptance criteria

- New student accounts show no fake assignment notifications
- Only real assignment data appears

---

## Issue 8: Welcome notification for new users

### Objective

Introduce a minimal but real notification pattern that can later support assignments, teacher messages, and results.

### Plan

- Define a simple notification record format in Firestore
- Create a welcome notification when a new verified student account is created or first enters the product
- Add unread/read status support
- Keep the first version lightweight and message-based
- Do not overbuild real-time messaging yet

### Suggested notification types for MVP

- `welcome`
- `subscription_update`
- `system_notice`

### Execution steps

1. Decide whether the welcome notification is created at signup, at first verified login, or during user bootstrap.
2. Keep the data model intentionally small so it does not block launch.
3. Ensure the notification can be dismissed or marked read cleanly.
4. Confirm the welcome notification does not duplicate on every session.

### Go-live check

- A truly new student sees exactly one welcome notification
- Existing users do not get duplicate welcome notifications unless intentionally migrated
- Empty-state notification behavior still works for users with no messages

### Likely files

- `src/components/ui/Notifications.jsx`
- `src/App.jsx`
- auth/signup flow
- Firestore user bootstrap logic

### Acceptance criteria

- A new user receives a visible welcome notification
- Notifications can support future expansion without redesigning from scratch

---

## Issue 9: My Saved Problems should show Pro-only gating

### Objective

Set clear package expectations and route upsell behavior correctly.

### Plan

- Change the dashboard label/content for **My Saved Problems** to indicate **Only available in Pro package**
- Make the Pro label/button clickable
- Reuse the same Pro/subscribe modal used elsewhere
- Ensure Standard users cannot enter an unfinished saved-problems experience

### Execution steps

1. Audit every visible entry point into saved problems.
2. Replace ambiguous labels with explicit Pro-only messaging.
3. Route the call to action into one consistent upgrade/subscription path.
4. Confirm non-Pro users cannot still reach the unfinished screen by direct navigation or stale state.

### Scope note

For MVP, this section should behave as a gated upsell surface, not as a partially open feature. If saved problems are not fully ready for Standard users, the product should not imply otherwise.

### Likely files

- dashboard/student view components
- `src/App.jsx` if the view is still defined there
- subscription/Pro modal components
- `src/components/student/EftUploadModal.jsx` if reused for subscription prompt behavior

### Acceptance criteria

- Standard users see a clear Pro-only label
- Clicking the Pro CTA opens the expected upsell modal
- No incomplete saved-problems workflow is exposed to Standard users

---

## Issue 10: Class assignments should show “facility not yet available in South Africa”

### Objective

Replace unfinished functionality with honest product messaging.

### Plan

- Replace active assignment-entry access for unsupported users with an informational blocked state
- Use consistent wording across dashboard cards, buttons, and modals
- Make sure this does not conflict with the future notifications/teacher roadmap

### Execution steps

1. Find all assignment entry points in the student-facing product.
2. Replace interactive assignment launch behavior with a blocked informational state.
3. Use one approved wording variant everywhere this appears.
4. Confirm assignment-related notifications do not contradict the blocked-state message.

### Go-live check

- Students cannot enter an unfinished assignment experience
- The blocked message is consistent across card, modal, and notification contexts

### Likely files

- student dashboard components
- `src/components/ui/Notifications.jsx`
- assignment-related hooks and views

### Acceptance criteria

- Users see the “not yet available in South Africa” message instead of unfinished assignment UX

---

## Issue 11: Remove Learning Tools and Components

### Objective

Remove legacy or low-confidence modules that reduce trust and clutter the MVP.

### Plan

- Remove the **Learning tools** section from the student/dashboard UI
- Remove public access to generic **Components** repositories or experimental component browsers
- Hide or delete routes/buttons that expose legacy math/science component galleries if they are not core to the MVP
- Confirm no broken imports remain after UI removal

### Execution steps

1. Inventory all student-visible links and cards for Learning Tools and Components.
2. Remove those entry points from the main product shell.
3. Check whether any router, registry, or workspace index still exposes those surfaces indirectly.
4. Verify import cleanup after removal so the dashboard does not break from unused or missing references.

### High-risk area

This cleanup can look small in the UI but still break shell navigation if component registries or route maps still assume those sections exist.

### Likely files

- dashboard and workspace navigation UI
- `src/components/workspace/Workspace.jsx`
- `src/App.jsx`
- header/shell render files

### Acceptance criteria

- Learning Tools and Components are no longer visible to end users
- No dead buttons or broken screens remain

---

## Issue 12: Non-Accounting subjects in Grade 10/11 should show “Coming soon”

### Objective

Focus the MVP on the only subjects currently ready for market.

### Plan

- Define the live subject matrix explicitly:
  - Grade 10 Accounting: live
  - Grade 11 Accounting: live
  - Other Grade 10/11 subjects: blocked with **Coming soon**
- Intercept subject card clicks before unsupported workspaces open
- Use one consistent modal/message component for unsupported subjects

### Decision lock for execution

Until launch, the supported subject matrix should be treated as fixed:

- Grade 10 Accounting: live
- Grade 11 Accounting: live
- all other student-visible Grade 10 and 11 subjects: blocked

Do not allow ad hoc exceptions during UI cleanup unless the content and workflow are production-ready.

### Execution steps

1. Centralize the supported-subject rule instead of scattering one-off checks across the UI.
2. Intercept unsupported subject selection before the workspace loads.
3. Standardize the Coming Soon message so it feels intentional rather than broken.
4. Test both Grade 10 and Grade 11 subject pickers against the approved matrix.

### Likely files

- curriculum navigation components
- `src/curriculumData.js`
- student dashboard/subject selection views
- `src/App.jsx` or extracted student render modules

### Acceptance criteria

- Unsupported Grade 10/11 subjects do not open unfinished flows
- Users see a clean “Coming soon” message instead

---

## Issue 13: Temporarily block sign-ups for grades other than 10 and 11, except owner/super admin emails

### Objective

Prevent users from signing up into grades that are not ready.

### Plan

- Restrict student signup grade options to 10 and 11 for normal users
- Keep an allowlist for owner/super admin emails that can still use other grades
- Enforce this both:
  - in the frontend form
  - and in backend/security validation where possible
- Show a clear explanation when a blocked grade is attempted

### Current observation

`AuthScreen.jsx` currently exposes CAPS grades 7 to 12. That should be reduced for production unless the email belongs to an approved internal allowlist.

### Execution steps

1. Replace the default student grade options with Grade 10 and Grade 11 only.
2. Define the internal allowlist source for owner/super admin emails.
3. Enforce the restriction in the signup submission path, not only in the visible dropdown.
4. Decide how blocked-grade attempts are communicated to internal users versus public users.

### Go-live check

- Normal student sign-up only allows Grades 10 and 11
- Internal allowlisted accounts can still access non-public grades if needed
- A crafted client-side request cannot silently bypass the rule

### Likely files

- `src/components/auth/AuthScreen.jsx`
- auth bootstrap and user creation logic
- optional backend/admin guard for allowlisted emails

### Acceptance criteria

- Normal users can only sign up for Grade 10 or 11
- Approved owner/admin emails can bypass the restriction when needed
- Grade restrictions are not enforced only in the UI; they are validated safely

---

## Issue 14: Be transparent about current availability and capture demand

### Objective

Set expectations clearly and learn what users want next.

### Plan

Add clear messaging in public surfaces that:

- Fundile currently supports **Grade 10 and 11 Accounting**
- More grades and subjects are coming soon
- Interested users can contact Fundile for rollout timelines or submit demand

### Recommended execution

- Add a short availability banner on the landing page
- Add the same availability note on the subscription page
- Add a lightweight demand capture form or interest form collecting:
  - name
  - email
  - curriculum
  - requested grade
  - requested subject
  - optional school/teacher role
- Store submissions in Firestore or a simple form backend for prioritization

### Execution steps

1. Approve one canonical wording block for current availability.
2. Reuse that wording across landing, subscription, and blocked-feature messaging where appropriate.
3. Keep the demand form lightweight enough that it does not become a mini-onboarding flow.
4. Decide where submissions are stored and who will monitor them.

### Scope note

The point of this section is to increase trust and collect demand, not to promise unsupported timelines. The wording should be clear, conservative, and consistent with the actual MVP scope.

### Likely files

- `src/components/ui/LandingPage.jsx`
- `src/components/ui/SubscriptionPage.jsx`
- new demand capture component/form

### Acceptance criteria

- Visitors can immediately understand what is live now
- The team receives usable demand signals for rollout prioritization

---

## Issue 15: POP upload hangs and the UX needs redesign

### Current observation

`EftUploadModal.jsx` uploads to Firebase Storage with `uploadBytes`, then writes a Firestore `pending_payments` record and updates the user document. The “uploading for 30 minutes” symptom suggests the need for upload diagnostics, validation, progress/error handling, or storage/firestore configuration review.

### Objective

Make proof-of-payment submission reliable, fast to understand, and visually trustworthy.

### Plan

#### Reliability work

- Add file-size and file-type validation before upload starts
- Use resumable upload with progress reporting instead of a blind spinner
- Add upload timeout/error states with user-friendly recovery messaging
- Log exact failure points:
  - file selection
  - storage upload start
  - storage upload success
  - download URL retrieval
  - Firestore write
  - user document update
- Check Firebase Storage rules and Firestore rules for POP paths
- Confirm PDFs are accepted and not blocked by rule or metadata constraints
- Prevent duplicate submissions during upload

#### UX redesign work

- Improve layout hierarchy and spacing
- Make the banking details section easier to scan and copy
- Show accepted file types, max file size, and upload status clearly
- Add a visible progress bar for upload
- Improve the success state and next-step messaging
- Make the modal feel more like a polished payment submission flow than a temporary admin form

### Execution steps

1. Reproduce the long-running upload symptom with the current modal before redesigning the flow.
2. Instrument the upload path so it is obvious whether failure occurs in Storage upload, URL retrieval, Firestore write, or user update.
3. Replace the current upload approach with a progress-aware upload path if the current implementation cannot provide reliable status.
4. Add clear preflight validation for type, size, and duplicate submission attempts.
5. Redesign the modal only after the failure points are understood, so the UI reflects the true system behavior.

### Diagnostic sequence

Run investigation in this order:

1. Confirm allowed file types and size thresholds.
2. Confirm Firebase Storage rules for the POP upload path.
3. Confirm Firestore write permissions for `pending_payments` and the related user update.
4. Test JPG, PNG, and PDF separately.
5. Verify whether the issue is a real hang, a missing progress state, or a silent permission failure.

### Go-live check

- A supported file either uploads successfully or fails with a clear reason in a reasonable time
- Users can see progress while upload is in flight
- A successful upload creates the required payment records and user status updates
- The modal clearly explains what happens next after submission

### Likely files

- `src/components/student/EftUploadModal.jsx`
- Firebase Storage rules
- Firestore rules
- subscription page entry points

### Acceptance criteria

- PDF and image uploads complete reliably
- Users can see progress and clear errors
- Submission cannot hang silently
- The POP modal looks production-ready

---

# Cross-Cutting Production Tasks

## A. Remove visible dev/test artifacts

Before release, audit and remove:

- test thumbnails button
- any demo-only entry points
- temporary teacher-mode leftovers exposed to students
- experimental component browsers exposed in the public/student experience
- console-heavy debug behavior in user-critical flows where appropriate

### Execution note

This audit should be treated as a release gate, not a cosmetic cleanup task. If a student can still see internal, demo, or unfinished product surfaces, the MVP message becomes less credible immediately.

## B. Scope guardrails

The MVP should intentionally present itself as:

- a Fundile launch focused on **Grade 10 and 11 Accounting**
- subscription-ready through EFT
- expanding by demand over time

Do not ship ambiguous access to incomplete grades, subjects, or teacher workflows.

### Execution note

Whenever a feature sits between “partly works” and “not ready,” default to blocking it with clear messaging rather than exposing it in a confusing state.

## C. Data model cleanup

Review user bootstrap fields to ensure production clarity:

- verification status
- subscription status
- payment status
- welcome notification seeded
- role separation between student/teacher/admin
- supported-grade/subject access logic

### Execution note

If these fields are inconsistent, the UI cleanup will not hold. Routing, notifications, subscription gating, and subject access all depend on user state being explicit and trustworthy.

---

# Suggested Implementation Sequence

This sequence should now be treated as the default execution order unless a blocking dependency is discovered during implementation.

### Execution rule

Do not run multiple risky foundations in parallel unless they are genuinely isolated. In particular, routing/auth changes and state/bootstrap changes should be stabilized before aggressive UI cleanup is merged on top.

## Sprint 1: Navigation and auth hardening

- Finalize route strategy
- Add `/dashboard`
- Fix sign-in landing behavior
- Enforce email verification
- Add explicit sign-in CTA
- Fix browser history/view consistency
- Block non-10/11 signups except allowlisted internal emails

### Sprint 1 exit criteria

- A new user can sign up, verify, sign in, and land in the correct authenticated state
- A returning user can sign in and reach `/dashboard` reliably
- Browser back, forward, refresh, and logout no longer leave the app in a mismatched route/view state
- Public users cannot sign up into unsupported grades unless explicitly allowlisted

## Sprint 2: MVP scope lockdown

- Remove test thumbnails button
- Remove Learning Tools and Components
- Block unsupported Grade 10/11 subjects with Coming Soon
- Replace Class Assignments access with the South Africa availability message
- Gate My Saved Problems behind Pro
- Remove fake student notifications

### Sprint 2 exit criteria

- Students only see production-safe dashboard options
- Unsupported subjects and unfinished facilities are blocked intentionally, not accidentally
- No stale test surfaces or fake assignment notifications remain in the student experience

## Sprint 3: Communication and monetization polish

- Add welcome notification
- Add availability messaging on landing/subscription pages
- Add demand capture form
- Ensure Pro upsell messaging is consistent everywhere

### Sprint 3 exit criteria

- Public messaging matches actual MVP scope everywhere a user might make a purchase decision
- New users receive the intended welcome communication without duplicate noise
- Upsell and availability messaging are clear enough that unsupported features do not feel broken

## Sprint 4: POP flow hardening

- Diagnose PDF upload failure
- Add progress-based resumable upload
- Improve validation and error handling
- Redesign POP modal UX
- Verify pending payment records and user updates end to end

### Sprint 4 exit criteria

- POP upload behavior is observable, reliable, and understandable to the user
- A failed upload produces a clear error state
- A successful upload updates the expected records and gives the user clear next-step messaging

## Sprint 5: Production readiness QA

- Fresh-account signup and verification test
- Returning-user sign-in test
- Logout and browser back-button test
- Grade restriction and owner bypass test
- Unsupported-subject coming-soon test
- Standard vs Pro gating test
- POP upload test with JPG, PNG, and PDF
- Mobile and desktop UI pass

### Sprint 5 exit criteria

- All critical-path tests pass on the staging-ready build
- No blocker remains in auth, routing, subject gating, or POP submission
- The product is credible enough to present to paying users without visible internal artifacts

## Launch blockers

Do not move to production if any of the following are still failing:

- verified users cannot reliably reach the dashboard
- browser URL and visible screen still fall out of sync
- unsupported grades or subjects still open unfinished flows
- students still see demo, test, or internal-only surfaces
- Pro gating can be bypassed accidentally
- POP upload can still hang silently or fail without explanation

---

# Production QA Checklist

This checklist should be run in order, not as isolated spot checks. The earlier items validate the base assumptions for the later ones.

## Critical path smoke-test order

1. Sign up with an allowed grade.
2. Verify the email and enter the product.
3. Sign out and sign back in as a returning user.
4. Validate dashboard-only access and blocked unsupported subjects.
5. Validate Standard versus Pro gating.
6. Submit POP with at least one image and one PDF.
7. Retest browser back/forward and refresh after the above flows.

## Public flows

- Landing page clearly communicates current availability
- Sign in is obvious for returning users
- Subscription page is trustworthy and accurate

## Auth flows

- Signup works only for allowed grades
- Verification email is sent
- Unverified users are blocked appropriately
- Verified users reach `/dashboard`

## Product scope

- Only Grade 10/11 Accounting is usable
- Other subjects show Coming Soon
- Unsupported facilities are clearly labeled

## Monetization

- Pro-only areas are gated consistently
- Subscription CTA paths are coherent
- POP uploads work reliably

## Navigation

- URL and visible page stay in sync
- Back/forward behavior is predictable
- Logout resets app state cleanly

## Data and state integrity

- Newly created users have the expected verification and access fields
- Welcome notifications are not duplicated on reload or relogin
- Subscription and payment state do not contradict visible gating

---

# Production cutover checklist

## Before deployment

- Confirm the staging-ready build is the one being released
- Confirm Firebase rules relevant to auth, POP upload, and payment records are the intended production rules
- Confirm any internal allowlists or admin bypasses are deliberate and current
- Confirm public-facing copy reflects only live MVP functionality

## Immediately after deployment

- Test one real sign-in flow
- Test one real verified-user entry flow
- Test one blocked unsupported-subject flow
- Test one POP submission flow
- Confirm the dashboard and landing routes load correctly on direct URL access

## First-day monitoring

- Watch for failed signups or verification confusion
- Watch for users getting stuck between landing, sign-in, and dashboard
- Watch for POP submissions that never complete or never create records
- Watch for unsupported-subject clicks that still leak into unfinished workspaces

---

# Final Recommendation

This production push should not try to ship every future capability. It should ship a **narrow, trustworthy, paid MVP**.

The winning production shape is:

- clean landing page
- obvious sign-in/sign-up paths
- verified-user access
- dashboard-first signed-in experience
- Grade 10/11 Accounting only
- honest coming-soon messaging elsewhere
- reliable EFT + POP submission
- no visible legacy/test clutter

## Immediate execution recommendation

The first implementation package should now be:

1. route and auth stabilization
2. grade and subject access restriction
3. removal of student-visible legacy/test surfaces

That package will create the stable foundation needed before POP hardening and final launch polish.

If executed in that order, Fundile can go live faster, look more credible, and start generating revenue without overexposing unfinished functionality.


