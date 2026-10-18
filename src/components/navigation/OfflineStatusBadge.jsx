import React, { useState, useEffect } from 'react';
import { Wifi, WifiOff, RefreshCw, Zap } from 'lucide-react';
import { telemetryBuffer } from '../../utils/telemetryBuffer';

/**
 * OfflineStatusBadge Component (South African Load Shedding Resilience)
 * Displays real-time connectivity status and pending offline session counts.
 * Allows students to practice with zero anxiety during power outages.
 */
export default function OfflineStatusBadge({ showControls = false }) {
  const [isOnline, setIsOnline] = useState(telemetryBuffer.isOnline());
  const [queuedCount, setQueuedCount] = useState(telemetryBuffer.getQueuedSessionCount());
  const [isSyncing, setIsSyncing] = useState(false);

  useEffect(() => {
    const unsubscribe = telemetryBuffer.subscribe(state => {
      setIsOnline(state.isOnline);
      setQueuedCount(state.queuedCount);
    });
    return unsubscribe;
  }, []);

  const handleManualSync = async () => {
    setIsSyncing(true);
    try {
      await telemetryBuffer.flushOfflineQueue();
      setQueuedCount(telemetryBuffer.getQueuedSessionCount());
    } finally {
      setIsSyncing(false);
    }
  };

  const handleSimulateOffline = () => {
    setIsOnline(false);
    // Queue a mock session to test
    telemetryBuffer.enqueueOfflineSession({
      sessionId: `mock_offline_${Date.now()}`,
      subject: 'Mathematics',
      grade: '10',
      topic: 'Algebraic Expressions',
      score: 0.85,
    });
  };

  const handleSimulateOnline = async () => {
    setIsOnline(true);
    await handleManualSync();
  };

  if (isOnline && queuedCount === 0 && !showControls) {
    return (
      <div
        className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/15 border border-white/25 text-[11px] text-white/90 font-medium"
        title="Connected to Fundile Cloud"
      >
        <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
        <span className="hidden sm:inline">Online</span>
      </div>
    );
  }

  return (
    <div className="inline-flex items-center gap-2">
      {!isOnline || queuedCount > 0 ? (
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/25 border border-amber-300/40 text-xs text-amber-200 font-semibold shadow-xs animate-pulse">
          <Zap className="w-3.5 h-3.5 text-amber-300" />
          <span>
            {!isOnline ? 'Load Shedding Active' : 'Offline Buffer'}: {queuedCount} saved
          </span>
          {isOnline && (
            <button
              onClick={handleManualSync}
              disabled={isSyncing}
              className="ml-1 min-h-[28px] px-2 py-0.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white text-[11px] font-bold flex items-center gap-1 cursor-pointer transition shadow-2xs"
            >
              <RefreshCw className={`w-3 h-3 ${isSyncing ? 'animate-spin' : ''}`} />
              <span>Sync</span>
            </button>
          )}
        </div>
      ) : (
        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-white/15 border border-white/25 text-[11px] text-white/90 font-medium">
          <span className="w-2 h-2 rounded-full bg-emerald-400" />
          <span className="hidden sm:inline">Online</span>
        </div>
      )}

      {showControls && (
        <div className="inline-flex items-center gap-1 text-[10px]">
          <button
            onClick={handleSimulateOffline}
            className="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 cursor-pointer"
          >
            Test Offline
          </button>
          <button
            onClick={handleSimulateOnline}
            className="px-2 py-0.5 rounded bg-emerald-900/60 hover:bg-emerald-800 text-emerald-200 border border-emerald-700 cursor-pointer"
          >
            Test Online
          </button>
        </div>
      )}
    </div>
  );
}
