import os
import json
import re
import math
from typing import Dict, Any, List, Optional

try:
    import sympy
    from sympy import sympify, solve, Eq, symbols, diff, integrate, pycode
except Exception:  # pragma: no cover
    sympy = None  # type: ignore
    sympify = solve = Eq = symbols = diff = integrate = pycode = None  # type: ignore

from app.services.journal_service import (
    validate_cash_receipts_journal as _validate_crj,
    validate_cash_payments_journal as _validate_cpj,
    mark_journal_submission as _mark_journal,
)
from app.services.llm_provider import get_llm_provider, BaseLLMProvider
from app.services.student_model import StudentModel
from app.services.topic_guardrail import TopicGuardrail
from app.services.generator_registry import generate_variant


# --- Singleton state ---
_llm_provider: Optional[BaseLLMProvider] = None
_student_model: Optional[StudentModel] = None
_guardrail: Optional[TopicGuardrail] = None


def _get_provider() -> BaseLLMProvider:
    global _llm_provider
    if _llm_provider is None:
        _llm_provider = get_llm_provider()
    return _llm_provider


# --- Math & formatting tools ---

def _solve_equation(equation: str) -> str:
    if sympify is None:
        return "Math tools are not available (missing sympy dependency)."
    try:
        if "=" not in equation:
            return "Error: Equation must contain an '=' sign."
        lhs_str, rhs_str = equation.split("=", 1)
        lhs = sympify(lhs_str.strip())
        rhs = sympify(rhs_str.strip())
        variables = lhs.free_symbols.union(rhs.free_symbols)
        if len(variables) == 1:
            variable = list(variables)[0]
            solution = solve(Eq(lhs, rhs), variable)
            return f"Solution: {variable} = {solution[0]}" if solution else "No unique solution found."
        return "Error: This tool can only solve equations with a single variable."
    except Exception as e:
        return f"Error solving equation: {e}"


def _evaluate_expression(expression: str, substitutions: Optional[Dict[str, Any]] = None) -> str:
    if sympify is None:
        return "Math tools are not available (missing sympy dependency)."
    try:
        expr = sympify(expression.strip())
        if substitutions:
            sym_subs = {symbols(k): v for k, v in substitutions.items()}
            result = expr.subs(sym_subs)
        else:
            result = expr.evalf() if not expr.free_symbols else expr
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}"


def _geometry_calculator(shape: str, **kwargs) -> str:
    try:
        shape = shape.lower()
        if shape == "circle":
            r = kwargs.get("radius", 1)
            return f"Circle r={r}: Area={math.pi * r ** 2:.2f}, Circumference={2 * math.pi * r:.2f}"
        if shape == "rectangle":
            l = kwargs.get("length", 1)
            w = kwargs.get("width", 1)
            return f"Rectangle {l}x{w}: Area={l * w:.2f}, Perimeter={2 * (l + w):.2f}"
        return "Supported shapes: circle, rectangle (expand as needed)."
    except Exception as e:
        return f"Error: {e}"


def _calculus(operation: str, expression: str, variable: str) -> str:
    if sympify is None:
        return "Math tools are not available (missing sympy dependency)."
    try:
        x = symbols(variable)
        expr = sympify(expression)
        if operation.lower() == "differentiate":
            return f"Derivative: {pycode(diff(expr, x))}"
        if operation.lower() == "integrate":
            return f"Integral: {pycode(integrate(expr, x))} + C"
        return "Invalid operation."
    except Exception as e:
        return f"Error: {e}"


def _format_expression(expression: str) -> str:
    if sympify is None:
        return "Math tools are not available (missing sympy dependency)."
    try:
        expression = expression.replace("sqrt", "√")
        subscript_expr = re.sub(r"([a-zA-Z])_(\d+)", r"\1<sub>\2</sub>", expression)
        expr = sympify(subscript_expr)
        code_str = pycode(expr)
        final_expr = re.sub(r"\*\*(\w+|\d+\.?\d*)", r"<sup>\1</sup>", code_str)
        return final_expr.replace("*", "×")
    except Exception as e:
        return f"Error formatting expression: {e}"


