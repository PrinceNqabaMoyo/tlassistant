import React from 'react';
import { Mail } from 'lucide-react';

export const UserFriendlyError = ({ error, isSuperAdmin }) => {
    if (!error) return null;

    if (isSuperAdmin) {
        return <>{String(error)}</>;
    }

    return (
        <div className="space-y-2">
            <div>We encountered a technical issue while generating this question.</div>
            <div>This might be a temporary hiccup. Please adjust your settings and try again.</div>
            <a 
                href={`mailto:info@fundile.com?subject=Technical Issue: Question Generation&body=Hello Fundile Technical Team,%0D%0A%0D%0AI encountered an issue while generating a question.%0D%0A%0D%0AError Details:%0D%0A${encodeURIComponent(String(error))}%0D%0A%0D%0APlease help!`}
                className="inline-flex items-center gap-1.5 mt-2 px-3 py-1.5 bg-red-100/50 hover:bg-red-200 text-red-800 rounded-md text-sm font-medium transition-colors border border-red-200"
            >
                <Mail className="w-4 h-4" />
                Report problem to Technical Team
            </a>
        </div>
    );
};
