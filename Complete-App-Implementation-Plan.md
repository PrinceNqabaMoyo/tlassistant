# Complete App — Implementation Plan

> **Layer dependency:**
> This plan is Layer D. It depends on:
> - **Layer A** — Core learning loop (generators, procedure tracker, student model) — already exists
> - **Layer B** — Simulation system — see `Simulation-implementation-plan.md` §1–13
> - **Layer C** — Pro Agent — see `Simulation-implementation-plan.md` §14–22
>
> Do not begin Layer D work until Layers B and C are stable and tested.

---

## 0. Guiding Principles for This Layer

1. **The deterministic systems always win.** The procedure tracker, cell marker, and rubric keyword
   detector are the sources of truth for correctness. No LLM output may override them.

2. **The `.md` session file is for audit and internal agent use — not the primary data pipeline.**
   Student mastery and error data flow in real time from the deterministic systems into the student
   model (Firestore). The `.md` file is a portable, machine-readable record the agent reads to
   generate reports. It is never sent to a teacher or parent directly.

3. **External reports (teacher, parent) are always PDF.** They contain only diagnostic, measurable,
   actionable, and forward-looking content. Raw session data, JSON blocks, and internal field names
   never appear in an external-facing document. The report is a value-demonstration and retention
   hook — it should read like a tutor's written feedback, not a system log.

4. **Students never see raw session files or internal data structures.** Everything surfaced to
   the student comes via the agent's language layer — plain, encouraging, and actionable.

5. **Teacher mode must work for independent tutors and private teachers, not only
   school-assigned teachers.** A solo tutor running their own practice can sign up without a
   school admin and invite students directly via a join code.

6. **Empty cells do not earn marks. Filling a cell that should be empty earns a deduction.**
   Only student-filled cells that are correct earn marks. A student cannot score positive marks
   by leaving everything blank.

7. **Every archetype has fixed, reproducible marking criteria** defined at generator time and
   stored alongside the question. The same archetype always awards marks on the same basis,
   regardless of seed, student, or session.

8. **The dashboard is a retention hook.** The student profile panel — showing strengths,
   focus areas, trajectory, and plan — is the most important value-demonstration surface in the
   app. Its design must be ready for the full data pipeline before Phase D1 ships.

9. **Landing page changes are deferred and require explicit owner approval before implementation.**

---

## 1. Session `.md` Audit Files

### 1.1 Purpose and Scope

A session `.md` file is written at the end of every practice session. It is:
- A **machine-readable record** of what the student did, what the correct answer was, and what
  the system found about their procedure — consumed by the agent to generate reports.
- An **internal audit trail** — in a dispute about a mark or a generated question, the session
  file is the definitive record.
- **Never sent externally as a `.md` file.** Teachers and parents receive a formatted PDF report
  derived from session data. The `.md` file is internal infrastructure.

It is **not** the primary source for real-time mastery updates. Those flow directly from the
deterministic systems into Firestore during the session.

### 1.2 File Format: YAML Frontmatter + Markdown Body

Every session file has two parts: a machine-parseable YAML header and a human-readable Markdown
body. This dual format means an agent can parse the header for structured fields without reading
prose, and a human can read the body without parsing JSON.

```markdown
---
sessionId:       "2025-03-15-acct-gr10-crj-entry-001"
userId:          "usr_abc123"
subject:         "Accounting"
grade:           "10"
topic:           "Sole Trader"
subskill:        "CRJ Entry"
archetypeKey:    "crj_entry"
questionSeed:    9
adaptiveLevel:   "scaffold"
timestamp:       "2025-03-15T14:32:00+02:00"
durationSeconds: 842
score:           0.67
markingResult:
  totalMarks:    12
  awarded:       8
  firstErrorCell:
    tableId:     "crj"
    side:        "debit"
    col:         "Creditors"
    row:         2
  misconceptionTag: "net_vs_gross_confusion"
procedureFlags:
  - "correct_date_entries"
  - "wrong_creditors_amount"
  - "omitted_closing_balance"
adaptiveOutcome:  "repeat_scaffold"   # repeat_scaffold | advance_to_practice | advance_to_assessment
cacheVersion:    1
---

# Question

[Generated question text, including source documents and context]

## Tables Given to Student

[Markdown table(s) or CSV blocks for pre-filled table data]

---

# Expected Answer

## [Table name, e.g. Cash Receipts Journal]

[Markdown table — the correct completed table]

<!-- machine-readable -->
```json
{
  "type": "table",
  "tableType": "cash_receipts_journal",
  "columns": ["Day", "Details", "Fol", "Bank", "Debtors", "Sales", "VAT"],
  "rows": [
    ["01", "Cash sales", "CRJ1", 11400, null, 10000, 1400],
    ["15", "J. Mokoena", "CRJ1", 5000, 5000, null, null]
  ]
}
```

---

# Student Input

## [Table name]

[Markdown table — what the student actually submitted]

<!-- machine-readable -->
```json
{
  "type": "table",
  "tableType": "cash_receipts_journal",
  "columns": ["Day", "Details", "Fol", "Bank", "Debtors", "Sales", "VAT"],
  "rows": [
    ["01", "Cash sales", "CRJ1", 10000, null, 10000, null],
    ["15", "J. Mokoena", "CRJ1", 5000, 5000, null, null]
  ]
}
```

---

# Procedure Tracking

```json
[
  { "step": 1, "description": "Date entries", "status": "correct", "durationMs": 4200 },
  { "step": 2, "description": "Details column", "status": "correct", "durationMs": 3100 },
  { "step": 3, "description": "Bank column (row 1)", "status": "wrong",
    "error": "Used net amount R10,000 instead of gross R11,400 — VAT not added",
    "misconceptionTag": "net_vs_gross_confusion", "durationMs": 12400 },
  { "step": 4, "description": "Closing balance", "status": "omitted", "durationMs": 0 }
]
```

## Agent Diagnosis

Student correctly identifies dates and details. The Bank column error in row 1 indicates confusion
between gross (Bank = Net + VAT) and net amounts. The closing balance was omitted entirely —
this is a procedural gap, not a calculation error.
```

### 1.3 Table Serialisation Rules

| Answer type | Markdown format | JSON machine-readable block |
|---|---|---|
| Simple table | Standard Markdown table | `type: "table"` with rows array |
| Nested-header table (accounting) | Flattened Markdown table with composite column names | `type: "table"` with schema comment |
| MCQ | `- [x] Option A` checklist | `type: "mcq"` with selected and correct |
| Word bank | Inline `[word]` tokens in a sentence | `type: "word_bank"` with token sequence |
| Column arrangement | Numbered ordered list | `type: "arrangement"` with order array |
| Mathematical working | LaTeX fenced block | `type: "working"` with step array |
| Semantic / essay | Plain text | `type: "semantic"` with markingPoints hit/miss |

