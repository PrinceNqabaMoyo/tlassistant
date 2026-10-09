# Critique — Autonomous Mock User Autopilot Plan (v1.1.0)

**Reviewed:** `autonomous_agent_test_plan.md` and the claims made in chat ("real clicks", "indistinguishable from a human", "not a simulation").
**Method:** Every claim was checked against the current code (grep results are cited).

---

## Verdict

The goal is right: watch embodied personas run real flows end-to-end before production. **The plan cannot deliver that as written.** It has three structural problems:

1. **It assumes features exist that don't.** Large parts of Pipeline B would test static UI, not persisted behaviour.
2. **It describes actions, not tests.** No step has an assertion, so a run can "succeed" while the system is broken.
3. **The in-page engine (Option A) can't do several things the plan requires:** switch Firebase identities, handle file pickers or clipboard, emulate a real phone, run two users at once.

All three are fixable. Fixing #3 means changing the driver, not the vision.

---

## 1. Claims that conflict with the codebase

| Plan claim | Reality in code | Impact |
|---|---|---|
| Lesedi selects **"School Term Pass R349"** | `EftUploadModal.jsx` only offers **R150/month** and **R1600/year** (no 349 / term option) | Step 3 of Pipeline A targets a button that doesn't exist. Pricing is also inconsistent with the marketing (R149/R349/R999). That is a real bug the plan should *flag*, not assume away. |
| Selectors `#btn-landing-signup`, `#btn-submit-pop`, `#btn-approve-payment-90d` | **0** matches. **0** `data-testid` attributes across all `src/**/*.jsx` | Every step needs a selector contract first. Otherwise the engine will match on text or classes and break on every UI tweak. |
| Context switch to Super Admin "Mr. Pillay" | `PersonaSwitcherModal.jsx` has **0** auth calls. Personas come from client-side mock arrays (`src/data/mock/`) and are not Firebase users | `PendingPayments.handleApprove` reads `users/{uid}` from Firestore and throws *"User profile not found"* for a mock persona. Approval can only work with a **real authenticated admin**. |
| "Paywall drops automatically" after approval | **0** `onSnapshot(doc(...'users'))` listeners found | The learner's session won't notice the approval without a reload or re-fetch. Either the plan or the app must change. That's a good finding, but it needs an explicit assertion. |
| Parent sees Sunday Pulse / data meter for Ayanda | `ParentDashboard.jsx` has **0** Firestore reads | The parent step would "pass" on hardcoded preview data. That is a simulation, which you explicitly don't want. |
| Principal reviews ATP heatmap / SASAMS export | `SchoolAdminView.jsx` has **0** Firestore reads | Same problem: static data. |
| Teacher "Dispatch Homework" pushes to Ayanda's Today's Desk | `TeacherDashboard.jsx` has 3 Firestore refs (partial). `JoinClassModal.jsx` and `TeacherRostersTab.jsx` exist | Needs verification that an assignment written by the teacher is actually what `TodaysDeskView` reads. Today's Desk cards were previously hardcoded. |
| 15-min parent handshake code | `LinkGuardianModal.jsx` exists | Likely real. Verify the backend/Firestore side before scripting it. |
| Grade 7 Number Patterns generator | Generators exist for Gr 8, 9, 10, 11, 12 patterns. **No Grade 7** | A mandatory topic has no generator. This needs authoring (generator_architect plus math specialist), not just a test. |
| Long Division marked by the Procedure Tracker | No long-division generator. The tracker checks **SymPy equivalence per line**, and lines like `8 ÷ 5 = 1 rem 3` / "bring down 4" are not SymPy-parseable | A mandatory topic needs a new **algorithmic-procedure modality** (digit-grid long division with per-step checks). This is real feature work. |
| Geometry question `[R1]` reason mark | Existing diagram support is `diagram_select` (edge click). There's no reason-matching marker | Either test `diagram_select` or build reason marking. The current plan tests a capability that doesn't exist. |
| Backend failures surface as errors | `LearnerAppContainer.fetchQuestion` **silently falls back** to `authenticDiagnosticBank` on any non-200 or network error. The maths fallback is the trinomial MCQ | **Critical.** If `/api/generate` fails, the "Geometry" step quietly renders a factorisation MCQ and the run looks green. The autopilot must treat fallback as a **failure**. |
| Production test data | No emulator wiring (`connectFirestoreEmulator`: 0) and no synthetic tagging (`isTestUser`/`testRunId`: 0) | Runs would write fake learners, POPs and Auth accounts into **production**. That pollutes admin queues and analytics and raises POPIA questions about fabricated minors' records. |

