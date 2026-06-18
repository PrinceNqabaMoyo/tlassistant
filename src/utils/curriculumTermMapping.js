/**
 * Curriculum Term Mapping Utility
 * 
 * Maps visual aid tools to specific terms and topics based on CAPS curriculum
 * This enables contextual filtering and adaptive tool configurations
 */

import { curriculumData } from '../curriculumData';

// South African CAPS term structure (4 terms, ~10 weeks each)
export const TERM_STRUCTURE = {
    1: { name: 'Term 1', weeks: 11, description: 'Foundation & Introduction' },
    2: { name: 'Term 2', weeks: 10, description: 'Development & Mid-year' },
    3: { name: 'Term 3', weeks: 10, description: 'Application & Trial Exams' },
    4: { name: 'Term 4', weeks: 9, description: 'Integration & Final Exams' }
};

/**
 * Visual Aid to Curriculum Term Mapping
 * Based on official CAPS curriculum documents and syllabus analysis
 */
export const VISUAL_AID_TERM_MAPPING = {
    'Mathematics': {
        7: {
            'number_line': [1, 2],
            'fraction_visualizer': [1, 2],
            'coordinate_plane': [3, 4],
            'geometric_construction': [2, 3],
            'statistical_analysis': [4],
            'probability_simulator': [4]
        },
        8: {
            'number_line': [1],
            'fraction_visualizer': [1, 2],
            'coordinate_plane': [2, 3],
            'geometric_construction': [2, 3],
            'statistical_analysis': [4],
            'probability_simulator': [4],
            'algebraic_expression_builder': [3, 4]
        },
        9: {
            'number_line': [1],
            'fraction_visualizer': [1],
            'coordinate_plane': [2, 3],
            'geometric_construction': [2, 3],
            'statistical_analysis': [3, 4],
            'probability_simulator': [4],
            'algebraic_expression_builder': [1, 2, 3],
            'linear_function': [3, 4]
        },
        10: {
            'algebraic_expression_builder': [1],
            'linear_function': [2],
            'quadratic_function': [2, 3],
            'coordinate_plane': [2, 3],
            'geometric_construction': [3],
            'trigonometric_function': [4],
            'statistical_analysis': [1, 4],
            'probability_simulator': [1, 4]
        },
        11: {
            'algebraic_expression_builder': [1],
            'quadratic_function': [1, 2],
            'exponential_function': [2],
            'trigonometric_function': [3, 4],
            'coordinate_plane': [1, 2],
            'geometric_construction': [3],
            'statistical_analysis': [4],
            'probability_simulator': [4]
        },
        12: {
            'quadratic_function': [1],
            'exponential_function': [1],
            'trigonometric_function': [3],
            'calculus_tools': [1, 2],
            'coordinate_plane': [1, 2],
            'geometric_construction': [2, 3],
            'statistical_analysis': [3, 4],
            'probability_simulator': [4]
        }
    },
    
    'Technical Mathematics': {
        10: {
            'algebraic_expression_builder': [1],
            'number_line': [1],
            'coordinate_plane': [1, 2],
            'quadratic_function': [2],
            'geometric_construction': [2, 3],
            'trigonometric_function': [3, 4],
            'circle_geometry': [3]
        },
        11: {
            'algebraic_expression_builder': [1],
            'quadratic_function': [1],
            'exponential_function': [1],
            'trigonometric_function': [2, 3],
            'coordinate_plane': [1, 2],
            'geometric_construction': [2],
            'circle_geometry': [3]
        },
        12: {
            'complex_numbers': [1],
            'quadratic_function': [1],
            'calculus_tools': [1, 2], // Differentiation & Integration
            'trigonometric_function': [3],
            'coordinate_plane': [2],
            'geometric_construction': [2, 3]
        }
    },
    
    'Mathematical Literacy': {
        10: {
            'number_line': [1],
            'fraction_visualizer': [1],
            'bar_chart': [1, 4],
            'pie_chart': [1, 4],
            'line_graph': [1, 4],
            'coordinate_plane': [2, 3],
            'statistical_analysis': [4]
        },
        11: {
            'bar_chart': [1, 3],
            'pie_chart': [1, 3],
            'line_graph': [1, 3],
            'coordinate_plane': [2],
            'statistical_analysis': [3],
            'probability_simulator': [3]
        },
        12: {
            'bar_chart': [1],
            'pie_chart': [1],
            'line_graph': [1],
            'statistical_analysis': [1],
            'probability_simulator': [3],
            'coordinate_plane': [2]
        }
    }
};

