from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from fastapi import FastAPI

import os
import math
import re
import json
from dotenv import load_dotenv
from typing import Optional, Union, Dict, Any
import sympy
from sympy import sympify, solve, Eq, S, symbols, diff, integrate, pycode
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.tools import tool
import datetime

# --- Firebase Admin SDK Imports ---
from firebase_admin import credentials, firestore, initialize_app

# --- Initial Setup ---
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY not found. The application will not be able to connect to the Gemini API.")

app = Flask(__name__)
CORS(app)

# --- FastAPI Sub-Applications for specialized modules ---
grade10_acct_app = FastAPI(title="Grade 10 Accounting API")

# Setup CORS for FastAPI as well
from fastapi.middleware.cors import CORSMiddleware
grade10_acct_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.grade10_accounting import router as grade10_acct_router
grade10_acct_app.include_router(grade10_acct_router)

# Mount FastAPI app onto Flask using DispatcherMiddleware
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/api/accounting/grade10': grade10_acct_app
})


# --- Firebase Admin SDK Initialization ---
# IMPORTANT: Replace 'path/to/your/serviceAccountKey.json' with the actual path
# to your Firebase service account key file. This file contains the credentials
# your backend needs to authenticate with Firestore.
# Ensure this block runs only once.
try:
    # Attempt to get an existing Firebase app to avoid re-initialization errors
    firestore_db = firestore.client()
    print("Firebase Admin SDK already initialized.")
except ValueError:
    # If not initialized, proceed with initialization
    # Make sure your service account key file is accessible to your Flask app.
    # For production, consider using environment variables for the path or directly
    # for the credentials JSON string.
    try:
        cred = credentials.Certificate("caps-ai-math-assistant-app-firebase-adminsdk-fbsvc-16f0a819d2.json") # !!! REPLACE THIS PATH !!!
        initialize_app(cred)
        firestore_db = firestore.client()
        print("Firebase Admin SDK initialized successfully.")
    except Exception as e:
        print(f"Error initializing Firebase Admin SDK: {e}")
        print("Firestore operations may fail.")

# --- Initialize LLM Rate Limiter with Firestore ---
try:
    from app.utils.llm_rate_limiter import init_firestore as init_llm_rate_limiter
    init_llm_rate_limiter(firestore_db)
    print("LLM Rate Limiter initialized with Firestore.")
except Exception as e:
    print(f"Warning: Could not initialize LLM Rate Limiter: {e}")

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
        # First, handle common function names to avoid them being treated as variables
        expression = expression.replace('sqrt', '√')

        # Use regex to find patterns like variable_number for subscripts
        subscript_expr = re.sub(r'([a-zA-Z])_(\d+)', r'\1<sub>\2</sub>', expression)

        # Sympify the expression after subscript replacement to validate it
        expr = sympify(subscript_expr)

        # Convert the sympy expression to a Python code string (e.g., "x**2")
        code_str = pycode(expr)

        # Use regex to replace Python's power operator (**) with HTML <sup> tags
        final_expr = re.sub(r'\*\*(\w+|\d+\.?\d*)', r'<sup>\1</sup>', code_str)
        
        # Replace multiplication sign
        final_expr = final_expr.replace('*', '×')

        return final_expr
    except Exception as e:
        return f"Error formatting expression: {e}. The expression might be invalid."

# --- Journal Processing Tools ---

