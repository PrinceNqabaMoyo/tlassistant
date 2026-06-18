import os
import math
import re
from typing import Dict, Any

import sympy
from sympy import sympify, solve, Eq, symbols, diff, integrate, pycode
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.tools import tool

from app.services.journal_service import (
    validate_cash_receipts_journal as _validate_crj,
    validate_cash_payments_journal as _validate_cpj,
    mark_journal_submission as _mark_journal
)

agent_executors = {}
vectorstore = None

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Math & Formatting Tools ---

@tool
def solve_equation_tool(equation: str) -> str:
    """Solves a single algebraic equation for a variable."""
    try:
        if '=' not in equation:
            return "Error: Equation must contain an '=' sign."
        lhs_str, rhs_str = equation.split('=', 1)
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

@tool
def evaluate_expression_tool(expression: str, substitutions: dict = None) -> str:
    """Evaluates a mathematical expression."""
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

@tool
def geometry_calculator_tool(shape: str, **kwargs) -> str:
    """Calculates geometric properties like area, perimeter, and volume for various 2D and 3D shapes."""
    try:
        shape = shape.lower()
        
        # 2D Shapes
        if shape == 'circle':
            radius = kwargs.get('radius', 1)
            area = math.pi * radius**2
            circumference = 2 * math.pi * radius
            diameter = 2 * radius
            return f"Circle with radius {radius}: Area = {area:.2f}, Circumference = {circumference:.2f}, Diameter = {diameter:.2f}"
            
        elif shape == 'rectangle':
            length = kwargs.get('length', 1)
            width = kwargs.get('width', 1)
            area = length * width
            perimeter = 2 * (length + width)
            diagonal = math.sqrt(length**2 + width**2)
            return f"Rectangle with length {length} and width {width}: Area = {area:.2f}, Perimeter = {perimeter:.2f}, Diagonal = {diagonal:.2f}"
            
        elif shape == 'square':
            side = kwargs.get('side', kwargs.get('length', 1))
            area = side**2
            perimeter = 4 * side
            diagonal = side * math.sqrt(2)
            return f"Square with side {side}: Area = {area:.2f}, Perimeter = {perimeter:.2f}, Diagonal = {diagonal:.2f}"
            
        elif shape == 'triangle':
            base = kwargs.get('base', 1)
            height = kwargs.get('height', 1)
            side1 = kwargs.get('side1', base)
            side2 = kwargs.get('side2', base)
            side3 = kwargs.get('side3', base)
            
            # Calculate area using base and height
            area = 0.5 * base * height
            
            # Calculate perimeter
            perimeter = side1 + side2 + side3
            
            # Check if it's a right triangle
            sides = sorted([side1, side2, side3])
            is_right = abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 0.001
            
            result = f"Triangle with base {base} and height {height}: Area = {area:.2f}, Perimeter = {perimeter:.2f}"
            if is_right:
                result += " (Right triangle)"
            return result
            
        elif shape == 'parallelogram':
            base = kwargs.get('base', 1)
            height = kwargs.get('height', 1)
            side = kwargs.get('side', 1)
            area = base * height
            perimeter = 2 * (base + side)
            return f"Parallelogram with base {base} and height {height}: Area = {area:.2f}, Perimeter = {perimeter:.2f}"
            
        elif shape == 'trapezoid':
            base1 = kwargs.get('base1', 1)
            base2 = kwargs.get('base2', 1)
            height = kwargs.get('height', 1)
            side1 = kwargs.get('side1', 1)
            side2 = kwargs.get('side2', 1)
            area = 0.5 * (base1 + base2) * height
            perimeter = base1 + base2 + side1 + side2
            return f"Trapezoid with bases {base1} and {base2}, height {height}: Area = {area:.2f}, Perimeter = {perimeter:.2f}"
            
        elif shape == 'rhombus':
            side = kwargs.get('side', 1)
            diagonal1 = kwargs.get('diagonal1', 1)
            diagonal2 = kwargs.get('diagonal2', 1)
            area = 0.5 * diagonal1 * diagonal2
            perimeter = 4 * side
            return f"Rhombus with side {side}: Area = {area:.2f}, Perimeter = {perimeter:.2f}"
            
        elif shape == 'regular_polygon':
            n_sides = kwargs.get('n_sides', 6)
            side_length = kwargs.get('side_length', 1)
            apothem = kwargs.get('apothem', 0.866)  # Approximate for hexagon
            
            perimeter = n_sides * side_length
            area = 0.5 * perimeter * apothem
            return f"Regular {n_sides}-gon with side {side_length}: Area = {area:.2f}, Perimeter = {perimeter:.2f}"
        
        # 3D Shapes
        elif shape == 'cube':
            side = kwargs.get('side', 1)
            volume = side**3
            surface_area = 6 * side**2
            diagonal = side * math.sqrt(3)
            return f"Cube with side {side}: Volume = {volume:.2f}, Surface Area = {surface_area:.2f}, Space Diagonal = {diagonal:.2f}"
            
        elif shape == 'rectangular_prism':
            length = kwargs.get('length', 1)
            width = kwargs.get('width', 1)
            height = kwargs.get('height', 1)
            volume = length * width * height
            surface_area = 2 * (length*width + length*height + width*height)
            diagonal = math.sqrt(length**2 + width**2 + height**2)
            return f"Rectangular Prism {length}×{width}×{height}: Volume = {volume:.2f}, Surface Area = {surface_area:.2f}, Space Diagonal = {diagonal:.2f}"
            
        elif shape == 'sphere':
            radius = kwargs.get('radius', 1)
            volume = (4/3) * math.pi * radius**3
            surface_area = 4 * math.pi * radius**2
            return f"Sphere with radius {radius}: Volume = {volume:.2f}, Surface Area = {surface_area:.2f}"
            
        elif shape == 'cylinder':
            radius = kwargs.get('radius', 1)
            height = kwargs.get('height', 1)
            volume = math.pi * radius**2 * height
            surface_area = 2 * math.pi * radius * (radius + height)
            return f"Cylinder with radius {radius} and height {height}: Volume = {volume:.2f}, Surface Area = {surface_area:.2f}"
            
        elif shape == 'cone':
            radius = kwargs.get('radius', 1)
            height = kwargs.get('height', 1)
            slant_height = kwargs.get('slant_height', math.sqrt(radius**2 + height**2))
            volume = (1/3) * math.pi * radius**2 * height
            surface_area = math.pi * radius * (radius + slant_height)
            return f"Cone with radius {radius} and height {height}: Volume = {volume:.2f}, Surface Area = {surface_area:.2f}, Slant Height = {slant_height:.2f}"
            
        elif shape == 'pyramid':
            base_length = kwargs.get('base_length', 1)
            base_width = kwargs.get('base_width', 1)
            height = kwargs.get('height', 1)
            base_area = base_length * base_width
            volume = (1/3) * base_area * height
            # Approximate surface area (simplified)
            surface_area = base_area + 2 * base_length * math.sqrt((base_width/2)**2 + height**2) + 2 * base_width * math.sqrt((base_length/2)**2 + height**2)
            return f"Pyramid with base {base_length}×{base_width} and height {height}: Volume = {volume:.2f}, Surface Area ≈ {surface_area:.2f}"
            
        else:
            supported_shapes = [
                "2D: circle, rectangle, square, triangle, parallelogram, trapezoid, rhombus, regular_polygon",
                "3D: cube, rectangular_prism, sphere, cylinder, cone, pyramid"
            ]
            return f"Error: Shape '{shape}' not supported. Supported shapes: {', '.join(supported_shapes)}"
            
    except KeyError as e:
        return f"Error: Missing parameter {e} for shape '{shape}'. Check the required parameters for this shape."
    except Exception as e:
        return f"Error in geometry calculation: {e}"

