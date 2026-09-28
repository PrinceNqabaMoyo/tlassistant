/**
 * studentStore.js
 * Reactive, persistent student progression model for Fundile.
 * 
 * Rules & Invariants:
 * - New users start at 0% Formative BKT Mastery and 0% Evaluative Score across all subjects.
 * - Every subject begins in 'diagnostic_required' mode.
 * - Super Admin can reset any individual subject or all subjects to 0% at any time.
 * - Backed by localStorage for immediate local responsiveness, with cross-tab listener dispatch.
 */

const STORAGE_KEY = 'fundile_student_state_v1';

// Base subjects registered in the platform
export const DEFAULT_SUBJECT_IDS = [
  'accounting',
  'mathematics',
  'physical_sciences',
  'business_studies',
  'life_sciences',
  'technical_mathematics',
  'mathematical_literacy',
  'ems',
  'natural_sciences'
];

const createInitialState = () => {
  const subjects = {};
  DEFAULT_SUBJECT_IDS.forEach(id => {
    subjects[id] = {
      id,
      formativeMastery: 0,
      evaluativeScore: 0,
      status: 'diagnostic_required', // 'diagnostic_required' | 'scaffold' | 'practice' | 'exam_ready'
      questionsAttempted: 0,
      questionsPassed: 0,
      xpEarned: 0,
      lastPracticed: null,
      history: []
    };
  });

  const storedPhoto = typeof window !== 'undefined' ? localStorage.getItem('fundile_user_photoURL') : null;
  return {
    studentName: 'Nqobile Dlamini',
    grade: 10,
    school: 'Westville High School',
    photoURL: storedPhoto || null,
    streakDays: 0,
    totalXp: 0,
    deskDues: 0,
    subjects,
    lastUpdated: new Date().toISOString()
  };
};

class StudentStore {
  constructor() {
    this.listeners = new Set();
    this.state = this.loadState();
  }

