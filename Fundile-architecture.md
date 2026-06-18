# Fundile TL Assistant Architecture

## 1. Frontend

**Tech Stack**: Vite, React, JSX, Vanilla CSS / Tailwind CSS, W3C MathML
**Role**: Provides the interactive workspace for the student. Renders semantic layouts and specific mathematical notations (via MathML).

### Standard Package
- **Features**: Scaffold Mode vs Practice Mode toggle.
- **Interactions**: Pre-generated dynamic questions with tiered hints (Nudge, Concept, Breakdown). Visual aids embedded directly.
- **Adaptive Progression**: If a student fails repeatedly, they are automatically dropped to lower-level precursor subjects (e.g., Gr 10 Business Studies down to Gr 9 EMS) to rebuild foundational knowledge.

### Pro Package
- **Features**: Live Socratic AI chat interface overlaying the workspace.
- **Interactions**: Direct Q&A with specialised AI tutors. Includes the "Frustration Index" visual or backend state to shift the agent from Socratic questioning to direct hinting.

---

## 2. Backend

**Tech Stack**: Python (FastAPI/Flask), LangChain, Firebase/Firestore

### Standard Package (Generators)
- **Generators**: `.py` files (e.g., `ems_generator.py`, `bs_generator.py`, `gr10sole_trader.py`).
- **Generation Strategy**: Hybrid Generation.
  - *Math*: Deterministic variance (randomizing numbers within bounds).
  - *Semantic Subjects*: Pulls from hardcoded archetypes and `caps_wiki` markdown notes. Uses `namelist.py` for dynamic "dressing" (scenario names, macro issues, products).
- **Curriculum API**: Exposes these generated objects to the frontend via REST endpoints.

### Pro Package (Multi-Agent Socratic Tutors)
- **Architecture**: A Multi-Agent LangChain Router framework.
- **Agents**:
  1. **Router Agent**: Evaluates requests and directs them to the correct subject matter expert.
  2. **Math Tutor Agent**: Specializes in calculations and formulas. Uses calculator tools.
  3. **Semantic Tutor Agent**: Specializes in theoretical concepts (EMS, BS). Uses `get_curriculum_page` to pull definitions directly from the knowledge base.
  4. **MathML Formatter Agent**: A pipeline step that intercepts raw Math output and strictly formats it in W3C MathML for pristine frontend rendering.
- **State Management**: Uses `get_student_history` to assess prior struggles and enforce the Frustration Index threshold.