**Nested accounting columns:** Accounting and EMS tables often have nested headers (e.g.,
a General Ledger with a Debit sub-column and a Credit sub-column under "Amount"). Markdown
cannot express nested headers. Use composite column names in the flattened Markdown table
and a `schema_note` in the JSON block:

```json
{
  "type": "table",
  "tableType": "general_ledger_t_account",
  "schema_note": "Columns prefixed 'dr_' are debit side; 'cr_' are credit side",
  "columns": ["dr_date", "dr_details", "dr_folio", "dr_amount",
               "cr_date", "cr_details", "cr_folio", "cr_amount"],
  "rows": [ ... ]
}
```

### 1.4 File Storage and Indexing

| Concern | Decision | Rationale |
|---|---|---|
| **File storage** | Firebase Storage | Already in use; `.md` files are tiny (2–10 KB each) — 10,000 sessions ≈ 100 MB, well within the free tier for the foreseeable post-launch period. No second database (e.g. Supabase) needed. |
| **Path structure** | `sessions/{userId}/{year}/{month}/{sessionId}.md` | Queryable by user and period |
| **Indexing** | Firestore collection `session_index` | Stores path + key metadata **and step-level procedure data** (see §1.4a) for fully deterministic queries without reading the file |
| **Retention** | Indefinite for subscribed users; 30 days post-trial | Retention hook: profile persists, session files prompt return |
| **Access control** | Student: own files read-only. Agent service account: all files (for report generation). No direct teacher or parent access to raw `.md` files. | Firebase Storage rules + custom claims |

### 1.4a session_index Firestore Document Schema

The `.md` file is the **human-readable audit trail**. The `session_index` Firestore document
is the **compute-ready record**. All aggregate metrics, error-rate calculations, and
intervention triggers operate exclusively on Firestore — the `.md` file is never read for
these purposes.

This is the dual-layer principle: structured data for deterministic computation; generated
prose (PDF reports) for human communication.

```json
// Firestore: session_index/{sessionId}
{
  "sessionId":      "2025-03-15-acct-gr10-crj-entry-001",
  "userId":         "usr_abc123",
  "subject":        "Accounting",
  "grade":          "10",
  "topic":          "Sole Trader",
  "subskill":       "crj_entry",
  "archetypeKey":   "crj_entry",
  "adaptiveLevel":  "scaffold",
  "date":           "2025-03-15",
  "timestamp":      "2025-03-15T14:32:00+02:00",
  "durationSeconds": 842,
  "score":          0.67,
  "totalMarks":     12,
  "awarded":        8,
  "mdStoragePath":  "sessions/usr_abc123/2025/03/2025-03-15-acct-gr10-crj-entry-001.md",

  "misconceptionTags": ["net_vs_gross_confusion"],

  "procedureSteps": [
    { "step": 1, "concept": "date_entries",      "status": "correct",
      "durationMs": 4200 },
    { "step": 2, "concept": "details_column",    "status": "correct",
      "durationMs": 3100 },
    { "step": 3, "concept": "bank_gross_amount", "status": "failed",
      "errorType": "net_vs_gross_confusion",     "durationMs": 12400 },
    { "step": 4, "concept": "closing_balance",   "status": "omitted",
      "durationMs": 0 }
  ],

  "cellErrors": [
    { "tableId": "crj", "col": "Bank", "row": 1,
      "errorType": "net_vs_gross_confusion", "studentValue": 10000, "expectedValue": 11400 }
  ]
}
```

**What this enables without an LLM:**

```python
# Error rate for a specific misconception across all sessions
def error_rate(user_id: str, error_type: str, concept: str) -> float:
    steps = db.collection("session_index") \
              .where("userId", "==", user_id) \
              .where("procedureSteps", "array_contains_any",
                     [{"concept": concept}]) \
              .stream()
    total, failed = 0, 0
    for doc in steps:
        for s in doc.get("procedureSteps", []):
            if s["concept"] == concept:
                total += 1
                if s.get("errorType") == error_type:
                    failed += 1
    return failed / max(total, 1)

# Trigger a targeted drill if error appears more than 3 times
if error_rate(user_id, "net_vs_gross_confusion", "bank_gross_amount") > 0.5:
    gamification_service.trigger_micro_drill(user_id, "net_vs_gross_confusion")
```

The LLM is never invoked for this logic. It runs in the backend after every submission,
using only Firestore data.

### 1.5 When the File is Written

The session file is written **once, at session end** — not incrementally during the session.
This avoids partial writes and keeps the record atomic. The write is triggered by:
- The student submitting their final answer in Assessment mode
- The student closing the session in Practice or Scaffold mode (with a confirmation prompt)
- A session timeout after 30 minutes of inactivity

The write happens in the background; it does not block the UI.

### 1.6 Backend: Session File Service

```
caps-ai-backend/app/services/session_file_writer.py
```

```python
class SessionFileWriter:
    def write(self, session: SessionData) -> str:
        """
        Two writes happen at session end, in order:
        1. Firestore session_index document (compute-ready, step-level data).
        2. Firebase Storage .md file (human-readable audit trail).
        The Firestore write is the authoritative record; the .md write is supplementary.
        """
        # 1. Write structured index to Firestore first
        self._index_in_firestore(session)   # includes procedureSteps, cellErrors

        # 2. Write human-readable audit file to Storage
        frontmatter = self._build_frontmatter(session)
        body        = self._build_body(session)
        content     = f"---\n{yaml.dump(frontmatter)}---\n\n{body}"
        path        = f"sessions/{session.user_id}/{session.year}/{session.month}/{session.session_id}.md"
        self.storage.upload(path, content, content_type="text/markdown")

        # 3. Update the Firestore index document with the storage path
        self._update_storage_path(session.session_id, path)
        return path
```

---

## 2. Student System Profile

### 2.1 Architecture: Real-Time, Not Nightly Batch

The student profile is updated **in real time by the deterministic systems** during each session.
The LLM is not part of the profile-update pipeline. This is a deliberate departure from the
batch-LLM approach.

