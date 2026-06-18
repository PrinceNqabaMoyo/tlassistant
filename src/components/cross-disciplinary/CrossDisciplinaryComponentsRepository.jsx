import React, { useState } from 'react';

const CrossDisciplinaryComponentsRepository = ({ isVisible, onComponentSelect, selectedSubject, selectedGrade }) => {
    const [selectedCategory, setSelectedCategory] = useState('all');

    // Don't render if not visible
    if (!isVisible) {
        return null;
    }

    const crossDisciplinaryComponents = {
        'mathematics': {
            name: 'Mathematical Tools',
            description: 'Scientific notation, unit conversions, and mathematical analysis',
            components: [
                {
                    id: 'scientific_notation_converter',
                    name: 'Scientific Notation Converter',
                    description: 'Convert between standard form, scientific notation, and engineering notation',
                    features: ['Scientific notation', 'Engineering notation', 'Unit conversions', 'Significant figures'],
                    difficulty: 'Intermediate',
                    category: 'mathematics'
                }
            ]
        },
        'data_analysis': {
            name: 'Data Analysis',
            description: 'Statistical analysis, trend fitting, and data visualization',
            components: [
                {
                    id: 'data_analysis_tools',
                    name: 'Data Analysis Tools',
                    description: 'Linear regression, polynomial fitting, and statistical analysis',
                    features: ['Linear regression', 'Polynomial fitting', 'Exponential fitting', 'Error analysis'],
                    difficulty: 'Advanced',
                    category: 'data_analysis'
                }
            ]
        },
        'academic_writing': {
            name: 'Academic Writing',
            description: 'Lab reports, scientific writing, and documentation tools',
            components: [
                {
                    id: 'lab_report_builder',
                    name: 'Lab Report Builder',
                    description: 'Structured lab report templates with data tables',
                    features: ['Report templates', 'Section organization', 'Data integration', 'Formatting'],
                    difficulty: 'Beginner',
                    category: 'academic_writing'
                }
            ]
        }
    };

    const allComponents = Object.values(crossDisciplinaryComponents).flatMap(category => 
        category.components
    );

    const filteredComponents = selectedCategory === 'all' 
        ? allComponents 
        : crossDisciplinaryComponents[selectedCategory]?.components || [];

    const handleComponentSelect = (componentId) => {
        if (onComponentSelect) {
            onComponentSelect(componentId);
        }
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm">
            <div className="mb-6">
                <h2 className="text-2xl font-bold text-gray-800 mb-2">Cross-Disciplinary Components Repository</h2>
                <p className="text-gray-600">
                    Explore and select from our comprehensive collection of cross-disciplinary tools and utilities.
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
                    {Object.entries(crossDisciplinaryComponents).map(([key, category]) => (
                        <option key={key} value={key}>{category.name}</option>
                    ))}
                </select>
            </div>

            {/* Components Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredComponents.map((component) => (
                    <div key={component.id} className="bg-gray-50 rounded-lg border border-gray-200 p-4 hover:shadow-md transition-shadow">
                        <div className="mb-3">
                            <h3 className="text-lg font-semibold text-gray-800 mb-2">{component.name}</h3>
                            <p className="text-sm text-gray-600 mb-3">{component.description}</p>
                            
                            <div className="mb-3">
                                <span className={`inline-block px-2 py-1 text-xs font-medium rounded-full ${
                                    component.difficulty === 'Beginner' ? 'bg-green-100 text-green-800' :
                                    component.difficulty === 'Intermediate' ? 'bg-yellow-100 text-yellow-800' :
                                    'bg-red-100 text-red-800'
                                }`}>
                                    {component.difficulty}
                                </span>
                                <span className="inline-block ml-2 px-2 py-1 text-xs font-medium bg-blue-100 text-blue-800 rounded-full">
                                    {component.category}
                                </span>
                            </div>
                        </div>

                        <div className="mb-4">
                            <h4 className="text-sm font-medium text-gray-700 mb-2">Key Features:</h4>
                            <ul className="text-sm text-gray-600 space-y-1">
                                {component.features.map((feature, index) => (
                                    <li key={index} className="flex items-center">
                                        <span className="text-green-500 mr-2">•</span>
                                        {feature}
                                    </li>
                                ))}
                            </ul>
                        </div>

                        <button
                            onClick={() => handleComponentSelect(component.id)}
                            className="w-full px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors"
                        >
                            Select Component
                        </button>
                    </div>
                ))}
            </div>

            {/* Statistics */}
            <div className="mt-8 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <h3 className="text-lg font-semibold text-blue-800 mb-3">Repository Statistics</h3>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{allComponents.length}</div>
                        <div className="text-sm text-blue-700">Total Components</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{Object.keys(crossDisciplinaryComponents).length}</div>
                        <div className="text-sm text-blue-700">Categories</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">
                            {allComponents.filter(c => c.difficulty === 'Beginner').length}
                        </div>
                        <div className="text-sm text-blue-700">Beginner Level</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">
                            {allComponents.filter(c => c.difficulty === 'Advanced').length}
                        </div>
                        <div className="text-sm text-blue-700">Advanced Level</div>
                    </div>
                </div>
            </div>

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 How to Use:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Browse components by category or view all at once</li>
                    <li>• Each component includes detailed descriptions and key features</li>
                    <li>• Difficulty levels help you choose appropriate tools</li>
                    <li>• Click "Select Component" to integrate into your project</li>
                    <li>• Components are designed for educational and research applications</li>
                </ul>
            </div>
        </div>
    );
};

export default CrossDisciplinaryComponentsRepository;
