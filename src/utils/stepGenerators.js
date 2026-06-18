/**
 * Step Generation Utilities
 * 
 * This module contains functions for generating step-by-step procedural guidance
 * for various mathematical operations and problem-solving techniques.
 */

/**
 * Enhanced Step-by-Step Procedural Guidance
 * Routes to appropriate step generator based on operation type
 * @param {string} operation - The mathematical operation to perform
 * @param {string} expression - The input expression
 * @param {string} result - The result of the operation
 * @returns {Array} - Array of step objects
 */
export const generateComprehensiveSteps = (operation, expression, result) => {
    const steps = [];
    
    try {
        switch (operation) {
            case 'simplify':
                steps.push(...generateSimplifySteps(expression, result));
                break;
            case 'factor':
                steps.push(...generateFactorSteps(expression, result));
                break;
            case 'expand':
                steps.push(...generateExpandSteps(expression, result));
                break;
            case 'solve':
                steps.push(...generateSolveSteps(expression, result));
                break;
            case 'complete_square':
                steps.push(...generateCompleteSquareSteps(expression, result));
                break;
            case 'long_division':
                steps.push(...generateLongDivisionSteps(expression, result));
                break;
            case 'cubic_solve':
                steps.push(...generateCubicSolveSteps(expression, result));
                break;
            case 'simultaneous':
                steps.push(...generateSimultaneousSteps(expression, result));
                break;
            case 'inequalities':
                steps.push(...generateInequalitySteps(expression, result));
                break;
            case 'quadratic_analysis':
                steps.push(...generateQuadraticAnalysisSteps(expression, result));
                break;
            case 'logarithmic_solve':
                steps.push(...generateLogarithmicSteps(expression, result));
                break;
            default:
                steps.push({
                    step: 1,
                    description: "Operation completed",
                    expression: result,
                    explanation: "The operation has been completed successfully."
                });
        }
    } catch (error) {
        console.error('Error generating steps:', error);
        steps.push({
            step: 1,
            description: "Error occurred during step generation",
            expression: "Error",
            explanation: "An error occurred while generating the step-by-step solution."
        });
    }
    
    return steps;
};

/**
 * Generates step-by-step instructions for simplifying expressions
 * @param {string} expression - The expression to simplify
 * @param {string} result - The simplified result
 * @returns {Array} - Array of step objects
 */
