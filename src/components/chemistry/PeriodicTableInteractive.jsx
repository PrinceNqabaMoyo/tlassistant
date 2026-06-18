import React, { useState, useEffect } from 'react';

const PeriodicTableInteractive = ({ initialData, onChange, isSubmitted }) => {
    const [selectedElement, setSelectedElement] = useState(null);
    const [searchTerm, setSearchTerm] = useState('');
    const [filterCategory, setFilterCategory] = useState('all');
    const [showProperties, setShowProperties] = useState(false);
    const [showTrends, setShowTrends] = useState(false);

    // Periodic table data with comprehensive element information
    const periodicTable = [
        // Period 1
        { number: 1, symbol: 'H', name: 'Hydrogen', mass: 1.008, category: 'nonmetal', group: 1, period: 1, electronegativity: 2.20, ionization: 13.598, electronConfig: '1s¹', discovery: 1766, discoverer: 'Henry Cavendish' },
        { number: 2, symbol: 'He', name: 'Helium', mass: 4.003, category: 'noble gas', group: 18, period: 1, electronegativity: null, ionization: 24.587, electronConfig: '1s²', discovery: 1895, discoverer: 'Pierre Janssen' },
        
        // Period 2
        { number: 3, symbol: 'Li', name: 'Lithium', mass: 6.941, category: 'alkali metal', group: 1, period: 2, electronegativity: 0.98, ionization: 5.392, electronConfig: '[He] 2s¹', discovery: 1817, discoverer: 'Johann August Arfvedson' },
        { number: 4, symbol: 'Be', name: 'Beryllium', mass: 9.012, category: 'alkaline earth', group: 2, period: 2, electronegativity: 1.57, ionization: 9.323, electronConfig: '[He] 2s²', discovery: 1798, discoverer: 'Louis-Nicolas Vauquelin' },
        { number: 5, symbol: 'B', name: 'Boron', mass: 10.811, category: 'metalloid', group: 13, period: 2, electronegativity: 2.04, ionization: 8.298, electronConfig: '[He] 2s² 2p¹', discovery: 1808, discoverer: 'Joseph Louis Gay-Lussac' },
        { number: 6, symbol: 'C', name: 'Carbon', mass: 12.011, category: 'nonmetal', group: 14, period: 2, electronegativity: 2.55, ionization: 11.260, electronConfig: '[He] 2s² 2p²', discovery: 'Ancient', discoverer: 'Unknown' },
        { number: 7, symbol: 'N', name: 'Nitrogen', mass: 14.007, category: 'nonmetal', group: 15, period: 2, electronegativity: 3.04, ionization: 14.534, electronConfig: '[He] 2s² 2p³', discovery: 1772, discoverer: 'Daniel Rutherford' },
        { number: 8, symbol: 'O', name: 'Oxygen', mass: 15.999, category: 'nonmetal', group: 16, period: 2, electronegativity: 3.44, ionization: 13.618, electronConfig: '[He] 2s² 2p⁴', discovery: 1774, discoverer: 'Joseph Priestley' },
        { number: 9, symbol: 'F', name: 'Fluorine', mass: 18.998, category: 'halogen', group: 17, period: 2, electronegativity: 3.98, ionization: 17.422, electronConfig: '[He] 2s² 2p⁵', discovery: 1886, discoverer: 'Henri Moissan' },
        { number: 10, symbol: 'Ne', name: 'Neon', mass: 20.180, category: 'noble gas', group: 18, period: 2, electronegativity: null, ionization: 21.565, electronConfig: '[He] 2s² 2p⁶', discovery: 1898, discoverer: 'Sir William Ramsay' },
        
        // Period 3
        { number: 11, symbol: 'Na', name: 'Sodium', mass: 22.990, category: 'alkali metal', group: 1, period: 3, electronegativity: 0.93, ionization: 5.139, electronConfig: '[Ne] 3s¹', discovery: 1807, discoverer: 'Humphry Davy' },
        { number: 12, symbol: 'Mg', name: 'Magnesium', mass: 24.305, category: 'alkaline earth', group: 2, period: 3, electronegativity: 1.31, ionization: 7.646, electronConfig: '[Ne] 3s²', discovery: 1755, discoverer: 'Joseph Black' },
        { number: 13, symbol: 'Al', name: 'Aluminum', mass: 26.982, category: 'post-transition', group: 13, period: 3, electronegativity: 1.61, ionization: 5.986, electronConfig: '[Ne] 3s² 3p¹', discovery: 1825, discoverer: 'Hans Christian Ørsted' },
        { number: 14, symbol: 'Si', name: 'Silicon', mass: 28.086, category: 'metalloid', group: 14, period: 3, electronegativity: 1.90, ionization: 8.152, electronConfig: '[Ne] 3s² 3p²', discovery: 1824, discoverer: 'Jöns Jacob Berzelius' },
        { number: 15, symbol: 'P', name: 'Phosphorus', mass: 30.974, category: 'nonmetal', group: 15, period: 3, electronegativity: 2.19, ionization: 10.487, electronConfig: '[Ne] 3s² 3p³', discovery: 1669, discoverer: 'Hennig Brand' },
        { number: 16, symbol: 'S', name: 'Sulfur', mass: 32.065, category: 'nonmetal', group: 16, period: 3, electronegativity: 2.58, ionization: 10.360, electronConfig: '[Ne] 3s² 3p⁴', discovery: 'Ancient', discoverer: 'Unknown' },
        { number: 17, symbol: 'Cl', name: 'Chlorine', mass: 35.453, category: 'halogen', group: 17, period: 3, electronegativity: 3.16, ionization: 12.968, electronConfig: '[Ne] 3s² 3p⁵', discovery: 1774, discoverer: 'Carl Wilhelm Scheele' },
        { number: 18, symbol: 'Ar', name: 'Argon', mass: 39.948, category: 'noble gas', group: 18, period: 3, electronegativity: null, ionization: 15.760, electronConfig: '[Ne] 3s² 3p⁶', discovery: 1894, discoverer: 'Lord Rayleigh' },
        
        // Period 4 (selected elements)
        { number: 19, symbol: 'K', name: 'Potassium', mass: 39.098, category: 'alkali metal', group: 1, period: 4, electronegativity: 0.82, ionization: 4.341, electronConfig: '[Ar] 4s¹', discovery: 1807, discoverer: 'Humphry Davy' },
        { number: 20, symbol: 'Ca', name: 'Calcium', mass: 40.078, category: 'alkaline earth', group: 2, period: 4, electronegativity: 1.00, ionization: 6.113, electronConfig: '[Ar] 4s²', discovery: 1808, discoverer: 'Humphry Davy' },
        { number: 26, symbol: 'Fe', name: 'Iron', mass: 55.845, category: 'transition', group: 8, period: 4, electronegativity: 1.83, ionization: 7.902, electronConfig: '[Ar] 3d⁶ 4s²', discovery: 'Ancient', discoverer: 'Unknown' },
        { number: 29, symbol: 'Cu', name: 'Copper', mass: 63.546, category: 'transition', group: 11, period: 4, electronegativity: 1.90, ionization: 7.726, electronConfig: '[Ar] 3d¹⁰ 4s¹', discovery: 'Ancient', discoverer: 'Unknown' },
        { number: 30, symbol: 'Zn', name: 'Zinc', mass: 65.38, category: 'transition', group: 12, period: 4, electronegativity: 1.65, ionization: 9.394, electronConfig: '[Ar] 3d¹⁰ 4s²', discovery: 'Ancient', discoverer: 'Unknown' },
        
        // Period 5 (selected elements)
        { number: 47, symbol: 'Ag', name: 'Silver', mass: 107.868, category: 'transition', group: 11, period: 5, electronegativity: 1.93, ionization: 7.576, electronConfig: '[Kr] 4d¹⁰ 5s¹', discovery: 'Ancient', discoverer: 'Unknown' },
        { number: 79, symbol: 'Au', name: 'Gold', mass: 196.967, category: 'transition', group: 11, period: 6, electronegativity: 2.54, ionization: 9.226, electronConfig: '[Xe] 4f¹⁴ 5d¹⁰ 6s¹', discovery: 'Ancient', discoverer: 'Unknown' }
    ];

    // Category colors for visual distinction
    const categoryColors = {
        'alkali metal': 'bg-red-500',
        'alkaline earth': 'bg-orange-500',
        'transition': 'bg-blue-500',
        'post-transition': 'bg-green-500',
        'metalloid': 'bg-yellow-500',
        'nonmetal': 'bg-purple-500',
        'halogen': 'bg-pink-500',
        'noble gas': 'bg-indigo-500'
    };

    // Filter categories
    const filterCategories = {
        'all': 'All Elements',
        'alkali metal': 'Alkali Metals',
        'alkaline earth': 'Alkaline Earth Metals',
        'transition': 'Transition Metals',
        'post-transition': 'Post-Transition Metals',
        'metalloid': 'Metalloids',
        'nonmetal': 'Nonmetals',
        'halogen': 'Halogens',
        'noble gas': 'Noble Gases'
    };

    useEffect(() => {
        const formattedData = {
            type: "periodic_table",
            selectedElement: selectedElement,
            searchTerm: searchTerm,
            filterCategory: filterCategory
        };
        onChange(formattedData);
    }, [selectedElement, searchTerm, filterCategory, onChange]);

    const filteredElements = periodicTable.filter(element => {
        const matchesSearch = element.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                            element.symbol.toLowerCase().includes(searchTerm.toLowerCase()) ||
                            element.number.toString().includes(searchTerm);
        const matchesCategory = filterCategory === 'all' || element.category === filterCategory;
        return matchesSearch && matchesCategory;
    });

    const handleElementClick = (element) => {
        if (isSubmitted) return;
        setSelectedElement(element);
        setShowProperties(true);
    };

    const getCategoryDescription = (category) => {
        const descriptions = {
            'alkali metal': 'Highly reactive metals that readily lose their outer electron to form +1 ions. They are soft, have low melting points, and are excellent conductors of electricity.',
            'alkaline earth': 'Reactive metals that readily lose their two outer electrons to form +2 ions. They are harder and have higher melting points than alkali metals.',
            'transition': 'Metals that have partially filled d orbitals. They exhibit variable oxidation states and often form colored compounds.',
            'post-transition': 'Metals that are softer and have lower melting points than transition metals. They often have multiple oxidation states.',
            'metalloid': 'Elements that have properties intermediate between metals and nonmetals. They are semiconductors and have variable conductivity.',
            'nonmetal': 'Elements that are poor conductors of heat and electricity. They tend to gain electrons in chemical reactions.',
            'halogen': 'Highly reactive nonmetals that readily gain an electron to form -1 ions. They exist as diatomic molecules in their elemental form.',
            'noble gas': 'Unreactive elements with filled electron shells. They rarely participate in chemical reactions and exist as monatomic gases.'
        };
        return descriptions[category] || 'No description available.';
    };

    const getTrends = () => {
        if (!selectedElement) return [];
        
        const trends = [];
        
        // Atomic radius trend
        if (selectedElement.period > 1) {
            trends.push(`Atomic radius decreases across period ${selectedElement.period} due to increasing nuclear charge.`);
        }
        
        // Electronegativity trend
        if (selectedElement.electronegativity) {
            if (selectedElement.group === 1) {
                trends.push('Electronegativity decreases down Group 1 (alkali metals).');
            } else if (selectedElement.group === 17) {
                trends.push('Electronegativity decreases down Group 17 (halogens).');
            }
        }
        
        // Ionization energy trend
        if (selectedElement.ionization) {
            trends.push(`Ionization energy increases across period ${selectedElement.period} due to increasing nuclear charge.`);
        }
        
        return trends;
    };

    const getUses = () => {
        if (!selectedElement) return [];
        
        const uses = {
            'H': ['Fuel for rockets', 'Hydrogenation of oils', 'Production of ammonia'],
            'He': ['Balloons and airships', 'Cryogenic research', 'Welding gas'],
            'Li': ['Lithium-ion batteries', 'Treatment of bipolar disorder', 'Nuclear fusion'],
            'C': ['Diamond and graphite', 'Organic compounds', 'Carbon dating'],
            'O': ['Respiration', 'Combustion', 'Ozone layer'],
            'Fe': ['Steel production', 'Hemoglobin in blood', 'Magnets'],
            'Cu': ['Electrical wiring', 'Coins', 'Antimicrobial surfaces'],
            'Au': ['Jewelry', 'Electronics', 'Dental work']
        };
        
        return uses[selectedElement.symbol] || ['Various industrial applications', 'Research and development', 'Specialized uses'];
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Interactive Periodic Table</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowProperties(!showProperties)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showProperties 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showProperties ? 'Hide Properties' : 'Show Properties'}
                    </button>
                    <button
                        onClick={() => setShowTrends(!showTrends)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showTrends 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showTrends ? 'Hide Trends' : 'Show Trends'}
                    </button>
                </div>
            </div>

            {/* Search and Filter Controls */}
            <div className="mb-6 grid grid-cols-1 md:grid-cols-2 gap-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Search Elements:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={searchTerm} 
                        onChange={(e) => !isSubmitted && setSearchTerm(e.target.value)} 
                        placeholder="Search by name, symbol, or number..." 
                        disabled={isSubmitted} 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Filter by Category:</label>
                    <select 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={filterCategory} 
                        onChange={(e) => !isSubmitted && setFilterCategory(e.target.value)} 
                        disabled={isSubmitted}
                    >
                        {Object.entries(filterCategories).map(([key, value]) => (
                            <option key={key} value={key}>{value}</option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Periodic Table Grid */}
            <div className="mb-6">
                <div className="grid grid-cols-18 gap-1 max-w-6xl mx-auto">
                    {filteredElements.map((element) => (
                        <div
                            key={element.number}
                            onClick={() => handleElementClick(element)}
                            className={`
                                relative p-2 text-center cursor-pointer transition-all duration-200 hover:scale-110 hover:shadow-lg
                                ${categoryColors[element.category] || 'bg-gray-400'}
                                ${selectedElement?.number === element.number ? 'ring-4 ring-yellow-400' : ''}
                                ${isSubmitted ? 'cursor-default' : ''}
                            `}
                            style={{
                                gridColumn: element.group,
                                gridRow: element.period
                            }}
                        >
                            <div className="text-xs font-bold text-white">{element.number}</div>
                            <div className="text-lg font-bold text-white">{element.symbol}</div>
                            <div className="text-xs text-white">{element.name}</div>
                            <div className="text-xs text-white">{element.mass}</div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Element Properties Panel */}
            {showProperties && selectedElement && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-lg font-medium text-blue-800 mb-3">
                        {selectedElement.name} ({selectedElement.symbol})
                    </h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div>
                            <h5 className="font-medium text-blue-700 mb-2">Basic Properties:</h5>
                            <div className="space-y-1 text-sm text-blue-600">
                                <div><strong>Atomic Number:</strong> {selectedElement.number}</div>
                                <div><strong>Atomic Mass:</strong> {selectedElement.mass} u</div>
                                <div><strong>Category:</strong> {filterCategories[selectedElement.category]}</div>
                                <div><strong>Group:</strong> {selectedElement.group}</div>
                                <div><strong>Period:</strong> {selectedElement.period}</div>
                                {selectedElement.electronegativity && (
                                    <div><strong>Electronegativity:</strong> {selectedElement.electronegativity}</div>
                                )}
                                <div><strong>Ionization Energy:</strong> {selectedElement.ionization} eV</div>
                            </div>
                        </div>
                        <div>
                            <h5 className="font-medium text-blue-700 mb-2">Electronic Configuration:</h5>
                            <div className="space-y-1 text-sm text-blue-600">
                                <div><strong>Configuration:</strong> {selectedElement.electronConfig}</div>
                                <div><strong>Discovery:</strong> {selectedElement.discovery}</div>
                                {selectedElement.discoverer !== 'Unknown' && (
                                    <div><strong>Discoverer:</strong> {selectedElement.discoverer}</div>
                                )}
                            </div>
                        </div>
                    </div>
                    
                    {/* Category Description */}
                    <div className="mt-4">
                        <h5 className="font-medium text-blue-700 mb-2">Category Description:</h5>
                        <p className="text-sm text-blue-600">{getCategoryDescription(selectedElement.category)}</p>
                    </div>

                    {/* Common Uses */}
                    <div className="mt-4">
                        <h5 className="font-medium text-blue-700 mb-2">Common Uses:</h5>
                        <ul className="text-sm text-blue-600 list-disc list-inside">
                            {getUses().map((use, index) => (
                                <li key={index}>{use}</li>
                            ))}
                        </ul>
                    </div>
                </div>
            )}

            {/* Periodic Trends */}
            {showTrends && selectedElement && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Periodic Trends for {selectedElement.name}:</h4>
                    <div className="space-y-2">
                        {getTrends().map((trend, index) => (
                            <div key={index} className="text-sm text-green-700">• {trend}</div>
                        ))}
                        {getTrends().length === 0 && (
                            <div className="text-sm text-green-700">No specific trends available for this element.</div>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Click on any element to view its detailed properties</li>
                    <li>• Use the search bar to find elements by name, symbol, or number</li>
                    <li>• Filter elements by category to explore specific groups</li>
                    <li>• Observe periodic trends across periods and down groups</li>
                    <li>• Each element is color-coded by its chemical category</li>
                </ul>
            </div>
        </div>
    );
};

export default PeriodicTableInteractive;
