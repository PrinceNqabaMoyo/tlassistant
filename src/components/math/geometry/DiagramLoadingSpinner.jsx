import React from 'react';
import { Loader2 } from 'lucide-react';

const DiagramLoadingSpinner = ({ message = "Generating diagram..." }) => {
    return (
        <div className="flex items-center justify-center p-8">
            <div className="text-center">
                <Loader2 className="h-8 w-8 animate-spin text-blue-500 mx-auto mb-2" />
                <p className="text-sm text-gray-600">{message}</p>
            </div>
        </div>
    );
};

export default DiagramLoadingSpinner;
