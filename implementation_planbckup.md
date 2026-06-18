# Implementation Plan: Fundile TL Assistant Updates

This plan outlines the implementation strategy for the standard package generators, adaptive progression, and data transfer, while preserving the evaluations and insights from the security and agent task reports.

## User Review Required

> [!IMPORTANT]
> Please review this comprehensive plan. Once approved, I can begin executing the tasks in whichever order you prefer (e.g., starting with the data transfer script, or scaffolding the new EMS generators).

## Open Questions

> [!WARNING]
> 1. **Landing Page Assets**: Do we have specific student/classroom imagery, mascots, or screenshots we can use?
> 2. **HuggingFace Gemma 4**: Do you have a HuggingFace Inference API key for the standard tier semantic evaluation, or do we plan to host Gemma 4 locally?

---

## 1. Standard Package Implementation: EMS (Gr 7-9) & Business Studies (Gr 10-12)

We will **not** rely entirely on the `caps_wiki` text or the Socratic agent for the Standard tier. Instead, the Standard package must have robust, deterministic practice mechanisms.

### Frontend UI Consistency (Topic Cards & Scaffold Toggle)
We will **strictly maintain the existing UI/UX paradigm** currently used in the Accounting modules. For EMS and Business Studies, students will experience the exact same interface:
- **Topic Selection Cards**: Numbered and labeled with Term tags (e.g., "Term 1: Macro Environment").
- **Subtopic Dropdowns**: Allowing granular selection of specific subskills.
- **Scaffold vs. Practice Toggle**: 
  - *Scaffold Mode*: Will provide the tiered hints (Nudge, Concept, Breakdown) and structural guidance.
  - *Practice Mode*: Will present the bare question/scenario to simulate exam conditions without training wheels.

### Enquiry-Based Generators: The Hybrid Approach
We will adopt the successful "enquiry-based at various topic and subskill levels" approach currently used in the Accounting generators. 

**Hybrid Generation (Notes + Archetypes):**
Our generation strategy will not be "either/or". It will utilize both resources available in the curriculum documents:
1. **Archetype Generation**: The generators will produce structured questions (Activities, Consolidation, Control Tests, Exams) that strictly mirror the exact question archetypes found in the curriculum docs to ensure complete CAPS compliance.
2. **Notes Generation**: To ensure infinite variety and prevent sheer copy-pasting, the generators will dynamically sample concepts from the extensive Term 1-3 `.md` notes. By combining the rigorous structure of the archetypes with the deep content of the notes, we get the best of both worlds.

### Semantic Variation via `bs_namelist.py`
To achieve variation in semantic subjects (like EMS/BS), we need randomized names, business types, and products.
- **Dedicated Namelist**: Instead of modifying the existing `namelist.py` (which could break the Accounting implementations), we will create a dedicated `bs_namelist.py` (and `ems_namelist.py`). 
- **BS-Specific Scenarios**: These new namelists will contain scenarios tailored specifically to Business Studies (e.g., corporate structures, unions, specific market environments) that the Accounting namelist does not cover.

**Visual Aids & Tiered Hints**:
- The `.py` generators will dynamically attach visual payloads (like a `Mermaid.js` supply chain diagram) to specific subskills.

### Curriculum Continuity
Because EMS branches into Accounting and Business Studies in Grade 10, the EMS generators will be specifically mapped to introduce the core subskills required for the Grade 10-12 generators.

---

## 2. Adaptive Progression System

The enquiry-based generator model perfectly supports adaptive progression:
1. **Subskill Mapping**: We will map advanced generators directly to foundational generators (e.g., `bs10_business_environments.py` maps back to `ems9_economic_systems.py`).
2. **Progression Drop Logic**: If the system detects a student failing a specific generator threshold (e.g., 3 consecutive failures), it will proactively "drop" the student down a level. 
3. **Intervention**: The student will be served questions from the lower-grade precursor generator to bolster their background knowledge. Once they pass, they are returned to their current grade level.

---

## 3. Data Transfer Pipeline: Curriculum Docs to `caps_wiki`

The raw curriculum documents located in `caps-ai-backend/curriculum_docs/` are already in Markdown (`.md`) format.

