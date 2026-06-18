import React, { useState, useEffect } from 'react';

const ChemicalBondingVisualizer = ({ initialData, onChange, isSubmitted }) => {
    const [molecule, setMolecule] = useState(initialData.molecule || '');
    const [showLewis, setShowLewis] = useState(false);
    const [showGeometry, setShowGeometry] = useState(false);
    const [showVSEPR, setShowVSEPR] = useState(false);
    const [showElectronPairs, setShowElectronPairs] = useState(false);

    // Common molecules and their properties
    const molecules = {
        'H2O': {
            name: 'Water',
            formula: 'H₂O',
            lewisStructure: 'H:O:H',
            electronPairs: { central: 4, bonding: 2, lone: 2 },
            geometry: 'bent',
            bondAngle: 104.5,
            polarity: 'polar',
            hybridization: 'sp³',
            description: 'Water is a polar molecule with a bent geometry due to two lone pairs on oxygen.'
        },
        'CO2': {
            name: 'Carbon Dioxide',
            formula: 'CO₂',
            lewisStructure: 'O::C::O',
            electronPairs: { central: 4, bonding: 4, lone: 0 },
            geometry: 'linear',
            bondAngle: 180,
            polarity: 'nonpolar',
            hybridization: 'sp',
            description: 'Carbon dioxide is a nonpolar molecule with linear geometry and no lone pairs.'
        },
        'NH3': {
            name: 'Ammonia',
            formula: 'NH₃',
            lewisStructure: 'H:N:H\n  H',
            electronPairs: { central: 4, bonding: 3, lone: 1 },
            geometry: 'trigonal pyramidal',
            bondAngle: 107.3,
            polarity: 'polar',
            hybridization: 'sp³',
            description: 'Ammonia is a polar molecule with trigonal pyramidal geometry due to one lone pair.'
        },
        'CH4': {
            name: 'Methane',
            formula: 'CH₄',
            lewisStructure: 'H\nH:C:H\nH',
            electronPairs: { central: 4, bonding: 4, lone: 0 },
            geometry: 'tetrahedral',
            bondAngle: 109.5,
            polarity: 'nonpolar',
            hybridization: 'sp³',
            description: 'Methane is a nonpolar molecule with tetrahedral geometry and no lone pairs.'
        },
        'BF3': {
            name: 'Boron Trifluoride',
            formula: 'BF₃',
            lewisStructure: 'F:B:F\n  F',
            electronPairs: { central: 3, bonding: 3, lone: 0 },
            geometry: 'trigonal planar',
            bondAngle: 120,
            polarity: 'nonpolar',
            hybridization: 'sp²',
            description: 'Boron trifluoride is a nonpolar molecule with trigonal planar geometry.'
        },
        'H2S': {
            name: 'Hydrogen Sulfide',
            formula: 'H₂S',
            lewisStructure: 'H:S:H',
            electronPairs: { central: 4, bonding: 2, lone: 2 },
            geometry: 'bent',
            bondAngle: 92.1,
            polarity: 'polar',
            hybridization: 'sp³',
            description: 'Hydrogen sulfide has bent geometry similar to water but with different bond angles.'
        }
    };

    // VSEPR theory rules and geometries
    const vseprGeometries = {
        'AX2': { name: 'Linear', angle: 180, examples: ['CO₂', 'BeCl₂'] },
        'AX3': { name: 'Trigonal Planar', angle: 120, examples: ['BF₃', 'SO₃'] },
        'AX4': { name: 'Tetrahedral', angle: 109.5, examples: ['CH₄', 'SiCl₄'] },
        'AX5': { name: 'Trigonal Bipyramidal', angle: '90°, 120°', examples: ['PCl₅', 'PF₅'] },
        'AX6': { name: 'Octahedral', angle: 90, examples: ['SF₆', 'PF₆⁻'] },
        'AX2E': { name: 'Bent', angle: '<120°', examples: ['SO₂', 'O₃'] },
        'AX3E': { name: 'Trigonal Pyramidal', angle: '<109.5°', examples: ['NH₃', 'PCl₃'] },
        'AX2E2': { name: 'Bent', angle: '<109.5°', examples: ['H₂O', 'H₂S'] },
        'AX4E': { name: 'Seesaw', angle: '<90°, <120°', examples: ['SF₄', 'TeCl₄'] },
        'AX3E2': { name: 'T-Shaped', angle: '<90°', examples: ['ClF₃', 'BrF₃'] }
    };

    useEffect(() => {
        const formattedData = {
            type: "chemical_bonding",
            molecule: molecule,
            selectedMolecule: molecules[molecule] || null
        };
        onChange(formattedData);
    }, [molecule, onChange]);

    const getVSEPRNotation = (moleculeData) => {
        if (!moleculeData) return '';
        
        const { electronPairs } = moleculeData;
        const bondingPairs = electronPairs.bonding;
        const lonePairs = electronPairs.lone;
        
        return `AX${bondingPairs}${lonePairs > 0 ? 'E'.repeat(lonePairs) : ''}`;
    };

    const getGeometryColor = (geometry) => {
        const colors = {
            'linear': 'bg-blue-500',
            'bent': 'bg-green-500',
            'trigonal planar': 'bg-yellow-500',
            'trigonal pyramidal': 'bg-orange-500',
            'tetrahedral': 'bg-purple-500',
            'trigonal bipyramidal': 'bg-red-500',
            'octahedral': 'bg-indigo-500'
        };
        return colors[geometry] || 'bg-gray-500';
    };

    const renderLewisStructure = (moleculeData) => {
        if (!moleculeData) return null;
        
        const { lewisStructure, electronPairs } = moleculeData;
        
        return (
            <div className="text-center p-4 bg-white rounded-lg border">
                <div className="text-lg font-mono text-gray-800 whitespace-pre-line mb-3">
                    {lewisStructure}
                </div>
                <div className="text-sm text-gray-600">
                    <div><strong>Bonding pairs:</strong> {electronPairs.bonding}</div>
                    <div><strong>Lone pairs:</strong> {electronPairs.lone}</div>
                    <div><strong>Total electron pairs:</strong> {electronPairs.central}</div>
                </div>
            </div>
        );
    };

    const renderMolecularGeometry = (moleculeData) => {
        if (!moleculeData) return null;
        
        const { geometry, bondAngle, hybridization } = moleculeData;
        
        return (
            <div className="text-center p-4 bg-white rounded-lg border">
                <div className={`inline-block w-24 h-24 ${getGeometryColor(geometry)} rounded-lg mb-3 flex items-center justify-center`}>
                    <span className="text-white font-bold text-sm">{geometry.charAt(0).toUpperCase()}</span>
                </div>
                <div className="text-sm text-gray-600">
                    <div><strong>Geometry:</strong> {geometry}</div>
                    <div><strong>Bond angle:</strong> {bondAngle}°</div>
                    <div><strong>Hybridization:</strong> {hybridization}</div>
                </div>
            </div>
        );
    };

    const renderVSEPRAnalysis = (moleculeData) => {
        if (!moleculeData) return null;
        
        const vseprNotation = getVSEPRNotation(moleculeData);
        const vseprInfo = vseprGeometries[vseprNotation];
        
        return (
            <div className="p-4 bg-white rounded-lg border">
                <h5 className="font-medium text-gray-800 mb-2">VSEPR Analysis:</h5>
                <div className="space-y-2 text-sm text-gray-600">
                    <div><strong>VSEPR Notation:</strong> {vseprNotation}</div>
                    {vseprInfo && (
                        <>
                            <div><strong>Predicted Geometry:</strong> {vseprInfo.name}</div>
                            <div><strong>Bond Angles:</strong> {vseprInfo.angle}</div>
                            <div><strong>Examples:</strong> {vseprInfo.examples.join(', ')}</div>
                        </>
                    )}
                </div>
            </div>
        );
    };

    const getPolarityExplanation = (moleculeData) => {
        if (!moleculeData) return '';
        
        const { polarity, geometry, formula } = moleculeData;
        
        if (polarity === 'polar') {
            return `${formula} is polar because it has an asymmetrical distribution of electron density. The ${geometry} geometry and presence of lone pairs create a dipole moment.`;
        } else {
            return `${formula} is nonpolar because it has a symmetrical distribution of electron density. The ${geometry} geometry results in no net dipole moment.`;
        }
    };

    const getHybridizationExplanation = (moleculeData) => {
        if (!moleculeData) return '';
        
        const { hybridization, electronPairs, formula } = moleculeData;
        const totalPairs = electronPairs.central;
        
        const explanations = {
            'sp': 'Linear geometry with 2 electron pairs around the central atom.',
            'sp²': 'Trigonal planar geometry with 3 electron pairs around the central atom.',
            'sp³': 'Tetrahedral geometry with 4 electron pairs around the central atom.',
            'sp³d': 'Trigonal bipyramidal geometry with 5 electron pairs around the central atom.',
            'sp³d²': 'Octahedral geometry with 6 electron pairs around the central atom.'
        };
        
        return `${formula} uses ${hybridization} hybridization. ${explanations[hybridization] || `This involves ${totalPairs} electron pairs around the central atom.`}`;
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Chemical Bonding Visualizer</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowLewis(!showLewis)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showLewis 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showLewis ? 'Hide Lewis' : 'Show Lewis'}
                    </button>
                    <button
                        onClick={() => setShowGeometry(!showGeometry)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showGeometry 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showGeometry ? 'Hide Geometry' : 'Show Geometry'}
                    </button>
                    <button
                        onClick={() => setShowVSEPR(!showVSEPR)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showVSEPR 
                                ? 'bg-purple-100 text-purple-700 hover:bg-purple-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showVSEPR ? 'Hide VSEPR' : 'Show VSEPR'}
                    </button>
                </div>
            </div>

            {/* Molecule Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Select Molecule:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={molecule} 
                    onChange={(e) => !isSubmitted && setMolecule(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="">Choose a molecule...</option>
                    {Object.entries(molecules).map(([key, mol]) => (
                        <option key={key} value={key}>{mol.name} ({mol.formula})</option>
                    ))}
                </select>
            </div>

            {/* Molecule Information */}
            {molecule && molecules[molecule] && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-lg font-medium text-gray-800 mb-3">
                        {molecules[molecule].name} ({molecules[molecule].formula})
                    </h4>
                    <p className="text-sm text-gray-600 mb-3">
                        {molecules[molecule].description}
                    </p>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Polarity</div>
                            <div className={`text-sm px-2 py-1 rounded-full inline-block ${
                                molecules[molecule].polarity === 'polar' 
                                    ? 'bg-blue-100 text-blue-800' 
                                    : 'bg-green-100 text-green-800'
                            }`}>
                                {molecules[molecule].polarity}
                            </div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Geometry</div>
                            <div className="text-sm text-gray-600">{molecules[molecule].geometry}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Hybridization</div>
                            <div className="text-sm text-gray-600">{molecules[molecule].hybridization}</div>
                        </div>
                    </div>
                </div>
            )}

            {/* Lewis Structure */}
            {showLewis && molecule && molecules[molecule] && (
                <div className="mb-6">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Lewis Structure:</h4>
                    {renderLewisStructure(molecules[molecule])}
                </div>
            )}

            {/* Molecular Geometry */}
            {showGeometry && molecule && molecules[molecule] && (
                <div className="mb-6">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Molecular Geometry:</h4>
                    {renderMolecularGeometry(molecules[molecule])}
                </div>
            )}

            {/* VSEPR Analysis */}
            {showVSEPR && molecule && molecules[molecule] && (
                <div className="mb-6">
                    <h4 className="text-md font-medium text-gray-800 mb-3">VSEPR Theory Analysis:</h4>
                    {renderVSEPRAnalysis(molecules[molecule])}
                </div>
            )}

            {/* Detailed Explanations */}
            {molecule && molecules[molecule] && (
                <div className="mb-6 space-y-4">
                    {/* Polarity Explanation */}
                    <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                        <h5 className="font-medium text-blue-800 mb-2">Polarity Explanation:</h5>
                        <p className="text-sm text-blue-700">{getPolarityExplanation(molecules[molecule])}</p>
                    </div>

                    {/* Hybridization Explanation */}
                    <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                        <h5 className="font-medium text-green-800 mb-2">Hybridization Explanation:</h5>
                        <p className="text-sm text-green-700">{getHybridizationExplanation(molecules[molecule])}</p>
                    </div>
                </div>
            )}

            {/* VSEPR Theory Guide */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">VSEPR Theory Guide:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    {Object.entries(vseprGeometries).slice(0, 6).map(([notation, info]) => (
                        <div key={notation} className="p-3 bg-white rounded border">
                            <div className="font-medium text-gray-800">{notation}</div>
                            <div className="text-sm text-gray-600">{info.name}</div>
                            <div className="text-xs text-gray-500">Angle: {info.angle}</div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• VSEPR theory predicts molecular geometry based on electron pair repulsion</li>
                    <li>• Lone pairs take up more space than bonding pairs</li>
                    <li>• Symmetrical molecules are usually nonpolar</li>
                    <li>• Hybridization explains the mixing of atomic orbitals</li>
                    <li>• Bond angles decrease with increasing number of lone pairs</li>
                </ul>
            </div>
        </div>
    );
};

export default ChemicalBondingVisualizer;
