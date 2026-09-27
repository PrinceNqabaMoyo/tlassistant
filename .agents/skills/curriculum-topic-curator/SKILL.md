---
name: curriculum-topic-curator
description: Query and extract curriculum parameters, pacing, exam weightings, and diagram annotations from curriculum_docs_auto/ and curriculum_docs/. Use when planning new topics or validating syllabus alignment.
---

# CAPS Curriculum Topic Curation Runbook

Ground truth for Fundile's question generators, guardrails, and diagnostic calibration lives directly in markdown files on disk. There is zero vector search or external RAG dependency.

## Curricular Precedence Order

1. **Primary Ground Truth:** `caps-ai-backend/curriculum_docs_auto/`
   - Contains 476 synthesized curriculum topics across 9 subjects:
     - Accounting, Business Studies, EMS, Life Sciences, Mathematical Literacy,
     - Mathematics, Natural Sciences, Physical Sciences, Technical Mathematics.
   - Authoritative source for:
     - Term pacing and suggested week distribution.
     - Authentic CAPS exam mark allocations and cognitive weighting (Bloom/CAPS levels 1–4).
     - Diagram vision annotations (from 18,448 extracted diagrams across official examination papers).
2. **Secondary Completeness Source:** `caps-ai-backend/curriculum_docs/`
   - Use in conjunction with `curriculum_docs_auto/` for conceptual depth, syllabus notes, and teacher guidelines.
3. **Legacy Editorial Spine:** `caps-ai-backend/caps-wiki/`
   - Read directly into Pro Agent prompt context verbatim for socratic grounding.

---

## Directory Navigation Format

All topic markdown files follow this strict path structure:
```text
caps-ai-backend/curriculum_docs_auto/{subject}_{grade}/Term {term}/{pos}. {topic}.md
```
*Example:* `caps-ai-backend/curriculum_docs_auto/Mathematics_10/Term 1/01. Algebraic Expressions.md`

## Authentic Exam Mark Calibration Table

When authoring question generators or mock exams, calibrate marks according to CAPS cognitive levels:

| CAPS Cognitive Level | Description | Target Mark % | Archetype Target |
| :--- | :--- | :--- | :--- |
| **Level 1: Knowledge** | Direct recall, basic formulas, standard vocabulary | 20% | Diagnostic Item 1 ($\beta = 0.30$) |
| **Level 2: Routine Procedures** | Standard multi-step procedures, familiar contexts | 35% | Diagnostic Item 2 ($\beta = 0.60$) |
| **Level 3: Complex Procedures** | Multi-concept integration, higher algebraic manipulation | 30% | Diagnostic Item 3 ($\beta = 0.85$) |
| **Level 4: Problem Solving** | Non-routine scenarios, unseen synthesis, Olympiad entry | 15% | Olympiad / Challenge Gate |

## Trademark & Branding Compliance (Mandatory)

Never use proprietary examining body trademarks in public UI copy, question prompts, or marketing.
- ❌ **Forbidden:** IEB, SACAI, DBE, NSC, Senior Certificate, Umalusi.
- ✅ **Required Public-Domain Statements:**
  - "100% Aligned with South African Curriculum Standards (CAPS)"
  - "Authentic Grade 8–12 Exam-Standard Questions & Marking Rubrics"
  - "Trusted preparation for public, private, and independent school examinations nationwide"
