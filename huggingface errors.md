# Hugging Face Deployment & Startup Status

**Status:** RESOLVED & RUNNING (HTTP 200 OK)  
**Last Verified:** 2026-09-27  
**Backend URL:** https://snombi-tlassistant.hf.space/  

---

### Root Cause
Python 3.11 in the Hugging Face Docker container (`python:3.11-slim`) strictly rejects backslashes inside f-string `{...}` replacement fields (PEP 701 backslash support in f-string expressions was introduced in Python 3.12+).

The offending files were:
1. `caps-ai-backend/app/utils/grade10_mathematics/term_2/functions_generator.py` (Line 626):
   - Backslash in LaTeX `\cdot` inside ternary expression in f-string.
2. `caps-ai-backend/app/utils/grade11_mathematics/probability_contingency_generator.py` (Lines 220 & 308):
   - Backslash in LaTeX `\neq` inside ternary expression in f-string.
3. `caps-ai-backend/app/utils/grade12_physical_sciences/momentum_impulse_generator.py` (Line 328):
   - Backslash in LaTeX `\le` inside ternary expression in f-string.

---

### Fix & Verification
1. Extracted all LaTeX expressions containing backslashes into external variables (`a_prefix`, `rel_sym`, `comp_sym`, `ineq_sym`) before string formatting.
2. Verified 0 remaining f-string backslash occurrences across the entire backend via AST scanner (`scratch/find_real_fstring_backslashes.py`).
3. Ran `python -m compileall caps-ai-backend/app` cleanly with exit code 0.
4. Uploaded fixed files to Hugging Face Space `snombi/tlassistant`.
5. Hugging Face Space rebuilt Docker container, booted Gunicorn worker with PID 7, and reached `RUNNING` stage.
6. Verified live endpoints:
   - `GET /` -> `{"message":"TLAssistant Backend API is running.","status":"ok"}` (200 OK)
   - `POST /api/generate` for Grade 10 Functions -> `{"success": true, "total_questions": 1}` (200 OK)

---

### Historical Startup Error (Resolved)
```
[2026-09-27 16:22:20 +0000] [7] [ERROR] Exception in worker process
  File "/code/app/utils/grade10_mathematics/term_2/functions_generator.py", line 626
    eq = f"f(x) = {('' if a == 1 else ('-' if a == -1 else num(a) + ' \\cdot '))}{b}^{{x}} {_signed(q)}"
SyntaxError: f-string expression part cannot include a backslash
```
