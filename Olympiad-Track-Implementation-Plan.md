# Olympiad Track — Implementation Plan

> **Status:** Planned. Implement after the gamification system (Phase D10) is stable.
>
> **Dependency:** CAPS Mathematics generators (Grade 10+) must be live. The olympiad track
> gates entry behind CAPS topic badge achievement, so the badge system (§15 of
> `Complete-App-Implementation-Plan.md`) must also be functional.

---

## 0. Philosophy and Scope

### Why an Olympiad Track?

The CAPS curriculum covers what every South African student must know. The Olympiad track
covers what the most mathematically curious students *can* explore beyond the curriculum.
It is a **stretch layer**, not a replacement for CAPS practice.

No comparable SA edtech product provides structured olympiad preparation. This is a genuine
differentiator — particularly in a market where students who want to prepare for SAMO or
similar competitions currently have no structured digital resource.

### Scope Decision: SAMO First, IMO Later

| Competition | Scope decision | Rationale |
|---|---|---|
| **SA Mathematics Olympiad (SAMO) Junior Round 1** | In scope — Phase O1 | MCQ + short answer, fully auto-markable, Grade 8–9 accessible |
| **SAMO Senior Round 1** | In scope — Phase O1 | MCQ + short answer, Grade 10–12, aligns with existing user base |
| **SAMO Round 2 (structured proofs)** | Partial — Phase O2 | SimuLearn worked examples for technique; proof comprehension MCQs |
| **SAMO Open (invitation-only proofs)** | Deferred | Requires human marking; out of scope for automated system |
| **AMC 8 / AMC 10 style** | In scope — Phase O1 | Pattern-based MCQ, fully generatable, internationally recognised |
| **IMO problems** | Deferred | Open-ended creative proofs — auto-marking not feasible at this level |

### Target User

A student who has achieved **Silver or Gold** Topic Badges in the relevant CAPS Mathematics
topics. The olympiad track is explicitly positioned as the next challenge for students who
have mastered the curriculum, not an alternative to it.

---

## 1. CAPS Mastery Gate

Access to olympiad problem sets is gated behind CAPS achievement. The gate is per-problem-area:

| Olympiad area | CAPS gate (Silver or Gold badge required in any of these topics) |
|---|---|
| Algebra problems | Algebraic Expressions, Equations & Inequalities |
| Number theory | Algebraic Expressions, Patterns (Grade 9) |
| Geometry | Euclidean Geometry, Trigonometry |
| Combinatorics | Probability, Statistics |
| Inequalities | Algebraic Expressions, Equations & Inequalities |
| Mixed (SAMO Round 1 full paper) | >= 3 topic Silver/Gold badges in Mathematics |

This gate is both an academic quality filter (olympiad problems assume curriculum fluency)
and a retention mechanic (CAPS achievement unlocks something aspirational).

The ProgressMap on the student dashboard shows the olympiad track as a separate "advanced"
cluster, greyed out with lock icons until the CAPS gate is met.

---

## 2. Olympiad Problem Architecture

### 2.1 What Makes Olympiad Problems Different

CAPS generators produce questions with a known, reproducible correct answer derivable by
applying a defined procedure. Olympiad problems at Round 1 level are similar — they have
definite correct answers, and at the MCQ level they are auto-markable. The difference is:

- **No single taught procedure:** The student must select the right technique from a wider
  repertoire (substitution, parity argument, modular arithmetic, geometric insight, etc.).
