---
name: manifest-sync
description: Synchronize fundile-architecture.json and regenerate fundile-architecture.html. Use at the start, middle, and end of coding sessions when modifying backend services, routes, frontend components, or generators.
---

# Architecture Manifest Synchronization Runbook

`fundile-architecture.json` is the single source of truth for all built components, planned items, and architectural constraints in Fundile.
`fundile-architecture.html` is generated directly from `fundile-architecture.json`.

## Mandatory Agent Rules (from `_workflow` & `AGENTS.md`)

1. **SESSION START (Rule 0a):** Read `fundile-architecture.json` in full before writing any code. Do not ask the user to explain the architecture.
2. **DURING SESSION (Rule 0b):** Whenever you build, partially build, or change the status of any layer, service, route, component, collection, or generator:
   - Move items from `planned` arrays to `built` arrays.
   - Update `"status": "planned"` to `"partial"` or `"built"`.
   - Update `"lastUpdated"` in `_meta` to today's date (`YYYY-MM-DD`).
   - Add new open questions to `openQuestions` or remove resolved ones.
3. **SESSION END (Rule 0c):** Run from the project root:
   ```bash
   python generate_architecture_html.py
   ```
   Never edit `fundile-architecture.html` directly—it is completely overwritten on each run.

---

## What Triggers a JSON Update?

| Change Made | Section to Update in `fundile-architecture.json` |
| :--- | :--- |
| New backend service or utility created | Add to `backendServices.built` |
| New API endpoint created | Add to `apiRoutes.built` |
| Question generator completed | Move from `generators.planned` to `generators.built` |
| Frontend React component built | Add to `frontendComponents.built` with layer tag |
| Firestore collection or index added | Add to `firestoreCollections.built` |
| New architectural decision or invariant agreed | Append to `designPrinciples` |
| Open design question resolved | Remove from `openQuestions` |

## What Does NOT Trigger an Update?
- Internal refactorings within an existing file.
- Bug fixes or unit test additions.
- Adding docstrings, comments, or variable renames.
- Minor styling tweaks.

---

## Step-by-Step Manifest Update Procedure

1. Open `fundile-architecture.json`.
2. Locate the appropriate section (e.g. `backendServices`, `frontendComponents`, `generators`).
3. Add or modify the entry:
   ```json
   {
     "name": "MyNewComponent",
     "path": "src/components/MyNewComponent.jsx",
     "description": "Concise summary of function and role",
     "layer": "D"
   }
   ```
4. Check that `_meta.lastUpdated` is set to the current date.
5. In terminal, execute:
   ```bash
   python generate_architecture_html.py
   ```
6. Confirm the script prints:
   `Generated: .../fundile-architecture.html (<size> KB)`
