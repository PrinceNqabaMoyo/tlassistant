---
name: simulearn-authoring
description: Create canonical declarative JSON animation scripts for SimuLearn worked solutions. Use when building or updating step-by-step visual solution replays for question archetypes.
---

# SimuLearn Worked Example Authoring Runbook

SimuLearn (Layer B) provides canonical, pre-animated worked solutions for every question archetype at **0.1% of video data cost** (~2KB JSON stream instead of a 20MB MP4 stream).
All users see the same canonical simulation for the same question archetype, generated deterministically from fixed canonical seeds.

## SimuLearn Architecture & Data Model

A SimuLearn animation payload consists of an array of synchronized timeline frames played by `SimuLearnPlayer.jsx`:

```json
{
  "simulation_id": "sim_gr10_acct_crj_vat",
  "archetype_id": "sole_trader_crj_analysis",
  "canonical_seed": 1001,
  "subject": "Accounting",
  "grade": 10,
  "title": "Recording a Cash Sale with 15% VAT",
  "steps": [
    {
      "step_index": 0,
      "title": "Read & Identify the Source Document",
      "narrative": "A cash receipt of R11,500 was issued for merchandise sold. The business is registered for VAT at 15%.",
      "spotlight": {"target_type": "transaction_text", "id": "t1"},
      "highlights": [],
      "calculation": null,
      "duration_ms": 2500
    },
    {
      "step_index": 1,
      "title": "Calculate the Cost of Sales & VAT Breakdown",
      "narrative": "Bank receives the gross amount (115%). Sales gets the exclusive price (100%), and Output VAT is 15%.",
      "spotlight": {"target_type": "formula_box"},
      "calculation": {
        "formula": "VAT = R11,500 \\times \\frac{15}{115} = R1,500",
        "sales": "Sales = R11,500 - R1,500 = R10,000"
      },
      "duration_ms": 3500
    },
    {
      "step_index": 2,
      "title": "Populate the Cash Receipts Journal Table",
      "spotlight": {"target_type": "table_cells", "coords": [[1, 4], [1, 5], [1, 6]]},
      "highlights": [
        {"cell": "R1C4", "value": "11 500", "label": "Bank Gross"},
        {"cell": "R1C5", "value": "10 000", "label": "Sales (Net)"},
        {"cell": "R1C6", "value": "1 500", "label": "Output VAT"}
      ],
      "duration_ms": 4000
    }
  ]
}
```

## SimuLearn Rules

1. **Fixed Canonical Seeds:** Developers pre-select one canonical seed per archetype. Never randomize the simulation seed at runtime; learners should have identical reference points.
2. **Circuit Breaker Escalation:** When a student triggers 3 strikes (frustration counter) in Socratic Tutor mode, the tutor automatically deploys the SimuLearn animation overlay before offering an isomorphic re-attempt.
3. **Bandwidth Optimization:** Never embed base64 image frames or video clips. Use SVG coordinates, LaTeX strings, and table cell coordinate pointers.
