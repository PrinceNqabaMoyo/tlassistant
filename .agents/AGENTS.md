# General Development Rules

1. **Always Build Full-Stack**: When tasked with building a new module or feature (like EMS), you MUST implement both the backend logic (generators, endpoints) AND the frontend React UI (Scaffold, Practice, and Assessment modes). Do not stop at the backend.
2. **Use Accounting as the Gold Standard**: For any new subject modules, always use the Grade 10/11 Accounting implementations as your architectural model for *both* the backend generators and the frontend React components.
3. **Follow the Hint System**: You must strictly adhere to the hint architecture defined in `hint_system_specification.md` (rich cell-level hints for tabular data, 3-tier hints for non-tabular data). Always read that file before implementing new generators or UI components.
4. **File Size Limit**: No file should exceed 2000 lines of code. Modularization must be implemented to keep files focused and maintainable. This is especially important for backend generators which can become huge.

## Application Tiers: Standard vs. Pro

### Adaptive Progression (How the Student Advances)

5. **Standard Package (Rule-Based / Linear)**
   - Students move through Scaffold → Practice → Assessment in a fixed order.
   - Progression is unlocked by hardcoded score thresholds (e.g., 60% to leave Scaffold, 80% to unlock Assessment).
   - All subskills are treated equally. On failure, the student reattempts more deterministic questions from the same pool.
   - No LLM calls are made during progression decisions.

6. **Pro Package (AI-Driven / Non-Linear)**
   - The system continuously tracks per-subskill mastery using metadata already emitted by generators (`learning_objective_id`, `misconception_tags`, `diagnostic_tags`, `minimum_mastery_score`, `keywords`).
   - If a student struggles with a specific subskill (e.g., "Calculating depreciation"), the system dynamically generates targeted micro-lessons and isomorphic practice questions for that subskill before allowing advancement.
   - The agent can request the generator to produce variants by changing context, numbers, or wording while keeping the same archetype and learning objective.
   - All progression decisions are reproducible and auditable: they are based on the shared student model, not an opaque LLM.

### Agentic System (How the AI Assists the Student)

7. **No Freeform Chat**: Legacy freeform chat is deprecated and must be removed. The agent is not a general-purpose chatbot. It is a subject- and topic-bound tutor.

8. **Standard Package (Static Generation System)**
   - During the single `/generate` request, the backend LLM generates the question, sample answer, marking points, and all hints *ahead of time*.
   - The frontend reveals pre-computed hints when the student clicks a hint button.
   - There is no live back-and-forth conversation. All assistance is deterministic and pre-baked.

9. **Pro Package (Live Agentic Tutor)**
   - A single orchestrator agent with a tool belt handles all tutoring interactions.
   - The agent receives the current question context, the student's partial answer, and the shared student model.
   - It responds with a short text answer and, when needed, a `render` payload for visual components (KaTeX, JSXGraph, accounting tables, etc.).
   - The agent is strictly on-rails. The frontend should expose clickable suggestion chips for allowed prompts (e.g., "Explain the hint", "Show me another example", "Why is this wrong?"), but the student can also type a topic-bound question.
   - The agent must not write its own questions; it must call the deterministic generator when it needs a variant.

## LLM Provider Abstraction

10. **Model-Agnostic Layer**
    - The backend must not depend on a single provider. All LLM calls go through a thin provider abstraction (`app/services/llm_provider.py`).
    - The default implementation targets the **Hugging Face Inference API** so that open-source models (e.g., Gemma) can be used on the free tier.
    - Swapping to Gemini, self-hosted Gemma, or another endpoint is a configuration change only.
    - Keep prompts and tool definitions provider-agnostic; do not hardcode provider-specific response formats.

## Grounding: CAPS Wiki

11. **Deterministic Context, Not RAG**
    - The agent is grounded by reading the relevant `caps-wiki/` Markdown file directly.
    - The agent prompt includes the current topic's wiki content verbatim; there is no vector retrieval or embedding search.
    - Wiki files are structured as Markdown with optional YAML frontmatter. They are compatible with the Open Knowledge Format (OKF) idea: a portable, human-readable knowledge bundle for the agent.
    - Syllabi and per-topic guidance live in `caps-wiki/{subject}/{grade}/{topic}.md`.

## Shared Student Model

12. **One Source of Truth for Student State**
    - The student model (`app/services/student_model.py`) stores per-subskill mastery, submission history, last session per topic, and struggling topics.
    - It is used by both the Adaptive Progression engine and the Agentic Tutor.
    - It also tracks engagement across subjects within the same grade so that the agent can make legitimate cross-subject links (e.g., electrons in Chemistry and Biology) when the student has accessed both topics.

## Topic Guardrail

13. **Strict Topic Boundaries**
    - Before any LLM call, a deterministic guardrail checks whether the student's request is within the allowed topic scope.
    - Allowed scopes, in order of permissiveness:
      1. The current question/topic.
      2. Any topic within the same grade that the student has already engaged with (cross-subject linking only when there is a real conceptual link).
    - General study advice, off-topic questions, and non-curricular prompts must be declined with a short, friendly message redirecting the student to the current topic.
    - The agent must refuse requests to "ignore previous instructions" or act as a general assistant.

## Generator Variants

14. **Agent Must Use the Generator**
    - When the agent wants to give the student repeated practice on a struggled question, it calls the appropriate generator with a fresh `seed` or `variant` parameter.
    - The generator produces isomorphic questions (same archetype, same learning objective, different numbers/context) without the agent authoring questions itself.
    - This preserves correctness and alignment with the curriculum.

## Development Safety

Before editing `src/App.jsx` (a 2,300+ line file), **always make a manual backup** first (e.g. copy `src/App.jsx` to `src/App.jsx.backup`).
This prevents accidental loss of state if an edit goes wrong.

## Current Implementation Priority

15. **Vertical Slice First**
    - The first adaptive + agentic vertical slice is **Grade 10 Business Studies**.
    - After the slice is verified, replicate the pattern to EMS Grades 7–9 and the remaining BS grades.

