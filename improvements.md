# Fundile Modernization: Comprehensive Architectural & Technical Improvements

This document catalogs the prioritized recommendations and identified enhancements for Fundile across performance, maintainability, architectural consistency, and low-bandwidth/load shedding optimization.

---

## 1. High-Priority Code & Performance Improvements

### A. Frontend Bundle Size Optimization (11.2 MB → ~250 KB Initial Load)
- **Problem**: 
  The current production build bundles all modules into a single monolithic file: `dist/assets/index-CLYxTg6h.js (11,237 kB | gzip: 2,821 kB)`. On South African mobile networks (Vodacom/MTN capped data bundles), an 11.2 MB download creates a 5–10s latency barrier and drains user data.
- **Remediation**:
  1. Configure `manualChunks` in `vite.config.js`:
     - `vendor-jsxgraph`: ~4 MB geometry canvas.
     - `vendor-katex`: ~2.5 MB math typesetting & webfonts.
     - `vendor-firebase`: ~1.5 MB authentication & firestore client.
  2. Implement `React.lazy()` + `<Suspense>` for views not needed on first paint:
     - `TeacherView`, `AdminDashboard`, `SubscriptionPage`, `PrintableTestModal`, `SimuLearnPlayer`.
  3. **Expected Impact**: Initial landing/student workspace payload drops from **11.2 MB to < 300 KB** (~97% reduction).

### B. Modularization of `src/App.jsx` (Enforcing Rule 4: < 2,000 Lines)
- **Problem**: 
  `src/App.jsx` contains 2,315 lines of code, violating Rule 4 (*"No file should exceed 2000 lines of code. Modularization must be implemented"*). Routing, modal managers, subscription status, and workspace components are tightly coupled.
- **Remediation**:
  1. Extract routing into `src/views/MainAppRouter.jsx` (handles view state: `landing`, `student_workspace`, `teacher`, `admin`, `curriculum_map`).
  2. Extract modal lifecycle into `src/components/modals/AppModalsHub.jsx` (`SubscriptionModal`, `MicroBenchmarkModal`, `SimuLearnPlayer`, `ChallengeGate`, `GamificationSummary`).
  3. Reduce `src/App.jsx` to under **250 lines**.

### C. Generator Registry Completeness (`generator_registry.py`)
- **Problem**: 
  `caps-ai-backend/app/services/generator_registry.py` only registers Business Studies and EMS. Calling `generate_variant(topic="...")` for Mathematics, Accounting, Physical Sciences, Life Sciences, Mathematical Literacy, or Technical Mathematics throws a `ValueError`.
- **Remediation**:
  Wire all existing utility generators from `caps-ai-backend/app/utils/` into `ALL_GENERATORS` in `generator_registry.py` under standardized topic keys.

---

## 2. Architectural & Data Pipeline Improvements

### D. Dual-Layer Session Audit Pipeline (Phase D1)
- **Problem**: 
  `Complete-App-Implementation-Plan.md` §1 specifies a dual-layer audit trail:
  1. A structured Markdown audit file in Firebase Storage (`sessions/{userId}/{year}/{month}/{sessionId}.md`).
  2. A compute-ready document in Firestore (`session_index/{sessionId}`).
  Currently, session telemetry sits in client memory (`telemetryBuffer.js`) and is not yet persisted to Firebase Storage and `session_index`.
- **Remediation**:
  Build `session_file_writer.py` on the backend and wire `telemetryBuffer.flushSession()` to `/api/session/end`.

### E. Pruning Deprecated LangChain / ChromaDB Remnants in `MainApp.py`
- **Problem**: 
  `caps-ai-backend/MainApp.py` retains legacy imports (`langchain_google_genai`, `langchain_chroma`, `Chroma`), which conflict with Rule 11 (*"Deterministic Context, Not RAG. The agent is grounded by reading the relevant caps-wiki/ Markdown file directly"*). `curriculum_bp` in `app/__init__.py` was commented out due to ChromaDB build issues.
- **Remediation**:
  Remove all legacy `chromadb` and `langchain` references; standardize all LLM interactions through the thin provider abstraction (`llm_provider.py`). Eliminates C++ compiler requirements in Docker containers and shaves ~400 MB from image size.

---

## 3. South African Contextual & Offline Enhancements

### F. Offline-Ready PWA (Progressive Web App) for Load Shedding Resilience
- **Opportunity**: 
  Fundile’s question generation, marking, and 3-tier hints are 100% deterministic Python and zero-LLM in Standard tier. Problem sets can be solved without an active internet connection.
- **Remediation**:
  Add `vite-plugin-pwa` so learners can install Fundile on Android phones and school tablets. Homework and practice sessions remain active during load shedding when cell towers go dark; telemetry syncs to Firestore upon reconnection.

---

## 4. Implementation Plan Document Updates

- Update `Complete-App-Implementation-Plan.md` §15 to mark Phase E (Gamification, 4-Tier Badges, ProgressMap, ChallengeGate) as completed.
- Update `Simulation-implementation-plan.md` to reflect the SimuLearn Animation Script Engine and Player as completed.
- Maintain `fundile-architecture.json` and generate `fundile-architecture.html` at session completion.