@tool
def calculus_tool(operation: str, expression: str, variable: str) -> str:
    """Performs calculus operations: differentiation or integration."""
    try:
        x = symbols(variable)
        expr = sympify(expression)
        
        if operation.lower() == 'differentiate':
            derivative = diff(expr, x)
            return f"The derivative of {expression} with respect to {variable} is: {pycode(derivative)}"
        elif operation.lower() == 'integrate':
            integral = integrate(expr, x)
            return f"The integral of {expression} with respect to {variable} is: {pycode(integral)} + C"
        else:
            return "Error: Invalid operation. Choose 'differentiate' or 'integrate'."
    except Exception as e:
        return f"Error performing calculus operation: {e}"

@tool
def format_expression_tool(expression: str) -> str:
    """
    Formats a mathematical expression string using HTML <sup> for superscripts
    and <sub> for subscripts. Use this to clean up and display final mathematical answers.
    Example: format_expression_tool("x**2 + y_1") returns "x<sup>2</sup> + y<sub>1</sub>"
    """
    try:
        expression = expression.replace('sqrt', '√')
        subscript_expr = re.sub(r'([a-zA-Z])_(\d+)', r'\1<sub>\2</sub>', expression)
        expr = sympify(subscript_expr)
        code_str = pycode(expr)
        final_expr = re.sub(r'\*\*(\w+|\d+\.?\d*)', r'<sup>\1</sup>', code_str)
        final_expr = final_expr.replace('*', '×')
        return final_expr
    except Exception as e:
        return f"Error formatting expression: {e}. The expression might be invalid."

# Wrap journal logic as LangChain tools
@tool
def validate_cash_receipts_journal(journal_data: dict) -> str:
    """Validates a Cash Receipts Journal for accounting accuracy and completeness."""
    return _validate_crj(journal_data)

