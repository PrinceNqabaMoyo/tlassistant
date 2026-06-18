# Implementation Status & Offline Capability Analysis

## 1. Extent of Implementation (Current Progress)

### ✅ Phase A: 3-Mode Architecture
- **Done:** `WorkspaceModeShell` supports Scaffold, Practice, and Marking modes.
- **Done:** LLM "Marking" mode isolated as a future Pro-tier feature.

### ✅ Phase C: Term Stickers
- **Done:** "Term 1" (blue) and "Term 2" (green) badges render correctly on topic selection cards across Grades 10, 11, and 12 Accounting.

### ✅ Phase D: Term 2 Topics with Subskills
- **Done:** Grade 10 — VAT, Salaries & Wages, Final Accounts (cards 6–8)
- **Done:** Grade 11 — Analysis & Interpretation, Clubs/Non-profits (cards 5–6)
- **Done:** Grade 12 — Fixed Assets, Inventories, Reconciliations, VAT (cards 6–9)
- **Done:** All 6 Term 2 backend generators verified against curriculum docs.
- **Done:** Registry entries with Term-2-only subskills (no Term 1 leakage in dropdowns).

### ✅ Phase E: Check/Compare UI (Evaluation System)
- **Done:** "Check" button parses user answers via `evaluation_service.py`, highlights incorrect cells in red, clickable for step-by-step rubric overlay.
- **Done:** "Compare" toggle swaps between user input and correct answer.

### 🔲 Phase B: Subscription Security (Extend Firebase)
- **Partially done:** Firebase Auth is in place. Owner bypass and grade-locking logic exist in `useAuthentication.js`.
- **Not yet done:** Firestore user doc fields (`tier`, `subscribedGrades`, `subscribedSubjects`, `subscriptionExpiry`) are not yet fully enforced.
- **Not yet done:** Dec 1 auto-upgrade logic.

### 🔲 Remaining Reads
- [ ] Gr12 `Reconciliations.md` — extract subskills
- [ ] Gr12 `Value Added Tax.md` — extract subskills

---

## 2. Offline Downloadable Standard Package

> [!IMPORTANT]
> **Priority:** Downloadability is a **future goal** that will be pursued only _after_ all phases in the `Evaluation_Subscriptions_Term2_Implementation_Plan.md` are complete.

### User Base Reality
The primary user base is **mobile-first** (smartphones), with a meaningful secondary audience on **desktop/laptop**. Any offline distribution strategy must serve both form factors.

### Strategy by Platform

#### 📱 Mobile (Primary — Android & iOS)

| Approach | How it works | Subscription enforcement |
|---|---|---|
| **PWA (Progressive Web App)** | Users "Add to home screen" from the browser. The React UI is cached via a Service Worker for instant offline loading. | Works well for UI caching, but question generation still requires the Python backend online. Suitable for **caching previously generated question sets** for offline practice. |
| **React Native / Capacitor wrapper** | Wrap the existing React app in a native shell (`.apk` / `.ipa`). Embed a bundled Python runtime (e.g. Chaquopy for Android) or pre-compiled WASM generators. | Full offline generation possible. Subscription validated via cached JWT token with expiry + last-seen-time anti-tampering. |

> [!NOTE]
> **Recommended mobile path:** Start with a **PWA** that caches the UI and pre-fetched question batches for offline use. This gives immediate value with minimal effort. A full native app with embedded Python can follow later as a premium offering.

#### 💻 Desktop (Secondary — Windows, Mac, Linux)

| Approach | How it works | Subscription enforcement |
|---|---|---|
| **Electron + PyInstaller** | Bundle the React frontend + compiled Python backend into a single `.exe` / `.dmg` / `.AppImage`. Python runs as a hidden local server. | Encrypted JWT token cached locally. App checks `currentDate > expiryDate` on launch. Records "last seen time" to prevent clock tampering. Forces internet check-in when expired. |

### Subscription Enforcement (Both Platforms)

```
┌─────────────────────────────────────────────────┐
│  App Launch                                     │
│  ├─ Read cached JWT token (encrypted)           │
│  ├─ Check: currentDate > expiryDate?            │
│  │   ├─ NO  → Allow offline use                 │
│  │   └─ YES → Force internet check-in           │
│  │            ├─ Subscription active → Renew JWT │
│  │            └─ Subscription lapsed → Lock app  │
│  └─ Anti-tamper: lastSeenTime > currentDate?    │
│       └─ YES → Clock rolled back → Lock app     │
└─────────────────────────────────────────────────┘
```

### Execution Order

1. ~~Phase A: 3-Mode Architecture~~ ✅
2. ~~Phase E: Check/Compare UI~~ ✅
3. ~~Phase C: Term Stickers~~ ✅
4. ~~Phase D: Term 2 Topics~~ ✅
5. **Phase B: Subscription Security** ← Next
6. **Remaining subskill extraction** (Gr12 Reconciliations, Gr12 VAT)
7. **PWA setup** (Service Worker + manifest for mobile offline caching)
8. **Electron packaging** (desktop offline bundle)
9. **Native mobile wrapper** (future, if needed beyond PWA)
