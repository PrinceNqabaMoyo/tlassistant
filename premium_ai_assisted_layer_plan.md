# Premium AI-Assisted Layer Plan

## Audit Findings

### Existing foundation already in the app
- `src/hooks/useAuthentication.js`
  - stores `tier`
  - stores `subscribedGrades`
  - stores `subscribedSubjects`
  - stores `subscriptionExpiry`
- `src/components/workspace/Workspace.jsx`
  - passes `currentUser?.tier || 'standard'` into workspace routes as `subscriptionTier`
- `src/components/workspace/shared/WorkspaceModeShell.jsx`
  - already locks `marking` for `standard`
  - still uses the older label `pro` in comments / lock copy
- `src/components/student/EftUploadModal.jsx`
  - already provides a paid upgrade submission flow
  - monthly and yearly options
  - uploads POP into storage and writes to `pending_payments`
- `src/components/forms/AdminForms.jsx`
  - already lets admin review and approve `pending_payments`

### Gaps and inconsistencies
- There is no clean package catalog for `standard` vs `premium`.
- Tier naming is inconsistent.
  - current code mixes `standard`, `pro`, and `owner`
- Admin approval currently writes approved users back to `tier: 'standard'`, so a real premium tier is not activated.
- Premium AI features are not modeled as capabilities.
- There is no AI quota, usage tracking, or backend model gateway.

## Conclusion
A partial package structure already exists.

This project should **extend and normalize the current tier system**, not replace it with a second parallel system.

## Recommended package model

### Standard
- grade / subject access from existing entitlements
- scaffold mode
- practice mode
- current repositories and visual tools
- non-premium learning flows already in product

### Premium
Everything in Standard, plus:
- AI marking
- AI tutor / guided explanation
- AI answer improvement feedback
- AI source-document review
- premium compare / improve loops
- future premium AI study tools

### Owner
- full internal access
- bypass quotas and package locks

## Canonical tier names
Use these names everywhere:
- `standard`
- `premium`
- `owner`

Remove `pro` from UI and logic.

## Recommended AI delivery model
Use **provider-hosted open-source models behind the backend** first.

Reasons:
- fastest rollout
- easier cost control
- safer key handling
- simpler model switching
- self-hosting can come later if usage justifies it

Suggested model split:
- premium teaching / explanation model:
  - `Llama 3.1 70B Instruct` or `Qwen 2.5 32B Instruct`
- lighter / cheaper utility model:
  - `Llama 3.1 8B Instruct` or `Qwen 2.5 7B Instruct`

## Implementation phases

### Phase 1: Normalize entitlements
- create one entitlement resolver from user data
- map user record to capabilities such as:
  - `canUseMarking`
  - `canUsePremiumTutor`
  - `canUsePremiumSourceDocReview`
  - `canUsePremiumWritingCoach`
- update frontend gates to use capabilities instead of scattered tier checks
- change admin approval so premium approvals can actually set `tier: 'premium'`

### Phase 2: Define premium AI capability flags
Add capability fields in the user record or a derived entitlement object.

Recommended premium capability set:
- `marking`
- `premiumTutor`
- `premiumSourceDocReview`
- `premiumWritingCoach`
- `premiumCompareImprove`

### Phase 3: Add backend AI gateway
Create one backend layer that:
- checks authenticated user entitlement
- selects the model
- applies quotas
- logs usage
- returns normalized responses

Do not call model providers directly from the frontend.

### Phase 4: Roll out premium features one at a time
Recommended order:
1. AI marking
2. AI tutor
3. AI answer improvement
4. AI source-document review

This keeps scope controlled and makes failures easier to isolate.

### Phase 5: Add usage and quota controls
Track:
- requests per month
- tokens or estimated cost per month
- feature-level usage
- last reset month

This allows future pricing changes without redesigning the whole system.

## Recommended data additions
Extend user/payment handling with fields like:
- `tier`
- `premiumActivatedAt`
- `premiumExpiresAt`
- `entitlements`
- `aiUsage`
- `aiQuota`
- `paymentStatus`

## High-priority code targets
- `src/hooks/useAuthentication.js`
- `src/components/workspace/Workspace.jsx`
- `src/components/workspace/shared/WorkspaceModeShell.jsx`
- `src/components/student/EftUploadModal.jsx`
- `src/components/forms/AdminForms.jsx`

## Immediate next actions
1. Normalize tier naming to `standard` / `premium` / `owner`
2. Fix admin approval so premium access can actually be granted
3. Introduce a shared entitlement resolver
4. Convert current marking lock to capability-based gating
5. Add backend premium AI gateway before exposing any new AI feature

## Recommendation
Yes, there is already a partial standard/premium-style foundation.

No, it is not complete enough yet to support a real premium AI-assisted product safely.

The right path is to **build the premium AI layer on top of the existing entitlement and payment flow**, while first cleaning up tier naming and approval logic.