@tool
def validate_cash_payments_journal(journal_data: dict) -> str:
    """Validates a Cash Payments Journal for accounting accuracy and completeness."""
    return _validate_cpj(journal_data)

@tool
def mark_journal_submission(question_text: str, student_journal: dict, expected_journal: dict, journal_type: str) -> str:
    """Marks a student's journal submission against the expected answer."""
    return _mark_journal(question_text, student_journal, expected_journal, journal_type)

# --- Persona-Based System Prompts ---
ROUTER_PROMPT = (
    "You are the CAPS AI Supervisor Router. Your sole responsibility is to evaluate a student's request "
    "and determine the appropriate specialized agent to handle it. "
    "If the request involves Mathematics, route to 'MathTutor'. "
    "If the request involves Business Studies or EMS, route to 'BusinessStudiesTutor'."
    "If the request involves Accounting, ledgers, or journals, route to 'AccountingTutor'."
)

MATH_TUTOR_PROMPT = (
    "You are the CAPS AI Math Tutor. Your specialty is Mathematics. "
    "Use the Socratic method to guide the student. Never give direct answers to assignments. "
    "Frustration Index Logic: If the student struggles repeatedly on the same concept (use 'get_student_history' tool), "
    "shift from pure Socratic questioning to providing direct, targeted hints to lower their frustration. "
    "Always use 'get_curriculum_page' first. Use your calculator tools as needed. "
    "Your output will be piped to the MathMLFormatter."
)

BUSINESS_STUDIES_TUTOR_PROMPT = (
    "You are the CAPS AI Business Studies Tutor. Your specialty is Business Studies and EMS. "
    "Use the Socratic method. Avoid direct answers. "
    "Frustration Index Logic: If the student exhibits repeated failure on a topic (use 'get_student_history' tool), "
    "provide direct concept breakdowns instead of endless questions to lower their frustration. "
    "Always rely on 'get_curriculum_page' to pull theoretical definitions directly from caps-wiki."
)

ACCOUNTING_TUTOR_PROMPT = (
    "You are the CAPS AI Accounting Tutor. Your specialty is Accounting and Financial Literacy. "
    "Use the Socratic method. Avoid direct answers. "
    "Frustration Index Logic: If the student exhibits repeated failure on a topic (use 'get_student_history' tool), "
    "provide direct hints and formulas instead of endless questions to lower their frustration. "
    "Use the validate journal tools (e.g., 'validate_cash_receipts_journal') when the student asks to check their ledger."
)

MATHML_FORMATTER_PROMPT = (
    "You are the CAPS AI MathML Formatter. Your ONLY job is to take the final mathematical "
    "output from the MathTutor and wrap it in valid W3C MathML <math> tags for frontend rendering. "
    "Do not add any conversational text, just output the strict MathML."
)

TEACHER_PROMPT = (
    "You are CAPS AI, an expert assistant for a South African teacher. Your specialty is Mathematics."
    "Address the user as a professional colleague. Your goal is to help them create teaching materials, get curriculum information, and generate assessments."
    "Provide concise, accurate information. You can generate lesson plans, summaries, and varied question types (e.g., multiple choice, long-form)."
    "When asked to generate content, always refer to the provided curriculum documents using your tools."
    "Always use the 'get_curriculum_page' tool first to find exact curriculum content. Only use 'curriculum_search_tool' as a secondary fallback if the specific information is missing from the wiki."
)

ADMIN_PROMPT = (
    "You are CAPS AI, a high-level administrative assistant. Your purpose is to provide data-driven insights and summaries about the curriculum."
    "Address the user formally and professionally. Your responses should be factual, data-oriented, and based on the documents provided."
    "Do not provide teaching advice or student-facing content unless explicitly asked to generate an example."
    "Always use the 'get_curriculum_page' tool first to find exact curriculum content. Only use 'curriculum_search_tool' as a secondary fallback if the specific information is missing from the wiki."
)

