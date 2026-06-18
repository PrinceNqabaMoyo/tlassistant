import React, { useState, useEffect } from 'react';

const ProbabilitySimulator = ({ initialData, onChange, isSubmitted }) => {
    const [simData, setSimData] = useState(initialData || {
        title: "Probability Simulator",
        experimentType: 'coin_flip',
        numberOfTrials: 100,
        customOutcomes: [],
        customProbabilities: [],
        results: [],
        showHistory: true,
        showChart: true,
        autoRun: false
    });

    const [isRunning, setIsRunning] = useState(false);
    const [currentTrial, setCurrentTrial] = useState(0);

    useEffect(() => {
        // Ensure all required properties are initialized
        if (!simData.results) {
            setSimData(prev => ({ ...prev, results: [] }));
            return;
        }
        if (!simData.customOutcomes) {
            setSimData(prev => ({ ...prev, customOutcomes: [] }));
            return;
        }
        if (!simData.customProbabilities) {
            setSimData(prev => ({ ...prev, customProbabilities: [] }));
            return;
        }
        
        onChange(simData);
    }, [simData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setSimData(prev => ({ ...prev, [field]: value }));
    };

    const predefinedExperiments = {
        coin_flip: {
            name: 'Coin Flip',
            outcomes: ['Heads', 'Tails'],
            probabilities: [0.5, 0.5],
            description: 'Simulate flipping a fair coin'
        },
        dice_roll: {
            name: 'Dice Roll',
            outcomes: ['1', '2', '3', '4', '5', '6'],
            probabilities: [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],
            description: 'Simulate rolling a fair 6-sided die'
        },
        two_dice: {
            name: 'Two Dice Sum',
            outcomes: ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'],
            probabilities: [1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36],
            description: 'Simulate the sum of two dice'
        },
        card_draw: {
            name: 'Card Draw',
            outcomes: ['Hearts', 'Diamonds', 'Clubs', 'Spades'],
            probabilities: [0.25, 0.25, 0.25, 0.25],
            description: 'Simulate drawing a card from a deck'
        },
        spinner: {
            name: 'Spinner',
            outcomes: ['Red', 'Blue', 'Green', 'Yellow'],
            probabilities: [0.3, 0.2, 0.25, 0.25],
            description: 'Simulate spinning a 4-color spinner'
        },
        custom: {
            name: 'Custom Experiment',
            outcomes: simData.customOutcomes,
            probabilities: simData.customProbabilities,
            description: 'Define your own outcomes and probabilities'
        }
    };

    const addCustomOutcome = () => {
        if (isSubmitted) return;
        const newOutcome = `Outcome ${(simData.customOutcomes || []).length + 1}`;
        const newProbability = 1 / ((simData.customOutcomes || []).length + 1);
        
        setSimData(prev => ({
            ...prev,
            customOutcomes: [...(prev.customOutcomes || []), newOutcome],
            customProbabilities: [...(prev.customProbabilities || []), newProbability]
        }));
    };

    const updateCustomOutcome = (index, field, value) => {
        if (isSubmitted) return;
        if (field === 'outcome') {
            setSimData(prev => ({
                ...prev,
                customOutcomes: (prev.customOutcomes || []).map((outcome, i) => 
                    i === index ? value : outcome
                )
            }));
        } else if (field === 'probability') {
            setSimData(prev => ({
                ...prev,
                customProbabilities: (prev.customProbabilities || []).map((prob, i) => 
                    i === index ? parseFloat(value) || 0 : prob
                )
            }));
        }
    };

    const removeCustomOutcome = (index) => {
        if (isSubmitted) return;
        setSimData(prev => ({
            ...prev,
            customOutcomes: prev.customOutcomes.filter((_, i) => i !== index),
            customProbabilities: prev.customProbabilities.filter((_, i) => i !== index)
        }));
    };

    const normalizeProbabilities = (probabilities) => {
        const sum = probabilities.reduce((acc, prob) => acc + prob, 0);
        if (sum === 0) return probabilities;
        return probabilities.map(prob => prob / sum);
    };

    const generateRandomOutcome = (outcomes, probabilities) => {
        const normalizedProbs = normalizeProbabilities(probabilities);
        const random = Math.random();
        let cumulative = 0;
        
        for (let i = 0; i < normalizedProbs.length; i++) {
            cumulative += normalizedProbs[i];
            if (random <= cumulative) {
                return outcomes[i];
            }
        }
        return outcomes[outcomes.length - 1];
    };

    const runSingleTrial = () => {
        if (isSubmitted) return;
        
        const experiment = predefinedExperiments[simData.experimentType];
        const outcome = generateRandomOutcome(experiment.outcomes, experiment.probabilities);
        
        setSimData(prev => ({
            ...prev,
            results: [...prev.results, {
                trial: prev.results.length + 1,
                outcome,
                timestamp: new Date().toLocaleTimeString()
            }]
        }));
    };

    const runMultipleTrials = async () => {
        if (isSubmitted || isRunning) return;
        
        setIsRunning(true);
        const experiment = predefinedExperiments[simData.experimentType];
        const newResults = [];
        
        for (let i = 0; i < simData.numberOfTrials; i++) {
            const outcome = generateRandomOutcome(experiment.outcomes, experiment.probabilities);
            newResults.push({
                trial: simData.results.length + i + 1,
                outcome,
                timestamp: new Date().toLocaleTimeString()
            });
            
            // Add small delay for visual effect
            if (simData.autoRun) {
                await new Promise(resolve => setTimeout(resolve, 50));
                setCurrentTrial(i + 1);
            }
        }
        
        setSimData(prev => ({
            ...prev,
            results: [...prev.results, ...newResults]
        }));
        
        setIsRunning(false);
        setCurrentTrial(0);
    };

    const clearResults = () => {
        if (isSubmitted) return;
        setSimData(prev => ({ ...prev, results: [] }));
    };

    const getOutcomeCounts = () => {
        const experiment = predefinedExperiments[simData.experimentType];
        const counts = {};
        
        experiment.outcomes.forEach(outcome => {
            counts[outcome] = 0;
        });
        
        simData.results.forEach(result => {
            counts[result.outcome] = (counts[result.outcome] || 0) + 1;
        });
        
        return counts;
    };

    const getOutcomeProbabilities = () => {
        const counts = getOutcomeCounts();
        const total = simData.results.length;
        const probabilities = {};
        
        Object.keys(counts).forEach(outcome => {
            probabilities[outcome] = total > 0 ? counts[outcome] / total : 0;
        });
        
        return probabilities;
    };

    const getExpectedProbabilities = () => {
        const experiment = predefinedExperiments[simData.experimentType];
        return experiment.probabilities;
    };

    const calculateChiSquare = () => {
        const observed = getOutcomeCounts();
        const expected = getExpectedProbabilities();
        const total = simData.results.length;
        
        let chiSquare = 0;
        Object.keys(observed).forEach((outcome, index) => {
            const expectedCount = expected[index] * total;
            const observedCount = observed[outcome];
            if (expectedCount > 0) {
                chiSquare += Math.pow(observedCount - expectedCount, 2) / expectedCount;
            }
        });
        
        return chiSquare;
    };

    const renderChart = () => {
        const experiment = predefinedExperiments[simData.experimentType];
        const counts = getOutcomeCounts();
        const maxCount = Math.max(...Object.values(counts));
        
        return (
            <div className="space-y-2">
                {experiment.outcomes.map((outcome, index) => {
                    const count = counts[outcome] || 0;
                    const percentage = simData.results.length > 0 ? (count / simData.results.length * 100) : 0;
                    const barWidth = maxCount > 0 ? (count / maxCount * 100) : 0;
                    
                    return (
                        <div key={outcome} className="flex items-center space-x-2">
                            <div className="w-20 text-sm font-medium text-gray-700">{outcome}:</div>
                            <div className="flex-1 bg-gray-200 rounded-full h-4">
                                <div 
                                    className="bg-blue-500 h-4 rounded-full transition-all duration-300"
                                    style={{ width: `${barWidth}%` }}
                                />
                            </div>
                            <div className="w-16 text-sm text-gray-600 text-right">
                                {count} ({percentage.toFixed(1)}%)
                            </div>
                        </div>
                    );
                })}
            </div>
        );
    };

    const renderResultsTable = () => {
        const experiment = predefinedExperiments[simData.experimentType];
        const counts = getOutcomeCounts();
        const observedProbs = getOutcomeProbabilities();
        const expectedProbs = getExpectedProbabilities();
        
        return (
            <div className="overflow-x-auto">
                <table className="min-w-full bg-white border border-gray-300">
                    <thead>
                        <tr className="bg-gray-50">
                            <th className="px-4 py-2 border-b text-left text-sm font-medium text-gray-700">Outcome</th>
                            <th className="px-4 py-2 border-b text-center text-sm font-medium text-gray-700">Count</th>
                            <th className="px-4 py-2 border-b text-center text-sm font-medium text-gray-700">Observed P</th>
                            <th className="px-4 py-2 border-b text-center text-sm font-medium text-gray-700">Expected P</th>
                            <th className="px-4 py-2 border-b text-center text-sm font-medium text-gray-700">Difference</th>
                        </tr>
                    </thead>
                    <tbody>
                        {experiment.outcomes.map((outcome, index) => {
                            const count = counts[outcome] || 0;
                            const observed = observedProbs[outcome] || 0;
                            const expected = expectedProbs[index] || 0;
                            const difference = observed - expected;
                            
                            return (
                                <tr key={outcome} className="border-b">
                                    <td className="px-4 py-2 text-sm text-gray-700">{outcome}</td>
                                    <td className="px-4 py-2 text-sm text-center text-gray-700">{count}</td>
                                    <td className="px-4 py-2 text-sm text-center text-gray-700">{(observed * 100).toFixed(1)}%</td>
                                    <td className="px-4 py-2 text-sm text-center text-gray-700">{(expected * 100).toFixed(1)}%</td>
                                    <td className={`px-4 py-2 text-sm text-center ${difference > 0 ? 'text-green-600' : 'text-red-600'}`}>
                                        {(difference * 100).toFixed(1)}%
                                    </td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>
        );
    };

    // Don't render if not properly initialized
    if (!simData.results || !simData.customOutcomes || !simData.customProbabilities) {
        return (
            <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
                <h3 className="font-semibold text-gray-700 mb-4">Probability Simulator</h3>
                <div className="text-center py-8 text-gray-500">
                    <p>Loading probability simulator configuration...</p>
                </div>
            </div>
        );
    }

    return (
        <div className="p-4 bg-gray-50 border border-gray-300 rounded-lg mt-4">
            <h3 className="font-semibold text-gray-700 mb-4">Probability Simulator</h3>
            
            {/* Configuration Section */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Title:</label>
                    <input
                        type="text"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={simData.title}
                        onChange={(e) => handleFieldChange('title', e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Probability Experiment Title"
                    />
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Experiment Type:</label>
                    <select
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={simData.experimentType}
                        onChange={(e) => handleFieldChange('experimentType', e.target.value)}
                        disabled={isSubmitted}
                    >
                        <option value="coin_flip">Coin Flip</option>
                        <option value="dice_roll">Dice Roll</option>
                        <option value="two_dice">Two Dice Sum</option>
                        <option value="card_draw">Card Draw</option>
                        <option value="spinner">Spinner</option>
                        <option value="custom">Custom Experiment</option>
                    </select>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">Number of Trials:</label>
                    <input
                        type="number"
                        className="w-full p-2 border border-gray-300 rounded-md text-sm"
                        value={simData.numberOfTrials}
                        onChange={(e) => handleFieldChange('numberOfTrials', parseInt(e.target.value) || 100)}
                        disabled={isSubmitted}
                        min="1"
                        max="10000"
                    />
                </div>
            </div>

            {/* Custom Experiment Configuration */}
            {simData.experimentType === 'custom' && (
                <div className="mb-4 p-4 bg-white border border-gray-200 rounded-lg">
                    <h4 className="font-semibold text-gray-700 mb-3">Custom Experiment Setup</h4>
                    
                    <div className="space-y-3">
                        {simData.customOutcomes.map((outcome, index) => (
                            <div key={index} className="flex items-center space-x-2">
                                <input
                                    type="text"
                                    className="flex-1 p-2 border border-gray-300 rounded-md text-sm"
                                    value={outcome}
                                    onChange={(e) => updateCustomOutcome(index, 'outcome', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Outcome name"
                                />
                                <input
                                    type="number"
                                    className="w-24 p-2 border border-gray-300 rounded-md text-sm"
                                    value={simData.customProbabilities[index]}
                                    onChange={(e) => updateCustomOutcome(index, 'probability', e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="0.5"
                                    step="0.01"
                                    min="0"
                                    max="1"
                                />
                                {!isSubmitted && (
                                    <button
                                        onClick={() => removeCustomOutcome(index)}
                                        className="px-3 py-2 bg-red-500 text-white rounded-md text-sm hover:bg-red-600"
                                    >
                                        Remove
                                    </button>
                                )}
                            </div>
                        ))}
                        
                        {!isSubmitted && (
                            <button
                                onClick={addCustomOutcome}
                                className="px-4 py-2 bg-green-500 text-white rounded-md text-sm hover:bg-green-600"
                            >
                                Add Outcome
                            </button>
                        )}
                    </div>
                    
                    {simData.customOutcomes.length > 0 && (
                        <div className="mt-3 text-sm text-gray-600">
                            Total Probability: {simData.customProbabilities.reduce((sum, prob) => sum + prob, 0).toFixed(3)}
                            {Math.abs(simData.customProbabilities.reduce((sum, prob) => sum + prob, 0) - 1) > 0.001 && (
                                <span className="text-red-600 ml-2">(Should equal 1.000)</span>
                            )}
                        </div>
                    )}
                </div>
            )}

            {/* Experiment Description */}
            <div className="mb-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                <p className="text-sm text-blue-800">
                    <strong>Current Experiment:</strong> {predefinedExperiments[simData.experimentType].description}
                </p>
            </div>

            {/* Controls */}
            <div className="flex flex-wrap gap-2 mb-4">
                {!isSubmitted && (
                    <>
                        <button
                            onClick={runSingleTrial}
                            className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm hover:bg-blue-600"
                            disabled={isRunning}
                        >
                            Single Trial
                        </button>
                        
                        <button
                            onClick={runMultipleTrials}
                            className="px-4 py-2 bg-green-500 text-white rounded-md text-sm hover:bg-green-600"
                            disabled={isRunning}
                        >
                            {isRunning ? `Running... (${currentTrial}/${simData.numberOfTrials})` : `Run ${simData.numberOfTrials} Trials`}
                        </button>
                        
                        <button
                            onClick={clearResults}
                            className="px-4 py-2 bg-red-500 text-white rounded-md text-sm hover:bg-red-600"
                            disabled={isRunning}
                        >
                            Clear Results
                        </button>
                    </>
                )}
            </div>

            {/* Options */}
            <div className="flex space-x-4 mb-4">
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={simData.showHistory}
                        onChange={(e) => handleFieldChange('showHistory', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show History</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={simData.showChart}
                        onChange={(e) => handleFieldChange('showChart', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Chart</span>
                </label>
                
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        className="mr-2"
                        checked={simData.autoRun}
                        onChange={(e) => handleFieldChange('autoRun', e.target.checked)}
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Auto-run Animation</span>
                </label>
            </div>

            {/* Results Summary */}
            {simData.results.length > 0 && (
                <div className="mb-4 p-4 bg-white border border-gray-200 rounded-lg">
                    <h4 className="font-semibold text-gray-700 mb-3">Results Summary</h4>
                    
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                        <div className="text-center">
                            <div className="text-2xl font-bold text-blue-600">{simData.results.length}</div>
                            <div className="text-sm text-gray-600">Total Trials</div>
                        </div>
                        <div className="text-center">
                            <div className="text-2xl font-bold text-green-600">
                                {calculateChiSquare().toFixed(3)}
                            </div>
                            <div className="text-sm text-gray-600">Chi-Square Statistic</div>
                        </div>
                        <div className="text-center">
                            <div className="text-2xl font-bold text-purple-600">
                                {new Set(simData.results.map(r => r.outcome)).size}
                            </div>
                            <div className="text-sm text-gray-600">Unique Outcomes</div>
                        </div>
                    </div>

                    {/* Chart */}
                    {simData.showChart && (
                        <div className="mb-4">
                            <h5 className="font-semibold text-gray-700 mb-2">Outcome Distribution</h5>
                            {renderChart()}
                        </div>
                    )}

                    {/* Results Table */}
                    <div className="mb-4">
                        <h5 className="font-semibold text-gray-700 mb-2">Detailed Results</h5>
                        {renderResultsTable()}
                    </div>

                    {/* History */}
                    {simData.showHistory && (
                        <div>
                            <h5 className="font-semibold text-gray-700 mb-2">Recent Trials (Last 20)</h5>
                            <div className="max-h-40 overflow-y-auto">
                                <div className="grid grid-cols-3 gap-2 text-xs">
                                    {simData.results.slice(-20).reverse().map((result, index) => (
                                        <div key={index} className="p-2 bg-gray-100 rounded">
                                            <div className="font-medium">Trial {result.trial}</div>
                                            <div className="text-blue-600">{result.outcome}</div>
                                            <div className="text-gray-500">{result.timestamp}</div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            )}

            {/* Instructions */}
            <div className="text-xs text-gray-500 bg-blue-50 p-2 rounded">
                <p><strong>Probability Simulator Instructions:</strong></p>
                <ul className="list-disc list-inside space-y-1 mt-1">
                    <li>Choose an experiment type or create a custom one</li>
                    <li>Set the number of trials you want to run</li>
                    <li>Click "Single Trial" for one experiment or "Run X Trials" for multiple</li>
                    <li>View the results in the chart and detailed table</li>
                    <li>Compare observed vs expected probabilities</li>
                    <li>Use the Chi-Square statistic to test goodness of fit</li>
                </ul>
            </div>
        </div>
    );
};

export default ProbabilitySimulator;
