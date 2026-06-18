import React, { useState, useEffect, useRef } from 'react';

const VennDiagram = ({ initialData, onChange, isSubmitted }) => {
    const [vennData, setVennData] = useState(initialData || {
        title: "Venn Diagram",
        sets: [
            { label: "Set A", elements: ["1", "2", "3", "4"], color: "#3B82F6" },
            { label: "Set B", elements: ["3", "4", "5", "6"], color: "#10B981" }
        ],
        showIntersection: true,
        showUnion: true,
        showElements: true,
        showLabels: true,
        showCounts: true,
        backgroundColor: '#ffffff',
        borderColor: '#374151'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(vennData);
        }
    }, [vennData, onChange]);

    useEffect(() => {
        drawVennDiagram();
    }, [vennData]);

    // Calculate set operations
    const calculateSetOperations = () => {
        const setA = new Set(vennData.sets[0]?.elements || []);
        const setB = new Set(vennData.sets[1]?.elements || []);
        
        const intersection = new Set([...setA].filter(x => setB.has(x)));
        const union = new Set([...setA, ...setB]);
        const onlyA = new Set([...setA].filter(x => !setB.has(x)));
        const onlyB = new Set([...setB].filter(x => !setA.has(x)));

        return {
            intersection: Array.from(intersection),
            union: Array.from(union),
            onlyA: Array.from(onlyA),
            onlyB: Array.from(onlyB),
            setA: Array.from(setA),
            setB: Array.from(setB)
        };
    };

    const drawVennDiagram = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = vennData.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        if (vennData.sets.length < 2) return;

        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) * 0.25;
        const separation = radius * 0.6;

        const setOperations = calculateSetOperations();

        // Draw Set A (left circle)
        const leftCenterX = centerX - separation / 2;
        ctx.beginPath();
        ctx.arc(leftCenterX, centerY, radius, 0, 2 * Math.PI);
        ctx.fillStyle = vennData.sets[0].color + '40'; // 40 = 25% opacity
        ctx.fill();
        ctx.strokeStyle = vennData.sets[0].color;
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw Set B (right circle)
        const rightCenterX = centerX + separation / 2;
        ctx.beginPath();
        ctx.arc(rightCenterX, centerY, radius, 0, 2 * Math.PI);
        ctx.fillStyle = vennData.sets[1].color + '40'; // 40 = 25% opacity
        ctx.fill();
        ctx.strokeStyle = vennData.sets[1].color;
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw intersection area with darker color
        if (vennData.showIntersection) {
            ctx.globalCompositeOperation = 'multiply';
            ctx.beginPath();
            ctx.arc(leftCenterX, centerY, radius, 0, 2 * Math.PI);
            ctx.fillStyle = vennData.sets[0].color + '80'; // 80 = 50% opacity
            ctx.fill();
            ctx.beginPath();
            ctx.arc(rightCenterX, centerY, radius, 0, 2 * Math.PI);
            ctx.fillStyle = vennData.sets[1].color + '80'; // 80 = 50% opacity
            ctx.fill();
            ctx.globalCompositeOperation = 'source-over';
        }

        // Draw set labels
        if (vennData.showLabels) {
            ctx.fillStyle = vennData.borderColor;
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            
            // Set A label
            ctx.fillText(vennData.sets[0].label, leftCenterX, centerY - radius - 20);
            
            // Set B label
            ctx.fillText(vennData.sets[1].label, rightCenterX, centerY - radius - 20);
        }

        // Draw element counts
        if (vennData.showCounts) {
            ctx.fillStyle = vennData.borderColor;
            ctx.font = '14px Arial';
            ctx.textAlign = 'center';
            
            // Only A count
            ctx.fillText(`n(A only) = ${setOperations.onlyA.length}`, leftCenterX - radius/2, centerY - 10);
            
            // Only B count
            ctx.fillText(`n(B only) = ${setOperations.onlyB.length}`, rightCenterX + radius/2, centerY - 10);
            
            // Intersection count
            ctx.fillText(`n(A∩B) = ${setOperations.intersection.length}`, centerX, centerY + 10);
            
            // Union count
            ctx.fillText(`n(A∪B) = ${setOperations.union.length}`, centerX, centerY + 40);
        }

        // Draw elements if requested
        if (vennData.showElements) {
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            
            // Elements only in A
            setOperations.onlyA.forEach((element, index) => {
                const x = leftCenterX - radius/2 - 20;
                const y = centerY - radius/2 + (index * 20);
                ctx.fillStyle = vennData.sets[0].color;
                ctx.fillText(element, x, y);
            });
            
            // Elements only in B
            setOperations.onlyB.forEach((element, index) => {
                const x = rightCenterX + radius/2 + 20;
                const y = centerY - radius/2 + (index * 20);
                ctx.fillStyle = vennData.sets[1].color;
                ctx.fillText(element, x, y);
            });
            
            // Elements in intersection
            setOperations.intersection.forEach((element, index) => {
                const x = centerX;
                const y = centerY - 20 + (index * 20);
                ctx.fillStyle = vennData.borderColor;
                ctx.fillText(element, x, y);
            });
        }

        // Draw title
        ctx.fillStyle = vennData.borderColor;
        ctx.font = 'bold 18px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(vennData.title, centerX, 30);
    };

    const handleInputChange = (field, value) => {
        setVennData(prev => ({
            ...prev,
            [field]: value
        }));
    };

    const handleSetChange = (setIndex, field, value) => {
        setVennData(prev => ({
            ...prev,
            sets: prev.sets.map((set, index) => 
                index === setIndex 
                    ? { ...set, [field]: field === 'elements' ? value.split(',').map(s => s.trim()).filter(s => s !== '') : value }
                    : set
            )
        }));
    };

    const addSet = () => {
        if (vennData.sets.length < 3) { // Limit to 3 sets for now
            const newSet = {
                label: `Set ${String.fromCharCode(65 + vennData.sets.length)}`,
                elements: [],
                color: `#${Math.floor(Math.random()*16777215).toString(16)}`
            };
            setVennData(prev => ({
                ...prev,
                sets: [...prev.sets, newSet]
            }));
        }
    };

    const removeSet = (setIndex) => {
        if (vennData.sets.length > 2) {
            setVennData(prev => ({
                ...prev,
                sets: prev.sets.filter((_, index) => index !== setIndex)
            }));
        }
    };

    const generateRandomData = () => {
        const newSets = [
            {
                label: "Set A",
                elements: Array.from({length: Math.floor(Math.random() * 5) + 3}, (_, i) => (i + 1).toString()),
                color: "#3B82F6"
            },
            {
                label: "Set B", 
                elements: Array.from({length: Math.floor(Math.random() * 5) + 3}, (_, i) => (i + 4).toString()),
                color: "#10B981"
            }
        ];
        
        setVennData(prev => ({
            ...prev,
            sets: newSets
        }));
    };

    const setOperations = calculateSetOperations();

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
                        value={vennData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Background Color
                    </label>
                    <input
                        type="color"
                        value={vennData.backgroundColor}
                        onChange={(e) => handleInputChange('backgroundColor', e.target.value)}
                        className="w-full h-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Border Color
                    </label>
                    <input
                        type="color"
                        value={vennData.borderColor}
                        onChange={(e) => handleInputChange('borderColor', e.target.value)}
                        className="w-full h-10 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={vennData.showIntersection}
                                onChange={(e) => handleInputChange('showIntersection', e.target.checked)}
                                className="mr-2"
                            />
                            Show Intersection
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={vennData.showUnion}
                                onChange={(e) => handleInputChange('showUnion', e.target.checked)}
                                className="mr-2"
                            />
                            Show Union
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={vennData.showElements}
                                onChange={(e) => handleInputChange('showElements', e.target.checked)}
                                className="mr-2"
                            />
                            Show Elements
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={vennData.showLabels}
                                onChange={(e) => handleInputChange('showLabels', e.target.checked)}
                                className="mr-2"
                            />
                            Show Labels
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={vennData.showCounts}
                                onChange={(e) => handleInputChange('showCounts', e.target.checked)}
                                className="mr-2"
                            />
                            Show Counts
                        </label>
                    </div>
                </div>
            </div>

            {/* Set Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex justify-between items-center mb-4">
                    <h4 className="font-semibold text-blue-800">Set Management</h4>
                    <div className="flex space-x-2">
                        <button
                            onClick={generateRandomData}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Random Data
                        </button>
                        <button
                            onClick={addSet}
                            disabled={vennData.sets.length >= 3}
                            className={`px-3 py-1 text-sm rounded ${
                                vennData.sets.length >= 3
                                    ? 'bg-gray-400 cursor-not-allowed'
                                    : 'bg-blue-600 hover:bg-blue-700 text-white'
                            }`}
                        >
                            Add Set
                        </button>
                    </div>
                </div>

                <div className="space-y-4">
                    {vennData.sets.map((set, setIndex) => (
                        <div key={setIndex} className="p-3 bg-white rounded border">
                            <div className="flex justify-between items-center mb-2">
                                <h5 className="font-medium text-gray-800">Set {String.fromCharCode(65 + setIndex)}</h5>
                                {vennData.sets.length > 2 && (
                                    <button
                                        onClick={() => removeSet(setIndex)}
                                        className="text-red-600 hover:text-red-800 text-sm"
                                    >
                                        Remove
                                    </button>
                                )}
                            </div>
                            
                            <div className="grid grid-cols-2 gap-3">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Label
                                    </label>
                                    <input
                                        type="text"
                                        value={set.label}
                                        onChange={(e) => handleSetChange(setIndex, 'label', e.target.value)}
                                        className="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                </div>
                                
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Color
                                    </label>
                                    <input
                                        type="color"
                                        value={set.color}
                                        onChange={(e) => handleSetChange(setIndex, 'color', e.target.value)}
                                        className="w-full h-8 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    />
                                </div>
                                
                                <div className="col-span-2">
                                    <label className="block text-sm font-medium text-gray-700 mb-1">
                                        Elements (comma-separated)
                                    </label>
                                    <input
                                        type="text"
                                        value={set.elements.join(', ')}
                                        onChange={(e) => handleSetChange(setIndex, 'elements', e.target.value)}
                                        className="w-full px-2 py-1 border border-gray-300 rounded text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                                        placeholder="Enter elements separated by commas..."
                                    />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Set Operations Display */}
            <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <h4 className="font-semibold text-green-800 mb-3">Set Operations</h4>
                <div className="grid grid-cols-2 gap-4 text-sm">
                    <div>
                        <strong>Set A:</strong> {setOperations.setA.join(', ') || 'Empty'}
                        <br />
                        <strong>Set B:</strong> {setOperations.setB.join(', ') || 'Empty'}
                    </div>
                    <div>
                        <strong>Intersection (A∩B):</strong> {setOperations.intersection.join(', ') || 'Empty'}
                        <br />
                        <strong>Union (A∪B):</strong> {setOperations.union.join(', ') || 'Empty'}
                    </div>
                    <div>
                        <strong>Only in A:</strong> {setOperations.onlyA.join(', ') || 'Empty'}
                    </div>
                    <div>
                        <strong>Only in B:</strong> {setOperations.onlyB.join(', ') || 'Empty'}
                    </div>
                </div>
            </div>

            {/* Venn Diagram Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={800}
                    height={500}
                    className="w-full h-auto"
                />
            </div>
        </div>
    );
};

export default VennDiagram;
