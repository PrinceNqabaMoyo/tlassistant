import React, { useState, useEffect, useRef } from 'react';

const TreeDiagram = ({ initialData, onChange, isSubmitted }) => {
    const [treeData, setTreeData] = useState(initialData || {
        title: "Tree Diagram",
        root: "Start",
        branches: [
            {
                label: "Branch 1",
                probability: 0.6,
                outcomes: ["Outcome A", "Outcome B"]
            },
            {
                label: "Branch 2",
                probability: 0.4,
                outcomes: ["Outcome C", "Outcome D"]
            }
        ],
        showProbabilities: true,
        showOutcomes: true,
        showLabels: true,
        showValues: true,
        orientation: 'horizontal',
        nodeSpacing: 120,
        levelSpacing: 80,
        backgroundColor: '#ffffff',
        nodeColor: '#3B82F6',
        branchColor: '#10B981',
        outcomeColor: '#F59E0B'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(treeData);
        }
    }, [treeData, onChange]);

    useEffect(() => {
        drawTreeDiagram();
    }, [treeData]);

    const drawTreeDiagram = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = treeData.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        const { root, branches, showProbabilities, showOutcomes, showLabels, showValues, orientation, nodeSpacing, levelSpacing, nodeColor, branchColor, outcomeColor } = treeData;

        if (orientation === 'horizontal') {
            drawHorizontalTree(ctx, width, height, root, branches, showProbabilities, showOutcomes, showLabels, showValues, nodeSpacing, levelSpacing, nodeColor, branchColor, outcomeColor);
        } else {
            drawVerticalTree(ctx, width, height, root, branches, showProbabilities, showOutcomes, showLabels, showValues, nodeSpacing, levelSpacing, nodeColor, branchColor, outcomeColor);
        }

        // Draw title
        ctx.fillStyle = '#374151';
        ctx.font = 'bold 18px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(treeData.title, width / 2, 30);
    };

    const drawHorizontalTree = (ctx, width, height, root, branches, showProbabilities, showOutcomes, showLabels, showValues, nodeSpacing, levelSpacing, nodeColor, branchColor, outcomeColor) => {
        const startX = 100;
        const startY = height / 2;

        // Draw root node
        ctx.fillStyle = nodeColor;
        ctx.beginPath();
        ctx.arc(startX, startY, 20, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#1e40af';
        ctx.lineWidth = 2;
        ctx.stroke();

        if (showLabels) {
            ctx.fillStyle = '#374151';
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(root, startX, startY + 35);
        }

        // Calculate total width needed
        const totalBranches = branches.length;
        const totalWidth = (totalBranches - 1) * nodeSpacing;
        const startBranchX = startX + levelSpacing;

        branches.forEach((branch, branchIndex) => {
            const branchX = startBranchX;
            const branchY = startY + (branchIndex - (totalBranches - 1) / 2) * nodeSpacing;

            // Draw branch line
            ctx.strokeStyle = branchColor;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(startX + 20, startY);
            ctx.lineTo(branchX - 20, branchY);
            ctx.stroke();

            // Draw branch node
            ctx.fillStyle = branchColor;
            ctx.beginPath();
            ctx.arc(branchX, branchY, 18, 0, 2 * Math.PI);
            ctx.fill();
            ctx.strokeStyle = '#059669';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw branch label
            if (showLabels) {
                ctx.fillStyle = '#374151';
                ctx.font = '12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(branch.label, branchX, branchY + 25);
            }

            // Draw probability
            if (showProbabilities) {
                ctx.fillStyle = '#7c3aed';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                
                // Calculate position for probability label
                const midX = (startX + branchX) / 2;
                const midY = (startY + branchY) / 2;
                ctx.fillText(`${(branch.probability * 100).toFixed(0)}%`, midX, midY - 5);
            }

            // Draw outcomes
            if (showOutcomes && branch.outcomes) {
                const outcomeSpacing = 60;
                const totalOutcomes = branch.outcomes.length;
                const startOutcomeX = branchX + levelSpacing;

                branch.outcomes.forEach((outcome, outcomeIndex) => {
                    const outcomeX = startOutcomeX;
                    const outcomeY = branchY + (outcomeIndex - (totalOutcomes - 1) / 2) * outcomeSpacing;

                    // Draw outcome line
                    ctx.strokeStyle = outcomeColor;
                    ctx.lineWidth = 1.5;
                    ctx.beginPath();
                    ctx.moveTo(branchX + 18, branchY);
                    ctx.lineTo(outcomeX - 15, outcomeY);
                    ctx.stroke();

                    // Draw outcome node
                    ctx.fillStyle = outcomeColor;
                    ctx.beginPath();
                    ctx.arc(outcomeX, outcomeY, 12, 0, 2 * Math.PI);
                    ctx.fill();
                    ctx.strokeStyle = '#d97706';
                    ctx.lineWidth = 1.5;
                    ctx.stroke();

                    // Draw outcome label
                    if (showLabels) {
                        ctx.fillStyle = '#374151';
                        ctx.font = '10px Arial';
                        ctx.textAlign = 'center';
                        ctx.fillText(outcome, outcomeX, outcomeY + 18);
                    }

                    // Draw outcome value if it's numeric
                    if (showValues && !isNaN(outcome)) {
                        ctx.fillStyle = '#dc2626';
                        ctx.font = 'bold 10px Arial';
                        ctx.textAlign = 'center';
                        ctx.fillText(outcome, outcomeX, outcomeY - 15);
                    }
                });
            }
        });
    };

    const drawVerticalTree = (ctx, width, height, root, branches, showProbabilities, showOutcomes, showLabels, showValues, nodeSpacing, levelSpacing, nodeColor, branchColor, outcomeColor) => {
        const startX = width / 2;
        const startY = 100;

        // Draw root node
        ctx.fillStyle = nodeColor;
        ctx.beginPath();
        ctx.arc(startX, startY, 20, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#1e40af';
        ctx.lineWidth = 2;
        ctx.stroke();

        if (showLabels) {
            ctx.fillStyle = '#374151';
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(root, startX, startY + 35);
        }

        // Calculate total height needed
        const totalBranches = branches.length;
        const totalHeight = (totalBranches - 1) * nodeSpacing;
        const startBranchY = startY + levelSpacing;

        branches.forEach((branch, branchIndex) => {
            const branchX = startX + (branchIndex - (totalBranches - 1) / 2) * nodeSpacing;
            const branchY = startBranchY;

            // Draw branch line
            ctx.strokeStyle = branchColor;
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(startX, startY + 20);
            ctx.lineTo(branchX, branchY - 18);
            ctx.stroke();

            // Draw branch node
            ctx.fillStyle = branchColor;
            ctx.beginPath();
            ctx.arc(branchX, branchY, 18, 0, 2 * Math.PI);
            ctx.fill();
            ctx.strokeStyle = '#059669';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw branch label
            if (showLabels) {
                ctx.fillStyle = '#374151';
                ctx.font = '12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(branch.label, branchX, branchY + 25);
            }

            // Draw probability
            if (showProbabilities) {
                ctx.fillStyle = '#7c3aed';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                
                // Calculate position for probability label
                const midX = (startX + branchX) / 2;
                const midY = (startY + branchY) / 2;
                ctx.fillText(`${(branch.probability * 100).toFixed(0)}%`, midX, midY - 5);
            }

            // Draw outcomes
            if (showOutcomes && branch.outcomes) {
                const outcomeSpacing = 60;
                const totalOutcomes = branch.outcomes.length;
                const startOutcomeY = branchY + levelSpacing;

                branch.outcomes.forEach((outcome, outcomeIndex) => {
                    const outcomeX = branchX + (outcomeIndex - (totalOutcomes - 1) / 2) * outcomeSpacing;
                    const outcomeY = startOutcomeY;

                    // Draw outcome line
                    ctx.strokeStyle = outcomeColor;
                    ctx.lineWidth = 1.5;
                    ctx.beginPath();
                    ctx.moveTo(branchX, branchY + 18);
                    ctx.lineTo(outcomeX, outcomeY - 15);
                    ctx.stroke();

                    // Draw outcome node
                    ctx.fillStyle = outcomeColor;
                    ctx.beginPath();
                    ctx.arc(outcomeX, outcomeY, 12, 0, 2 * Math.PI);
                    ctx.fill();
                    ctx.strokeStyle = '#d97706';
                    ctx.lineWidth = 1.5;
                    ctx.stroke();

                    // Draw outcome label
                    if (showLabels) {
                        ctx.fillStyle = '#374151';
                        ctx.font = '10px Arial';
                        ctx.textAlign = 'center';
                        ctx.fillText(outcome, outcomeX, outcomeY + 18);
                    }

                    // Draw outcome value if it's numeric
                    if (showValues && !isNaN(outcome)) {
                        ctx.fillStyle = '#dc2626';
                        ctx.font = 'bold 10px Arial';
                        ctx.textAlign = 'center';
                        ctx.fillText(outcome, outcomeX, outcomeY - 15);
                    }
                });
            }
        });
    };

    const handleInputChange = (field, value) => {
        setTreeData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    const handleBranchChange = (branchIndex, field, value) => {
        setTreeData(prev => ({
            ...prev,
            branches: prev.branches.map((branch, index) => 
                index === branchIndex 
                    ? { ...branch, [field]: field === 'outcomes' ? value.split(',').map(s => s.trim()).filter(s => s !== '') : field === 'probability' ? parseFloat(value) || 0 : value }
                    : branch
            )
        }));
    };

    const addBranch = () => {
        const newBranch = {
            label: `Branch ${treeData.branches.length + 1}`,
            probability: 1 / (treeData.branches.length + 1),
            outcomes: ["Outcome 1", "Outcome 2"]
        };
        setTreeData(prev => ({
            ...prev,
            branches: [...prev.branches, newBranch]
        }));
    };

    const removeBranch = (branchIndex) => {
        if (treeData.branches.length > 1) {
            setTreeData(prev => ({
                ...prev,
                branches: prev.branches.filter((_, index) => index !== branchIndex)
            }));
        }
    };

    const addOutcome = (branchIndex) => {
        setTreeData(prev => ({
            ...prev,
            branches: prev.branches.map((branch, index) => 
                index === branchIndex 
                    ? { ...branch, outcomes: [...branch.outcomes, `Outcome ${branch.outcomes.length + 1}`] }
                    : branch
            )
        }));
    };

    const removeOutcome = (branchIndex, outcomeIndex) => {
        if (treeData.branches[branchIndex].outcomes.length > 1) {
            setTreeData(prev => ({
                ...prev,
                branches: prev.branches.map((branch, index) => 
                    index === branchIndex 
                        ? { ...branch, outcomes: branch.outcomes.filter((_, oIndex) => oIndex !== outcomeIndex) }
                        : branch
                )
            }));
        }
    };

    const generateRandomData = () => {
        const newBranches = [
            {
                label: "Option A",
                probability: 0.6,
                outcomes: ["Success", "Failure"]
            },
            {
                label: "Option B",
                probability: 0.4,
                outcomes: ["Win", "Lose", "Draw"]
            }
        ];
        
        setTreeData(prev => ({
            ...prev,
            branches: newBranches
        }));
    };

    const calculateTotalProbability = () => {
        return treeData.branches.reduce((sum, branch) => sum + branch.probability, 0);
    };

    const totalProbability = calculateTotalProbability();

    return (
        <div className="space-y-4">
            {/* Controls */}
            <div className="grid grid-cols-2 gap-4 p-4 bg-gray-50 rounded-lg">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Title
                    </label>
                    <input
                        type="text"
                        value={treeData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Root Label
                    </label>
                    <input
                        type="text"
                        value={treeData.root}
                        onChange={(e) => handleInputChange('root', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Orientation
                    </label>
                    <select
                        value={treeData.orientation}
                        onChange={(e) => handleInputChange('orientation', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    >
                        <option value="horizontal">Horizontal</option>
                        <option value="vertical">Vertical</option>
                    </select>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Node Spacing
                    </label>
                    <input
                        type="number"
                        min="60"
                        max="200"
                        value={treeData.nodeSpacing}
                        onChange={(e) => handleInputChange('nodeSpacing', parseInt(e.target.value) || 120)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Level Spacing
                    </label>
                    <input
                        type="number"
                        min="40"
                        max="150"
                        value={treeData.levelSpacing}
                        onChange={(e) => handleInputChange('levelSpacing', parseInt(e.target.value) || 80)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={treeData.showProbabilities}
                                onChange={(e) => handleInputChange('showProbabilities', e.target.checked)}
                                className="mr-2"
                            />
                            Show Probabilities
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={treeData.showOutcomes}
                                onChange={(e) => handleInputChange('showOutcomes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Outcomes
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={treeData.showLabels}
                                onChange={(e) => handleInputChange('showLabels', e.target.checked)}
                                className="mr-2"
                            />
                            Show Labels
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={treeData.showValues}
                                onChange={(e) => handleInputChange('showValues', e.target.checked)}
                                className="mr-2"
                            />
                            Show Values
                        </label>
                    </div>
                </div>
            </div>

            {/* Branch Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex justify-between items-center mb-4">
                    <h4 className="font-semibold text-blue-800">Branch Management</h4>
                    <div className="flex space-x-2">
                        <button
                            onClick={generateRandomData}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Random Data
                        </button>
                        <button
                            onClick={addBranch}
                            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                        >
                            Add Branch
                        </button>
                    </div>
                </div>

                <div className="space-y-4">
                    {treeData.branches.map((branch, branchIndex) => (
                        <div key={branchIndex} className="p-3 bg-white rounded border">
                            <div className="flex justify-between items-center mb-2">
                                <h5 className="font-medium text-gray-800">Branch {branchIndex + 1}</h5>
                                {treeData.branches.length > 1 && (
                                    <button
                                        onClick={() => removeBranch(branchIndex)}
                                        className="text-red-600 hover:text-red-800 text-sm"
                                    >
                                        Remove
                                    </button>
                                )}
                            </div>
                            
                            <div className="grid grid-cols-3 gap-3 mb-3">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Label
                                    </label>
                                    <input
                                        type="text"
                                        value={branch.label}
                                        onChange={(e) => handleBranchChange(branchIndex, 'label', e.target.value)}
                                        className="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                </div>
                                
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Probability
                                    </label>
                                    <input
                                        type="number"
                                        step="0.1"
                                        min="0"
                                        max="1"
                                        value={branch.probability}
                                        onChange={(e) => handleBranchChange(branchIndex, 'probability', e.target.value)}
                                        className="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                </div>
                                
                                <div className="flex items-end">
                                    <button
                                        onClick={() => addOutcome(branchIndex)}
                                        className="px-2 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-xs"
                                    >
                                        Add Outcome
                                    </button>
                                </div>
                            </div>
                            
                            <div className="mb-2">
                                <label className="block text-sm font-medium text-gray-700 mb-1">
                                    Outcomes (comma-separated)
                                </label>
                                <input
                                    type="text"
                                    value={branch.outcomes.join(', ')}
                                    onChange={(e) => handleBranchChange(branchIndex, 'outcomes', e.target.value)}
                                    className="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    placeholder="Enter outcomes separated by commas..."
                                />
                            </div>
                        </div>
                    ))}
                </div>

                {/* Probability Validation */}
                <div className="mt-4 p-3 bg-yellow-50 border border-yellow-200 rounded text-sm">
                    <strong>Total Probability:</strong> {totalProbability.toFixed(3)}
                    {Math.abs(totalProbability - 1) > 0.001 && (
                        <span className="text-red-600 ml-2">
                            ⚠️ Probabilities should sum to 1.0
                        </span>
                    )}
                    {Math.abs(totalProbability - 1) <= 0.001 && (
                        <span className="text-green-600 ml-2">
                            ✓ Probabilities sum to 1.0
                        </span>
                    )}
                </div>
            </div>

            {/* Tree Diagram Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={800}
                    height={600}
                    className="w-full h-auto"
                />
            </div>
        </div>
    );
};

export default TreeDiagram;