---

## 2. Technical errors in the "it's real, not simulated" argument

The earlier chat answer overstated what in-page scripting can do. Corrections:

1. **"Indistinguishable from a hardware click" is false.** Script-dispatched events have `event.isTrusted === false`. React handlers usually still fire, but **gesture-gated browser APIs refuse untrusted events**:
   - `navigator.clipboard.writeText` ("Copy Bank Reference") → will reject or require permission.
   - Clicking `<input type=file>` → cannot open the OS file picker. You must inject the file via `DataTransfer` and fire `change`. That works, but it is not what a human does, and it skips the picker path entirely.
   - `getUserMedia` (profile photo), fullscreen, orientation lock, PWA install prompt → can't be triggered.
2. **Typing into React-controlled inputs** needs the native value setter (`Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set`) followed by an `input` event. "Set value + dispatch change" as written will leave React state empty, so forms will submit blank.
3. **One tab means one Firebase identity.** Pipeline A needs Lesedi → Admin → Lesedi. In one page that means sign out and sign in with *stored credentials*. In practice the engine would have to hold a super-admin password inside the client bundle, which is a serious security hole if it ever ships.
4. **Mobile cannot be emulated from inside the page.** A script can't change the viewport, `devicePixelRatio`, user agent, touch capability or orientation. `MobileWebApkView` would only render if the window is narrowed by hand or the app is put in an iframe. Even then you get mouse events, not touch, so 44 px targets, sticky tucking and pinned rails under a real mobile viewport aren't really exercised.
5. **Shipping risk.** An in-app engine that can upload POPs and approve payments must never reach the production bundle. The main chunk is already **4.5 MB**. The plan has no build gate.

---

## 3. The plan tests happy paths only

- **Every persona answers correctly.** Ayanda's profile says he "skips the subtraction step", but the script has him get it right. An embodied persona should **behave like their profile**: a seeded error policy keyed to the generator's `misconception_tags` (e.g. a 30% chance of `subtraction_borrowing_inversion`). Only then do you exercise:
  - hints
  - error localisation in the Procedure Tracker
  - consequential marking
  - the "fail twice → elementary mode" regression
  - triage tags
  - the Parent pulse that reports repaired misconceptions

  These are Fundile's differentiators, and the current plan never touches them.
- **No negative paths:** wrong file type for the POP, file over 10 MB, admin rejects the POP, expired guardian code, wrong class code, backend down, offline mid-question, resume after a refresh (the session-resumption engine you just built goes untested).

---

## 4. The plan has no oracle, so it isn't a test yet

- **Steps have no expected outcomes.** Each step needs an `expect` block:
  - DOM state
  - network call and status
  - Firestore document and fields
  - **no fallback used**
  - a timeout
- **The engine can't know the right answer.** `fetchQuestion` uses `seed=Date.now()`, so the autopilot can't know the correct answer for a random question. Options:
  - (a) fixed seeds per step, with expected answers pre-computed by the generator itself in a test fixture, or
  - (b) a dev-only `/api/test/oracle` endpoint.

  Never read answers from the client payload: the security audit already flagged answer leakage.
- **Section 5.4 ("any subject, any topic on demand") overpromises.** Without an oracle the autopilot can type *something*, not *the right thing*. And driving 9 subjects × 6 grades × 4 terms at human cursor speed takes hours, which contradicts "least shortest path". Coverage breadth belongs in the **existing headless Monte Carlo generator auditor** (`npm run audit:full`). The visual persona runs should cover **flows**, plus one representative question per **modality** (ledger, maths steps, diagram, rubric, MCQ).
- **No run report.** You asked to *see* how the system reacts. A watched run is not evidence. Each run needs persistent output:
  - a JSON step log
  - a screenshot per step
  - the network log
  - a pass/fail summary visible in the Super Admin dashboard

---

## 5. Recommended corrections

### 5.1 Change the driver (strongly recommended)
Use **Playwright in headed mode with `slowMo`, plus an injected cursor overlay and HUD** (`page.addInitScript`). It keeps everything you liked about Option A and removes the blockers:

