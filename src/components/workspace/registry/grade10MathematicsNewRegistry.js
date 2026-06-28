import { createMathTopicRegistry } from '../shared/mathx/createMathTopicRegistry';

/**
 * Rebuilt Grade 10 Mathematics registry (SymPy-backed, KaTeX-rendered, with the
 * Working Pad + procedure tracker). Spread AFTER the legacy
 * ``grade10MathematicsRegistry`` so these modes take over as topics migrate.
 */
export const grade10MathematicsNewRegistry = {
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_algebraic_expressions',
        modePrefix: 'grade10_algebraic_expressions',
    }),
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_exponents',
        modePrefix: 'grade10_exponents',
    }),
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_equations_inequalities',
        modePrefix: 'grade10_equations_inequalities',
    }),
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_patterns_sequences',
        modePrefix: 'grade10_patterns_sequences',
    }),
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_trigonometry',
        modePrefix: 'grade10_trigonometry_1',
    }),
    ...createMathTopicRegistry({
        topicKey: 'grade10_math_functions',
        modePrefix: 'grade10_functions',
    }),
};
