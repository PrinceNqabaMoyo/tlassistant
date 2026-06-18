
import math
import random
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass
class GeneratedQuestion:
    prompt: str
    answer: Any
    explanation: str
    question_type: str
    options: Optional[List[str]] = None
    metadata: Optional[Dict[str, Any]] = None
 
 
def _rng(seed: Optional[int]) -> random.Random:
    return random.Random(seed if seed is not None else 0)


def _choice(r: random.Random, items: List[Any]) -> Any:
    return items[r.randrange(0, len(items))]


def _format_frac(n: int, d: int) -> str:
     if d == 0:
         raise ValueError("Denominator cannot be 0")
     if n == 0:
         return "0"
     sign = "-" if (n < 0) ^ (d < 0) else ""
     n_abs = abs(n)
     d_abs = abs(d)
     g = math.gcd(n_abs, d_abs)
     n_abs //= g
     d_abs //= g
     if d_abs == 1:
         return f"{sign}{n_abs}"
     return f"{sign}{n_abs}/{d_abs}"
 
 
def _safe_int(v: Any) -> int:
     if isinstance(v, bool):
         raise ValueError("Invalid integer")
     return int(v)
 
 
def _normalize_question_type(question_type: Optional[str]) -> str:
     qt = (question_type or "typed").strip().lower()
     return qt if qt in {"typed", "mcq"} else "typed"
 
 
SubskillGenerator = Callable[[random.Random, str, str], GeneratedQuestion]
 
 
SUBSKILLS: Dict[str, SubskillGenerator] = {}
 
 
def register_subskill(name: str) -> Callable[[SubskillGenerator], SubskillGenerator]:
     def _decorator(fn: SubskillGenerator) -> SubskillGenerator:
         SUBSKILLS[name] = fn
         return fn
 
     return _decorator


def _linear_expr(a: int, q: int) -> str:
     if a == 0:
         raise ValueError("a cannot be 0 for an invertible linear function")
     if q == 0:
         return f"f(x) = {a}x"
     sign = "+" if q > 0 else "-"
     return f"f(x) = {a}x {sign} {abs(q)}"


def _linear_inverse_expr(a: int, q: int) -> str:
     # f(x)=ax+q => f^-1(x) = (x-q)/a
     if a == 0:
         raise ValueError("a cannot be 0")

     q_part = "" if q == 0 else (f" - {q}" if q > 0 else f" + {abs(q)}")
     if a == 1:
         return f"f^-1(x) = x{q_part}"
     if a == -1:
         return f"f^-1(x) = -(x{q_part})"
     return f"f^-1(x) = (x{q_part})/{a}"


@register_subskill("inverse_linear_find_inverse")
def _inverse_linear_find_inverse(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     a_choices = [2, 3, 4, 5, -2, -3, -4, -5]
     q_choices = [0, 1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
     a = _choice(r, a_choices)
     q = _choice(r, q_choices)

     prompt = f"Given {_linear_expr(a, q)}, determine f^-1(x)."
     answer = _linear_inverse_expr(a, q)
     explanation = "Swap x and y then solve for y: x = ay + q => y = (x - q)/a."
     if qt == "mcq":
         wrong_1 = _linear_inverse_expr(a, -q)
         wrong_2 = _linear_inverse_expr(-a, q)
         wrong_3 = f"f^-1(x) = {a}x {('+ ' + str(q)) if q >= 0 else ('- ' + str(abs(q)))}"
         options = [answer, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=answer,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "inverse_linear_find_inverse", "a": a, "q": q},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=answer,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "inverse_linear_find_inverse", "a": a, "q": q},
     )


@register_subskill("inverse_linear_intercepts_swap")
def _inverse_linear_intercepts_swap(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     a = _choice(r, [1, 2, 3, 4, 5, -1, -2, -3, -4, -5])
     while a == 0:
         a = _choice(r, [2, 3, 4, 5, -2, -3, -4, -5])
     q = _choice(r, [1, 2, 3, 4, 5, -1, -2, -3, -4, -5])

     # f(x)=ax+q => y-int (0,q). x-int (-q/a,0)
     x_int = _format_frac(-q, a)
     # inverse intercepts swapped: (0, x_int) and (q,0)
     prompt = (
         f"Let {_linear_expr(a, q)} and f^-1 be its inverse. "
         "Write down the intercepts of f^-1."
     )
     answer = f"(0; {x_int}) and ({q}; 0)"
     explanation = "For an inverse, points (x,y) swap to (y,x). So intercepts swap as well."
     if qt == "mcq":
         wrong_1 = f"(0; {q}) and ({x_int}; 0)"
         wrong_2 = f"(0; {x_int}) and ({-q}; 0)"
         wrong_3 = f"(0; {q}) and ({q}; 0)"
         options = [answer, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=answer,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "inverse_linear_intercepts_swap", "a": a, "q": q},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=answer,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "inverse_linear_intercepts_swap", "a": a, "q": q},
     )


@register_subskill("exp_to_log_convert")
def _exp_to_log_convert(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     base = _choice(r, [2, 3, 4, 5, 10])
     power = _choice(r, [2, 3, 4, 5, -2, -3])
     if power >= 0:
         value = base**power
         exp = f"{base}^{power} = {value}"
         ans = f"{power} = log_{base} {value}"
     else:
         # represent as fraction if possible
         value = _format_frac(1, base ** abs(power))
         exp = f"{base}^{power} = {value}"
         ans = f"{power} = log_{base} {value}"

     prompt = f"Write the following in logarithmic form: {exp}"
     explanation = "Use x = b^y  <=>  y = log_b x."
     if qt == "mcq":
         wrong_1 = f"{base} = log_{power} {value}"
         wrong_2 = f"{value} = log_{base} {power}"
         wrong_3 = f"{power} = log {value}"
         options = [ans, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=ans,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "exp_to_log_convert", "base": base, "power": power},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=ans,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "exp_to_log_convert", "base": base, "power": power},
     )


