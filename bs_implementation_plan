# Grade 10 Business Studies Implementation Plan

## Objective
Implement Grade 10 Business Studies (Term 1 and Term 2) from the ground up, adopting the modern, feature-rich format used in Grade 10 Accounting (Sole Trader / Final Accounts). This includes properly structured backend generators, a robust marking mode, timed practice flows, and advanced scaffold UI (Check, Hint, Compare).

## Open Questions for the User
- **Memo Structure:** For semantic/discussion-based questions, do you approve of showing the marking points as bullet points, accompanied by an "Ideal Narrative Paragraph" so students can compare their semantic answers against a structured example?
- **Missing Topics:** The curriculum docs jump from Topic 4 (Term 1) to Topic 7 (Term 2). Should I reserve space for Topics 5 and 6, or just number them according to the docs?
- **Visual Aids:** Are there any specific visual aids (like the accounting tables) you want implemented for Business Studies, or should the Visual Aids panel mostly contain definition flashcards and summaries?

## Phase 1: Foundation & Registry (Frontend)

1. **Update `CurriculumHelper.jsx`:**
   - Register `isGrade10BusinessStudies`.
   - Add the Term 1 and Term 2 topics with numbering and `[Term 1]` / `[Term 2]` tags on the selection cards.
   
2. **Create Core Shared Hooks:**
   - Create `src/components/workspace/grade10/business-studies/useGrade10BusinessStudiesMarking.js` to handle secure assessment submission and state management, identical to the accounting marking hook.

## Phase 2: Directory Structure & Routing

### Frontend Structure
Organize files strictly into term folders to avoid clutter:
- `src/components/workspace/grade10/business-studies/term-1/`
  - `/micro-environment/` (Topic 1)
  - `/business-functions/` (Topic 2)
  - `/market-environment/` (Topic 3)
  - `/macro-environment/` (Topic 4)
- `src/components/workspace/grade10/business-studies/term-2/`
  - `/socio-economic-issues/` (Topic 7)
  - `/social-responsibility/` (Topic 8)
  - `/entrepreneurial-qualities/` (Topic 9)
  - `/forms-of-ownership/` (Topic 10)
  - `/concept-of-quality/` (Topic 11)

### Backend Structure
Organize generators into term folders:
- `caps-ai-backend/app/utils/grade10_business_studies/term_1/`
- `caps-ai-backend/app/utils/grade10_business_studies/term_2/`
- Create an API router: `caps-ai-backend/app/api/grade10_business_studies.py` to route generation requests.

## Phase 3: Generator Parsing & Implementation (Backend)

1. **Parse Archetype Documents (`Mixed-1.md` to `Mixed-4.md`)**:
   - I will do in-depth reading of the mixed files and categorize the questions into their respective topics based on keywords (e.g., "Macro environment", "Forms of ownership").
   - I will extract both the MCQ/short-answer questions and the discussion-based questions.
2. **Develop Subskills**:
   - Each generator will break down the topic into subskills (e.g., `forms_of_ownership_generator.py` will have subskills: `characteristics`, `advantages_disadvantages`, `differences`).
3. **Memo Parsing**:
   - For questions that require a discussion, the `sample_answer` will be parsed as a list of marking points, followed by a sample paragraph. The grading rubric will enforce checking for these marking points.

## Phase 4: Modern Component Implementation (Frontend)

For **each** topic, I will implement:
1. **`controller.js`**:
   - Fetch 8 questions for the timed practice mode (mix of MCQs, short answers, and table matching if applicable).
2. **`Scaffold.jsx`**:
   - Implement the modern UI with the **Check**, **Get a Hint**, and **Compare to Memo** buttons.
   - For semantic questions, the "Compare to Memo" will reveal the structured marking points and the ideal narrative.
3. **`Practice.jsx`**:
   - Implement the 8-question timed flow with the "Finish and Review" mode that locks inputs and evaluates the entire assessment against the backend logic.

## Verification Plan
- **Backend Setup:** Start the backend and verify the new endpoints `/api/business-studies/grade10/...` respond with correctly formatted question objects.
- **Frontend Routing:** Click through the selection cards in the UI to ensure they correctly navigate to the new workspace modes.
- **Scaffold/Practice Testing:** Test typing semantic answers and triggering the "Compare" mode to verify the memo renders the marking points clearly.
