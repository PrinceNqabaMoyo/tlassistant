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
        className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-950/30 border border-emerald-500/20 text-[11px] text-emerald-400 font-medium"
        title="Connected to Fundile Cloud"
      >
        <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
        <span>Online</span>
      </div>
    );
  }

  return (
    <div className="inline-flex items-center gap-2">
      {!isOnline || queuedCount > 0 ? (
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-950/60 border border-amber-500/50 text-xs text-amber-300 font-semibold shadow-sm animate-pulse">
          <Zap className="w-3.5 h-3.5 text-amber-400" />
          <span>
            {!isOnline ? 'Load Shedding Active' : 'Offline Buffer'}: {queuedCount} saved locally
          </span>
          {isOnline && (
            <button
              onClick={handleManualSync}
              disabled={isSyncing}
              className="ml-1 px-1.5 py-0.5 rounded bg-amber-800/80 hover:bg-amber-700 text-white text-[10px] flex items-center gap-1 cursor-pointer"
            >
              <RefreshCw className={`w-2.5 h-2.5 ${isSyncing ? 'animate-spin' : ''}`} />
              Sync
            </button>
          )}
        </div>
      ) : (
        <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-950/30 border border-emerald-500/20 text-[11px] text-emerald-400 font-medium">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
          <span>Online</span>
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
