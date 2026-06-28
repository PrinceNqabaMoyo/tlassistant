# Implementation Plan 1 — Procedure / Working Tracker

## 1. The idea (restated)
Track the **steps a learner takes** while solving a question, then review that step
sequence *together with* their working and final answer so the system can pinpoint
**exactly where they went wrong** — not just "right/wrong" on the final answer.

This is genuinely high value and, importantly, it mirrors how **NSC/CAPS maths and
science are actually marked**: examiners award *method marks* (M), *accuracy marks*
(A), and *consistent-accuracy* marks. A learner can:
- get the right answer with a flawed method (loses method marks),
- use the right method but make an arithmetic slip (loses one accuracy mark, keeps the rest via "carry-over"),
- go wrong at step 3 but be marked correct for steps 4–6 *relative to their step-3 value*.

A pure final-answer checker cannot do any of this. A procedure tracker can. **This is
a strong differentiator and a real selling point** (transparent, exam-style marking).

## 2. One agent or a new one?
**Recommendation: keep ONE orchestrator agent (per AGENTS.md Rule 9) and add a new
TOOL**, not a second agent. The tracker is mostly a deterministic subsystem; the agent
only narrates *why* a step is wrong.

- New backend service: `app/services/procedure_tracker.py`
- New orchestrator tool: `diagnose_procedure(question_id, student_steps, final_answer)`
- The agent calls it, receives a structured diagnosis, and turns it into a short
  Socratic explanation. The agent never invents the diagnosis itself.

## 3. Capture: how steps get recorded
Two layers, in order of fidelity:

1. **Structured "Working Pad" (primary, deterministic-friendly).**
   A vertical, line-by-line working area (this also satisfies the maths doc comment:
   *"All working … should be vertical, the same way a user would arrange it on paper"*).
   Each line is a discrete entry the learner types via the maths keypad. Each step
   optionally tagged with the operation claimed (e.g. "expand", "divide both sides").
   This is shared with Plan 3 (it IS the maths answer surface).

2. **Free-form / drawn working (later).**
   Canvas or photo of handwritten working → OCR/diagram-spec extraction. Much harder;
   explicitly a phase-2 stretch goal, not in the first slice.

Each captured step is stored as:
```json
{ "index": 2, "latex": "2x = 8", "claimed_op": "subtract 2 both sides",
  "ts": 1699999999 }
```

## 4. Diagnosis pipeline (the core)
Generators must emit a **canonical solution graph** alongside each question (this is new
work in the generators — see Plan 3). Shape:
```json
{
  "goal": "solve for x",
  "steps": [
    {"from": "2x + 2 = 10", "op": "subtract 2", "to": "2x = 8",
     "rule": "additive inverse", "common_errors": ["sign_error", "moved_only_one_side"]},
    {"from": "2x = 8", "op": "divide by 2", "to": "x = 4",
     "rule": "multiplicative inverse", "common_errors": ["divide_only_one_term"]}
  ],
  "final": "x = 4"
}
```

**Standard tier (deterministic only):**
- For each learner step, check **symbolic equivalence to the previous line** using
  `sympy` (e.g. `2x+2=10` and `2x=8` are equivalent equations; `x=4` satisfies it).
- Classify the first break:
  - equivalence holds + moves toward goal → `correct`
  - equivalence holds but no progress → `valid_but_stuck`
  - equivalence breaks → `error` (sub-classify: sign error, arithmetic slip,
    invalid operation, dropped term, etc. via the canonical `common_errors` + simple checks)
- Output: per-step status array, **first error index**, error label, and
  carry-over-aware final mark (method marks + accuracy marks).
- No LLM. Fully reproducible.

**Pro tier (adds the agent):**
- Feed the agent: `{canonical steps, student steps, first_divergence_index,
  matched misconception_tags}`.
- Agent returns a short Socratic explanation pinned to the exact step
  ("Look at line 3 — what happened to the sign when you moved the 2?") and can call the
  generator (Rule 14) for an isomorphic variant targeting that misconception.

## 5. Marking model (method + accuracy)
Return a breakdown, not a single number:
```json
{ "final_answer_correct": false,
  "method_score": 0.8, "accuracy_score": 0.5,
  "first_error_step": 3, "error_type": "sign_error",
  "marks": {"M": 2, "A": 1, "CA": 1, "max": 5} }
```
This feeds the shared `StudentModel` (`record_attempt` per subskill, `record_struggle`
with the specific misconception tag) so adaptive progression can target the *exact*
weakness.

## 6. Where it plugs into existing code
- `app/services/procedure_tracker.py` — new deterministic engine (sympy).
- `app/services/orchestrator_service.py` — register `diagnose_procedure` tool.
- `app/services/student_model.py` — already has `record_attempt` / `record_struggle`;
  extend payload with `error_type` + `step_index`.
- Generators — emit `canonical_solution` graph (Plan 3).
- Frontend — `WorkingPad.jsx` (vertical step entry + keypad) + a per-step status gutter
  (tick / warning / cross) and an "Explain step" affordance (Pro).

## 7. Tier summary
| | Standard | Pro |
|---|---|---|
| Step capture | yes (Working Pad) | yes |
| Per-step equivalence check | yes (sympy) | yes |
| Error localisation + label | yes (rule-based) | yes |
| Method/accuracy marks | yes | yes |
| Socratic "why" explanation | no (static hint only) | yes (agent) |
| Targeted variant on the weak step | no | yes (generator tool) |

## 8. Open questions
1. First subject for the tracker: **maths** (best fit; couples with Plan 3) — agreed?
2. Do we want method/accuracy ("M/A/CA") marks surfaced to learners from day one, or
   start with simple "first wrong step" highlighting and add mark breakdown later?
3. Free-form/handwritten capture — confirm it's phase 2 (structured Working Pad first).
