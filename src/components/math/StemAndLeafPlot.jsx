import React, { useState, useEffect, useRef } from 'react';

const StemAndLeafPlot = ({ initialData, onChange, isSubmitted }) => {
    const [stemLeafData, setStemLeafData] = useState(initialData || {
        title: "Stem and Leaf Plot",
        dataSet: [12, 23, 34, 45, 56, 67, 78, 89, 90, 11, 22, 33, 44, 55, 66, 77, 88, 99],
        stemUnit: 10,
        leafUnit: 1,
        showStatistics: true,
        showSortedData: true,
        showFrequency: true,
        showRange: true,
        showMedian: true,
        showMode: true,
        showMean: true,
        backgroundColor: '#ffffff',
        stemColor: '#3B82F6',
        leafColor: '#10B981',
        textColor: '#374151'
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(stemLeafData);
        }
    }, [stemLeafData, onChange]);

    useEffect(() => {
        // Ensure canvas is ready before drawing
        const timer = setTimeout(() => {
            drawStemAndLeafPlot();
        }, 100);
        
        return () => clearTimeout(timer);
    }, [stemLeafData]);

    // Initial draw when component mounts
    useEffect(() => {
        drawStemAndLeafPlot();
    }, []);

    const processData = () => {
        const sortedData = [...stemLeafData.dataSet].sort((a, b) => a - b);
        const stemMap = new Map();

        sortedData.forEach(value => {
            const stem = Math.floor(value / stemLeafData.stemUnit);
            const leaf = value % stemLeafData.stemUnit;
            
            if (!stemMap.has(stem)) {
                stemMap.set(stem, []);
            }
            stemMap.get(stem).push(leaf);
        });

        return { sortedData, stemMap };
    };

    const calculateStatistics = () => {
        const { sortedData } = processData();
        const n = sortedData.length;
        
        if (n === 0) return null;

        const sum = sortedData.reduce((acc, val) => acc + val, 0);
        const mean = sum / n;
        const median = n % 2 === 0 
            ? (sortedData[n/2 - 1] + sortedData[n/2]) / 2 
            : sortedData[Math.floor(n/2)];
        
        // Calculate mode
        const frequency = {};
        sortedData.forEach(val => {
            frequency[val] = (frequency[val] || 0) + 1;
        });
        const maxFreq = Math.max(...Object.values(frequency));
        const mode = Object.keys(frequency).filter(key => frequency[key] === maxFreq).map(Number);
        
        const range = sortedData[n - 1] - sortedData[0];
        const min = sortedData[0];
        const max = sortedData[n - 1];

        return { mean, median, mode, range, min, max, n };
    };

    const drawStemAndLeafPlot = () => {
        const canvas = canvasRef.current;
        if (!canvas) {
            console.log('StemAndLeafPlot: Canvas not found');
            return;
        }

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.log('StemAndLeafPlot: Canvas context not available');
            return;
        }

        const width = canvas.width;
        const height = canvas.height;

        console.log('StemAndLeafPlot: Drawing with dimensions:', { width, height, dataSet: stemLeafData.dataSet });

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = stemLeafData.backgroundColor || '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Test drawing - draw a simple rectangle to verify canvas is working
        ctx.fillStyle = '#ff00ff';
        ctx.fillRect(10, 10, 50, 50);

        const { stemMap } = processData();
        const stats = calculateStatistics();

        if (!stats) return;

        const stems = Array.from(stemMap.keys()).sort((a, b) => a - b);
        const maxStem = Math.max(...stems);
        const minStem = Math.min(...stems);

        // Calculate layout
        const margin = 50;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;
        const stemWidth = 60;
        const leafWidth = plotWidth - stemWidth;
        const rowHeight = Math.min(30, plotHeight / (stems.length + 2));

        // Draw title
        ctx.fillStyle = stemLeafData.textColor;
        ctx.font = 'bold 18px Arial';
        ctx.textAlign = 'center';
        ctx.fillText(stemLeafData.title, width / 2, 30);

        // Draw legend
        ctx.font = '12px Arial';
        ctx.textAlign = 'left';
        ctx.fillText(`Stem Unit: ${stemLeafData.stemUnit}`, margin, 50);
        ctx.fillText(`Leaf Unit: ${stemLeafData.leafUnit}`, margin + 150, 50);

        // Draw stem and leaf plot
        let yOffset = margin + 80;
        
        // Draw header
        ctx.fillStyle = stemLeafData.textColor;
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Stem', margin + stemWidth / 2, yOffset);
        ctx.fillText('Leaf', margin + stemWidth + leafWidth / 2, yOffset);
        yOffset += 20;

        // Draw separator line
        ctx.strokeStyle = stemLeafData.textColor;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(margin, yOffset);
        ctx.lineTo(margin + plotWidth, yOffset);
        ctx.stroke();
        yOffset += 10;

        // Draw each stem and its leaves
        ctx.font = '14px Arial';
        for (let stem = minStem; stem <= maxStem; stem++) {
            const leaves = stemMap.get(stem) || [];
            const sortedLeaves = leaves.sort((a, b) => a - b);
            
            // Draw stem
            ctx.fillStyle = stemLeafData.stemColor;
            ctx.textAlign = 'center';
            ctx.fillText(stem.toString(), margin + stemWidth / 2, yOffset + 5);
            
            // Draw separator
            ctx.strokeStyle = stemLeafData.stemColor;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(margin + stemWidth, yOffset - 10);
            ctx.lineTo(margin + stemWidth, yOffset + 10);
            ctx.stroke();
            
            // Draw leaves
            ctx.fillStyle = stemLeafData.leafColor;
            ctx.textAlign = 'left';
            let xOffset = margin + stemWidth + 10;
            sortedLeaves.forEach(leaf => {
                ctx.fillText(leaf.toString(), xOffset, yOffset + 5);
                xOffset += 20;
            });
            
            // Draw frequency if enabled
            if (stemLeafData.showFrequency) {
                ctx.fillStyle = stemLeafData.textColor;
                ctx.textAlign = 'right';
                ctx.fillText(`(${leaves.length})`, margin + plotWidth - 10, yOffset + 5);
            }
            
            yOffset += rowHeight;
        }

        // Draw statistics if enabled
        if (stemLeafData.showStatistics) {
            yOffset += 20;
            ctx.fillStyle = stemLeafData.textColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Statistics:', margin, yOffset);
            yOffset += 20;

            ctx.font = '12px Arial';
            ctx.fillText(`Count: ${stats.n}`, margin, yOffset);
            ctx.fillText(`Mean: ${stats.mean.toFixed(2)}`, margin + 100, yOffset);
            ctx.fillText(`Median: ${stats.median}`, margin + 200, yOffset);
            yOffset += 15;

            ctx.fillText(`Mode: ${stats.mode.join(', ')}`, margin, yOffset);
            ctx.fillText(`Range: ${stats.range}`, margin + 100, yOffset);
            ctx.fillText(`Min: ${stats.min}`, margin + 200, yOffset);
            ctx.fillText(`Max: ${stats.max}`, margin + 300, yOffset);
        }

        // Draw sorted data if enabled
        if (stemLeafData.showSortedData) {
            const { sortedData } = processData();
            yOffset += 30;
            ctx.fillStyle = stemLeafData.textColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Sorted Data:', margin, yOffset);
            yOffset += 20;

            ctx.font = '12px Arial';
            const dataText = sortedData.join(', ');
            const maxWidth = plotWidth - 20;
            const words = dataText.split(', ');
            let line = '';
            let lineY = yOffset;

            words.forEach(word => {
                const testLine = line + (line ? ', ' : '') + word;
                const testWidth = ctx.measureText(testLine).width;
                
                if (testWidth > maxWidth && line) {
                    ctx.fillText(line, margin, lineY);
                    line = word;
                    lineY += 15;
                } else {
                    line = testLine;
                }
            });
            
            if (line) {
                ctx.fillText(line, margin, lineY);
            }
        }
    };

    const handleInputChange = (field, value) => {
        setStemLeafData(prev => ({
            ...prev,
            [field]: field === 'stemUnit' || field === 'leafUnit' ? parseFloat(value) || 1 : value
        }));
    };

    const handleDataSetChange = (value) => {
        const numbers = value.split(',').map(s => parseFloat(s.trim())).filter(n => !isNaN(n));
        setStemLeafData(prev => ({
            ...prev,
            dataSet: numbers
        }));
    };

    const generateRandomData = () => {
        const count = Math.floor(Math.random() * 20) + 10;
        const data = Array.from({ length: count }, () => Math.floor(Math.random() * 100));
        setStemLeafData(prev => ({
            ...prev,
            dataSet: data
        }));
    };

    const addDataPoint = () => {
        const newValue = Math.floor(Math.random() * 100);
        setStemLeafData(prev => ({
            ...prev,
            dataSet: [...prev.dataSet, newValue]
        }));
    };

    const clearData = () => {
        setStemLeafData(prev => ({
            ...prev,
            dataSet: []
        }));
    };

    const stats = calculateStatistics();

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
                        value={stemLeafData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Stem Unit
                    </label>
                    <input
                        type="number"
                        min="1"
                        value={stemLeafData.stemUnit}
                        onChange={(e) => handleInputChange('stemUnit', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Leaf Unit
                    </label>
                    <input
                        type="number"
                        min="0.1"
                        step="0.1"
                        value={stemLeafData.leafUnit}
                        onChange={(e) => handleInputChange('leafUnit', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Data Set (comma-separated numbers)
                    </label>
                    <input
                        type="text"
                        value={stemLeafData.dataSet.join(', ')}
                        onChange={(e) => handleDataSetChange(e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                        placeholder="Enter numbers separated by commas..."
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={stemLeafData.showStatistics}
                                onChange={(e) => handleInputChange('showStatistics', e.target.checked)}
                                className="mr-2"
                            />
                            Show Statistics
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={stemLeafData.showSortedData}
                                onChange={(e) => handleInputChange('showSortedData', e.target.checked)}
                                className="mr-2"
                            />
                            Show Sorted Data
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={stemLeafData.showFrequency}
                                onChange={(e) => handleInputChange('showFrequency', e.target.checked)}
                                className="mr-2"
                            />
                            Show Frequency
                        </label>
                    </div>
                </div>
            </div>

            {/* Data Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <h4 className="font-semibold text-blue-800 mb-3">Data Management</h4>
                <div className="flex space-x-2">
                    <button
                        onClick={generateRandomData}
                        className="px-4 py-2 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                    >
                        Generate Random Data
                    </button>
                    <button
                        onClick={addDataPoint}
                        className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                    >
                        Add Random Point
                    </button>
                    <button
                        onClick={clearData}
                        className="px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded text-sm"
                    >
                        Clear Data
                    </button>
                </div>
            </div>

            {/* Statistics Summary */}
            {stats && (
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-3">Quick Statistics</h4>
                    <div className="grid grid-cols-3 gap-4 text-sm">
                        <div>
                            <strong>Count:</strong> {stats.n}
                        </div>
                        <div>
                            <strong>Mean:</strong> {stats.mean.toFixed(2)}
                        </div>
                        <div>
                            <strong>Median:</strong> {stats.median}
                        </div>
                        <div>
                            <strong>Mode:</strong> {stats.mode.join(', ')}
                        </div>
                        <div>
                            <strong>Range:</strong> {stats.range}
                        </div>
                        <div>
                            <strong>Min/Max:</strong> {stats.min} / {stats.max}
                        </div>
                    </div>
                </div>
            )}

            {/* Stem and Leaf Plot Canvas */}
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

export default StemAndLeafPlot;
