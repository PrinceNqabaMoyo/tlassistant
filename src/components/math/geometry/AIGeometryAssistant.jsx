import React, { useState } from 'react';
import { useGeometryBackend } from '../../../hooks/useGeometryBackend';
import { Send, Bot, User, Loader2 } from 'lucide-react';

/**
 * AI Geometry Assistant Component
 * Provides AI-powered geometry help and problem solving
 */
const AIGeometryAssistant = () => {
    const { calculateProperties, generateDiagram, loading } = useGeometryBackend();
    const [messages, setMessages] = useState([
        {
            id: 1,
            type: 'ai',
            content: "Hello! I'm your AI Geometry Assistant. I can help you with geometry problems, calculations, and visualizations. What would you like to know?",
            timestamp: new Date()
        }
    ]);
    const [inputValue, setInputValue] = useState('');
    const [isProcessing, setIsProcessing] = useState(false);

    const handleSendMessage = async () => {
        if (!inputValue.trim() || isProcessing) return;

        const userMessage = {
            id: Date.now(),
            type: 'user',
            content: inputValue,
            timestamp: new Date()
        };

        setMessages(prev => [...prev, userMessage]);
        setInputValue('');
        setIsProcessing(true);

        try {
            // Simple AI response logic (in a real app, this would call an AI service)
            const aiResponse = await generateAIResponse(inputValue);
            
            const aiMessage = {
                id: Date.now() + 1,
                type: 'ai',
                content: aiResponse.content,
                timestamp: new Date(),
                diagram: aiResponse.diagram,
                calculation: aiResponse.calculation
            };

            setMessages(prev => [...prev, aiMessage]);
        } catch (error) {
            const errorMessage = {
                id: Date.now() + 1,
                type: 'ai',
                content: "I'm sorry, I encountered an error processing your request. Please try again.",
                timestamp: new Date(),
                isError: true
            };
            setMessages(prev => [...prev, errorMessage]);
        } finally {
            setIsProcessing(false);
        }
    };

    const generateAIResponse = async (input) => {
        const lowerInput = input.toLowerCase();
        
        // Detect geometry problems and provide solutions
        if (lowerInput.includes('area') || lowerInput.includes('perimeter') || lowerInput.includes('volume')) {
            return await handleCalculationRequest(input);
        }
        
        if (lowerInput.includes('draw') || lowerInput.includes('show') || lowerInput.includes('diagram')) {
            return await handleDiagramRequest(input);
        }
        
        // General geometry help
        return {
            content: `I can help you with geometry problems! Here are some things I can do:

• **Calculate areas, perimeters, and volumes** - Just ask "What's the area of a circle with radius 5?"
• **Generate diagrams** - Say "Draw a triangle with sides 3, 4, 5"
• **Explain concepts** - Ask about angles, shapes, or formulas
• **Solve problems** - Describe any geometry problem you're working on

What specific geometry topic would you like help with?`,
            diagram: null,
            calculation: null
        };
    };

    const handleCalculationRequest = async (input) => {
        // Extract shape and parameters from input
        let shape = 'circle';
        let parameters = { radius: 5 };
        
        if (input.includes('circle')) {
            const radiusMatch = input.match(/radius[:\s]*(\d+)/i);
            parameters = { radius: radiusMatch ? parseInt(radiusMatch[1]) : 5 };
        } else if (input.includes('rectangle')) {
            shape = 'rectangle';
            const lengthMatch = input.match(/length[:\s]*(\d+)/i);
            const widthMatch = input.match(/width[:\s]*(\d+)/i);
            parameters = { 
                length: lengthMatch ? parseInt(lengthMatch[1]) : 4,
                width: widthMatch ? parseInt(widthMatch[1]) : 3
            };
        } else if (input.includes('triangle')) {
            shape = 'triangle';
            const baseMatch = input.match(/base[:\s]*(\d+)/i);
            const heightMatch = input.match(/height[:\s]*(\d+)/i);
            parameters = { 
                base: baseMatch ? parseInt(baseMatch[1]) : 4,
                height: heightMatch ? parseInt(heightMatch[1]) : 3
            };
        }

        try {
            const result = await calculateProperties(shape, parameters, true);
            return {
                content: `Here are the calculations for your ${shape}:\n\n${result.calculations}`,
                diagram: result.diagram,
                calculation: result
            };
        } catch (error) {
            return {
                content: `I can help calculate ${shape} properties, but I need more specific parameters. Please provide the dimensions clearly.`,
                diagram: null,
                calculation: null
            };
        }
    };

    const handleDiagramRequest = async (input) => {
        let diagramType = 'triangle';
        let parameters = { vertices: [[-1, -1], [1, -1], [0, 1]] };
        
        if (input.includes('circle')) {
            diagramType = 'circle';
            const radiusMatch = input.match(/radius[:\s]*(\d+)/i);
            parameters = { center: [0, 0], radius: radiusMatch ? parseInt(radiusMatch[1]) : 2 };
        } else if (input.includes('square') || input.includes('rectangle')) {
            diagramType = 'rectangle';
            parameters = { width: 3, height: 2 };
        }

        try {
            const result = await generateDiagram(diagramType, '2d', parameters);
            return {
                content: `Here's your ${diagramType} diagram:`,
                diagram: result.image_data,
                calculation: null
            };
        } catch (error) {
            return {
                content: `I can generate diagrams, but I need clearer instructions. Try saying "Draw a circle with radius 3" or "Show me a triangle".`,
                diagram: null,
                calculation: null
            };
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    return (
        <div className="flex flex-col h-full bg-white rounded-lg border">
            {/* Header */}
            <div className="p-4 border-b bg-blue-50 rounded-t-lg">
                <div className="flex items-center space-x-2">
                    <Bot className="w-6 h-6 text-blue-600" />
                    <h3 className="text-lg font-semibold text-blue-900">AI Geometry Assistant</h3>
                </div>
            </div>

            {/* Messages */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {messages.map((message) => (
                    <div
                        key={message.id}
                        className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
                    >
                        <div
                            className={`max-w-[80%] rounded-lg p-3 ${
                                message.type === 'user'
                                    ? 'bg-blue-600 text-white'
                                    : message.isError
                                    ? 'bg-red-100 text-red-800 border border-red-200'
                                    : 'bg-gray-100 text-gray-800'
                            }`}
                        >
                            <div className="flex items-start space-x-2">
                                {message.type === 'ai' && !message.isError && (
                                    <Bot className="w-4 h-4 mt-1 flex-shrink-0" />
                                )}
                                {message.type === 'user' && (
                                    <User className="w-4 h-4 mt-1 flex-shrink-0" />
                                )}
                                <div className="flex-1">
                                    <p className="whitespace-pre-wrap">{message.content}</p>
                                    
                                    {message.diagram && (
                                        <div className="mt-3">
                                            <img 
                                                src={message.diagram} 
                                                alt="Generated diagram" 
                                                className="max-w-full h-auto rounded border"
                                            />
                                        </div>
                                    )}
                                    
                                    <div className="text-xs opacity-70 mt-2">
                                        {message.timestamp.toLocaleTimeString()}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                ))}
                
                {isProcessing && (
                    <div className="flex justify-start">
                        <div className="bg-gray-100 rounded-lg p-3">
                            <div className="flex items-center space-x-2">
                                <Bot className="w-4 h-4" />
                                <Loader2 className="w-4 h-4 animate-spin" />
                                <span className="text-sm">Thinking...</span>
                            </div>
                        </div>
                    </div>
                )}
            </div>

            {/* Input */}
            <div className="p-4 border-t">
                <div className="flex space-x-2">
                    <input
                        type="text"
                        value={inputValue}
                        onChange={(e) => setInputValue(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="Ask me anything about geometry..."
                        className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                        disabled={isProcessing}
                    />
                    <button
                        onClick={handleSendMessage}
                        disabled={!inputValue.trim() || isProcessing}
                        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-1"
                    >
                        <Send className="w-4 h-4" />
                        <span>Send</span>
                    </button>
                </div>
            </div>
        </div>
    );
};

export default AIGeometryAssistant;
