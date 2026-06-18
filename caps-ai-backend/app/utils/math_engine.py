import sympy
from sympy import sympify, solve, Eq, diff, integrate, symbols, simplify, expand, factor

import numpy as np
from typing import Dict, Any, Union, List

class MathEngine:
    def __init__(self):
        self.supported_operations = {
            'derivative': self._calculate_derivative,
            'integral': self._calculate_integral,
            'solve': self.solve_equation,
            'evaluate': self.evaluate_expression,
            'simplify': self._simplify_expression,
            'factor': self._factor_expression,
            'expand': self._expand_expression
        }
    
    def calculate(self, operation: str, expression: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Main calculation method"""
        if operation not in self.supported_operations:
            raise ValueError(f"Unsupported operation: {operation}")
        
        return self.supported_operations[operation](expression, params or {})
    
    def validate(self, expression: str) -> bool:
        """Validate mathematical expression"""
        if not SYMPY_AVAILABLE:
            return False
        try:
            sympify(expression)
            return True
        except:
            return False
    
    def solve_equation(self, equation: str) -> Dict[str, Any]:
        """Solve mathematical equation"""
        try:
            if '=' not in equation:
                raise ValueError("Equation must contain an '=' sign.")
            
            lhs_str, rhs_str = equation.split('=', 1)
            lhs = sympify(lhs_str.strip())
            rhs = sympify(rhs_str.strip())
            
            variables = lhs.free_symbols.union(rhs.free_symbols)
            if len(variables) == 1:
                variable = list(variables)[0]
                solution = solve(Eq(lhs, rhs), variable)
                return {
                    'result': str(solution[0]) if solution else "No unique solution found.",
                    'latex': sympy.latex(solution[0]) if solution else "No solution",
                    'variable': str(variable),
                    'steps': self._generate_solve_steps(equation, variable)
                }
            else:
                raise ValueError("This tool can only solve equations with a single variable.")
        except Exception as e:
            raise ValueError(f"Error solving equation: {e}")
    
    def evaluate_expression(self, expression: str, substitutions: Dict[str, Any] = None) -> Dict[str, Any]:
        """Evaluate mathematical expression with optional substitutions"""
        try:
            expr = sympify(expression.strip())
            if substitutions:
                sym_subs = {symbols(k): v for k, v in substitutions.items()}
                result = expr.subs(sym_subs)
            else:
                result = expr.evalf() if not expr.free_symbols else expr
            
            return {
                'result': str(result),
                'latex': sympy.latex(result),
                'expression': expression,
                'substitutions': substitutions or {}
            }
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")
    
    def _calculate_derivative(self, expression: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate derivative of expression"""
        variable = params.get('variable', 'x')
        x = symbols(variable)
        expr = sympify(expression)
        derivative = diff(expr, x)
        
        return {
            'result': str(derivative),
            'latex': sympy.latex(derivative),
            'steps': self._generate_derivative_steps(expression, variable)
        }
    
    def _calculate_integral(self, expression: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate integral of expression"""
        variable = params.get('variable', 'x')
        x = symbols(variable)
        expr = sympify(expression)
        integral = integrate(expr, x)
        
        return {
            'result': str(integral),
            'latex': sympy.latex(integral),
            'steps': self._generate_integral_steps(expression, variable)
        }
    
    def _simplify_expression(self, expression: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Simplify mathematical expression"""
        expr = sympify(expression)
        simplified = simplify(expr)
        
        return {
            'result': str(simplified),
            'latex': sympy.latex(simplified),
            'original': expression
        }
    
    def _factor_expression(self, expression: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Factor mathematical expression"""
        expr = sympify(expression)
        factored = factor(expr)
        
        return {
            'result': str(factored),
            'latex': sympy.latex(factored),
            'original': expression
        }
    
    def _expand_expression(self, expression: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Expand mathematical expression"""
        expr = sympify(expression)
        expanded = expand(expr)
        
        return {
            'result': str(expanded),
            'latex': sympy.latex(expanded),
            'original': expression
        }
    
    def _generate_derivative_steps(self, expression: str, variable: str) -> List[str]:
        """Generate step-by-step derivative solution"""
        return [
            f"Step 1: Identify the function f({variable}) = {expression}",
            f"Step 2: Apply derivative rules",
            f"Step 3: Result: d/d{variable}({expression})"
        ]
    
    def _generate_integral_steps(self, expression: str, variable: str) -> List[str]:
        """Generate step-by-step integral solution"""
        return [
            f"Step 1: Identify the function to integrate: {expression}",
            f"Step 2: Apply integration rules",
            f"Step 3: Result: ∫{expression} d{variable}"
        ]
    
    def _generate_solve_steps(self, equation: str, variable: str) -> List[str]:
        """Generate step-by-step equation solution"""
        return [
            f"Step 1: Original equation: {equation}",
            f"Step 2: Isolate {variable}",
            f"Step 3: Solve for {variable}"
        ]
