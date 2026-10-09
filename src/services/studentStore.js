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
    isIndependent: false,
    phase: 'FET Phase (Gr 10–12)',
    photoURL: storedPhoto || null,
    streakDays: 5,
    totalXp: 1420,
    deskDues: 2,
    unviewedTaskIds: ['task_acc_1', 'task_math_1'],
    parentLinks: [
      {
        id: 'parent_1',
        name: 'Sipho Dlamini',
        contact: '+27 82 456 7890',
        relationship: 'Father',
        status: 'Linked',
        verified: true,
      }
    ],
    teacherLinks: [
      {
        id: 'teacher_1',
        name: 'Mrs. P. Khumalo',
        subject: 'Accounting',
        code: 'ACC10A',
        school: 'Westville High School'
      },
      {
        id: 'teacher_2',
        name: 'Mr. J. Botha',
        subject: 'Mathematics',
        code: 'MAT10B',
        school: 'Westville High School'
      }
    ],
    messages: [
      {
        id: 'msg_1',
        sender: 'Mrs. P. Khumalo',
        senderRole: 'Teacher',
        subject: 'Accounting',
        text: 'Class task sent from Mrs. P. Khumalo / Accounting: Debtors Journal & Bad Debts, deadline Friday 17:00.',
        date: new Date().toLocaleDateString('en-ZA', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
        deadline: new Date(Date.now() + 86400000 * 2).toISOString(),
        isRead: false
      },
      {
        id: 'msg_2',
        sender: 'Fundile Learning Team',
        senderRole: 'Fundile',
        subject: 'Platform',
        text: 'Welcome to Term 1 Benchmark Week! Remember to complete your diagnostic benchmark in your registered subjects.',
        date: new Date().toLocaleDateString('en-ZA', { month: 'short', day: 'numeric' }),
        deadline: null,
        isRead: true
      }
    ],
    activeSession: {
      subjectId: 'accounting',
      topic: 'Cash Receipts Journal (VAT 15%)',
      progressionMode: 'diagnostic',
      lastActiveTab: 'desk',
      lastUpdated: new Date().toISOString()
    },
    subjects,
    lastUpdated: new Date().toISOString()
  };
};

/**
 * Returns dynamic greeting based on exact South African time:
 * - 00:00 – 11:59: "Good morning"
 * - 12:00 – 17:30: "Good afternoon"
 * - 17:31 – 23:59: "Good evening"
 */
