import React from 'react';

const VisualAidsPanel = ({
    isOpen,
    setIsOpen,
    children,
}) => {
    if (!isOpen) return null;

    return (
        <>
            <div className="w-full max-w-sm bg-white rounded-xl shadow-xl border border-gray-200 overflow-hidden hidden lg:block">
                {children}
            </div>
            <div className="fixed inset-0 z-50 lg:hidden">
                <button
                    type="button"
                    aria-label="Close visual aids"
                    onClick={() => setIsOpen(false)}
                    className="absolute inset-0 bg-black/40"
                />
                <div className="absolute right-0 top-0 h-full w-[22rem] max-w-[90vw] bg-white shadow-2xl border-l border-gray-200">
                    {children}
                </div>
            </div>
        </>
    );
};

export default VisualAidsPanel;
