import React, { useState, useEffect } from 'react';

/**
 * Enhanced Math Keypad Component
 * 
 * This component provides a sophisticated math keypad with mathematical notation support,
 * cursor positioning, and expression state management. It can be used across the entire
 * application to provide consistent math input functionality.
 */

const EnhancedMathKeypad = ({ 
    isVisible, 
    onClose, 
    onKeyClick, 
    inputRef, 
    onExpressionChange,
    isSubmitted = false,
    className = ""
}) => {
    const mathKeys = ['+', '-', '×', '÷', '=', '(', ')', '√', 'π', 'θ', 'λ', 'μ', '°', 'x²', 'x₂'];

    const [disablePopup, setDisablePopup] = useState(() => localStorage.getItem('mathKeypadSettings_disableAutoPopup') === 'true');
    const [showHint, setShowHint] = useState(false);

    useEffect(() => {
        if (isVisible && !disablePopup) {
            setShowHint(true);
            const timer = setTimeout(() => setShowHint(false), 5000);
            return () => clearTimeout(timer);
        }
    }, [isVisible]);

    const togglePopupSetting = () => {
        const newVal = !disablePopup;
        setDisablePopup(newVal);
        localStorage.setItem('mathKeypadSettings_disableAutoPopup', newVal ? 'true' : 'false');
    };

    // Enhanced keypad input handling with mathematical notation support
    const handleKeyClick = (symbol) => {
        if (isSubmitted) return;
        
        const inputField = inputRef?.current;
        if (!inputField) {
            // If no input ref, just call the basic onKeyClick
            onKeyClick?.(symbol);
            return;
        }

        // Focus the input field
        inputField.focus();
        
        // Handle special symbols - preserve mathematical notation
        let insertText = symbol;
        if (symbol === 'x²') {
            insertText = 'x²'; // Keep superscript ²
        } else if (symbol === 'x₂') {
            insertText = 'x₂'; // Keep subscript ₂
        } else if (symbol === '×') {
            insertText = '×'; // Keep multiplication symbol
        } else if (symbol === '÷') {
            insertText = '÷'; // Keep division symbol
        } else if (symbol === '√') {
            insertText = '√'; // Keep square root symbol
        } else if (symbol === 'π') {
            insertText = 'π'; // Keep pi symbol
        } else if (symbol === 'θ') {
            insertText = 'θ'; // Keep theta symbol
        } else if (symbol === 'λ') {
            insertText = 'λ'; // Keep lambda symbol
        } else if (symbol === 'μ') {
            insertText = 'μ'; // Keep mu symbol
        }
        
        // Get current cursor position
        const start = inputField.selectionStart;
        const end = inputField.selectionEnd;
        const currentValue = inputField.value;
        
        // Insert the symbol at cursor position
        const newValue = currentValue.substring(0, start) + insertText + currentValue.substring(end);
        
        // Update the expression if callback provided
        if (onExpressionChange) {
            onExpressionChange(newValue);
        }
        
        // Set cursor position after the inserted symbol
        setTimeout(() => {
            inputField.setSelectionRange(start + insertText.length, start + insertText.length);
            inputField.focus();
        }, 0);
    };

    if (!isVisible) return null;

    return (
        <div className={`fixed bottom-20 right-4 z-50 bg-gray-200 p-2 rounded-lg shadow-xl border border-gray-300 w-80 animate-fade-in-up ${className}`}>
            <div className="flex justify-between items-center mb-2">
                <span className="font-semibold text-gray-700">Math Keypad</span>
                <div className="flex items-center gap-3 relative">
                    <button
                        onClick={togglePopupSetting}
                        className={`text-lg transition-colors ${disablePopup ? 'text-gray-400' : 'text-indigo-600 hover:text-indigo-800'}`}
                        title={disablePopup ? "Auto pop-up OFF" : "Auto pop-up ON"}
                    >
                        ⚙️
                    </button>
                    {showHint && !disablePopup && (
                        <div className="absolute -top-8 right-8 bg-indigo-900 text-white text-xs px-2 py-1 rounded whitespace-nowrap animate-bounce shadow-lg">
                            Tap to stop keypad pop up
                            <div className="absolute top-full right-2 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-indigo-900"></div>
                        </div>
                    )}
                    <button 
                        onClick={onClose} 
                        className="text-xl font-bold hover:text-gray-500 transition-colors"
                    >
                        &times;
                    </button>
                </div>
            </div>
            <div className="grid grid-cols-5 gap-2">
                {mathKeys.map(key => (
                    <button 
                        key={key} 
                        onClick={() => handleKeyClick(key)} 
                        className="p-2 rounded-md bg-white hover:bg-gray-100 font-mono text-lg transition-colors"
                        disabled={isSubmitted}
                    >
                        {key}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default EnhancedMathKeypad;
