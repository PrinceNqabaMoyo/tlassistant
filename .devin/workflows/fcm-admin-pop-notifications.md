---
description: Implement Firebase Cloud Messaging admin notifications for new POP uploads, with a non-email payment reference design
---
# Goal

Receive a phone notification in the Fundile admin experience whenever a new Proof of Payment (POP) is uploaded, without using the student's email address as the EFT reference.

# Current state in this project

- Student POP uploads are handled in `src/components/student/EftUploadModal.jsx`
- POP files are stored in Firebase Storage under `proofs_of_payment/...`
- POP records are stored in Firestore collection `pending_payments`
- Admin review already exists through the EFT approvals UI
- There is currently no email notification or push notification path
- The current `referenceUsed` fallback is based on `currentUser.email`, which should be replaced

# Recommended architecture

## 1. Keep uploads where they are

Continue using the existing flow:

1. Student uploads POP in `EftUploadModal`
2. File is uploaded to Firebase Storage
3. A Firestore document is created in `pending_payments`

This is already working and should remain the source of truth.

## 2. Use Firestore create events as the notification trigger

When a new `pending_payments` document is created, trigger a backend process to send an admin push notification.

Recommended implementation:

1. Add a Firebase Cloud Function
2. Listen for new documents in `pending_payments`
3. Send a push notification using Firebase Cloud Messaging (FCM)
4. Include enough context in the notification payload to identify the payment quickly

Suggested payload fields:

- `paymentId`
- `userId`
- `plan`
- `requestedGrade`
- `referenceUsed`
- `screen: eftApprovals`

## 3. Register admin devices for push notifications

To send notifications to your phone, the admin client must register an FCM token.

Implementation steps:

1. Add Firebase Messaging to the frontend
2. Request notification permission only for admin users
3. Get the device FCM token
4. Save the token to Firestore in an admin-owned collection

Recommended collection design:

- Collection: `admin_notification_tokens`
- Document fields:
  - `token`
  - `email`
  - `uid`
  - `platform`
  - `createdAt`
  - `lastSeenAt`
  - `isActive`

If multiple phones or browsers are used, store multiple tokens.

## 4. Make the admin experience phone-friendly

Use the existing admin area rather than building a separate app first.

Recommended approach:

1. Make sure the admin EFT approvals screen is usable on mobile
2. Install the app on the phone as a PWA if possible
3. When the notification is tapped, deep-link to the EFT approvals view

Recommended deep-link target:

- Open admin dashboard
- Route directly to `eftApprovals`

## 5. Add service worker support for web push

For web/PWA notifications, configure Firebase Messaging service worker support.

Typical pieces needed:

1. Firebase Messaging setup in the client
2. A messaging service worker in `public`
3. Foreground notification handling in the app
4. Click-handling logic to open the admin approvals screen

## 6. Create the Cloud Function that sends notifications

Recommended flow:

1. Firestore trigger fires on new `pending_payments` document
2. Function reads active admin notification tokens
3. Function builds a concise notification
4. Function sends push via FCM
5. Function logs success/failure and deactivates invalid tokens

Recommended notification content:

- Title: `New POP uploaded`
- Body: `Grade {requestedGrade} · {plan} · Ref {referenceUsed}`
- Data payload:
  - `paymentId`
  - `screen: eftApprovals`

## 7. Add admin-side notification handling

In the app:

1. If the app is open, show an in-app toast/banner for new POPs
2. If the app is closed or backgrounded, let FCM display the push notification
3. On notification click, navigate to EFT approvals

## 8. Secure the token registration and sending flow

Security rules and checks should ensure:

1. Only authenticated admins can register admin notification tokens
2. Students cannot write admin tokens
3. Only server-side code sends FCM notifications
4. Client-side code never contains admin server keys or private credentials

## 9. Test the notification flow end to end

Recommended test sequence:

1. Log in as admin on your phone
2. Grant notification permission
3. Confirm an FCM token is saved to Firestore
4. Log in as a student on another device
5. Upload a test POP
6. Confirm:
   - the file appears in Storage
   - the record appears in `pending_payments`
   - the admin phone receives a push notification
   - tapping the notification opens EFT approvals

## 10. Add fallback observability

Even after push is working, keep a fallback path:

1. Continue storing all POPs in `pending_payments`
2. Optionally add an unread pending-payments badge in admin
3. Log notification send failures so uploads are never missed

# Recommended payment reference design

## Why not use email

Do not use the student's email as the EFT reference because:

- it exposes personal data
- it looks messy in bank statements
- it is harder to read quickly
- it can vary in formatting and length

## Recommended format

Use a short, bank-safe, fixed-length reference with a maximum of 10 characters.

Recommended production pattern:

- `F{C}{GG}{NNNNNN}`

