/**
 * Registry-driven mathematics keypad.
 *
 * Each key has:
 *   label   LaTeX shown on the button (rendered with KaTeX)
 *   insert  plain text inserted into the input (SymPy-parseable: ``^`` powers,
 *           ``sqrt(`` surds, ``,`` decimals, ``*`` / ``/`` operators)
 *   offset  optional caret offset after insertion (e.g. -1 to sit inside "()")
 *   title   accessible tooltip title
 *
 * Keys are grouped so topics declare which groups they need.
 */
export const KEYPAD_GROUPS = {
    arithmetic: [
        { label: '+', insert: ' + ', title: 'Addition' },
        { label: '-', insert: ' - ', title: 'Subtraction' },
        { label: '\\times', insert: ' * ', title: 'Multiplication' },
        { label: '\\div', insert: ' / ', title: 'Division' },
        { label: '=', insert: ' = ', title: 'Equals' },
        { label: ',', insert: ',', title: 'Decimal Comma (SA)' },
        { label: '\\pm', insert: ' +- ', title: 'Plus-minus' },
        { label: '\\approx', insert: ' approx ', title: 'Approximately' },
    ],
    powers_roots: [
        { label: 'x^2', insert: '^2', title: 'Square (superscript 2)' },
        { label: 'x^3', insert: '^3', title: 'Cube (superscript 3)' },
        { label: 'x^{n}', insert: '^()', offset: -1, title: 'Power / Exponent n' },
        { label: 'x^{-1}', insert: '^(-1)', title: 'Inverse power -1' },
        { label: 'a^b', insert: '^()', offset: -1, title: 'Superscript power' },
        { label: '\\sqrt{\\;}', insert: 'sqrt()', offset: -1, title: 'Square root' },
        { label: '\\sqrt[3]{\\;}', insert: 'cbrt()', offset: -1, title: 'Cube root' },
        { label: '\\sqrt[n]{\\;}', insert: 'root(n, )', offset: -1, title: 'Nth root' },
    ],
    fractions_division: [
        { label: '\\dfrac{a}{b}', insert: '()/()', offset: -4, title: 'Fraction' },
        { label: '\\dfrac{1}{x}', insert: '1/', title: 'Reciprocal fraction' },
        { label: '\\overline{)\\;}', insert: ' / ', title: 'Long division' },
        { label: '\\div', insert: ' / ', title: 'Division symbol' },
        { label: '%', insert: '%', title: 'Percent' },
    ],
    subscripts: [
        { label: 'x_1', insert: 'x_1', title: 'Subscript 1' },
        { label: 'x_2', insert: 'x_2', title: 'Subscript 2' },
        { label: 'y_1', insert: 'y_1', title: 'Subscript y1' },
        { label: 'y_2', insert: 'y_2', title: 'Subscript y2' },
        { label: 'T_n', insert: 'T_n', title: 'Sequence term Tn' },
        { label: 'T_{n-1}', insert: 'T_{n-1}', title: 'Previous term Tn-1' },
        { label: 'a_n', insert: '_()', offset: -1, title: 'Custom Subscript' },
        { label: 'n', insert: 'n', title: 'Variable n' },
        { label: '\\ldots', insert: '...', title: 'Ellipsis' },
    ],
    algebra: [
        { label: 'x', insert: 'x', title: 'Variable x' },
        { label: 'y', insert: 'y', title: 'Variable y' },
        { label: 'a', insert: 'a', title: 'Variable a' },
        { label: 'b', insert: 'b', title: 'Variable b' },
        { label: '(\\;)', insert: '()', offset: -1, title: 'Parentheses' },
        { label: '[\\;]', insert: '[]', offset: -1, title: 'Square brackets' },
        { label: '\\{\\;\\}', insert: '{}', offset: -1, title: 'Curly braces' },
    ],
    inequalities: [
        { label: '<', insert: ' < ', title: 'Less than' },
        { label: '>', insert: ' > ', title: 'Greater than' },
        { label: '\\leq', insert: ' <= ', title: 'Less than or equal' },
        { label: '\\geq', insert: ' >= ', title: 'Greater than or equal' },
        { label: '\\neq', insert: ' != ', title: 'Not equal' },
        { label: '\\infty', insert: 'oo', title: 'Infinity' },
    ],
    trigonometry: [
        { label: '\\sin', insert: 'sin()', offset: -1, title: 'Sine' },
        { label: '\\cos', insert: 'cos()', offset: -1, title: 'Cosine' },
        { label: '\\tan', insert: 'tan()', offset: -1, title: 'Tangent' },
        { label: '\\theta', insert: 'theta', title: 'Theta' },
        { label: '^{\\circ}', insert: 'deg', title: 'Degrees' },
        { label: '\\pi', insert: 'pi', title: 'Pi' },
        { label: '\\angle', insert: 'angle ', title: 'Angle' },
        { label: '\\triangle', insert: 'triangle ', title: 'Triangle' },
    ],
};

