# Response to "Towards a Complete App"

> This document is a section-by-section response to `Towards a complete app.md`, covering architecture decisions, feasibility, and implementation recommendations.

---

## 1. Session .md Files — The User Record System

### What the document proposes
Each session generates a single `.md` file, headed by subject/topic/subskill/adaptive-progression-levels. The file contains: generated question, expected answer, and student input. The file should be LLM-readable so an agent can use it to build a student system profile.

### My assessment: Strong idea, with refinements needed

**What works:**
- A per-session `.md` file is an excellent, portable, human-readable record. It survives database migrations, can be exported/emailed, and is directly consumable by an LLM agent.
- Having the expected answer in the same file as the student input creates a self-contained record — an agent can compare them without cross-referencing.

**Refinements I recommend:**

1. **Use YAML frontmatter for structured data, Markdown body for content.** The file should be both human-readable and machine-parseable. Frontmatter gives the agent structured fields (subject, topic, subskill, level, timestamp, session ID, user ID, score, procedure-tracking flags) without parsing prose. The body holds the question, expected answer, and student input in readable Markdown.

   ```markdown
   ---
   sessionId: "2025-01-15-acct-gr10-bank-recon-001"
   userId: "usr_abc123"
   subject: "Accounting"
   grade: "10"
   topic: "Bank reconciliation"
   subskill: "Identify outstanding cheques"
   adaptiveLevel: "scaffold"
   timestamp: "2025-01-15T14:32:00+02:00"
   score: 0.67
   procedureFlags: ["correct_opening_balance", "wrong_deduct_cheques", "omitted_outstanding_deposits"]
   duration: 842
   ---

   # Question
   [Generated question text here, including any tables in Markdown or CSV]

   # Expected Answer
   [Expected answer text here]

   # Student Input
   [Student's answer here, in the same format as the expected answer for easy comparison]
   ```

2. **Tables: use Markdown tables for simple, CSV for complex.** Accounting and EMS have nested columns (e.g., General Ledger with Date/Details/Folio/Debit/Credit). Markdown tables can't express nested headers well. For these, use a fenced CSV block with a schema comment:
   ```markdown
   ```csv
   # schema: date,details,folio,debit,credit
   2025-01-01,Bank,CB,5000,
   2025-01-03,Rent,CB,,2000
   ```
   ```
   This is both human-readable and trivially parseable by an agent.

3. **Store .md files in Supabase Storage (or filesystem) + index in Firestore.** The `.md` file is the source of truth, but querying across sessions ("show me all sessions where the user struggled with bank reconciliation") requires a database index. Store the file path + key metadata (subject, topic, score, date) in a Firestore collection for fast queries, and the `.md` file itself in Supabase Storage or a filesystem bucket.

---

## 2. Answer Types — Input Capture

### What the document proposes
Answers come in multiple formats: table inputs, selections, MCQ choices, word bank picks, column arrangements, word puzzles, mathematical workings, semantic discussions. All should be written under the question in the .md file.

### My assessment: Feasible, but needs a serialization schema

**The challenge:** Each answer type has a different structure. A table input is a 2D grid. A word bank pick is a set of tokens. A column arrangement is an ordered list. Semantic discussions are free text. Writing all of these into a single .md format requires a consistent serialization approach.

**Recommendation:** Define a JSON schema for each answer type, serialize to JSON in the .md file under a fenced code block, and also render a human-readable version.

```markdown
# Student Input

## Answer (table)
| Date | Details | Debit | Credit |
|------|---------|-------|--------|
| 01/01 | Bank | 5000 | |
| 03/01 | Rent | | 2000 |

<!-- machine-readable -->
```json
{
  "type": "table",
  "schema": ["date", "details", "debit", "credit"],
  "rows": [
    ["2025-01-01", "Bank", "5000", null],
    ["2025-01-03", "Rent", null, "2000"]
  ]
}
```
```

This dual format means:
- A human (teacher, parent, student) can read the Markdown table
- An agent can parse the JSON block for structured analysis
- The rendering is deterministic and lossless