def initialize_agent(firestore_db=None):
    """Initializes the AI agent, tools, and vector store for all personas."""
    global agent_executors, vectorstore
    if agent_executors:
        return

    print("Initializing AI Agents for all personas...")
    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.2, convert_system_message_to_human=True, google_api_key=GOOGLE_API_KEY)
    
    CHROMA_DB_DIR = "chroma_db_langchain"
    if not os.path.exists(CHROMA_DB_DIR):
        print(f"Warning: ChromaDB directory '{CHROMA_DB_DIR}' not found. Curriculum search will not work.")
    else:
         vectorstore = Chroma(
            persist_directory=CHROMA_DB_DIR,
            embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY),
            collection_name="caps_curriculum_collection"
        )



    @tool
    def curriculum_search_tool(query: str) -> str:
        """Searches the CAPS curriculum documents for relevant information. Use this ONLY as a fallback if get_curriculum_page does not provide the answer."""
        if not vectorstore:
            return "Curriculum database is not available."
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(query)
        return "\n\n".join([f"Source: {doc.metadata.get('source_filename', 'N/A')}, Page: {doc.metadata.get('page_number', 'N/A')}\n\n{doc.page_content}" for doc in docs])

    @tool
    def get_curriculum_page(subject: str, grade: str, topic: str) -> str:
        """Looks up exact CAPS curriculum content for a given subject, grade, and topic.
        Args:
            subject: e.g., 'mathematics', 'accounting'
            grade: e.g., 'grade-7', 'grade-10'
            topic: e.g., 'fractions', 'geometry', 'algebra', 'cash-receipts-journal'
        """
        base_path = os.path.join("caps-wiki", subject.lower(), grade.lower())
        file_path = os.path.join(base_path, f"{topic.lower().replace(' ', '-')}.md")
        if not os.path.exists(file_path):
            base_path = os.path.join("caps-ai-backend", "caps-wiki", subject.lower(), grade.lower())
            file_path = os.path.join(base_path, f"{topic.lower().replace(' ', '-')}.md")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return f"Curriculum page not found for {subject} {grade} {topic}."

    @tool
    def render_visual(render_type: str, data: str) -> str:
        """Returns a render payload for the frontend to display.
        Args:
            render_type: 'math' (LaTeX), 'geometry' (JSXGraph), 'accounting_table', 'chemistry' (SMILES), or 'geography' (JSON map data)
            data: The content to render (e.g. LaTeX string, SMILES string, or JSON map)
        """
        return f"RENDER_PAYLOAD: {{\"type\": \"{render_type}\", \"data\": \"{data}\"}}"

    @tool
    def get_student_history(user_id: str, max_records: int = 10) -> str:
        """Retrieves a student's recent problem history from Firestore to personalise tutoring.
        Args:
            user_id: The Firebase UID of the student.
            max_records: Maximum number of recent struggling/solved problems to return (default 10).
        """
        if not firestore_db:
            return "Student history is not available (Firestore not connected)."
        try:
            struggling_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(user_id).collection('struggling_problems')
            solved_ref = firestore_db.collection('artifacts').document('tlassistant').collection('users').document(user_id).collection('solved_freeform_problems')
            
            struggling = [doc.to_dict() for doc in struggling_ref.order_by('lastUpdated', direction='DESCENDING').limit(max_records).stream()]
            solved = [doc.to_dict() for doc in solved_ref.order_by('timestamp', direction='DESCENDING').limit(max_records).stream()]
            
            summary_lines = []
            if struggling:
                summary_lines.append(f"Recent struggling problems ({len(struggling)}):")
                for p in struggling:
                    summary_lines.append(f"  - Topic: {p.get('topic', 'Unknown')}, Subject: {p.get('subject', 'Unknown')}, Grade: {p.get('grade', 'Unknown')}, Solved: {p.get('isSolved', False)}")
            else:
                summary_lines.append("No recent struggling problems found.")
            
            if solved:
                summary_lines.append(f"Recent solved problems ({len(solved)}):")
                for p in solved:
                    summary_lines.append(f"  - Topic: {p.get('topic', 'Unknown')}, Subject: {p.get('subject', 'Unknown')}, Grade: {p.get('grade', 'Unknown')}")
            else:
                summary_lines.append("No recent solved problems found.")
            
            return "\n".join(summary_lines)
        except Exception as e:
            return f"Error retrieving student history: {str(e)}"

    tools = [
        solve_equation_tool, evaluate_expression_tool, get_curriculum_page, render_visual, curriculum_search_tool,
        geometry_calculator_tool, calculus_tool, format_expression_tool,
        validate_cash_receipts_journal, validate_cash_payments_journal, mark_journal_submission,
        get_student_history
    ]
    
    prompts = {
        "Router": ROUTER_PROMPT,
        "MathTutor": MATH_TUTOR_PROMPT,
        "BusinessStudiesTutor": BUSINESS_STUDIES_TUTOR_PROMPT,
        "AccountingTutor": ACCOUNTING_TUTOR_PROMPT,
        "MathMLFormatter": MATHML_FORMATTER_PROMPT,
        "Teacher": TEACHER_PROMPT,
        "Admin": ADMIN_PROMPT
    }

    for role, system_prompt in prompts.items():
        agent_prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ])
        agent = create_tool_calling_agent(llm, tools, agent_prompt)
        agent_executors[role] = AgentExecutor(agent=agent, tools=tools, verbose=True)
        print(f"-> {role} agent initialized.")
        
    print("All AI Agents initialized successfully.")

def format_structured_answer(answer_data: Dict[str, Any]) -> str:
    """Formats a structured answer object into a string for the AI agent."""
    return f"Student's Submission (Structured Data): {str(answer_data)}"