export const getTimeGreeting = (date = new Date()) => {
  const totalMinutes = date.getHours() * 60 + date.getMinutes();
  if (totalMinutes < 720) {
    return 'Good morning';
  } else if (totalMinutes <= 1050) {
    return 'Good afternoon';
  } else {
    return 'Good evening';
  }
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
        parsed.activeSession = parsed.activeSession || initial.activeSession;
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

  // Active Session Persistence (Resume where learner left off)
  setActiveSession({ subjectId, topic, progressionMode, lastActiveTab }) {
    const prev = this.state.activeSession || {};
    const updated = {
      subjectId: subjectId || prev.subjectId || 'accounting',
      topic: topic !== undefined ? topic : (prev.topic || null),
      progressionMode: progressionMode || prev.progressionMode || 'diagnostic',
      lastActiveTab: lastActiveTab !== undefined ? lastActiveTab : (prev.lastActiveTab || 'desk'),
      lastUpdated: new Date().toISOString()
    };
    this.saveState({
      ...this.state,
      activeSession: updated
    });
    return updated;
  }

  getActiveSession() {
    return this.state.activeSession || {
      subjectId: 'accounting',
      topic: 'Cash Receipts Journal (VAT 15%)',
      progressionMode: 'diagnostic',
      lastActiveTab: 'desk',
      lastUpdated: new Date().toISOString()
    };
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

  // Update student profile details
  updateProfileDetails({ studentName, grade, school, isIndependent }) {
    const updatedGrade = grade !== undefined ? Number(grade) : this.state.grade;
    const phase = updatedGrade >= 10 ? 'FET Phase (Gr 10–12)' : 'Senior Phase (Gr 7–9)';
    this.saveState({
      ...this.state,
      studentName: studentName || this.state.studentName,
      grade: updatedGrade,
      phase,
      school: school !== undefined ? school : this.state.school,
      isIndependent: isIndependent !== undefined ? Boolean(isIndependent) : Boolean(this.state.isIndependent),
    });
  }

  // Mark task as opened/viewed (stops red shading and blinking count circle immediately)
  markTaskViewed(taskId) {
    if (!taskId) return;
    const unviewed = this.state.unviewedTaskIds || [];
    if (!unviewed.includes(taskId)) return;
    const nextUnviewed = unviewed.filter(id => id !== taskId);
    this.saveState({
      ...this.state,
      unviewedTaskIds: nextUnviewed
    });
  }

  isTaskUnviewed(taskId) {
    if (!taskId) return false;
    const unviewed = this.state.unviewedTaskIds || [];
    return unviewed.includes(taskId);
  }

  // Manage up to 2 parent links
  addParentLink(parentData) {
    const current = this.state.parentLinks || [];
    if (current.length >= 2) {
      throw new Error('Maximum of 2 parental links allowed.');
    }
    const newParent = {
      id: `parent_${Date.now()}`,
      name: parentData.name || 'Parent / Guardian',
      contact: parentData.contact || '',
      relationship: parentData.relationship || 'Guardian',
      status: 'Linked',
      verified: true,
      ...parentData
    };
    this.saveState({
      ...this.state,
      parentLinks: [...current, newParent]
    });
    return newParent;
  }

  removeParentLink(parentId) {
    const current = this.state.parentLinks || [];
    this.saveState({
      ...this.state,
      parentLinks: current.filter(p => p.id !== parentId)
    });
  }

  // Manage teacher links
  joinTeacherClass(code) {
    const normalizedCode = String(code || '').trim().toUpperCase();
    if (!normalizedCode) return false;
    const current = this.state.teacherLinks || [];
    const exists = current.some(t => t.code === normalizedCode);
    if (exists) return true;

    // Detect subject from join code prefix
    let subject = 'Curriculum Practice';
    let teacherName = `Educator (${normalizedCode})`;
    if (normalizedCode === 'MTH701') {
      subject = 'Mathematics';
      teacherName = 'Mrs. Patience Khumalo';
    } else if (normalizedCode.startsWith('ACC')) subject = 'Accounting';
    else if (normalizedCode.startsWith('MAT') || normalizedCode.startsWith('MTH')) subject = 'Mathematics';
    else if (normalizedCode.startsWith('PHY')) subject = 'Physical Sciences';
    else if (normalizedCode.startsWith('BUS')) subject = 'Business Studies';
    else if (normalizedCode.startsWith('EMS')) subject = 'EMS';

    const newTeacher = {
      id: `teacher_${Date.now()}`,
      name: teacherName,
      subject,
      code: normalizedCode,
      school: this.state.school || 'Westville High School'
    };

    let updatedTasks = this.state.currentUser?.assignedTasks || [];
    let updatedGrade = this.state.grade;
    let updatedPhase = this.state.phase;
    let unviewed = this.state.unviewedTaskIds || [];

    if (normalizedCode === 'MTH701') {
      updatedGrade = 7;
      updatedPhase = 'Senior Phase (Gr 7–9)';
      updatedTasks = [
        {
          id: 'task_g7_pat',
          subject: 'mathematics',
          subjectName: 'Mathematics',
          title: 'Grade 7 Number Patterns (Tn = 4n - 1)',
          topic: 'Numeric and Geometric Patterns',
          assignedBy: 'Mrs. Patience Khumalo',
          dueText: 'DUE TODAY',
          dueTime: '16:00',
          marks: 5,
          notes: 'Mrs. Khumalo assigned 5 marks patterns practice.',
          estimatedMins: 10
        },
        {
          id: 'task_g7_div',
          subject: 'mathematics',
          subjectName: 'Mathematics',
          title: 'Whole Numbers: Long Division Algorithm',
          topic: 'Working with Whole Numbers',
          subskill: 'long_division',
          assignedBy: 'Mrs. Patience Khumalo',
          dueText: 'DUE TOMORROW',
          dueTime: '08:30',
          marks: 4,
          notes: 'Mrs. Khumalo • 4 Marks • Column division procedure practice.',
          estimatedMins: 8
        }
      ];
      unviewed = ['task_g7_pat', 'task_g7_div'];
    }

    this.saveState({
      ...this.state,
      grade: updatedGrade,
      phase: updatedPhase,
      teacherLinks: [...current, newTeacher],
      currentUser: {
        ...(this.state.currentUser || {}),
        assignedTasks: updatedTasks,
      },
      unviewedTaskIds: unviewed,
    });
    return true;
  }

  // Message Board: auto-deletes 3 days after deadline
  addMessage(msg) {
    const current = this.state.messages || [];
    const newMsg = {
      id: `msg_${Date.now()}`,
      sender: msg.sender || 'Teacher',
      senderRole: msg.senderRole || 'Teacher',
      subject: msg.subject || 'Class Notice',
      text: msg.text || '',
      date: new Date().toLocaleDateString('en-ZA', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
      deadline: msg.deadline || null,
      isRead: false,
      ...msg
    };
    this.saveState({
      ...this.state,
      messages: [newMsg, ...current]
    });
    return newMsg;
  }

  getValidMessages() {
    const now = Date.now();
    const threeDaysMs = 3 * 24 * 60 * 60 * 1000;
    const current = this.state.messages || [];
    // Filter out messages that had a deadline and are more than 3 days past the deadline
    return current.filter(msg => {
      if (!msg.deadline) return true;
      const deadlineTime = new Date(msg.deadline).getTime();
      if (isNaN(deadlineTime)) return true;
      return now <= (deadlineTime + threeDaysMs);
    });
  }

  markMessageRead(msgId) {
    const current = this.state.messages || [];
    const updated = current.map(m => m.id === msgId ? { ...m, isRead: true } : m);
    this.saveState({
      ...this.state,
      messages: updated
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
    const nextActiveSession = {
      ...(this.state.activeSession || {}),
      subjectId: normalized,
      progressionMode: mode,
      lastUpdated: new Date().toISOString()
    };

    this.saveState({
      ...this.state,
      subjects: newSubjects,
      totalXp: earnedXp,
      streakDays: newStreak,
      activeSession: nextActiveSession
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
