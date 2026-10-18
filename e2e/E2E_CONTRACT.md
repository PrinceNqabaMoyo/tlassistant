# Fundile E2E Testing Contract & Anti-Hollywood Specification

> **Status:** Active & Mandatory  
> **Applicability:** All Playwright E2E suites (`e2e/*.spec.js`), subagents, human engineers, and testing automation.  
> **Enforcement:** Mechanical validation via `python scripts/audit_e2e_specs.py` and Rules 0d-1 through 0d-7 in `.agents/AGENTS.md`.

---

## 1. Executive Summary & The Anti-Hollywood Standard

In software engineering, **"Hollywood Testing"** (or theatrical engineering) is the practice of authoring test suites that produce entertaining, cosmetically reassuring console logs while avoiding actual end-to-end execution. Common Hollywood patterns include:
- Wrapping missing or broken UI elements in `if (await isVisible())` so that failures are silently skipped.
- Directly writing to the production or test database mid-test (e.g. flipping a user's subscription to `paid`) to pretend an approval occurred, bypassing broken UI buttons or authentication gates.
- Emulating administrative users with artificial URL parameters (`?persona=admin`) rather than authentic credentials, causing mock state leaks.
- Narrating success in `console.log` statements *before* or *without* verifying that DOM state actually changed.

**The Fundile Law:** Testing is an adversarial audit of genuine application behavior. Tests exist to expose defects, not to produce green checkmarks at all costs. Every test step must execute genuine end-to-end movements: authentic authentication, live form interactions, real file uploads, genuine on-screen button clicks, and real-time reactive state updates.

---

## 2. The 7 Non-Negotiable Invariants

### Invariant 1: Genuine User Actions vs. Backdoor Database Mutations (Rules 0d-1 & 0d-5)

1. **Clear Demarcation:**
   - **Pre-Flight Setup (Permitted):** Database helper scripts (`purgeTestUser.js`, database resets) are permitted **exclusively** before test execution begins to ensure a clean slate (e.g., deleting pre-existing test accounts in Firebase Auth and Firestore).
   - **In-Test Execution (Strictly Prohibited):** Once a test starts, database helper scripts (such as `approveTestPayment.js`) must **NEVER** substitute for user actions.
2. **The Clearance Flow Invariant:**
   - If a test journey states *"Super Admin reviews and approves the EFT Proof of Payment"*, the Super Admin browser window MUST:
     1. Authenticate as the Super Admin.
     2. Navigate to the Payment Approvals / Clearance Desk in the UI.
     3. Locate the pending payment card matching the learner's email and banking reference (`FND-...`).
     4. Click the "View POP" action to open the uploaded PDF via the authentic backend signed-URL endpoint (`/api/payments/pop-view-url`).
     5. Click the on-screen "Approve 90-Day Term Pass" button.
   - The learner browser window MUST then observe the paywall drop organically via Firestore's real-time `onSnapshot` listener.
3. Any test bypassing this flow via direct Firestore writes is considered defective and invalid.

---

### Invariant 2: Strict Super Admin Identity & Privilege Isolation (Rule 0d-2)

1. **Platform Owner Distinction:**
   - In `firestore.rules` (lines 10–17), owner privileges belong exclusively to verified owner emails:
     - `princenqaba@gmail.com`
     - `princenqabamoyo@outlook.com`
   - Super Admin is the **actual platform owner**, responsible for financial clearances, signed-URL issuance, and platform governance.
2. **Strict Isolation from Mock Personas:**
   - Super Admin is **NEVER** a mock persona (`MOCK_SUPER_ADMIN`).
   - Super Admin is **NEVER** simulated via URL query parameters (`?persona=admin` or `?persona=super_admin`).
   - Super Admin is **NEVER** seeded from mock classroom rosters (e.g., Westville High faculty).
   - Classroom stakeholders (teachers, parents, school admins) may use simulated environments (`?persona=teacher`, etc.) for roster demonstration; Super Admin clearance operations **MUST** use authentic credentials and valid Firebase Auth ID tokens.
3. **Signed URL Authorization Requirement:**
   - Viewing uploaded Proof of Payment files requires calling `/api/payments/pop-view-url`. This endpoint validates the caller's Firebase ID token via `_verify_request_user` and strictly checks `isOwnerEmail`. Passing fake query parameters fails this check; authentic authentication is required.

---

### Invariant 3: Role-State Decoupling Invariant (Rule 0d-3)

1. **State Isolation:**
   - Administrative (`AdminView`, `SystemSettingsView`), teacher (`TeacherDashboard`), parent (`ParentDashboard`), and school admin (`SchoolAdminView`) components must **NEVER** read or display state from `studentStore` unless explicitly inspecting a learner's academic record.
2. **Profile & Avatar Decoupling:**
   - Header avatars, profile modals (`UserProfileModal`), and settings for non-student roles must strictly derive identity from the authenticated role profile (`currentUser.name`, `currentUser.email`, `currentUser.photoURL`), never defaulting to mock learner state (e.g. "Nqobile Dlamini" or "FP").
3. **Test Assertion:**
   - In E2E tests, the Super Admin window must assert that the logged-in profile reflects the owner's identity, with zero contamination from student state stores.

---

### Invariant 4: Source-Code Grounding & Zero Phantom Selectors (Rule 0d-4)

1. **No Memory Guessing:**
   - An engineer or AI agent is strictly forbidden from writing or modifying a locator or test ID in an E2E spec without first viewing the exact target component in `src/`.
   - Guessing, hallucinating, or copying selectors from unrelated projects is strictly prohibited.
2. **Test ID Convention:**
   - All interactive elements must carry semantic `data-testid` attributes formatted as `[data-testid="<category>-<action/name>"]`:
     - Buttons: `data-testid="btn-landing-signup"`, `data-testid="btn-auth-submit"`, `data-testid="btn-approve-payment"`
     - Inputs: `data-testid="input-signup-email"`, `data-testid="input-signup-password"`
     - Tabs / Navigation: `data-testid="tab-admin-payments"`, `data-testid="tab-today-desk"`
     - Modals / Surfaces: `data-testid="modal-eft-upload"`, `data-testid="modal-user-profile"`
3. **Presence Verification:**
   - Every `data-testid` referenced in an E2E spec must exist in `src/`. The audit script (`scripts/audit_e2e_specs.py`) mechanically asserts this.

---

### Invariant 5: Zero Silent Skips in E2E (Rule 0d-6)

1. **The Banned Anti-Pattern:**
   - Banned: `if (await locator.isVisible())`
   - Banned: `if (await locator.count() > 0)`
   - Banned: `try { await locator.click() } catch (e) {}` (empty catch blocks)
2. **Why It Is Banned:**
   - If an element fails to appear due to a regression, network latency, or defect, an `if (isVisible())` wrapper quietly skips the code block. The test logs success despite the entire user journey failing to execute.
3. **The Mandatory Pattern:**
   - Every critical step must use explicit Playwright assertions with bounded timeouts:
     ```javascript
     const submitBtn = page.locator('[data-testid="btn-auth-submit"]');
     await expect(submitBtn).toBeVisible({ timeout: 10000 });
     await expect(submitBtn).toBeEnabled({ timeout: 5000 });
     await submitBtn.click();
     ```
   - If the element fails to appear or is disabled, the test halts loudly and produces an actionable error report.

---

### Invariant 6: Runtime Execution Verification (Rule 0d-7)

1. **Building is Not Executing:**
   - A successful build (`npm run build`) or clean linter (`npm run lint`) merely proves syntax and module resolution. It does **not** prove runtime functionality.
2. **Mandatory Execution Verification:**
   - Engineers and agents must run the actual Playwright specs:
     ```bash
     npx playwright test e2e/<spec_name>.spec.js --headed
     ```
   - The engineer must inspect the runtime console output, confirm that all steps executed without errors or timeouts, and verify that the expected state changes occurred in both the UI and database.

---

### Invariant 7: Viewport & Instrumentation Non-Interference (Rule 0d-7)

1. **Non-Interactive Margin Budget:**
   - Test instrumentation (such as `autopilotHud.js`, gliding cursors, pause toggles, or debug overlays) must **NEVER** be placed in interactive application zones:
     - Banned: Top headers, navigation bars, bottom tab bars, or modal action zones.
     - Allowed: Non-interactive margins, e.g. `bottom: 16px; left: 16px; width: 280px; max-height: 140px`.
2. **Pointer Events Isolation:**
   - Animated cursor overlays and HUD wrappers must have `pointer-events: none` on their visual surfaces so they never intercept or block clicks intended for underlying React components.

---

## 3. Concrete DO vs. DON'T Code Comparisons

### Comparison 1: Handling Payment Approvals in E2E

#### ❌ WRONG (Hollywood / Backdoor Pattern):
```javascript
// DON'T: Mid-test database write bypassing the UI
await pageLearner.click('[data-testid="btn-submit-pop"]');

// BACKDOOR MUTATION: Faking approval directly in Firestore
await approveTestPayment(testEmail, 90); 

// Cosmetic window open that doesn't actually approve anything
const pageAdmin = await browserAdmin.newPage();
await pageAdmin.goto('http://localhost:5173/?persona=admin');
await pageAdmin.click('[data-testid="tab-admin-payments"]');
// Test claims approval happened, but UI action was never tested!
```

#### ✅ CORRECT (Genuine End-to-End User Movement):
```javascript
// DO: Real submission in Learner window
await pageLearner.click('[data-testid="btn-submit-pop"]');

// DO: Super Admin authentically logs in and performs approval via UI
const pageAdmin = await browserAdmin.newPage();
await pageAdmin.goto('http://localhost:5173/');

// Sign in with verified platform owner credentials
await pageAdmin.click('[data-testid="btn-landing-signin"]');
await pageAdmin.fill('[data-testid="input-signin-email"]', process.env.SUPER_ADMIN_EMAIL);
await pageAdmin.fill('[data-testid="input-signin-password"]', process.env.SUPER_ADMIN_PASSWORD);
await pageAdmin.click('[data-testid="btn-auth-submit"]');

// Navigate to Payment Clearance Desk
const clearanceTab = pageAdmin.locator('[data-testid="tab-admin-payments"]');
await expect(clearanceTab).toBeVisible({ timeout: 10000 });
await clearanceTab.click();

// Locate the specific learner's pending payment email
const paymentEmail = pageAdmin.locator(`[data-testid="payment-email-${testEmail}"]`);
await expect(paymentEmail).toBeVisible({ timeout: 10000 });

// Verify the signed URL POP preview opens authentically via /api/payments/pop-view-url
const viewPopBtn = pageAdmin.locator('[data-testid="btn-view-pop"]').first();
await expect(viewPopBtn).toBeVisible();
const [popup] = await Promise.all([
  pageAdmin.waitForEvent('popup'),
  viewPopBtn.click()
]);
// Popup opens the signed storage download URL issued by the endpoint
await expect(popup).not.toBeNull();
await popup.close();

// Approve payment via on-screen UI button (90-day term pass)
const approveBtn = pageAdmin.locator('[data-testid="btn-approve-payment-90d"]').first();
await expect(approveBtn).toBeEnabled();
await approveBtn.click();

// Verify Learner window automatically unlocks via real-time onSnapshot paywall drop
await pageLearner.bringToFront();
await expect(pageLearner.locator('[data-testid="btn-open-subject-session"]').first()).toBeVisible({ timeout: 15000 });
```

---

### Comparison 2: Asserting Elements vs. Silent Skips

#### ❌ WRONG (Silent Skip Pattern):
```javascript
// DON'T: Silent skip using isVisible() condition
const termPlan = page.locator('[data-testid="plan-term-pass-349"]');
if (await termPlan.isVisible()) {
  await termPlan.click();
}

const popiaCheckbox = page.locator('[data-testid="checkbox-popia-consent"]');
if (await popiaCheckbox.isVisible()) {
  await popiaCheckbox.click();
}
// If either element failed to render, this test silently moves on and passes!
```

#### ✅ CORRECT (Strict Assertion Pattern):
```javascript
// DO: Explicit assertions that fail loudly on defect
const termPlan = page.locator('[data-testid="plan-term-pass-349"]');
await expect(termPlan).toBeVisible({ timeout: 10000 });
await termPlan.click();

const popiaCheckbox = page.locator('[data-testid="checkbox-popia-consent"]');
await expect(popiaCheckbox).toBeVisible({ timeout: 10000 });
await expect(popiaCheckbox).not.toBeChecked();
await popiaCheckbox.check();
await expect(popiaCheckbox).toBeChecked();
```

---

### Comparison 3: Authenticating Administrative Stakeholders

#### ❌ WRONG (Mock URL Parameter Infiltration):
```javascript
// DON'T: Spoofing admin privileges with query parameters
await page.goto('http://localhost:5173/?persona=admin');
// This bypasses Firebase Auth, fails token verification for secure endpoints,
// and contaminates the header with studentStore mock profiles (e.g. Nqobile Dlamini).
```

#### ✅ CORRECT (Authentic Role Authentication):
```javascript
// DO: Sign in through the genuine authentication gate with verified credentials
await page.goto('http://localhost:5173/');
const signInBtn = page.locator('[data-testid="btn-landing-signin"]');
await expect(signInBtn).toBeVisible({ timeout: 10000 });
await signInBtn.click();

await page.locator('[data-testid="input-signin-email"]').fill(adminEmail);
await page.locator('[data-testid="input-signin-password"]').fill(adminPassword);
await page.locator('[data-testid="btn-auth-submit"]').click();

// Assert that the administrative interface loads with authentic user identity
await expect(page.locator('[data-testid="tab-admin-payments"]')).toBeVisible({ timeout: 15000 });
await expect(page.locator('[data-testid="btn-user-profile"]')).toBeVisible();
```

---

## 4. Mechanical Audit Standard (`scripts/audit_e2e_specs.py`)

To ensure that no Hollywood engineering patterns can be introduced into the repository, every E2E specification is audited mechanically by `scripts/audit_e2e_specs.py`.

### Audited Rules:
| Check Code | Rule Description | Severity |
| :--- | :--- | :--- |
| **AUD-01** | **No Silent Skips:** Detects `if (await ...isVisible())`, `if (await ...count() > 0)`, or ternary wrappers on locators. | **FATAL** |
| **AUD-02** | **No Admin Query Spoofing:** Detects `?persona=admin` or `?persona=super_admin` in `goto()` or URL strings. | **FATAL** |
| **AUD-03** | **No Mid-Test Backdoor Mutations:** Detects calls to `approveTestPayment()` or direct Firestore mutations outside pre-flight setup. | **FATAL** |
| **AUD-04** | **No Phantom Selectors:** Extracts all `[data-testid="..."]` locators from the spec and verifies that every test ID exists in `src/`. | **FATAL** |
| **AUD-05** | **Explicit Assertion Requirement:** Ensures that interaction steps (`click`, `fill`, `selectOption`) are preceded by explicit `expect(...).toBeVisible()` or `expect(...).toBeEnabled()`. | **WARNING** |

### Running the Audit:
```bash
# Audit all E2E specifications
python scripts/audit_e2e_specs.py

# Audit a specific specification
python scripts/audit_e2e_specs.py --file e2e/set1_interactive_side_by_side.spec.js
```

A non-zero exit code halts the workflow and blocks completion.

---

## 5. Execution Runbook & Verification Workflow

1. **Step 1 — Source-Code Grounding:** Before writing test steps, open the relevant React components in `src/` and verify the exact `data-testid` attributes and DOM structures.
2. **Step 2 — Pre-Flight Clean Slate:** Use targeted purge helpers (`purgeTestUser.js`) before launching browser contexts to ensure no stale account state pollutes the test.
3. **Step 3 — Write Explicit Steps:** Author test steps with explicit assertions (`toBeVisible`, `toBeEnabled`). Avoid conditional branches or empty catch blocks.
4. **Step 4 — Run the Mechanical Linter:** Execute `python scripts/audit_e2e_specs.py` and confirm 0 violations.
5. **Step 5 — Run Live Playwright Execution:** Execute the test suite in headed mode against the local dev server (`http://localhost:5173`).
6. **Step 6 — Verify Real Database & UI State:** Confirm that data transitions (e.g. payment approved, class enrolled, diagnostic calibrated) occurred in the live application.
