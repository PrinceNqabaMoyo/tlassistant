import React from 'react';

/**
 * Centralized Visual Aid Serializer
 * Converts visual aid states into AI-understandable formats for all subjects
 * Supports JSON and POML output formats
 */
const VisualAidSerializer = ({ 
    visualAidData, 
    visualAidType, 
    format = 'json', // 'json' | 'poml' | 'both'
    onSerialize 
}) => {
    
    // Serialize visual aid data to JSON for all subject types
    const serializeToJSON = (data, type) => {
        const baseStructure = {
            type: type,
            timestamp: new Date().toISOString(),
            version: "1.0"
        };

        switch (type.toLowerCase()) {
            // Mathematics Visual Aids
            case 'linear_function':
            case 'linear_function_graph':
                return {
                    ...baseStructure,
                    data: {
                        slope: data.m,
                        y_intercept: data.c,
                        x_intercept: data.xIntercept,
                        equation: data.equation,
                        x_range: data.x_range,
                        y_range: data.y_range,
                        display_options: {
                            show_grid: data.showGrid,
                            show_points: data.showPoints,
                            show_slope: data.showSlope,
                            show_y_intercept: data.showYIntercept,
                            show_x_intercept: data.showXIntercept
                        }
                    }
                };

            case 'quadratic_function':
            case 'quadratic_graph':
                return {
                    ...baseStructure,
                    data: {
                        coefficients: {
                            a: data.a,
                            b: data.b,
                            c: data.c
                        },
                        vertex: data.vertex,
                        roots: data.roots,
                        equation: data.equation,
                        x_range: data.x_range,
                        y_range: data.y_range,
                        display_options: {
                            show_grid: data.showGrid,
                            show_points: data.showPoints,
                            show_vertex: data.showVertex,
                            show_roots: data.showRoots
                        }
                    }
                };

            case 'statistical_analysis':
            case 'box_whisker_plot':
            case 'boxplot':
                return {
                    ...baseStructure,
                    data: {
                        datasets: data.dataSet?.map(dataset => ({
                            label: dataset.label,
                            values: dataset.values,
                            statistics: {
                                min: Math.min(...dataset.values),
                                q1: calculateQuartile(dataset.values, 0.25),
                                median: calculateQuartile(dataset.values, 0.5),
                                q3: calculateQuartile(dataset.values, 0.75),
                                max: Math.max(...dataset.values),
                                mean: dataset.values.reduce((a, b) => a + b, 0) / dataset.values.length
                            }
                        })) || [],
                        display_options: {
                            show_outliers: data.showOutliers,
                            show_mean: data.showMean,
                            show_median: data.showMedian,
                            show_quartiles: data.showQuartiles
                        }
                    }
                };

            case 'geometric_construction':
            case 'coordinate_plane':
            case 'coordinate_system':
                return {
                    ...baseStructure,
                    data: {
                        x_range: data.x_range,
                        y_range: data.y_range,
                        points: data.points || [],
                        lines: data.lines || [],
                        display_options: {
                            show_grid: data.showGrid,
                            show_axes: data.showAxes,
                            show_points: data.showPoints
                        }
                    }
                };

            // Accounting Visual Aids
            case 'balance_sheet':
                return {
                    ...baseStructure,
                    data: {
                        assets: {
                            current: data.assets?.current || {},
                            non_current: data.assets?.non_current || {}
                        },
                        liabilities: {
                            current: data.liabilities?.current || {},
                            non_current: data.liabilities?.non_current || {}
                        },
                        equity: data.equity || {},
                        total_assets: calculateTotalAssets(data.assets),
                        total_liabilities: calculateTotalLiabilities(data.liabilities),
                        total_equity: calculateTotalEquity(data.equity)
                    }
                };

            case 'income_statement':
                return {
                    ...baseStructure,
                    data: {
                        revenue: data.revenue || {},
                        expenses: data.expenses || {},
                        gross_profit: data.grossProfit,
                        net_income: data.netIncome,
                        period: data.period
                    }
                };

            case 't_accounts':
                return {
                    ...baseStructure,
                    data: {
                        accounts: data.accounts || [],
                        transactions: data.transactions || [],
                        balances: data.balances || {}
                    }
                };

            case 'cash_flow':
                return {
                    ...baseStructure,
                    data: {
                        operating_activities: data.operatingActivities || {},
                        investing_activities: data.investingActivities || {},
                        financing_activities: data.financingActivities || {},
                        net_cash_flow: data.netCashFlow
                    }
                };

            // Physics Visual Aids
            case 'motion_graphs':
                return {
                    ...baseStructure,
                    data: {
                        initial_velocity: data.initial_velocity,
                        acceleration: data.acceleration,
                        time_range: data.time_range,
                        units: data.units,
                        display_options: {
                            show_position: data.show_position,
                            show_velocity: data.show_velocity,
                            show_acceleration: data.show_acceleration
                        }
                    }
                };

            case 'force_diagram':
                return {
                    ...baseStructure,
                    data: {
                        forces: data.forces || [],
                        object_mass: data.object_mass,
                        net_force: calculateNetForce(data.forces),
                        units: data.units
                    }
                };

            // Chemistry Visual Aids
            case 'molecular_structure':
                return {
                    ...baseStructure,
                    data: {
                        molecule_name: data.molecule_name,
                        chemical_formula: data.chemical_formula,
                        atoms: data.atoms || [],
                        bonds: data.bonds || [],
                        molecular_geometry: data.molecular_geometry,
                        units: data.units
                    }
                };

            case 'chemical_reaction':
                return {
                    ...baseStructure,
                    data: {
                        reaction_name: data.reaction_name,
                        reactants: data.reactants || [],
                        products: data.products || [],
                        reaction_type: data.reaction_type,
                        enthalpy_change: data.enthalpy_change,
                        units: data.units,
                        is_balanced: checkReactionBalance(data.reactants, data.products)
                    }
                };

            default:
                return {
                    ...baseStructure,
                    data: data,
                    error: "Unknown visual aid type"
                };
        }
    };

    // Helper functions for calculations
    const calculateQuartile = (values, q) => {
        if (!values || values.length === 0) return 0;
        const sorted = [...values].sort((a, b) => a - b);
        const pos = (sorted.length - 1) * q;
        const base = Math.floor(pos);
        const rest = pos - base;
        if (sorted[base + 1] !== undefined) {
            return sorted[base] + rest * (sorted[base + 1] - sorted[base]);
        } else {
            return sorted[base];
        }
    };

    const calculateTotalAssets = (assets) => {
        if (!assets) return 0;
        let total = 0;
        Object.values(assets).forEach(category => {
            Object.values(category).forEach(value => {
                total += parseFloat(value) || 0;
            });
        });
        return total;
    };

    const calculateTotalLiabilities = (liabilities) => {
        if (!liabilities) return 0;
        let total = 0;
        Object.values(liabilities).forEach(category => {
            Object.values(category).forEach(value => {
                total += parseFloat(value) || 0;
            });
        });
        return total;
    };

    const calculateTotalEquity = (equity) => {
        if (!equity) return 0;
        let total = 0;
        Object.values(equity).forEach(value => {
            total += parseFloat(value) || 0;
        });
        return total;
    };

    const calculateNetForce = (forces) => {
        if (!forces || forces.length === 0) return { magnitude: 0, angle: 0 };
        let fx = 0, fy = 0;
        forces.forEach(force => {
            const angleRad = (force.angle * Math.PI) / 180;
            fx += force.magnitude * Math.cos(angleRad);
            fy += force.magnitude * Math.sin(angleRad);
        });
        const magnitude = Math.sqrt(fx * fx + fy * fy);
        const angle = Math.atan2(fy, fx) * 180 / Math.PI;
        return { magnitude, angle, fx, fy };
    };

    const checkReactionBalance = (reactants, products) => {
        if (!reactants || !products) return false;
        const reactantMoles = reactants.reduce((total, item) => total + (item.coefficient * item.moles), 0);
        const productMoles = products.reduce((total, item) => total + (item.coefficient * item.moles), 0);
        return Math.abs(reactantMoles - productMoles) < 0.01;
    };

    // Serialize visual aid data to POML
    const serializeToPOML = (data, type) => {
        const jsonData = serializeToJSON(data, type);
        let poml = `# Visual Aid Data - ${type}\n`;
        poml += `# Generated: ${jsonData.timestamp}\n`;
        poml += `# Version: ${jsonData.version}\n\n`;
        
        poml += `[metadata]\n`;
        poml += `type = ${jsonData.type}\n`;
        poml += `timestamp = ${jsonData.timestamp}\n`;
        poml += `version = ${jsonData.version}\n\n`;
        
        poml += `[data]\n`;
        serializeObjectToPOML(jsonData.data, poml, 'data');
        
        return poml;
    };

    // Recursively serialize object to POML format
    const serializeObjectToPOML = (obj, poml, section) => {
        Object.entries(obj).forEach(([key, value]) => {
            if (typeof value === 'object' && value !== null && !Array.isArray(value)) {
                poml += `\n[${section}.${key}]\n`;
                serializeObjectToPOML(value, poml, `${section}.${key}`);
            } else if (Array.isArray(value)) {
                poml += `${key} = [${value.join(', ')}]\n`;
            } else if (typeof value === 'boolean') {
                poml += `${key} = ${value}\n`;
            } else if (typeof value === 'number') {
                poml += `${key} = ${value}\n`;
            } else {
                poml += `${key} = "${value}"\n`;
            }
        });
    };

    // Handle serialization
    const handleSerialize = () => {
        if (!visualAidData || !visualAidType) {
            console.error('Missing visual aid data or type');
            return;
        }

        let result = {};
        
        if (format === 'json' || format === 'both') {
            result.json = serializeToJSON(visualAidData, visualAidType);
        }
        
        if (format === 'poml' || format === 'both') {
            result.poml = serializeToPOML(visualAidData, visualAidType);
        }

        if (onSerialize) {
            onSerialize(result);
        }

        return result;
    };

    // Auto-serialize when component mounts or data changes
    React.useEffect(() => {
        if (visualAidData && visualAidType) {
            handleSerialize();
        }
    }, [visualAidData, visualAidType]);

    return (
        <div className="visual-aid-serializer">
            <div className="mb-4">
                <h3 className="text-lg font-semibold text-gray-800 mb-2">
                    Visual Aid Serializer
                </h3>
                <p className="text-sm text-gray-600">
                    Converts visual aid state to AI-understandable formats for all subjects
                </p>
            </div>

            <div className="space-y-4">
                <div className="flex space-x-2">
                    <button
                        onClick={() => handleSerialize()}
                        className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors"
                    >
                        Serialize Now
                    </button>
                    
                    <select
                        value={format}
                        onChange={(e) => format = e.target.value}
                        className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="json">JSON Only</option>
                        <option value="poml">POML Only</option>
                        <option value="both">Both Formats</option>
                    </select>
                </div>

                {visualAidData && visualAidType && (
                    <div className="text-sm text-gray-600">
                        <p><strong>Type:</strong> {visualAidType}</p>
                        <p><strong>Data Points:</strong> {Object.keys(visualAidData).length}</p>
                        <p><strong>Subject:</strong> {getSubjectFromType(visualAidType)}</p>
                    </div>
                )}

                {!visualAidData && (
                    <div className="text-amber-600 text-sm">
                        ⚠️ No visual aid data available for serialization
                    </div>
                )}
            </div>
        </div>
    );
};

// Helper function to determine subject from visual aid type
const getSubjectFromType = (type) => {
    const mathTypes = ['linear_function', 'quadratic_function', 'statistical_analysis', 'geometric_construction'];
    const accountingTypes = ['balance_sheet', 'income_statement', 't_accounts', 'cash_flow'];
    const physicsTypes = ['motion_graphs', 'force_diagram'];
    const chemistryTypes = ['molecular_structure', 'chemical_reaction'];

    if (mathTypes.includes(type)) return 'Mathematics';
    if (accountingTypes.includes(type)) return 'Accounting';
    if (physicsTypes.includes(type)) return 'Physics';
    if (chemistryTypes.includes(type)) return 'Chemistry';
    return 'Unknown';
};

export default VisualAidSerializer;
