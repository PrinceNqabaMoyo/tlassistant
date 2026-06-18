# General Development Rules

1. **Always Build Full-Stack**: When tasked with building a new module or feature (like EMS), you MUST implement both the backend logic (generators, endpoints) AND the frontend React UI (Scaffold, Practice, and Assessment modes). Do not stop at the backend.
2. **Use Accounting as the Gold Standard**: For any new subject modules, always use the Grade 10/11 Accounting implementations as your architectural model for *both* the backend generators and the frontend React components.
3. **Follow the Hint System**: You must strictly adhere to the hint architecture defined in `hint_system_specification.md` (rich cell-level hints for tabular data, 3-tier hints for non-tabular data). Always read that file before implementing new generators or UI components.

## Application Tiers: Standard vs. Pro

4. **Adaptive Progression**: When designing or implementing progression systems, maintain the boundary between packages:
   - **Standard Package**: Uses linear or simple rule-based progression. Students move linearly through Scaffold -> Practice -> Assessment. Progression is unlocked based on hardcoded score thresholds (e.g., getting 80% on Practice unlocks Assessment).
   - **Pro Package**: Uses AI-driven, non-linear adaptive progression. The system continuously analyzes the student's performance across granular subskills. If a student struggles with a specific concept (e.g., "Calculating depreciation"), the system dynamically generates targeted micro-lessons and practice questions specifically for that subskill before allowing them to advance.

5. **Agentic System**: When designing AI assistance, differentiate the tutor's capabilities by package:
   - **Standard Package**: Uses a **Static Generation System**. The backend LLM generates the questions, answers, and all possible hints *ahead of time* during the single `/generate` request. When the student gets stuck, they click a button to reveal pre-computed hint text (like the rich cell-level hints). There is no live back-and-forth communication.
   - **Pro Package**: Uses a **Live Agentic Tutor**. The AI acts as an active, conversational companion tracking the user's state. If a student gets stuck, the frontend passes their partial answer and workspace state back to an active backend Agent. The Agent engages the student in a live, real-time Socratic dialogue, actively diagnosing their misunderstanding and guiding them to the correct answer through dynamic conversation, rather than just showing pre-written text.

6. **File Size Limit**: No file should exceed 2000 lines of code. Modularization must be implemented to keep files focused and maintainable. This is especially important for backend generators which can become huge.

