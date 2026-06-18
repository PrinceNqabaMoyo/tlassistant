import React from 'react';
import VisualAidFactory from './VisualAidFactory';
import VisualAidSerializer from './VisualAidSerializer';
import AIQuestionGenerator from './AIQuestionGenerator';

/**
 * Centralized Visual Aid System
 * Handles all subject types: Math, Accounting, EMS, Physical Science, etc.
 * Located outside subject-specific folders for reusability
 */
const VisualAidSystem = ({ 
    type = 'question', // 'question' | 'factory' | 'serializer' | 'exploration'
    specification, 
    mode = 'ai-generated',
    onVisualAidChange,
    onQuestionComplete,
    onSerialize,
    isSubmitted = false
}) => {
    
    // Determine the subject type from specification
    const getSubjectType = (spec) => {
        if (typeof spec === 'string') {
            try {
                const parsed = JSON.parse(spec);
                return parsed.subject_type || parsed.type?.split('_')[0] || 'unknown';
            } catch {
                // POML parsing
                const lines = spec.split('\n');
                const subjectLine = lines.find(line => line.includes('subject_type =') || line.includes('type ='));
                if (subjectLine) {
                    const subject = subjectLine.split('=')[1].trim();
                    return subject.replace(/"/g, '').split('_')[0];
                }
            }
        } else if (spec && typeof spec === 'object') {
            return spec.subject_type || spec.type?.split('_')[0] || 'unknown';
        }
        return 'unknown';
    };

    // Get subject-specific configuration
    const getSubjectConfig = (subjectType) => {
        const configs = {
            math: {
                supportedTypes: [
                    'linear_function', 'quadratic_function', 'cubic_function',
                    'exponential_function', 'logarithmic_function', 'box_whisker_plot',
                    'coordinate_plane', 'trigonometric_function', 'statistical_analysis'
                ],
                defaultMode: 'interactive',
                validationRules: {
                    requireCoordinates: true,
                    requireRanges: true
                }
            },
            accounting: {
                supportedTypes: [
                    'balance_sheet', 'income_statement', 'cash_flow_statement',
                    't_account', 'ledger', 'trial_balance', 'chart_of_accounts',
                    'financial_ratios', 'budget_analysis', 'cost_analysis'
                ],
                defaultMode: 'readonly',
                validationRules: {
                    requireData: true,
                    requireFormatting: true
                }
            },
            ems: {
                supportedTypes: [
                    'business_plan', 'market_analysis', 'swot_analysis',
                    'financial_forecast', 'break_even_analysis', 'inventory_management',
                    'supply_chain', 'marketing_strategy', 'risk_assessment'
                ],
                defaultMode: 'interactive',
                validationRules: {
                    requireData: true,
                    requireCharts: true
                }
            },
            physical_science: {
                supportedTypes: [
                    'motion_graphs', 'force_diagrams', 'circuit_diagrams',
                    'wave_analysis', 'energy_conservation', 'thermodynamics',
                    'optics_diagrams', 'atomic_models', 'chemical_reactions'
                ],
                defaultMode: 'interactive',
                validationRules: {
                    requireUnits: true,
                    requireScales: true
                }
            },
            chemistry: {
                supportedTypes: [
                    'molecular_structures', 'reaction_mechanisms', 'equilibrium_diagrams',
                    'phase_diagrams', 'concentration_graphs', 'reaction_kinetics',
                    'electrochemistry', 'organic_compounds', 'spectroscopy'
                ],
                defaultMode: 'interactive',
                validationRules: {
                    requireFormulas: true,
                    requireStructures: true
                }
            },
            biology: {
                supportedTypes: [
                    'cell_structures', 'ecosystem_diagrams', 'genetic_analysis',
                    'evolution_trees', 'physiology_diagrams', 'biochemical_pathways',
                    'population_dynamics', 'classification_charts', 'experiment_setups'
                ],
                defaultMode: 'interactive',
                validationRules: {
                    requireLabels: true,
                    requireScales: true
                }
            }
        };
        
        return configs[subjectType] || configs.math;
    };

    // Validate specification against subject requirements
    const validateSpecification = (spec, subjectType) => {
        const config = getSubjectConfig(subjectType);
        const errors = [];
        
        if (!spec.type) {
            errors.push('Missing visual aid type');
        } else if (!config.supportedTypes.includes(spec.type)) {
            errors.push(`Type '${spec.type}' not supported for subject '${subjectType}'`);
        }
        
        // Subject-specific validation
        if (subjectType === 'math' && config.validationRules.requireCoordinates) {
            if (!spec.config?.x_range || !spec.config?.y_range) {
                errors.push('Math visual aids require coordinate ranges');
            }
        }
        
        if (subjectType === 'accounting' && config.validationRules.requireData) {
            if (!spec.config?.data && !spec.config?.dataSet) {
                errors.push('Accounting visual aids require data');
            }
        }
        
        if (subjectType === 'physical_science' && config.validationRules.requireUnits) {
            if (!spec.config?.units) {
                errors.push('Physical science visual aids should specify units');
            }
        }
        
        return {
            isValid: errors.length === 0,
            errors,
            warnings: []
        };
    };

    // Render appropriate component based on type
    const renderComponent = () => {
        const subjectType = getSubjectType(specification);
        const validation = validateSpecification(specification, subjectType);
        const subjectConfig = getSubjectConfig(subjectType);
        
        if (!validation.isValid) {
            return (
                <div className="bg-red-50 border border-red-200 rounded-lg p-4">
                    <h3 className="text-lg font-semibold text-red-800 mb-2">
                        Specification Validation Failed
                    </h3>
                    <div className="text-red-700">
                        <p><strong>Subject:</strong> {subjectType}</p>
                        <p><strong>Errors:</strong></p>
                        <ul className="list-disc list-inside ml-4">
                            {validation.errors.map((error, index) => (
                                <li key={index}>{error}</li>
                            ))}
                        </ul>
                    </div>
                </div>
            );
        }

        switch (type) {
            case 'question':
                return (
                    <AIQuestionGenerator
                        questionSpecification={specification}
                        onQuestionComplete={onQuestionComplete}
                        mode={mode}
                        subjectType={subjectType}
                        subjectConfig={subjectConfig}
                    />
                );
                
            case 'factory':
                return (
                    <VisualAidFactory
                        specification={specification}
                        mode={mode}
                        onVisualAidChange={onVisualAidChange}
                        isSubmitted={isSubmitted}
                        subjectType={subjectType}
                        subjectConfig={subjectConfig}
                    />
                );
                
            case 'serializer':
                return (
                    <VisualAidSerializer
                        visualAidData={specification}
                        visualAidType={specification?.type || 'unknown'}
                        format="both"
                        onSerialize={onSerialize}
                        subjectType={subjectType}
                        subjectConfig={subjectConfig}
                    />
                );
                
            case 'exploration':
                return (
                    <VisualAidFactory
                        specification={specification}
                        mode="user-interactive"
                        onVisualAidChange={onVisualAidChange}
                        isSubmitted={false}
                        subjectType={subjectType}
                        subjectConfig={subjectConfig}
                    />
                );
                
            default:
                return (
                    <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
                        <p className="text-yellow-800">Unknown visual aid system type: {type}</p>
                    </div>
                );
        }
    };

    return (
        <div className="visual-aid-system">
            {renderComponent()}
        </div>
    );
};

export default VisualAidSystem;
