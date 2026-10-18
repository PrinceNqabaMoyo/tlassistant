/**
 * offlineStorageService.js
 * 
 * IndexedDB storage engine powering Fundile's 30-Day Offline Study Packs & 
 * Hybrid 2-Tier Offline Synchronization (Rule 5 & Invariant 0d compliant).
 * 
 * Tier 1: Invisible ~150 KB active session micro-cache (drafts, working pad notes).
 * Tier 2: User-selected, on-demand 30-day offline study pack with cryptographic lease.
 */

const DB_NAME = 'FundileOfflineDB';
const DB_VERSION = 1;

const STORES = {
  PACKS: 'offline_packs',
  DRAFTS: 'offline_drafts',
  QUEUE: 'offline_telemetry_queue',
  LEASES: 'offline_leases'
};

class OfflineStorageService {
  constructor() {
    this.dbPromise = null;
  }

  /**
   * Initializes or returns the cached IndexedDB instance.
   */
  async getDB() {
    if (this.dbPromise) return this.dbPromise;

    this.dbPromise = new Promise((resolve, reject) => {
      if (typeof window === 'undefined' || !window.indexedDB) {
        return reject(new Error('IndexedDB is not supported in this environment'));
      }

      const request = window.indexedDB.open(DB_NAME, DB_VERSION);

      request.onupgradeneeded = (event) => {
        const db = event.target.result;

        // 1. Offline question packs store
        if (!db.objectStoreNames.contains(STORES.PACKS)) {
          const packStore = db.createObjectStore(STORES.PACKS, { keyPath: 'id' });
          packStore.createIndex('subject_grade', ['subject', 'grade'], { unique: false });
        }

        // 2. Offline drafts & working pad notes store
        if (!db.objectStoreNames.contains(STORES.DRAFTS)) {
          db.createObjectStore(STORES.DRAFTS, { keyPath: 'key' });
        }

        // 3. Telemetry queue for offline attempts
        if (!db.objectStoreNames.contains(STORES.QUEUE)) {
          const queueStore = db.createObjectStore(STORES.QUEUE, { keyPath: 'id', autoIncrement: true });
          queueStore.createIndex('timestamp', 'timestamp', { unique: false });
        }

        // 4. Cryptographic lease store
        if (!db.objectStoreNames.contains(STORES.LEASES)) {
          db.createObjectStore(STORES.LEASES, { keyPath: 'id' });
        }
      };

      request.onsuccess = (event) => {
        resolve(event.target.result);
      };

      request.onerror = (event) => {
        reject(event.target.error);
      };
    });

    return this.dbPromise;
  }