export const generateSimplifySteps = (expression, result) => {
    const steps = [];
    let currentExpr = expression;
    
    // Step 1: Identify the expression
    steps.push({
        step: 1,
        description: "Identify the expression to simplify",
        expression: currentExpr,
        explanation: "We start with the given expression that needs to be simplified."
    });
    
    // Step 2: Check for like terms
    if (currentExpr.includes('+') || currentExpr.includes('-')) {
        steps.push({
            step: 2,
            description: "Identify and combine like terms",
            expression: currentExpr,
            explanation: "Look for terms with the same variable and exponent, then combine their coefficients."
        });
    }
    
    // Step 3: Apply distributive property if needed
    if (currentExpr.includes('(') && currentExpr.includes(')')) {
        steps.push({
            step: 3,
            description: "Apply distributive property",
            expression: currentExpr,
            explanation: "Multiply each term inside the parentheses by the factor outside."
        });
    }
    
    // Step 4: Final simplified form
    steps.push({
        step: steps.length + 1,
        description: "Final simplified expression",
        expression: result,
        explanation: "The expression has been simplified to its most basic form."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for factoring expressions
 * @param {string} expression - The expression to factor
 * @param {string} result - The factored result
 * @returns {Array} - Array of step objects
 */
export const generateFactorSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the expression to factor",
        expression: expression,
        explanation: "We start with the given expression that needs to be factored."
    });
    
    steps.push({
        step: 2,
        description: "Look for common factors",
        expression: expression,
        explanation: "Check if all terms have a common factor that can be extracted."
    });
    
    if (expression.includes('x²') || expression.includes('x^2')) {
        steps.push({
            step: 3,
            description: "Identify as quadratic expression",
            expression: expression,
            explanation: "This is a quadratic expression in the form ax² + bx + c."
        });
        
        steps.push({
            step: 4,
            description: "Apply quadratic factoring techniques",
            expression: expression,
            explanation: "Use methods like factoring by grouping, difference of squares, or perfect square trinomials."
        });
    }
    
    steps.push({
        step: steps.length + 1,
        description: "Final factored form",
        expression: result,
        explanation: "The expression has been factored into its component parts."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for expanding expressions
 * @param {string} expression - The expression to expand
 * @param {string} result - The expanded result
 * @returns {Array} - Array of step objects
 */
export const generateExpandSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the expression to expand",
        expression: expression,
        explanation: "We start with the given expression that needs to be expanded."
    });
    
    if (expression.includes('(') && expression.includes(')')) {
        steps.push({
            step: 2,
            description: "Apply distributive property",
            expression: expression,
            explanation: "Multiply each term inside the parentheses by the factor outside."
        });
    }
    
    if (expression.includes('²') || expression.includes('^2')) {
        steps.push({
            step: 3,
            description: "Expand squared terms",
            expression: expression,
            explanation: "Use the formula (a + b)² = a² + 2ab + b² for perfect squares."
        });
    }
    
    steps.push({
        step: steps.length + 1,
        description: "Combine like terms",
        expression: result,
        explanation: "Group and combine terms with the same variables and exponents."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for solving equations
 * @param {string} expression - The equation to solve
 * @param {string} result - The solution
 * @returns {Array} - Array of step objects
 */
export const generateSolveSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the equation to solve",
        expression: expression,
        explanation: "We start with the given equation that needs to be solved."
    });
    
    steps.push({
        step: 2,
        description: "Isolate the variable",
        expression: expression,
        explanation: "Move all terms containing the variable to one side and constants to the other."
    });
    
    steps.push({
        step: 3,
        description: "Combine like terms",
        expression: expression,
        explanation: "Simplify both sides of the equation by combining similar terms."
    });
    
    steps.push({
        step: 4,
        description: "Solve for the variable",
        expression: result,
        explanation: "Divide both sides by the coefficient of the variable to find the solution."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for completing the square
 * @param {string} expression - The quadratic expression
 * @param {string} result - The completed square form
 * @returns {Array} - Array of step objects
 */
export const generateCompleteSquareSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the quadratic expression",
        expression: expression,
        explanation: "We start with a quadratic expression in the form ax² + bx + c."
    });
    
    steps.push({
        step: 2,
        description: "Factor out the coefficient of x²",
        expression: expression,
        explanation: "If a ≠ 1, factor out the coefficient a from the x² and x terms."
    });
    
    steps.push({
        step: 3,
        description: "Add and subtract (b/2a)²",
        expression: expression,
        explanation: "Add (b/2a)² inside the parentheses and subtract a(b/2a)² to maintain equality."
    });
    
    steps.push({
        step: 4,
        description: "Write as perfect square plus constant",
        expression: result,
        explanation: "The expression is now in the form a(x + b/2a)² + k, where k is the constant term."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for polynomial long division
 * @param {string} expression - The division expression
 * @param {string} result - The division result
 * @returns {Array} - Array of step objects
 */
export const generateLongDivisionSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Set up the long division",
        expression: expression,
        explanation: "Arrange the dividend and divisor for polynomial long division."
    });
    
    steps.push({
        step: 2,
        description: "Divide the leading terms",
        expression: expression,
        explanation: "Divide the leading term of the dividend by the leading term of the divisor."
    });
    
    steps.push({
        step: 3,
        description: "Multiply and subtract",
        expression: expression,
        explanation: "Multiply the divisor by the quotient term and subtract from the dividend."
    });
    
    steps.push({
        step: 4,
        description: "Bring down the next term",
        expression: expression,
        explanation: "Bring down the next term and repeat the process until all terms are processed."
    });
    
    steps.push({
        step: 5,
        description: "Final result",
        expression: result,
        explanation: "The quotient and remainder from the polynomial long division."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for solving cubic equations
 * @param {string} expression - The cubic equation
 * @param {string} result - The solution
 * @returns {Array} - Array of step objects
 */
export const generateCubicSolveSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the cubic equation",
        expression: expression,
        explanation: "We start with a cubic equation in the form ax³ + bx² + cx + d = 0."
    });
    
    steps.push({
        step: 2,
        description: "Check for rational roots",
        expression: expression,
        explanation: "Use the Rational Root Theorem to find possible rational solutions."
    });
    
    steps.push({
        step: 3,
        description: "Apply synthetic division",
        expression: expression,
        explanation: "Use synthetic division to test potential roots and factor the polynomial."
    });
    
    steps.push({
        step: 4,
        description: "Factor the remaining quadratic",
        expression: expression,
        explanation: "If a root is found, factor out (x - root) and solve the remaining quadratic equation."
    });
    
    steps.push({
        step: 5,
        description: "Find all solutions",
        expression: result,
        explanation: "Combine the rational root with the solutions from the quadratic factor."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for solving simultaneous equations
 * @param {string} expression - The system of equations
 * @param {string} result - The solution
 * @returns {Array} - Array of step objects
 */
export const generateSimultaneousSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the system of equations",
        expression: expression,
        explanation: "We start with a system of linear equations that need to be solved simultaneously."
    });
    
    steps.push({
        step: 2,
        description: "Choose a solution method",
        expression: expression,
        explanation: "Decide whether to use substitution, elimination, or matrix methods."
    });
    
    steps.push({
        step: 3,
        description: "Solve for one variable",
        expression: expression,
        explanation: "Express one variable in terms of the other from one equation."
    });
    
    steps.push({
        step: 4,
        description: "Substitute and solve",
        expression: expression,
        explanation: "Substitute the expression into the other equation and solve for the remaining variable."
    });
    
    steps.push({
        step: 5,
        description: "Find the other variable",
        expression: result,
        explanation: "Use the found value to determine the other variable from the first equation."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for solving inequalities
 * @param {string} expression - The inequality
 * @param {string} result - The solution
 * @returns {Array} - Array of step objects
 */
export const generateInequalitySteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the inequality",
        expression: expression,
        explanation: "We start with an inequality that needs to be solved."
    });
    
    steps.push({
        step: 2,
        description: "Solve as an equation",
        expression: expression,
        explanation: "First, solve the inequality as if it were an equation to find critical points."
    });
    
    steps.push({
        step: 3,
        description: "Determine test intervals",
        expression: expression,
        explanation: "Use the critical points to divide the number line into test intervals."
    });
    
    steps.push({
        step: 4,
        description: "Test each interval",
        expression: expression,
        explanation: "Choose a test value from each interval to determine where the inequality holds."
    });
    
    steps.push({
        step: 5,
        description: "Write the solution",
        expression: result,
        explanation: "Express the solution in interval notation or as a compound inequality."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for quadratic analysis
 * @param {string} expression - The quadratic expression
 * @param {string} result - The analysis result
 * @returns {Array} - Array of step objects
 */
export const generateQuadraticAnalysisSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the quadratic expression",
        expression: expression,
        explanation: "We start with a quadratic expression in the form ax² + bx + c."
    });
    
    steps.push({
        step: 2,
        description: "Calculate the discriminant",
        expression: "Δ = b² - 4ac",
        explanation: "The discriminant determines the nature of the roots of the quadratic equation."
    });
    
    steps.push({
        step: 3,
        description: "Analyze the roots",
        expression: expression,
        explanation: "If Δ > 0: two distinct real roots; if Δ = 0: one repeated root; if Δ < 0: complex roots."
    });
    
    steps.push({
        step: 4,
        description: "Find the vertex",
        expression: "x = -b/(2a), y = f(-b/(2a))",
        explanation: "The vertex represents the maximum or minimum point of the parabola."
    });
    
    steps.push({
        step: 5,
        description: "Determine direction",
        expression: result,
        explanation: "If a > 0, the parabola opens upward; if a < 0, it opens downward."
    });
    
    return steps;
};

