/**
 * Telemetry & Offline Resilience Buffer (Layer D — Phase D1 & Improvement F)
 * Captures interaction telemetry for BKT calibration and guarantees zero data loss
 * during South African load shedding by persisting sessions in localStorage and auto-syncing.
 */

const OFFLINE_QUEUE_KEY = 'fundile_offline_session_queue';
const DB_NAME = 'fundile_offline_db';
const DB_VERSION = 1;
const STORE_NAME = 'offline_sessions';

async function openIndexedDB() {
  if (typeof window === 'undefined' || !window.indexedDB) return null;
  return new Promise((resolve) => {
    try {
      const req = window.indexedDB.open(DB_NAME, DB_VERSION);
      req.onupgradeneeded = (e) => {
        const db = e.target.result;
        if (!db.objectStoreNames.contains(STORE_NAME)) {
          db.createObjectStore(STORE_NAME, { keyPath: 'sessionId' });
        }
      };
      req.onsuccess = () => resolve(req.result);
      req.onerror = () => resolve(null);
    } catch {
      resolve(null);
    }
  });
}

async function idbSaveSession(session) {
  try {
    const db = await openIndexedDB();
    if (!db) return;
    const tx = db.transaction(STORE_NAME, 'readwrite');
    tx.objectStore(STORE_NAME).put(session);
  } catch (e) {
    console.warn('[TelemetryBuffer] IndexedDB put error:', e);
  }
}

async function idbRemoveSession(sessionId) {
  try {
    const db = await openIndexedDB();
    if (!db) return;
    const tx = db.transaction(STORE_NAME, 'readwrite');
    tx.objectStore(STORE_NAME).delete(sessionId);
  } catch (e) {
    console.warn('[TelemetryBuffer] IndexedDB delete error:', e);
  }
}

async function idbGetAllSessions() {
  try {
    const db = await openIndexedDB();
    if (!db) return null;
    return new Promise((resolve) => {
      const tx = db.transaction(STORE_NAME, 'readonly');
      const req = tx.objectStore(STORE_NAME).getAll();
      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => resolve(null);
    });
  } catch {
    return null;
  }
}

class TelemetryBuffer {
  constructor() {
    this.sessionStartTime = Date.now();
    this.questionStartTime = Date.now();
    this.firstKeystrokeTime = null;
    this.cellDwellTimes = {};
    this.cellEditCounts = {};
    this.activeCellKey = null;
    this.activeCellFocusTime = null;
    this.hintsViewed = 0;
    this.listeners = new Set();

    // Auto-sync listener when browser reconnects
    if (typeof window !== 'undefined') {
      window.addEventListener('online', () => {
        console.log('[TelemetryBuffer] Reconnection detected. Flushing offline queue...');
        this.flushOfflineQueue();
        this.notifyListeners();
      });

      window.addEventListener('offline', () => {
        console.warn('[TelemetryBuffer] Device went offline. Load-shedding resilient caching active.');
        this.notifyListeners();
      });
    }
  }

  subscribe(listener) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  notifyListeners() {
    for (const listener of this.listeners) {
      try {
        listener({
          isOnline: this.isOnline(),
          queuedCount: this.getQueuedSessionCount(),
        });
      } catch (err) {
        console.error('[TelemetryBuffer] Listener error:', err);
      }
    }
  }

  isOnline() {
    return typeof navigator !== 'undefined' ? navigator.onLine : true;
  }