@tool
def validate_cash_receipts_journal(journal_data: dict) -> str:
    """Validates a Cash Receipts Journal for accounting accuracy and completeness."""
    try:
        if not journal_data or 'rows' not in journal_data:
            return "Error: Invalid journal data structure."
        
        rows = journal_data.get('rows', [])
        if not rows:
            return "Error: No journal entries found."
        
        total_analysis = 0
        total_bank = 0
        total_income = 0
        total_sundry = 0
        errors = []
        
        for i, row in enumerate(rows, 1):
            # Calculate row totals
            analysis = float(row.get('analysis', {}).get('main', 0) or 0) + float(row.get('analysis', {}).get('cents', 0) or 0) / 100
            bank = float(row.get('bank', {}).get('main', 0) or 0) + float(row.get('bank', {}).get('cents', 0) or 0) / 100
            income = float(row.get('income', {}).get('main', 0) or 0) + float(row.get('income', {}).get('cents', 0) or 0) / 100
            sundry = float(row.get('sundry_amount', {}).get('main', 0) or 0) + float(row.get('sundry_amount', {}).get('cents', 0) or 0) / 100
            
            total_analysis += analysis
            total_bank += bank
            total_income += income
            total_sundry += sundry
            
            # Check for required fields
            if not row.get('doc'):
                errors.append(f"Row {i}: Missing document number")
            if not row.get('day'):
                errors.append(f"Row {i}: Missing day")
            if not row.get('details'):
                errors.append(f"Row {i}: Missing details")
        
        # Check balancing
        if abs(total_bank - (total_income + total_sundry)) > 0.01:
            errors.append(f"Journal not balanced: Bank ({total_bank:.2f}) ≠ Income ({total_income:.2f}) + Sundry ({total_sundry:.2f})")
        
        if errors:
            return f"Validation failed:\n" + "\n".join(errors)
        else:
            return f"Journal is valid and balanced.\nTotals: Analysis={total_analysis:.2f}, Bank={total_bank:.2f}, Income={total_income:.2f}, Sundry={total_sundry:.2f}"
            
    except Exception as e:
        return f"Error validating journal: {str(e)}"

@tool
def validate_cash_payments_journal(journal_data: dict) -> str:
    """Validates a Cash Payments Journal for accounting accuracy and completeness."""
    try:
        if not journal_data or 'rows' not in journal_data:
            return "Error: Invalid journal data structure."
        
        rows = journal_data.get('rows', [])
        if not rows:
            return "Error: No journal entries found."
        
        total_bank = 0
        total_consumables = 0
        total_wages = 0
        total_sundry = 0
        errors = []
        
        for i, row in enumerate(rows, 1):
            # Calculate row totals
            bank = float(row.get('bank', {}).get('main', 0) or 0) + float(row.get('bank', {}).get('cents', 0) or 0) / 100
            consumables = float(row.get('consumables', {}).get('main', 0) or 0) + float(row.get('consumables', {}).get('cents', 0) or 0) / 100
            wages = float(row.get('wages', {}).get('main', 0) or 0) + float(row.get('wages', {}).get('cents', 0) or 0) / 100
            sundry = float(row.get('sundry_amount', {}).get('main', 0) or 0) + float(row.get('sundry_amount', {}).get('cents', 0) or 0) / 100
            
            total_bank += bank
            total_consumables += consumables
            total_wages += wages
            total_sundry += sundry
            
            # Check for required fields
            if not row.get('doc'):
                errors.append(f"Row {i}: Missing document number")
            if not row.get('day'):
                errors.append(f"Row {i}: Missing day")
            if not row.get('payee'):
                errors.append(f"Row {i}: Missing payee name")
        
        # Check balancing
        if abs(total_bank - (total_consumables + total_wages + total_sundry)) > 0.01:
            errors.append(f"Journal not balanced: Bank ({total_bank:.2f}) ≠ Consumables ({total_consumables:.2f}) + Wages ({total_wages:.2f}) + Sundry ({total_sundry:.2f})")
        
        if errors:
            return f"Validation failed:\n" + "\n".join(errors)
        else:
            return f"Journal is valid and balanced.\nTotals: Bank={total_bank:.2f}, Consumables={total_consumables:.2f}, Wages={total_wages:.2f}, Sundry={total_sundry:.2f}"
            
    except Exception as e:
        return f"Error validating journal: {str(e)}"