/**
 * Generates step-by-step instructions for solving logarithmic equations
 * @param {string} expression - The logarithmic equation
 * @param {string} result - The solution
 * @returns {Array} - Array of step objects
 */
export const generateLogarithmicSteps = (expression, result) => {
    const steps = [];
    
    steps.push({
        step: 1,
        description: "Identify the logarithmic equation",
        expression: expression,
        explanation: "We start with a logarithmic equation that needs to be solved."
    });
    
    steps.push({
        step: 2,
        description: "Use logarithmic properties",
        expression: "Apply properties like log(a) + log(b) = log(ab)",
        explanation: "Use logarithmic properties to simplify the equation."
    });
    
    steps.push({
        step: 3,
        description: "Convert to exponential form",
        expression: "If log_b(x) = y, then b^y = x",
        explanation: "Convert the logarithmic equation to exponential form to solve for the variable."
    });
    
    steps.push({
        step: 4,
        description: "Solve the exponential equation",
        expression: "Use appropriate methods to solve the resulting exponential equation",
        explanation: "Apply techniques for solving exponential equations."
    });
    
    steps.push({
        step: 5,
        description: "Check for extraneous solutions",
        expression: "Verify that solutions are valid",
        explanation: "Logarithmic functions have domain restrictions, so check that solutions are valid."
    });
    
    steps.push({
        step: 6,
        description: "Solution",
        expression: result,
        explanation: "The valid solution(s) to the logarithmic equation."
    });
    
    return steps;
};
