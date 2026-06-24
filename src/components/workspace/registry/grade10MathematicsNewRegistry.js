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
};
