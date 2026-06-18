import React, { useState } from 'react';

const ChemistryComponentsRepository = ({ isVisible, onComponentSelect, selectedSubject, selectedGrade }) => {
    const [selectedCategory, setSelectedCategory] = useState('all');

    // Don't render if not visible
    if (!isVisible) {
        return null;
    }

    const chemistryComponents = {
        'fundamentals': {
            name: 'Fundamental Chemistry',
            description: 'Core concepts and calculations',
            components: [
                {
                    id: 'chemical_equation_balancer',
                    name: 'Chemical Equation Balancer',
                    description: 'Interactive equation balancing with step-by-step solutions',
                    features: ['Multiple equation types', 'Atom counting', 'Balancing algorithms', 'Step-by-step guidance'],
                    difficulty: 'Beginner to Intermediate'
                },
                {
                    id: 'mole_calculator',
                    name: 'Mole Calculator',
                    description: 'Molar mass, concentration, stoichiometry calculations',
                    features: ['Molar mass calculation', 'Mass-mole conversions', 'Concentration calculations', 'Stoichiometry'],
                    difficulty: 'Beginner to Intermediate'
                }
            ]
        },
        'periodic_table': {
            name: 'Periodic Table & Elements',
            description: 'Element properties and periodic trends',
            components: [
                {
                    id: 'periodic_table_interactive',
                    name: 'Interactive Periodic Table',
                    description: 'Interactive periodic table with element properties',
                    features: ['Element search', 'Category filtering', 'Property details', 'Periodic trends'],
                    difficulty: 'Beginner'
                }
            ]
        },
        'bonding': {
            name: 'Chemical Bonding',
            description: 'Molecular structure and bonding theories',
            components: [
                {
                    id: 'chemical_bonding_visualizer',
                    name: 'Chemical Bonding Visualizer',
                    description: 'Lewis structures, molecular geometry, VSEPR theory',
                    features: ['Lewis structures', 'Molecular geometry', 'VSEPR analysis', 'Hybridization'],
                    difficulty: 'Intermediate'
                }
            ]
        },
        'reactions': {
            name: 'Chemical Reactions',
            description: 'Reaction mechanisms and kinetics',
            components: [
                {
                    id: 'reaction_rate_simulator',
                    name: 'Reaction Rate Simulator',
                    description: 'Temperature, concentration, catalyst effects on reaction rates',
                    features: ['Rate law simulation', 'Temperature effects', 'Catalyst analysis', 'Concentration impact'],
                    difficulty: 'Intermediate to Advanced'
                },
                {
                    id: 'acid_base_titration',
                    name: 'Acid-Base Titration',
                    description: 'pH curves, equivalence points, buffer solutions',
                    features: ['pH curve plotting', 'Equivalence point detection', 'Buffer calculations', 'Indicator selection'],
                    difficulty: 'Intermediate'
                }
            ]
        },
        'electrochemistry': {
            name: 'Electrochemistry',
            description: 'Redox reactions and electrochemical cells',
            components: [
                {
                    id: 'electrochemistry_simulator',
                    name: 'Electrochemistry Simulator',
                    description: 'Galvanic cells, electrolysis, standard potentials',
                    features: ['Cell potential calculation', 'Redox reactions', 'Electrolysis simulation', 'Nernst equation'],
                    difficulty: 'Advanced'
                }
            ]
        }
    };

    const handleComponentSelect = (componentId) => {
        if (onComponentSelect) {
            onComponentSelect(componentId);
        }
    };

    const getDifficultyColor = (difficulty) => {
        const colors = {
            'Beginner': 'bg-green-100 text-green-800',
            'Intermediate': 'bg-yellow-100 text-yellow-800',
            'Advanced': 'bg-red-100 text-red-800'
        };
        return colors[difficulty] || 'bg-gray-100 text-gray-700';
    };

    const filteredCategories = selectedCategory === 'all' 
        ? Object.keys(chemistryComponents)
        : [selectedCategory];

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-800 mb-2">Chemistry Components Repository</h3>
                <p className="text-sm text-gray-600">
                    Explore our comprehensive collection of chemistry learning tools and simulations.
                </p>
            </div>

            {/* Category Filter */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Filter by Category:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={selectedCategory} 
                    onChange={(e) => setSelectedCategory(e.target.value)}
                >
                    <option value="all">All Categories</option>
                    {Object.entries(chemistryComponents).map(([key, category]) => (
                        <option key={key} value={key}>{category.name}</option>
                    ))}
                </select>
            </div>

            {/* Components Grid */}
            <div className="space-y-6">
                {filteredCategories.map(categoryKey => {
                    const category = chemistryComponents[categoryKey];
                    return (
                        <div key={categoryKey} className="border border-gray-200 rounded-lg p-4">
                            <div className="mb-4">
                                <h4 className="text-md font-semibold text-gray-800 mb-1">{category.name}</h4>
                                <p className="text-sm text-gray-600">{category.description}</p>
                            </div>
                            
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {category.components.map(component => (
                                    <div 
                                        key={component.id}
                                        className="border border-gray-200 rounded-lg p-4 hover:border-blue-300 hover:shadow-md transition-all cursor-pointer"
                                        onClick={() => handleComponentSelect(component.id)}
                                    >
                                        <div className="flex items-start justify-between mb-3">
                                            <h5 className="font-medium text-gray-800">{component.name}</h5>
                                            <span className={`px-2 py-1 rounded-full text-xs font-medium ${getDifficultyColor(component.difficulty)}`}>
                                                {component.difficulty}
                                            </span>
                                        </div>
                                        
                                        <p className="text-sm text-gray-600 mb-3">{component.description}</p>
                                        
                                        <div className="mb-3">
                                            <h6 className="text-xs font-medium text-gray-700 mb-2">Key Features:</h6>
                                            <ul className="text-xs text-gray-600 space-y-1">
                                                {component.features.map((feature, index) => (
                                                    <li key={index} className="flex items-center">
                                                        <span className="w-1.5 h-1.5 bg-blue-400 rounded-full mr-2"></span>
                                                        {feature}
                                                    </li>
                                                ))}
                                            </ul>
                                        </div>
                                        
                                        <div className="text-xs text-blue-600 font-medium hover:text-blue-800 transition-colors">
                                            Click to explore →
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    );
                })}
            </div>

            {/* Learning Paths */}
            <div className="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <h4 className="text-md font-medium text-blue-800 mb-3">Suggested Learning Paths:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Beginner Path:</h5>
                        <div className="text-sm text-gray-600 space-y-1">
                            <div>1. Interactive Periodic Table</div>
                            <div>2. Chemical Equation Balancer</div>
                            <div>3. Mole Calculator</div>
                        </div>
                    </div>
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Intermediate Path:</h5>
                        <div className="text-sm text-gray-600 space-y-1">
                            <div>1. Chemical Bonding Visualizer</div>
                            <div>2. Acid-Base Titration</div>
                            <div>3. Reaction Rate Simulator</div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Start with fundamental concepts before moving to advanced topics</li>
                    <li>• Use the Interactive Periodic Table to understand element properties</li>
                    <li>• Practice equation balancing with the Chemical Equation Balancer</li>
                    <li>• Explore molecular geometry with the Chemical Bonding Visualizer</li>
                    <li>• Each component includes step-by-step guidance and explanations</li>
                </ul>
            </div>
        </div>
    );
};

export default ChemistryComponentsRepository;
