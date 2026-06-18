from sympy import sympify, solve, Eq, S
from sympy.abc import symbols
from langchain_core.tools import tool
import re # Added for potential regex use, though not strictly used in current sympify

@tool
def solve_equation_tool(equation: str) -> str:
    """
    Solves a single algebraic equation for a variable.
    Assumes the equation is in the format 'expression1 = expression2'.
    Returns the solution as a string, or an error message if it cannot solve.
    Example: solve_equation_tool("2*x + 5 = 15")
    """
    try:
        # Split the equation at '='
        if '=' not in equation:
            return "Error: Equation must contain an '=' sign."
        
        lhs_str, rhs_str = equation.split('=', 1)
        lhs = sympify(lhs_str.strip())
        rhs = sympify(rhs_str.strip())
        
        # Define common symbolic variables for robust parsing
        x, y, z, a, b, c = symbols('x y z a b c') 

        # Identify variables present in the equation
        variables = lhs.free_symbols.union(rhs.free_symbols)

        if len(variables) == 1:
            variable = list(variables)[0]
            solution = solve(Eq(lhs, rhs), variable)
            if solution:
                # Handle multiple solutions (e.g., x**2 = 9 gives [3, -3])
                if len(solution) == 1:
                    return f"Solution: {variable} = {solution[0]}"
                else:
                    return f"Solutions for {variable}: {', '.join(map(str, solution))}"
            else:
                return "Could not find a unique solution for the equation, or no solution exists."
        elif len(variables) > 1:
            return "Equation contains multiple variables. This tool can only solve for a single variable."
        else:
            # No variables found, check if it's a contradiction or identity
            if lhs == rhs:
                return "The equation is an identity (always true for any variable values)."
            else:
                return "The equation is a contradiction (no variables, and is false, e.g., '5 = 6')."

    except Exception as e:
        return f"Error solving equation: {e}. Please ensure it's a valid algebraic equation."

@tool
def evaluate_expression_tool(expression: str, substitutions: dict = None) -> str:
    """
    Evaluates a mathematical expression.
    Optionally accepts a dictionary of variable substitutions.
    Example: evaluate_expression_tool(expression="2*x + 3", substitutions={"x": 5})
    Example: evaluate_expression_tool(expression="sin(pi/2)")
    """
    try:
        expr = sympify(expression.strip())
        
        if substitutions:
            # Convert string keys to sympy symbols for substitution
            sym_subs = {symbols(k): v for k, v in substitutions.items()}
            result = expr.subs(sym_subs)
        else:
            # If no substitutions, try to evaluate to a numerical result
            # Only call evalf() if there are no free symbols after optional substitution
            if not expr.free_symbols:
                result = expr.evalf()
            else:
                return f"Expression '{expression}' contains variables ({', '.join(map(str, expr.free_symbols))}) but no substitutions were provided for all of them. Cannot evaluate to a numerical result."
        
        return f"Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {e}. Please ensure it's a valid mathematical expression."

@tool
def calculate_area_of_rectangle(length: float, width: float) -> str:
    """
    Calculates the area of a rectangle given its length and width.
    Both length and width must be positive numbers.
    Example: calculate_area_of_rectangle(length=10.0, width=5.0)
    """
    if length <= 0 or width <= 0:
        return "Length and width must be positive numbers."
    
    try:
        area = length * width
        return f"The area of the rectangle is: {area}"
    except Exception as e:
        return f"Error calculating area: {e}. Please provide valid numerical inputs."

if __name__ == "__main__":
    print("Testing math tools:")
    print(solve_equation_tool("2*x + 5 = 15")) # Expected: Solution: x = 5
    print(solve_equation_tool("y - 7 = 3*y")) # Expected: Solution: y = -7/2
    print(solve_equation_tool("x**2 = 9"))    # Expected: Solutions for x: -3, 3
    print(solve_equation_tool("x + y = 5")) # Expected: Equation contains multiple variables...
    print(solve_equation_tool("5 = 5")) # Expected: The equation is an identity...
    print(solve_equation_tool("5 = 6")) # Expected: The equation is a contradiction...
    print(evaluate_expression_tool("5 + 3 * 2")) # Expected: Result: 11
    print(evaluate_expression_tool("x**2 + 2*y", {"x": 3, "y": 4})) # Expected: Result: 17
    print(evaluate_expression_tool("sqrt(16) + 1")) # Expected: Result: 5.0
    print(calculate_area_of_rectangle(10, 5)) # Expected: The area of the rectangle is: 50
    print(calculate_area_of_rectangle(-2, 5)) # Expected: Length and width must be positive numbers.