// Aliases for backwards-compatibility
KEYPAD_GROUPS.exponents = KEYPAD_GROUPS.powers_roots;
KEYPAD_GROUPS.sequences = KEYPAD_GROUPS.subscripts;

export const KEYPAD_CATEGORY_TABS = [
    { id: 'topic', label: 'Topic Keys' },
    { id: 'powers_roots', label: 'Powers & Roots' },
    { id: 'fractions_division', label: 'Fractions & Div' },
    { id: 'subscripts', label: 'Subscripts' },
    { id: 'algebra', label: 'Algebra' },
    { id: 'trigonometry', label: 'Trig & Angles' },
    { id: 'inequalities', label: 'Inequalities' },
    { id: 'all', label: 'All Symbols' },
];

export const TOPIC_KEYPADS = {
    grade10_math_algebraic_expressions: ['algebra', 'powers_roots', 'fractions_division', 'arithmetic'],
    grade10_math_exponents: ['powers_roots', 'fractions_division', 'algebra', 'arithmetic'],
    grade10_math_trigonometry: ['trigonometry', 'powers_roots', 'fractions_division', 'algebra', 'arithmetic'],
    grade10_math_equations_inequalities: ['algebra', 'inequalities', 'powers_roots', 'arithmetic'],
    grade10_math_patterns_sequences: ['subscripts', 'algebra', 'arithmetic'],
};

/** Resolve the flat key list for a topic (deduped, group order preserved). */
export const getKeypadForTopic = (topic) => {
    const raw = String(topic || '').toLowerCase();
    let groups = [];

    if (TOPIC_KEYPADS[topic]) {
        groups = TOPIC_KEYPADS[topic];
    } else if (raw.includes('exponent') || raw.includes('power') || raw.includes('surd') || raw.includes('radic')) {
        groups = ['powers_roots', 'fractions_division', 'algebra', 'arithmetic'];
    } else if (raw.includes('trig')) {
        groups = ['trigonometry', 'powers_roots', 'fractions_division', 'algebra', 'arithmetic'];
    } else if (raw.includes('sequence') || raw.includes('pattern') || raw.includes('series')) {
        groups = ['subscripts', 'algebra', 'powers_roots', 'arithmetic'];
    } else if (raw.includes('equation') || raw.includes('inequal') || raw.includes('algebra')) {
        groups = ['algebra', 'powers_roots', 'fractions_division', 'inequalities', 'arithmetic'];
    } else if (raw.includes('fraction') || raw.includes('decimal') || raw.includes('ratio')) {
        groups = ['fractions_division', 'arithmetic', 'powers_roots', 'algebra'];
    } else if (raw.includes('whole') || raw.includes('number') || raw.includes('integer')) {
        groups = ['arithmetic', 'powers_roots', 'fractions_division', 'algebra'];
    } else if (raw.includes('geometry') || raw.includes('angle') || raw.includes('shape')) {
        groups = ['trigonometry', 'algebra', 'arithmetic', 'powers_roots'];
    } else if (raw.includes('function') || raw.includes('graph')) {
        groups = ['powers_roots', 'fractions_division', 'subscripts', 'algebra', 'arithmetic'];
    } else {
        // Broad default for general mathematics
        groups = ['powers_roots', 'fractions_division', 'subscripts', 'algebra', 'arithmetic'];
    }

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

/** Get keys for a specific category tab */
export const getKeysForCategory = (category, topic) => {
    if (category === 'topic') return getKeypadForTopic(topic);
    if (category === 'all') {
        const keys = [];
        const seen = new Set();
        for (const groupName of Object.keys(KEYPAD_GROUPS)) {
            for (const key of KEYPAD_GROUPS[groupName] || []) {
                if (!seen.has(key.insert + key.label)) {
                    seen.add(key.insert + key.label);
                    keys.push(key);
                }
            }
        }
        return keys;
    }
    return KEYPAD_GROUPS[category] || getKeypadForTopic(topic);
};