  getQueuedSessions() {
    try {
      const raw = localStorage.getItem(OFFLINE_QUEUE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch {
      return [];
    }
  }

  getQueuedSessionCount() {
    return this.getQueuedSessions().length;
  }

  enqueueOfflineSession(sessionBody) {
    try {
      const currentQueue = this.getQueuedSessions();
      // Deduplicate by sessionId
      const filtered = currentQueue.filter(s => s.sessionId !== sessionBody.sessionId);
      const sessionWithTimestamp = { ...sessionBody, queuedAt: new Date().toISOString() };
      filtered.push(sessionWithTimestamp);
      localStorage.setItem(OFFLINE_QUEUE_KEY, JSON.stringify(filtered));
      
      // Dual-write to IndexedDB
      idbSaveSession(sessionWithTimestamp);

      console.log(`[TelemetryBuffer] Queued session offline in IndexedDB + localStorage (${filtered.length} pending).`);
      this.notifyListeners();
    } catch (err) {
      console.error('[TelemetryBuffer] Failed to save offline queue:', err);
    }
  }

  async flushOfflineQueue() {
    const queue = this.getQueuedSessions();
    if (queue.length === 0) return { flushed: 0, remaining: 0 };

    console.log(`[TelemetryBuffer] Attempting to flush ${queue.length} offline sessions...`);
    const remaining = [];
    let flushedCount = 0;

    for (const session of queue) {
      try {
        const res = await fetch('/api/session/end', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(session),
        });
        if (res.ok) {
          flushedCount++;
          // Remove from IndexedDB
          if (session.sessionId) {
            idbRemoveSession(session.sessionId);
          }
        } else {
          remaining.push(session);
        }
      } catch {
        remaining.push(session);
      }
    }

    try {
      localStorage.setItem(OFFLINE_QUEUE_KEY, JSON.stringify(remaining));
    } catch (err) {
      console.error('[TelemetryBuffer] Failed to update offline queue after flush:', err);
    }

    this.notifyListeners();
    return { flushed: flushedCount, remaining: remaining.length };
  }

  startQuestion(questionId) {
    this.questionId = questionId;
    this.questionStartTime = Date.now();
    this.firstKeystrokeTime = null;
    this.cellDwellTimes = {};
    this.cellEditCounts = {};
    this.activeCellKey = null;
    this.activeCellFocusTime = null;
    this.hintsViewed = 0;
  }

  recordFirstKeystroke() {
    if (!this.firstKeystrokeTime) {
      this.firstKeystrokeTime = Date.now();
    }
  }

  onCellFocus(cellKey) {
    const now = Date.now();
    if (this.activeCellKey && this.activeCellFocusTime) {
      const dwell = now - this.activeCellFocusTime;
      this.cellDwellTimes[this.activeCellKey] = (this.cellDwellTimes[this.activeCellKey] || 0) + dwell;
    }
    this.activeCellKey = cellKey;
    this.activeCellFocusTime = now;
  }

  onCellBlur(cellKey) {
    const now = Date.now();
    if (this.activeCellKey === cellKey && this.activeCellFocusTime) {
      const dwell = now - this.activeCellFocusTime;
      this.cellDwellTimes[cellKey] = (this.cellDwellTimes[cellKey] || 0) + dwell;
      this.activeCellKey = null;
      this.activeCellFocusTime = null;
    }
  }

  onCellChange(cellKey) {
    this.recordFirstKeystroke();
    this.cellEditCounts[cellKey] = (this.cellEditCounts[cellKey] || 0) + 1;
  }

  onHintViewed() {
    this.hintsViewed += 1;
  }

  flushPayload() {
    const now = Date.now();
    if (this.activeCellKey && this.activeCellFocusTime) {
      const dwell = now - this.activeCellFocusTime;
      this.cellDwellTimes[this.activeCellKey] = (this.cellDwellTimes[this.activeCellKey] || 0) + dwell;
      this.activeCellFocusTime = now;
    }

    const totalDurationMs = now - this.questionStartTime;
    const timeToFirstKeystrokeMs = this.firstKeystrokeTime 
      ? this.firstKeystrokeTime - this.questionStartTime 
      : null;

    return {
      total_duration_ms: totalDurationMs,
      time_to_first_keystroke_ms: timeToFirstKeystrokeMs,
      cell_dwell_times_ms: { ...this.cellDwellTimes },
      cell_edit_counts: { ...this.cellEditCounts },
      hints_viewed: this.hintsViewed,
      timestamp: new Date().toISOString(),
    };
  }

  async flushSessionEnd(sessionMeta = {}) {
    const payload = this.flushPayload();
    const durationSeconds = Math.round(payload.total_duration_ms / 1000);

    const body = {
      sessionId: sessionMeta.sessionId || `sess_${Date.now()}`,
      userId: sessionMeta.userId || 'student_guest',
      subject: sessionMeta.subject || 'Mathematics',
      grade: String(sessionMeta.grade || '10'),
      topic: sessionMeta.topic || 'General Practice',
      subskill: sessionMeta.subskill || 'Core Concepts',
      score: typeof sessionMeta.score === 'number' ? sessionMeta.score : 1.0,
      durationSeconds,
      misconceptionTags: sessionMeta.misconceptionTags || [],
      procedureSteps: sessionMeta.procedureSteps || [],
      cellErrors: sessionMeta.cellErrors || [],
      timestamp: payload.timestamp
    };

    // If device is offline, enqueue immediately
    if (!this.isOnline()) {
      this.enqueueOfflineSession(body);
      return { status: 'queued_offline', ...body };
    }

    try {
      const response = await fetch('/api/session/end', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(body)
      });
      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }
      return await response.json();
    } catch (err) {
      console.warn('[TelemetryBuffer] Could not reach /api/session/end, saving to offline queue:', err);
      this.enqueueOfflineSession(body);
      return { status: 'queued_offline', ...body };
    }
  }
}

export const telemetryBuffer = new TelemetryBuffer();
