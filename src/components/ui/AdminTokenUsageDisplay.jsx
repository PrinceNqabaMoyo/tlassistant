import React, { useState, useEffect } from 'react';

// Token usage tracking and optimization
const tokenUsageTracker = {
  totalTokens: 0,
  aiCalls: 0,
  cachedResponses: 0,
  
  logAICall: (tokens) => {
    tokenUsageTracker.totalTokens += tokens || 0;
    tokenUsageTracker.aiCalls += 1;
    console.log(`AI Call #${tokenUsageTracker.aiCalls}: ${tokens || 'unknown'} tokens. Total: ${tokenUsageTracker.totalTokens}`);
  },
  
  logCachedResponse: () => {
    tokenUsageTracker.cachedResponses += 1;
    console.log(`Cached response used. Total cached: ${tokenUsageTracker.cachedResponses}`);
  },
  
  getStats: () => ({
    totalTokens: tokenUsageTracker.totalTokens,
    aiCalls: tokenUsageTracker.aiCalls,
    cachedResponses: tokenUsageTracker.cachedResponses,
    savings: tokenUsageTracker.cachedResponses * 100 // Estimated token savings
  }),
  
  reset: () => {
    tokenUsageTracker.totalTokens = 0;
    tokenUsageTracker.aiCalls = 0;
    tokenUsageTracker.cachedResponses = 0;
  }
};

const AdminTokenUsageDisplay = ({ currentUser }) => {
  const [stats, setStats] = useState(tokenUsageTracker.getStats());
  const [isVisible, setIsVisible] = useState(false);

  const hasAccess =
    !!currentUser &&
    (currentUser.role === 'admin' || currentUser.role === 'teacher');
  
  useEffect(() => {
    if (!hasAccess) return;

    const interval = setInterval(() => {
      setStats(tokenUsageTracker.getStats());
    }, 5000); // Update every 5 seconds
    
    return () => clearInterval(interval);
  }, [hasAccess]);

  // Only show for admins/teachers
  if (!hasAccess) {
    return null;
  }
  
  const toggleVisibility = () => setIsVisible(!isVisible);
  
  if (!isVisible) {
    return (
      <button
        onClick={toggleVisibility}
        className="fixed bottom-4 right-4 bg-purple-500 text-white p-2 rounded-full shadow-lg hover:bg-purple-600 z-50"
        title="Admin: Show Token Usage"
      >
        <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
        </svg>
      </button>
    );
  }
  
  return (
    <div className="fixed bottom-4 right-4 bg-white border border-gray-300 rounded-lg shadow-xl p-4 w-80 z-50">
      <div className="flex justify-between items-center mb-3">
        <h3 className="text-lg font-semibold text-gray-800">Admin: Token Usage & Savings</h3>
        <button
          onClick={toggleVisibility}
          className="text-gray-500 hover:text-gray-700"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
      
      <div className="space-y-3">
        <div className="flex justify-between">
          <span className="text-gray-600">Total AI Calls:</span>
          <span className="font-semibold text-blue-600">{stats.aiCalls}</span>
        </div>
        
        <div className="flex justify-between">
          <span className="text-gray-600">Cached Responses:</span>
          <span className="font-semibold text-green-600">{stats.cachedResponses}</span>
        </div>
        
        <div className="flex justify-between">
          <span className="text-gray-600">Estimated Tokens:</span>
          <span className="font-semibold text-orange-600">{stats.totalTokens.toLocaleString()}</span>
        </div>
        
        <div className="flex justify-between">
          <span className="text-gray-600">Token Savings:</span>
          <span className="font-semibold text-green-600">{stats.savings.toLocaleString()}</span>
        </div>
        
        <div className="pt-2 border-t border-gray-200">
          <div className="flex justify-between">
            <span className="text-gray-600">Cache Hit Rate:</span>
            <span className="font-semibold text-purple-600">
              {stats.aiCalls > 0 ? Math.round((stats.cachedResponses / (stats.aiCalls + stats.cachedResponses)) * 100) : 0}%
            </span>
          </div>
        </div>
      </div>
      
      <div className="mt-3 pt-3 border-t border-gray-200">
        <button
          onClick={() => {
            tokenUsageTracker.reset();
            setStats(tokenUsageTracker.getStats());
          }}
          className="w-full bg-red-500 text-white py-2 px-3 rounded-md text-sm hover:bg-red-600 transition-colors"
        >
          Reset Stats
        </button>
      </div>
    </div>
  );
};

export default AdminTokenUsageDisplay;
export { tokenUsageTracker };