# --- Accounting journal tools ---

def _validate_crj_tool(journal_data: Dict) -> str:
    return str(_validate_crj(journal_data))


def _validate_cpj_tool(journal_data: Dict) -> str:
    return str(_validate_cpj(journal_data))


def _mark_journal_tool(question_text: str, student_journal: Dict, expected_journal: Dict, journal_type: str) -> str:
    return str(_mark_journal(question_text, student_journal, expected_journal, journal_type))


# --- Wiki & visual tools ---

def _get_curriculum_page(subject: str, grade: str, topic: str) -> str:
    subject = subject.lower()
    grade = grade.lower()
    topic = topic.lower().replace(" ", "-")
    base_paths = [
        os.path.join("caps-wiki", subject, grade),
        os.path.join("caps-ai-backend", "caps-wiki", subject, grade),
    ]
    for base_path in base_paths:
        file_path = os.path.join(base_path, f"{topic}.md")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
    return f"Curriculum page not found for {subject} {grade} {topic}."


def _render_visual(render_type: str, data: str) -> str:
    return json.dumps({"type": render_type, "data": data})


def _get_student_history(user_id: str, max_records: int = 10) -> str:
    if not _student_model or not user_id:
        return "Student history is not available."
    try:
        struggling = _student_model.get_recent_struggles(user_id, max_records)
        successes = _student_model.get_recent_successes(user_id, max_records)
        weak = []
        # We don't know subject/grade/topic here; keep the summary broad.
        lines = []
        if struggling:
            lines.append("Recent struggling problems:")
            for p in struggling:
                lines.append(f"  - {p.get('topic', 'Unknown')} ({p.get('subject', 'Unknown')} {p.get('grade', 'Unknown')})")
        else:
            lines.append("No recent struggling problems.")
        if successes:
            lines.append("Recent solved problems:")
            for p in successes:
                lines.append(f"  - {p.get('topic', 'Unknown')} ({p.get('subject', 'Unknown')} {p.get('grade', 'Unknown')})")
        else:
            lines.append("No recent solved problems.")
        return "\n".join(lines)
    except Exception as e:
        return f"Error retrieving history: {e}"


# --- Tool definitions for the prompt ---

TOOL_DESCRIPTIONS = """
You have access to the following tools. Use exactly one tool at a time by responding with a line like:
TOOL: <tool_name>(arg1="value1", arg2="value2")
Then wait for the tool result before giving your final answer.

Tools:
1. get_curriculum_page(subject, grade, topic) - Read the relevant CAPS wiki page.
2. get_student_history(user_id, max_records) - Read the student's recent struggles and successes.
3. generate_variant(topic, subskill, difficulty, count, seed) - Create a new isomorphic question from the deterministic generator.
4. render_visual(render_type, data) - Return a render payload for the frontend (math/geometry/accounting_table).
5. solve_equation(equation) - Solve an algebraic equation.
6. evaluate_expression(expression, substitutions) - Evaluate a math expression.
7. geometry_calculator(shape, **kwargs) - Compute area/perimeter for basic shapes.
8. calculus(operation, expression, variable) - Differentiate or integrate.
9. validate_cash_receipts_journal(journal_data) - Validate a CRJ.
10. validate_cash_payments_journal(journal_data) - Validate a CPJ.

Only use a tool if the student's request requires it. If the answer is contained in the curriculum context provided, answer directly.
""".strip()


# --- Agent prompt ---

