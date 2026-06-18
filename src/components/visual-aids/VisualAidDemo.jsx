import React, { useState } from 'react';
import VisualAidFactory from './VisualAidFactory';

/**
 * Centralized Visual Aid System Demo
 * Demonstrates the modular, subject-agnostic visual aid system
 */
const VisualAidDemo = () => {
    const [selectedType, setSelectedType] = useState('linear-function');
    const [selectedSubject, setSelectedSubject] = useState('Mathematics');
    const [mode, setMode] = useState('user-interactive');
    const [customSpec, setCustomSpec] = useState('');
    const [currentVisualAid, setCurrentVisualAid] = useState(null);

    // Get available types organized by subject
    const availableTypes = VisualAidFactory.getAvailableTypes();

    // Handle visual aid creation
    const createVisualAid = (type = selectedType) => {
        const visualAid = VisualAidFactory.createWithDefaults(
            type, 
            {}, 
            mode, 
            handleVisualAidChange
        );
        setCurrentVisualAid(visualAid);
    };

    // Handle custom specification
    const createFromCustomSpec = () => {
        if (!customSpec.trim()) return;
        
        const visualAid = VisualAidFactory.createVisualAid(
            customSpec,
            {},
            mode,
            handleVisualAidChange
        );
        setCurrentVisualAid(visualAid);
    };

    // Handle visual aid data changes
    const handleVisualAidChange = (newData) => {
        console.log('Visual aid data changed:', newData);
        // In a real app, you might want to save this data or send it somewhere
    };

    // Handle subject change
    const handleSubjectChange = (subject) => {
        setSelectedSubject(subject);
        const firstType = availableTypes[subject][0];
        setSelectedType(firstType);
        createVisualAid(firstType);
    };

    // Handle type change
    const handleTypeChange = (type) => {
        setSelectedType(type);
        createVisualAid(type);
    };

    // Create initial visual aid
    React.useEffect(() => {
        createVisualAid();
    }, []);

    return (
        <div className="visual-aid-demo min-h-screen bg-gray-50 p-6">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <div className="text-center mb-8">
                    <h1 className="text-4xl font-bold text-gray-800 mb-4">
                        🎯 Centralized Visual Aid System
                    </h1>
                    <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                        A modular, subject-agnostic system for creating interactive visual aids 
                        across mathematics, accounting, physics, chemistry, and more.
                    </p>
                </div>

                {/* Control Panel */}
                <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
                    <h2 className="text-2xl font-bold text-gray-800 mb-6">Control Panel</h2>
                    
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {/* Subject Selection */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Subject Area
                            </label>
                            <select
                                value={selectedSubject}
                                onChange={(e) => handleSubjectChange(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            >
                                {Object.keys(availableTypes).map(subject => (
                                    <option key={subject} value={subject}>
                                        {subject}
                                    </option>
                                ))}
                            </select>
                        </div>

                        {/* Visual Aid Type Selection */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Visual Aid Type
                            </label>
                            <select
                                value={selectedType}
                                onChange={(e) => handleTypeChange(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            >
                                {availableTypes[selectedSubject].map(type => (
                                    <option key={type} value={type}>
                                        {type.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                                    </option>
                                ))}
                            </select>
                        </div>

                        {/* Mode Selection */}
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">
                                Display Mode
                            </label>
                            <select
                                value={mode}
                                onChange={(e) => setMode(e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            >
                                <option value="user-interactive">User Interactive</option>
                                <option value="ai-generated">AI Generated</option>
                                <option value="read-only">Read Only</option>
                            </select>
                        </div>
                    </div>

                    {/* Custom Specification */}
                    <div className="mt-6">
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Custom Specification (JSON or simple format)
                        </label>
                        <div className="flex gap-2">
                            <input
                                type="text"
                                value={customSpec}
                                onChange={(e) => setCustomSpec(e.target.value)}
                                placeholder="e.g., linear-function:m=2,c=3 or JSON specification"
                                className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            />
                            <button
                                onClick={createFromCustomSpec}
                                className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 focus:ring-2 focus:ring-blue-500"
                            >
                                Create
                            </button>
                        </div>
                        <p className="text-xs text-gray-500 mt-1">
                            Examples: "linear-function:m=2,c=3", "balance-sheet", or full JSON
                        </p>
                    </div>
                </div>

                {/* Visual Aid Display */}
                <div className="bg-white rounded-lg shadow-lg p-6">
                    <div className="flex justify-between items-center mb-6">
                        <h2 className="text-2xl font-bold text-gray-800">
                            {selectedSubject}: {selectedType.replace('-', ' ').replace(/\b\w/g, l => l.toUpperCase())}
                        </h2>
                        <button
                            onClick={() => createVisualAid()}
                            className="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 focus:ring-2 focus:ring-green-500"
                        >
                            Refresh
                        </button>
                    </div>

                    {/* Current Visual Aid */}
                    <div className="min-h-96">
                        {currentVisualAid ? (
                            <div className="visual-aid-container">
                                {currentVisualAid}
                            </div>
                        ) : (
                            <div className="text-center text-gray-500 py-20">
                                <div className="text-4xl mb-4">🎨</div>
                                <div>Select a visual aid type to get started</div>
                            </div>
                        )}
                    </div>
                </div>

                {/* System Information */}
                <div className="bg-white rounded-lg shadow-lg p-6 mt-8">
                    <h2 className="text-2xl font-bold text-gray-800 mb-6">System Information</h2>
                    
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Available Types */}
                        <div>
                            <h3 className="text-lg font-semibold text-gray-700 mb-3">Available Visual Aid Types</h3>
                            {Object.entries(availableTypes).map(([subject, types]) => (
                                <div key={subject} className="mb-4">
                                    <h4 className="font-medium text-gray-600 mb-2">{subject}</h4>
                                    <div className="flex flex-wrap gap-2">
                                        {types.map(type => (
                                            <span
                                                key={type}
                                                className="px-2 py-1 bg-blue-100 text-blue-800 text-xs rounded-full cursor-pointer hover:bg-blue-200"
                                                onClick={() => handleTypeChange(type)}
                                            >
                                                {type.replace('-', ' ')}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/* System Features */}
                        <div>
                            <h3 className="text-lg font-semibold text-gray-700 mb-3">System Features</h3>
                            <ul className="space-y-2 text-sm text-gray-600">
                                <li>✅ <strong>Modular Design:</strong> Easy to add new subject areas</li>
                                <li>✅ <strong>Subject Agnostic:</strong> Works across all disciplines</li>
                                <li>✅ <strong>Flexible Modes:</strong> AI-generated, user-interactive, read-only</li>
                                <li>✅ <strong>Specification Parsing:</strong> JSON and simple text formats</li>
                                <li>✅ <strong>Error Handling:</strong> Graceful fallbacks for invalid specs</li>
                                <li>✅ <strong>Default Data:</strong> Pre-configured examples for each type</li>
                                <li>✅ <strong>Validation:</strong> Built-in specification validation</li>
                                <li>✅ <strong>Extensible:</strong> Easy to add new visual aid types</li>
                            </ul>
                        </div>
                    </div>
                </div>

                {/* Migration Path */}
                <div className="bg-blue-50 rounded-lg p-6 mt-8">
                    <h2 className="text-2xl font-bold text-blue-800 mb-4">🚀 Future Migration Path</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h3 className="text-lg font-semibold text-blue-700 mb-3">Current: Frontend-Centric</h3>
                            <ul className="space-y-2 text-sm text-blue-600">
                                <li>• All components in React frontend</li>
                                <li>• Client-side rendering and interaction</li>
                                <li>• Easy to develop and test</li>
                                <li>• Good for prototyping and small-scale use</li>
                            </ul>
                        </div>
                        <div>
                            <h3 className="text-lg font-semibold text-blue-700 mb-3">Future: Backend-Centric</h3>
                            <ul className="space-y-2 text-sm text-blue-600">
                                <li>• Move specification parsing to backend</li>
                                <li>• Server-side validation and processing</li>
                                <li>• Better for large-scale deployments</li>
                                <li>• Integration with AI services</li>
                            </ul>
                        </div>
                    </div>
                    <div className="mt-4 text-center">
                        <p className="text-blue-700 font-medium">
                            The current architecture makes future backend migration seamless!
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default VisualAidDemo;