### Transfer Strategy
We will write a simple Python automation script to handle the transfer:
- **Migration**: The script will traverse the `curriculum_docs` directories and copy the `.md` files.
- **Structuring**: It will rename and organize them into the exact `caps-wiki/subject/grade/topic.md` hierarchy required by the backend LangChain agent's `get_curriculum_page` tool.
- **Sanitization**: The script will perform a basic regex pass to ensure the markdown headers and formatting are clean and consistent.

---

## 4. Veracity of Implementation Reports

I have evaluated the codebase against the claims in `agent_task.md` and `SECURITY_AUDIT_REPORT.md` and **confirm they are true and successfully implemented**:
- **Security Fixes**: The `dangerouslySetInnerHTML` vectors are gone (`src/backup-App.jsx` deleted), `DOMParser` is correctly utilized, and backend endpoints have payload validation. NPM vulnerabilities have been patched.
- **Agent Infrastructure**: The React visual components and backend agent tools (`get_curriculum_page`, `render_visual`) are live and operational.

---

## 5. Evaluation: `caps_wiki` vs. RAG System

- **`caps_wiki` (Structured Markdown)**: 
  - *Merits*: Highly deterministic, fast, and completely prevents LLM hallucinations. The agent pulls the exact vetted file. This is the correct primary source of truth for the Socratic agent.
- **RAG System (ChromaDB Vector Search)**: 
  - *Demerits*: Prone to retrieval errors and latency. 
  - *Recommendation*: Reserve RAG strictly as a Pro feature (e.g., "Search Past Exam Papers") where parsing massive unstructured text is required.

---

## 6. Socratic Agent System: Experience, Tiers, and Proposed Improvements

### Current Socratic Experience
The Socratic Agent is your live, personalized tutor, invoked when a student clicks "Explain My Mistake". Instead of giving the answer, the agent reviews the student's `get_student_history` to see past struggles and asks leading questions to help the student discover the answer themselves.

### Proposed Improvements to `agent_task.md`
Currently, the system uses a large, monolithic agent that handles all subjects. **This should be upgraded to a Multi-Agent Architecture**:
1. **The Routing Agent**: A lightweight model that reads the student's context and routes the query to a specialized sub-agent.
2. **Specialized Subject Tutors**: Instead of one massive prompt, we will have distinct personas (e.g., `AccountingTutorAgent`, `BusinessStudiesTutorAgent`). This prevents "prompt dilution" and makes the agent's logic much sharper for semantic vs. computational subjects.
3. **The MathML Formatting Agent**: The reasoning agent should NOT be burdened with complex W3C MathML or KaTeX syntax. The reasoning agent should output raw math or simple LaTeX. A dedicated, deterministic **Formatting Agent** (or pipeline step) will intercept this and convert it to perfect MathML/KaTeX for the frontend. This reduces errors and latency.
4. **Session State Context**: Beyond just `get_student_history` (which is long-term), the agent should maintain a short-term "Frustration Index." If a student has tried to answer the Socratic question 3 times and failed, the agent must dynamically soften its tone and give a more direct hint, rather than infinitely asking open-ended questions.

### Standard vs. Pro Package Routing
- **Pro Package**: Has full access to this multi-agent live chat.
- **Standard Package**: Bypasses the live chat. Semantic answers in the standard tier will be routed to a lightweight, free-tier HuggingFace endpoint (Gemma 4) to evaluate correctness, outputting pre-written feedback rather than entering a live chat.

---

## 7. Architecture Documentation & Landing Page Revamp

### Architecture (`Fundile-architecture.md`)
Will be updated to document the clear separation between the Frontend (React/Vite/Firebase), Backend (Flask/Firebase Admin SDK), and the AI toolchain (`.py` Generators for Standard, LangChain/Gemini for Pro).

### Landing Page Revamp (`LandingPage.jsx`)
- **Tone**: Shift to an empowering, student-centric tone ("Ace your exams", "24/7 Personal Tutor").
- **Value Proposition**: Highlight why Fundile is superior to generic AI (Curriculum alignment via `caps_wiki`, deep deterministic practice generators, safe learning).
- **Segmentation & Pricing**: Clear paths for Students, Teachers, and Admins, with prominent Free Plan visibility.

---

## Verification Plan

### Automated Tests
- Run existing UI tests. Verify `npm audit` remains clean.

### Manual Verification
- Write a smoke test for the new EMS/BS Python generators to ensure they output valid JSON.
- Verify the Python transfer script successfully structures the `.md` files into the `caps-wiki` directory.
- Review the newly designed Landing Page locally.