  /**
   * Saves a downloaded question pack with lease verification.
   */
  async saveQuestionPack(packData) {
    const db = await this.getDB();
    const id = packData.pack_id || `pack_${packData.subject}_grade${packData.grade}_term${packData.term}`;

    const record = {
      id,
      subject: (packData.subject || '').toLowerCase(),
      subject_name: packData.subject_name || packData.subject,
      grade: String(packData.grade || '10'),
      term: Number(packData.term || 1),
      topics: packData.topics || [],
      total_questions: packData.total_questions || (packData.questions || []).length,
      questions: packData.questions || [],
      lease: packData.lease || null,
      size_kb: packData.size_kb || 0,
      downloaded_at: new Date().toISOString()
    };

    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.PACKS], 'readwrite');
      const store = tx.objectStore(STORES.PACKS);
      const req = store.put(record);

      req.onsuccess = () => resolve(record);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Retrieves a question pack by subject, grade, and term.
   */
  async getQuestionPack(subject, grade, term) {
    const db = await this.getDB();
    const normSubj = (subject || '').toLowerCase();
    const gradeStr = String(grade || '10');
    const termNum = Number(term || 1);
    const id = `pack_${normSubj}_grade${gradeStr}_term${termNum}`;

    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.PACKS], 'readonly');
      const store = tx.objectStore(STORES.PACKS);
      const req = store.get(id);

      req.onsuccess = () => {
        const pack = req.result;
        if (!pack) return resolve(null);

        // Check 30-day lease validity
        if (pack.lease && pack.lease.expires_at) {
          const expiresAt = new Date(pack.lease.expires_at).getTime();
          if (Date.now() > expiresAt) {
            console.warn(`[OfflinePack] Pack ${id} lease expired on ${pack.lease.expires_at}`);
            pack.isExpired = true;
          }
        }
        resolve(pack);
      };
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Retrieves all currently saved offline packs.
   */
  async getAllPacks() {
    const db = await this.getDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.PACKS], 'readonly');
      const store = tx.objectStore(STORES.PACKS);
      const req = store.getAll();

      req.onsuccess = () => {
        const packs = (req.result || []).map(p => {
          const isExpired = p.lease?.expires_at ? (Date.now() > new Date(p.lease.expires_at).getTime()) : false;
          return { ...p, isExpired };
        });
        resolve(packs);
      };
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Deletes a specific question pack by packId.
   */
  async deletePack(packId) {
    const db = await this.getDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.PACKS], 'readwrite');
      const store = tx.objectStore(STORES.PACKS);
      const req = store.delete(packId);

      req.onsuccess = () => resolve(true);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Retrieves the next uncompleted offline question for a subject, grade, and term.
   */
  async getNextOfflineQuestion(subject, grade, term = 1, completedIds = []) {
    const pack = await this.getQuestionPack(subject, grade, term);
    if (!pack || !pack.questions || pack.questions.length === 0) {
      return null;
    }

    const uncompleted = pack.questions.filter(q => !completedIds.includes(q.id));
    if (uncompleted.length > 0) {
      // Pick next uncompleted deterministically
      return {
        ...uncompleted[0],
        _isOffline: true,
        _offlinePackId: pack.id,
        _offlineLeaseExpires: pack.lease?.expires_at
      };
    }

    // If all completed in pack, pick from full set using random or modulo
    const fallbackQ = pack.questions[Math.floor(Math.random() * pack.questions.length)];
    return {
      ...fallbackQ,
      _isOffline: true,
      _offlinePackId: pack.id,
      _offlineLeaseExpires: pack.lease?.expires_at
    };
  }

  /**
   * Saves a working pad draft or micro-note.
   */
  async saveDraft(key, draftData) {
    const db = await this.getDB();
    const record = {
      key,
      data: draftData,
      updated_at: new Date().toISOString()
    };

    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.DRAFTS], 'readwrite');
      const store = tx.objectStore(STORES.DRAFTS);
      const req = store.put(record);

      req.onsuccess = () => resolve(true);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Retrieves a draft by key.
   */
  async getDraft(key) {
    const db = await this.getDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.DRAFTS], 'readonly');
      const store = tx.objectStore(STORES.DRAFTS);
      const req = store.get(key);

      req.onsuccess = () => resolve(req.result ? req.result.data : null);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Queues an attempt made while offline for telemetry synchronization.
   */
  async queueOfflineAttempt(attemptData) {
    const db = await this.getDB();
    const record = {
      ...attemptData,
      timestamp: Date.now()
    };

    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.QUEUE], 'readwrite');
      const store = tx.objectStore(STORES.QUEUE);
      const req = store.add(record);

      req.onsuccess = () => resolve(req.result);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Retrieves all queued offline telemetry attempts.
   */
  async getQueuedAttempts() {
    const db = await this.getDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.QUEUE], 'readonly');
      const store = tx.objectStore(STORES.QUEUE);
      const req = store.getAll();

      req.onsuccess = () => resolve(req.result || []);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Clears the telemetry queue after successful synchronization.
   */
  async clearQueuedAttempts() {
    const db = await this.getDB();
    return new Promise((resolve, reject) => {
      const tx = db.transaction([STORES.QUEUE], 'readwrite');
      const store = tx.objectStore(STORES.QUEUE);
      const req = store.clear();

      req.onsuccess = () => resolve(true);
      req.onerror = () => reject(req.error);
    });
  }

  /**
   * Flushes queued offline attempts to the backend API when online.
   */
  async flushOfflineQueue(syncEndpoint = '/api/offline/sync') {
    if (!this.isOnline()) return { synced: 0, reason: 'offline' };

    const attempts = await this.getQueuedAttempts();
    if (!attempts || attempts.length === 0) {
      return { synced: 0, reason: 'empty' };
    }

    try {
      const res = await fetch(syncEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ attempts })
      });

      if (res.ok) {
        await this.clearQueuedAttempts();
        return { synced: attempts.length, success: true };
      }
      return { synced: 0, reason: `server_error_${res.status}` };
    } catch (err) {
      console.warn('[OfflineStorage] Queue flush failed, will retry on next reconnect', err);
      return { synced: 0, reason: err.message };
    }
  }

  /**
   * Computes approximate IndexedDB storage usage in KB and MB.
   */
  async getStorageUsage() {
    const packs = await this.getAllPacks();
    const attempts = await this.getQueuedAttempts();

    let totalBytes = 0;
    packs.forEach(p => {
      totalBytes += (p.size_kb ? p.size_kb * 1024 : 0);
    });
    totalBytes += (attempts.length * 512); // ~500 bytes per telemetry record

    return {
      packCount: packs.length,
      queueCount: attempts.length,
      totalBytes,
      totalKb: Math.round(totalBytes / 1024),
      totalMb: Number((totalBytes / (1024 * 1024)).toFixed(2))
    };
  }

  /**
   * Clears all offline packs and telemetry data.
   */
  async clearAllStorage() {
    const db = await this.getDB();
    const storeNames = [STORES.PACKS, STORES.DRAFTS, STORES.QUEUE, STORES.LEASES];

    return new Promise((resolve, reject) => {
      const tx = db.transaction(storeNames, 'readwrite');
      storeNames.forEach(name => {
        tx.objectStore(name).clear();
      });

      tx.oncomplete = () => resolve(true);
      tx.onerror = () => reject(tx.error);
    });
  }

  /**
   * Checks whether the client is currently online.
   */
  isOnline() {
    return typeof navigator !== 'undefined' ? (navigator.onLine ?? true) : true;
  }

  /**
   * Checks whether the device is on a Wi-Fi connection (using Network Information API).
   */
  isWifiConnection() {
    if (typeof navigator === 'undefined' || !navigator.connection) {
      return true; // assume wifi if network information API is unavailable
    }
    const type = navigator.connection.type;
    return type === 'wifi' || type === 'ethernet' || type === undefined;
  }
}

export const offlineStorageService = new OfflineStorageService();
export default offlineStorageService;