```
Deterministic systems (procedure tracker, cell marker, rubric KD)
        │
        │  emit: { misconception_tag, error_type, subskill, score, duration }
        ▼
student_model.py (in-process, every submission)
        │
        │  writes: mastery updates, error pattern increments, session history
        ▼
Firestore: students/{userId}/profile
        │
        │  (separately, at session end)
        ▼
session_file_writer.py → Firebase Storage (.md file)
        │
        │  (separately, on demand: report generation, recommendation panel)
        ▼
LLM (Hugging Face managed endpoint) reads recent session files
        │
        │  outputs: plain-language summary, recommendations, report text
        ▼
Rendered to student / teacher / parent
```

The LLM reads session files to *articulate* insights — it does not *derive* them. The profile
data already exists in Firestore before the LLM is ever called.

### 2.2 Profile Schema (Firestore)

```
students/{userId}/
  profile: {
    displayName:      string,
    profilePictureUrl: string | null,   // Firebase Storage URL; user-uploaded or initials fallback
    grade:            string,
    subjects:         string[],
    createdAt:        timestamp,
    lastActiveAt:     timestamp,
    trialEndsAt:      timestamp | null,
    subscriptionTier: "trial" | "standard" | "pro" | "school",

    mastery: {
      "{subject}": {
        "{topic}": {
          "{subskill}": {
            attempts:          number,
            correct:           number,
            confidenceScore:   number,   // 0.0–1.0, decays with recency
            lastAssessed:      timestamp,
            masteryReached:    boolean,  // true after 3 correct across 2+ sessions
            averageDuration:   number    // ms per question
          }
        }
      }
    },

    errorPatterns: [
      {
        misconceptionTag:  string,
        subject:           string,
        topic:             string,
        occurrences:       number,
        lastSeen:          timestamp,
        resolved:          boolean      // true if 3 correct after the error
      }
    ],

    learningStyleSignals: {
      prefersScaffold:       boolean,
      rushesToAssessment:    boolean,
      skipsFeedback:         boolean,
      averageSessionMinutes: number
    },

    progressTrajectory: [
      { date: string, overallMastery: number, bySubject: { [subject]: number } }
    ],

    sessionCount:    number,
    currentStreak:   number,          // consecutive days with at least one session
    longestStreak:   number
  }
```

### 2.2a Profile Picture

Every user dashboard has a profile picture slot. If the user has not uploaded a photo, the app
renders a styled initials avatar (first + last initial, coloured by a hash of the user ID —
consistent across sessions). Profile pictures are uploaded to Firebase Storage at
`profile-pictures/{userId}/avatar.jpg`, resized server-side to 256×256 px.

The `profilePictureUrl` field on the Firestore profile is updated after successful upload. All
dashboard components that display the user's identity read from this field via `useStudentProfile`.

### 2.3 Confidence Score Calculation

A single correct answer does not confer mastery. The confidence score uses a weighted formula:

```
confidenceScore = (correctRatio * 0.6) + (recencyWeight * 0.25) + (consistencyWeight * 0.15)

correctRatio      = correct / max(attempts, 1)
recencyWeight     = e^(-daysSinceLastAssessed / 14)   // decays to 0.5 at 14 days
consistencyWeight = 1.0 if correct across ≥ 2 different sessions, else 0.5
```

`masteryReached = true` when `confidenceScore >= 0.8` and `attempts >= 3`.

### 2.4 "What We Know About You" Panel

After every session, the student sees a brief, honest summary rendered by the agent from the
Firestore profile (no LLM needed for this — it is template-driven):

```
┌──────────────────────────────────────────────────────────┐
│  Your session — 15 March 2025                           │
│                                                          │
│  ✅ You're strong at:                                    │
│     Date entries, Details column, Folio references      │
│                                                          │
│  🎯 You're working on:                                   │
│     Bank column — gross vs. net amounts                  │
│     (This has come up in 3 sessions)                     │
│                                                          │
│  📋 Your plan:                                           │
│     2 more scaffold sessions on CRJ entries              │
│     Focus: VAT and gross amounts                         │
│                                                          │
│  📈 This week: 4 sessions · 67% avg · ↑ improving       │
└──────────────────────────────────────────────────────────┘
```

This panel is generated from Firestore data only — no LLM call. The LLM is reserved for
longer-form reports (teacher/parent) and the Pro agent's live tutor interaction.

### 2.5 Backend: Student Model Updates

The existing `app/services/student_model.py` is extended to:

```python
def record_submission(self, user_id: str, submission_result: SubmissionResult):
    """
    Called after every marking event. Updates mastery, error patterns, streak,
    and learning style signals in real time.
    """
    self._update_mastery(user_id, submission_result)
    self._update_error_patterns(user_id, submission_result)
    self._update_learning_signals(user_id, submission_result)
    self._update_streak(user_id)
    self._append_trajectory_point(user_id)   # daily, not per-submission

def generate_session_summary(self, user_id: str) -> SessionSummary:
    """
    Template-driven. Reads Firestore profile and returns structured summary data.
    No LLM call.
    """
    ...
```

---

## 3. Agent-Generated Reports

### 3.1 Report Types

| Report | Format | Recipient | Trigger | During trial? | LLM? |
|---|---|---|---|---|---|
| Session summary panel | In-app | Student | After every session | **Yes** | No — template |
| Weekly progress digest | In-app + email | Student | Every 7 days | **Yes** | Light |
| Parent weekly report | **PDF email** | Parent | Every 7 days, if linked | **Yes** | Yes |
| Teacher class report | **PDF, on demand** | Teacher | Teacher requests | Yes | Yes |
| Trial conversion summary | In-app + email | Student | Days 7, 10, 13, 14 | — | No — template |

> **Trial period reports are active from Day 1.** The session summary panel, weekly digest, and
> parent PDF are the primary mechanisms for demonstrating value during the trial. A student who
> sees their own data growing — and whose parent receives a readable PDF about their progress —
> has a far stronger reason to subscribe. Reports must ship with Phase D1, not later.

### 3.2 PDF Report Format

All external-facing reports (parent, teacher) are **PDFs generated server-side via Puppeteer**.
They never expose `.md` content, JSON, field names, or internal identifiers.

**PDF content rules:**
- ✅ Diagnostic: what the student understands and what they are confused about
- ✅ Measurable: specific subskill scores, session counts, trend direction
- ✅ Actionable: what to practise next, how many sessions recommended
- ✅ Forward-looking: projected path to mastery, next milestone
- ❌ No raw JSON, no field names, no internal tags, no system language
- ❌ No comparison to other students (privacy)