@tool
def mark_journal_submission(question_text: str, student_journal: dict, expected_journal: dict, journal_type: str) -> str:
    """Marks a student's journal submission against the expected answer."""
    try:
        if journal_type.lower() == 'crj':
            student_validation = validate_cash_receipts_journal(student_journal)
            expected_validation = validate_cash_receipts_journal(expected_journal)
        elif journal_type.lower() == 'cpj':
            student_validation = validate_cash_payments_journal(student_journal)
            expected_validation = validate_cash_payments_journal(expected_journal)
        else:
            return f"Error: Unknown journal type '{journal_type}'. Supported types: CRJ, CPJ"
        
        # Check if student journal is valid
        if "Error" in student_validation or "failed" in student_validation.lower():
            return f"Student journal has errors:\n{student_validation}\n\nMark: 0/100"
        
        # Compare key totals
        student_totals = extract_totals_from_validation(student_validation)
        expected_totals = extract_totals_from_validation(expected_validation)
        
        if not student_totals or not expected_totals:
            return "Error: Could not extract totals for comparison."
        
        # Calculate marks based on accuracy
        marks = calculate_journal_marks(student_totals, expected_totals, journal_type)
        
        feedback = generate_journal_feedback(student_totals, expected_totals, journal_type)
        
        return f"Journal Marking Results:\n\n{feedback}\n\nFinal Mark: {marks}/100"
        
    except Exception as e:
        return f"Error marking journal: {str(e)}"

def extract_totals_from_validation(validation_text: str) -> dict:
    """Extracts totals from validation text."""
    totals = {}
    lines = validation_text.split('\n')
    for line in lines:
        if '=' in line and ':' in line:
            try:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace(' ', '_')
                value = float(value.strip().split('=')[1].strip())
                totals[key] = value
            except:
                continue
    return totals

