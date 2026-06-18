import React from 'react';
export const Button = ({ children, onClick, disabled, className = '', variant = 'primary' }) => {
    return (
        <button
            onClick={onClick}
            disabled={disabled}
            className={`px-4 py-2 rounded-xl font-semibold transition-colors flex items-center justify-center ${disabled ? 'opacity-50 cursor-not-allowed' : ''} ${className}`}
        >
            {children}
        </button>
    );
};
