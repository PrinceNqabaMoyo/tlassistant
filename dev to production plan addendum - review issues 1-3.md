# Dev to Production Plan Addendum - Review Issues 1-3

This addendum should be read alongside `dev to production plan.md`.

It exists because the review issues in `dev to production changes.md` require implementation decisions that are more specific than the current main plan text.

## Scope of this addendum

This document covers only these 3 review issues:

1. verification emails should use Fundile branding rather than the default Firebase sender
2. signed-in users should submit proof of payment from the subscription page instead of a payment-critical popup
3. the POP reference should use a stable user-linked identifier instead of defaulting to the user email address

## Implementation positioning

These issues do not replace the main plan. They refine it.

Recommended placement in the existing rollout:

- **Issue 1 below** belongs with auth hardening and verification work
- **Issues 2 and 3 below** belong with POP flow hardening and payment UX cleanup

---

# Issue 1: Verification emails should use Fundile branding

## Problem

The current verification flow appears to send from the default Firebase sender identity such as `noreply@...app.firebase.com`.

Even if the verification flow works technically, this weakens trust during onboarding because students see a platform-default sender instead of a Fundile sender.

## Decision lock

For production, verification email sender identity must be treated as a product trust requirement, not just a technical default.

Preferred outcome:

- use a Fundile-branded sender such as `noreply@fundile.com`

If Firebase Auth cannot support the desired sender identity directly in the current setup, then the fallback must be explicit and temporary, not accidental.

## Recommended implementation path

### Path A: Native provider configuration if available

Use Firebase Authentication email template and domain settings if they can support the intended branded sender and action links.

### Path B: Custom verification email flow if Path A cannot satisfy branding

If the default Firebase-auth email templates cannot deliver the required sender identity, move to a custom verification delivery path where:

- the app generates the verification action link securely
- Fundile sends the verification email through its own trusted sender/domain
- the app still enforces verified-email access before dashboard entry

## Execution steps

1. Audit the current verification flow in `AuthScreen.jsx` and the authenticated entry enforcement in `useAuthentication.js` and `App.jsx`.
2. Check the current Firebase Authentication email template and domain capabilities.
3. Decide whether the branded sender can be achieved through provider configuration alone.
4. If yes, configure the production sender/domain and verify deliverability.
5. If no, define a custom verification email delivery path and treat it as production auth work.
6. Keep resend verification support and the verification waiting state aligned with whichever path is chosen.
7. Confirm the branded sender is used in the real production flow, not only in test assumptions.

## Likely files and systems

- `src/components/auth/AuthScreen.jsx`
- `src/hooks/useAuthentication.js`
- `src/App.jsx`
- `src/components/auth/VerificationScreen.jsx`
- Firebase Authentication email template/domain configuration
- possibly a Fundile-managed verification email delivery path

## Acceptance criteria

- newly registered users receive a verification email
- the verification sender identity is Fundile-branded, or an explicitly approved temporary fallback is documented
- unverified users cannot enter the main product
- verified users can continue normally to the dashboard
- resend verification remains available and understandable

## QA checks

- sign up with a real test inbox
- verify the visible sender identity and reply-to behavior
- confirm spam-folder guidance is present if needed
- confirm the verification link completes the intended entry path

---

# Issue 2: Move POP submission from popup to the subscription page for signed-in users

## Problem

The current POP submission flow relies on a popup/modal interaction.

That may be acceptable for a temporary admin-style utility, but it is not the strongest UX for a payment-critical production journey. A signed-in user should be able to go to `/subscribe` and complete payment submission in a clear, stable page flow.

## Decision lock

For production:

- `/subscribe` should be the canonical payment submission surface
- signed-out users should still see the subscription information and the sign-in/sign-up path
- signed-in users should not be forced through a blocking popup to upload proof of payment

## Recommended UX decision

For a signed-in user on `/subscribe`:

- replace `Sign in to upload POP` with `Upload Proof of Payment`
- use a clear attachment-style affordance or button treatment
- keep the upload experience in-page
- show banking details, selected package context, upload requirements, upload status, and next-step messaging on the page

The old modal should either:

- be retired completely, or
- be reduced to a reusable internal upload panel extracted into a page section

## Execution steps

1. Keep `/subscribe` as the public subscription route.
2. Detect the signed-in state on that page.
3. For signed-out users, continue showing the public subscription information and sign-in path.
4. For signed-in users, render the upload flow directly in-page.
5. Refactor the useful parts of `EftUploadModal.jsx` into a reusable upload section if needed.
6. Remove modal-only assumptions from the payment path.
7. Ensure success and failure states remain visible without blocking overlays.

