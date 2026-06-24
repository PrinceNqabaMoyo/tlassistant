# Implementation Plan — Gr10 Mathematics, Term 1: Exponents

**Status:** outstanding (Algebra ✅ + Trig ✅ already shipped in PR #6). This is topic 2 of the 5 Term-1 topics.
**Pattern to follow:** same deterministic SymPy stack proven by `algebraic_expressions_generator.py` (seeded RNG → SymPy computes answer + canonical solution graph → KaTeX + comma decimals → Procedure Tracker marks working). **No LLM in the generator.**

Source doc: `caps-ai-backend/curriculum_docs/Mathematics_Gr10/Term 1/2 Exponents .md` (1330 lines).

## Embedded-comment compliance
- `^` is a WordPad limitation → render exponents as **true superscripts** (KaTeX `^{...}`). ✓ already how MathText works.
- Fractions must render as proper stacked fractions; brackets/spaces only where mathematically required. ✓ `to_latex()` already does `\frac`.
- Use **comma decimals** (`0{,}008`, `0{,}25`). ✓ shared helper.
- "Always write the final answer with **positive exponents**." → answer-form rule (see `answer_mode` below).

## Subskills (generators), with archetypes from the doc

| key | what it tests | answer mode | example seed-archetype |
|-----|---------------|-------------|------------------------|
| `zero_negative_exponents` | `a^0=1`, `a^{-n}=1/a^n`, simple negatives | `expression` (positive exps) | `16^0`, `16a^0`, `2^{-2}/3^2`, `(2/3)^{-3}` |
| `laws_monomial` | product/quotient/power laws on monomials | `expression` | `x^2 x^{3t+1}`, `32p^2/4p^8`, `(2t^4)^3`, `(2a^4)(3ab^2)` |
| `laws_with_brackets` | `(ab)^n`, `(a/b)^n`, nested powers | `expression` | `(3x)^2`, `(a^6/b^7)^5`, `[3^{n+3}]^2` |
| `prime_base_simplify` | rewrite to prime bases, then simplify | `expression` (single value or prime-power) | `[2^{2n}·4^n·2]/16^n = 2`, `[5^{2x-1}9^{x-2}]/15^{2x-3}` |
| `common_factor_exponents` | factor `a^t` out of sums, cancel | `value`/`expression` | `[2^t − 2^{t−2}]/[3·2^t − 2^t] = 3/8` |
| `difference_of_squares_exp` | `9^x−1 = (3^x)^2−1` factorise | `expression` | `(9^x−1)/(3^x+1) = 3^x − 1` |
| `rational_exponents` | `a^{1/n}`, roots, mixed | `expression`/`value` | `2x^{1/2}·4x^{-1/2}=8`, `(0{,}008)^{1/3}=1/5`, `(27)^{-1/3}` |
| `exponential_equations` | equate bases & solve (linear/quadratic/common-factor) | `steps` (Procedure Tracker) + `set` | `3^{x+1}=9 → x=1`, `5^t+3·5^{t+1}=400 → t=2`, `p−13p^{1/2}+36=0 → {16,81}` |

> Term-1 scope note: `2^x = 7` "trial and error to 2 d.p." and the digit-count / proof questions (doc Q7, Q8) are **enrichment** — out of scope for the first deterministic pass (no clean single archetype). Flag for a later "challenge" tier.

## Generator design (per subskill)
Reuse `_math_common.py` helpers exactly as Algebra did:
- `rng(seed, subskill)` → deterministic params (bases from small primes {2,3,5,7,10,11,13}, exponents as seeded linear forms in a symbol like `n`,`x`,`t`).
- Build the SymPy expression, compute the simplified result with `sympy.powsimp`/`sympy.simplify` under positive-exponent normalisation (`sympy.Pow` rewrite; force `a**-n → 1/a**n` for display).
- Emit canonical solution graph via `step()`/`solution()` — each law application is one transition with `op` (e.g. "add exponents (same base)"), `rule` (e.g. "a^m·a^n = a^{m+n}"), and `common_errors`.
- `make_short(...)` for one-line answers; `make_steps(...)` for `exponential_equations`.

### Answer-form enforcement (critical)
Add an `answer_mode="expression_positive_exponents"` normaliser to `_math_common.py`: a learner answer is correct iff it is **symbolically equal** to the key AND contains no negative exponents (so `2x^{-2}` is marked "simplify further: positive exponents" not "correct"). This mirrors the Algebra `expanded`/`factored` form-locks.

### Canonical `common_errors` to encode (for Procedure Tracker + hints)
- `multiply_instead_of_add_exponents` (`a^m·a^n → a^{mn}`)
- `subtract_wrong_direction` (`a^m/a^n → a^{n−m}`)
- `distribute_power_over_sum` (`(a+b)^n → a^n+b^n`) — doc Q6 explicitly lists this misconception
- `coefficient_raised_wrongly` (`(3x)^2 → 3x^2`)
- `negative_exponent_sign` (`a^{-n} → −a^n`)
- `zero_exponent` (`a^0 → 0`)

## Frontend
- **No new components needed** — reuses `MathText`, `WorkingPad`, `MathAnswerArea`, `useMathController`, `createMathTopicRegistry`.
- **Keypad additions** (registry-driven, per the doc's "specialised keypad" comment): superscript `x^n` and `x^2` (already exist), plus an **n-th root** `\sqrt[n]{}` key and a **negative-exponent** quick token. Add to `mathKeypadRegistry` under an `exponents` group.
- Register `grade10_math_exponents` in `grade10MathematicsNewRegistry` (override any legacy Exponents modes).

## Backend wiring
- New file `caps-ai-backend/app/utils/grade10_mathematics/term_1/exponents_generator.py`.
- Add to `_math_curriculum.py` `TOPICS["grade10_math_exponents"]` with the 8 subskills + scaffold sections.
- Register in `app/api/grade10_mathematics.py` `GENERATORS` dict. Marking reuses the existing `math_short` / `math_steps` paths — no new marking branch.

## Adaptive metadata (per question, via `with_metadata`)
`learning_objective_id` (e.g. `g10.exp.laws`), `misconception_tags` (from `common_errors`), `diagnostic_tags`, `minimum_mastery_score`, `keywords`.

## Testing
- Determinism: `generate(seed=42)` byte-identical across processes.
- Exercise all 8 subskills: valid SymPy + KaTeX + (for equations) canonical solution graph.
- Procedure Tracker: feed a correct multi-line solution to `5^t+3·5^{t+1}=400` → full method+accuracy marks; feed a `multiply_instead_of_add_exponents` slip → localised first-error + carry-over.
- Frontend: scaffold/practice render; keypad shows root key; comma decimals accepted.
- `npm run build` green.

## Estimated surface
~1 backend generator file (~350–450 lines), ~30 lines across `_math_common.py` (form normaliser) + `_math_curriculum.py` + API + registry + keypad registry. No new React components.
