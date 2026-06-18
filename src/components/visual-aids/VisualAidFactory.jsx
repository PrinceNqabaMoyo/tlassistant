import React from 'react';

// Import all subject-specific visual aid components
import MathVisualAids from './subjects/MathVisualAids';
import AccountingVisualAids from './subjects/AccountingVisualAids';
import PhysicsVisualAids from './subjects/PhysicsVisualAids';
import ChemistryVisualAids from './subjects/ChemistryVisualAids';

/**
 * Centralized Visual Aid Factory
 * Creates visual aids for any subject based on specification
 * Located outside subject-specific folders for reusability
 */
class VisualAidFactory {
    constructor() {
        // Register all available visual aid types
        this.availableTypes = {
            // Math
            'linear-function': MathVisualAids.LinearFunctionGraph,
            'quadratic-function': MathVisualAids.QuadraticFunctionGraph,
            'statistical-analysis': MathVisualAids.StatisticalAnalysis,
            'geometric-construction': MathVisualAids.GeometricConstruction,
            
            // Accounting
            'balance-sheet': AccountingVisualAids.BalanceSheet,
            'income-statement': AccountingVisualAids.IncomeStatement,
            't-accounts': AccountingVisualAids.TAccounts,
            'cash-flow': AccountingVisualAids.CashFlowStatement,
            
            // Physics
            'motion-graphs': PhysicsVisualAids.MotionGraphs,
            'force-diagram': PhysicsVisualAids.ForceDiagram,
            'pulse-simulator': PhysicsVisualAids.PulseSimulator,
            'sound-wave-analyzer': PhysicsVisualAids.SoundWaveAnalyzer,
            'motion-graph-builder': PhysicsVisualAids.MotionGraphBuilder,
            'free-fall-simulator': PhysicsVisualAids.FreeFallSimulator,
            'superposition-visualizer': PhysicsVisualAids.SuperpositionVisualizer,
            'electric-field-visualizer': PhysicsVisualAids.ElectricFieldVisualizer,
            'capacitor-charging-simulator': PhysicsVisualAids.CapacitorChargingSimulator,
            'electromagnetic-induction-simulator': PhysicsVisualAids.ElectromagneticInductionSimulator,
            'ac-circuit-analyzer': PhysicsVisualAids.ACCircuitAnalyzer,
            
            // Chemistry
            'molecular-structure': ChemistryVisualAids.MolecularStructure,
            'chemical-reaction': ChemistryVisualAids.ChemicalReaction,
            'matter-classification': ChemistryVisualAids.MatterClassificationSimulator,
            'states-of-matter': ChemistryVisualAids.StatesOfMatterVisualizer,
            'atomic-structure': ChemistryVisualAids.AtomicStructureBuilder,
            'isotope-calculator': ChemistryVisualAids.IsotopeCalculator,
            'gas-law-simulator': ChemistryVisualAids.GasLawSimulator,
            'equilibrium-constant': ChemistryVisualAids.EquilibriumConstantCalculator,
            'le-chatelier': ChemistryVisualAids.LeChatelierSimulator,
            'oxidation-number': ChemistryVisualAids.OxidationNumberCalculator,
            'buffer-solution': ChemistryVisualAids.BufferSolutionBuilder,
            'advanced-stoichiometry': ChemistryVisualAids.AdvancedStoichiometryCalculator
        };
    }

    /**
     * Create a visual aid component based on specification
     * @param {string|object} specification - Visual aid specification
     * @param {object} config - Configuration options
     * @param {string} mode - 'ai-generated' | 'user-interactive' | 'read-only'
     * @param {function} onVisualAidChange - Callback for data changes
     * @returns {React.Component|null} - Visual aid component or null if not found
     */
    createVisualAid(specification, config = {}, mode = 'ai-generated', onVisualAidChange = null) {
        try {
            // Parse specification
            const spec = this.parseSpecification(specification);
            if (!spec) {
                console.error('Invalid specification format:', specification);
                return null;
            }

            // Get the component type
            const ComponentType = this.availableTypes[spec.type];
            if (!ComponentType) {
                console.error(`Unknown visual aid type: ${spec.type}`);
                return this.renderUnknownType(spec.type, spec.data);
            }

            // Create the component with props
            return React.createElement(ComponentType, {
                data: spec.data || {},
                config: { ...config, ...spec.config },
                mode: spec.mode || mode,
                onVisualAidChange: onVisualAidChange || spec.onVisualAidChange,
                key: `${spec.type}-${Date.now()}`
            });

        } catch (error) {
            console.error('Error creating visual aid:', error);
            return this.renderError(error.message);
        }
    }

    /**
     * Parse specification string or object
     * @param {string|object} specification - Specification to parse
     * @returns {object|null} - Parsed specification object
     */
    parseSpecification(specification) {
        if (typeof specification === 'string') {
            try {
                // Try to parse as JSON
                return JSON.parse(specification);
            } catch (e) {
                // Try to parse as simple type string
                return this.parseSimpleSpecification(specification);
            }
        } else if (typeof specification === 'object' && specification !== null) {
            return specification;
        }
        return null;
    }

    /**
     * Parse simple specification string (e.g., "linear-function:slope=2,intercept=3")
     * @param {string} specString - Simple specification string
     * @returns {object} - Parsed specification object
     */
    parseSimpleSpecification(specString) {
        const parts = specString.split(':');
        const type = parts[0];
        const data = {};

        if (parts.length > 1) {
            const params = parts[1].split(',');
            params.forEach(param => {
                const [key, value] = param.split('=');
                if (key && value !== undefined) {
                    // Try to parse as number, fallback to string
                    const numValue = parseFloat(value);
                    data[key.trim()] = isNaN(numValue) ? value.trim() : numValue;
                }
            });
        }

        return { type, data };
    }