**For semantic discussions** (essay-type answers), store as plain text with optional marking-point annotations:
```markdown
# Student Input

## Answer (semantic)
[Free text answer here...]

<!-- marking points hit -->
```json
{
  "type": "semantic",
  "markingPoints": [
    { "id": "mp1", "text": "Identifies the going concern concept", "hit": true },
    { "id": "mp2", "text": "Explains why assets are valued at cost", "hit": false }
  ]
}
```
```

---

## 3. Procedure Tracking in .md Files

### What the document asks
Should procedure tracking findings be recorded in the .md as well, for building a useful user system profile?

### My assessment: Yes, absolutely — this is the highest-value data for the profile

**Procedure tracking** (which I understand from `01_procedure_tracker_agent.md` to be the step-by-step method the student follows) is the single richest signal for diagnosing *where* a student's understanding breaks down. A final answer tells you *whether* they got it right; procedure tracking tells you *why* they got it wrong.

**Recommendation:** Add a `# Procedure Tracking` section to the .md file:

```markdown
# Procedure Tracking

## Steps
```json
[
  { "step": 1, "description": "Identify opening bank balance", "status": "correct", "duration": 12 },
  { "step": 2, "description": "Compare to bank statement", "status": "correct", "duration": 8 },
  { "step": 3, "description": "Deduct outstanding cheques", "status": "wrong", "error": "subtracted from wrong side", "duration": 45 },
  { "step": 4, "description": "Add outstanding deposits", "status": "omitted", "duration": 0 }
]
```

## Diagnosis
Student correctly identifies opening balance and comparison step but confuses which side to adjust for outstanding cheques. Outstanding deposits were omitted entirely — suggests incomplete understanding of the reconciliation procedure, not just a calculation error.
```

**Why this matters for the profile:** The agent can now say to the student: "You know the *what* of bank reconciliation, but you're confusing the *how* — specifically, which side to adjust for outstanding cheques. Let's practice that step." This is far more actionable than "You got 67% on bank reconciliation."

---

## 4. Student System Profile

### What the document proposes
The .md files are the data an agent uses to build and update a student's system profile — a record of weaknesses and strengths that helps the agent plot a path, advise the user, and write detailed reports to teachers or parents.

### My assessment: This is the core retention engine. Design it carefully.

**Architecture recommendation:**

```
Session .md files (raw data)
        │
        ▼
   Agent (LLM) reads .md files
        │
        ▼
   Student System Profile (structured, in Firestore)
        │
        ├── Strengths: [{ subject, topic, subskill, confidence, lastAssessed }]
        ├── Weaknesses: [{ subject, topic, subskill, errorPattern, occurrences, lastAssessed }]
        ├── Learning style signals: { prefersScaffold, rushesToAssessment, skipsFeedback, ... }
        ├── Progress trajectory: [{ date, overallMastery, subjects: {...} }]
        └── Recommendations: [{ priority, subject, topic, reason, suggestedAction }]
```

**Key design decisions:**

1. **The profile is a living document, not a static snapshot.** Every session updates it. The agent reads recent .md files, compares to the existing profile, and updates strengths/weaknesses/recommendations.

2. **Students do NOT see .md files.** The .md session files are internal data — the agent reads them, updates the profile, and delivers insights/recommendations to the student in plain language. The student experiences the agent as a conversation: "You're confusing which side to adjust for outstanding cheques — let's practice that." They never see raw YAML frontmatter, JSON procedure steps, or diagnosis blocks. This keeps the experience clean and human.

3. **Store the profile in Firestore** (not just as a .md file) because it needs to be queryable and updateable in real-time. The .md session files are the raw data; the profile is the derived, structured insight.

4. **Error patterns, not just scores.** The profile should track *what kind of errors* the student makes, not just how many. "Confuses debit/credit sides" is more useful than "got 3/10 on ledgers."

5. **Confidence intervals.** Don't claim mastery after one correct answer. Track confidence as a function of (correct/total attempts, recency, consistency across sessions). A student who gets bank reconciliation right once might have guessed; three correct in a row across two weeks is mastery.

6. **Reports to teachers/parents** are generated by the agent from the profile, not hand-written. The agent should be able to produce:
   - **Weekly parent report:** "This week, [student] practiced 4 sessions on Accounting. Strengths: identifying concepts. Focus area: bank reconciliation procedure — specifically outstanding cheques. Recommended: 2 more scaffold sessions on this subskill."
   - **Term teacher report:** Full breakdown by subject/topic/subskill with trajectory graph, class comparison (anonymized), and flagged students needing intervention.

