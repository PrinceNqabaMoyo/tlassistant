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
  let initialEnabledSubjects = null;
  try {
    const saved = localStorage.getItem('fundile_enabled_subjects');
    if (saved) initialEnabledSubjects = JSON.parse(saved);
  } catch {}
  if (!initialEnabledSubjects || !Array.isArray(initialEnabledSubjects) || initialEnabledSubjects.length === 0) {
    initialEnabledSubjects = ['accounting', 'mathematics', 'physical_sciences', 'life_sciences'];
  }

  return {
    studentName: 'Nqobile Dlamini',
    grade: 10,
    school: 'Westville High School',
    isIndependent: false,
    subscription: {
      plan: 'term_pass',
      status: 'active',
      totalMonths: 3,
      paidAmountRands: 349,
      activatedAt: new Date(Date.now() - 20 * 86400000).toISOString(),
      expiresAt: new Date(Date.now() + 70 * 86400000).toISOString()
    },
    familyWallet: {
      creditBalanceRands: 0,
      pendingRefundClaims: []
    },
    phase: 'FET Phase (Gr 10–12)',
    photoURL: storedPhoto || null,
    enabledSubjects: initialEnabledSubjects,
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
    teacherLinks: [],
    messages: [],
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
        parsed.enabledSubjects = (Array.isArray(parsed.enabledSubjects) && parsed.enabledSubjects.length > 0)
          ? parsed.enabledSubjects
          : initial.enabledSubjects;
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

  setState(partialState) {
    this.saveState({
      ...this.state,
      ...partialState
    });
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

  // Reactive enabled phase subjects management
  getEnabledSubjects(grade = null) {
    if (this.state.enabledSubjects && Array.isArray(this.state.enabledSubjects) && this.state.enabledSubjects.length > 0) {
      return this.state.enabledSubjects;
    }
    try {
      const saved = localStorage.getItem('fundile_enabled_subjects');
      if (saved) {
        const parsed = JSON.parse(saved);
        if (Array.isArray(parsed) && parsed.length > 0) {
          return parsed;
        }
      }
    } catch {}
    const g = Number(grade || this.state.grade || 10);
    return g <= 9
      ? ['mathematics', 'ems', 'natural_sciences']
      : ['accounting', 'mathematics', 'physical_sciences', 'life_sciences'];
  }

  setEnabledSubjects(subjects) {
    if (!Array.isArray(subjects) || subjects.length === 0) return;
    try {
      localStorage.setItem('fundile_enabled_subjects', JSON.stringify(subjects));
    } catch {}
    this.saveState({
      ...this.state,
      enabledSubjects: subjects
    });
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

  setStudentProfile(studentName, grade, school) {
    this.updateProfileDetails({ studentName, grade, school });
  }

  // Set student grade directly (Grades 7–12)
  setGrade(grade) {
    if (grade !== undefined && grade !== null) {
      this.updateProfileDetails({ grade: Number(grade) });
    }
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

    const resolvedSchool = (this.state.school && this.state.school !== 'Independent Homeschool Learner' && this.state.school !== 'Independent Homeschool' && this.state.school !== 'Independent Account')
      ? this.state.school
      : 'Westville High School';

    const newTeacher = {
      id: `teacher_${Date.now()}`,
      name: teacherName,
      subject,
      code: normalizedCode,
      school: resolvedSchool
    };

    let updatedTasks = Array.isArray(this.state.currentUser?.assignedTasks) ? [...this.state.currentUser.assignedTasks] : [];
    let updatedGrade = this.state.grade;
    let updatedPhase = this.state.phase;
    let unviewed = Array.isArray(this.state.unviewedTaskIds) ? [...this.state.unviewedTaskIds] : [];

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
    } else if (normalizedCode.startsWith('ACC')) {
      const accTask = {
        id: `task_acc_${Date.now()}`,
        subject: 'accounting',
        subjectName: 'Accounting',
        title: 'Cash Receipts Journal (VAT 15%)',
        topic: 'Cash Receipts Journal (VAT 15%)',
        assignedBy: teacherName,
        dueText: 'DUE TODAY',
        dueTime: '17:00',
        marks: 12,
        notes: `${teacherName} • 12 Marks • Enter transactions into 2D ledger columns.`,
        estimatedMins: 15
      };
      updatedTasks = [accTask, ...updatedTasks.filter(t => t.title !== accTask.title)];
      unviewed = [accTask.id, ...unviewed];
    } else if (normalizedCode.startsWith('MAT') || normalizedCode.startsWith('MTH')) {
      const matTask = {
        id: `task_mat_${Date.now()}`,
        subject: 'mathematics',
        subjectName: 'Mathematics',
        title: 'Quadratic Trinomial Factorisation',
        topic: 'Algebraic Expressions',
        assignedBy: teacherName,
        dueText: 'DUE TOMORROW',
        dueTime: '08:30',
        marks: 10,
        notes: `${teacherName} • 10 Marks • Factorise trinomial expressions stepwise.`,
        estimatedMins: 12
      };
      updatedTasks = [matTask, ...updatedTasks.filter(t => t.title !== matTask.title)];
      unviewed = [matTask.id, ...unviewed];
    } else if (normalizedCode.startsWith('PHY')) {
      const phyTask = {
        id: `task_phy_${Date.now()}`,
        subject: 'physical_sciences',
        subjectName: 'Physical Sciences',
        title: 'Vectors & Resultants in Two Dimensions',
        topic: 'Vectors in Two Dimensions',
        assignedBy: teacherName,
        dueText: 'DUE TODAY',
        dueTime: '16:00',
        marks: 8,
        notes: `${teacherName} • 8 Marks • Calculate resultant vector and directional bearing.`,
        estimatedMins: 12
      };
      updatedTasks = [phyTask, ...updatedTasks.filter(t => t.title !== phyTask.title)];
      unviewed = [phyTask.id, ...unviewed];
    } else {
      const genericTask = {
        id: `task_gen_${Date.now()}`,
        subject: subject.toLowerCase().replace(/\s+/g, '_'),
        subjectName: subject,
        title: `${subject} Core Procedural Practice`,
        topic: 'Foundational Drill',
        assignedBy: teacherName,
        dueText: 'DUE TODAY',
        dueTime: '17:00',
        marks: 10,
        notes: `${teacherName} • Active class assignment.`,
        estimatedMins: 15
      };
      updatedTasks = [genericTask, ...updatedTasks.filter(t => t.title !== genericTask.title)];
      unviewed = [genericTask.id, ...unviewed];
    }

    this.saveState({
      ...this.state,
      isIndependent: false,
      school: resolvedSchool,
      grade: updatedGrade,
      phase: updatedPhase,
      deskDues: updatedTasks.length,
      teacherLinks: [...current, newTeacher],
      currentUser: {
        ...(this.state.currentUser || {}),
        isIndependent: false,
        school: resolvedSchool,
        schoolName: resolvedSchool,
        assignedTasks: updatedTasks,
      },
      unviewedTaskIds: unviewed,
    });
    return true;
  }

  // Set Independent Mode for testing / onboarding
  setIndependentMode(isIndependent = true, plan = 'term_pass') {
    const totalMonths = plan === 'annual_pass' ? 12 : plan === 'term_pass' ? 3 : 1;
    const paidAmount = plan === 'annual_pass' ? 999 : plan === 'term_pass' ? 349 : 149;
    this.saveState({
      ...this.state,
      isIndependent,
      schoolId: isIndependent ? null : (this.state.schoolId || 'sch_westville_high'),
      school: isIndependent ? 'Independent Homeschool Learner' : 'Westville High School',
      subscription: {
        plan,
        status: 'active',
        totalMonths,
        paidAmountRands: paidAmount,
        activatedAt: new Date(Date.now() - 20 * 86400000).toISOString(),
        expiresAt: new Date(Date.now() + (totalMonths * 30 - 20) * 86400000).toISOString()
      }
    });
  }

  // Institutional Transition & Refund Calculation
  // Policy: Within active month is forfeited; remaining un-activated full months trigger refund claim.
  transitionIndependentToSchool(passkey, schoolInfo = {}) {
    const sub = this.state.subscription || { plan: 'term_pass', totalMonths: 3, paidAmountRands: 349 };
    const totalMonths = sub.totalMonths || (sub.plan === 'annual_pass' ? 12 : sub.plan === 'term_pass' ? 3 : 1);
    const paidAmount = sub.paidAmountRands || (totalMonths === 12 ? 999 : totalMonths === 3 ? 349 : 149);

    const now = Date.now();
    const activatedTime = sub.activatedAt ? new Date(sub.activatedAt).getTime() : (now - 20 * 86400000);
    const daysElapsed = Math.max(1, Math.floor((now - activatedTime) / (1000 * 60 * 60 * 24)));
    const monthsElapsed = Math.ceil(daysElapsed / 30); // 1-based current active month

    const unactivatedMonths = Math.max(0, totalMonths - monthsElapsed);
    let refundAmount = 0;
    if (unactivatedMonths > 0) {
      refundAmount = Math.round((paidAmount * (unactivatedMonths / totalMonths)) * 100) / 100;
    }

    const claimId = `ref_claim_${Date.now()}`;
    const refundClaim = {
      id: claimId,
      passkey,
      schoolName: schoolInfo.name || 'Westville High School',
      totalPlanMonths: totalMonths,
      monthsUsed: monthsElapsed,
      unactivatedMonths,
      paidAmountRands: paidAmount,
      refundAmountRands: refundAmount,
      claimDate: new Date().toISOString(),
      status: refundAmount > 0 ? 'queued_for_disbursement' : 'forfeited_final_month',
      policyNote: refundAmount > 0 
        ? `Month ${monthsElapsed} active (forfeited). ${unactivatedMonths} un-activated month(s) queued for refund to guardian.`
        : 'Active month access utilized (forfeited). Zero un-activated months remaining.'
    };

    const updatedRefunds = [refundClaim, ...(this.state.familyWallet?.pendingRefundClaims || [])];
    const updatedMessages = [
      {
        id: `msg_ref_${Date.now()}`,
        sender: 'Fundile Billing & Administration',
        senderRole: 'Billing',
        subject: 'Institutional Transition & Refund Notice',
        text: `Your school (${schoolInfo.name || 'Westville High School'}) has subscribed institutionally. ` +
              (refundAmount > 0
                ? `Your retail pass has been transitioned. Current month was forfeited; ${unactivatedMonths} un-activated month(s) totaling R${refundAmount.toFixed(2)} have been queued for refund to your guardian.`
                : 'Your retail pass has been transitioned to the school institutional license. Current active month was forfeited.'),
        date: new Date().toLocaleDateString('en-ZA', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' }),
        deadline: null,
        isRead: false
      },
      ...(this.state.messages || [])
    ];

    this.saveState({
      ...this.state,
      isIndependent: false,
      schoolId: schoolInfo.id || 'sch_westville_high',
      school: schoolInfo.name || 'Westville High School',
      subscription: {
        ...sub,
        status: 'transitioned_to_school',
        transitionedAt: new Date().toISOString(),
        passkeyUsed: passkey
      },
      familyWallet: {
        ...(this.state.familyWallet || {}),
        pendingRefundClaims: updatedRefunds
      },
      messages: updatedMessages
    });

    return refundClaim;
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

  markAllMessagesRead() {
    const current = this.state.messages || [];
    const updated = current.map(m => ({ ...m, isRead: true }));
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
      newFormative >= 60 ? 'practice' : 'scaffold';

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

  // Award XP directly (e.g. from Post-Exam Triage or SimuLearn completion)
  awardXP(amount = 50) {
    const currentXp = this.state.totalXp || 0;
    this.saveState({
      ...this.state,
      totalXp: currentXp + amount
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
      status: initialScore >= 80 ? 'exam_ready' : initialScore >= 60 ? 'practice' : 'scaffold',
      questionsAttempted: Math.max(1, (currentSub.questionsAttempted || 0) + 1),
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
    this.resetAllProgress();
  }

  // Full progression reset to 0% baseline (Item 7)
  resetAllProgress() {
    const fresh = createInitialState();
    const isInd = Boolean(this.state.isIndependent);
    const updated = {
      ...fresh,
      isIndependent: isInd,
      school: isInd ? 'Independent Homeschool' : 'Westville High School',
      teacherLinks: isInd ? [] : fresh.teacherLinks,
      deskDues: 0,
      unviewedTaskIds: [],
      messages: [],
      streakDays: 0,
      totalXp: 0,
      hasFailedExam: false,
      triageRecord: null
    };
    this.saveState(updated);

    // Clean up draft storage keys
    if (typeof window !== 'undefined') {
      try {
        Object.keys(localStorage).forEach((key) => {
          if (key.startsWith('fundile_draft_') || key.startsWith('fundile_offline_draft_')) {
            localStorage.removeItem(key);
          }
        });
        Object.keys(sessionStorage).forEach((key) => {
          if (key.startsWith('fundile_draft_')) {
            sessionStorage.removeItem(key);
          }
        });
      } catch (e) {}
    }
    return updated;
  }

  // Super Admin switch for independent vs institutional learner (Item 1)
  setEnrolmentType(isIndependent) {
    const isInd = Boolean(isIndependent);
    this.saveState({
      ...this.state,
      isIndependent: isInd,
      school: isInd ? 'Independent Homeschool' : (this.state.school && this.state.school !== 'Independent Homeschool' ? this.state.school : 'Westville High School'),
      teacherLinks: isInd ? [] : (this.state.teacherLinks?.length ? this.state.teacherLinks : createInitialState().teacherLinks),
      deskDues: isInd ? 0 : this.state.deskDues,
      unviewedTaskIds: isInd ? [] : this.state.unviewedTaskIds
    });
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
