# Autonomous Mock User Autopilot Engine — Master Architecture & Execution Plan (v2.0.0)

> **Note:** This is the identical plan document for the Autonomous Mock User Autopilot Engine. See also [`autonomous_agent_test_plan.md`](file:///c:/Users/princ/fundile-tlassistant-vite/autonomous_agent_test_plan.md).

**Document Version:** 2.0.0 (Post-Opus Architectural Synthesis)  
**Execution Driver:** Playwright Headed Runner with Injected Gliding Cursor & HUD Overlay (`e2e/`)  
**Target Environment:** Firebase Local Emulator Suite / Staging Environment (Zero Production Pollution)  
**Curriculum Scope:** ALL 9 CAPS Subjects (Grades 7–12), with Dedicated Calibration Anchors in Euclidean Geometry, Grade 7 Number Patterns, and Grade 7 Long Division  

---

## 1. Executive Summary: The Opus Synthesis

Following our rigorous architectural audit and critique, the plan has evolved from an internal in-page dispatcher (Option A) into a **Playwright-Headed Visual Autopilot Engine**.

### Why This Architecture Wins
- **You Still Watch the Entire Run Visually**: A visible Google Chrome window launches on your desktop. Playwright runs in `slowMo: 600` mode with an injected virtual cursor (`🖱️`) glides smoothly along cubic-bezier paths and a top glassmorphism HUD narration bar.
- **Your Computer Mouse is Never Hijacked**: Playwright controls the browser via the Chrome DevTools Protocol (CDP). You can freely use your physical mouse, type in other apps, or take over the browser window at will.
- **True Multi-User Concurrency (Side-by-Side Windows)**:
  - **Window 1 (Left)**: Independent learner Lesedi Khumalo signs up and uploads her Access Bank POP receipt.
  - **Window 2 (Right)**: Super Admin Mr. Pillay's dashboard receives the real-time Firestore record and clicks "Approve".
  - You literally watch Lesedi's paywall drop on the left the second the Admin approves it on the right!
- **Authentic Mobile WebAPK Emulation**:
  - Ayanda Ndlovu’s Grade 7 session runs in a native Playwright mobile context (`devices['Pixel 7']`) with true touch events (`TouchEvent`), genuine device pixel ratio (`DPR: 2.625`), and accurate Android viewport heights.
- **Trusted Events & Clean Production Bundle**:
  - File picker uploads (`setInputFiles`) and clipboard actions are 100% native (`isTrusted: true`).
  - Zero test scripts or payment approval backdoors are shipped inside the production web app; all test automation lives in `/e2e`.

---

## 2. Environment & Data Isolation: Zero Production Contamination

### 2.1 The Problem With Testing in Production
Running mock sessions with synthetic learner profiles in production pollutes:
1. Production Firebase Authentication with fake accounts.
2. The Super Admin `pending_payments` queue with fabricated banking slips.
3. Class analytics and Annual Teaching Plan (ATP) mastery reports.
4. Compliance with South Africa's **POPIA Section 35** regarding minors' personal data.

### 2.2 The Isolation Architecture
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                          FIREBASE LOCAL EMULATOR SUITE                                 │
│  • Auth Emulator (localhost:9099): Pre-seeded with Lesedi, Admin, Mrs Khumalo, Ayanda  │
│  • Firestore Emulator (localhost:8080): Isolated test collections                      │
│  • Storage Emulator (localhost:9199): Stores synthetic PDF POP binaries                │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                            │
                                            ▼
                    All Test Documents Tagged With Strict Metadata:
                    {
                      isSynthetic: true,
                      testRunId: "autopilot-run-20261009-1430",
                      seededBy: "playwright-autopilot"
                    }
```
*Note: A dedicated staging Firebase project (`fundile-staging`) may be used when testing multi-device physical handsets over LAN.*

---

## 3. The 5 Embodied Synthetic Personas & Behavioral Error Policies

Unlike naive test scripts that always answer 100% correctly, our embodied personas carry **Behavioral Error Policies** keyed to curriculum `misconception_tags`. This exercises Fundile’s core differentiators: **3-Tier Pre-baked Hints**, the **Procedure Tracker**, and **Adaptive Prerequisite Regression**.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   THE 5 EMBODIED PERSONAS                                        │
├─────────────────────────┬──────────────────────────┬───────────────────────┬─────────────────────┤
│ Persona Name            │ Role & Phase             │ Device & Profile      │ Behavioral Policy   │
├─────────────────────────┼──────────────────────────┼───────────────────────┼─────────────────────┤
│ 1. Lesedi Khumalo       │ Independent Learner      │ Laptop (1366×768)     │ High Accuracy (92%) │
│                         │ Grade 10 FET             │ Self-paced homeschool │ Requests Tier 1 hint│
├─────────────────────────┼──────────────────────────┼───────────────────────┼─────────────────────┤
│ 2. Ayanda Ndlovu        │ School Learner (Westville│ Pixel 7 Mobile (Touch)│ Struggling (65%)    │
│                         │ Grade 7 Senior Phase     │ Prepaid MTN (<2MB)    │ Subtraction error in│
│                         │                          │                       │ division -> Tier 2  │
├─────────────────────────┼──────────────────────────┼───────────────────────┼─────────────────────┤
│ 3. Mrs. Patience Khumalo│ Lead Educator / HOD      │ Desktop PC (1080p)    │ Teacher Workflow    │
│                         │ Grades 7 & 10            │ School LAN            │ Dispatches micro-fix│
├─────────────────────────┼──────────────────────────┼───────────────────────┼─────────────────────┤
│ 4. Mr. Sipho Ndlovu     │ Parent / Guardian        │ Android Mobile        │ Guardian Workflow   │
│                         │ (Ayanda's Father)        │ Mobile Data           │ Reviews Sunday pulse│
├─────────────────────────┼──────────────────────────┼───────────────────────┼─────────────────────┤
│ 5. Mr. Vinay Pillay     │ Principal & Super Admin  │ Desktop PC (1080p)    │ Admin Workflow      │
│                         │ Westville High / Fundile │ School Office         │ Approves POP, SASAMS│
└─────────────────────────┴──────────────────────────┴───────────────────────┴─────────────────────┘
```

---

## 4. Test Oracles & The Anti-Fallback Invariant

### 4.1 The Fatal Fallback Masking Trap
In `LearnerAppContainer.jsx`, when `/api/generate` fails, the client quietly falls back to a local question bank (typically a quadratic factorisation MCQ). 
**Strict Rule:** If a generator times out or throws an unhandled 500 error, the autopilot **MUST FAIL IMMEDIATELY**.
```typescript
// Playwright Step Assertion Contract:
const questionSource = await page.getAttribute('[data-testid="question-surface"]', 'data-source');
expect(questionSource).not.toBe('fallback');
expect(questionSource).toBe('deterministic_generator');
```

### 4.2 Deterministic Seeds
To eliminate random answer mismatches, all automated runs pass an explicit `seed` parameter (e.g. `seed=42101`), ensuring that the generator emits a byte-identical question, answer, and canonical solution graph that matches the test runner's expected oracle.

---

## 5. Explicit Selector Contract (`data-testid`)

To ensure tests never break when styling or Tailwind utility classes change, all scripted elements require explicit `data-testid` attributes:

| Component | Target Element | Required `data-testid` |
| :--- | :--- | :--- |
| **LandingPage** | Sign Up CTA Button | `data-testid="btn-landing-signup"` |
| **AuthScreen** | Full Name Input | `data-testid="input-signup-name"` |
| **AuthScreen** | Email Input | `data-testid="input-signup-email"` |
| **AuthScreen** | Grade Select | `data-testid="select-signup-grade"` |
| **AuthScreen** | POPIA Consent Checkbox | `data-testid="checkbox-popia-consent"` |
| **AuthScreen** | Submit Signup Button | `data-testid="btn-auth-submit"` |
| **EftUploadModal**| Term Pass Radio (R349) | `data-testid="plan-term-pass-349"` |
| **EftUploadModal**| Copy Reference Button | `data-testid="btn-copy-bank-ref"` |
| **EftUploadModal**| Hidden File Input | `data-testid="input-file-pop"` |
| **EftUploadModal**| Submit POP Button | `data-testid="btn-submit-pop"` |
| **AdminView** | Pending Payments Tab | `data-testid="tab-admin-payments"` |
| **AdminForms** | Approve 90 Days Button | `data-testid="btn-approve-payment-90d"` |
| **Workspace** | Question Problem Surface | `data-testid="question-surface"` |
| **Workspace** | Check Answer Button | `data-testid="btn-check-answer"` |
| **Workspace** | Tier 1 / 2 / 3 Hint Pills| `data-testid="btn-hint-tier-1"`, `tier-2` |
| **TodaysDesk** | Upcoming Task Card | `data-testid="card-task-upcoming"` |
| **JoinClass** | Class Join Code Input | `data-testid="input-join-class-code"` |

---

## 6. The Two Core Enrollment Pipelines

### Pipeline A: The Independent Learner Journey (Lesedi Khumalo)
1. **Window 1 (Lesedi - Laptop Viewport 1366×768)**:
   - Navigates to `http://localhost:5173`.
   - Clicks `[data-testid="btn-landing-signup"]`.
   - Fills Lesedi Khumalo, Grade 10 FET, POPIA consent.
   - Enters `EftUploadModal`, selects **School Term Pass (R349)**.
   - Attaches authentic Access Bank PDF generated in memory (`tests/fixtures/sample_pop.pdf`).
   - Clicks `[data-testid="btn-submit-pop"]`.
   - **Expectation**: Firestore receives `pending_payments` doc with `status: "pending"`, `amount: 349`.
2. **Window 2 (Mr. Pillay - Super Admin Viewport 1920×1080)**:
   - Opens `AdminView` -> `PendingPayments`.
   - Sees Lesedi's payment appear via real-time Firestore listener.
   - Clicks `[data-testid="btn-approve-payment-90d"]`.
   - **Expectation**: Payment status becomes `"approved"`, user document subscription becomes `"active"`.
3. **Window 1 (Lesedi's Workspace Unlocks)**:
   - Real-time subscription listener detects active status -> Paywall dismisses.
   - Navigates to **Mathematics -> Euclidean Geometry**.
   - Solves Grade 10 Geometry figure (`diagram_select` interaction).
   - **Expectation**: Result marks awarded, MasteryDial updates, question source is NOT fallback.

### Pipeline B: The School Batch Enrollment Journey (Ayanda Ndlovu)
1. **Window 3 (Ayanda - Pixel 7 Mobile Viewport 390×844)**:
   - Launches mobile WebAPK interface.
   - Enters class code `MTH701` -> instantly enrolled via school roster.
   - Today's Desk reveals homework assigned by Mrs. Khumalo.
   - Solves **Grade 7 Number Patterns** ($T_n = 4n - 1$).
   - Solves **Grade 7 Long Division** ($845 \div 5 = 169$ on the arithmetic grid).
   - Simulates a subtraction error: verifies Tier 2 directional hint appears, corrects answer, passes.
2. **Window 4 (Mr. Sipho Ndlovu - Parent Mobile Viewport)**:
   - Enters ephemeral 15-minute handshake code (`PAR-7892`).
   - Verifies Sunday Academic Pulse displays:
     - Ayanda's focus time & accuracy.
     - Repaired misconception: `subtraction_borrowing_inversion`.
     - Mobile data meter: confirms **1.4 MB** consumption.

---

## 7. Phased Implementation Roadmap

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                             PHASED ROADMAP OVERVIEW                                    │
│                                                                                        │
│  PHASE 1: Core Headed Runner & Pipeline A (Ready Now)                                  │
│  ────────────────────────────────────────────────────                                  │
│  1. Author Playwright headed runner with injected gliding cursor & HUD overlay         │
│  2. Add `data-testid` contracts to Landing, Auth, EFT Modal, and Admin Panels           │
│  3. Reconcile `EftUploadModal` pricing: add R349 Term Pass option                      │
│  4. Add real-time user subscription listener (`onSnapshot`) to `LearnerAppContainer`   │
│  5. Execute Pipeline A (Lesedi + Admin side-by-side run) with zero silent fallbacks    │
│                                                                                        │
│  PHASE 2: Curriculum & Modality Engineering                                            │
│  ─────────────────────────────────────────                                             │
│  1. Author `caps-ai-backend/app/utils/grade7_patterns_generator.py`                    │
│  2. Author Grade 7 Long Division generator & Columnar Arithmetic Grid Modality         │
│  3. Wire live Firestore queries into `ParentDashboard` and `SchoolAdminView`           │
│                                                                                        │
│  PHASE 3: Full Multi-Persona Integrated Suite                                          │
│  ───────────────────────────────────────────                                           │
│  1. Execute Pipeline B (Ayanda + Mrs Khumalo + Mr Ndlovu)                              │
│  2. Verify error injection, hint progression, and Sunday Pulse telemetry               │
│  3. Export automated HTML Run Report with screenshots and traces                       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