---

## 5. Teacher Mode

### What the document proposes (extensive)
- Generate questions at subskill/topic/term level
- Editable questions + editable expected answers
- Semantic answers with editable marking points
- Highlight-to-create-marking-point
- Store teacher marking points, mark student work against them
- Assignments/tests/exams with immediate or teacher-review reveal
- Teacher-markable answers + editable auto-marking
- Printable PDF with cover page (school badge, student details)
- Class/community formation + push assignments
- Collaborative student work (remote, comments, branches, voting)
- Mark record management + manual entry

### My assessment: This is a full LMS feature set. Build in phases.

This is ambitious — it's essentially building a learning management system on top of the learning assistant. It's the right vision for school subscriptions (the Pro/School revenue path), but it needs to be phased to avoid overbuilding before you have users.

**Critical design constraint: Teacher mode must work for independent tutors and private teachers, not just school-assigned teachers.** A tutor running their own practice must be able to sign up, create assignments, and see student results without a school admin. The RBAC hierarchy (superadmin → school admin → teacher → student) must support a "solo tutor" path where the teacher is self-provisioned — no school admin required. This means:

- A tutor can create an account directly (no school invitation needed)
- They get teacher-level permissions immediately
- They can invite students directly (student signs up with a join code)
- They see their own student results dashboard
- If they later join a school, their account can be linked to that school's admin

**Recommended phasing:**