/**
 * Topic-based adaptive configurations for visual aids
 */
export const ADAPTIVE_CONFIGURATIONS = {
    'quadratic_function': {
        'Mathematics_10_Term_2': {
            title: "Quadratic Functions - Introduction",
            focusAreas: ['parabola shape', 'vertex', 'axis of symmetry'],
            examples: ['y = x²', 'y = 2x²', 'y = -x²'],
            difficulty: 'introduction',
            config: {
                a: 1, b: 0, c: 0,
                showVertex: true,
                showAxis: true,
                showRoots: false,
                showDiscriminant: false
            }
        },
        'Mathematics_10_Term_3': {
            title: "Quadratic Functions - Solving Equations",
            focusAreas: ['finding roots', 'factoring', 'quadratic formula'],
            examples: ['y = x² - 4', 'y = x² + 2x - 3'],
            difficulty: 'intermediate',
            config: {
                a: 1, b: 0, c: -4,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showDiscriminant: false
            }
        },
        'Mathematics_11_Term_1': {
            title: "Quadratic Functions - Advanced Analysis",
            focusAreas: ['discriminant', 'nature of roots', 'completing square'],
            examples: ['y = 2x² - 4x + 3', 'y = -x² + 4x - 5'],
            difficulty: 'advanced',
            config: {
                a: 2, b: -4, c: 3,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showDiscriminant: true
            }
        },
        'TechnicalMathematics_12_Term_1': {
            title: "Polynomial Functions - Calculus Ready",
            focusAreas: ['optimization', 'derivatives', 'turning points'],
            examples: ['y = x² - 6x + 8', 'optimization problems'],
            difficulty: 'advanced',
            config: {
                a: 1, b: -6, c: 8,
                showVertex: true,
                showAxis: true,
                showRoots: true,
                showDiscriminant: true,
                showDerivative: true,
                showTangent: true
            }
        }
    },
    
    'trigonometric_function': {
        'Mathematics_10_Term_4': {
            title: "Trigonometry - Basic Ratios",
            focusAreas: ['sine', 'cosine', 'tangent', 'special angles'],
            examples: ['sin(30°)', 'cos(45°)', 'tan(60°)'],
            difficulty: 'introduction',
            config: {
                function: 'sin',
                amplitude: 1,
                period: 360,
                phase: 0,
                showUnitCircle: true,
                showSpecialAngles: true,
                angleMode: 'degrees'
            }
        },
        'TechnicalMathematics_11_Term_2': {
            title: "Trigonometric Graphs",
            focusAreas: ['sine curve', 'cosine curve', 'amplitude', 'period'],
            examples: ['y = 2sin(x)', 'y = cos(2x)', 'y = sin(x) + 1'],
            difficulty: 'intermediate',
            config: {
                function: 'sin',
                amplitude: 2,
                period: 180,
                phase: 0,
                showUnitCircle: false,
                showSpecialAngles: false,
                angleMode: 'degrees',
                showTransformations: true
            }
        },
        'TechnicalMathematics_12_Term_3': {
            title: "Advanced Trigonometry",
            focusAreas: ['compound angles', 'identities', 'calculus applications'],
            examples: ['sin(A+B)', 'd/dx[sin(x)]', 'trigonometric equations'],
            difficulty: 'advanced',
            config: {
                function: 'sin',
                amplitude: 1,
                period: 180,
                phase: 30,
                showUnitCircle: false,
                showSpecialAngles: false,
                angleMode: 'degrees',
                showDerivative: true,
                showIdentities: true
            }
        }
    }
};

