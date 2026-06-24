# Implementation Plan 2 — Landing Page Revamp + CAPS/NSC Positioning

## 1. The problem
The current `src/components/ui/LandingPage.jsx` (694 lines) is generic: value cards,
feature cards, audience cards, a demand-capture form. It does not convey the *vision*
or convert. The vision (your words, distilled):

> A 21st-century / intelligence-age **student's companion** — every subject in one
> platform, one affordable monthly payment (vs the cost of private tutors). A space
> where **teachers, tutors and students collaborate**, review work and complete tasks
> flexibly, any time. An **unlimited** practice + exam-prep resource. **Exam-level prep
> from day one** — no hidden-curriculum burden; learners are never surprised by an exam.

Plus a positioning challenge around examining bodies (Section 4).

## 2. Narrative spine (what the page should say, in order)
1. **Hero — one bold promise.** e.g. *"Exam-ready from day one. Every subject. One
   companion."* Sub: *"All your subjects, unlimited practice, and exam-level questions —
   for less than one hour of private tutoring a month."* Primary CTA: **Start free** ·
   Secondary: **See how it works**.
2. **The problem we remove ("the hidden curriculum").** Learners are surprised by exams
   because day-to-day work rarely looks like the exam. We close that gap: exam-standard
   questions, transparent mastery, no surprises.
3. **How it works (3 steps).** Pick a topic → guided Scaffold → Practice → exam-style
   Assessment, with an AI tutor that shows you *where* you went wrong (ties to Plan 1).
4. **The CAPS / NSC clarity section.** (Section 4 — the centrepiece for trust.)
5. **For students / For teachers & tutors / For parents.** Tri-fold with a CTA each;
   surface the collaboration features (assign, review work, complete tasks, flexible timing).
6. **Pricing anchor.** One subscription, all subjects, vs tutoring cost.
7. **Proof.** Research index (already present) + alignment/credibility badges.
8. **FAQ** — explicitly answers the examining-bodies myth (Section 4).
9. **Final CTA** + keep `DemandCaptureForm` as waitlist.

## 3. Affordability framing
Anchor against the real alternative: private tutoring is roughly **R200–R450/hour** in
SA. One monthly subscription < one tutoring hour, covering **all subjects, unlimited**.
Lead with the comparison visually (a simple "tutor vs companion" cost bar).
*(Insert your actual price; placeholder until you confirm.)*

## 4. CAPS vs DBE/IEB/SACAI — how to message it (the hard part)
**The misconception to dissolve:** many parents believe IEB/SACAI are "superior" and
teach a *different curriculum* from "CAPS/DBE".

**The accurate frame (verify exact wording with your compliance/marketing before publishing):**
- **CAPS** (Curriculum and Assessment Policy Statement) is the **single national
  curriculum**. It is *what* must be learned.
- The **NSC** (National Senior Certificate) is the **qualification** at the end of Grade 12.
- **DBE, IEB and SACAI are all assessment bodies that examine the NSC against CAPS**, and
  **all are quality-assured by Umalusi** (the same standards body). They differ in
  *assessment style, school-based assessment, and emphasis* — **not in the underlying
  curriculum**.
- Therefore: *"The difference is not the curriculum — it's the preparation."*

**Messaging do's:**
- State plainly: **"Built on CAPS — the national curriculum all three examining bodies
  (DBE, IEB, SACAI) follow — and tuned to the exam standard of each."**
- Validate the parent's instinct (they care about quality) and redirect it: the lever
  that actually moves results is **exam-level preparation**, which we give every learner.
- Use a simple diagram: **CAPS (foundation)** → **DBE · IEB · SACAI (exam styles)** →
  **one NSC qualification**.
- A short comparison table: rows = Curriculum, Qualification, Quality assurance
  (Umalusi), What differs. Columns = DBE / IEB / SACAI. The first three rows are
  identical across columns (that's the whole point); only "what differs" varies.

**Messaging don'ts:**
- Don't disparage any body or claim one is "easier/harder".
- Don't claim we *are* affiliated with or endorsed by DBE/IEB/SACAI/Umalusi — only that
  we **align to CAPS and prepare for the NSC**.
- Treat exam-body claims as **legally sensitive**: you (or a reviewer) should sign off
  on the final copy.

## 5. Implementation approach
- Refactor `LandingPage.jsx` into composed section components under
  `src/components/ui/landing/`: `Hero`, `HiddenCurriculum`, `HowItWorks`, `CapsNscClarity`,
  `Audiences`, `Pricing`, `Proof`, `Faq`, `FinalCta`. Keeps each file small (Rule 4) and
  the page readable.
- Move all marketing copy into a single constants module
  (`src/app/constants/landingCopy.js`) so wording (especially the CAPS/NSC section) can be
  edited/approved without touching layout.
- Preserve the existing `palette` (light/dark) system and `DemandCaptureForm`.
- Add an `CapsNscDiagram` (lightweight SVG) and a responsive comparison table.
- No backend change required.

## 5b. LOCKED decisions (from user)
- **Pricing:** Standard (no/limited agent) = **R150/month**; Pro (full agentic) =
  **R299/month** (promo likely on Pro). Anchor: tutors charge **R50–R200/hour**; even at the
  low end, 3 sessions/week ≈ R150 × 4 weeks = R600+/month — and Fundile is available anytime.
- **Teacher/tutor collaboration:** NOT shippable this round → market as **"coming soon"**;
  full implementation targeted for the next shipping (user will provide a teacher-mode spec
  after the current task).
- **Exam-body copy — stick to what the bodies themselves publish:**
  - **SACAI:** "a private assessment body accredited by Umalusi to assess the National
    Senior Certificate (NSC) and GETC: ABET." Assessment bodies conduct national external
    exams and quality-assure internal assessment.
  - **CAPS:** "policy documents that outline the aims, scope, content and assessment
    requirements for each subject in the National Curriculum Statement Grades R–12."
  - **IEB:** does **not** mention CAPS by name (strategic). They say: "Umalusi-accredited
    examinations in all subjects recognised in the NSC… The IEB NSC is internationally
    benchmarked and equivalent to Cambridge AS level. The IEB uses the South African
    National Curriculum which is regulated by the Department of Basic Education."
  - **Safe framing for the page:** *"Built on the CAPS curriculum — the South African
    National Curriculum behind the NSC — Fundile prepares you for your NSC exams whether
    they're set by the DBE, IEB or SACAI."* (All three are Umalusi-accredited NSC assessment
    bodies; IEB itself states it uses the SA National Curriculum regulated by the DBE.)
  - Do not name CAPS *for* the IEB; instead point to their own wording ("SA National
    Curriculum regulated by the DBE"). Never imply endorsement by any body.

## 6. Open questions
1. Confirm the **price point** (and whether there's a free tier / trial) so the anchor is real.
2. Are **teacher/tutor collaboration** features (assign, review, tasks) shippable enough
   to advertise now, or do we market them as "coming soon"?
3. Who signs off the **CAPS/NSC/examining-body copy**? (Recommended before publish.)
4. Tone: aspirational ("intelligence-age companion") vs concrete ("pass your exams") —
   or hero = aspirational, body = concrete? My recommendation is the latter.