**Parent report PDF structure (1 page):**
```
┌─────────────────────────────────────────────────────────┐
│  [Fundile logo]     [Student name]  [Grade]  [Date]     │
├─────────────────────────────────────────────────────────┤
│  THIS WEEK                                              │
│  Sessions completed: 4  ·  Avg score: 67%  ·  ↑ +8%   │
│  Current streak: 4 days                                 │
├─────────────────────────────────────────────────────────┤
│  STRENGTHS                                              │
│  [Subject] — [Topic]: performing confidently            │
├─────────────────────────────────────────────────────────┤
│  FOCUS AREA                                             │
│  [Subject] — [Subskill]: appearing in 3 sessions.      │
│  Recommended: 2 more scaffold sessions this week.       │
├─────────────────────────────────────────────────────────┤
│  NEXT MILESTONE                                         │
│  On track to reach mastery in [subskill] by [date]     │
└─────────────────────────────────────────────────────────┘
```

**Teacher class report PDF structure (multi-page):**
1. Cover: class name, subject, grade, period, teacher name
2. Class overview: mastery heatmap by topic × student
3. Flagged students: those below threshold, with specific subskill gaps
4. LLM-written narrative: what to re-teach, which subskills are ready for assessment
5. Individual summaries: one paragraph per student

### 3.3 LLM Report Generation

The LLM receives a stripped-down JSON summary of profile data — not raw `.md` files:

```python
REPORT_PROMPT_TEMPLATE = """
You are writing a {report_type} for a South African high school student using Fundile.

## Student Profile Summary
{profile_json}

## Rules
- Tone: encouraging, specific, actionable.
- Do NOT use field names, JSON keys, or system language.
- DO use CAPS subject and topic names.
- DO give 1–2 specific, concrete recommendations.
- Length: 150 words max for parent report; 300 words max for teacher report.
- Do NOT invent data not present in the summary.
- Write as if you are a knowledgeable tutor, not a software system.
"""
```

---

## 4. Teacher Mode

### 4.1 RBAC for Teachers

Two paths to teacher status:

| Path | How | Permissions |
|---|---|---|
| **Solo tutor** | Self-registers at `/signup?role=teacher`. Gets teacher permissions immediately. | Manages their own classes, assignments, marks |
| **School teacher** | Invited by school admin (email or staff number). Accepts invitation. | Same as solo, plus linked to school's admin dashboard |

A solo tutor can later be linked to a school by a school admin without losing their existing
classes or data.

### 4.2 Phase 1: Teacher Question Generation (MVP)

**What this delivers:** A teacher can generate, edit, save, and push questions to students.

#### Features
- Teacher selects: subject → grade → topic → subskill → difficulty
- Generator produces the question (same deterministic generators as the student workspace)
- Teacher can **edit the question text** in a rich-text editor
- Teacher can **edit the expected answer** (with a warning that edits affect auto-marking)
- Teacher saves the question to a personal question bank
- Teacher assembles questions into an **Assignment** (ordered set of questions)
- Teacher pushes the assignment to a class or sends a join link to individual students

#### Technical Notes
- The question editor is a simple `<textarea>` with Markdown preview for the question text field
- For tabular answers (accounting), the expected answer editor shows the table structure; the
  teacher edits individual cells
- Saving a teacher-edited question stores the original generator output + the teacher's diff
  (not a full copy), so the original can always be recovered
- Assignments are stored in Firestore: `assignments/{assignmentId}` with fields:
  `{ teacherId, classId, title, questions: [{ questionId, seed, teacherEdits }], dueDate,
  revealImmediately, status }`

### 4.3 Phase 2: Marking Points and Semantic Answers

**What this delivers:** Teachers can define and edit marking points for open-ended answers.

#### Features
- Semantic (essay/paragraph) answers display the auto-generated marking points
- Teacher can **edit marking point text** inline
- **Highlight-to-mark-point:** teacher highlights any section of the expected answer and clicks
  "Add as marking point" — the highlighted text becomes a marking point
- Teacher can **override auto-marking** on individual student submissions with a comment
- Override is logged: `{ originalScore, overriddenScore, teacherComment, timestamp }`

#### Technical Notes
- Highlighting uses the browser's `Selection` API:
  `window.getSelection().getRangeAt(0)` → `{ startOffset, endOffset, text }`
- Marking points are stored as: `{ id, text, offset: { start, end }, required: boolean, marks: number }`
- The auto-marker checks for keyword presence; the teacher's stored marking points extend this
  vocabulary for their specific assignment
- A "restore auto-mark" button reverts teacher overrides

### 4.4 Phase 3: Assignment Management

**What this delivers:** Full assignment lifecycle — distribution, timing, results, and PDF.

#### Features
- **Reveal toggle:** "Show results immediately after submission" vs "Hold for teacher review"
- **Due date:** assignments become unavailable after the due date (students can view but not submit)
- **PDF generation:** teacher clicks "Export as PDF" — server-side Puppeteer renders the
  assignment as a print-ready document
- **Cover page wizard:** school name, school badge (image upload), teacher name, subject, grade,
  date, student name field (blank for printing), class name
- **Class management:** teacher creates classes (free-text name), adds students by email or
  student number, pushes assignments to a class in one click
- **Join code:** teacher generates a 6-character join code; students enter it to join the class

#### PDF Technical Notes
- Use `puppeteer` on the backend to render a dedicated print route (`/print/assignment/{id}`)
  as a PDF
- The print route renders the assignment using the same React components as the student view,
  but in a `@media print`-optimised CSS mode (no colour gradients, clear typography, page breaks
  between questions)
