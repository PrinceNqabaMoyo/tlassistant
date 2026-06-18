# Master Implementation Plan & Tracker

This document serves as the master phased implementation plan for the EMS (Grade 7-9) and Business Studies (Grade 10-12) integration, including adaptive progression and agentic systems.

## Phased Roadmap

### [x] Phase 1: Grade 7 EMS Backend Generators
*   **Status:** Complete.
*   **Details:** Built dynamic `.py` generators for Term 1 (Money/Needs, Businesses), Term 2 (Accounting concepts, Net Worth, Budgets), and Term 3 (Entrepreneurship). Included hard variations from controlled tests.

### [x] Phase 1.5: Grade 7 EMS Frontend Integration
*   **Status:** Complete.
*   **Details:** Wired Grade 7 generators to the React frontend. Built `EmsScaffold.jsx`, `EmsPractice.jsx`, and `EmsAssessment.jsx` using the Grade 10 Accounting tabular models and rich cell-level hints. Registered routes in `workspaceRegistry.js`.

### [ ] Phase 2: Grade 8 EMS Implementation (Full-Stack)
*   **Status:** **IN PROGRESS (See details below)**
*   **Details:** Build the backend generators for Grade 8 EMS (CRJ, CPJ, Accounting Equation) and wire them to the frontend using the generic EMS components.

### [ ] Phase 3: Grade 9 EMS Implementation (Full-Stack)
*   **Status:** **IN PROGRESS (See details below)**
*   **Details:** Build backend generators for Grade 9 EMS (Debtors/Creditors Journals, General Ledger, trading business concepts) and wire them to the frontend using the Gold Standard tabular UI.

### [ ] Phase 4: Business Studies (Gr 10-12) & Socratic Agent Upgrades
*   **Status:** Pending
*   **Details:** Implement Business Studies generators utilizing both extensive notes and archetype questions. Implement the **Pro Package Live Agentic Tutor** for live Socratic dialogue and AI-driven adaptive progression logic.

### [ ] Phase 5: Architecture Docs & Polish
*   **Status:** Pending
*   **Details:** Finalize frontend UI updates, documentation, and verify the standard vs. pro package separation.

---

## Phase 4 Focus: Business Studies Gr 10-12 & Socratic Agent Upgrades

### 1. Curriculum Audit & Generator Expansion

**Grade 10 Business Studies**
*   **Existing:** Term 1 & 2 generators exist in `caps-ai-backend/app/utils/grade10_business_studies`. Need enhancement to ensure semantic richness and variation.
*   **Outstanding:** Term 3 (Creative thinking, Business opportunities, Contracts, Presentation) and Term 4 (Business plan, Self-management, Relationships).

**Grade 11 Business Studies**
*   **Existing:** Term 1 generators exist in `caps-ai-backend/app/utils/grade11_business_studies/term_1`. Note that `influences_on_business_environments_generator.py` is currently 1606 lines long.
*   **Outstanding:** Term 2, 3, and 4.
*   **Action:** Apply the 2000-line rule. Large term modules will be split into isolated subtopic generators (e.g., separating the scenario datasets from the question generator logic).

**Grade 12 Business Studies**
*   **Outstanding:** Create generators for Term 1, 2, and 3 from scratch, strictly mapping to the CAPS curriculum docs.

### 2. Semantic UI Integration
While Accounting and EMS relied heavily on the tabular mathematical layout, Business Studies requires a robust semantic testing interface.
*   We will wire up existing React components (`WordBankQuestionUI.jsx`, `MatchQuestionUI.jsx`, `InlineFillQuestionUI.jsx`, `MCQOption.jsx`) into a unified `BusinessStudiesScaffold.jsx`.
*   Register Gr 10-12 Business Studies in `workspaceRegistry.js`.

### 3. Socratic Agent Upgrades (Pro Package)
Per the `AGENTS.md` rules, we will implement the **Live Agentic Tutor** for the Pro package:
*   Instead of static pre-generated hint text, the Pro package will feature an interactive chat interface overlay.
*   The frontend will transmit the user's partial answers/state to a new backend Agent endpoint (e.g., `/api/tutor/chat`).
*   The Agent will engage in real-time Socratic dialogue, actively diagnosing misunderstandings.

## User Review Required for Phase 4

> [!IMPORTANT]
> **Phase 4 Implementation Approach**
> 1. **Rule Enforcement:** I have added the 2000-line file limit and modularity requirement to `AGENTS.md`. We will strictly enforce this across Gr 10-12 generators.
> 2. **Backend Expansion:** I will first refactor the existing Gr 11 Term 1 files to be highly modular, then proceed to build out the outstanding terms for Gr 10, 11, and 12.
> 3. **UI & Agent System:** Once the generators are complete, I will build `BusinessStudiesScaffold.jsx` and implement the Agentic Tutor endpoint for the Pro package, ensuring it supports dynamic multi-turn conversation.
> 
> **Are you happy with this approach for Phase 4?**


## Phase 2 Focus: Grade 8 EMS

### Grade 8 EMS Curriculum Audit (Categorized by Subskill)

#### Term 1 Focus: Financial Literacy Basics & Government
*   `1-Government.md` & `2-National Budget.md` & `3-Standard of living.md`: **Semantic/Conceptual focus** covering the roles of government, national expenditure, and poverty.
*   `4-Accounting concepts.md`: **Accounting Maths focus** covering the Accounting Equation (Assets = Owner's Equity + Liability) and classification of accounts.
*   `5-Source Documents.md`: **Accounting Maths focus** covering receipts, deposit slips, and cash register rolls.

#### Term 2 Focus: The CRJ and Markets
*   `6-The accounting cycle.md`: **Conceptual accounting focus**.
*   `7-Cash Receipts Journal of a services (1).md`: **Accounting Maths focus** introducing the CRJ columns and posting receipts.
*   `8-Factors of production.md` & `9-The markets.md`: **Semantic/Conceptual focus**.

#### Term 3 Focus: CPJ and Ownership
*   `10-Cash Receipts Journal of a services business (2).md`: **Accounting Maths focus**.
*   `11-Cash Payments Journal of a services business.md`: **Accounting Maths focus** covering the CPJ and its relation to the CRJ.
*   `12-Forms of ownership.md`: **Semantic/Conceptual focus** covering Sole Traders, Partnerships, etc.

### User Review Required for Phase 2

> [!IMPORTANT]
> **Grade 8 Generator Grouping Proposal**
> To maintain modularity (< 2000 lines) while preventing an explosion of tiny files, I propose grouping the Grade 8 generators as follows:
> 
> *   **`term1_gov_and_society.py`**: Combines Government, National Budget, and Standard of Living.
> *   **`term1_accounting_basics.py`**: Combines Accounting Concepts, Equation, and Source Documents.
> *   **`term2_markets_and_production.py`**: Combines Factors of Production and The Markets.
> *   **`term2_crj.py`**: Combines The Accounting Cycle and CRJ (1).
> *   **`term3_cpj_and_crj.py`**: Combines CRJ (2) and CPJ.
> *   **`term3_ownership.py`**: Handles Forms of Ownership.
> 
> **Are you happy for me to begin writing these backend generators for Phase 2 based on this grouping?**