  loadState() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        // Ensure all registered subjects exist
        const initial = createInitialState();
        parsed.subjects = { ...initial.subjects, ...(parsed.subjects || {}) };
        parsed.photoURL = parsed.photoURL || (typeof window !== 'undefined' ? localStorage.getItem('fundile_user_photoURL') : null);
        return parsed;
      }
    } catch (e) {
      console.warn('Could not parse stored student state, initializing baseline 0% state', e);
    }
    const fresh = createInitialState();
    this.saveState(fresh);
    return fresh;
  }

  saveState(state = this.state) {
    this.state = { ...state, lastUpdated: new Date().toISOString() };
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(this.state));
    } catch (e) {
      console.warn('Failed to save student state to localStorage', e);
    }
    this.notify();
  }

  subscribe(listener) {
    this.listeners.add(listener);
    return () => this.listeners.delete(listener);
  }

  notify() {
    this.listeners.forEach(fn => {
      try {
        fn(this.state);
      } catch (err) {
        console.error('Error notifying studentStore listener:', err);
      }
    });
  }

  getState() {
    return this.state;
  }

  // Update student profile photo
  updateProfilePhoto(photoURL) {
    if (typeof window !== 'undefined' && photoURL) {
      try {
        localStorage.setItem('fundile_user_photoURL', photoURL);
      } catch (e) {
        console.warn('Failed to save profile photo to localStorage', e);
      }
    }
    this.saveState({
      ...this.state,
      photoURL
    });
  }

  getSubject(subjectId) {
    const sId = String(subjectId || '').toLowerCase().replace(/[\s-]+/g, '_');
    const normalized = 
      sId === 'maths' ? 'mathematics' :
      sId === 'mathslit' || sId === 'maths_lit' ? 'mathematical_literacy' :
      sId === 'physics' ? 'physical_sciences' :
      sId === 'business' ? 'business_studies' :
      sId === 'lifesci' ? 'life_sciences' :
      sId === 'techmaths' ? 'technical_mathematics' :
      sId === 'natsci' || sId === 'nat_sci' ? 'natural_sciences' :
      sId;

    return this.state.subjects[normalized] || {
      id: normalized,
      formativeMastery: 0,
      evaluativeScore: 0,
      status: 'diagnostic_required',
      questionsAttempted: 0,
      questionsPassed: 0,
      xpEarned: 0
    };
  }

  // Record a completed question attempt
  recordAttempt(subjectId, { isCorrect, score = 0, totalMarks = 1, xp = 20, mode = 'practice' }) {
    const sId = String(subjectId || '').toLowerCase();
    const normalized = 
      sId === 'maths' ? 'mathematics' :
      sId === 'physics' ? 'physical_sciences' :
      sId === 'business' ? 'business_studies' :
      sId === 'lifesci' ? 'life_sciences' :
      sId === 'techmaths' ? 'technical_mathematics' :
      sId;

    const currentSub = this.getSubject(normalized);
    const pct = totalMarks > 0 ? Math.round((score / totalMarks) * 100) : (isCorrect ? 100 : 0);

    // Exponential Moving Average BKT update
    const alpha = 0.25;
    const newFormative = Math.min(100, Math.max(0, Math.round(currentSub.formativeMastery * (1 - alpha) + pct * alpha)));
    const newEvaluative = mode === 'exam' || mode === 'assessment' 
      ? Math.round(currentSub.evaluativeScore * 0.7 + pct * 0.3)
      : currentSub.evaluativeScore;

    const newStatus = 
      newFormative >= 80 ? 'exam_ready' :
      newFormative >= 60 ? 'practice' :
      newFormative > 0 ? 'scaffold' : 'diagnostic_required';

    const updatedSub = {
      ...currentSub,
      formativeMastery: newFormative,
      evaluativeScore: newEvaluative,
      status: newStatus,
      questionsAttempted: currentSub.questionsAttempted + 1,
      questionsPassed: currentSub.questionsPassed + (isCorrect ? 1 : 0),
      xpEarned: currentSub.xpEarned + xp,
      lastPracticed: new Date().toISOString()
    };

    const newSubjects = {
      ...this.state.subjects,
      [normalized]: updatedSub
    };

    const earnedXp = this.state.totalXp + xp;
    const newStreak = this.state.streakDays === 0 ? 1 : this.state.streakDays;

    this.saveState({
      ...this.state,
      subjects: newSubjects,
      totalXp: earnedXp,
      streakDays: newStreak
    });
  }

  // Complete diagnostic test and assign baseline score
  completeDiagnostic(subjectId, initialScore = 40) {
    const sId = String(subjectId || '').toLowerCase();
    const normalized = 
      sId === 'maths' ? 'mathematics' :
      sId === 'physics' ? 'physical_sciences' :
      sId === 'business' ? 'business_studies' :
      sId === 'lifesci' ? 'life_sciences' :
      sId === 'techmaths' ? 'technical_mathematics' :
      sId;

    const currentSub = this.getSubject(normalized);
    const updatedSub = {
      ...currentSub,
      formativeMastery: initialScore,
      evaluativeScore: Math.round(initialScore * 0.8),
      status: initialScore >= 60 ? 'practice' : 'scaffold',
      lastPracticed: new Date().toISOString()
    };

    this.saveState({
      ...this.state,
      subjects: {
        ...this.state.subjects,
        [normalized]: updatedSub
      }
    });
  }

  // ═══════════════════════════════════════════════════════════
  // SUPER ADMIN TESTING TOOLS
  // ═══════════════════════════════════════════════════════════

  // Reset a single subject to 0% (Diagnostic Required)
  resetSubjectToZero(subjectId) {
    const sId = String(subjectId || '').toLowerCase();
    const normalized = 
      sId === 'maths' ? 'mathematics' :
      sId === 'physics' ? 'physical_sciences' :
      sId === 'business' ? 'business_studies' :
      sId === 'lifesci' ? 'life_sciences' :
      sId === 'techmaths' ? 'technical_mathematics' :
      sId;

    const updatedSub = {
      id: normalized,
      formativeMastery: 0,
      evaluativeScore: 0,
      status: 'diagnostic_required',
      questionsAttempted: 0,
      questionsPassed: 0,
      xpEarned: 0,
      lastPracticed: null,
      history: []
    };

    this.saveState({
      ...this.state,
      subjects: {
        ...this.state.subjects,
        [normalized]: updatedSub
      }
    });
  }

  // Reset all subjects to 0% and clear dues
  resetAllSubjectsToZero() {
    const fresh = createInitialState();
    this.saveState(fresh);
  }

  // Set predefined testing profiles
  setPresetProfile(presetName) {
    if (presetName === 'new_0') {
      this.resetAllSubjectsToZero();
    } else if (presetName === 'intermediate_50') {
      const subjects = {};
      DEFAULT_SUBJECT_IDS.forEach(id => {
        subjects[id] = {
          id,
          formativeMastery: 52,
          evaluativeScore: 48,
          status: 'practice',
          questionsAttempted: 12,
          questionsPassed: 8,
          xpEarned: 420,
          lastPracticed: new Date().toISOString(),
          history: []
        };
      });
      this.saveState({
        ...this.state,
        totalXp: 850,
        streakDays: 3,
        deskDues: 2,
        subjects
      });
    } else if (presetName === 'exam_ready_85') {
      const subjects = {};
      DEFAULT_SUBJECT_IDS.forEach(id => {
        subjects[id] = {
          id,
          formativeMastery: 86,
          evaluativeScore: 82,
          status: 'exam_ready',
          questionsAttempted: 45,
          questionsPassed: 40,
          xpEarned: 1420,
          lastPracticed: new Date().toISOString(),
          history: []
        };
      });
      this.saveState({
        ...this.state,
        totalXp: 2150,
        streakDays: 7,
        deskDues: 0,
        subjects
      });
    }
  }
}

export const studentStore = new StudentStore();
export default studentStore;