#### Phase 1: Teacher Question Generation (MVP)
- Teacher (including solo tutors) selects subject → topic → subskill → generates questions
- Teacher can edit question text and expected answer
- Teacher can save a set as an "assignment"
- Students see the assignment (via class or via tutor's join code)
- Auto-marking runs against the expected answer
- Results visible to teacher in a simple table

**This is the minimum viable teacher mode.** It proves the core loop: teacher creates → student completes → auto-marks → teacher sees results. Works for both school-assigned teachers and independent tutors.

#### Phase 2: Marking Points + Semantic Answers
- Semantic answers get editable marking points
- Highlight-to-create-marking-point UI (text selection → "Add as marking point")
- Teacher can edit auto-marking results
- Teacher can override marks with comments

#### Phase 3: Assignment Management
- Immediate vs. teacher-review reveal toggle
- Printable PDF generation with cover page wizard
- Class formation (name class, assign students)
- Push assignments to class

#### Phase 4: Collaboration (skeletons/scaffolding only)
- Student collaborative work (branches, comments, voting)
- **Decision: Build skeletons/scaffolding only — not full functionality.** Expose the UI and data structures (branch creation, comment threads, vote buttons) but don't invest in real-time sync or full branching logic yet. This lets us validate interest before committing to the complexity of real-time collaboration.
- Full collaboration should wait until you have active classes using the basic assignment flow and users explicitly request it

#### Phase 5: Mark Records + Reporting
- Mark book / gradebook
- Manual mark entry (for non-app work)
- Term report generation from app + manual marks
- Collation to school admin

**Technical notes:**

- **Highlight-to-create-marking-point:** Use the browser's `Selection` API (`window.getSelection()`) to capture the highlighted text range, store it as `{ startOffset, endOffset, text, markingPointText }` relative to the student's answer. This is a standard rich-text interaction pattern.

- **Printable PDF:** Use a server-side PDF library (e.g., `puppeteer` for HTML→PDF, or `pdfmake` for declarative PDF generation). The cover page wizard collects: school name, school badge (image upload), teacher name, subject, grade, date, student name field. Generate a multi-page PDF: cover page + question pages + (optional) answer pages.

- **Collaborative branches:** This requires real-time sync (WebSockets or Supabase Realtime). Each student's input is a "branch" — a versioned tree of working. Voting promotes a branch (or part of it) to the "main" submission. This is essentially a simplified Git branching model applied to student work. It's powerful but complex — build it last.

---

## 6. Admin Mode

### What the document proposes
Two levels:
- **Superadmin/owner:** overrides everything, access to all parts of the app
- **School admin:** manages the app for subscribed schools — registers teachers (staff number/email), registers students (student number/email), assigns students to teachers, forms classes (flexible naming), collates records for final reports

### My assessment: Standard LMS admin model, well-suited to the SA school context

**Architecture recommendation:**

```
Superadmin (Fundile owner)
    │
    ├── Manages: school subscriptions, pricing, global settings, all data
    │
    ▼
School Admin (per school)
    │
    ├── Registers teachers (staff number or email)
    ├── Registers students (student number or email)
    ├── Assigns students to teachers / forms classes
    ├── Collates records for final reports
    │
    ▼
Teacher
    │
    ├── Manages: their classes, assignments, marks
    │
    ▼
Student
    │
    └── Learns
```

**Key design decisions:**

1. **Role-based access control (RBAC) in Firestore.** Use Firestore Security Rules + custom claims on the auth token:
   - `role: 'superadmin'` — access to all collections
   - `role: 'schooladmin', schoolId: 'xyz'` — access to their school's collections
   - `role: 'teacher', schoolId: 'xyz', teacherId: 'abc'` — access to their classes
   - `role: 'student', schoolId: 'xyz', studentId: 'def'` — access to their own data

2. **Flexible class naming.** SA schools use different naming conventions: "Grade 10A," "10 Accounting Set 1," "Ms. Nkosi's Class." Store class name as a free-text field, not a constrained format. The class object: `{ id, schoolId, teacherId, name, studentIds: [], subject, grade }`.

3. **Registration by staff/student number OR email.** Support both:
   - If email provided: send invitation email with signup link
   - If only number provided: admin creates the account, student/teacher claims it on first login with a matching identifier
   - Bulk import: CSV upload for schools registering many students at once

4. **Record collation.** School admin sees a dashboard: all classes → all teachers → all students. Can export term reports aggregating: app-generated marks (auto) + teacher-entered marks (manual). This is the "LMS" layer that makes Fundile sellable to whole schools.

---

## 7. Utility of the User System Profile

### What the document proposes
Telling users what you know about them + giving them a plan to improve = better retention. Richer tracking → richer feedback → richer advice → more perceived value. .md files help design a notification/reminder system. Drive retention after free trial.

### My assessment: This is the correct retention thesis. Here's how to operationalize it.

**The retention loop:**

```
Session → .md file → Agent updates profile → Agent generates:
    ├── "What we know about you" summary (shown to student)
    ├── Personalized improvement plan (shown to student)
    ├── Notification triggers (e.g., "You haven't practiced in 3 days")
    └── Report to parent/teacher (if applicable)
        │
        ▼
    Student feels seen + gets actionable advice → returns
```

**"What we know about you" panel:**
After each session, show the student a brief, honest summary:
- "You're strong at: identifying accounting concepts, classifying accounts"
- "You're working on: bank reconciliation — specifically the outstanding cheques step"
- "Your plan: 2 more scaffold sessions on outstanding cheques, then reassess"
- "This week: 4 sessions, 67% average, improving trend ↑"

This transparency builds trust and makes the app feel like a tutor who actually knows them, not a generic practice tool.

**Notification/reminder system:**
Using the profile + .md session history:
- **Re-engagement:** "You haven't practiced [topic] in 5 days. Your last session showed [weakness]. Ready for another go?"
- **Mastery celebration:** "You've mastered [subskill]! 3 correct in a row across 2 weeks. Moving you to [next subskill]."
- **Trial-ending reminder:** "Your 2-week trial ends in 3 days. You've completed 12 sessions and improved 23% on [topic]. Subscribe to keep your progress." (This is the key trial-to-paid conversion moment.)
- **Streak protection:** "You're on a 4-day streak. Practice today to keep it alive."

**Driving retention after free trial:**
The trial-to-paid conversion hinges on the student feeling that:
1. The app knows them (profile)
2. The app has a plan for them (improvement path)
3. Losing the app means losing their progress (sunk cost + profile continuity)
4. The cost is trivial vs. tutoring (pricing anchor)

The profile is what makes #1 and #2 work. Without it, Fundile is just a question bank. With it, Fundile is a personal tutor that remembers everything.

---

## 8. Free Trial + Package Review

### What the document proposes
- No free package — remove all intimations of free package from landing page
- Institute a 2-week free trial
- May need to relook Standard and Pro packages

### My assessment: Agreed. Specific recommendations:

**Free trial mechanics:**
- 2 weeks, full Standard access, no card required
- On trial signup: collect email + grade + subject(s) of interest
- Trial starts immediately
- Day 10: email reminder ("3 days left in your trial")
- Day 13: email reminder ("1 day left — subscribe to keep your progress")
- Day 14: trial ends. **Hard paywall** — student cannot start new sessions. Profile and past session history persist (retention hook), but practice requires a subscription.
- **Critical:** The profile and session history persist after trial. This is the retention hook — they don't want to lose their record. The hard paywall creates stronger conversion pressure than read-only access.

**Package review:**

| Package | Current | Recommendation | Rationale |
|---------|---------|---------------|-----------|
| Free | R0 forever | **Remove** | Per document. Replace with trial. |
| Standard | R150/mo | **Keep at R150/mo** | Competitive vs. tutoring. Full learning assistant. |
| Pro | R299/mo | **Keep at R299/mo, "coming soon"** | Socratic AI tutor is a differentiator but not ready. |
| School | Not defined | **Add: School plan (custom pricing)** | Per-school subscription, includes teacher mode + admin mode. This is the B2B revenue path. |

**School plan pricing approach:** Per-student-per-month or flat per-school. SA schools have limited budgets — consider a per-student model (e.g., R50/student/month for schools, vs. R150 for individual). This makes Fundile cheaper per student when bought in bulk, incentivizing school adoption.

---

## 9. Cost Savings — Free/Open-Source LLM via Hugging Face

### What the document proposes
Use a free or open-source model via Hugging Face as the LLM for agents.

### My assessment: Feasible and wise for cost control, with important caveats.

**The cost problem:** Using OpenAI GPT-4 or Anthropic Claude for every agent interaction (profile updates, report generation, feedback analysis) would be expensive at scale. If you have 1000 students each generating 5 sessions/week, that's 5000 agent calls/week. At even $0.01/call, that's $50/week = $200/month — more than your Cloudflare Stream budget.

**Hugging Face approach (confirmed decision):**

1. **Use Hugging Face managed Inference Endpoints** (not self-hosting on a VPS):
   - **Recommended models:** Llama 3.1 8B (Meta) or Mistral 7B — both open-weights, capable enough for structured analysis tasks (reading .md files, updating profiles, generating reports)
   - **Cost:** Hugging Face Inference Endpoint for a 7-8B model: ~$0.06/hour (CPU) or ~$0.60/hour (GPU). If you only need the agent for batch processing (not real-time), you can spin up the endpoint on-demand, process a batch of .md files, and spin down — paying only for minutes used.
   - **Why not self-host:** Self-hosting on a VPS (e.g., Hetzner GPU) was considered but rejected — it adds infrastructure management overhead (monitoring, updates, security, scaling) that isn't worth it at this stage. Hugging Face managed endpoints handle all of this. We can revisit self-hosting if costs grow significantly at scale.

2. **Use the model for agent tasks, not for question generation:**
   - **Question generation** (creating questions, expected answers, marking points) should remain **deterministic** (your existing generators) — this is the "internal consistency" promise. An LLM generating questions risks inconsistency between question and answer.
   - **Agent tasks** (reading .md files, updating profiles, generating reports, diagnosing error patterns) are perfect for an open-source LLM — they're analysis tasks, not generation tasks.

3. **Hybrid approach (recommended):**
   - **Question generation:** Deterministic code (your existing generators) — zero LLM cost, guaranteed consistency
   - **Agent analysis (profile, reports, diagnosis):** Open-source LLM via Hugging Face managed endpoints — low cost, good enough for structured analysis
   - **Pro tier Socratic tutor (future):** Larger model (Llama 3.1 70B or GPT-4o-mini) — this is the premium feature that justifies the R299/mo price

4. **Prompt engineering for small models:** 7-8B models are less capable than GPT-4. Prompts must be:
   - Highly structured (use JSON output format)
   - Few-shot (include examples in the prompt)
   - Narrow in scope (one task per call — "read this .md, output a JSON profile update" — not "read all .md files and write a comprehensive report")

**Caveats:**
- **Latency:** 7B models on CPU are slow (5-15s per response). For batch processing (nightly profile updates), this is fine. For real-time (student sees feedback immediately), use GPU endpoints.
- **Quality:** 7-8B models can misinterpret complex answers. Always validate agent output against the deterministic expected answer. If the agent says "student got it wrong" but the deterministic marker says "correct," trust the deterministic marker.
- **Data privacy:** Using Hugging Face managed endpoints means data goes to HF servers — check their data retention policy for POPIA compliance. If this becomes a blocker, we can revisit self-hosting later.

**Recommended architecture:**

```
Student session
    │
    ▼
Deterministic generator (question + expected answer)  ← zero LLM cost
    │
    ▼
Student answers → Deterministic marker (score + procedure tracking)  ← zero LLM cost
    │
    ▼
.md file written (question + expected answer + student input + procedure tracking)
    │
    ▼
Agent (open-source LLM via Hugging Face managed endpoint, batch/nightly) reads .md files  ← ~$30/month on-demand
    │
    ▼
Profile updated in Firestore
    │
    ▼
Reports + recommendations generated
```

**Estimated monthly cost at 1000 students:**
- Hugging Face managed LLM endpoint: ~$30/month (on-demand batch processing)
- Cloudflare Stream: ~$2/month
- Supabase (database + storage): Free tier → ~$25/month at scale
- Firebase/Firestore: Free tier → ~$25/month at scale
- **Total: ~$100-120/month for 1000 students** — sustainable on R150/mo subscriptions

---

## 10. Summary of Recommendations

| Area | Recommendation | Priority |
|------|---------------|----------|
| Session .md files | YAML frontmatter + Markdown body, dual human/machine format | Phase 1 |
| Answer types | JSON serialization + human-readable rendering per type | Phase 1 |
| Procedure tracking in .md | Yes — add `# Procedure Tracking` section with step-by-step JSON | Phase 1 |
| Student system profile | Living document in Firestore, updated by agent from .md files. Students do NOT see .md files — agent delivers insights in plain language | Phase 1 |
| Teacher mode | Phase in 5 stages: generation → marking points → assignments → collaboration (skeletons only) → records. Must support independent tutors, not just school-assigned teachers | Phase 2-4 |
| Admin mode | RBAC with superadmin + school admin roles, flexible class naming | Phase 2 |
| Profile utility | "What we know about you" panel + notification system + trial conversion | Phase 1-2 |
| Free trial | 2 weeks, full Standard, no card, **hard paywall** at end, profile persists after trial | Phase 1 |
| Package review | Remove Free, keep Standard R150, keep Pro R299, add School plan (per-student pricing, TBD) | Phase 1 |
| LLM cost savings | Open-source 7-8B model (Llama 3.1 / Mistral) via **Hugging Face managed endpoints** (not self-hosted), deterministic code for generation | Phase 1 |

---

## 11. Open Questions — Resolved

1. **School plan pricing:** Per-student model. Price TBD (consider ~R50/student/month for schools vs. R150 for individual). Makes Fundile cheaper per student in bulk, incentivizing school adoption.
2. **Teacher mode priority:** Teacher mode must work for **independent tutors and private teachers**, not just school-assigned teachers. A tutor running their own practice (not employed by a school) must be able to sign up, create assignments, and see student results — without a school admin. This means teacher mode needs a "solo tutor" path alongside the "school teacher" path.
3. **Collaboration feature:** Build **skeletons/scaffolding only** — not full functionality. Scaffold the branches/voting UI so the architecture is in place, but don't build the real-time sync engine yet. This keeps the door open without over-investing.
4. **LLM hosting:** **Hugging Face managed endpoints** (not self-hosting on a VPS). Easier to manage, no server maintenance, slightly more expensive but worth the operational simplicity. Use on-demand batch processing to control cost.
5. **Profile transparency:** Students **do not see the .md files**. They receive communication *from the agent* — the agent reads the .md files, updates the profile, and delivers insights/recommendations to the student in plain language. The .md files are internal system data; the student-facing surface is the agent's communication (e.g., "You're struggling with bank reconciliation — here's what to focus on").
6. **Trial conversion:** **Hard paywall** at trial end (not soft/read-only). When the 2-week trial ends, the student cannot start new sessions. The profile and past session history persist (retention hook), but practice requires a subscription. This is a stronger conversion signal than read-only access.
