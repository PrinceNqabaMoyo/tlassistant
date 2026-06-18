# Grade 7 EMS Full-Stack Implementation Walkthrough

I have successfully wired the Grade 7 EMS backend to the React frontend, strictly following the Grade 10 Accounting Scaffold and Practice models as requested.

## 1. Customizations & Rules Applied
I created `.agents/AGENTS.md` in the root of the project. This sets a permanent rule for the workspace that forces all agents moving forward to:
- Always build full-stack (frontend + backend).
- Use Grade 10/11 Accounting implementations as the architectural gold standard.
- Always refer to the `hint_system_specification.md` when designing tabular UI/hints.

### Phase 3: Grade 9 EMS Full-Stack

**Backend Generators:**
Created 9 modular generators in `caps-ai-backend/app/utils/grade9_ems/`:
1. `term1_crj_cpj.py`: Focuses on CRJ and CPJ for trading businesses (includes Cost of Sales).
2. `term1_general_ledger.py`: Handles T-accounts posting (Bank account sample).
3. `term1_economy.py`: Semantic generation for Economic Systems and Circular flow.
4. `term2_debtors_journal.py`: Generates Debtors Journal (DJ) instances with Cost of Sales.
5. `term2_economy.py`: Semantic generation for Price theory and Sectors of the economy.
6. `term3_creditors_journal.py`: Generates Creditors Journal (CJ) tables.
7. `term3_debtors_ledger.py`: Generates Debtors Ledger (DL) T-account variations.
8. `term3_business.py`: Semantic generation for Functions of a Business and Trade unions.
9. `assessment_generator.py`: Mixed assessment compilation across all Grade 9 topics.

**Frontend Integration:**
1. Cloned the "Gold Standard" Grade 10 Accounting Scaffold architecture and customized it for Grade 9 EMS in `src/components/workspace/grade9/ems`.
2. Created `grade9EmsRegistry.js` mapping all the newly created Grade 9 topics to the UI.
3. Hooked `Grade9EmsScaffold` into `workspaceRegistry.js` for dynamic rendering.

> [!TIP]
> The Grade 9 EMS system seamlessly inherits the 3-tier rich cell hint functionality from the Gold Standard Grade 10 layout!

### What to Verify Next
Please restart the React dev server and test:
1. Navigate to `/workspace?mode=grade9_ems_crj` to verify the Trading Business CRJ UI.
2. Navigate to `/workspace?mode=grade9_ems_debtors_journal` to test the new DJ generation.
3. Navigate to `/workspace?mode=grade9_ems_assessment` to test the full-stack Grade 9 mixture logic.

## Phase 2: Grade 8 EMS Full-Stack Implementation
We successfully delivered Phase 2, which extends the platform to Grade 8 EMS following the "Gold Standard" architectural patterns established by Grade 10 Accounting.

### 1. Frontend Architecture
- **Grade 10 Accounting as Gold Standard**: In direct response to your feedback, the frontend UI for Grade 8 EMS (`Grade8EmsScaffold.jsx` and `Grade8EmsPractice.jsx`) was strictly derived from the `Grade10AccountingSoleTraderScaffold.jsx`. This ensures full support for tabular components like the Cash Receipts Journal and Cash Payments Journal.
- **Routing & Registry**: Created `grade8EmsRegistry.js` and hooked all endpoints into `workspaceRegistry.js` to ensure the frontend application dynamically renders the Grade 8 EMS curriculum modules.

### 2. Backend Generators
- Created comprehensive generators for Term 1, Term 2, and Term 3, accurately modelling the Grade 8 EMS curriculum requirements.
- Implemented `term2_crj.py`, `term3_cpj_and_crj.py`, and `term1_accounting_basics.py` to output the highly specialized `"question_type": "journal"` schema. This guarantees seamless compatibility with the Grade 10 Accounting frontend tables.
- All generators strictly adhere to the 3-Tier Hint System for standard questions and Rich Cell-Level Hints for tabular data.

## 2. Generic EMS Workspace Controllers
Rather than copying the massive Accounting components 6 separate times (for the 6 different Grade 7 EMS topics), I built a unified set of generic components in `src/components/workspace/grade7/ems/`.

- **`EmsScaffold.jsx` & `EmsPractice.jsx`**: Ported directly from `Grade10AccountingFinalAccountsScaffold.jsx`. They utilize the exact same rich, cell-level hints, interactive tables, and word-bank handling for journals and ledgers.
- **`controller.js`**: A generic controller that takes a `config` prop specifying the topic (e.g. `grade7_ems_money_and_needs` or `grade7_ems_businesses`) and fetches the relevant questions from the backend.
- **`useEmsMarking.jsx`**: A direct adaptation of `useGrade10AccountingMarking.js` to ensure the same robust evaluation logic for typed, calculate, and tabular answers.

## 3. Assessment Mode
I created the initial stub for **`EmsAssessment.jsx`**, which allows students to fetch exam-length papers using the new `/api/grade7_ems/assessment` backend endpoint. Unlike Scaffold and Practice, this mode renders questions sequentially without hints and calculates a final mark upon submission.

## 4. UI Wiring
- **`EmsTopicModeCards.jsx`**: Added a new mode card renderer that correctly identifies Grade 7 EMS topics (via updated matchers in `topicMatchers.js`) and presents the Scaffold, Practice, and Assessment buttons.
- **`grade7EmsRegistry.js`**: Registered all of the Term 1, 2, and 3 topics into the system.
- **`workspaceRegistry.js`**: Spread the new EMS registry so the router can successfully mount the components.

You can now boot up your local Vite server and navigate to Grade 7 EMS. You will be able to select Term 1, 2, or 3 topics, launch the Scaffold/Practice/Assessment modes, and interact with the newly generated questions!