| Need | Option A (in-page) | Playwright headed + overlay |
|---|---|---|
| Watch a moving pointer + HUD narration | ✅ | ✅ (same overlay, injected) |
| Doesn't hijack your OS mouse | ✅ | ✅ (drives its own Chrome window via CDP) |
| Trusted events (`isTrusted: true`) | ❌ | ✅ (CDP input is trusted) |
| File picker, clipboard permissions | ❌ / workaround | ✅ `setInputFiles`, `grantPermissions` |
| Lesedi and Admin **simultaneously**, separate real auth | ❌ | ✅ two browser contexts side by side |
| Real mobile emulation (viewport, touch, DPR, UA, landscape) | ❌ | ✅ `devices['Pixel 7']`, `hasTouch`, `isMobile` |
| Network / Firestore assertions, screenshots, video, trace viewer | ❌ / manual | ✅ built in |
| Zero code shipped in the production bundle | ❌ risk | ✅ lives in `/e2e`, outside `src/` |
| Re-runnable in CI before every deploy | ❌ | ✅ |

You'd run it with `npm run e2e:watch` and watch real Chrome windows: a laptop-sized one for Lesedi and the Admin, and a Pixel-sized one for Ayanda and his dad.

### 5.2 Isolate data
- **Default:** Firebase Emulator Suite (Auth, Firestore, Storage) with seeded real users (Lesedi, Admin with custom claims, Mrs Khumalo, Ayanda, Mr Ndlovu). Their records are **real in that environment** and visible in the Super Admin dashboard pointed at the emulator.
- **Optional staging run** against a dedicated staging Firebase project. Never run against production. Every synthetic doc gets `isSynthetic: true` and `testRunId`, plus a cleanup script.

### 5.3 Fix the plan's content
1. Add a **`data-testid` contract** for every scripted control (cognitive_ui_engineer).
2. Reconcile **pricing**: one source of truth for R149/R349/R999 vs R150/R1600 across the EFT modal, landing page, admin approval durations and marketing.
3. Add a **subscription listener**, or make "reload required after approval" an explicit, tested behaviour.
4. Make `fetchQuestion` **report fallback** with `question.source = 'fallback'` and fail the run on it.
5. Author the **Grade 7 patterns** generator and a **long-division procedure modality** before scripting those runs (generator_architect + math_sciences_specialist).
6. Choose the geometry interaction that exists (`diagram_select`), or schedule reason marking as a feature.
7. Give each persona a **behaviour profile**: accuracy, error policy by misconception tag, hint-seeking tendency, typing speed, device. Run each persona twice: once mastering, once struggling.
8. Add **negative-path** and **resume-after-refresh** scenarios.
9. Wire Pipeline B steps to Firestore only after **Parent** and **School Admin** dashboards read real data. Until then, mark those steps `UI-only (static data)` in the HUD so nothing pretends to be real.

### 5.4 Revised structure
```
Layer 1  Headless coverage sweep (exists: npm run audit:full)
         all generators × grades × seeds; oracle = generator's own answers

Layer 2  Visual persona flows (Playwright headed + cursor/HUD overlay, emulator)
         Desktop track:  D1 Lesedi signup→POP→(Admin context approves)→resume→geometry
                         D2 Mrs Khumalo roster→assign→misconception dispatch
                         D3 Admin/Principal queue, reject path, SASAMS export
         Mobile track:   M1 Ayanda join MTH701→desk→patterns (struggling profile)
                         M2 Ayanda long division→hint tiers→regression→resume after refresh
                         M3 Mr Ndlovu guardian code→pulse reflects M1/M2 real data
         every step: action + expect{dom, network, firestore, noFallback} + timeout

Layer 3  Run report → JSON + screenshots + trace, summary card in Super Admin
```

---

## 6. Questions for you

1. **Driver:** Switch to Playwright headed with the cursor and HUD overlay (recommended), or keep Option A and accept its limits (no simultaneous users, no real mobile, workarounds for files and clipboard)?
2. **Environment:** Firebase Emulator (recommended), a dedicated staging project, or tagged production (not recommended)?
3. **Scope order:** Run the flows that are real today first (D1, D2, M1-join, guardian link) while the Grade 7 patterns generator, the long-division modality and the real-data Parent/Admin dashboards are built? Or build those first so the first run covers everything?
