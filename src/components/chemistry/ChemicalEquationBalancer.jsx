import React, { useState, useEffect } from 'react';

const ChemicalEquationBalancer = ({ initialData, onChange, isSubmitted }) => {
    const [reactants, setReactants] = useState(initialData.reactants || ['']);
    const [products, setProducts] = useState(initialData.products || ['']);
    const [coefficients, setCoefficients] = useState(initialData.coefficients || {});
    const [showSolution, setShowSolution] = useState(false);
    const [showBalanced, setShowBalanced] = useState(false);
    const [equationType, setEquationType] = useState(initialData.equationType || 'synthesis');
    const [showSteps, setShowSteps] = useState(false);

    // Common elements and their symbols
    const elements = {
        'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium', 'B': 'Boron',
        'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine', 'Ne': 'Neon',
        'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus',
        'S': 'Sulfur', 'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium',
        'Fe': 'Iron', 'Cu': 'Copper', 'Zn': 'Zinc', 'Ag': 'Silver', 'Au': 'Gold'
    };

    // Equation types
    const equationTypes = {
        'synthesis': 'Synthesis (A + B → AB)',
        'decomposition': 'Decomposition (AB → A + B)',
        'single_replacement': 'Single Replacement (A + BC → AC + B)',
        'double_replacement': 'Double Replacement (AB + CD → AD + CB)',
        'combustion': 'Combustion (Fuel + O₂ → CO₂ + H₂O)',
        'acid_base': 'Acid-Base (HA + BOH → H₂O + BA)',
        'redox': 'Redox (Oxidation-Reduction)'
    };

    useEffect(() => {
        const formattedData = {
            type: "chemical_equation",
            equationType: equationType,
            reactants: reactants.filter(r => r.trim() !== ''),
            products: products.filter(p => p.trim() !== ''),
            coefficients: coefficients,
            isBalanced: isEquationBalanced()
        };
        onChange(formattedData);
    }, [reactants, products, coefficients, equationType, onChange]);

    const addReactant = () => {
        if (!isSubmitted) setReactants([...reactants, '']);
    };

    const removeReactant = (index) => {
        if (!isSubmitted) setReactants(reactants.filter((_, i) => i !== index));
    };

    const addProduct = () => {
        if (!isSubmitted) setProducts([...products, '']);
    };

    const removeProduct = (index) => {
        if (!isSubmitted) setProducts(products.filter((_, i) => i !== index));
    };

    const handleReactantChange = (index, value) => {
        if (isSubmitted) return;
        const newReactants = [...reactants];
        newReactants[index] = value;
        setReactants(newReactants);
    };

    const handleProductChange = (index, value) => {
        if (isSubmitted) return;
        const newProducts = [...products];
        newProducts[index] = value;
        setProducts(newProducts);
    };

    const parseFormula = (formula) => {
        const atoms = {};
        const regex = /([A-Z][a-z]?)(\d*)/g;
        let match;
        
        while ((match = regex.exec(formula)) !== null) {
            const element = match[1];
            const count = match[2] ? parseInt(match[2]) : 1;
            atoms[element] = (atoms[element] || 0) + count;
        }
        
        return atoms;
    };

    const countAtoms = (formulas, coefficients) => {
        const totalAtoms = {};
        
        formulas.forEach((formula, index) => {
            if (formula.trim() === '') return;
            
            const atoms = parseFormula(formula);
            const coefficient = coefficients[index] || 1;
            
            Object.keys(atoms).forEach(element => {
                totalAtoms[element] = (totalAtoms[element] || 0) + (atoms[element] * coefficient);
            });
        });
        
        return totalAtoms;
    };

    const isEquationBalanced = () => {
        const reactantAtoms = countAtoms(reactants, coefficients);
        const productAtoms = countAtoms(products, coefficients);
        
        if (Object.keys(reactantAtoms).length === 0 || Object.keys(productAtoms).length === 0) {
            return false;
        }
        
        return Object.keys(reactantAtoms).every(element => 
            reactantAtoms[element] === productAtoms[element]
        );
    };

    const balanceEquation = () => {
        if (isSubmitted) return;
        
        // Simple balancing algorithm for common equations
        const newCoefficients = {};
        
        // Handle common patterns
        if (equationType === 'combustion' && reactants.length >= 2 && products.length >= 2) {
            // CₓHᵧ + O₂ → CO₂ + H₂O
            if (reactants[0].includes('C') && reactants[1] === 'O₂') {
                const carbonCount = (reactants[0].match(/C(\d*)/) || [])[1] || 1;
                const hydrogenCount = (reactants[0].match(/H(\d*)/) || [])[1] || 1;
                
                newCoefficients[0] = 1; // CₓHᵧ
                newCoefficients[1] = Math.ceil((carbonCount + hydrogenCount / 4)); // O₂
                newCoefficients[2] = carbonCount; // CO₂
                newCoefficients[3] = Math.ceil(hydrogenCount / 2); // H₂O
            }
        } else if (equationType === 'acid_base' && reactants.length >= 2 && products.length >= 2) {
            // HA + BOH → H₂O + BA
            newCoefficients[0] = 1; // HA
            newCoefficients[1] = 1; // BOH
            newCoefficients[2] = 1; // H₂O
            newCoefficients[3] = 1; // BA
        } else {
            // Generic balancing - start with 1s
            reactants.forEach((_, index) => {
                newCoefficients[index] = 1;
            });
            products.forEach((_, index) => {
                newCoefficients[reactants.length + index] = 1;
            });
        }
        
        setCoefficients(newCoefficients);
        setShowBalanced(true);
    };

    const getBalancingSteps = () => {
        const steps = [];
        
        if (equationType === 'combustion') {
            steps.push('1. Identify the hydrocarbon (CₓHᵧ) and oxygen (O₂)');
            steps.push('2. Balance carbon atoms: CO₂ coefficient = number of C atoms');
            steps.push('3. Balance hydrogen atoms: H₂O coefficient = H atoms ÷ 2');
            steps.push('4. Balance oxygen atoms: O₂ coefficient = (C + H/4)');
        } else if (equationType === 'acid_base') {
            steps.push('1. Identify the acid (HA) and base (BOH)');
            steps.push('2. Water (H₂O) is always a product');
            steps.push('3. Salt (BA) is formed from the remaining ions');
            steps.push('4. All coefficients are typically 1');
        } else {
            steps.push('1. Count atoms on each side');
            steps.push('2. Start with the most complex molecule');
            steps.push('3. Adjust coefficients to balance atoms');
            steps.push('4. Verify all atoms are balanced');
        }
        
        return steps;
    };

    const formatFormula = (formula, coefficient) => {
        if (coefficient === 1) return formula;
        return `${coefficient}${formula}`;
    };

    const getEquationString = () => {
        const reactantStr = reactants
            .map((r, i) => formatFormula(r, coefficients[i] || 1))
            .filter(r => r.trim() !== '')
            .join(' + ');
        
        const productStr = products
            .map((p, i) => formatFormula(p, coefficients[reactants.length + i] || 1))
            .filter(p => p.trim() !== '')
            .join(' + ');
        
        return `${reactantStr} → ${productStr}`;
    };

    const getAtomCounts = () => {
        const reactantAtoms = countAtoms(reactants, coefficients);
        const productAtoms = countAtoms(products, coefficients);
        
        return { reactantAtoms, productAtoms };
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Chemical Equation Balancer</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowSolution(!showSolution)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showSolution 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showSolution ? 'Hide Solution' : 'Show Solution'}
                    </button>
                    <button
                        onClick={() => setShowBalanced(!showBalanced)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showBalanced 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showBalanced ? 'Hide Balanced' : 'Show Balanced'}
                    </button>
                </div>
            </div>

            {/* Equation Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Equation Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={equationType} 
                    onChange={(e) => !isSubmitted && setEquationType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    {Object.entries(equationTypes).map(([key, value]) => (
                        <option key={key} value={key}>{value}</option>
                    ))}
                </select>
            </div>

            {/* Reactants */}
            <div className="mb-6">
                <div className="flex items-center justify-between mb-3">
                    <h4 className="text-md font-medium text-gray-800">Reactants</h4>
                    {!isSubmitted && (
                        <button 
                            onClick={addReactant}
                            className="px-3 py-1 bg-blue-600 text-white rounded-lg text-sm hover:bg-blue-700 transition-colors"
                        >
                            + Add Reactant
                        </button>
                    )}
                </div>
                <div className="space-y-3">
                    {reactants.map((reactant, index) => (
                        <div key={index} className="flex items-center space-x-3">
                            <input 
                                type="text" 
                                className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={reactant} 
                                onChange={(e) => handleReactantChange(index, e.target.value)} 
                                placeholder="e.g., H₂SO₄" 
                                disabled={isSubmitted} 
                            />
                            <input 
                                type="number" 
                                min="1"
                                className="w-20 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={coefficients[index] || 1} 
                                onChange={(e) => !isSubmitted && setCoefficients({...coefficients, [index]: parseInt(e.target.value) || 1})} 
                                disabled={isSubmitted} 
                            />
                            {!isSubmitted && reactants.length > 1 && (
                                <button 
                                    onClick={() => removeReactant(index)}
                                    className="px-3 py-1 bg-red-600 text-white rounded-lg text-sm hover:bg-red-700 transition-colors"
                                >
                                    Remove
                                </button>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Arrow */}
            <div className="text-center mb-6">
                <div className="text-2xl font-bold text-gray-600">→</div>
            </div>

            {/* Products */}
            <div className="mb-6">
                <div className="flex items-center justify-between mb-3">
                    <h4 className="text-md font-medium text-gray-800">Products</h4>
                    {!isSubmitted && (
                        <button 
                            onClick={addProduct}
                            className="px-3 py-1 bg-green-600 text-white rounded-lg text-sm hover:bg-green-700 transition-colors"
                        >
                            + Add Product
                        </button>
                    )}
                </div>
                <div className="space-y-3">
                    {products.map((product, index) => (
                        <div key={index} className="flex items-center space-x-3">
                            <input 
                                type="text" 
                                className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={product} 
                                onChange={(e) => handleProductChange(index, e.target.value)} 
                                placeholder="e.g., H₂O" 
                                disabled={isSubmitted} 
                            />
                            <input 
                                type="number" 
                                min="1"
                                className="w-20 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={coefficients[reactants.length + index] || 1} 
                                onChange={(e) => !isSubmitted && setCoefficients({...coefficients, [reactants.length + index]: parseInt(e.target.value) || 1})} 
                                disabled={isSubmitted} 
                            />
                            {!isSubmitted && products.length > 1 && (
                                <button 
                                    onClick={() => removeProduct(index)}
                                    className="px-3 py-1 bg-red-600 text-white rounded-lg text-sm hover:bg-red-700 transition-colors"
                                >
                                    Remove
                                </button>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            {/* Balance Button */}
            {!isSubmitted && (
                <div className="mb-6 text-center">
                    <button 
                        onClick={balanceEquation}
                        className="px-6 py-3 bg-purple-600 text-white rounded-lg text-lg font-medium hover:bg-purple-700 transition-colors"
                    >
                        Balance Equation
                    </button>
                </div>
            )}

            {/* Balanced Equation Display */}
            {showBalanced && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-2">Balanced Equation:</h4>
                    <div className="text-xl font-mono text-green-700 text-center p-3 bg-white rounded border">
                        {getEquationString()}
                    </div>
                    <div className="mt-3 text-center">
                        <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium ${
                            isEquationBalanced() 
                                ? 'bg-green-100 text-green-800' 
                                : 'bg-red-100 text-red-800'
                        }`}>
                            {isEquationBalanced() ? '✓ Balanced' : '✗ Not Balanced'}
                        </span>
                    </div>
                </div>
            )}

            {/* Solution Steps */}
            {showSolution && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Balancing Steps:</h4>
                    <div className="space-y-2">
                        {getBalancingSteps().map((step, index) => (
                            <div key={index} className="text-sm text-blue-700">{step}</div>
                        ))}
                    </div>
                </div>
            )}

            {/* Atom Count Analysis */}
            {showBalanced && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Atom Count Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <h5 className="font-medium text-gray-700 mb-2">Reactants:</h5>
                            <div className="space-y-1">
                                {Object.entries(getAtomCounts().reactantAtoms).map(([element, count]) => (
                                    <div key={element} className="text-sm text-gray-600">
                                        {element}: {count}
                                    </div>
                                ))}
                            </div>
                        </div>
                        <div>
                            <h5 className="font-medium text-gray-700 mb-2">Products:</h5>
                            <div className="space-y-1">
                                {Object.entries(getAtomCounts().productAtoms).map(([element, count]) => (
                                    <div key={element} className="text-sm text-gray-600">
                                        {element}: {count}
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Use proper chemical formulas (e.g., H₂SO₄, not H2SO4)</li>
                    <li>• Start with the most complex molecule when balancing</li>
                    <li>• Remember that coefficients must be whole numbers</li>
                    <li>• Check that all atoms are balanced on both sides</li>
                    <li>• Use the equation type to guide your balancing strategy</li>
                </ul>
            </div>
        </div>
    );
};

export default ChemicalEquationBalancer;