- **Higher cognitive demand:** Problems require multiple steps with no scaffolding.
- **Technique vocabulary:** Students need familiarity with olympiad-specific techniques
  (e.g. AM-GM inequality, Pigeonhole principle, Vieta's formulas) before solving novel problems.

This means the olympiad system needs two components:

1. **Technique Library:** SimuLearn-style worked examples for each olympiad technique.
2. **Practice Problem Sets:** Seeded, deterministic problems at increasing difficulty.

### 2.2 Generator Architecture for SAMO Round 1

SAMO Round 1 problems follow identifiable archetypes (number patterns, digit problems,
combinatorial counting, geometric ratios). These can be generated deterministically with
seeded generators, exactly like CAPS generators.

```
caps-ai-backend/app/utils/
  olympiad/
    _olympiad_common.py           <- Shared utilities (modular arithmetic helpers,
                                     combinatorial functions, geometric ratio checks)
    junior/
      number_patterns.py          <- SAMO Junior-style number sequence problems
      digit_arithmetic.py         <- Sum-of-digits, digit reversal problems
      basic_combinatorics.py      <- Counting arrangements, simple probability
      basic_geometry.py           <- Area ratios, similar triangle problems
    senior/
      algebraic_manipulations.py  <- Factorisation, substitution, Vieta's formulas
      number_theory_sr.py         <- Divisibility, congruences, mod arithmetic
      geometric_proofs.py         <- Circle theorems, concyclic points (MCQ/short answer only)
      inequality_basics.py        <- AM-GM, Cauchy-Schwarz at introductory level
      combinatorics_sr.py         <- Inclusion-exclusion, pigeonhole
    amcstyle/
      amc8_arithmetic.py          <- AMC 8 style arithmetic/logic problems
      amc10_algebra.py            <- AMC 10 style algebra and number theory
```

Each generator follows the same contract as CAPS generators:
- `generate(seed: int) -> OlympiadQuestion`
- Returns: question text, answer choices (MCQ) or expected value (short answer),
  worked solution graph (step-by-step), technique tags, difficulty rating (1-5)
- Same seed -> identical question, every time

### 2.3 Difficulty Progression

| Level | Description | SAMO equivalent |
|---|---|---|
| 1 | Straightforward application of one technique | Round 1, Q1-5 |
| 2 | One technique with a twist | Round 1, Q6-10 |
| 3 | Combine two techniques | Round 1, Q11-15 |
| 4 | Non-obvious technique selection | Round 2, Q1-2 |
| 5 | Multi-step creative proof (comprehension MCQs only) | Round 2, Q3-5 |

The student workspace auto-advances difficulty: start at Level 1, unlock Level 2 after
3 correct at Level 1, and so on — same progression logic as Scaffold to Practice to Assessment.

---

## 3. Technique Library (Olympiad SimuLearn)

For each major olympiad technique, there is a SimuLearn-style worked example — a pre-generated,
canonical animation showing exactly how the technique is applied to a clean example problem.

### 3.1 Technique Registry

```python
# caps-ai-backend/app/utils/olympiad/technique_registry.py

OLYMPIAD_TECHNIQUES = {
    "am_gm_inequality": {
        "name": "AM-GM Inequality",
        "description": "For non-negative reals, the arithmetic mean is >= the geometric mean.",
        "applicable_to": ["inequalities", "optimisation"],
        "example_seed": 42,
        "generator": "senior.inequality_basics",
        "simulearn_script": "techniques/am_gm.json"
    },
    "pigeonhole": {
        "name": "Pigeonhole Principle",
        "description": "If n items fill k containers and n > k, at least one container "
                       "holds more than one item.",
        "applicable_to": ["combinatorics", "number_theory"],
        "example_seed": 17,
        "generator": "senior.combinatorics_sr",
        "simulearn_script": "techniques/pigeonhole.json"
    },
    "modular_arithmetic":   { "...": "..." },
    "vieta_formulas":       { "...": "..." },
    "parity_argument":      { "...": "..." },
    "dirichlet_principle":  { "...": "..." },
    # Junior techniques
    "digit_sum_trick":      { "...": "..." },
    "systematic_listing":   { "...": "..." },
    "working_backwards":    { "...": "..." },
}
```

### 3.2 How the Technique Library Is Presented

The student enters the Technique Library from the olympiad dashboard. It presents as a
skill tree — techniques grouped (Algebra, Number Theory, Geometry, Combinatorics), each
either locked, available, or mastered.

A technique becomes **available** when:
- The relevant CAPS area badge is earned (gate), OR
- A lower-level technique in the same group is mastered (progressive unlock)

A technique is **mastered** when the student has correctly solved 3 problems tagged with
that technique at difficulty >= 2.

Each technique page shows:
1. Plain-English explanation (2-3 sentences)
2. A SimuLearn worked example showing the technique applied step-by-step
3. A "Try a problem using this technique" button — launches the generator at Level 1
   filtered to problems tagged with this technique

---

## 4. Olympiad Badge System

Olympiad badges are **visually distinct** from CAPS badges — deep indigo/violet tones vs
the gold/silver/bronze of CAPS, and geometric star/compass iconography vs subject icons.

### 4.1 Olympiad Badge Types

| Badge | Earn condition |
|---|---|
| **Technique Badge** | Master a specific olympiad technique (3 correct at difficulty >= 2) |
| **Problem Set Badge** | Complete an area's Level 1-3 problems with >= 60% overall |
| **Junior Round 1 Qualifier** | Score >= 60% on the simulated SAMO Junior Round 1 (seeded) |
| **Senior Round 1 Qualifier** | Score >= 60% on the simulated SAMO Senior Round 1 (seeded) |
| **Olympiad Medal** | Gold/Silver/Bronze by Round 1 score: >=90% / >=75% / >=60% |

The Round 1 Qualifier simulations are full 20-question papers, seeded and fixed, modelled
on the actual SAMO Round 1 format (120 minutes suggested duration shown as reference —
not enforced as a hard timer at this stage).

### 4.2 Olympiad Leaderboard

The Olympiad track includes the **only leaderboard in the app**. Justification:
- Olympiad culture is explicitly competitive — rankings are the point
- The leaderboard is **opt-in** (students choose a display name, not their real name)
- It is scoped to the olympiad track only — CAPS performance is never ranked publicly
- POPIA compliance: no real names, no school names, no identifying information displayed

Leaderboard dimensions:
- National (all opt-in students) — top 100 by Round 1 simulation score
- By grade level (Junior / Senior)
- By problem area (top solvers in Algebra, Number Theory, etc.)

The leaderboard refreshes weekly. A student's personal best score determines their ranking.

---

## 5. Frontend Components

```
src/components/
  olympiad/
    OlympiadDashboard.jsx      <- Entry point, CAPS gate status, technique tree,
                                  problem sets, leaderboard link
    TechniqueLibrary.jsx       <- Skill tree of olympiad techniques
    TechniquePage.jsx          <- Technique explanation + SimuLearn + practice CTA
    OlympiadWorkspace.jsx      <- Problem workspace (hint-free by design)
    OlympiadResultCard.jsx     <- Post-problem result with technique reinforcement
    RoundSimulation.jsx        <- Full SAMO Round 1 simulation (exam layout)
    OlympiadBadgeGallery.jsx   <- Olympiad-specific badge display
    Leaderboard.jsx            <- Opt-in national/grade leaderboard
    OlympiadProgressMap.jsx    <- Visual map of olympiad areas and technique mastery
```

### 5.1 Olympiad Workspace Differences from CAPS Workspace

| Feature | CAPS Workspace | Olympiad Workspace |
|---|---|---|
| Hints | 4-tier hint system (Pro Agent) | **None** — olympiad is hint-free by design |
| SimuLearn | Available on request | Technique Library only, not mid-problem |
| Scaffold mode | Yes | No — all problems are assessment-mode difficulty |
| Working pad | Yes (KaTeX) | Yes — same component |
| Timer | No (suggested duration only) | Suggested duration shown; no enforcement |
| MCQ | Sometimes | Always for Round 1 simulation |

---

## 6. Marking Architecture

### 6.1 Auto-Markable Problems (Round 1, Level 1-3)

**MCQ:** Compare selected option to correct option. Straightforward.

**Short answer (numeric/algebraic):** Use the same SymPy-equivalence check as CAPS
mathematics markers. The student enters a number or simple expression; the system
evaluates symbolic equality. Tolerance: exact for integers; 0.001 for decimal answers.

### 6.2 Round 2 Proof Problems (Level 4-5)

These cannot be auto-marked. Solution: provide a **SimuLearn proof walkthrough** for the
canonical solution. The student reads the worked proof, then answers comprehension MCQs
about it ("Which lemma was used in Step 3?" / "Why does this inequality hold?"). The MCQs
are auto-markable and test genuine understanding of the proof technique, not memorisation
of the answer.

Teacher/manual marking (School plan only) is deferred to a later phase.

---

## 7. Firestore Data Model

```
students/{userId}/
  olympiad: {
    gateUnlockedAt:    timestamp | null,
    optInLeaderboard:  boolean,
    leaderboardAlias:  string | null,

    techniques: {
      "{techniqueKey}": {
        unlocked:           boolean,
        mastered:           boolean,
        correctAtLevel2Plus: number,
        lastPracticed:      timestamp
      }
    },

    problemSetProgress: {
      "{areaKey}": {
        currentLevel:   number,
        correctByLevel: { "1": number, "2": number, "3": number },
        totalByLevel:   { "1": number, "2": number, "3": number }
      }
    },

    roundSimulations: [
      {
        roundType:    "junior_round1" | "senior_round1",
        seed:         number,
        score:        number,
        totalMarks:   number,
        attemptedAt:  timestamp,
        badgeAwarded: "gold" | "silver" | "bronze" | null
      }
    ],

    badges: {
      techniques:  { "{techniqueKey}": { earnedAt: timestamp } },
      problemSets: { "{areaKey}": { tier: string, earnedAt: timestamp } },
      rounds: {
        "junior_round1": { tier: string | null, bestScore: number, attempts: number },
        "senior_round1": { tier: string | null, bestScore: number, attempts: number }
      }
    }
  }
```

---

## 8. Backend Additions

```
caps-ai-backend/app/
  utils/
    olympiad/
      _olympiad_common.py
      technique_registry.py
      junior/               <- problem generators (see section 2.2)
      senior/
      amcstyle/
  services/
    olympiad_service.py     <- gate check, technique mastery updates, badge awards
    leaderboard_service.py  <- weekly leaderboard refresh, opt-in management
  routes/
    olympiad.py             <- GET  /api/olympiad/status
                               GET  /api/olympiad/technique/{key}
                               POST /api/olympiad/problem/attempt
                               GET  /api/olympiad/simulation/{roundType}
                               POST /api/olympiad/simulation/submit
                               GET  /api/olympiad/leaderboard
```

---

## 9. Package Availability

| Feature | Trial | Standard | Pro | School |
|---|---|---|---|---|
| Technique Library (first 3 techniques) | Yes | Yes | Yes | Yes |
| Full Technique Library | No | Yes | Yes | Yes |
| Junior problem sets (Level 1-2) | Yes | Yes | Yes | Yes |
| Junior problem sets (Level 3-5) | No | Yes | Yes | Yes |
| Senior problem sets | No | Yes | Yes | Yes |
| Round 1 simulation | No | Yes | Yes | Yes |
| Leaderboard participation | No | Yes | Yes | Yes |
| Proof comprehension MCQs (Level 4-5) | No | No | Yes | Yes |

---

## 10. Implementation Phases

### Phase O1 — Junior Track Foundation
1. Build `_olympiad_common.py` shared utilities.
2. Build Junior generators: `number_patterns.py`, `digit_arithmetic.py`,
   `basic_combinatorics.py`, `basic_geometry.py`.
3. Build `olympiad_service.py` — gate check + technique mastery logic.
4. Build `OlympiadDashboard.jsx` — gate status display, placeholder technique tree.
5. Build `OlympiadWorkspace.jsx` — hint-free, MCQ + numeric short answer.
6. Build `TechniqueLibrary.jsx` + `TechniquePage.jsx` — first 5 junior techniques with
   SimuLearn worked examples.
7. Test: CAPS gate met -> olympiad unlocks -> technique available -> problem generated ->
   correct answer -> technique mastery updated.

### Phase O2 — Senior Track and Round 1 Simulation
8. Build Senior generators: `algebraic_manipulations.py`, `number_theory_sr.py`,
   `geometric_proofs.py`, `inequality_basics.py`, `combinatorics_sr.py`.
9. Build `RoundSimulation.jsx` — full SAMO Round 1 simulation layout.
10. Build `olympiad.py` simulation routes.
11. Build `OlympiadBadgeGallery.jsx` and olympiad badge award logic.

### Phase O3 — Leaderboard and Social
12. Build `leaderboard_service.py` and weekly leaderboard refresh.
13. Build `Leaderboard.jsx` with opt-in flow and alias selection.
14. Build badge sharing image generation (Puppeteer) if approved in Open Questions.

### Phase O4 — AMC Style and Proof Comprehension
15. Build `amcstyle/` generators.
16. Build proof comprehension MCQ sets for Level 4-5 problems.
17. Surface on OlympiadDashboard as a Pro feature.

---

## 11. Open Questions

1. **Leaderboard alias moderation:** Student-chosen aliases need basic content moderation.
   Use a blocklist + Firebase Extension trigger on write. Define alias rules before Phase O3.

2. **Round 1 simulation timing:** Enforce a 120-minute time limit (soft: warn at 110 min,
   auto-submit at 120 min) to accurately simulate the real SAMO experience, or keep it as
   a reference only? Confirm before Phase O2.

3. **SAMO format update cadence:** SAMO Round 1 format changes occasionally. Designate a
   developer responsible for reviewing new SAMO papers each year and updating generator
   archetypes accordingly. Set a calendar reminder.

4. **Teacher visibility of olympiad progress:** Should teachers on the School plan see a
   student's olympiad badge progress? Recommendation: yes — useful for identifying gifted
   learners. Add to Teacher Mode Phase 2 (Phase D5) if confirmed.

5. **Cross-grade access:** Should the gate be grade-locked or achievement-locked only?
   Recommendation: achievement-locked only. A student with the relevant CAPS badges can
   attempt any olympiad level regardless of grade. Grade is displayed on the leaderboard
   but does not restrict access.

6. **Collaborative olympiad preparation:** Some students prepare for olympiads in groups.
   Should the Phase D9 collaborative work feature extend to olympiad problems? Proof problems
   are a natural use case. Flag for Phase O4.