Where:

- `F` = Fundile prefix
- `C` = curriculum code
  - `C` = CAPS
  - `M` = Cambridge, if ever supported later
- `GG` = 2-digit grade
  - `08`, `09`, `10`, `11`, `12`
- `NNNNNN` = unique 6-digit numeric seed

Examples:

- `FC10381742`
- `FC08004219`

This format is exactly 10 characters, uses only uppercase letters and numbers, and is easier to fit into strict bank reference fields.

## What should make it unique

Do not generate the payment reference from email directly.

Instead, create a stored reference seed per user profile and then derive the bank reference from that seed plus curriculum and grade.

Recommended fields on the user document:

- `paymentReferenceSeed`
- `paymentReferenceCurrent`

Example:

- `paymentReferenceSeed: 381742`
- `paymentReferenceCurrent: FC10381742`

## How to generate it safely

Recommended approach:

1. On user creation, generate a random 6-digit numeric seed that is not already in use
2. Store it on the user document
3. Build the visible reference from:
   - curriculum code
   - seed
   - grade
4. Display that reference in `EftUploadModal`
5. Save the exact reference actually used into `pending_payments.referenceUsed`

## Why a stored seed is better than generating every time

A stored seed gives you:

- a stable identity for the user across payments
- easy tracing in admin
- less confusion if they upload more than once
- no exposure of email addresses

## Suggested mapping rules

- `CAPS` -> `C`
- `Cambridge` -> `M`
- Grade 8 -> `08`
- Grade 10 -> `10`
- Grade 12 -> `12`

## Example reference builder logic

Inputs:

- curriculum: `CAPS`
- grade: `10`
- seed: `381742`

Output:

- `FC10381742`

## Internal readability recommendation

If you still want a more descriptive label inside the admin UI, keep that separate from the bank reference.

Recommended split:

- Bank reference: `FC10381742`
- Internal display label: `CAPS Grade 10 - FC10381742`

## Reference lookup design for admin approval

Because the bank reference is short, the system should include a dedicated lookup/index so an admin can match a reference to a learner before approval.

Recommended approach:

1. Keep the user profile as the source of truth
2. Add a dedicated Firestore reference index for fast admin lookup
3. Search by the exact reference shown on the bank statement
4. Display learner identity details before approving the POP

### Source of truth in the user document

Recommended fields on `users/{uid}`:

- `paymentReferenceSeed`
- `paymentReferenceCurrent`
- `name`
- `email`
- `curriculum`
- `grade`

### Fast lookup collection

Recommended collection:

- `payment_reference_index`

Recommended document ID:

- the reference itself, for example `FC10381742`

Recommended document fields:

- `uid`
- `name`
- `email`
- `curriculum`
- `grade`
- `reference`
- `seed`
- `isActive`
- `createdAt`
- `updatedAt`

### Why this lookup collection is recommended

- exact-reference lookup is fast and simple
- the admin does not need to query across all users
- the bank statement reference can be matched before POP approval
- name and email can be confirmed without exposing them in the reference itself

### Recommended admin workflow

1. Admin sees a bank statement reference such as `FC10381742`
2. Admin searches or opens `payment_reference_index/FC10381742`
3. The system shows:
   - learner name
   - learner email
   - curriculum
   - grade
   - user ID
4. Admin compares that result to the uploaded POP in `pending_payments`
5. Admin approves or rejects the payment

### Recommended stability rule

The preferred implementation is to keep one current active reference per learner profile and update the index whenever the displayed reference changes.

If grade remains encoded in the bank reference, then the system must refresh `paymentReferenceCurrent` and the corresponding `payment_reference_index` record whenever grade or curriculum changes.

If you later decide to move to one fully stable lifetime reference instead, the same lookup collection design can remain in place.

# Recommended implementation order

1. Replace email-based `referenceId` in `EftUploadModal`
2. Add a stored payment reference seed to user profiles
3. Add and maintain `payment_reference_index` for fast admin lookup
4. Update POP uploads to save the new reference format
5. Add admin-side reference lookup before payment approval
6. Add admin token registration for notifications
7. Add FCM Cloud Function trigger on `pending_payments`
8. Add notification click routing to EFT approvals
9. Test the full student-upload to admin-phone flow

# Notes for this project

- FCM itself is free, but related Firebase usage may incur cost depending on scale
- Do not put FCM server credentials in the frontend
- Use backend or serverless code for notification sending
- The first version should prioritize reliability over a separate native app

# Suggested outcome

The preferred first release is:

1. Existing Fundile app remains the main app
2. Admin logs in on phone
3. Phone receives push when a POP is uploaded
4. Notification opens EFT approvals
5. EFT reference uses a short Fundile-specific identifier like `FC10381742`, not email