@register_subskill("log_to_exp_convert")
def _log_to_exp_convert(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     base = _choice(r, [2, 3, 4, 5, 10])
     power = _choice(r, [2, 3, 4, 5, -2, -3])
     if power >= 0:
         value = base**power
     else:
         value = _format_frac(1, base ** abs(power))
     log_form = f"log_{base} {value} = {power}"
     ans = f"{base}^{power} = {value}"
     prompt = f"Write the following in exponential form: {log_form}"
     explanation = "Use y = log_b x  <=>  x = b^y."
     if qt == "mcq":
         wrong_1 = f"{value}^{base} = {power}"
         wrong_2 = f"{base}^{value} = {power}"
         wrong_3 = f"{base}^{power} = {base**abs(power) if isinstance(value, int) else base**abs(power)}"
         options = [ans, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=ans,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "log_to_exp_convert", "base": base, "power": power},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=ans,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "log_to_exp_convert", "base": base, "power": power},
     )


@register_subskill("log_power_law_simplify")
def _log_power_law_simplify(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     base = _choice(r, [2, 3, 4, 5, 10])
     inner_base = _choice(r, [2, 3, 5])
     k = _choice(r, [2, 3, 4, 5])
     m = _choice(r, [2, 3, 4])

     # log_a (b^{k})^{m} = km log_a b
     prompt = f"Simplify: log_{base} ({inner_base}^{k})^{m}"
     ans = f"{k*m} log_{base} {inner_base}"
     explanation = "Use log_a(x^b) = b log_a x."
     if qt == "mcq":
         wrong_1 = f"{k+m} log_{base} {inner_base}"
         wrong_2 = f"{k*m} log_{inner_base} {base}"
         wrong_3 = f"log_{base} {inner_base}^{k*m}"
         options = [ans, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=ans,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "log_power_law_simplify", "base": base, "inner_base": inner_base, "k": k, "m": m},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=ans,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "log_power_law_simplify", "base": base, "inner_base": inner_base, "k": k, "m": m},
     )


@register_subskill("log_change_of_base")
def _log_change_of_base(r: random.Random, difficulty: str, question_type: str) -> GeneratedQuestion:
     qt = _normalize_question_type(question_type)
     a = _choice(r, [2, 3, 4, 5, 7, 10])
     b = _choice(r, [2, 3, 5, 10])
     x = _choice(r, [2, 3, 4, 5, 8, 9, 16, 25, 27, 32])
     while a == 1 or b == 1 or a == b:
         a = _choice(r, [2, 3, 4, 5, 7, 10])
         b = _choice(r, [2, 3, 5, 10])

     prompt = f"Use change of base to rewrite log_{a} {x} in terms of base {b}."
     ans = f"log_{b} {x} / log_{b} {a}"
     explanation = "Use log_a x = (log_b x)/(log_b a)."
     if qt == "mcq":
         wrong_1 = f"log_{b} {a} / log_{b} {x}"
         wrong_2 = f"log_{a} {b} / log_{b} {x}"
         wrong_3 = f"log_{b} {x} * log_{b} {a}"
         options = [ans, wrong_1, wrong_2, wrong_3]
         r.shuffle(options)
         return GeneratedQuestion(
             prompt=prompt,
             answer=ans,
             explanation=explanation,
             question_type="mcq",
             options=options,
             metadata={"subskill": "log_change_of_base", "a": a, "b": b, "x": x},
         )
     return GeneratedQuestion(
         prompt=prompt,
         answer=ans,
         explanation=explanation,
         question_type="typed",
         metadata={"subskill": "log_change_of_base", "a": a, "b": b, "x": x},
     )


def list_subskills() -> List[str]:
    return sorted(SUBSKILLS.keys())


def _to_dict(q: GeneratedQuestion) -> Dict[str, Any]:
    md = q.metadata or {}
    return {
        "question": q.prompt,
        "correct_answer": q.answer,
        "explanation": q.explanation,
        "options": q.options,
        "subskill": md.get("subskill"),
    }
def generate_questions(
     subskill: Optional[str] = None,
     difficulty: str = "easy",
     question_type: str = "typed",
     count: int = 1,
     seed: Optional[int] = None,
 ) -> Dict[str, Any]:
     qt = _normalize_question_type(question_type)
     n = max(1, min(20, _safe_int(count)))
     r = _rng(seed)

     if subskill:
         if subskill not in SUBSKILLS:
             return {
                 "ok": False,
                 "error": f"Unknown subskill: {subskill}",
                 "available_subskills": list_subskills(),
             }
         chosen = [subskill] * n
     else:
         keys = list_subskills()
         chosen = [keys[i % len(keys)] for i in range(n)]
         r.shuffle(chosen)

     questions: List[Dict[str, Any]] = []
     for i, sk in enumerate(chosen):
         # offset seed deterministically per question
         ri = _rng((seed or 0) + 9973 * (i + 1))
         q = SUBSKILLS[sk](ri, difficulty, qt)
         questions.append(_to_dict(q))

     return {
         "ok": True,
         "topic": "grade12_functions",
         "seed": seed if seed is not None else 0,
         "subskill": subskill,
         "difficulty": difficulty,
         "question_type": qt,
         "count": n,
         "available_subskills": list_subskills(),
         "questions": questions,
     }