def calculate_journal_marks(student_totals: dict, expected_totals: dict, journal_type: str) -> int:
    """Calculates marks for journal submission."""
    if journal_type.lower() == 'crj':
        key_fields = ['bank', 'income', 'sundry']
    else:  # CPJ
        key_fields = ['bank', 'consumables', 'wages', 'sundry']
    
    total_marks = 0
    max_marks = 100
    
    for field in key_fields:
        if field in student_totals and field in expected_totals:
            student_val = student_totals[field]
            expected_val = expected_totals[field]
            
            if abs(student_val - expected_val) < 0.01:
                total_marks += max_marks // len(key_fields)
            elif abs(student_val - expected_val) < expected_val * 0.1:  # Within 10%
                total_marks += (max_marks // len(key_fields)) // 2
    
    return min(total_marks, max_marks)

def generate_journal_feedback(student_totals: dict, expected_totals: dict, journal_type: str) -> str:
    """Generates detailed feedback for journal submission."""
    feedback = []
    
    if journal_type.lower() == 'crj':
        fields = [('bank', 'Bank'), ('income', 'Current Income'), ('sundry', 'Sundry Accounts')]
    else:  # CPJ
        fields = [('bank', 'Bank'), ('consumables', 'Consumables'), ('wages', 'Wages'), ('sundry', 'Sundry Accounts')]
    
    for field_key, field_name in fields:
        if field_key in student_totals and field_key in expected_totals:
            student_val = student_totals[field_key]
            expected_val = expected_totals[field_key]
            
            if abs(student_val - expected_val) < 0.01:
                feedback.append(f"✓ {field_name}: Correct (R{student_val:.2f})")
            elif abs(student_val - expected_val) < expected_val * 0.1:
                feedback.append(f"⚠ {field_name}: Close but incorrect (R{student_val:.2f} vs R{expected_val:.2f})")
            else:
                feedback.append(f"✗ {field_name}: Incorrect (R{student_val:.2f} vs R{expected_val:.2f})")
    
    return "\n".join(feedback)

# --- Journal Repository Functions ---

def get_available_journals() -> dict:
    """Returns available journal templates."""
    return {
        "CRJ": {
            "name": "Cash Receipts Journal",
            "description": "Record all cash received by the business",
            "columns": ["Doc. no.", "Day", "Details", "Fol.", "Analysis of receipts", "Bank", "Current income", "Sundry accounts"],
            "template": {
                "companyName": "",
                "month": "",
                "journalNumber": "",
                "rows": [{"doc": "", "day": "", "details": "", "fol": "", "analysis": {"main": "", "cents": ""}, "bank": {"main": "", "cents": ""}, "income": {"main": "", "cents": ""}, "sundry_amount": {"main": "", "cents": ""}, "sundry_fol": "", "sundry_details": ""}]
            }
        },
        "CPJ": {
            "name": "Cash Payments Journal", 
            "description": "Record all cash payments made by the business",
            "columns": ["Doc. no.", "Day", "Name of payee", "Fol.", "Bank", "Consumables", "Wages", "Sundry accounts"],
            "template": {
                "companyName": "",
                "month": "",
                "journalNumber": "",
                "rows": [{"doc": "", "day": "", "payee": "", "fol": "", "bank": {"main": "", "cents": ""}, "consumables": {"main": "", "cents": ""}, "wages": {"main": "", "cents": ""}, "sundry_amount": {"main": "", "cents": ""}, "sundry_fol": "", "sundry_details": ""}]
            }
        }
    }

# --- RAG and Agent Setup ---
agent_executors = {}
vectorstore = None

# --- Persona-Based System Prompts ---
STUDENT_PROMPT = (
    "You are CAPS AI, a friendly and expert personal tutor for a South African student. Your specialty is Mathematics."
    "Always address the student directly in an encouraging, supportive, and clear manner. Never talk about the student in the third person (e.g., do not say 'the student should...')."
    "Your primary goal is to help the user, who is a student, to understand concepts and solve problems."
    "When the user asks for help, first decide if a specialized tool is needed. For any final mathematical expression you output, you MUST use the 'format_expression_tool'."
    "When the user submits an answer for feedback, analyze their work carefully and provide helpful, step-by-step guidance."
)

TEACHER_PROMPT = (
    "You are CAPS AI, an expert assistant for a South African teacher. Your specialty is Mathematics."
    "Address the user as a professional colleague. Your goal is to help them create teaching materials, get curriculum information, and generate assessments."
    "Provide concise, accurate information. You can generate lesson plans, summaries, and varied question types (e.g., multiple choice, long-form)."
    "When asked to generate content, always refer to the provided curriculum documents using your tools."
)

ADMIN_PROMPT = (
    "You are CAPS AI, a high-level administrative assistant. Your purpose is to provide data-driven insights and summaries about the curriculum."
    "Address the user formally and professionally. Your responses should be factual, data-oriented, and based on the documents provided."
    "Do not provide teaching advice or student-facing content unless explicitly asked to generate an example."
)

def initialize_agent():
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
        """Searches the CAPS curriculum documents for relevant information."""
        if not vectorstore:
            return "Curriculum database is not available."
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
        docs = retriever.invoke(query)
        return "\n\n".join([f"Source: {doc.metadata.get('source_filename', 'N/A')}, Page: {doc.metadata.get('page_number', 'N/A')}\n\n{doc.page_content}" for doc in docs])

    tools = [
        solve_equation_tool, evaluate_expression_tool, curriculum_search_tool,
        geometry_calculator_tool, calculus_tool, format_expression_tool,
        validate_cash_receipts_journal, validate_cash_payments_journal, mark_journal_submission
    ]
    
    prompts = {
        "Student": STUDENT_PROMPT,
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

# --- Helper function to format structured answers ---
def format_structured_answer(answer_data: Dict[str, Any]) -> str:
    """Formats a structured answer object into a string for the AI agent."""
    # This function is unchanged and remains a placeholder for future implementation.
    return f"Student's Submission (Structured Data): {str(answer_data)}"

# --- Flask API Endpoints ---

@app.route('/api/agent', methods=['POST'])
def handle_agent_query():
    if not agent_executors:
        return jsonify({"error": "Agents not initialized"}), 500
    
    data = request.get_json()
    user_input = data.get("input")
    chat_history_json = data.get("chat_history", [])
    user_role = data.get("user_role", "Student") # Default to Student if no role is provided

    # Capitalize the user role to match the agent_executors dictionary keys
    capitalized_role = user_role.capitalize()
    agent_executor = agent_executors.get(capitalized_role)
    
    if not agent_executor:
        return jsonify({"error": f"Invalid user role: {user_role}"}), 400

    final_input_for_agent = user_input

    if isinstance(user_input, dict):
        question_text = user_input.get("question", "A student submitted the following answer to a previous question:")
        answer_data = user_input.get("answer", {})
        formatted_answer_str = format_structured_answer(answer_data)
        final_input_for_agent = f'Question: "{question_text}"\n\n{formatted_answer_str}'

    # FIX: Add error handling for KeyError on 'role' and 'content'
    chat_history = []
    for msg in chat_history_json:
        try:
            role = msg['role']
            content = msg['content']
            if role == 'human':
                chat_history.append(HumanMessage(content=content))
            else:
                chat_history.append(AIMessage(content=content))
        except KeyError as e:
            # Log the error for debugging
            print(f"KeyError: Missing key {e} in chat history message: {msg}")
            # Skip this message and continue, or handle it as an error
            # For now, we will simply skip the malformed message
            continue

    try:
        response = agent_executor.invoke({"input": final_input_for_agent, "chat_history": chat_history})
        return jsonify({"output": response.get('output')})
    except Exception as e:
        # Catch and handle general exceptions from the agent
        print(f"Error during agent invocation: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/journals/available', methods=['GET'])
def get_journals():
    """Get available journal templates."""
    try:
        journals = get_available_journals()
        return jsonify({"journals": journals})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/journals/validate', methods=['POST'])
def validate_journal():
    """Validate a journal submission."""
    try:
        data = request.get_json()
        journal_data = data.get("journal_data")
        journal_type = data.get("journal_type", "CRJ")
        
        if journal_type.upper() == "CRJ":
            result = validate_cash_receipts_journal(journal_data)
        elif journal_type.upper() == "CPJ":
            result = validate_cash_payments_journal(journal_data)
        else:
            return jsonify({"error": f"Unknown journal type: {journal_type}"}), 400
        
        return jsonify({"validation_result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/journals/mark', methods=['POST'])
def mark_journal():
    """Mark a journal submission against expected answer."""
    try:
        data = request.get_json()
        question_text = data.get("question_text", "")
        student_journal = data.get("student_journal")
        expected_journal = data.get("expected_journal")
        journal_type = data.get("journal_type", "CRJ")
        
        if not student_journal or not expected_journal:
            return jsonify({"error": "Missing journal data"}), 400
        
        result = mark_journal_submission(question_text, student_journal, expected_journal, journal_type)
        return jsonify({"marking_result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# -------------------------------------------------------------------
# --- ENDPOINT FOR EVALUATING TYPED (FREE-TEXT) ANSWERS ---
# -------------------------------------------------------------------

@app.route('/api/evaluate-typed', methods=['POST'])
def evaluate_typed_answer():
    """
    Evaluate a student's free-text answer against a sample answer using Gemini.
    Only used for 'typed' question types where deterministic marking is not possible.
    """
    try:
        data = request.get_json()
        question_prompt = data.get("question_prompt", "")
        sample_answer = data.get("sample_answer", "")
        student_answer = data.get("student_answer", "")
        subject = data.get("subject", "")
        grade = data.get("grade", "")

        if not question_prompt or not student_answer:
            return jsonify({"error": "Missing question_prompt or student_answer"}), 400

        if not GOOGLE_API_KEY:
            return jsonify({"error": "AI service not configured"}), 500

        llm = ChatGoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            temperature=0.1,
            google_api_key=GOOGLE_API_KEY,
        )

        evaluation_prompt = f"""You are a {subject} Grade {grade} teacher marking a student's answer.

QUESTION: {question_prompt}

SAMPLE ANSWER (marking guide): {sample_answer}

STUDENT'S ANSWER: {student_answer}

Evaluate the student's answer against the sample answer. Respond in this exact JSON format:
{{
  "is_correct": true/false,
  "score": <number 0-100>,
  "feedback": "<brief, encouraging feedback explaining what was correct and what was missing or wrong. Max 3 sentences.>",
  "key_points_hit": ["<point 1>", "<point 2>"],
  "key_points_missed": ["<missed point 1>"]
}}

Rules:
- Award partial credit for partially correct answers.
- The student does not need to match the sample answer word-for-word; accept equivalent meanings.
- is_correct = true if score >= 50.
- Be encouraging but honest.
- Return ONLY valid JSON, no markdown fences."""

        response = llm.invoke(evaluation_prompt)
        raw_output = response.content.strip()

        # Try to parse as JSON; if it fails, return raw text as feedback
        try:
            parsed = json.loads(raw_output)
            return jsonify({"evaluation": parsed})
        except json.JSONDecodeError:
            return jsonify({
                "evaluation": {
                    "is_correct": False,
                    "score": 0,
                    "feedback": raw_output,
                    "key_points_hit": [],
                    "key_points_missed": [],
                }
            })

    except Exception as e:
        print(f"Error in evaluate-typed: {e}")
        return jsonify({"error": str(e)}), 500

# -------------------------------------------------------------------
# --- ENDPOINT FOR ASSESSMENT GENERATION ---
# -------------------------------------------------------------------

@app.route('/api/teacher/create-assessment', methods=['POST'])
def create_assessment():
    """
    Generates a new assessment with questions, a detailed marking scheme/rubric, and a worked solution.
    """
    if not agent_executors:
        return jsonify({"error": "Agents not initialized"}), 500

    data = request.get_json()
    topic = data.get("topic")
    grade = data.get("grade")
    num_questions = data.get("num_questions", 3)

    if not all([topic, grade]):
        return jsonify({"error": "Missing required parameters: topic and grade"}), 400

    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash", temperature=0.3, convert_system_message_to_human=True, google_api_key=GOOGLE_API_KEY)
    
    prompt_template = f"""
    You are an expert in creating educational materials for the South African CAPS curriculum.
    Your task is to generate an assessment for a Grade {grade} student on the topic of "{topic}".
    The assessment should contain exactly {num_questions} questions.

    For each question, you must provide:
    1. The question text.
    2. The question type (e.g., "short_answer_with_steps", "long_answer").
    3. A detailed marking scheme.
    4. A complete, step-by-step worked solution. The steps in the solution MUST be separated by a comma and a space.

    You MUST respond with ONLY a valid JSON object. Do not include any other text, explanations, or markdown formatting like ```json.
    The JSON object must have a single key "assessment" which is an array of question objects.
    Each question object must have the following keys: "question_text", "question_type", "marking_scheme", and "solution".
    The "marking_scheme" must be an array of objects, each with a "point" (the step or keyword) and "marks" (the value for that point).
    The "solution" must be a string containing the full worked-out answer, with each logical step separated by a comma and a space.

    Example of the required JSON structure:
    {{
      "assessment": [
        {{
          "question_text": "Solve for x: 2x + 5 = 15",
          "question_type": "short_answer_with_steps",
          "marking_scheme": [
            {{ "point": "Subtracts 5 from both sides (2x = 10)", "marks": 1 }},
            {{ "point": "Divides both sides by 2 (x = 5)", "marks": 1 }}
          ],
          "solution": "2x + 5 = 15, 2x = 15 - 5, 2x = 10, x = 10 / 2, x = 5"
        }},
        {{
          "question_text": "Define 'photosynthesis'.",
          "question_type": "long_answer",
          "marking_scheme": [
            {{ "point": "Mentions 'light energy' or 'sunlight'", "marks": 1 }},
            {{ "point": "Mentions 'carbon dioxide' and 'water'", "marks": 1 }},
            {{ "point": "Mentions 'glucose' or 'sugar' as a product", "marks": 1 }}
          ],
          "solution": "Photosynthesis is the process used by plants, algae, and some bacteria to convert light energy into chemical energy, through a process that converts carbon dioxide and water into glucose (sugar) and oxygen."
        }}
      ]
    }}
    """

    try:
        response = llm.invoke(prompt_template)
        ai_response_str = response.content
        
        # --- NEW: Robust JSON Extraction Logic ---
        # Find the start and end of the JSON block
        json_match = re.search(r'\{.*\}', ai_response_str, re.DOTALL)
        
        if not json_match:
            # If no JSON block is found at all, raise the error
            raise json.JSONDecodeError("No valid JSON object found in the AI's response.", ai_response_str, 0)
            
        json_str = json_match.group(0)
        assessment_data = json.loads(json_str)
        
        return jsonify(assessment_data)

    except json.JSONDecodeError:
        # This error is now more specific to a truly malformed JSON response
        return jsonify({"error": "Failed to decode the AI's JSON response. The response may be malformed."}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# --- NEW: Endpoint for Deleting Expired Solved Problems ---
@app.route('/api/admin/delete-expired-solved-problems', methods=['POST'])
def delete_expired_solved_problems():
    """
    Deletes solved_freeform_problems documents where retentionDate has passed.
    This endpoint is intended to be called by a scheduled job, not directly by the frontend.
    """
    print("Starting deletion of expired solved problems...")
    
    # Get the current timestamp in UTC
    now = datetime.datetime.now(datetime.timezone.utc)
    
    # Assuming __app_id is passed or configured. For a backend, you'd likely have this
    # as an environment variable or a configuration.
    app_id = os.getenv("FIREBASE_APP_ID", "default-app-id") 

    deleted_count = 0
    batch_size = 500 # Firestore limit for batch writes

    try:
        # Iterate through all users to find their solved problems
        # This approach iterates through all users, which can be inefficient for very large user bases.
        # For a more scalable solution, consider alternative strategies like
        # storing expired problem IDs in a queue or using Firestore collection group queries
        # if your security rules allow it and you have appropriate indexes.
        users_ref = firestore_db.collection('users')
        users_docs = users_ref.stream()

        for user_doc in users_docs:
            user_id = user_doc.id
            print(f"Processing user: {user_id}")
            
            problems_ref = firestore_db.collection('artifacts').document(app_id).collection('users').document(user_id).collection('solved_freeform_problems')
            
            # Query for documents where retentionDate is less than or equal to now (ISO format string)
            # Firestore queries on string dates require consistent formatting.
            query_ref = problems_ref.where('retentionDate', '<=', now.isoformat()) 

            while True:
                docs_to_delete = query_ref.limit(batch_size).stream()
                batch = firestore_db.batch()
                
                doc_count_in_batch = 0
                for doc_snapshot in docs_to_delete:
                    batch.delete(doc_snapshot.reference)
                    doc_count_in_batch += 1
                
                if doc_count_in_batch == 0:
                    break # No more documents to delete for this user in this batch

                batch.commit()
                deleted_count += doc_count_in_batch
                print(f"  Deleted {doc_count_in_batch} problems for user {user_id}. Total deleted: {deleted_count}")

                # If we processed a full batch, there might be more documents matching the query.
                # The .stream() method from firebase-admin SDK handles pagination automatically
                # when you continue to iterate, so explicit start_after is not strictly needed here
                # for simple iteration, but it's good practice for more complex scenarios or
                # when constructing new queries.
                if doc_count_in_batch < batch_size:
                    break # Less than a full batch means we're done for this user

        print(f"Finished deleting expired solved problems. Total deleted: {deleted_count}")
        return jsonify({"message": f"Successfully deleted {deleted_count} expired solved problems."}), 200

    except Exception as e:
        print(f"Error during deletion of expired solved problems: {e}")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500





# --- Main Execution ---
if __name__ == '__main__':
    initialize_agent()
    app.run(debug=True, port=5001)