def _build_system_prompt(context: Dict[str, Any]) -> str:
    subject = context.get("subject", "the current subject")
    grade = context.get("grade", "")
    topic = context.get("topic", "the current topic")
    subskill = context.get("subskill", "")
    sample_answer = context.get("sample_answer", "")
    marking_points = context.get("marking_points", [])
    wiki = context.get("wiki_content", "")

    prompt = f"""You are a CAPS-aligned tutor for South African schools. You are helping a student with {subject} {grade} - {topic}.
Current subskill: {subskill}

You are a Socratic tutor. Never give the full answer to an assignment question. Ask guiding questions, give hints, and help the student discover the answer.

Strict rules:
- Stay on the current topic.
- If the student asks something off-topic, decline and redirect them to {topic}.
- You may only use the generator tool to create another isomorphic question; you must not invent your own questions.
- For math questions, use the calculator tools if needed.
- For accounting questions, use the journal tools if needed.

{TOOL_DESCRIPTIONS}

Curriculum context:
{wiki}

Sample answer for the current question (do not reveal unless the student is truly stuck):
{sample_answer}

Marking points (do not reveal unless the student is truly stuck):
{json.dumps(marking_points)}
"""
    return prompt


# --- Tool execution router ---

def _execute_tool_call(tool_line: str) -> str:
    """Parses and executes a tool call of the form: TOOL: name(args)"""
    match = re.match(r"TOOL:\s*(\w+)\s*\((.*)\)\s*$", tool_line.strip(), re.DOTALL)
    if not match:
        return "Error: Invalid tool call format."

    tool_name = match.group(1)
    args_str = match.group(2).strip()

    # Try JSON object first (for dict arguments like journal_data)
    kwargs: Dict[str, Any] = {}
    if args_str.startswith("{"):
        try:
            kwargs = json.loads(args_str)
        except json.JSONDecodeError:
            return "Error: Invalid JSON arguments."
    else:
        # Parse simple keyword arguments (supports strings, ints)
        for key, value in re.findall(r"(\w+)\s*=\s*(?:\"(.*?)\"|(\d+))", args_str):
            kwargs[key] = value[0] if value[0] else int(value[1])

    if tool_name == "get_curriculum_page":
        return _get_curriculum_page(kwargs.get("subject", ""), kwargs.get("grade", ""), kwargs.get("topic", ""))
    if tool_name == "get_student_history":
        return _get_student_history(kwargs.get("user_id", ""), kwargs.get("max_records", 10))
    if tool_name == "generate_variant":
        try:
            questions = generate_variant(
                topic=kwargs.get("topic", ""),
                subskill=kwargs.get("subskill", "concepts"),
                difficulty=kwargs.get("difficulty", "medium"),
                count=kwargs.get("count", 1),
                seed=kwargs.get("seed", None),
            )
            return json.dumps(questions, default=str)
        except Exception as e:
            return f"Error generating variant: {e}"
    if tool_name == "render_visual":
        return _render_visual(kwargs.get("render_type", ""), kwargs.get("data", ""))
    if tool_name == "solve_equation":
        return _solve_equation(kwargs.get("equation", ""))
    if tool_name == "evaluate_expression":
        return _evaluate_expression(kwargs.get("expression", ""), kwargs.get("substitutions"))
    if tool_name == "geometry_calculator":
        shape = kwargs.get("shape", "")
        return _geometry_calculator(shape, **{k: v for k, v in kwargs.items() if k != "shape"})
    if tool_name == "calculus":
        return _calculus(kwargs.get("operation", ""), kwargs.get("expression", ""), kwargs.get("variable", ""))
    if tool_name == "validate_cash_receipts_journal":
        return _validate_crj_tool(kwargs.get("journal_data", {}))
    if tool_name == "validate_cash_payments_journal":
        return _validate_cpj_tool(kwargs.get("journal_data", {}))

    return f"Error: Unknown tool '{tool_name}'."


# --- Initialization ---

def initialize_agent(firestore_db=None):
    global _student_model, _guardrail
    _student_model = StudentModel(firestore_db) if firestore_db else None
    _guardrail = TopicGuardrail(_student_model)
    print("AI Tutor initialized with provider:", _get_provider().__class__.__name__)