    /**
     * Get list of available visual aid types
     * @returns {object} - Object with type categories and available types
     */
    getAvailableTypes() {
        return {
            'Mathematics': [
                'linear-function',
                'quadratic-function', 
                'statistical-analysis',
                'geometric-construction'
            ],
            'Accounting': [
                'balance-sheet',
                'income-statement',
                't-accounts',
                'cash-flow'
            ],
            'Physics': [
                'motion-graphs',
                'force-diagram',
                'pulse-simulator',
                'sound-wave-analyzer',
                'motion-graph-builder',
                'free-fall-simulator',
                'superposition-visualizer',
                'electric-field-visualizer',
                'capacitor-charging-simulator',
                'electromagnetic-induction-simulator',
                'ac-circuit-analyzer'
            ],
            'Chemistry': [
                'molecular-structure',
                'chemical-reaction',
                'matter-classification',
                'states-of-matter',
                'atomic-structure',
                'isotope-calculator',
                'gas-law-simulator',
                'equilibrium-constant',
                'le-chatelier',
                'oxidation-number',
                'buffer-solution',
                'advanced-stoichiometry'
            ]
        };
    }

    /**
     * Validate specification
     * @param {string|object} specification - Specification to validate
     * @returns {object} - Validation result with isValid and errors
     */
    validateSpecification(specification) {
        const result = { isValid: true, errors: [] };
        
        try {
            const spec = this.parseSpecification(specification);
            if (!spec) {
                result.isValid = false;
                result.errors.push('Invalid specification format');
                return result;
            }

            if (!spec.type) {
                result.isValid = false;
                result.errors.push('Missing visual aid type');
            } else if (!this.availableTypes[spec.type]) {
                result.isValid = false;
                result.errors.push(`Unknown visual aid type: ${spec.type}`);
            }

            // Subject-specific validation
            if (spec.type && spec.type.startsWith('linear-function')) {
                if (spec.data && typeof spec.data.m !== 'number') {
                    result.errors.push('Linear function requires slope (m) parameter');
                }
            }

            if (result.errors.length > 0) {
                result.isValid = false;
            }

        } catch (error) {
            result.isValid = false;
            result.errors.push(`Parsing error: ${error.message}`);
        }

        return result;
    }

    /**
     * Render error component
     * @param {string} errorMessage - Error message to display
     * @returns {React.Component} - Error display component
     */
    renderError(errorMessage) {
        return React.createElement('div', {
            className: 'visual-aid-error bg-red-50 border border-red-200 rounded-lg p-4 text-center'
        }, [
            React.createElement('div', {
                key: 'icon',
                className: 'text-red-500 text-2xl mb-2'
            }, '⚠️'),
            React.createElement('div', {
                key: 'title',
                className: 'text-red-800 font-semibold mb-2'
            }, 'Visual Aid Error'),
            React.createElement('div', {
                key: 'message',
                className: 'text-red-600 text-sm'
            }, errorMessage)
        ]);
    }

    /**
     * Render unknown type component
     * @param {string} type - Unknown type that was requested
     * @param {object} data - Data that was provided
     * @returns {React.Component} - Unknown type display component
     */
    renderUnknownType(type, data) {
        return React.createElement('div', {
            className: 'visual-aid-unknown bg-yellow-50 border border-yellow-200 rounded-lg p-4 text-center'
        }, [
            React.createElement('div', {
                key: 'icon',
                className: 'text-yellow-500 text-2xl mb-2'
            }, '❓'),
            React.createElement('div', {
                key: 'title',
                className: 'text-yellow-800 font-semibold mb-2'
            }, 'Unknown Visual Aid Type'),
            React.createElement('div', {
                key: 'type',
                className: 'text-yellow-600 mb-2'
            }, `Type: ${type}`),
            React.createElement('div', {
                key: 'message',
                className: 'text-yellow-600 text-sm'
            }, 'This visual aid type is not yet implemented.'),
            React.createElement('div', {
                key: 'available',
                className: 'text-yellow-500 text-xs mt-2'
            }, `Available types: ${Object.keys(this.availableTypes).join(', ')}`)
        ]);
    }

    /**
     * Get default data for a visual aid type
     * @param {string} type - Visual aid type
     * @returns {object} - Default data object
     */
    getDefaultData(type) {
        const defaults = {
            'linear-function': { m: 2, c: 3, x_range: [-5, 10] },
            'balance-sheet': {
                assets: { current: { cash: 50000 }, non_current: { equipment: 100000 } },
                liabilities: { current: { accounts_payable: 20000 } },
                equity: { share_capital: 200000 }
            },
            'motion-graphs': { initial_velocity: 10, acceleration: -2, time_range: [0, 10] },
            'molecular-structure': {
                molecule_name: 'Water',
                chemical_formula: 'H₂O',
                atoms: [
                    { symbol: 'O', x: 0, y: 0, valence: 2 },
                    { symbol: 'H', x: -1, y: 1, valence: 1 },
                    { symbol: 'H', x: 1, y: 1, valence: 1 }
                ]
            }
        };

        return defaults[type] || {};
    }

    /**
     * Create a visual aid with default data
     * @param {string} type - Visual aid type
     * @param {object} config - Configuration options
     * @param {string} mode - Display mode
     * @param {function} onVisualAidChange - Change callback
     * @returns {React.Component} - Visual aid component
     */
    createWithDefaults(type, config = {}, mode = 'user-interactive', onVisualAidChange = null) {
        const defaultData = this.getDefaultData(type);
        const specification = { type, data: defaultData, config, mode };
        return this.createVisualAid(specification, config, mode, onVisualAidChange);
    }
}

// Export singleton instance
export default new VisualAidFactory();
