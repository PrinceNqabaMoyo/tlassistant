# Phase 1 — Implementation Tracker

## Frontend — CDN Dependencies
- `[x]` **[MODIFY]** `index.html` — Added KaTeX CSS + JS CDN links (dormant until Pro activation)
- `[x]` **[MODIFY]** `index.html` — Added JSXGraph CSS + JS CDN links (dormant until Pro activation)

## Frontend — New React Components (All Dormant — NOT imported anywhere)
- `[x]` **[NEW]** `src/components/shared/KaTeXRenderer.jsx` — Renders LaTeX strings
- `[x]` **[NEW]** `src/components/shared/JSXGraphRenderer.jsx` — Renders interactive geometry
- `[x]` **[NEW]** `src/components/shared/RenderDispatcher.jsx` — Routes render payloads

## Backend — Email Notification (LIVE AND WORKING)
- `[x]` **[NEW]** `caps-ai-backend/app/services/email_service.py` — Resend API email sender
- `[x]` **[MODIFY]** `caps-ai-backend/app/api/payments/routes.py` — Triggers email after POP upload
- `[x]` **[MODIFY]** `caps-ai-backend/Dockerfile` — Logging enhancements only

## Backend — CAPS Wiki Knowledge Base (COMPLETED)
- `[x]` `caps-ai-backend/caps-wiki/mathematics/grade-7/fractions.md`
- `[x]` `caps-ai-backend/caps-wiki/mathematics/grade-7/geometry.md`
- `[x]` `caps-ai-backend/caps-wiki/mathematics/grade-10/algebra.md`
- `[x]` `caps-ai-backend/caps-wiki/mathematics/grade-10/financial-maths.md`
- `[x]` `caps-ai-backend/caps-wiki/accounting/grade-10/cash-receipts-journal.md`
- `[x]` `caps-ai-backend/caps-wiki/accounting/grade-10/general-ledger.md`

## Backend — New Agent Tools (COMPLETED)
- `[x]` `agent_service.py` — Add `get_curriculum_page` tool
- `[x]` `agent_service.py` — Add `render_visual` tool
- `[x]` `agent_service.py` — Register both new tools

## Subscription Tier Gating (COMPLETED)
- `[x]` Frontend Pro/Standard conditional rendering
- `[x]` Backend Pro/Standard tool selection

## Verification (COMPLETED)
- `[x]` Frontend builds cleanly (`npm run build`)
- `[x]` Backend imports cleanly

---

# Phase 2 — Science & Visuals (COMPLETED)

## Frontend — CDN Dependencies
- `[x]` **[MODIFY]** `index.html` — Added Leaflet.js CSS + JS CDN links
- `[x]` **[MODIFY]** `index.html` — Added RDKit.js CDN link
- `[x]` **[MODIFY]** `index.html` — Added Plotly.js CDN link
- `[x]` **[MODIFY]** `index.html` — Added Mermaid.js CDN link

## Frontend — New React Components
- `[x]` **[NEW]** `src/components/science/ChemistryRenderer.jsx` — Renders molecules from SMILES via RDKit
- `[x]` **[NEW]** `src/components/science/GeographyMapRenderer.jsx` — Renders interactive maps via Leaflet.js
- `[x]` **[NEW]** `src/components/science/PlotlyRenderer.jsx` — Renders interactive graphs via Plotly.js
- `[x]` **[NEW]** `src/components/science/MermaidRenderer.jsx` — Renders timelines/diagrams via Mermaid.js
- `[x]` **[NEW]** `src/components/science/SVGRenderer.jsx` — Renders raw SVG strings
- `[x]` **[NEW]** `src/components/science/ChemistryInput.jsx` — Student chemistry input (SMILES fallback for Ketcher)
- `[x]` **[MODIFY]** `src/components/shared/RenderDispatcher.jsx` — Added cases for `chemistry`, `geography`, `graph`, `timeline`, `diagram`

## Backend — CAPS Wiki Expansion
- `[x]` **[NEW]** `caps-ai-backend/caps-wiki/physical-sciences/grade-10/chemical-bonding.md`
- `[x]` **[NEW]** `caps-ai-backend/caps-wiki/geography/grade-10/mapwork.md`
- `[x]` **[MODIFY]** `caps-ai-backend/app/services/agent_service.py` — Updated `render_visual` docstring to include `chemistry` and `geography` types

## Verification (COMPLETED)
- `[x]` Frontend builds cleanly (`npm run build`)
- `[x]` Backend imports cleanly (`python -m py_compile`)

---

# Step 2 — Chat Session Management & "Explain My Mistake" (COMPLETED)

## Frontend — "Explain My Mistake" Feature
- `[x]` **[MODIFY]** `src/components/workspace/Workspace.jsx` — Added "Explain my mistake" button to incorrect feedback blocks
- `[x]` **[MODIFY]** `src/App.jsx` — Added `handleExplainMistake` function that initializes a freeform chat session with problem context
- `[x]` **[MODIFY]** `src/app/render/renderStudentContent.jsx` — Wired `handleExplainMistake` through to `Workspace`

## Frontend — Chat Session Context (Implemented via existing `useFreeformProblemFlow`)
- `[x]` `addQuestionToChat` / `updateAnswerInChat` already handle chat history arrays
- `[x]` Context window management (truncation to last 10 messages) already implemented in `useFreeformProblemFlow.js`
- `[x]` Session linking via `threadId` already implemented

## Verification (COMPLETED)
- `[x]` Frontend builds cleanly (`npm run build`)

---

# Phase 3 — Personalisation (Pro) (COMPLETED)

## Backend — Firestore Initialization
- `[x]` **[MODIFY]** `caps-ai-backend/app/__init__.py` — Added Firebase Admin SDK / Firestore initialization and wired up LLM Rate Limiter