## Likely files

- `src/components/ui/SubscriptionPage.jsx`
- `src/components/student/EftUploadModal.jsx`
- possibly a new extracted in-page upload component such as a shared upload panel
- `src/App.jsx`
- subscription page entry points

## Acceptance criteria

- a signed-in user can go to `/subscribe` and immediately understand how to submit POP
- the signed-in payment flow works without relying on a payment-critical popup
- required payment details and upload requirements are visible on the page
- upload progress, errors, and success states are clearly shown in-page
- the overall experience feels like a production subscription flow rather than a temporary admin tool

## QA checks

- signed-out visit to `/subscribe`
- signed-in visit to `/subscribe`
- upload JPG, PNG, and PDF from the in-page flow
- confirm route stability during upload and after upload completion

---

# Issue 3: POP reference must use a stable user-linked identifier, not email

## Problem

The current payment guidance appears to still suggest the user email address as the POP reference.

That is weaker than using a stable user-linked payment identifier because:

- emails can change in presentation and readability
- admins need a single canonical reference format
- the user should be linked to payment records through one stable identifier

## Decision lock

For production, the POP reference shown to the user must be a stable user-linked identifier.

Preferred direction:

- use an already existing assigned user/payment reference if one is already present in the current user state or Firestore data model
- do not invent a second competing reference if a suitable unique identifier already exists
- do not use email as the primary visible POP reference unless there is no stable alternative and that limitation is explicitly accepted

## Required audit

Before implementation, confirm whether a usable existing reference already exists in one of these places:

- authenticated user state
- `users/{uid}` Firestore documents
- payment-related user fields already written during signup or subscription flows
- `pending_payments` records
- any existing reference/ID logic already used internally in EFT or admin review

## Implementation steps

1. Audit current reference generation and display in the subscription and POP upload flow.
2. Identify the best existing stable reference if it already exists.
3. If no suitable reference exists, define one canonical reference format and persist it deliberately.
4. Show that same reference in the signed-in subscription UI.
5. Store that same reference in `pending_payments`.
6. Keep the same reference visible in admin review workflows.
7. Remove email as the default user-facing payment reference.

## Likely files

- `src/components/ui/SubscriptionPage.jsx`
- `src/components/student/EftUploadModal.jsx`
- `src/hooks/useAuthentication.js`
- `src/components/forms/AdminForms.jsx`
- Firestore payment/user document fields

## Acceptance criteria

- the POP reference shown to the user is not the email address
- the same reference is stored with the payment record used for review
- the same reference can be traced back reliably to the signed-in user
- admin review does not depend on email-only matching

## QA checks

- inspect the signed-in subscription page and confirm the displayed reference
- upload POP and confirm the reference stored in `pending_payments`
- verify admin-side review can locate and understand the same reference

---

# Recommended implementation order

To minimize rework, implement these in this order:

1. **Reference audit first**
   - determine whether a stable user-linked reference already exists
2. **POP page refactor second**
   - move signed-in POP submission to `/subscribe`
3. **Verification sender branding third, unless blocked by provider setup lead time**
   - complete the sender/domain decision and delivery path

If verification branding depends on external provider configuration and takes longer, the POP reference audit and `/subscribe` refactor can proceed in parallel, but the branded sender decision should still be tracked as a launch gate.

---

# Release gate additions

These should be added to the real production readiness review even if the main plan file is not yet amended.

## Auth

- verification email sender identity matches the intended Fundile production brand
- verification sender fallback, if any, is deliberate and documented

## Subscription and POP

- signed-in users submit POP from `/subscribe`, not from a payment-critical popup
- the displayed POP reference is a stable user-linked identifier
- payment records store the same reference used in the user-facing flow

## Launch blockers for these issues

Do not move to production if any of the following remain true:

- verification emails still appear to come from an accidental default sender with no approved fallback decision
- signed-in POP submission still depends on a confusing popup when the page flow is supposed to be canonical
- the POP reference still defaults to the user email instead of the intended stable user-linked identifier

---

# Summary

This addendum converts the 3 review issues into implementation work:

- **Issue 1** is now an auth trust and verification branding task
- **Issue 2** is now a subscription-page payment UX refactor
- **Issue 3** is now a payment reference canonicalization task

These changes should be treated as production-facing trust work, not cosmetic polish.
