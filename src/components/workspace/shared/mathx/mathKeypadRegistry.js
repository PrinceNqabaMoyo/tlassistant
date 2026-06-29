/**
 * Registry-driven mathematics keypad.
 *
 * Each key has:
 *   label   LaTeX shown on the button (rendered with KaTeX)
 *   insert  plain text inserted into the input (SymPy-parseable: ``^`` powers,
 *           ``sqrt(`` surds, ``,`` decimals, ``*`` / ``/`` operators)
 *   offset  optional caret offset after insertion (e.g. -1 to sit inside "()")
 *
 * Keys are grouped so new topics declare which groups they need; the registry
 * grows per topic instead of one monolithic keypad.
 */
export const KEYPAD_GROUPS = {
    arithmetic: [
        { label: '+', insert: '+' },
        { label: '-', insert: '-' },
        { label: '\\times', insert: '*' },
        { label: '\\div', insert: '/' },
        { label: '=', insert: '=' },
        { label: ',', insert: ',' },
    ],
    algebra: [
        { label: 'x', insert: 'x' },
        { label: 'x^2', insert: '^2' },
        { label: 'x^{n}', insert: '^' },
        { label: '(\\;)', insert: '()', offset: -1 },
        { label: '\\sqrt{\\;}', insert: 'sqrt()', offset: -1 },
        { label: '\\dfrac{a}{b}', insert: '/' },
    ],
    exponents: [
        { label: 'x^2', insert: '^2' },
        { label: 'x^3', insert: '^3' },
        { label: 'x^{n}', insert: '^' },
        { label: 'x^{-1}', insert: '^(-1)' },
        { label: '\\sqrt{\\;}', insert: 'sqrt()', offset: -1 },
        { label: '\\sqrt[3]{\\;}', insert: '()', offset: -1 },
        { label: '\\dfrac{1}{x}', insert: '1/' },
    ],
    inequalities: [
        { label: '<', insert: '<' },
        { label: '>', insert: '>' },
        { label: '\\leq', insert: '<=' },
        { label: '\\geq', insert: '>=' },
        { label: '\\neq', insert: '!=' },
        { label: '\\infty', insert: 'oo' },
        { label: '(\\;)', insert: '()', offset: -1 },
        { label: '[\\;]', insert: '[]', offset: -1 },
    ],
    sequences: [
        { label: 'T_n', insert: 'T_n' },
        { label: 'T_{n-1}', insert: 'T_{n-1}' },
        { label: ';', insert: ';' },
        { label: '\\ldots', insert: 'ldots' },
        { label: 'n', insert: 'n' },
    ],
    trigonometry: [
        { label: '\\sin', insert: 'sin()', offset: -1 },
        { label: '\\cos', insert: 'cos()', offset: -1 },
        { label: '\\tan', insert: 'tan()', offset: -1 },
        { label: '\\theta', insert: 'theta' },
        { label: '^{\\circ}', insert: 'deg' },
        { label: '\\pi', insert: 'pi' },
    ],
    functions: [
        { label: 'f(x)', insert: 'f(x)' },
        { label: '(\\;;\\;)', insert: '(;)', offset: -2 },
        { label: 'y =', insert: 'y=' },
        { label: '\\in', insert: ' in ' },
        { label: '\\mathbb{R}', insert: 'R' },
        { label: '\\neq', insert: '!=' },
    ],
};

export const TOPIC_KEYPADS = {
    grade10_math_algebraic_expressions: ['algebra', 'arithmetic'],
    grade10_math_exponents: ['exponents', 'algebra', 'arithmetic'],
    grade10_math_trigonometry: ['trigonometry', 'algebra', 'arithmetic'],
    grade10_math_equations_inequalities: ['inequalities', 'algebra', 'arithmetic'],
    grade10_math_patterns_sequences: ['sequences', 'algebra', 'arithmetic'],
    grade10_math_functions: ['functions', 'trigonometry', 'algebra', 'arithmetic'],
};

/** Resolve the flat key list for a topic (deduped, group order preserved). */
export const getKeypadForTopic = (topic) => {
    const groups = TOPIC_KEYPADS[topic] || ['algebra', 'arithmetic'];
    const keys = [];
    const seen = new Set();
    for (const g of groups) {
        for (const key of KEYPAD_GROUPS[g] || []) {
            if (!seen.has(key.insert + key.label)) {
                seen.add(key.insert + key.label);
                keys.push(key);
            }
        }
    }
    return keys;
};