## Backend — New Agent Tool
- `[x]` **[MODIFY]** `caps-ai-backend/app/services/agent_service.py` — Added `get_student_history` tool that reads `struggling_problems` and `solved_freeform_problems` from Firestore
- `[x]` **[MODIFY]** `caps-ai-backend/app/services/agent_service.py` — Updated `STUDENT_PROMPT` to instruct the agent to use `get_student_history` for adaptive tutoring
- `[x]` **[MODIFY]** `caps-ai-backend/app/services/agent_service.py` — `initialize_agent` now accepts optional `firestore_db` parameter

## Backend — API Endpoint Update
- `[x]` **[MODIFY]** `caps-ai-backend/app/api/agent.py` — Extracts `user_id` from request and passes it to agent executor

## Frontend — Identity & Tier Propagation
- `[x]` **[MODIFY]** `src/App.jsx` — `getAgentResponse` now sends `subscription` (tier) and `user_id` with every agent request

## Backend — CAPS Wiki Humanities Expansion
- `[x]` **[NEW]** `caps-ai-backend/caps-wiki/history/grade-10/the-cold-war.md`
- `[x]` **[NEW]** `caps-ai-backend/caps-wiki/economics/grade-10/economic-systems.md`

## Verification (COMPLETED)
- `[x]` Frontend builds cleanly (`npm run build`)
- `[x]` Backend imports cleanly (`python -m py_compile`)

---

---

# Phase 4 — Teacher & Admin Modes (IN PROGRESS)

## Frontend — Teacher Mode Gating
- `[x]` **[MODIFY]** `src/components/teacher/TeacherView.jsx` — Added `canAccessTeacherMode` gate: shows `FeatureGatePanel` with "Coming soon / Not yet available in South Africa" for non-owner/superadmin users; Owner/SuperAdmin bypasses gate and sees full Teacher UI

## Frontend — Teacher Mode UI (Owner/SuperAdmin Bypass)
- `[x]` **[NEW]** `src/components/teacher/ClassManager.jsx` — Create classes with subject/grade selection (up to 3 each), enroll Fundile-subscribed students, delete classes
- `[x]` **[NEW]** `src/components/teacher/HomeworkManager.jsx` — Create and send homework to classes, with mark-visibility toggle (show immediately or hide until teacher releases)
- `[x]` **[NEW]** `src/components/teacher/AssessmentManager.jsx` — Create timed assessments sent to classes, with mark-visibility toggle
- `[x]` **[MODIFY]** `src/components/forms/TeacherForms.jsx` — Updated `TeacherDashboard` with Classes, Homework, and Assessments cards
- `[x]` **[MODIFY]** `src/components/teacher/TeacherView.jsx` — Added routing for `classManagement`, `homework`, `assessments`

## Frontend — School Admin Mode
- `[x]` **[NEW]** `src/components/admin/SchoolAdminView.jsx` — Gated UI with placeholders for Teaching Staff, Class Oversight, Marks & Reports, Student Enrollment, Subscription Tracking, School Settings
- `[x]` **[MODIFY]** `src/components/forms/AdminForms.jsx` — Added "School Admin" dashboard card (Owner/SuperAdmin only)
- `[x]` **[MODIFY]** `src/components/admin/AdminView.jsx` — Added `schoolAdmin` view case routing to `SchoolAdminView`
- `[x]` **[MODIFY]** `src/components/admin/index.js` — Exported `SchoolAdminView`

## Frontend — App Shell & Routing
- `[x]` **[MODIFY]** `src/hooks/useTeacherAdminViews.js` — Added `schoolAdminView` / `setSchoolAdminView` state
- `[x]` **[MODIFY]** `src/App.jsx` — Wired `schoolAdminView` / `setSchoolAdminView` into `roleState`
- `[x]` **[MODIFY]** `src/app/render/renderRoleContent.jsx` — Destructured `schoolAdminView` / `setSchoolAdminView` from `roleState`

## Backend — Teacher API
- `[x]` **[MODIFY]** `caps-ai-backend/app/api/teacher.py` — Added endpoints:
  - `GET /api/teacher/tier-status/<teacher_id>` — Free-tier eligibility (average 15+ subscribed students per class)
  - `GET /api/teacher/classes/<teacher_id>` — List teacher classes
  - `GET /api/teacher/homework/<teacher_id>` — List teacher homework
  - `GET /api/teacher/assessments/<teacher_id>` — List teacher assessments

## Backend — School Admin API
- `[x]` **[NEW]** `caps-ai-backend/app/api/school_admin.py` — Blueprint with endpoints:
  - `GET /api/school-admin/teachers` — List all teachers
  - `GET /api/school-admin/classes` — Aggregate all classes
  - `GET /api/school-admin/marks-summary` — Marks reporting placeholder
  - `GET /api/school-admin/subscription-check` — Active subscription counts
- `[x]` **[MODIFY]** `caps-ai-backend/app/__init__.py` — Registered `school_admin_bp` at `/api/school-admin`

## Verification (COMPLETED)
- `[x]` Frontend builds cleanly (`npm run build`)
- `[x]` Backend imports cleanly (`python -m py_compile`)

---

## Next Steps
- Phase 4 UI is scaffolded and gated. When the feature is ready for public rollout:
  1. Remove the `canAccessTeacherMode` gate from `TeacherView.jsx`
  2. Implement teacher signup flow with subject/grade selection
  3. Wire School Admin components to live Firestore data
  4. Connect the frontend to the new backend API endpoints for class/homework/assessment CRUD
  5. Implement the 15+ students free-tier check in the frontend billing flow