/**
 * Get visual aids appropriate for current curriculum context
 */
export function getContextualVisualAids(subject, grade, term) {
    const subjectKey = subject.replace(' ', '');
    const mapping = VISUAL_AID_TERM_MAPPING[subjectKey];
    
    if (!mapping || !mapping[grade]) {
        return [];
    }
    
    const gradeMapping = mapping[grade];
    const contextualAids = [];
    
    for (const [aidId, termList] of Object.entries(gradeMapping)) {
        if (termList.includes(term)) {
            contextualAids.push({
                id: aidId,
                relevance: 'high',
                termAlignment: termList
            });
        }
    }
    
    return contextualAids;
}

/**
 * Get adaptive configuration for a specific visual aid
 */
export function getAdaptiveConfiguration(aidId, subject, grade, term) {
    const configKey = `${subject.replace(' ', '')}_${grade}_Term_${term}`;
    const aidConfigs = ADAPTIVE_CONFIGURATIONS[aidId];
    
    if (!aidConfigs) {
        return null;
    }
    
    // Look for exact match first
    if (aidConfigs[configKey]) {
        return aidConfigs[configKey];
    }
    
    // Look for fallback configurations
    const fallbackKeys = Object.keys(aidConfigs).filter(key => 
        key.includes(`${subject.replace(' ', '')}_${grade}`)
    );
    
    if (fallbackKeys.length > 0) {
        return aidConfigs[fallbackKeys[0]];
    }
    
    return null;
}

/**
 * Get current curriculum topics for grade and term
 */
export function getCurrentCurriculumTopics(subject, grade, term) {
    const subjectKey = subject.toLowerCase().replace(' ', '_');
    const subjectData = curriculumData[subjectKey];
    
    if (!subjectData || !subjectData[grade]) {
        return [];
    }
    
    // For now, return all topics for the grade
    // In future, this could be enhanced with term-specific topic mapping
    return subjectData[grade].topics || [];
}

/**
 * Check if a visual aid is currently relevant
 */
export function isVisualAidRelevant(aidId, subject, grade, term, strictMode = false) {
    const contextualAids = getContextualVisualAids(subject, grade, term);
    const isInCurrentTerm = contextualAids.some(aid => aid.id === aidId);
    
    if (strictMode) {
        return isInCurrentTerm;
    }
    
    // In non-strict mode, also check adjacent terms
    const adjacentTerms = [term - 1, term, term + 1].filter(t => t >= 1 && t <= 4);
    return adjacentTerms.some(t => 
        getContextualVisualAids(subject, grade, t).some(aid => aid.id === aidId)
    );
}

/**
 * Get learning progression for a visual aid across grades
 */
export function getVisualAidProgression(aidId, subject) {
    const subjectKey = subject.replace(' ', '');
    const mapping = VISUAL_AID_TERM_MAPPING[subjectKey];
    
    if (!mapping) return [];
    
    const progression = [];
    
    for (const [grade, aids] of Object.entries(mapping)) {
        if (aids[aidId]) {
            progression.push({
                grade: parseInt(grade),
                terms: aids[aidId],
                complexity: getComplexityLevel(aidId, subject, grade)
            });
        }
    }
    
    return progression.sort((a, b) => a.grade - b.grade);
}

/**
 * Get complexity level for a visual aid at specific grade
 */
function getComplexityLevel(aidId, subject, grade) {
    const config = getAdaptiveConfiguration(aidId, subject, grade, 1);
    return config?.difficulty || 'intermediate';
}

export default {
    TERM_STRUCTURE,
    VISUAL_AID_TERM_MAPPING,
    ADAPTIVE_CONFIGURATIONS,
    getContextualVisualAids,
    getAdaptiveConfiguration,
    getCurrentCurriculumTopics,
    isVisualAidRelevant,
    getVisualAidProgression
};