- The cover page is a separate first page, assembled from the teacher's wizard inputs
- Multi-page PDF: cover → questions (with blank answer spaces) → optional answer key (separate
  PDF or second copy, teacher's choice)

### 4.5 Phase 4: Collaborative Student Work (Scaffolded)

**What this delivers:** The data structures and UI shells for collaboration — not full
real-time sync. This phase validates interest before committing to the engineering cost.

#### What is built (scaffolded)
- UI shell for a "Collaborative session" view (shows multiple student inputs side by side)
- "Branch" concept: each student's working is a named branch (e.g., "Lerato's working")
- Comment threads on each branch (stored in Firestore, not real-time yet — reload to refresh)
- "Vote to include" button on each branch section (stored, not live-counted)
- "Merge to main" button for the teacher to promote a branch to the group submission

#### What is NOT built yet
- Real-time WebSocket sync (students see each other's changes live)
- Full branching/diff logic
- Conflict resolution

This deliberately leaves the real-time engine for Phase 5 or later, pending user validation.

### 4.6 Phase 5: Mark Records and Reporting

**What this delivers:** A gradebook covering both app-generated and manually-entered marks.

#### Features
- **Mark book:** table of all students × all assignments, auto-populated from submission results
- **Manual mark entry:** teacher adds a row for non-app work (e.g., "Class test 1: 65%")
  with a description and date
- **Term report export:** aggregates app marks + manual marks per student per subject
  → exports as PDF or CSV
- **Class-level analytics:** average per assignment, per topic, per student — trend charts
- **Collation to school admin:** teacher marks become visible in the school admin dashboard
  once the teacher publishes them (explicit publish step — not automatic)

---

## 5. Admin Mode

### 5.1 RBAC Hierarchy

```
Superadmin (Fundile owner)
    ├── All data, all schools, pricing, global settings
    ├── Can impersonate any user for support purposes
    └── Manages: system announcements, feature flags, billing

School Admin (per subscribed school)
    ├── Registers teachers (staff number or email → invitation)
    ├── Registers students (student number or email → invitation, or bulk CSV)
    ├── Assigns students to teachers / creates classes (flexible naming)
    ├── Views collated marks from all classes
    └── Exports term reports for the school

Teacher (solo or school-assigned)
    ├── Manages their own classes and assignments
    └── Views their own students' results

Student
    └── Practices, submits, views their own results
```

### 5.2 Firebase Auth Custom Claims

```json
// Superadmin
{ "role": "superadmin" }

// School Admin
{ "role": "schooladmin", "schoolId": "jhb-north-high-001" }

// School Teacher
{ "role": "teacher", "schoolId": "jhb-north-high-001", "teacherId": "tch_xyz" }

// Solo Tutor (no schoolId)
{ "role": "teacher", "schoolId": null, "teacherId": "tch_abc" }

// Student
{ "role": "student", "schoolId": "jhb-north-high-001", "studentId": "std_123" }
```

Firestore Security Rules enforce these claims on every read and write.

### 5.3 School Admin Dashboard

```
┌─────────────────────────────────────────────────────┐
│  Johannesburg North High — Admin Dashboard           │
├─────────────────────────────────────────────────────┤
│  Teachers: 12  ·  Students: 340  ·  Active: 287    │
│                                                     │
│  [Manage Teachers]  [Manage Students]  [Classes]   │
│                                                     │
│  Term Overview                                      │
│  Subject       Avg mastery    Sessions this week    │
│  Accounting    72%            1,240                 │
│  Mathematics   58%            980                   │
│  Bus Studies   65%            430                   │
│                                                     │
│  [Export Term Report]  [View Flagged Students]      │
└─────────────────────────────────────────────────────┘
```

### 5.4 Student Registration Options

| Method | Flow |
|---|---|
| **Email invitation** | Admin enters email → system sends invitation with signup link → student completes profile |
| **Student number** | Admin enters number → system creates pending account → student claims it on first login by entering matching number |
| **Bulk CSV upload** | Admin uploads CSV (`studentNumber, email, firstName, surname, grade`) → system creates all accounts and sends invitations |
| **Join code** | Teacher generates a 6-character code → student enters it at signup → linked to teacher's class |

### 5.5 Flexible Class Naming

Class names are free-text strings with no format constraint. Examples:
- `"Grade 10A"`, `"10 Accounting Set 1"`, `"Ms. Nkosi's Maths"`, `"Term 2 Exam Group"`

The class object in Firestore:
```json
{
  "id":        "cls_001",
  "schoolId":  "jhb-north-high-001",
  "teacherId": "tch_xyz",
  "name":      "Grade 10 Accounting A",
  "subject":   "Accounting",
  "grade":     "10",
  "studentIds": ["std_001", "std_002"],
  "createdAt": "2025-01-15T08:00:00Z"
}
```

---

## 6. Notification and Retention System

### 6.1 Notification Types

| Trigger | Channel | Template-driven or LLM? |
|---|---|---|
| Session completed | In-app panel | Template |
| No session in 3 days | Push + email | Template |
| No session in 7 days | Push + email | Template with personalised subject mention |
| Mastery milestone reached | Push | Template |
| Streak at risk (hasn't practiced today) | Push | Template |
| Trial ends in 4 days | Email | Template |
| Trial ends in 1 day | Email | Template — emphasises profile persistence |
| Trial ended | In-app gate | Template |
| Weekly digest | Email | LLM light (3–4 sentences) |

### 6.2 Trial Conversion Sequence

The free trial is the most critical funnel moment. The notification sequence:

```
Day 1  → Welcome email: "Your 2-week trial has started. Here's how to get the most from it."
Day 7  → Progress email: "Halfway through your trial — here's what you've accomplished." (profile data)
Day 10 → Conversion email: "4 days left. Subscribe to keep your progress and your plan."
Day 13 → Urgency email: "1 day left. Your profile and history will be safe — but you'll
                          need a subscription to keep practising."
Day 14 → Hard paywall: student cannot start new sessions. Profile visible. CTA: "Subscribe"
```

### 6.3 Hard Paywall Implementation

At trial end:
- All session-start API calls return `403 TRIAL_EXPIRED` if `trialEndsAt < now` and
  `subscriptionTier === "trial"`
- The frontend detects `403 TRIAL_EXPIRED` and renders the paywall gate instead of the workspace
- The student can still view their profile, session history, and the "What we know about you" panel
- A prominent "Subscribe to continue" CTA links to the pricing page

Profile data is never deleted at trial end. This is the retention hook — the student has invested
time; their record is there waiting for them.

### 6.4 Streak System

- A streak is a consecutive-day count of sessions
- A session counts toward the streak if the student completes at least one question in any mode
- The streak resets at midnight (South African time, UTC+2)
- "Streak at risk" notification is sent at 18:00 if the student hasn't practiced that day and
  their current streak is ≥ 3 days

---

## 7. Curriculum Wiki Integration

The curriculum wiki (`caps-wiki/`) is a developer-curated, static Markdown corpus. It is not
generated by an LLM and cannot be modified by a student or teacher. It is the authoritative
curriculum ground truth for the entire system.

### 7.1 What the Wiki Is Used For (Without an LLM)

| System | How the wiki is used |
|---|---|
| **Generators** | Each generator reads its wiki page to confirm valid subskills, question types, and mark allocations for that topic/grade |
| **Topic guardrail** | Checks the student's request against wiki scope before routing to the LLM |
| **Teacher mode** | When a teacher generates questions, the wiki defines what is valid for a term — no LLM inference |
| **Misconception library** | Every entry cites a `curriculum_reference` from the wiki |
| **Student-facing reports** | The agent cites CAPS topic names using wiki terminology |
| **Student profile** | Mastery subskills are named and structured to match wiki vocabulary |

The wiki is what makes the app's curriculum claims defensible. It is the editorial spine of the
system — not an LLM input, but the document that constrains all LLM inputs.

### 7.2 Wiki File Structure

```
caps-wiki/
  accounting/
    grade10/
      sole_trader.md
      final_accounts.md
      bank_reconciliation.md
    grade11/
      ...
  mathematics/
    grade10/
      algebraic_expressions.md
      trigonometry.md
      ...
  business_studies/
    grade10/
      business_environments.md
      forms_of_ownership.md
      ...
  physical_sciences/
    grade10/
      mechanics.md
      electricity.md
      ...
```

### 7.3 Wiki Page Structure

```markdown
---
subject:   "Accounting"
grade:     "10"
topic:     "Sole Trader"
term:      1
capsRef:   "CAPS Accounting FET Grade 10 p.18"
---

# Sole Trader — Grade 10, Term 1

## Learning Objectives
- Understand the accounting equation
- Record transactions in the Cash Receipts Journal (CRJ) and Cash Payments Journal (CPJ)
- Post from journals to the General Ledger

## Subskills
| Subskill key              | Description                               | Min marks | Max marks |
|---------------------------|-------------------------------------------|-----------|-----------|
| crj_entry                 | Complete a CRJ from source documents      | 8         | 20        |
| cpj_entry                 | Complete a CPJ from source documents      | 8         | 20        |
| general_ledger_posting    | Post from CRJ/CPJ to General Ledger       | 6         | 15        |

## Common Errors (from NSC Examiner Reports)
- Using net amount instead of gross in Bank column
- Omitting VAT analysis column
- Posting to wrong side of ledger

## Question Types Allowed
- table_fill (CRJ, CPJ, General Ledger)
- mcq (identify correct entry)
- short_answer (explain a concept)
```

---

## 8. Package Structure and Pricing

### 8.1 Revised Package Table

| Package | Price | What it includes | Status |
|---|---|---|---|
| ~~Free~~ | ~~R0~~ | **Removed** — replace with trial | Remove all references from landing page (pending approval) |
| **Trial** | R0 for 14 days | Full Standard access, no card required | Phase 1 |
| **Standard** | R150/month | Full learning loop (Scaffold/Practice/Assessment), session files, student profile panel, notifications | Current |
| **Pro** | R299/month | Everything in Standard + live Pro Agent tutor (4-tier hints, teach-back, simulation triggers) | After Layer C complete |
| **School** | Custom (per-student) | Everything in Standard + teacher mode (all phases) + admin dashboard + school-level reporting | After Phase 3 of teacher mode |

### 8.2 School Plan Pricing Approach

Suggested: R50 per student per month (minimum 30 students), billed per term.
Rationale: R50 × 30 students = R1,500/month per school — lower per-student cost than individual
R150 plan, incentivising bulk school adoption. Pricing is negotiable for large schools.

### 8.3 Removing Free Package References

This is a landing page change and **requires explicit owner approval before implementation**.
When approved, the following must be updated:
- Landing page copy and pricing section
- `landingCopy.js` constants
- Any "Free" tier labels in the app
- Test drive / explore copy (already uses "Test Drive" language — confirm this is correct)

---

## 9. LLM Cost Architecture

### 9.1 Model Selection: Gemma 2 / Gemma 3 via Hugging Face

**Recommended model:** `google/gemma-2-9b-it` (instruction-tuned, 9B parameters) for all
standard tasks. For teacher class reports (longer, more complex): `google/gemma-2-27b-it`.

**Why Gemma over Llama for this application:**
- High school content (CAPS curriculum) is well-covered in Gemma's training data, which draws
  from high-quality English educational corpora.
- Gemma 2 9B matches or exceeds Llama 3.1 8B on structured instruction-following tasks —
  exactly what the narrow hint/report prompts require.
- Google-maintained: better alignment with the structured output format instructions used
  in the Pro Agent prompt templates.
- Gemma 3 4B (released 2025) is a strong option for latency-sensitive real-time hints —
  smaller, faster, and still more than capable for CAPS-level content.
- Available on Hugging Face Serverless Inference API at comparable cost to Llama.

### 9.2 Tiered LLM Usage

| Task | Model | When | Cost tier |
|---|---|---|---|
| Session summary panel | None (template) | After every session | Free |
| Tier 1–2 hints (Pro Agent) | None (deterministic) | On every hint request | Free |
| Tier 3 hint (Pro Agent) | Gemma 3 4B via HF | When student requests help | Low |
| Tier 4 hint (Pro Agent) | Gemma 2 9B via HF | On escalation | Low |
| Teach-back evaluation | Gemma 3 4B via HF | After teach-back response | Low |
| Weekly digest (student) | Gemma 2 9B via HF | Weekly, per user | Low |
| Parent PDF report | Gemma 2 9B via HF | Weekly, per linked parent | Low |
| Teacher class PDF report | Gemma 2 27B via HF | On demand, per class | Medium |

### 9.3 Cost Estimate at 1,000 Active Students

```
Agent hint calls (Pro only, ~30% of users):
  300 students × 3 sessions/week × 2 hint calls/session = 1,800 calls/week
  At ~$0.001/call on Gemma 3 4B: $1.80/week = $7/month

Weekly digests:
  1,000 students × 1 digest/week = 4,000/month
  At $0.001/call: $4/month

Parent/teacher PDF reports: ~$10/month

Total estimated LLM cost at 1,000 students: ~$21/month
```

### 9.4 Hugging Face Configuration

- **Endpoint type:** Serverless Inference API (not a dedicated endpoint) — pay per call, no
  always-on cost.
- **Timeout:** 8s for real-time hints (Gemma 3 4B is fast enough); 60s for PDF reports.
- **Fallback:** If HF endpoint unavailable → Pro Agent silently falls back to Tier 2
  (deterministic directional hint). Never surface LLM errors to the student.
- **Output format:** All prompts instruct the model to respond in plain text with no markdown
  formatting, no bullet points unless explicitly requested, and no LaTeX. JSON output is used
  only for the teach-back evaluation call (YES/NO + one sentence).

---

## 10. File Structure

```
caps-ai-backend/
  app/
    services/
      session_file_writer.py      ← NEW: writes .md to Firebase Storage
      student_model.py            ← EXTEND: record_submission, generate_session_summary
      report_generator.py         ← NEW: LLM-backed report generation
      notification_service.py     ← NEW: push + email triggers
      trial_manager.py            ← NEW: trial lifecycle, hard paywall enforcement
    routes/
      session.py                  ← EXTEND: session-end trigger for file writer
      reports.py                  ← NEW: GET /api/reports/{type}
      teacher.py                  ← NEW: teacher mode endpoints
      admin.py                    ← NEW: admin mode endpoints
    knowledge/
      caps-wiki/                  ← EXISTING: extend with new subjects/grades
  scripts/
    bulk_register_students.py     ← NEW: CLI for school admin CSV import

src/
  components/
    workspace/
      shared/
        SessionSummaryPanel.jsx   ← NEW: post-session "what we know" panel
    teacher/
      TeacherDashboard.jsx        ← NEW
      QuestionEditor.jsx          ← NEW
      AssignmentBuilder.jsx       ← NEW
      ClassManager.jsx            ← NEW
      MarkBook.jsx                ← NEW (Phase 5)
      CollabShell.jsx             ← NEW (Phase 4, scaffolded)
    admin/
      SchoolAdminDashboard.jsx    ← NEW
      TeacherManager.jsx          ← NEW
      StudentManager.jsx          ← NEW
      ReportCollator.jsx          ← NEW (Phase 5)
    ui/
      Paywall.jsx                 ← NEW: hard paywall gate
      NotificationBanner.jsx      ← NEW: in-app notifications
      TrialCountdown.jsx          ← NEW: trial remaining days banner
  app/
    hooks/
      useStudentProfile.js        ← NEW: reads and subscribes to Firestore profile
      useTrialStatus.js           ← NEW: computes trial state from profile
```

---

## 11. Implementation Phases (Layer D)

### Phase D1 — Session Files and Profile Foundation
1. Extend `student_model.py` with `record_submission()` (real-time Firestore writes).
2. Build `session_file_writer.py` and connect to the session-end event.
3. Build `useStudentProfile.js` hook (Firestore listener).
4. Build `SessionSummaryPanel.jsx` (template-driven, no LLM).
5. Test: complete a session → verify `.md` file written correctly → verify Firestore profile
   updated → verify summary panel shows correct data.

### Phase D2 — Trial, Paywall, and Packaging
6. Build `trial_manager.py` and the `trialEndsAt` field on the profile.
7. Build `Paywall.jsx` and `TrialCountdown.jsx`.
8. Implement `403 TRIAL_EXPIRED` in session-start API.
9. Build `notification_service.py` with the Day 7, 10, 13, 14 email triggers.
10. Remove free package references from the landing page **after owner approval**.

### Phase D3 — LLM Reports and Digests
11. Build `report_generator.py` with Hugging Face managed endpoint integration.
12. Implement weekly digest email (student-facing).
13. Implement parent report (if parent linked to account).
14. Test report quality: does the LLM accurately reflect profile data without hallucinating?

### Phase D4 — Teacher Mode Phase 1 (Question Generation MVP)
15. Build teacher RBAC (Firebase custom claims, solo tutor path).
16. Build `TeacherDashboard.jsx` and `QuestionEditor.jsx`.
17. Build `AssignmentBuilder.jsx` — assemble questions, set due date, push to class.
18. Build `ClassManager.jsx` — create class, join code, add students.
19. Build `teacher.py` routes.
20. Test end-to-end: teacher generates → edits → assigns → student completes → teacher sees result.

### Phase D5 — Teacher Mode Phase 2 (Marking Points)
21. Implement highlight-to-marking-point UI using `Selection` API.
22. Implement teacher mark override with comment.
23. Extend auto-marker to include teacher-defined marking points.

### Phase D6 — Teacher Mode Phase 3 (Assignment Management + PDF)
24. Implement reveal toggle and due date enforcement.
25. Implement Puppeteer PDF generation on backend.
26. Build cover page wizard.

### Phase D7 — Admin Mode
27. Build `SchoolAdminDashboard.jsx`.
28. Build teacher/student registration flows (email + number, bulk CSV).
29. Build Firestore Security Rules for full RBAC hierarchy.
30. Build collation and term report export.

### Phase D8 — Notification System
31. Implement push notification service (Firebase Cloud Messaging).
32. Implement streak tracking and streak-at-risk notification.
33. Implement mastery milestone notifications.

### Phase D9 — Collaborative Work (Scaffolded)
34. Build `CollabShell.jsx` with branch UI, comment threads, vote buttons.
35. Store branches and votes in Firestore (no real-time sync yet).
36. Teacher "Merge to main" function.

---

## 12. Marking Correctness Rules (All Archetypes)

These rules apply universally to every archetype, every subject, every grade.

### 12.1 Empty Cell Rule

**An empty cell never earns a mark. Filling a cell that should be empty earns a deduction.**

The generator classifies every cell in every table as one of:
- `required` — the student must fill this in; correct value earns the mark
- `given` — pre-filled in the question; the student cannot edit it; no mark attached
- `must_be_empty` — the cell should be left blank in the correct answer

Marking logic:

```python
def mark_cell(cell: Cell, student_value: Any) -> CellMark:
    if cell.cell_type == "given":
        return CellMark(marks=0, status="given")  # never marked

    if cell.cell_type == "must_be_empty":
        if student_value is None or student_value == "":
            return CellMark(marks=0, status="correct_empty")  # correct, but 0 marks
        else:
            return CellMark(marks=-1, status="incorrect_filled",
                            note="This cell should be left blank")

    if cell.cell_type == "required":
        if student_value is None or student_value == "":
            return CellMark(marks=0, status="omitted")
        elif is_correct(student_value, cell.expected_value, cell.tolerance):
            return CellMark(marks=cell.marks, status="correct")
        else:
            return CellMark(marks=0, status="wrong")
```

The total score is `sum(mark.marks for mark in cell_marks)`, clamped at 0 (a student cannot
score negative overall, but deductions reduce positive marks earned from correct cells).

### 12.2 Archetype Marking Criteria

Every archetype definition (in the generator and in the wiki) must include a `marking_schema`
block. This block is the single source of truth for what earns marks, stored with the question
and included in the session `.md` file:

```json
{
  "archetype": "crj_entry",
  "marking_schema": {
    "total_marks": 12,
    "marking_points": [
      { "id": "mp1", "description": "Correct date in each row",
        "cells": [{"col": "Day"}], "marks_per_cell": 1, "max_marks": 3 },
      { "id": "mp2", "description": "Correct Bank amount (gross, including VAT)",
        "cells": [{"col": "Bank"}], "marks_per_cell": 2, "max_marks": 6 },
      { "id": "mp3", "description": "Correct analysis column amounts",
        "cells": [{"col": "Sales"}, {"col": "VAT"}], "marks_per_cell": 1, "max_marks": 3 }
    ],
    "deductions": [
      { "rule": "must_be_empty_filled", "deduction_per_cell": -1 }
    ],
    "carry_forward_rule": "If Bank is wrong but analysis columns sum to student's Bank value,
                           award analysis column marks (method marks)"
  }
}
```

This schema is:
- **Reproducible:** the same seed and archetype always produce the same schema
- **Scalable:** adding a new archetype requires only defining its `marking_schema` — the
  marking engine applies it automatically
- **Transparent:** included in the session file so any dispute can be resolved by inspection
- **NSC-aligned:** carry-forward (method mark) logic is included, matching real exam marking

---

## 13. Dashboard Design Requirements

All user dashboards must be designed with the full data pipeline in mind from the start.
Building a dashboard that cannot display profile data, session history, or trajectory charts
without a redesign later is not acceptable.

### 13.1 Student Dashboard Requirements

| Panel | Data source | Phase available |
|---|---|---|
| Profile picture + name + grade | Firestore profile | Phase D1 |
| Current streak + session count | Firestore profile | Phase D1 |
| "What we know about you" summary | Firestore profile (template) | Phase D1 |
| Mastery by subject (progress bars) | Firestore mastery map | Phase D1 |
| Error pattern history | Firestore errorPatterns | Phase D1 |
| Trajectory chart (mastery over time) | Firestore progressTrajectory | Phase D1 |
| Trial countdown / subscription status | Firestore trialEndsAt | Phase D2 |
| Notification centre | notification_service | Phase D8 |
| SimuLearn access (simulation trigger) | Simulation system | Layer B |
| Pro Agent tutor access | Pro Agent | Layer C |

### 13.2 Teacher Dashboard Requirements

| Panel | Data source | Phase available |
|---|---|---|
| Profile picture + name | Firestore profile | Phase D4 |
| Class list with student counts | Firestore classes | Phase D4 |
| Assignment status (submitted/pending) | Firestore assignments | Phase D4 |
| Per-student mastery overview | Firestore student profiles | Phase D4 |
| Flagged students (below threshold) | Firestore mastery map | Phase D4 |
| Class PDF report generator | report_generator.py | Phase D5 |
| Mark book | Firestore marks | Phase D6 |

### 13.3 SimuLearn Branding on Dashboards

The simulation feature is branded as **SimuLearn** throughout the UI. It appears on the student
dashboard as a distinct entry point — not buried in the workspace. The marketing rationale:

> *SimuLearn is a data-light tutoring tool — each simulation is a pre-generated animation script,
> not a video stream. On a typical mobile connection, a SimuLearn session uses less than 50 KB.
> In a market where data costs are a real barrier to education, SimuLearn is a genuine
> differentiator: full worked-example tutoring at near-zero data cost.*

The dashboard SimuLearn entry point shows:
- Subjects and topics the student has started practising
- Which archetypes have a SimuLearn worked example available
- Which archetypes the student has already watched (with a "Watch again" option)

---

## 14. Open Questions (Resolve Before Phase D1)

1. **Session file trigger on mobile / unexpected close:** If the student closes the browser tab
   mid-session, the session-end event may not fire. Use `beforeunload` + a server-side
   session-expiry heartbeat to detect abandoned sessions and write a partial `.md` file with
   status `"abandoned"`. Decide: do abandoned sessions count toward the student model?

2. **Parent account linking:** How does a parent link to a student's account? Options:
   - Student generates a "parent code" in their profile → parent enters it at signup
   - Parent enters student's email → student approves the link
   Decide before building `report_generator.py` parent report path.

3. **Notification opt-out:** POPIA requires students (or guardians, for under-18s) to be able to
   opt out of marketing communications. Email digests and trial conversion emails are arguably
   marketing. Build an opt-out mechanism before the notification system ships.

4. **School plan contracts:** The school plan is sold at custom pricing. Is there an in-app
   subscription flow for schools, or is it handled manually (invoice + admin activation)?
   If manual, the superadmin dashboard needs an "Activate school subscription" function.

5. **Collaboration real-time sync threshold:** At what point (user count, session count) does
   the scaffolded collaboration phase get upgraded to full WebSocket real-time sync?
   Set a measurable threshold (e.g., "when 3 teachers request real-time collaboration in the
   same term") before committing to the engineering cost.

6. **PDF report privacy (teacher access):** Teachers receive a PDF derived from student session
   data. Raw `.md` files are never shared with teachers directly — only the agent-generated PDF.
   Confirm this distinction is disclosed in the privacy statement before Phase D3.

7. **Streak timezone:** Confirm the system uses `Africa/Johannesburg` (UTC+2) for streak
   midnight resets and trial expiry calculations — not UTC.

8. **Profile picture moderation:** User-uploaded profile pictures require basic content
   moderation (no inappropriate images). Options: Firebase Extensions (Google Vision API
   content moderation trigger on Storage upload) or manual review for schools. Decide before
   Phase D1 if profile pictures ship in Phase D1.

---

## 15. Phase E — Gamification, 4-Tier Badges, ProgressMap & ChallengeGate (Completed)

### 15.1 Core Architecture Status: Built
- **Backend Gamification Engine**: `caps-ai-backend/app/services/gamification_service.py`
  - Four-tier hierarchy: Subskill Pin ($\ge 80\%$), Topic Medal (Bronze 60%, Silver 80%, Gold 95%), Term Trophy (4+ Silver/Gold topic medals in term), Subject Medallion (full-grade completion).
  - Ungameable XP: Awarded strictly on first-mastery only, zero decay, capped daily streak bonuses.
- **Backend Challenge Engine**: `caps-ai-backend/app/services/challenge_generator.py`
  - Fixed canonical challenge seeds for standardized milestone tests.
  - Generates CAPS curriculum DAG skill tree nodes across Terms 1–4.
- **Frontend Components**:
  - `src/components/gamification/BadgeCard.jsx`: Metallic glowing badge card with locked/unlocked animations.
  - `src/components/gamification/XPProgressBar.jsx`: Circular progress ring with ungameable XP counter and streak indicator.
  - `src/components/gamification/GamificationSummary.jsx`: Trophy room modal with tier filtering.
  - `src/components/gamification/ProgressMap.jsx`: Dynamic visual curriculum skill tree with connecting strokes and action popovers.
  - `src/components/gamification/ChallengeGate.jsx`: Standardized assessment exam gate with countdown timer and zero-hint enforcement.
  - `src/components/gamification/ChallengeResultCard.jsx`: Credential award celebration card.
  - Integrated into `src/views/StudentWorkspaceView.jsx` with 1-tap mode switching.

