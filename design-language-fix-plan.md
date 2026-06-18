# Design Language Alignment — Grade 10 Accounting Indigenous Bookkeeping

Fix the 5 UI/UX problems listed in `design language.txt`, using Grade 10 Accounting Indigenous Bookkeeping as the reference implementation to set the standard for all other workspace topics.

## Problem Summary & Root Cause Analysis

| # | Problem | Root Cause |
|---|---------|-----------|
| 1 | After "Generate Questions" the expected 2-card layout (question card + answer card) doesn't appear. Instead, the WorkspaceModeShell overlay is covered by the child scaffold/practice component's own full-page container | Scaffold & Practice JSX files render their own `<div className="bg-gray-50 min-h-screen">` wrapper, headers, back buttons, and difficulty selectors — even when `hideConfig: true`. This paints a second full-page layer on top of WorkspaceModeShell's overlay, with clashing gray color tones |
| 2 | Practice mode generates multiple questions at once | `Grade10AccountingIndigenousPractice.jsx` does `questions.map(...)` and renders ALL returned questions. Should show 1 at a time with a "Next" button |
| 3 | MCQ radio bullets are inconsistent (some circular, some oval) | Radio indicators are custom `<span className="h-4 w-4 rounded-full">` elements. Without `flex-shrink-0` and explicit `aspect-ratio`, CSS layout can squash them into ovals |
| 4 | Visual aids panel looks clumsy | The panel is rendered inline via `<VisualAidsPanel>` inside the child component's flex layout. Within WorkspaceModeShell's fixed overlay, this creates a cramped side-by-side that doesn't work well |
| 5 | "Change settings" should be "Go back", and a "Next" button is needed below the answer section | WorkspaceModeShell hardcodes "Change settings" text (line 265) and has no "Next Question" button. Users must navigate back to the config panel to generate the next question |

---

## Proposed Changes

### WorkspaceModeShell — overlay chrome & navigation

#### [MODIFY] WorkspaceModeShell.jsx

1. **Rename "Change settings" → "Go back"** (line 265)
2. **Accept an `onNext` prop** — a callback the parent route can supply (calls `onGenerate` again with same config to fetch the next question)
3. **Render a "Next" button** at the bottom of the overlay content area, below `{children}`. Style: `w-full rounded-xl h-12 bg-slate-900 text-white` (matching the Generate button)
4. **Expose `showQuestion` state upward (or accept it as prop)** — so the child component knows it is in overlay mode and can adapt

---

### Scaffold component — strip redundant chrome

#### [MODIFY] Grade10AccountingIndigenousScaffold.jsx

1. **Remove the outer full-page wrapper** (`<div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">`) — replace with a simple `<div>` or `<>` fragment
2. **Remove the duplicate header** (title, back button, difficulty selector) — these are already handled by WorkspaceModeShell. The `hideConfig` prop already guards most of this, but the surrounding div and VisualAidsPanel stay
3. **Move VisualAidsPanel outside the main content flow** — render it as a floating/collapsible panel rather than inline flex
4. **Adopt the design language colour tokens** — replace `bg-gray-50`, `text-gray-900`, `bg-indigo-600` with `bg-slate-50`, `text-slate-800`, `bg-slate-900` etc. matching the WorkspaceModeShell/Workspace UI.js palette

---

### Practice component — single question + radio fix

#### [MODIFY] Grade10AccountingIndigenousPractice.jsx

1. **Remove the outer full-page wrapper** — same treatment as Scaffold above
2. **Single-question display** — instead of `questions.map(...)`, track a `currentIndex` (starting at 0). Render only `questions[currentIndex]`. The "Next" button in WorkspaceModeShell will advance the index (or fetch a new question)
3. **Fix MCQ radio bullets** — add `flex-shrink-0` and explicitly set `aspect-square` (or `aspect-ratio: 1`) to the outer `<span>` so it stays perfectly circular regardless of flex context
4. **Move VisualAidsPanel** to floating/collapsible treatment (same as Scaffold)
5. **Adopt design language colour tokens** — same palette alignment

---

### Registry wiring — pass `onNext` to WorkspaceModeShell

#### [MODIFY] grade10Registry.js

- In `Grade10AccountingIndigenousRoute`, add an `onNext` prop to the `WorkspaceModeShell` invocations that calls the appropriate fetch function with the current config

---

## Suggestions & Improvements

### Suggestion 1 — Shared MCQOption component
Since radio bullets are used in many scaffold/practice files across the app, consider extracting a `shared/MCQOption.jsx` component that handles the radio indicator, text, and styling consistently. This prevents the oval/circle inconsistency from recurring in other topics.

### Suggestion 2 — Visual Aids as a Shell-level feature
Rather than each scaffold/practice managing its own `VisualAidsPanel`, WorkspaceModeShell could accept a `renderVisualAids` prop and render the panel in a consistent, non-intrusive position (e.g., a slide-out from the right side of the overlay, or a collapsible section below the question card). This removes the visual aids burden from every child component.

### Suggestion 3 — "Next" navigates the same batch
For practice mode, if the API already returns multiple questions, you could keep them in state but display one at a time via index navigation (cheaper than re-fetching). "Next" simply increments `currentIndex`. When the batch is exhausted, auto-fetch a new batch. This gives instant "Next" response with no loading spinner.

### Setting the standard
Once these changes are validated on Indigenous Bookkeeping, the same pattern should be applied to all other Grade 10 accounting topics (GAAP, Ethics, Internal Control, Sole Trader) and eventually all grades. The changes to WorkspaceModeShell and the new shared MCQOption component will make this rollout mostly mechanical.

---

## Verification Plan

### Manual Verification (recommended — UI-driven changes)

1. Run the app locally with `npm run dev`
2. Navigate to **Grade 10 → Accounting → Informal/Indigenous Bookkeeping**
3. Select **Scaffold mode**, pick a difficulty and subskill, click **Generate Question**
   - ✅ Verify: The WorkspaceModeShell overlay appears with blur backdrop
   - ✅ Verify: Inside the overlay, a **single white card** with the question content appears (no duplicate header, no gray-50 background behind it)
   - ✅ Verify: The button at top-right says **"Go back"** not "Change settings"
   - ✅ Verify: A **"Next"** button appears at the bottom of the overlay
4. Click **"Next"**
   - ✅ Verify: A new question loads within the same overlay (no navigation to config panel)
5. Switch to **Practice mode** and click Generate Question
   - ✅ Verify: Only **1 question** is displayed at a time (not a list of multiple questions)
   - ✅ Verify: MCQ questions have **perfectly circular** radio bullets (no ovals)
   - ✅ Verify: Clicking "Next" advances to the next question in the batch
6. Click **"Go back"**
   - ✅ Verify: Returns to the configuration panel
7. Open **Visual Aids**
   - ✅ Verify: Panel appears in a clean, non-overlapping way (slide-out or collapsible)