def get_student_model() -> Optional[StudentModel]:
    return _student_model


# --- Main entry point ---

def run_agent(
    user_input: str,
    context: Dict[str, Any],
    chat_history: Optional[List[Dict[str, str]]] = None,
    user_id: Optional[str] = None,
    tier: str = "standard",
) -> Dict[str, Any]:
    """Runs the topic-bound tutor agent.

    Context must include: subject, grade, topic, subskill, sample_answer, marking_points, wiki_content.
    Returns: {"text": str, "render": Optional[Dict], "variant": Optional[Dict]}
    """
    if tier != "pro":
        return {"text": "AI tutoring is available in the Pro package only.", "render": None, "variant": None}

    if not all(k in context for k in ("subject", "grade", "topic", "subskill")):
        return {"text": "Missing question context. Please start from a topic.", "render": None, "variant": None}

    # Auto-populate wiki content if the frontend did not provide it.
    if not context.get("wiki_content"):
        context["wiki_content"] = _get_curriculum_page(
            context["subject"], context["grade"], context["topic"]
        )

    if _guardrail:
        guard_result = _guardrail.check(
            user_input,
            context["subject"],
            context["grade"],
            context["topic"],
            user_id=user_id,
        )
        if not guard_result["allowed"]:
            return {
                "text": "I'm here to help with your current topic. Let's stay focused on that. You can ask me to explain a hint, show another example, or explain why an answer is wrong.",
                "render": None,
                "variant": None,
            }

    provider = _get_provider()
    system_prompt = _build_system_prompt(context)

    def _norm_role(msg: Dict[str, str]) -> Dict[str, str]:
        role_map = {"human": "user", "ai": "assistant", "system": "system", "user": "user", "assistant": "assistant"}
        return {"role": role_map.get(msg.get("role", "user"), "user"), "content": msg.get("content", "")}

    messages = [{"role": "system", "content": system_prompt}]
    if user_id:
        messages.append({"role": "user", "content": f"Student ID: {user_id}"})
    if chat_history:
        messages.extend([_norm_role(m) for m in chat_history])
    messages.append({"role": "user", "content": user_input})

    # Simple tool loop: up to 3 iterations to prevent runaway calls.
    tool_results = []
    for _ in range(3):
        full_prompt = "\n".join(
            [m["content"] for m in messages]
            + [f"Tool result: {tr}" for tr in tool_results]
            + ["\nNow respond to the student. If you need a tool, use the TOOL: format."]
        )

        response = provider.invoke(messages=[{"role": "user", "content": full_prompt}])
        tool_match = re.search(r"^\s*TOOL:\s*\w+\s*\(.*\)\s*$", response, re.MULTILINE)
        if not tool_match:
            break

        tool_line = tool_match.group(0)
        tool_result = _execute_tool_call(tool_line)
        tool_results.append(f"{tool_line} -> {tool_result}")
        messages.append({"role": "assistant", "content": tool_line})
        messages.append({"role": "user", "content": f"Tool result: {tool_result}"})

    # Extract render payload if present
    render = None
    render_match = re.search(r'RENDER_PAYLOAD:\s*(\{.*?\})', response, re.DOTALL)
    if render_match:
        try:
            render = json.loads(render_match.group(1))
        except json.JSONDecodeError:
            pass

    # Extract variant payload if present
    variant = None
    variant_match = re.search(r'VARIANT_PAYLOAD:\s*(\{.*?\})', response, re.DOTALL)
    if variant_match:
        try:
            variant = json.loads(variant_match.group(1))
        except json.JSONDecodeError:
            pass

    return {"text": response, "render": render, "variant": variant}


def format_structured_answer(answer_data: Dict[str, Any]) -> str:
    """Formats a structured answer object into a string for the AI agent."""
    return f"Student's Submission (Structured Data): {str(answer_data)}"
