import React from 'react';
import { useState } from 'react';

/**
 * Chemistry Visual Aid Components
 * Handles molecular structures, reaction mechanisms, equilibrium, etc.
 */

// Molecular Structure Component
export const MolecularStructure = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        molecule_name: 'Water',
        chemical_formula: 'H₂O',
        atoms: [
            { symbol: 'O', x: 0, y: 0, valence: 2, color: 'red' },
            { symbol: 'H', x: -1, y: 1, valence: 1, color: 'white' },
            { symbol: 'H', x: 1, y: 1, valence: 1, color: 'white' }
        ],
        bonds: [
            { from: 0, to: 1, type: 'single', length: 0.96 },
            { from: 0, to: 2, type: 'single', length: 0.96 }
        ],
        molecular_geometry: 'bent',
        units: { length: 'Å', angle: '°' }
    });

    const handleAtomChange = (index, field, value) => {
        const newData = { ...visualData };
        newData.atoms[index][field] = field === 'x' || field === 'y' || field === 'valence' ? parseFloat(value) : value;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const addAtom = () => {
        const newData = { ...visualData };
        newData.atoms.push({
            symbol: 'C',
            x: 0,
            y: 0,
            valence: 4,
            color: 'gray'
        });
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const removeAtom = (index) => {
        const newData = { ...visualData };
        newData.atoms.splice(index, 1);
        // Remove bonds involving this atom
        newData.bonds = newData.bonds.filter(bond => bond.from !== index && bond.to !== index);
        // Adjust bond indices
        newData.bonds.forEach(bond => {
            if (bond.from > index) bond.from--;
            if (bond.to > index) bond.to--;
        });
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateBondAngle = (atom1, atom2, atom3) => {
        const dx1 = atom1.x - atom2.x;
        const dy1 = atom1.y - atom2.y;
        const dx2 = atom3.x - atom2.x;
        const dy2 = atom3.y - atom2.y;
        
        const dot = dx1 * dx2 + dy1 * dy2;
        const det = dx1 * dy2 - dy1 * dx2;
        
        return Math.atan2(det, dot) * 180 / Math.PI;
    };

    const calculateBondLength = (atom1, atom2) => {
        const dx = atom1.x - atom2.x;
        const dy = atom1.y - atom2.y;
        return Math.sqrt(dx * dx + dy * dy);
    };

    return (
        <div className="molecular-structure bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Molecular Structure: {visualData.molecule_name}
            </h3>
            
            {/* Chemical Information */}
            <div className="bg-blue-50 p-4 rounded-lg mb-6">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Molecule</div>
                        <div className="text-xl font-bold text-blue-800">{visualData.molecule_name}</div>
                    </div>
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Formula</div>
                        <div className="text-xl font-bold text-blue-800">{visualData.chemical_formula}</div>
                    </div>
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Geometry</div>
                        <div className="text-xl font-bold text-blue-800">{visualData.molecular_geometry}</div>
                    </div>
                </div>
            </div>

            {/* Molecular Visualization */}
            <div className="border border-gray-300 rounded-lg p-6 bg-gray-50 mb-6">
                <div className="text-center mb-4">
                    <div className="inline-block bg-green-100 px-4 py-2 rounded-lg">
                        <span className="font-medium">Molecular Structure</span>
                    </div>
                </div>
                
                {/* Simple ASCII Molecular Diagram */}
                <div className="font-mono text-center text-sm">
                    <div className="mb-4">Molecular Layout</div>
                    {visualData.atoms.map((atom, index) => (
                        <div key={index} className="mb-2">
                            <div className={`text-${atom.color}-600 font-medium`}>
                                {atom.symbol} at ({atom.x.toFixed(1)}, {atom.y.toFixed(1)})
                            </div>
                            <div className="text-xs text-gray-500">
                                Valence: {atom.valence}
                            </div>
                        </div>
                    ))}
                    
                    <div className="mt-4 text-center">
                        <div className="text-sm text-gray-600">Bond Information</div>
                        {visualData.bonds.map((bond, index) => {
                            const atom1 = visualData.atoms[bond.from];
                            const atom2 = visualData.atoms[bond.to];
                            const length = calculateBondLength(atom1, atom2);
                            
                            return (
                                <div key={index} className="text-xs text-gray-500">
                                    {atom1.symbol}-{atom2.symbol}: {length.toFixed(2)} {visualData.units.length} ({bond.type})
                                </div>
                            );
                        })}
                    </div>
                </div>
            </div>

            {/* Molecular Properties */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <div className="bg-green-50 p-4 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-3">Bond Angles</h4>
                    <div className="space-y-2 text-sm">
                        {visualData.atoms.length >= 3 && (
                            <div>
                                <strong>H-O-H Angle:</strong> {Math.abs(calculateBondAngle(
                                    visualData.atoms[1], 
                                    visualData.atoms[0], 
                                    visualData.atoms[2]
                                )).toFixed(1)}°
                            </div>
                        )}
                    </div>
                </div>
                
                <div className="bg-purple-50 p-4 rounded-lg">
                    <h4 className="font-semibold text-purple-800 mb-3">Molecular Properties</h4>
                    <div className="space-y-2 text-sm">
                        <div><strong>Total Atoms:</strong> {visualData.atoms.length}</div>
                        <div><strong>Total Bonds:</strong> {visualData.bonds.length}</div>
                        <div><strong>Geometry:</strong> {visualData.molecular_geometry}</div>
                    </div>
                </div>
            </div>

            {/* Atom Controls */}
            {mode === 'user-interactive' && (
                <div className="mb-6">
                    <div className="flex justify-between items-center mb-4">
                        <h4 className="text-lg font-semibold text-gray-800">Atoms</h4>
                        <button
                            onClick={addAtom}
                            className="px-4 py-2 bg-blue-100 text-blue-700 rounded hover:bg-blue-200"
                        >
                            + Add Atom
                        </button>
                    </div>
                    
                    <div className="space-y-4">
                        {visualData.atoms.map((atom, index) => (
                            <div key={index} className="border border-gray-200 rounded-lg p-4">
                                <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-1">Symbol</label>
                                        <input
                                            type="text"
                                            value={atom.symbol}
                                            onChange={(e) => handleAtomChange(index, 'symbol', e.target.value)}
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-1">X Position</label>
                                        <input
                                            type="number"
                                            value={atom.x}
                                            onChange={(e) => handleAtomChange(index, 'x', e.target.value)}
                                            step="0.1"
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-1">Y Position</label>
                                        <input
                                            type="number"
                                            value={atom.y}
                                            onChange={(e) => handleAtomChange(index, 'y', e.target.value)}
                                            step="0.1"
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                        />
                                    </div>
                                    <div>
                                        <label className="block text-sm font-medium text-gray-700 mb-1">Valence</label>
                                        <input
                                            type="number"
                                            value={atom.valence}
                                            onChange={(e) => handleAtomChange(index, 'valence', e.target.value)}
                                            min="1"
                                            max="8"
                                            className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                        />
                                    </div>
                                    <div className="flex items-end">
                                        <button
                                            onClick={() => removeAtom(index)}
                                            className="w-full px-3 py-2 bg-red-100 text-red-700 rounded hover:bg-red-200"
                                        >
                                            Remove
                                        </button>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

// Chemical Reaction Component
export const ChemicalReaction = ({ data, config, mode, onVisualAidChange }) => {
    const [visualData, setVisualData] = React.useState(data || {
        reaction_name: 'Formation of Water',
        reactants: [
            { formula: 'H₂', coefficient: 2, state: 'g', moles: 2 },
            { formula: 'O₂', coefficient: 1, state: 'g', moles: 1 }
        ],
        products: [
            { formula: 'H₂O', coefficient: 2, state: 'l', moles: 2 }
        ],
        reaction_type: 'synthesis',
        enthalpy_change: -285.8,
        units: { energy: 'kJ/mol', moles: 'mol' }
    });

    const handleReactantChange = (index, field, value) => {
        const newData = { ...visualData };
        newData.reactants[index][field] = field === 'coefficient' || field === 'moles' ? parseFloat(value) : value;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const handleProductChange = (index, field, value) => {
        const newData = { ...visualData };
        newData.products[index][field] = field === 'coefficient' || field === 'moles' ? parseFloat(value) : value;
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const addReactant = () => {
        const newData = { ...visualData };
        newData.reactants.push({
            formula: 'New',
            coefficient: 1,
            state: 'g',
            moles: 1
        });
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const addProduct = () => {
        const newData = { ...visualData };
        newData.products.push({
            formula: 'New',
            coefficient: 1,
            state: 'g',
            moles: 1
        });
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const removeReactant = (index) => {
        const newData = { ...visualData };
        newData.reactants.splice(index, 1);
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const removeProduct = (index) => {
        const newData = { ...visualData };
        newData.products.splice(index, 1);
        setVisualData(newData);
        if (onVisualAidChange) onVisualAidChange(newData);
    };

    const calculateTotalMoles = (species) => {
        return species.reduce((total, item) => total + (item.coefficient * item.moles), 0);
    };

    const isBalanced = () => {
        const reactantMoles = calculateTotalMoles(visualData.reactants);
        const productMoles = calculateTotalMoles(visualData.products);
        return Math.abs(reactantMoles - productMoles) < 0.01;
    };

    return (
        <div className="chemical-reaction bg-white border border-gray-200 rounded-lg p-6">
            <h3 className="text-xl font-bold text-gray-800 mb-4 text-center">
                Chemical Reaction: {visualData.reaction_name}
            </h3>
            
            {/* Reaction Information */}
            <div className="bg-blue-50 p-4 rounded-lg mb-6">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Reaction Type</div>
                        <div className="text-xl font-bold text-blue-800">{visualData.reaction_type}</div>
                    </div>
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Enthalpy Change</div>
                        <div className={`text-xl font-bold ${visualData.enthalpy_change < 0 ? 'text-green-600' : 'text-red-600'}`}>
                            {visualData.enthalpy_change} {visualData.units.energy}
                        </div>
                        <div className="text-xs text-gray-500">
                            {visualData.enthalpy_change < 0 ? 'Exothermic' : 'Endothermic'}
                        </div>
                    </div>
                    <div>
                        <div className="text-sm text-blue-600 font-medium">Balanced</div>
                        <div className={`text-xl font-bold ${isBalanced() ? 'text-green-600' : 'text-red-600'}`}>
                            {isBalanced() ? 'Yes' : 'No'}
                        </div>
                    </div>
                </div>
            </div>

            {/* Reaction Equation */}
            <div className="border border-gray-300 rounded-lg p-6 bg-gray-50 mb-6">
                <div className="text-center mb-4">
                    <div className="inline-block bg-green-100 px-4 py-2 rounded-lg">
                        <span className="font-medium">Balanced Chemical Equation</span>
                    </div>
                </div>
                
                <div className="text-center text-lg font-mono">
                    {visualData.reactants.map((reactant, index) => (
                        <span key={index}>
                            {reactant.coefficient > 1 ? reactant.coefficient : ''}{reactant.formula}
                            <sub>{reactant.state}</sub>
                            {index < visualData.reactants.length - 1 ? ' + ' : ''}
                        </span>
                    ))}
                    <span className="mx-4 text-gray-500">→</span>
                    {visualData.products.map((product, index) => (
                        <span key={index}>
                            {product.coefficient > 1 ? product.coefficient : ''}{product.formula}
                            <sub>{product.state}</sub>
                            {index < visualData.products.length - 1 ? ' + ' : ''}
                        </span>
                    ))}
                </div>
            </div>

            {/* Reactants and Products */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                {/* Reactants */}
                <div className="bg-red-50 p-4 rounded-lg">
                    <div className="flex justify-between items-center mb-4">
                        <h4 className="font-semibold text-red-800">Reactants</h4>
                        {mode === 'user-interactive' && (
                            <button
                                onClick={addReactant}
                                className="px-3 py-1 bg-red-100 text-red-700 rounded hover:bg-red-200 text-sm"
                            >
                                + Add
                            </button>
                        )}
                    </div>
                    
                    <div className="space-y-3">
                        {visualData.reactants.map((reactant, index) => (
                            <div key={index} className="border border-red-200 rounded p-3">
                                {mode === 'user-interactive' ? (
                                    <div className="grid grid-cols-4 gap-2">
                                        <input
                                            type="text"
                                            value={reactant.formula}
                                            onChange={(e) => handleReactantChange(index, 'formula', e.target.value)}
                                            placeholder="Formula"
                                            className="px-2 py-1 border border-red-300 rounded text-sm"
                                        />
                                        <input
                                            type="number"
                                            value={reactant.coefficient}
                                            onChange={(e) => handleReactantChange(index, 'coefficient', e.target.value)}
                                            placeholder="Coeff"
                                            className="px-2 py-1 border border-red-300 rounded text-sm"
                                        />
                                        <input
                                            type="text"
                                            value={reactant.state}
                                            onChange={(e) => handleReactantChange(index, 'state', e.target.value)}
                                            placeholder="State"
                                            className="px-2 py-1 border border-red-300 rounded text-sm"
                                        />
                                        <button
                                            onClick={() => removeReactant(index)}
                                            className="px-2 py-1 bg-red-200 text-red-700 rounded hover:bg-red-300 text-xs"
                                        >
                                            ×
                                        </button>
                                    </div>
                                ) : (
                                    <div className="text-center">
                                        <div className="font-medium">{reactant.coefficient > 1 ? reactant.coefficient : ''}{reactant.formula}</div>
                                        <div className="text-xs text-gray-500">{reactant.state}</div>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                </div>

                {/* Products */}
                <div className="bg-green-50 p-4 rounded-lg">
                    <div className="flex justify-between items-center mb-4">
                        <h4 className="font-semibold text-green-800">Products</h4>
                        {mode === 'user-interactive' && (
                            <button
                                onClick={addProduct}
                                className="px-3 py-1 bg-green-100 text-green-700 rounded hover:bg-green-200 text-sm"
                            >
                                + Add
                            </button>
                        )}
                    </div>
                    
                    <div className="space-y-3">
                        {visualData.products.map((product, index) => (
                            <div key={index} className="border border-green-200 rounded p-3">
                                {mode === 'user-interactive' ? (
                                    <div className="grid grid-cols-4 gap-2">
                                        <input
                                            type="text"
                                            value={product.formula}
                                            onChange={(e) => handleProductChange(index, 'formula', e.target.value)}
                                            placeholder="Formula"
                                            className="px-2 py-1 border border-green-300 rounded text-sm"
                                        />
                                        <input
                                            type="number"
                                            value={product.coefficient}
                                            onChange={(e) => handleProductChange(index, 'coefficient', e.target.value)}
                                            placeholder="Coeff"
                                            className="px-2 py-1 border border-green-300 rounded text-sm"
                                        />
                                        <input
                                            type="text"
                                            value={product.state}
                                            onChange={(e) => handleProductChange(index, 'state', e.target.value)}
                                            placeholder="State"
                                            className="px-2 py-1 border border-green-300 rounded text-sm"
                                        />
                                        <button
                                            onClick={() => removeProduct(index)}
                                            className="px-2 py-1 bg-green-200 text-green-700 rounded hover:bg-green-300 text-xs"
                                        >
                                            ×
                                        </button>
                                    </div>
                                ) : (
                                    <div className="text-center">
                                        <div className="font-medium">{product.coefficient > 1 ? product.coefficient : ''}{product.formula}</div>
                                        <div className="text-xs text-gray-500">{product.state}</div>
                                    </div>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* Reaction Analysis */}
            <div className="bg-purple-50 p-4 rounded-lg">
                <h4 className="font-semibold text-purple-800 mb-3">Reaction Analysis</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                    <div>
                        <strong>Total Reactant Moles:</strong> {calculateTotalMoles(visualData.reactants).toFixed(2)} {visualData.units.moles}
                    </div>
                    <div>
                        <strong>Total Product Moles:</strong> {calculateTotalMoles(visualData.products).toFixed(2)} {visualData.units.moles}
                    </div>
                    <div>
                        <strong>Balance Status:</strong> {isBalanced() ? 'Balanced' : 'Unbalanced'}
                    </div>
                </div>
                {!isBalanced() && (
                    <div className="mt-3 text-center text-red-600 text-sm">
                        Reaction is not balanced. Check coefficients and ensure conservation of mass.
                    </div>
                )}
            </div>
        </div>
    );
};

// Matter Classification Simulator - CAPS Grade 10 Foundation
const MatterClassificationSimulator = ({ 
  initialData = {
    mixtures: [
      { name: "Sand and Water", type: "heterogeneous", description: "Sand particles visible in water", properties: ["particles visible", "can be filtered", "settles over time"] },
      { name: "Salt Water", type: "homogeneous", description: "Salt dissolved in water", properties: ["uniform appearance", "cannot be filtered", "does not settle"] },
      { name: "Air", type: "homogeneous", description: "Mixture of gases", properties: ["uniform composition", "transparent", "cannot be filtered"] },
      { name: "Granite", type: "heterogeneous", description: "Rock with visible crystals", properties: ["different minerals visible", "can be separated", "irregular composition"] }
    ],
    pureSubstances: [
      { name: "Copper", type: "element", symbol: "Cu", properties: ["shiny", "conducts electricity", "malleable", "reddish-brown"] },
      { name: "Water", type: "compound", formula: "H₂O", properties: ["boils at 100°C", "freezes at 0°C", "transparent", "liquid at room temperature"] },
      { name: "Oxygen", type: "element", symbol: "O₂", properties: ["colorless gas", "supports combustion", "essential for life", "diatomic molecule"] },
      { name: "Sodium Chloride", type: "compound", formula: "NaCl", properties: ["white crystalline", "salty taste", "dissolves in water", "high melting point"] }
    ],
    selectedCategory: "mixtures",
    selectedSubstance: null
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);
  const [selectedCategory, setSelectedCategory] = useState(data.selectedCategory);
  const [selectedSubstance, setSelectedSubstance] = useState(data.selectedSubstance);
  const [showProperties, setShowProperties] = useState(false);
  const [testResults, setTestResults] = useState({});

  const handleCategoryChange = (category) => {
    setSelectedCategory(category);
    setSelectedSubstance(null);
    setShowProperties(false);
    setTestResults({});
    
    const newData = { ...data, selectedCategory: category };
    setData(newData);
    onChange(newData);
  };

  const handleSubstanceSelect = (substance) => {
    setSelectedSubstance(substance);
    setShowProperties(true);
    setTestResults({});
    
    const newData = { ...data, selectedSubstance: substance };
    setData(newData);
    onChange(newData);
  };

  const runTest = (testType) => {
    if (!selectedSubstance) return;

    let result = {};
    
    switch (testType) {
      case 'filtration':
        result = {
          canFilter: selectedSubstance.type === 'heterogeneous',
          explanation: selectedSubstance.type === 'heterogeneous' 
            ? "Heterogeneous mixtures can be filtered because particles are visible and large enough"
            : "Homogeneous mixtures and pure substances cannot be filtered through normal means"
        };
        break;
      
      case 'settling':
        result = {
          willSettle: selectedSubstance.type === 'heterogeneous',
          explanation: selectedSubstance.type === 'heterogeneous'
            ? "Heterogeneous mixtures will settle over time due to different particle densities"
            : "Homogeneous mixtures and pure substances maintain uniform composition"
        };
        break;
      
      case 'melting':
        result = {
          hasFixedMeltingPoint: selectedSubstance.type === 'pure',
          explanation: selectedSubstance.type === 'pure'
            ? "Pure substances have fixed, sharp melting points"
            : "Mixtures have variable melting points over a range of temperatures"
        };
        break;
      
      case 'conductivity':
        result = {
          conducts: selectedSubstance.properties?.includes('conducts electricity'),
          explanation: selectedSubstance.properties?.includes('conducts electricity')
            ? "This substance conducts electricity due to its metallic or ionic nature"
            : "This substance does not conduct electricity (insulator)"
        };
        break;
    }

    setTestResults(prev => ({ ...prev, [testType]: result }));
  };

  const getSubstanceType = (substance) => {
    if (substance.type === 'element' || substance.type === 'compound') return 'pure';
    return substance.type;
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-4xl mx-auto">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Matter Classification Simulator</h2>
        <p className="text-gray-600">Explore the properties and classification of matter - CAPS Grade 10 Foundation</p>
      </div>

      {/* Category Selection */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        <button
          onClick={() => handleCategoryChange('mixtures')}
          className={`p-4 rounded-lg border-2 transition-all ${
            selectedCategory === 'mixtures'
              ? 'border-blue-500 bg-blue-50 text-blue-700'
              : 'border-gray-200 hover:border-gray-300'
          }`}
        >
          <h3 className="font-semibold text-lg">Mixtures</h3>
          <p className="text-sm text-gray-600">Heterogeneous and homogeneous combinations</p>
        </button>
        
        <button
          onClick={() => handleCategoryChange('pureSubstances')}
          className={`p-4 rounded-lg border-2 transition-all ${
            selectedCategory === 'pureSubstances'
              ? 'border-blue-500 bg-blue-50 text-blue-700'
              : 'border-gray-200 hover:border-gray-300'
          }`}
        >
          <h3 className="font-semibold text-lg">Pure Substances</h3>
          <p className="text-sm text-gray-600">Elements and compounds</p>
        </button>
      </div>

      {/* Substance Grid */}
      <div className="grid grid-cols-2 gap-4 mb-6">
        {data[selectedCategory].map((substance, index) => (
          <div
            key={index}
            onClick={() => handleSubstanceSelect(substance)}
            className={`p-4 rounded-lg border-2 cursor-pointer transition-all ${
              selectedSubstance?.name === substance.name
                ? 'border-green-500 bg-green-50'
                : 'border-gray-200 hover:border-gray-300 hover:bg-gray-50'
            }`}
          >
            <h4 className="font-semibold text-lg mb-2">{substance.name}</h4>
            <div className="flex items-center gap-2 mb-2">
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                substance.type === 'heterogeneous' ? 'bg-orange-100 text-orange-800' :
                substance.type === 'homogeneous' ? 'bg-blue-100 text-blue-800' :
                substance.type === 'element' ? 'bg-purple-100 text-purple-800' :
                'bg-green-100 text-green-800'
              }`}>
                {substance.type}
              </span>
              {substance.symbol && (
                <span className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs font-mono">
                  {substance.symbol}
                </span>
              )}
              {substance.formula && (
                <span className="px-2 py-1 bg-gray-100 text-gray-700 rounded text-xs font-mono">
                  {substance.formula}
                </span>
              )}
            </div>
            <p className="text-sm text-gray-600">{substance.description}</p>
          </div>
        ))}
      </div>

      {/* Properties and Tests */}
      {selectedSubstance && (
        <div className="border-t pt-6">
          <h3 className="text-xl font-semibold mb-4">Properties & Analysis</h3>
          
          {/* Properties */}
          <div className="mb-6">
            <h4 className="font-medium text-gray-700 mb-3">Key Properties:</h4>
            <div className="flex flex-wrap gap-2">
              {selectedSubstance.properties.map((prop, index) => (
                <span key={index} className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                  {prop}
                </span>
              ))}
            </div>
          </div>

          {/* Tests */}
          <div className="mb-6">
            <h4 className="font-medium text-gray-700 mb-3">Laboratory Tests:</h4>
            <div className="grid grid-cols-2 gap-4">
              <button
                onClick={() => runTest('filtration')}
                className="p-3 bg-blue-100 hover:bg-blue-200 text-blue-800 rounded-lg transition-colors"
              >
                Test Filtration
              </button>
              <button
                onClick={() => runTest('settling')}
                className="p-3 bg-green-100 hover:bg-green-200 text-green-800 rounded-lg transition-colors"
              >
                Test Settling
              </button>
              <button
                onClick={() => runTest('melting')}
                className="p-3 bg-purple-100 hover:bg-purple-200 text-purple-800 rounded-lg transition-colors"
              >
                Test Melting Point
              </button>
              <button
                onClick={() => runTest('conductivity')}
                className="p-3 bg-orange-100 hover:bg-orange-200 text-orange-800 rounded-lg transition-colors"
              >
                Test Conductivity
              </button>
            </div>
          </div>

          {/* Test Results */}
          {Object.keys(testResults).length > 0 && (
            <div className="bg-gray-50 rounded-lg p-4">
              <h4 className="font-medium text-gray-700 mb-3">Test Results:</h4>
              <div className="space-y-3">
                {Object.entries(testResults).map(([testType, result]) => (
                  <div key={testType} className="border-l-4 border-blue-500 pl-4">
                    <h5 className="font-medium capitalize text-gray-700">{testType} Test</h5>
                    <p className={`text-sm ${result.canFilter !== undefined ? (result.canFilter ? 'text-green-600' : 'text-red-600') : 
                                     result.willSettle !== undefined ? (result.willSettle ? 'text-green-600' : 'text-red-600') :
                                     result.hasFixedMeltingPoint !== undefined ? (result.hasFixedMeltingPoint ? 'text-green-600' : 'text-red-600') :
                                     result.conducts !== undefined ? (result.conducts ? 'text-green-600' : 'text-red-600') : 'text-gray-600'}`}>
                      {result.explanation}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Classification Summary */}
          <div className="mt-6 p-4 bg-blue-50 rounded-lg">
            <h4 className="font-medium text-blue-800 mb-2">Classification Summary</h4>
            <div className="text-sm text-blue-700">
              <p><strong>Name:</strong> {selectedSubstance.name}</p>
              <p><strong>Type:</strong> {selectedSubstance.type}</p>
              <p><strong>Category:</strong> {getSubstanceType(selectedSubstance)}</p>
              <p><strong>Description:</strong> {selectedSubstance.description}</p>
            </div>
          </div>
        </div>
      )}

      {/* CAPS Learning Objectives */}
      <div className="mt-8 p-4 bg-yellow-50 rounded-lg">
        <h4 className="font-medium text-yellow-800 mb-2">CAPS Grade 10 Learning Objectives</h4>
        <ul className="text-sm text-yellow-700 space-y-1">
          <li>• Revise matter and classification from Grade 9</li>
          <li>• Understand heterogeneous vs homogeneous mixtures</li>
          <li>• Distinguish between pure substances, compounds, and elements</li>
          <li>• Use macroscopic and sub-microscopic representations</li>
          <li>• Apply scientific classification criteria</li>
        </ul>
      </div>
    </div>
  );
};

// States of Matter Visualizer - CAPS Grade 10 KMT Foundation
const StatesOfMatterVisualizer = ({ 
  initialData = {
    selectedState: 'solid',
    temperature: 25,
    pressure: 1.0,
    particleCount: 50,
    showEnergy: true,
    showForces: true,
    selectedSubstance: 'water'
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);
  const [isAnimating, setIsAnimating] = useState(true);
  const [animationSpeed, setAnimationSpeed] = useState(1);

  const substances = {
    water: { 
      name: 'Water (H₂O)', 
      meltingPoint: 0, 
      boilingPoint: 100,
      color: '#3B82F6',
      particleSize: 8
    },
    carbon: { 
      name: 'Carbon (C)', 
      meltingPoint: 3550, 
      boilingPoint: 4027,
      color: '#374151',
      particleSize: 6
    },
    oxygen: { 
      name: 'Oxygen (O₂)', 
      meltingPoint: -218, 
      boilingPoint: -183,
      color: '#10B981',
      particleSize: 7
    },
    iron: { 
      name: 'Iron (Fe)', 
      meltingPoint: 1538, 
      boilingPoint: 2862,
      color: '#DC2626',
      particleSize: 9
    }
  };

  const handleStateChange = (state) => {
    const newData = { ...data, selectedState: state };
    setData(newData);
    onChange(newData);
  };

  const handleTemperatureChange = (temp) => {
    const newData = { ...data, temperature: temp };
    setData(newData);
    onChange(newData);
  };

  const handleSubstanceChange = (substance) => {
    const newData = { ...data, selectedSubstance: substance };
    setData(newData);
    onChange(newData);
  };

  const getStateProperties = (state, temp) => {
    const substance = substances[data.selectedSubstance];
    
    switch (state) {
      case 'solid':
        return {
          particleArrangement: 'Ordered, fixed positions',
          particleMotion: 'Vibrational only',
          particleSpacing: 'Close, regular',
          compressibility: 'Very low',
          shape: 'Fixed, definite',
          volume: 'Fixed, definite',
          energy: 'Lowest',
          description: 'Particles are tightly packed in a regular pattern, vibrating in fixed positions'
        };
      case 'liquid':
        return {
          particleArrangement: 'Random, close together',
          particleMotion: 'Sliding, flowing',
          particleSpacing: 'Close, irregular',
          compressibility: 'Low',
          shape: 'Takes container shape',
          volume: 'Fixed, definite',
          energy: 'Medium',
          description: 'Particles are close together but can move past each other, taking the shape of their container'
        };
      case 'gas':
        return {
          particleArrangement: 'Random, far apart',
          particleMotion: 'Fast, random',
          particleSpacing: 'Far apart, irregular',
          compressibility: 'High',
          shape: 'Takes container shape',
          volume: 'Takes container volume',
          energy: 'Highest',
          description: 'Particles are far apart and move rapidly in all directions, filling their container completely'
        };
      default:
        return {};
    }
  };

  const getStateFromTemperature = (temp) => {
    const substance = substances[data.selectedSubstance];
    if (temp < substance.meltingPoint) return 'solid';
    if (temp < substance.boilingPoint) return 'liquid';
    return 'gas';
  };

  const currentState = getStateFromTemperature(data.temperature);
  const properties = getStateProperties(currentState, data.temperature);

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-6xl mx-auto">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">States of Matter Visualizer</h2>
        <p className="text-gray-600">Explore Kinetic Molecular Theory and state changes - CAPS Grade 10 Foundation</p>
      </div>

      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        {/* Substance Selection */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Substance</h3>
          <select
            value={data.selectedSubstance}
            onChange={(e) => handleSubstanceChange(e.target.value)}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            {Object.keys(substances).map(substance => (
              <option key={substance} value={substance}>
                {substances[substance].name}
              </option>
            ))}
          </select>
          <div className="mt-2 text-sm text-gray-600">
            <p>Melting: {substances[data.selectedSubstance].meltingPoint}°C</p>
            <p>Boiling: {substances[data.selectedSubstance].boilingPoint}°C</p>
          </div>
        </div>

        {/* Temperature Control */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Temperature Control</h3>
          <div className="flex items-center gap-2 mb-2">
            <span className="text-sm text-gray-600">-200°C</span>
            <input
              type="range"
              min="-200"
              max="4000"
              value={data.temperature}
              onChange={(e) => handleTemperatureChange(parseInt(e.target.value))}
              className="flex-1"
            />
            <span className="text-sm text-gray-600">4000°C</span>
          </div>
          <div className="text-center">
            <span className="text-2xl font-bold text-blue-600">{data.temperature}°C</span>
          </div>
          <div className="text-center mt-1">
            <span className={`px-2 py-1 rounded-full text-xs font-medium ${
              currentState === 'solid' ? 'bg-blue-100 text-blue-800' :
              currentState === 'liquid' ? 'bg-green-100 text-green-800' :
              'bg-red-100 text-red-800'
            }`}>
              {currentState.toUpperCase()}
            </span>
          </div>
        </div>

        {/* Animation Controls */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Animation</h3>
          <div className="flex items-center gap-2 mb-3">
            <input
              type="checkbox"
              checked={isAnimating}
              onChange={(e) => setIsAnimating(e.target.checked)}
              className="w-4 h-4"
            />
            <label className="text-sm text-gray-700">Animate</label>
          </div>
          <div className="mb-3">
            <label className="text-sm text-gray-700 block mb-1">Speed</label>
            <input
              type="range"
              min="0.1"
              max="3"
              step="0.1"
              value={animationSpeed}
              onChange={(e) => setAnimationSpeed(parseFloat(e.target.value))}
              className="w-full"
            />
          </div>
          <div className="flex gap-2">
            <input
              type="checkbox"
              checked={data.showEnergy}
              onChange={(e) => setData({...data, showEnergy: e.target.checked})}
              className="w-4 h-4"
            />
            <label className="text-sm text-gray-700">Show Energy</label>
          </div>
          <div className="flex gap-2">
            <input
              type="checkbox"
              checked={data.showForces}
              onChange={(e) => setData({...data, showForces: e.target.checked})}
              className="w-4 h-4"
            />
            <label className="text-sm text-gray-700">Show Forces</label>
          </div>
        </div>
      </div>

      {/* Main Visualization */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        {/* Particle Animation */}
        <div className="bg-gray-900 rounded-lg p-4 h-80 relative overflow-hidden">
          <div className="text-white text-center mb-4">
            <h3 className="font-semibold">Particle Behavior</h3>
            <p className="text-sm text-gray-300">{properties.description}</p>
          </div>
          
          {/* Particle Container */}
          <div className="relative w-full h-48 bg-gray-800 rounded border border-gray-600">
            {/* Particles */}
            {Array.from({ length: data.particleCount }, (_, i) => {
              const size = substances[data.selectedSubstance].particleSize;
              const baseX = (i * 20) % 280 + 20;
              const baseY = Math.floor(i / 10) * 30 + 30;
              
              // Add some randomness based on state
              const randomX = currentState === 'gas' ? Math.random() * 20 - 10 : 
                             currentState === 'liquid' ? Math.random() * 10 - 5 : 0;
              const randomY = currentState === 'gas' ? Math.random() * 20 - 10 : 
                             currentState === 'liquid' ? Math.random() * 10 - 5 : 0;
              
              return (
                <div
                  key={i}
                  className={`absolute rounded-full ${isAnimating ? 'animate-pulse' : ''}`}
                  style={{
                    left: baseX + randomX,
                    top: baseY + randomY,
                    width: size,
                    height: size,
                    backgroundColor: substances[data.selectedSubstance].color,
                    animationDuration: `${2 / animationSpeed}s`,
                    opacity: currentState === 'gas' ? 0.7 : 1
                  }}
                />
              );
            })}
            
            {/* State Indicators */}
            <div className="absolute top-2 right-2 text-white text-xs">
              <div className="bg-gray-700 px-2 py-1 rounded">
                State: {currentState}
              </div>
            </div>
          </div>
        </div>

        {/* Properties Panel */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-4">State Properties</h3>
          <div className="space-y-3">
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Arrangement:</span>
              <span className="text-sm text-gray-800">{properties.particleArrangement}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Motion:</span>
              <span className="text-sm text-gray-800">{properties.particleMotion}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Spacing:</span>
              <span className="text-sm text-gray-800">{properties.particleSpacing}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Compressibility:</span>
              <span className="text-sm text-gray-800">{properties.compressibility}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Shape:</span>
              <span className="text-sm text-gray-800">{properties.shape}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Volume:</span>
              <span className="text-sm text-gray-800">{properties.volume}</span>
            </div>
            <div className="grid grid-cols-2 gap-2">
              <span className="text-sm font-medium text-gray-600">Energy:</span>
              <span className="text-sm text-gray-800">{properties.energy}</span>
            </div>
          </div>
        </div>
      </div>

      {/* State Change Examples */}
      <div className="bg-blue-50 p-4 rounded-lg mb-6">
        <h3 className="font-semibold text-blue-800 mb-3">State Change Examples</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="text-center">
            <div className="text-2xl mb-2">❄️</div>
            <h4 className="font-medium text-blue-700">Freezing</h4>
            <p className="text-sm text-blue-600">Liquid → Solid</p>
            <p className="text-xs text-blue-500">Energy released</p>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">🔥</div>
            <h4 className="font-medium text-blue-700">Melting</h4>
            <p className="text-sm text-blue-600">Solid → Liquid</p>
            <p className="text-xs text-blue-500">Energy absorbed</p>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">💨</div>
            <h4 className="font-medium text-blue-700">Evaporation</h4>
            <p className="text-sm text-blue-600">Liquid → Gas</p>
            <p className="text-xs text-blue-500">Energy absorbed</p>
          </div>
        </div>
      </div>

      {/* CAPS Learning Objectives */}
      <div className="bg-yellow-50 p-4 rounded-lg">
        <h4 className="font-medium text-yellow-800 mb-2">CAPS Grade 10 Learning Objectives</h4>
        <ul className="text-sm text-yellow-700 space-y-1">
          <li>• Verify the particulate nature of matter</li>
          <li>• List and characterize the three states of matter</li>
          <li>• Define freezing point, melting point, and boiling point</li>
          <li>• Describe states according to Kinetic Molecular Theory</li>
          <li>• Demonstrate changes of state</li>
          <li>• Use macroscopic and sub-microscopic representations</li>
        </ul>
      </div>
    </div>
  );
};

// Atomic Structure Builder - CAPS Grade 10 Foundation
const AtomicStructureBuilder = ({ 
  initialData = {
    selectedElement: 'carbon',
    showElectronShells: true,
    showNucleus: true,
    showOrbitals: false,
    showQuantumNumbers: false,
    selectedModel: 'bohr'
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);
  const [showInfo, setShowInfo] = useState(false);

  const elements = {
    hydrogen: { 
      name: 'Hydrogen', 
      symbol: 'H', 
      atomicNumber: 1, 
      massNumber: 1, 
      protons: 1, 
      neutrons: 0, 
      electrons: 1,
      electronConfiguration: '1s¹',
      shells: [1],
      color: '#FF6B6B'
    },
    helium: { 
      name: 'Helium', 
      symbol: 'He', 
      atomicNumber: 2, 
      massNumber: 4, 
      protons: 2, 
      neutrons: 2, 
      electrons: 2,
      electronConfiguration: '1s²',
      shells: [2],
      color: '#4ECDC4'
    },
    carbon: { 
      name: 'Carbon', 
      symbol: 'C', 
      atomicNumber: 6, 
      massNumber: 12, 
      protons: 6, 
      neutrons: 6, 
      electrons: 6,
      electronConfiguration: '1s² 2s² 2p²',
      shells: [2, 4],
      color: '#45B7D1'
    },
    nitrogen: { 
      name: 'Nitrogen', 
      symbol: 'N', 
      atomicNumber: 7, 
      massNumber: 14, 
      protons: 7, 
      neutrons: 7, 
      electrons: 7,
      electronConfiguration: '1s² 2s² 2p³',
      shells: [2, 5],
      color: '#96CEB4'
    },
    oxygen: { 
      name: 'Oxygen', 
      symbol: 'O', 
      atomicNumber: 8, 
      massNumber: 16, 
      protons: 8, 
      neutrons: 8, 
      electrons: 8,
      electronConfiguration: '1s² 2s² 2p⁴',
      shells: [2, 6],
      color: '#FFEAA7'
    },
    neon: { 
      name: 'Neon', 
      symbol: 'Ne', 
      atomicNumber: 10, 
      massNumber: 20, 
      protons: 10, 
      neutrons: 10, 
      electrons: 10,
      electronConfiguration: '1s² 2s² 2p⁶',
      shells: [2, 8],
      color: '#DDA0DD'
    },
    sodium: { 
      name: 'Sodium', 
      symbol: 'Na', 
      atomicNumber: 11, 
      massNumber: 23, 
      protons: 11, 
      neutrons: 12, 
      electrons: 11,
      electronConfiguration: '1s² 2s² 2p⁶ 3s¹',
      shells: [2, 8, 1],
      color: '#FFB347'
    },
    magnesium: { 
      name: 'Magnesium', 
      symbol: 'Mg', 
      atomicNumber: 12, 
      massNumber: 24, 
      protons: 12, 
      neutrons: 12, 
      electrons: 12,
      electronConfiguration: '1s² 2s² 2p⁶ 3s²',
      shells: [2, 8, 2],
      color: '#98D8C8'
    }
  };

  const handleElementChange = (element) => {
    const newData = { ...data, selectedElement: element };
    setData(newData);
    onChange(newData);
  };

  const handleModelChange = (model) => {
    const newData = { ...data, selectedModel: model };
    setData(newData);
    onChange(newData);
  };

  const selectedElement = elements[data.selectedElement];

  const renderBohrModel = () => (
    <div className="relative w-64 h-64 mx-auto">
      {/* Nucleus */}
      {data.showNucleus && (
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <div className="w-16 h-16 bg-red-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
            {selectedElement.symbol}
          </div>
          <div className="text-center text-xs mt-1">
            <div>p⁺: {selectedElement.protons}</div>
            <div>n⁰: {selectedElement.neutrons}</div>
          </div>
        </div>
      )}

      {/* Electron Shells */}
      {data.showElectronShells && selectedElement.shells.map((electrons, shellIndex) => {
        const radius = (shellIndex + 1) * 40;
        const shellNumber = shellIndex + 1;
        
        return (
          <div key={shellIndex} className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            {/* Shell Circle */}
            <div 
              className="absolute border-2 border-gray-300 rounded-full"
              style={{
                width: radius * 2,
                height: radius * 2,
                marginLeft: -radius,
                marginTop: -radius
              }}
            />
            
            {/* Shell Label */}
            <div 
              className="absolute text-xs text-gray-500 font-medium"
              style={{
                left: radius + 5,
                top: -10
              }}
            >
              n={shellNumber}
            </div>

            {/* Electrons */}
            {Array.from({ length: electrons }, (_, electronIndex) => {
              const angle = (electronIndex * 360) / electrons;
              const x = Math.cos((angle - 90) * Math.PI / 180) * radius;
              const y = Math.sin((angle - 90) * Math.PI / 180) * radius;
              
              return (
                <div
                  key={electronIndex}
                  className="absolute w-3 h-3 bg-blue-500 rounded-full"
                  style={{
                    left: x + radius - 1.5,
                    top: y + radius - 1.5
                  }}
                />
              );
            })}
          </div>
        );
      })}
    </div>
  );

  const renderQuantumModel = () => (
    <div className="relative w-64 h-64 mx-auto">
      {/* Nucleus */}
      {data.showNucleus && (
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <div className="w-16 h-16 bg-red-500 rounded-full flex items-center justify-center text-white font-bold text-sm">
            {selectedElement.symbol}
          </div>
        </div>
      )}

      {/* Orbital Shapes */}
      {data.showOrbitals && (
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          {/* 1s orbital (spherical) */}
          <div className="w-32 h-32 border-2 border-blue-300 rounded-full opacity-50" />
          
          {/* 2s orbital (larger spherical) */}
          <div className="w-48 h-48 border-2 border-green-300 rounded-full opacity-30" />
          
          {/* 2p orbitals (dumbbell shaped) */}
          <div className="w-40 h-16 border-2 border-purple-300 rounded-full opacity-40 transform rotate-0" />
          <div className="w-40 h-16 border-2 border-purple-300 rounded-full opacity-40 transform rotate-90" />
        </div>
      )}
    </div>
  );

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 max-w-6xl mx-auto">
      <div className="text-center mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Atomic Structure Builder</h2>
        <p className="text-gray-600">Explore atomic structure and electron configurations - CAPS Grade 10 Foundation</p>
      </div>

      {/* Controls */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
        {/* Element Selection */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Select Element</h3>
          <select
            value={data.selectedElement}
            onChange={(e) => handleElementChange(e.target.value)}
            className="w-full p-2 border border-gray-300 rounded-md"
          >
            {Object.keys(elements).map(element => (
              <option key={element} value={element}>
                {elements[element].name} ({elements[element].symbol})
              </option>
            ))}
          </select>
          
          <div className="mt-3 text-sm text-gray-600">
            <p><strong>Atomic Number:</strong> {selectedElement.atomicNumber}</p>
            <p><strong>Mass Number:</strong> {selectedElement.massNumber}</p>
            <p><strong>Protons:</strong> {selectedElement.protons}</p>
            <p><strong>Neutrons:</strong> {selectedElement.neutrons}</p>
            <p><strong>Electrons:</strong> {selectedElement.electrons}</p>
          </div>
        </div>

        {/* Model Selection */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Atomic Model</h3>
          <div className="space-y-2">
            <label className="flex items-center">
              <input
                type="radio"
                name="model"
                value="bohr"
                checked={data.selectedModel === 'bohr'}
                onChange={(e) => handleModelChange(e.target.value)}
                className="mr-2"
              />
              Bohr Model
            </label>
            <label className="flex items-center">
              <input
                type="radio"
                name="model"
                value="quantum"
                checked={data.selectedModel === 'quantum'}
                onChange={(e) => handleModelChange(e.target.value)}
                className="mr-2"
              />
              Quantum Model
            </label>
          </div>
          
          <div className="mt-3 space-y-2">
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={data.showNucleus}
                onChange={(e) => setData({...data, showNucleus: e.target.checked})}
                className="mr-2"
              />
              Show Nucleus
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={data.showElectronShells}
                onChange={(e) => setData({...data, showElectronShells: e.target.checked})}
                className="mr-2"
              />
              Show Electron Shells
            </label>
            <label className="flex items-center">
              <input
                type="checkbox"
                checked={data.showOrbitals}
                onChange={(e) => setData({...data, showOrbitals: e.target.checked})}
                className="mr-2"
              />
              Show Orbitals
            </label>
          </div>
        </div>

        {/* Element Info */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-3">Element Information</h3>
          <div className="text-sm text-gray-600 space-y-1">
            <p><strong>Name:</strong> {selectedElement.name}</p>
            <p><strong>Symbol:</strong> {selectedElement.symbol}</p>
            <p><strong>Electron Configuration:</strong></p>
            <p className="font-mono text-xs bg-gray-100 p-1 rounded">
              {selectedElement.electronConfiguration}
            </p>
            <p><strong>Shell Structure:</strong></p>
            <p className="font-mono text-xs bg-gray-100 p-1 rounded">
              {selectedElement.shells.join(', ')}
            </p>
          </div>
        </div>
      </div>

      {/* Main Visualization */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        {/* Atomic Model */}
        <div className="bg-gray-900 rounded-lg p-4 h-80 flex items-center justify-center">
          {data.selectedModel === 'bohr' ? renderBohrModel() : renderQuantumModel()}
        </div>

        {/* Electron Configuration Details */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-semibold text-gray-800 mb-4">Electron Configuration Details</h3>
          
          {/* Shell Breakdown */}
          <div className="space-y-3">
            {selectedElement.shells.map((electrons, shellIndex) => (
              <div key={shellIndex} className="border-l-4 border-blue-500 pl-4">
                <h4 className="font-medium text-gray-700">Shell {shellIndex + 1} (n = {shellIndex + 1})</h4>
                <div className="text-sm text-gray-600">
                  <p>Maximum capacity: {2 * Math.pow(shellIndex + 1, 2)} electrons</p>
                  <p>Current electrons: {electrons}</p>
                  <p>Orbital type: {shellIndex === 0 ? 's' : shellIndex === 1 ? 's, p' : 's, p, d'}</p>
                </div>
                
                {/* Electron Representation */}
                <div className="flex gap-1 mt-2">
                  {Array.from({ length: electrons }, (_, i) => (
                    <div key={i} className="w-3 h-3 bg-blue-500 rounded-full" />
                  ))}
                  {Array.from({ length: 2 * Math.pow(shellIndex + 1, 2) - electrons }, (_, i) => (
                    <div key={`empty-${i}`} className="w-3 h-3 bg-gray-200 rounded-full border border-gray-300" />
                  ))}
                </div>
              </div>
            ))}
          </div>

          {/* Quantum Numbers */}
          {data.showQuantumNumbers && (
            <div className="mt-4 p-3 bg-blue-50 rounded">
              <h4 className="font-medium text-blue-800 mb-2">Quantum Numbers</h4>
              <div className="text-sm text-blue-700 space-y-1">
                <p><strong>Principal (n):</strong> Shell number</p>
                <p><strong>Angular (l):</strong> Orbital shape (s=0, p=1, d=2)</p>
                <p><strong>Magnetic (m):</strong> Orbital orientation</p>
                <p><strong>Spin (s):</strong> Electron spin (±½)</p>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Historical Development */}
      <div className="bg-blue-50 p-4 rounded-lg mb-6">
        <h3 className="font-semibold text-blue-800 mb-3">Historical Development of Atomic Models</h3>
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 text-sm">
          <div className="text-center">
            <div className="text-2xl mb-2">⚫</div>
            <h4 className="font-medium text-blue-700">Dalton (1803)</h4>
            <p className="text-blue-600">Solid spheres</p>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">🍇</div>
            <h4 className="font-medium text-blue-700">Thomson (1897)</h4>
            <p className="text-blue-600">Plum pudding model</p>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">☀️</div>
            <h4 className="font-medium text-blue-700">Rutherford (1911)</h4>
            <p className="text-blue-600">Nuclear model</p>
          </div>
          <div className="text-center">
            <div className="text-2xl mb-2">🌍</div>
            <h4 className="font-medium text-blue-700">Bohr (1913)</h4>
            <p className="text-blue-600">Planetary model</p>
          </div>
        </div>
      </div>

      {/* CAPS Learning Objectives */}
      <div className="bg-yellow-50 p-4 rounded-lg">
        <h4 className="font-medium text-yellow-800 mb-2">CAPS Grade 10 Learning Objectives</h4>
        <ul className="text-sm text-yellow-700 space-y-1">
          <li>• Understand models of the atom through history</li>
          <li>• Describe atomic structure in terms of protons, neutrons, and electrons</li>
          <li>• Calculate atomic mass and diameter</li>
          <li>• Understand isotopes and relative atomic mass</li>
          <li>• Give electron configuration up to Z=20</li>
          <li>• Describe atomic orbitals and shapes</li>
          <li>• Apply Hund's rule and Pauli's Exclusion Principle</li>
        </ul>
      </div>
    </div>
  );
};

// Isotope Calculator Component
const IsotopeCalculator = ({
  initialData = {
    element: 'Carbon',
    atomicNumber: 6,
    isotopes: [
      { massNumber: 12, abundance: 98.9, mass: 12.0000 },
      { massNumber: 13, abundance: 1.1, mass: 13.0034 },
      { massNumber: 14, abundance: 0.0, mass: 14.0032 }
    ],
    showCalculations: true,
    showGraph: true,
    selectedIsotope: 0
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const calculateRelativeAtomicMass = () => {
    let totalMass = 0;
    let totalAbundance = 0;
    
    data.isotopes.forEach(isotope => {
      totalMass += (isotope.mass * isotope.abundance) / 100;
      totalAbundance += isotope.abundance;
    });
    
    return totalAbundance > 0 ? totalMass : 0;
  };

  const addIsotope = () => {
    const newIsotope = {
      massNumber: data.isotopes.length + 12,
      abundance: 0,
      mass: 0
    };
    const newData = { ...data, isotopes: [...data.isotopes, newIsotope] };
    handleDataChange(newData);
  };

  const removeIsotope = (index) => {
    const newIsotopes = data.isotopes.filter((_, i) => i !== index);
    const newData = { ...data, isotopes: newIsotopes };
    handleDataChange(newData);
  };

  const updateIsotope = (index, field, value) => {
    const newIsotopes = [...data.isotopes];
    newIsotopes[index][field] = parseFloat(value) || 0;
    const newData = { ...data, isotopes: newIsotopes };
    handleDataChange(newData);
  };

  const relativeAtomicMass = calculateRelativeAtomicMass();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Isotope Calculator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Element</label>
          <input
            type="text"
            value={data.element}
            onChange={(e) => handleDataChange({ ...data, element: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Atomic Number</label>
          <input
            type="number"
            value={data.atomicNumber}
            onChange={(e) => handleDataChange({ ...data, atomicNumber: parseInt(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            min="1"
          />
        </div>
      </div>

      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <h4 className="font-medium">Isotopes</h4>
          <button
            onClick={addIsotope}
            className="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600"
          >
            Add Isotope
          </button>
        </div>
        
        <div className="space-y-2">
          {data.isotopes.map((isotope, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="number"
                value={isotope.massNumber}
                onChange={(e) => updateIsotope(index, 'massNumber', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="A"
                min="1"
              />
              <span className="text-sm text-gray-600">amu</span>
              <input
                type="number"
                value={isotope.abundance}
                onChange={(e) => updateIsotope(index, 'abundance', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="%"
                step="0.1"
                min="0"
                max="100"
              />
              <span className="text-sm text-gray-600">%</span>
              <input
                type="number"
                value={isotope.mass}
                onChange={(e) => updateIsotope(index, 'mass', e.target.value)}
                className="w-24 px-2 py-1 border rounded"
                placeholder="Mass"
                step="0.0001"
                min="0"
              />
              <span className="text-sm text-gray-600">u</span>
              <button
                onClick={() => removeIsotope(index)}
                className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showCalculations}
            onChange={(e) => handleDataChange({ ...data, showCalculations: e.target.checked })}
            className="mr-2"
          />
          Show Calculations
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showGraph}
            onChange={(e) => handleDataChange({ ...data, showGraph: e.target.checked })}
            className="mr-2"
          />
          Show Abundance Graph
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[300px]">
        <div className="text-center text-gray-600 mb-4">
          Isotope Analysis for {data.element}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Relative Atomic Mass</div>
            <div className="text-lg font-bold text-blue-800">
              {relativeAtomicMass.toFixed(4)} u
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Number of Isotopes</div>
            <div className="text-lg font-bold text-green-800">
              {data.isotopes.length}
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Total Abundance</div>
            <div className="text-lg font-bold text-purple-800">
              {data.isotopes.reduce((sum, iso) => sum + iso.abundance, 0).toFixed(1)}%
            </div>
          </div>
        </div>
        
        {data.showCalculations && (
          <div className="text-sm text-gray-600 space-y-2">
            <p><strong>Calculation Method:</strong></p>
            <p>Relative Atomic Mass = Σ(mass × abundance%) / 100</p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">Step-by-step calculation:</p>
              {data.isotopes.map((isotope, index) => (
                <p key={index} className="text-xs">
                  {isotope.massNumber}×{isotope.mass} × {isotope.abundance}% = {(isotope.mass * isotope.abundance / 100).toFixed(4)} u
                </p>
              ))}
              <p className="font-medium mt-2">
                Total: {relativeAtomicMass.toFixed(4)} u
              </p>
            </div>
          </div>
        )}
        
        {data.showGraph && (
          <div className="mt-4">
            <h4 className="font-medium text-gray-700 mb-2">Abundance Distribution</h4>
            <div className="flex items-end space-x-1 h-32 bg-gray-100 p-2 rounded">
              {data.isotopes.map((isotope, index) => (
                <div key={index} className="flex-1 flex flex-col items-center">
                  <div
                    className="bg-blue-500 w-full rounded-t"
                    style={{ height: `${isotope.abundance * 0.3}%` }}
                  ></div>
                  <div className="text-xs text-gray-600 mt-1">{isotope.massNumber}</div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Gas Law Simulator Component
const GasLawSimulator = ({
  initialData = {
    lawType: 'boyle',
    pressure: 1.0,
    volume: 1.0,
    temperature: 273,
    moles: 1.0,
    showGraph: true,
    showParticles: true,
    isAnimating: false,
    units: { pressure: 'atm', volume: 'L', temperature: 'K', moles: 'mol' }
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetSimulation = () => {
    handleDataChange({ ...data, pressure: 1.0, volume: 1.0, temperature: 273, moles: 1.0, isAnimating: false });
  };

  const calculateGasLaw = () => {
    const R = 0.0821; // L·atm/(mol·K)
    
    switch (data.lawType) {
      case 'boyle':
        // P₁V₁ = P₂V₂
        return { pressure: data.pressure, volume: data.volume, constant: data.pressure * data.volume };
      case 'charles':
        // V₁/T₁ = V₂/T₂
        return { volume: data.volume, temperature: data.temperature, constant: data.volume / data.temperature };
      case 'gay-lussac':
        // P₁/T₁ = P₂/T₂
        return { pressure: data.pressure, temperature: data.temperature, constant: data.pressure / data.temperature };
      case 'combined':
        // P₁V₁/T₁ = P₂V₂/T₂
        return { pressure: data.pressure, volume: data.volume, temperature: data.temperature, constant: (data.pressure * data.volume) / data.temperature };
      case 'ideal':
        // PV = nRT
        return { pressure: data.pressure, volume: data.volume, temperature: data.temperature, moles: data.moles, constant: data.pressure * data.volume / (data.moles * data.temperature) };
      default:
        return {};
    }
  };

  const gasLawResult = calculateGasLaw();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Gas Law Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Gas Law</label>
          <select
            value={data.lawType}
            onChange={(e) => handleDataChange({ ...data, lawType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="boyle">Boyle's Law (P-V)</option>
            <option value="charles">Charles's Law (V-T)</option>
            <option value="gay-lussac">Gay-Lussac's Law (P-T)</option>
            <option value="combined">Combined Gas Law</option>
            <option value="ideal">Ideal Gas Law (PV=nRT)</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Units</label>
          <select
            value={data.units.pressure}
            onChange={(e) => {
              const newUnits = { ...data.units, pressure: e.target.value };
              handleDataChange({ ...data, units: newUnits });
            }}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="atm">Pressure: atm</option>
            <option value="kPa">Pressure: kPa</option>
            <option value="mmHg">Pressure: mmHg</option>
          </select>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 md:grid-cols-4 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Pressure</label>
          <input
            type="number"
            value={data.pressure}
            onChange={(e) => handleDataChange({ ...data, pressure: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
          <span className="text-sm text-gray-600">{data.units.pressure}</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Volume</label>
          <input
            type="number"
            value={data.volume}
            onChange={(e) => handleDataChange({ ...data, volume: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
          <span className="text-sm text-gray-600">{data.units.volume}</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Temperature</label>
          <input
            type="number"
            value={data.temperature}
            onChange={(e) => handleDataChange({ ...data, temperature: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
          <span className="text-sm text-gray-600">{data.units.temperature}</span>
        </div>
        
        {data.lawType === 'ideal' && (
          <div>
            <label className="block text-sm font-medium mb-1">Moles</label>
            <input
              type="number"
              value={data.moles}
              onChange={(e) => handleDataChange({ ...data, moles: parseFloat(e.target.value) || 0 })}
              className="w-full px-3 py-2 border rounded"
              step="0.1"
              min="0"
            />
            <span className="text-sm text-gray-600">{data.units.moles}</span>
          </div>
        )}
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Animation
        </button>
        <button
          onClick={resetSimulation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showGraph}
            onChange={(e) => handleDataChange({ ...data, showGraph: e.target.checked })}
            className="mr-2"
          />
          Show Graph
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showParticles}
            onChange={(e) => handleDataChange({ ...data, showParticles: e.target.checked })}
            className="mr-2"
          />
          Show Particle Motion
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          {data.lawType === 'boyle' && "Boyle's Law: P₁V₁ = P₂V₂"}
          {data.lawType === 'charles' && "Charles's Law: V₁/T₁ = V₂/T₂"}
          {data.lawType === 'gay-lussac' && "Gay-Lussac's Law: P₁/T₁ = P₂/T₂"}
          {data.lawType === 'combined' && "Combined Gas Law: P₁V₁/T₁ = P₂V₂/T₂"}
          {data.lawType === 'ideal' && "Ideal Gas Law: PV = nRT"}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Pressure</div>
            <div className="text-lg font-bold text-blue-800">
              {data.pressure} {data.units.pressure}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Volume</div>
            <div className="text-lg font-bold text-green-800">
              {data.volume} {data.units.volume}
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Temperature</div>
            <div className="text-lg font-bold text-purple-800">
              {data.temperature} {data.units.temperature}
            </div>
          </div>
        </div>
        
        {gasLawResult.constant && (
          <div className="text-center p-2 bg-yellow-100 rounded mb-4">
            <div className="text-sm text-yellow-600 font-medium">Constant Value</div>
            <div className="text-lg font-bold text-yellow-800">
              {gasLawResult.constant.toFixed(4)}
            </div>
          </div>
        )}
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Gas Law Equations:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Boyle's Law: P₁V₁ = P₂V₂ (constant temperature)</li>
            <li>Charles's Law: V₁/T₁ = V₂/T₂ (constant pressure)</li>
            <li>Gay-Lussac's Law: P₁/T₁ = P₂/T₂ (constant volume)</li>
            <li>Combined Gas Law: P₁V₁/T₁ = P₂V₂/T₂</li>
            <li>Ideal Gas Law: PV = nRT</li>
          </ul>
        </div>
        
        {data.showParticles && (
          <div className="mt-4 p-4 bg-gray-900 rounded">
            <div className="text-center text-white mb-2">Particle Motion Simulation</div>
            <div className="h-32 bg-blue-900 rounded relative overflow-hidden">
              {/* Animated particles would go here */}
              <div className="absolute inset-0 flex items-center justify-center text-blue-300">
                Particle motion visualization
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Equilibrium Constant Calculator Component
const EquilibriumConstantCalculator = ({
  initialData = {
    reactionType: 'kc',
    reaction: 'A + B ⇌ C + D',
    reactants: [
      { name: 'A', initialConcentration: 1.0, equilibriumConcentration: 0.5, coefficient: 1 },
      { name: 'B', initialConcentration: 1.0, equilibriumConcentration: 0.5, coefficient: 1 }
    ],
    products: [
      { name: 'C', initialConcentration: 0.0, equilibriumConcentration: 0.5, coefficient: 1 },
      { name: 'D', initialConcentration: 0.0, equilibriumConcentration: 0.5, coefficient: 1 }
    ],
    temperature: 298,
    showCalculations: true,
    showGraph: true,
    units: { concentration: 'mol/L', pressure: 'atm', temperature: 'K' }
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const calculateKc = () => {
    let numerator = 1;
    let denominator = 1;
    
    data.products.forEach(product => {
      numerator *= Math.pow(product.equilibriumConcentration, product.coefficient);
    });
    
    data.reactants.forEach(reactant => {
      denominator *= Math.pow(reactant.equilibriumConcentration, reactant.coefficient);
    });
    
    return numerator / denominator;
  };

  const calculateKp = () => {
    // For gas phase reactions, Kp = Kc(RT)^Δn
    const R = 0.0821; // L·atm/(mol·K)
    const deltaN = data.products.reduce((sum, p) => sum + p.coefficient, 0) - 
                   data.reactants.reduce((sum, r) => sum + r.coefficient, 0);
    
    const kc = calculateKc();
    return kc * Math.pow(R * data.temperature, deltaN);
  };

  const addReactant = () => {
    const newReactant = {
      name: `R${data.reactants.length + 1}`,
      initialConcentration: 1.0,
      equilibriumConcentration: 0.5,
      coefficient: 1
    };
    const newData = { ...data, reactants: [...data.reactants, newReactant] };
    handleDataChange(newData);
  };

  const addProduct = () => {
    const newProduct = {
      name: `P${data.products.length + 1}`,
      initialConcentration: 0.0,
      equilibriumConcentration: 0.5,
      coefficient: 1
    };
    const newData = { ...data, products: [...data.products, newProduct] };
    handleDataChange(newData);
  };

  const updateSpecies = (type, index, field, value) => {
    const newData = { ...data };
    const species = type === 'reactant' ? newData.reactants : newData.products;
    species[index][field] = field === 'coefficient' ? parseInt(value) || 1 : parseFloat(value) || 0;
    handleDataChange(newData);
  };

  const kc = calculateKc();
  const kp = calculateKp();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Equilibrium Constant Calculator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Reaction Type</label>
          <select
            value={data.reactionType}
            onChange={(e) => handleDataChange({ ...data, reactionType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="kc">Concentration (Kc)</option>
            <option value="kp">Pressure (Kp)</option>
            <option value="both">Both Kc and Kp</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Temperature</label>
          <input
            type="number"
            value={data.temperature}
            onChange={(e) => handleDataChange({ ...data, temperature: parseFloat(e.target.value) || 298 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
          <span className="text-sm text-gray-600">{data.units.temperature}</span>
        </div>
      </div>

      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <h4 className="font-medium">Reactants</h4>
          <button
            onClick={addReactant}
            className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Add Reactant
          </button>
        </div>
        
        <div className="space-y-2">
          {data.reactants.map((reactant, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="text"
                value={reactant.name}
                onChange={(e) => updateSpecies('reactant', index, 'name', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Name"
              />
              <input
                type="number"
                value={reactant.coefficient}
                onChange={(e) => updateSpecies('reactant', index, 'coefficient', e.target.value)}
                className="w-12 px-2 py-1 border rounded"
                placeholder="Coeff"
                min="1"
              />
              <input
                type="number"
                value={reactant.initialConcentration}
                onChange={(e) => updateSpecies('reactant', index, 'initialConcentration', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Initial"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">→</span>
              <input
                type="number"
                value={reactant.equilibriumConcentration}
                onChange={(e) => updateSpecies('reactant', index, 'equilibriumConcentration', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Equilibrium"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">{data.units.concentration}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <h4 className="font-medium">Products</h4>
          <button
            onClick={addProduct}
            className="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600"
          >
            Add Product
          </button>
        </div>
        
        <div className="space-y-2">
          {data.products.map((product, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="text"
                value={product.name}
                onChange={(e) => updateSpecies('product', index, 'name', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Name"
              />
              <input
                type="number"
                value={product.coefficient}
                onChange={(e) => updateSpecies('product', index, 'coefficient', e.target.value)}
                className="w-12 px-2 py-1 border rounded"
                placeholder="Coeff"
                min="1"
              />
              <input
                type="number"
                value={product.initialConcentration}
                onChange={(e) => updateSpecies('product', index, 'initialConcentration', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Initial"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">→</span>
              <input
                type="number"
                value={product.equilibriumConcentration}
                onChange={(e) => updateSpecies('product', index, 'equilibriumConcentration', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Equilibrium"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">{data.units.concentration}</span>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showCalculations}
            onChange={(e) => handleDataChange({ ...data, showCalculations: e.target.checked })}
            className="mr-2"
          />
          Show Calculations
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showGraph}
            onChange={(e) => handleDataChange({ ...data, showGraph: e.target.checked })}
            className="mr-2"
          />
          Show Concentration Graph
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Equilibrium Analysis: {data.reactants.map(r => `${r.coefficient}${r.name}`).join(' + ')} ⇌ {data.products.map(p => `${p.coefficient}${p.name}`).join(' + ')}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Kc (Concentration)</div>
            <div className="text-lg font-bold text-blue-800">
              {kc.toFixed(4)}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Kp (Pressure)</div>
            <div className="text-lg font-bold text-green-800">
              {kp.toFixed(4)}
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Temperature</div>
            <div className="text-lg font-bold text-purple-800">
              {data.temperature} {data.units.temperature}
            </div>
          </div>
        </div>
        
        {data.showCalculations && (
          <div className="text-sm text-gray-600 space-y-2">
            <p><strong>Equilibrium Constant Calculation:</strong></p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">Kc = [Products]^coefficients / [Reactants]^coefficients</p>
              <p className="text-xs mt-1">
                Kc = {data.products.map(p => `[${p.name}]^${p.coefficient}`).join(' × ')} / {data.reactants.map(r => `[${r.name}]^${r.coefficient}`).join(' × ')}
              </p>
              <p className="text-xs mt-1">
                Kc = {data.products.map(p => `${p.equilibriumConcentration}^${p.coefficient}`).join(' × ')} / {data.reactants.map(r => `${r.equilibriumConcentration}^${r.coefficient}`).join(' × ')}
              </p>
              <p className="font-medium mt-2">Kc = {kc.toFixed(4)}</p>
            </div>
          </div>
        )}
        
        {data.showGraph && (
          <div className="mt-4">
            <h4 className="font-medium text-gray-700 mb-2">Concentration Changes</h4>
            <div className="flex items-end space-x-1 h-32 bg-gray-100 p-2 rounded">
              {[...data.reactants, ...data.products].map((species, index) => (
                <div key={index} className="flex-1 flex flex-col items-center">
                  <div className="flex flex-col items-center space-y-1">
                    <div
                      className="bg-red-500 w-full rounded-t"
                      style={{ height: `${species.initialConcentration * 20}px` }}
                    ></div>
                    <div
                      className="bg-blue-500 w-full rounded-t"
                      style={{ height: `${species.equilibriumConcentration * 20}px` }}
                    ></div>
                  </div>
                  <div className="text-xs text-gray-600 mt-1">{species.name}</div>
                </div>
              ))}
            </div>
            <div className="flex justify-center space-x-4 mt-2 text-xs">
              <div className="flex items-center">
                <div className="w-3 h-3 bg-red-500 rounded mr-1"></div>
                <span>Initial</span>
              </div>
              <div className="flex items-center">
                <div className="w-3 h-3 bg-blue-500 rounded mr-1"></div>
                <span>Equilibrium</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Le Chatelier Simulator Component
const LeChatelierSimulator = ({
  initialData = {
    reaction: 'N₂ + 3H₂ ⇌ 2NH₃',
    initialConditions: {
      temperature: 298,
      pressure: 1.0,
      catalyst: false,
      concentrations: {
        'N₂': 1.0,
        'H₂': 3.0,
        'NH₃': 0.0
      }
    },
    stressType: 'concentration',
    stressValue: 0.5,
    stressSpecies: 'N₂',
    showBeforeAfter: true,
    showShift: true,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetSimulation = () => {
    handleDataChange({
      ...data,
      initialConditions: {
        temperature: 298,
        pressure: 1.0,
        catalyst: false,
        concentrations: {
          'N₂': 1.0,
          'H₂': 3.0,
          'NH₃': 0.0
        }
      },
      isAnimating: false
    });
  };

  const predictShift = () => {
    const { stressType, stressValue, stressSpecies } = data;
    
    if (stressType === 'concentration') {
      if (stressSpecies === 'N₂' || stressSpecies === 'H₂') {
        return 'right'; // Forward reaction
      } else {
        return 'left'; // Reverse reaction
      }
    } else if (stressType === 'temperature') {
      // Exothermic reaction: N₂ + 3H₂ → 2NH₃ + heat
      if (stressValue > data.initialConditions.temperature) {
        return 'left'; // Endothermic direction
      } else {
        return 'right'; // Exothermic direction
      }
    } else if (stressType === 'pressure') {
      // 4 moles → 2 moles (decrease in moles)
      if (stressValue > data.initialConditions.pressure) {
        return 'right'; // Toward fewer moles
      } else {
        return 'left'; // Toward more moles
      }
    }
    return 'none';
  };

  const shift = predictShift();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Le Chatelier's Principle Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Reaction</label>
          <input
            type="text"
            value={data.reaction}
            onChange={(e) => handleDataChange({ ...data, reaction: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Stress Type</label>
          <select
            value={data.stressType}
            onChange={(e) => handleDataChange({ ...data, stressType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="concentration">Concentration Change</option>
            <option value="temperature">Temperature Change</option>
            <option value="pressure">Pressure Change</option>
            <option value="catalyst">Catalyst Addition</option>
          </select>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Stress Value</label>
          <input
            type="number"
            value={data.stressValue}
            onChange={(e) => handleDataChange({ ...data, stressValue: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">
            {data.stressType === 'temperature' ? 'K' : 
             data.stressType === 'pressure' ? 'atm' : 'mol/L'}
          </span>
        </div>
        
        {data.stressType === 'concentration' && (
          <div>
            <label className="block text-sm font-medium mb-1">Species</label>
            <select
              value={data.stressSpecies}
              onChange={(e) => handleDataChange({ ...data, stressSpecies: e.target.value })}
              className="w-full px-3 py-2 border rounded"
            >
              <option value="N₂">N₂</option>
              <option value="H₂">H₂</option>
              <option value="NH₃">NH₃</option>
            </select>
          </div>
        )}
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetSimulation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showBeforeAfter}
            onChange={(e) => handleDataChange({ ...data, showBeforeAfter: e.target.checked })}
            className="mr-2"
          />
          Show Before/After Comparison
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showShift}
            onChange={(e) => handleDataChange({ ...data, showShift: e.target.checked })}
            className="mr-2"
          />
          Show Equilibrium Shift
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Le Chatelier's Principle: {data.reaction}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Initial Temperature</div>
            <div className="text-lg font-bold text-blue-800">
              {data.initialConditions.temperature} K
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Initial Pressure</div>
            <div className="text-lg font-bold text-green-800">
              {data.initialConditions.pressure} atm
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Equilibrium Shift</div>
            <div className="text-lg font-bold text-purple-800">
              {shift === 'right' ? '→ Forward' : shift === 'left' ? '← Reverse' : 'No Change'}
            </div>
          </div>
        </div>
        
        {data.showBeforeAfter && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
            <div className="text-center p-2 bg-yellow-100 rounded">
              <h4 className="font-medium text-yellow-800 mb-2">Before Stress</h4>
              <div className="text-sm text-yellow-700 space-y-1">
                <p>N₂: {data.initialConditions.concentrations['N₂']} mol/L</p>
                <p>H₂: {data.initialConditions.concentrations['H₂']} mol/L</p>
                <p>NH₃: {data.initialConditions.concentrations['NH₃']} mol/L</p>
              </div>
            </div>
            
            <div className="text-center p-2 bg-orange-100 rounded">
              <h4 className="font-medium text-orange-800 mb-2">After Stress</h4>
              <div className="text-sm text-orange-700 space-y-1">
                <p>N₂: {(data.initialConditions.concentrations['N₂'] + (data.stressSpecies === 'N₂' ? data.stressValue : 0)).toFixed(2)} mol/L</p>
                <p>H₂: {(data.initialConditions.concentrations['H₂'] + (data.stressSpecies === 'H₂' ? data.stressValue : 0)).toFixed(2)} mol/L</p>
                <p>NH₃: {(data.initialConditions.concentrations['NH₃'] + (data.stressSpecies === 'NH₃' ? data.stressValue : 0)).toFixed(2)} mol/L</p>
              </div>
            </div>
          </div>
        )}
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Le Chatelier's Principle:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>When a system at equilibrium is disturbed, it responds to minimize the change</li>
            <li>Concentration: System shifts to consume added reactant/product</li>
            <li>Temperature: System shifts in endothermic direction when heated</li>
            <li>Pressure: System shifts toward fewer gas molecules when pressure increases</li>
            <li>Catalyst: No shift, only speeds up both directions equally</li>
          </ul>
        </div>
        
        {data.showShift && (
          <div className="mt-4 p-4 bg-gray-900 rounded">
            <div className="text-center text-white mb-2">Equilibrium Shift Visualization</div>
            <div className="h-32 bg-blue-900 rounded relative overflow-hidden">
              <div className="absolute inset-0 flex items-center justify-center text-blue-300">
                {shift === 'right' ? '→ Forward Reaction Favored' : 
                 shift === 'left' ? '← Reverse Reaction Favored' : 
                 'No Net Shift'}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Oxidation Number Calculator Component
const OxidationNumberCalculator = ({
  initialData = {
    compound: 'H₂SO₄',
    elements: [
      { symbol: 'H', oxidationNumber: 1, count: 2 },
      { symbol: 'S', oxidationNumber: 6, count: 1 },
      { symbol: 'O', oxidationNumber: -2, count: 4 }
    ],
    showRules: true,
    showCalculation: true,
    showRedox: false,
    redoxReaction: 'Fe + CuSO₄ → FeSO₄ + Cu'
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const calculateTotalCharge = () => {
    return data.elements.reduce((total, element) => {
      return total + (element.oxidationNumber * element.count);
    }, 0);
  };

  const addElement = () => {
    const newElement = {
      symbol: 'X',
      oxidationNumber: 0,
      count: 1
    };
    const newData = { ...data, elements: [...data.elements, newElement] };
    handleDataChange(newData);
  };

  const removeElement = (index) => {
    const newElements = data.elements.filter((_, i) => i !== index);
    const newData = { ...data, elements: newElements };
    handleDataChange(newData);
  };

  const updateElement = (index, field, value) => {
    const newElements = [...data.elements];
    newElements[index][field] = field === 'count' ? parseInt(value) || 1 : 
                                field === 'oxidationNumber' ? parseFloat(value) || 0 : value;
    const newData = { ...data, elements: newElements };
    handleDataChange(newData);
  };

  const totalCharge = calculateTotalCharge();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Oxidation Number Calculator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Compound</label>
          <input
            type="text"
            value={data.compound}
            onChange={(e) => handleDataChange({ ...data, compound: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Total Charge</label>
          <div className="w-full px-3 py-2 border rounded bg-gray-50">
            {totalCharge}
          </div>
        </div>
      </div>

      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <h4 className="font-medium">Elements</h4>
          <button
            onClick={addElement}
            className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Add Element
          </button>
        </div>
        
        <div className="space-y-2">
          {data.elements.map((element, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="text"
                value={element.symbol}
                onChange={(e) => updateElement(index, 'symbol', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Symbol"
              />
              <input
                type="number"
                value={element.oxidationNumber}
                onChange={(e) => updateElement(index, 'oxidationNumber', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Ox. #"
                step="0.5"
              />
              <input
                type="number"
                value={element.count}
                onChange={(e) => updateElement(index, 'count', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Count"
                min="1"
              />
              <span className="text-sm text-gray-600">= {element.oxidationNumber * element.count}</span>
              <button
                onClick={() => removeElement(index)}
                className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showRules}
            onChange={(e) => handleDataChange({ ...data, showRules: e.target.checked })}
            className="mr-2"
          />
          Show Oxidation Number Rules
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showCalculation}
            onChange={(e) => handleDataChange({ ...data, showCalculation: e.target.checked })}
            className="mr-2"
          />
          Show Calculation Steps
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showRedox}
            onChange={(e) => handleDataChange({ ...data, showRedox: e.target.checked })}
            className="mr-2"
          />
          Show Redox Reaction Analysis
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Oxidation Number Analysis: {data.compound}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Total Charge</div>
            <div className="text-lg font-bold text-blue-800">
              {totalCharge}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Number of Elements</div>
            <div className="text-lg font-bold text-green-800">
              {data.elements.length}
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Compound Type</div>
            <div className="text-lg font-bold text-purple-800">
              {totalCharge === 0 ? 'Neutral' : totalCharge > 0 ? 'Cation' : 'Anion'}
            </div>
          </div>
        </div>
        
        {data.showCalculation && (
          <div className="text-sm text-gray-600 space-y-2">
            <p><strong>Calculation:</strong></p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">Total Charge = Σ(Oxidation Number × Count)</p>
              <p className="text-xs mt-1">
                {data.elements.map((element, index) => 
                  `${element.oxidationNumber} × ${element.count}${index < data.elements.length - 1 ? ' + ' : ''}`
                ).join('')} = {totalCharge}
              </p>
            </div>
          </div>
        )}
        
        {data.showRules && (
          <div className="text-sm text-gray-600 space-y-2 mt-4">
            <p><strong>Oxidation Number Rules:</strong></p>
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li>Free elements: oxidation number = 0</li>
              <li>Monatomic ions: oxidation number = charge</li>
              <li>Hydrogen: +1 (except in hydrides: -1)</li>
              <li>Oxygen: -2 (except in peroxides: -1)</li>
              <li>Group 1 metals: +1, Group 2 metals: +2</li>
              <li>Halogens: -1 (except when bonded to oxygen)</li>
            </ul>
          </div>
        )}
        
        {data.showRedox && (
          <div className="mt-4 p-4 bg-yellow-50 rounded">
            <h4 className="font-medium text-yellow-800 mb-2">Redox Reaction Analysis</h4>
            <div className="text-sm text-yellow-700">
              <p><strong>Reaction:</strong> {data.redoxReaction}</p>
              <p><strong>Oxidation:</strong> Fe → Fe²⁺ + 2e⁻ (loses electrons)</p>
              <p><strong>Reduction:</strong> Cu²⁺ + 2e⁻ → Cu (gains electrons)</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Buffer Solution Builder Component
const BufferSolutionBuilder = ({
  initialData = {
    bufferType: 'acidic',
    weakAcid: 'CH₃COOH',
    conjugateBase: 'CH₃COO⁻',
    acidConcentration: 0.1,
    baseConcentration: 0.1,
    volume: 1.0,
    targetPH: 4.74,
    ka: 1.8e-5,
    showHendersonHasselbalch: true,
    showTitration: true,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetBuffer = () => {
    handleDataChange({
      ...data,
      acidConcentration: 0.1,
      baseConcentration: 0.1,
      targetPH: 4.74,
      isAnimating: false
    });
  };

  const calculatePH = () => {
    // Henderson-Hasselbalch equation: pH = pKa + log([A⁻]/[HA])
    const pKa = -Math.log10(data.ka);
    const ratio = data.baseConcentration / data.acidConcentration;
    return pKa + Math.log10(ratio);
  };

  const calculateBufferCapacity = () => {
    // Buffer capacity = 2.303 × [HA] × [A⁻] / ([HA] + [A⁻])
    const numerator = 2.303 * data.acidConcentration * data.baseConcentration;
    const denominator = data.acidConcentration + data.baseConcentration;
    return numerator / denominator;
  };

  const ph = calculatePH();
  const bufferCapacity = calculateBufferCapacity();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Buffer Solution Builder</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Buffer Type</label>
          <select
            value={data.bufferType}
            onChange={(e) => handleDataChange({ ...data, bufferType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="acidic">Acidic Buffer</option>
            <option value="basic">Basic Buffer</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Target pH</label>
          <input
            type="number"
            value={data.targetPH}
            onChange={(e) => handleDataChange({ ...data, targetPH: parseFloat(e.target.value) || 7 })}
            className="w-full px-3 py-2 border rounded"
            step="0.01"
            min="0"
            max="14"
          />
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Weak Acid</label>
          <input
            type="text"
            value={data.weakAcid}
            onChange={(e) => handleDataChange({ ...data, weakAcid: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Conjugate Base</label>
          <input
            type="text"
            value={data.conjugateBase}
            onChange={(e) => handleDataChange({ ...data, conjugateBase: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          />
        </div>
      </div>

      <div className="mb-4 grid grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Acid Concentration</label>
          <input
            type="number"
            value={data.acidConcentration}
            onChange={(e) => handleDataChange({ ...data, acidConcentration: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.01"
            min="0"
          />
          <span className="text-sm text-gray-600">mol/L</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Base Concentration</label>
          <input
            type="number"
            value={data.baseConcentration}
            onChange={(e) => handleDataChange({ ...data, baseConcentration: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.01"
            min="0"
          />
          <span className="text-sm text-gray-600">mol/L</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Volume</label>
          <input
            type="number"
            value={data.volume}
            onChange={(e) => handleDataChange({ ...data, volume: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
          <span className="text-sm text-gray-600">L</span>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetBuffer}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showHendersonHasselbalch}
            onChange={(e) => handleDataChange({ ...data, showHendersonHasselbalch: e.target.checked })}
            className="mr-2"
          />
          Show Henderson-Hasselbalch Equation
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showTitration}
            onChange={(e) => handleDataChange({ ...data, showTitration: e.target.checked })}
            className="mr-2"
          />
          Show pH Titration Curve
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Buffer Solution: {data.weakAcid} + {data.conjugateBase}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">pH</div>
            <div className="text-lg font-bold text-blue-800">
              {ph.toFixed(2)}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">pKa</div>
            <div className="text-lg font-bold text-green-800">
              {(-Math.log10(data.ka)).toFixed(2)}
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Buffer Capacity</div>
            <div className="text-lg font-bold text-purple-800">
              {bufferCapacity.toFixed(4)}
            </div>
          </div>
          
          <div className="text-center p-2 bg-yellow-100 rounded">
            <div className="text-sm text-yellow-600 font-medium">Ratio [A⁻]/[HA]</div>
            <div className="text-lg font-bold text-yellow-800">
              {(data.baseConcentration / data.acidConcentration).toFixed(2)}
            </div>
          </div>
        </div>
        
        {data.showHendersonHasselbalch && (
          <div className="text-sm text-gray-600 space-y-2">
            <p><strong>Henderson-Hasselbalch Equation:</strong></p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">pH = pKa + log([A⁻]/[HA])</p>
              <p className="text-xs mt-1">
                pH = {(-Math.log10(data.ka)).toFixed(2)} + log({data.baseConcentration}/{data.acidConcentration})
              </p>
              <p className="text-xs mt-1">
                pH = {(-Math.log10(data.ka)).toFixed(2)} + {Math.log10(data.baseConcentration / data.acidConcentration).toFixed(2)}
              </p>
              <p className="font-medium mt-2">pH = {ph.toFixed(2)}</p>
            </div>
          </div>
        )}
        
        <div className="text-sm text-gray-600 space-y-2 mt-4">
          <p><strong>Buffer Properties:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Resists pH changes when small amounts of acid/base are added</li>
            <li>Most effective when pH ≈ pKa (ratio ≈ 1)</li>
            <li>Buffer capacity depends on concentrations of weak acid and conjugate base</li>
            <li>Optimal buffer range: pKa ± 1</li>
          </ul>
        </div>
        
        {data.showTitration && (
          <div className="mt-4 p-4 bg-gray-900 rounded">
            <div className="text-center text-white mb-2">pH Titration Curve</div>
            <div className="h-32 bg-blue-900 rounded relative overflow-hidden">
              <div className="absolute inset-0 flex items-center justify-center text-blue-300">
                pH vs. Volume titration curve
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

// Advanced Stoichiometry Calculator Component
const AdvancedStoichiometryCalculator = ({
  initialData = {
    reaction: '2H₂ + O₂ → 2H₂O',
    reactants: [
      { name: 'H₂', coefficient: 2, molarMass: 2.016, available: 10.0, unit: 'g' },
      { name: 'O₂', coefficient: 1, molarMass: 32.00, available: 16.0, unit: 'g' }
    ],
    products: [
      { name: 'H₂O', coefficient: 2, molarMass: 18.016, unit: 'g' }
    ],
    showLimitingReagent: true,
    showTheoreticalYield: true,
    showPercentYield: false,
    actualYield: 0,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetCalculation = () => {
    handleDataChange({
      ...data,
      reactants: [
        { name: 'H₂', coefficient: 2, molarMass: 2.016, available: 10.0, unit: 'g' },
        { name: 'O₂', coefficient: 1, molarMass: 32.00, available: 16.0, unit: 'g' }
      ],
      actualYield: 0,
      isAnimating: false
    });
  };

  const calculateMoles = (mass, molarMass) => {
    return mass / molarMass;
  };

  const findLimitingReagent = () => {
    let limitingReagent = null;
    let maxMoles = Infinity;

    data.reactants.forEach(reactant => {
      const moles = calculateMoles(reactant.available, reactant.molarMass);
      const maxPossibleMoles = moles / reactant.coefficient;
      
      if (maxPossibleMoles < maxMoles) {
        maxMoles = maxPossibleMoles;
        limitingReagent = reactant;
      }
    });

    return { limitingReagent, maxMoles };
  };

  const calculateTheoreticalYield = () => {
    const { limitingReagent, maxMoles } = findLimitingReagent();
    if (!limitingReagent) return 0;

    // Find the product that corresponds to the limiting reagent
    const product = data.products[0]; // Assuming one product for simplicity
    const productMoles = maxMoles * product.coefficient;
    return productMoles * product.molarMass;
  };

  const calculatePercentYield = () => {
    const theoretical = calculateTheoreticalYield();
    return theoretical > 0 ? (data.actualYield / theoretical) * 100 : 0;
  };

  const { limitingReagent, maxMoles } = findLimitingReagent();
  const theoreticalYield = calculateTheoreticalYield();
  const percentYield = calculatePercentYield();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Advanced Stoichiometry Calculator</h3>
      
      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Chemical Reaction</label>
        <input
          type="text"
          value={data.reaction}
          onChange={(e) => handleDataChange({ ...data, reaction: e.target.value })}
          className="w-full px-3 py-2 border rounded"
        />
      </div>

      <div className="mb-4">
        <h4 className="font-medium mb-2">Reactants</h4>
        <div className="space-y-2">
          {data.reactants.map((reactant, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="text"
                value={reactant.name}
                onChange={(e) => {
                  const newReactants = [...data.reactants];
                  newReactants[index].name = e.target.value;
                  handleDataChange({ ...data, reactants: newReactants });
                }}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Name"
              />
              <input
                type="number"
                value={reactant.coefficient}
                onChange={(e) => {
                  const newReactants = [...data.reactants];
                  newReactants[index].coefficient = parseInt(e.target.value) || 1;
                  handleDataChange({ ...data, reactants: newReactants });
                }}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Coeff"
                min="1"
              />
              <input
                type="number"
                value={reactant.molarMass}
                onChange={(e) => {
                  const newReactants = [...data.reactants];
                  newReactants[index].molarMass = parseFloat(e.target.value) || 0;
                  handleDataChange({ ...data, reactants: newReactants });
                }}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Molar Mass"
                step="0.001"
                min="0"
              />
              <span className="text-sm text-gray-600">g/mol</span>
              <input
                type="number"
                value={reactant.available}
                onChange={(e) => {
                  const newReactants = [...data.reactants];
                  newReactants[index].available = parseFloat(e.target.value) || 0;
                  handleDataChange({ ...data, reactants: newReactants });
                }}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Available"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">{reactant.unit}</span>
              <span className="text-sm text-gray-600">
                = {calculateMoles(reactant.available, reactant.molarMass).toFixed(3)} mol
              </span>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <h4 className="font-medium mb-2">Products</h4>
        <div className="space-y-2">
          {data.products.map((product, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <input
                type="text"
                value={product.name}
                onChange={(e) => {
                  const newProducts = [...data.products];
                  newProducts[index].name = e.target.value;
                  handleDataChange({ ...data, products: newProducts });
                }}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Name"
              />
              <input
                type="number"
                value={product.coefficient}
                onChange={(e) => {
                  const newProducts = [...data.products];
                  newProducts[index].coefficient = parseInt(e.target.value) || 1;
                  handleDataChange({ ...data, products: newProducts });
                }}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Coeff"
                min="1"
              />
              <input
                type="number"
                value={product.molarMass}
                onChange={(e) => {
                  const newProducts = [...data.products];
                  newProducts[index].molarMass = parseFloat(e.target.value) || 0;
                  handleDataChange({ ...data, products: newProducts });
                }}
                className="w-20 px-2 py-1 border rounded"
                placeholder="Molar Mass"
                step="0.001"
                min="0"
              />
              <span className="text-sm text-gray-600">g/mol</span>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Actual Yield</label>
          <input
            type="number"
            value={data.actualYield}
            onChange={(e) => handleDataChange({ ...data, actualYield: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
          <span className="text-sm text-gray-600">g</span>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetCalculation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showLimitingReagent}
            onChange={(e) => handleDataChange({ ...data, showLimitingReagent: e.target.checked })}
            className="mr-2"
          />
          Show Limiting Reagent Analysis
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showTheoreticalYield}
            onChange={(e) => handleDataChange({ ...data, showTheoreticalYield: e.target.checked })}
            className="mr-2"
          />
          Show Theoretical Yield Calculation
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showPercentYield}
            onChange={(e) => handleDataChange({ ...data, showPercentYield: e.target.checked })}
            className="mr-2"
          />
          Show Percent Yield
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Stoichiometry Analysis: {data.reaction}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Limiting Reagent</div>
            <div className="text-lg font-bold text-blue-800">
              {limitingReagent ? limitingReagent.name : 'None'}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Theoretical Yield</div>
            <div className="text-lg font-bold text-green-800">
              {theoreticalYield.toFixed(2)} g
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Percent Yield</div>
            <div className="text-lg font-bold text-purple-800">
              {percentYield.toFixed(1)}%
            </div>
          </div>
          
          <div className="text-center p-2 bg-yellow-100 rounded">
            <div className="text-sm text-yellow-600 font-medium">Excess Reagent</div>
            <div className="text-lg font-bold text-yellow-800">
              {limitingReagent ? data.reactants.find(r => r.name !== limitingReagent.name)?.name : 'None'}
            </div>
          </div>
        </div>
        
        {data.showLimitingReagent && limitingReagent && (
          <div className="text-sm text-gray-600 space-y-2">
            <p><strong>Limiting Reagent Analysis:</strong></p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">{limitingReagent.name} is the limiting reagent</p>
              <p className="text-xs mt-1">
                Available: {limitingReagent.available} g ÷ {limitingReagent.molarMass} g/mol = {calculateMoles(limitingReagent.available, limitingReagent.molarMass).toFixed(3)} mol
              </p>
              <p className="text-xs mt-1">
                Max possible: {calculateMoles(limitingReagent.available, limitingReagent.molarMass).toFixed(3)} mol ÷ {limitingReagent.coefficient} = {maxMoles.toFixed(3)} mol of reaction
              </p>
            </div>
          </div>
        )}
        
        {data.showTheoreticalYield && (
          <div className="text-sm text-gray-600 space-y-2 mt-4">
            <p><strong>Theoretical Yield Calculation:</strong></p>
            <div className="bg-white p-2 rounded border">
              <p className="font-medium">Based on limiting reagent: {limitingReagent?.name}</p>
              <p className="text-xs mt-1">
                Product moles = {maxMoles.toFixed(3)} mol × {data.products[0]?.coefficient} = {(maxMoles * (data.products[0]?.coefficient || 1)).toFixed(3)} mol
              </p>
              <p className="text-xs mt-1">
                Theoretical yield = {(maxMoles * (data.products[0]?.coefficient || 1)).toFixed(3)} mol × {data.products[0]?.molarMass} g/mol = {theoreticalYield.toFixed(2)} g
              </p>
            </div>
          </div>
        )}
        
        <div className="text-sm text-gray-600 space-y-2 mt-4">
          <p><strong>Stoichiometry Steps:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Convert masses to moles using molar masses</li>
            <li>Use coefficients to find limiting reagent</li>
            <li>Calculate theoretical yield from limiting reagent</li>
            <li>Compare actual vs theoretical yield for percent yield</li>
            <li>Identify excess reagents and calculate remaining amounts</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default {
    MolecularStructure,
    ChemicalReaction,
    MatterClassificationSimulator,
    StatesOfMatterVisualizer,
    AtomicStructureBuilder,
    IsotopeCalculator,
    GasLawSimulator,
    EquilibriumConstantCalculator,
    LeChatelierSimulator,
    OxidationNumberCalculator,
    BufferSolutionBuilder,
    AdvancedStoichiometryCalculator
};
