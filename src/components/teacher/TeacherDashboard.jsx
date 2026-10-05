import React, { useState, useEffect, useMemo } from 'react';
import {
  Users, BookOpen, BarChart3, Plus, Printer,
  Sparkles, AlertTriangle, ShieldCheck, FileText, CheckCircle2,
  Clock, X, Trash2, RefreshCw
} from 'lucide-react';
import {
  STORAGE_KEY,
  getInitialTeacherClasses,
  FIVE_TEST_CLASSES,
  generateCapsTestQuestions
} from './sampleClassesData';
import TeacherRostersTab from './tabs/TeacherRostersTab';
import TeacherAnalyticsTab from './tabs/TeacherAnalyticsTab';
import TeacherAssessmentsTab from './tabs/TeacherAssessmentsTab';
import ClassManagerModal from './ClassManagerModal';
import PrintableTestModal from './PrintableTestModal';

/**
 * TeacherDashboard Component (Educator LMS Cockpit — Clean 3-Tab Architecture)
 * Visuals: Option 1 Light Palette (bg-slate-50 canvas, bg-white cards, #13519C, #FF9100, #10B981, Afacad headings)
 * 3 Primary Tabs:
 *   1. 📋 Rosters (Class cards, 6-char join codes, WhatsApp invites, learner mark book with real photos & POPIA initials)
 *   2. 📊 Analytics (Class Diagnostic Weakness Heatmap, systemic misconception drills, ATP Pacing, Grade distribution)
 *   3. 📝 Assessments & Activities (Author & Generate with diagram blanking & mark lock-in + Submissions review & release toggle)
 */
export default function TeacherDashboard({
  currentUser = { name: 'Mr. N. Sithole', email: 'sithole@school.co.za' },
  onNavigate = () => {},
  db = null
}) {
  // 1. Dynamic class roster state with scoped seeding
  const [classes, setClasses] = useState(() => {
    return getInitialTeacherClasses(currentUser);
  });

  // Active Tab State: 'rosters' | 'analytics' | 'assessments'
  const [activeTab, setActiveTab] = useState('rosters');

  // Sync classes to localStorage
  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(classes));
    } catch (e) {
      console.warn('Unable to persist teacher classes to localStorage:', e);
    }
  }, [classes]);

  // Firestore sync if connected
  useEffect(() => {
    if (!db || !currentUser?.uid) return;
    let isMounted = true;

    async function hydrateFromFirestore() {
      try {
        const { collection, query, where, getDocs } = await import('firebase/firestore');
        const q = query(collection(db, 'classes'), where('teacherId', '==', currentUser.uid));
        const snapshot = await getDocs(q);
        if (!snapshot.empty && isMounted) {
          const remoteClasses = snapshot.docs.map(docSnap => ({
            classId: docSnap.id,
            ...docSnap.data()
          }));
          setClasses(remoteClasses);
        }
      } catch (err) {
        console.warn('Firestore class sync notice:', err);
      }
    }

    hydrateFromFirestore();
    return () => { isMounted = false; };
  }, [db, currentUser?.uid]);

  // Modals & UI interactive states
  const [dispatchedAlert, setDispatchedAlert] = useState(null);
  const [moderatedAvatarToast, setModeratedAvatarToast] = useState(null);
  const [showClassModal, setShowClassModal] = useState(false);
  const [showPrintableModal, setShowPrintableModal] = useState(false);
  const [showQuickCreateModal, setShowQuickCreateModal] = useState(false);
  const [showExamGeneratorModal, setShowExamGeneratorModal] = useState(false);

  // 3-Click Printable Exam State
  const [printableProps, setPrintableProps] = useState({
    title: 'CAPS Classroom Assessment',
    subject: 'Accounting',
    grade: '10',
    term: 1,
    durationMins: 60,
    questions: []
  });

  const [examBuilder, setExamBuilder] = useState({
    subject: 'Accounting',
    grade: '10',
    term: 1,
    marks: 50,
    durationMins: 60,
  });

  // Quick Create Class Form State
  const [newClassForm, setNewClassForm] = useState({
    name: '',
    subject: 'Accounting',
    grade: '10',
    joinCode: 'ACC10B',
  });

  // Teacher Monogram Initials
  const teacherInitials = useMemo(() => {
    return (currentUser?.name || 'N S')
      .split(' ')
      .filter(Boolean)
      .map(n => n[0])
      .join('')
      .slice(0, 2)
      .toUpperCase();
  }, [currentUser?.name]);

  // Aggregate All Students Dynamically
  const allStudents = useMemo(() => {
    return classes.flatMap(cls => 
      (cls.students || []).map(s => ({
        ...s,
        classId: cls.classId,
        className: cls.name,
        classSubject: cls.subject,
        classGrade: cls.grade,
      }))
    );
  }, [classes]);

  // Dynamic KPI Calculations
  const totalLearners = useMemo(() => {
    return classes.reduce((sum, c) => sum + (c.students?.length ?? c.studentCount ?? 0), 0);
  }, [classes]);

  const overallMastery = useMemo(() => {
    if (allStudents.length > 0) {
      const total = allStudents.reduce((sum, s) => sum + (s.score || 0), 0);
      return Math.round(total / allStudents.length);
    }
    if (classes.length > 0) {
      const total = classes.reduce((sum, c) => sum + (c.avgMastery || 0), 0);
      return Math.round(total / classes.length);
    }
    return 0;
  }, [allStudents, classes]);

  const totalHomeworkDue = useMemo(() => {
    return classes.reduce((sum, c) => sum + (c.homeworkDue || c.recentSubmissionCount || 0), 0);
  }, [classes]);

  const activeMisconceptionsCount = useMemo(() => {
    return classes.filter(c => Boolean(c.topMisconception)).length;
  }, [classes]);

  // 1-Click Remedial Micro-Drill Dispatcher
  const handleDispatchDrill = (misconceptionTag, className, learnerCount) => {
    const count = learnerCount || 18;
    setDispatchedAlert(`Assigned 5-minute targeted drill to ${count} learners (${misconceptionTag || 'Core Diagnostic barrier'}) in ${className}`);
    setTimeout(() => setDispatchedAlert(null), 4500);
  };

  // POPIA Child Safety: Reset learner avatar to monogram initials
  const handleResetAvatar = (studentId, studentName) => {
    setClasses(prev => prev.map(cls => ({
      ...cls,
      students: (cls.students || []).map(s => s.id === studentId ? { ...s, photoURL: null } : s)
    })));
    setModeratedAvatarToast(`Avatar for ${studentName} reset to initials (POPIA minor safety policy enforced).`);
    setTimeout(() => setModeratedAvatarToast(null), 4500);
  };

  // Reset or Load Sample CAPS Roster
  const handleLoadSampleRoster = () => {
    setClasses(FIVE_TEST_CLASSES);
    setDispatchedAlert('Loaded authentic 5-class CAPS test suite (Accounting, Maths Alpha, Maths Extended, EMS, Physical Sciences).');
    setTimeout(() => setDispatchedAlert(null), 3500);
  };

  const handleClearAllClasses = () => {
    if (window.confirm('Are you sure you want to clear all classes to test the empty state? You can reload the sample roster anytime.')) {
      setClasses([]);
    }
  };

  // Select class for test generation from roster card
  const handleSelectClassForTest = (cls) => {
    setExamBuilder({
      subject: cls.subject,
      grade: cls.grade,
      term: 1,
      marks: 50,
      durationMins: 60
    });
    setActiveTab('assessments');
  };

  // Handle Quick Create Class Submission
  const handleCreateNewClass = (e) => {
    e.preventDefault();
    if (!newClassForm.name.trim()) return;

    const newCode = newClassForm.joinCode || Math.random().toString(36).substring(2, 8).toUpperCase();
    const newClassItem = {
      classId: `cls_${newClassForm.grade}_${Date.now()}`,
      name: newClassForm.name.trim(),
      subject: newClassForm.subject,
      grade: newClassForm.grade,
      term: 1,
      joinCode: newCode,
      studentCount: 0,
      avgMastery: 0,
      homeworkDue: 0,
      topMisconception: null,
      misconceptionLabel: null,
      recentSubmissionCount: 0,
      students: []
    };

    setClasses(prev => [newClassItem, ...prev]);
    setShowQuickCreateModal(false);
    setNewClassForm({
      name: '',
      subject: 'Accounting',
      grade: '10',
      joinCode: generateRandomJoinCode('Accounting', '10')
    });
    setDispatchedAlert(`Created class "${newClassItem.name}" with Join Code ${newCode}!`);
    setTimeout(() => setDispatchedAlert(null), 3500);
  };

  function generateRandomJoinCode(subj, gr) {
    const prefix = subj === 'Accounting' ? 'ACC' : subj === 'Mathematics' ? 'MAT' : subj === 'Physical Sciences' ? 'PHY' : 'EMS';
    const randChars = Math.random().toString(36).substring(2, 4).toUpperCase();
    return `${prefix}${gr}${randChars}`.slice(0, 6);
  }

  // 3-Click Exam Launch
  const handleLaunch3ClickExam = () => {
    const questions = generateCapsTestQuestions(
      examBuilder.subject,
      examBuilder.grade,
      examBuilder.term,
      examBuilder.marks
    );

    const title = `CAPS Term ${examBuilder.term} ${examBuilder.subject} Standard Assessment`;
    setPrintableProps({
      title,
      subject: examBuilder.subject,
      grade: examBuilder.grade,
      term: examBuilder.term,
      durationMins: examBuilder.durationMins || (examBuilder.marks === 25 ? 30 : examBuilder.marks === 50 ? 60 : 90),
      questions
    });

    setShowExamGeneratorModal(false);
    setShowPrintableModal(true);
  };

  return (
    <div className="w-full min-h-screen bg-slate-50 text-slate-800 p-4 sm:p-6 lg:p-8 space-y-6 font-sans">
      
      {/* 1. TOP HEADER & TEACHER PROFILE BANNER */}
      <header className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200 relative overflow-hidden">
        <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-[#13519C]/5 via-sky-50 to-transparent rounded-full blur-2xl pointer-events-none" />

        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
          <div className="flex items-center gap-4">
            {/* Teacher Monogram */}
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-[#13519C] to-[#2B7BD8] text-white flex items-center justify-center font-bold text-2xl shadow-md ring-4 ring-blue-50 relative shrink-0">
              <span style={{ fontFamily: "'Afacad', sans-serif" }} className="font-bold tracking-tight">
                {teacherInitials}
              </span>
              <span className="absolute -bottom-1 -right-1 bg-emerald-500 text-white text-[9px] font-bold px-1.5 py-0.2 rounded-full uppercase tracking-wider shadow-xs">
                Teacher
              </span>
            </div>

            <div>
              <div className="flex flex-wrap items-center gap-2">
                <h1 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-2xl sm:text-3xl font-bold text-slate-900 tracking-tight"
                >
                  {currentUser.name || 'Educator Portal'}
                </h1>
                <span className="bg-blue-50 border border-blue-200/80 text-[#13519C] text-xs font-semibold px-2.5 py-0.5 rounded-full inline-flex items-center gap-1">
                  <ShieldCheck className="w-3.5 h-3.5" />
                  CAPS LMS Cockpit
                </span>
              </div>
              <p className="text-sm text-slate-500 mt-1 flex flex-wrap items-center gap-2">
                <span className="text-[#13519C] font-semibold">High School Commerce &amp; STEM</span>
                <span>•</span>
                <span>{classes.length} Active Classes</span>
                <span>•</span>
                <span>{totalLearners} Learners Enrolled</span>
              </p>
            </div>
          </div>

          {/* Quick Cockpit Primary Actions */}
          <div className="flex flex-wrap items-center gap-2.5 w-full lg:w-auto">
            <button
              onClick={() => {
                setNewClassForm({
                  name: '',
                  subject: 'Accounting',
                  grade: '10',
                  joinCode: generateRandomJoinCode('Accounting', '10')
                });
                setShowQuickCreateModal(true);
              }}
              className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 bg-[#13519C] hover:bg-[#0f3e77] text-white px-4 py-2.5 rounded-xl font-semibold text-xs transition-all shadow-xs shadow-[#13519C]/20 cursor-pointer"
            >
              <Plus className="w-4 h-4" />
              <span>Create Class</span>
            </button>

            <button
              onClick={() => setShowExamGeneratorModal(true)}
              className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 bg-white hover:bg-slate-50 border border-slate-200/90 text-slate-700 px-4 py-2.5 rounded-xl font-semibold text-xs transition-all shadow-xs hover:border-[#13519C]/40 cursor-pointer"
            >
              <Printer className="w-4 h-4 text-[#13519C]" />
              <span>Print Test &amp; Memo</span>
            </button>

            <button
              onClick={() => onNavigate('classDiagnostics')}
              className="flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 bg-white hover:bg-slate-50 border border-slate-200/90 text-slate-700 px-4 py-2.5 rounded-xl font-semibold text-xs transition-all shadow-xs hover:border-amber-400 cursor-pointer"
            >
              <BarChart3 className="w-4 h-4 text-[#FF9100]" />
              <span>Diagnostic Heatmap</span>
            </button>

            {classes.length > 0 ? (
              currentUser?.isSuperAdmin && (
                <button
                  onClick={handleClearAllClasses}
                  title="Super Admin Test Tool: Clear classes to test empty state"
                  className="p-2.5 rounded-xl border border-slate-200/90 hover:bg-slate-100 text-slate-400 hover:text-rose-600 transition-colors cursor-pointer"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              )
            ) : (
              <button
                onClick={handleLoadSampleRoster}
                className="inline-flex items-center gap-1.5 bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 px-3 py-2 rounded-xl text-xs font-semibold transition cursor-pointer"
              >
                <Sparkles className="w-3.5 h-3.5 text-[#FF9100]" />
                <span>Load CAPS Roster</span>
              </button>
            )}
          </div>
        </div>
      </header>

      {/* Dispatched Drill & Notification Toasts */}
      {dispatchedAlert && (
        <div className="bg-emerald-50 border border-emerald-200 text-emerald-900 p-3.5 rounded-xl text-xs font-semibold flex items-center justify-between shadow-xs animate-in fade-in duration-300">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>{dispatchedAlert}</span>
          </div>
          <button onClick={() => setDispatchedAlert(null)} className="text-emerald-700 hover:text-emerald-950 p-1">
            <X className="w-4 h-4" />
          </button>
        </div>
      )}

      {moderatedAvatarToast && (
        <div className="bg-amber-50 border border-amber-200 text-amber-900 p-3.5 rounded-xl text-xs font-semibold flex items-center justify-between shadow-xs animate-in fade-in duration-300">
          <div className="flex items-center gap-2">
            <AlertTriangle className="w-4 h-4 text-[#FF9100] shrink-0" />
            <span>{moderatedAvatarToast}</span>
          </div>
          <button onClick={() => setModeratedAvatarToast(null)} className="text-amber-800 hover:text-amber-950 p-1">
            <X className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* 2. DYNAMIC OVERVIEW KPI METRIC CARDS */}
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* KPI 1: Total Learners */}
        <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs hover:shadow-md transition-all duration-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider font-sans">Total Learners</span>
            <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center">
              <Users className="w-4 h-4" />
            </div>
          </div>
          <div 
            style={{ fontFamily: "'Afacad', sans-serif" }} 
            className="text-3xl font-bold text-slate-900 mt-2 font-mono"
          >
            {totalLearners}
          </div>
          <p className="text-xs text-slate-500 mt-1">Across {classes.length} registered class rosters</p>
        </div>

        {/* KPI 2: Average Curriculum Mastery */}
        <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs hover:shadow-md transition-all duration-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider font-sans">Average Mastery</span>
            <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center">
              <ShieldCheck className="w-4 h-4" />
            </div>
          </div>
          <div 
            style={{ fontFamily: "'Afacad', sans-serif" }} 
            className="text-3xl font-bold text-emerald-600 mt-2 font-mono"
          >
            {overallMastery}%
          </div>
          <div className="w-full bg-slate-100 rounded-full h-1.5 mt-2 overflow-hidden">
            <div 
              className="bg-emerald-500 h-full rounded-full transition-all duration-500"
              style={{ width: `${Math.min(overallMastery, 100)}%` }}
            />
          </div>
          <p className="text-xs text-slate-500 mt-1">CAPS Target: 65% benchmark</p>
        </div>

        {/* KPI 3: Homework & Submissions Due */}
        <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs hover:shadow-md transition-all duration-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider font-sans">Homework &amp; Submissions</span>
            <div className="w-8 h-8 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center">
              <Clock className="w-4 h-4 text-[#FF9100]" />
            </div>
          </div>
          <div 
            style={{ fontFamily: "'Afacad', sans-serif" }} 
            className="text-3xl font-bold text-amber-700 mt-2 font-mono"
          >
            {totalHomeworkDue} Submissions
          </div>
          <p className="text-xs text-slate-500 mt-1">Due Friday 23:59 • Auto-marked</p>
        </div>

        {/* KPI 4: Active Misconceptions */}
        <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs hover:shadow-md transition-all duration-200">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-500 uppercase tracking-wider font-sans">Active Misconceptions</span>
            <div className="w-8 h-8 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center">
              <AlertTriangle className="w-4 h-4" />
            </div>
          </div>
          <div 
            style={{ fontFamily: "'Afacad', sans-serif" }} 
            className="text-3xl font-bold text-rose-600 mt-2 font-mono"
          >
            {activeMisconceptionsCount} Flagged
          </div>
          <p className="text-xs text-slate-500 mt-1">Ready for 1-click remedial drill</p>
        </div>
      </section>

      {/* 3. PRIMARY 3-TAB NAVIGATION BAR (Item 4) */}
      <nav className="bg-white border border-slate-200/90 rounded-2xl p-1.5 shadow-xs flex items-center justify-start gap-1">
        <button
          onClick={() => setActiveTab('rosters')}
          className={`flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl text-xs font-bold transition cursor-pointer ${
            activeTab === 'rosters'
              ? 'bg-[#13519C] text-white shadow-xs'
              : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
          }`}
        >
          <BookOpen className="w-4 h-4" />
          <span>📋 Rosters</span>
          <span className={`px-2 py-0.2 rounded-full text-[10px] font-mono ${
            activeTab === 'rosters' ? 'bg-white/20 text-white' : 'bg-slate-100 text-slate-600'
          }`}>
            {classes.length}
          </span>
        </button>

        <button
          onClick={() => setActiveTab('analytics')}
          className={`flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl text-xs font-bold transition cursor-pointer ${
            activeTab === 'analytics'
              ? 'bg-[#13519C] text-white shadow-xs'
              : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
          }`}
        >
          <BarChart3 className="w-4 h-4" />
          <span>📊 Analytics</span>
        </button>

        <button
          onClick={() => setActiveTab('assessments')}
          className={`flex-1 sm:flex-initial inline-flex items-center justify-center gap-2 px-6 py-2.5 rounded-xl text-xs font-bold transition cursor-pointer ${
            activeTab === 'assessments'
              ? 'bg-[#13519C] text-white shadow-xs'
              : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
          }`}
        >
          <FileText className="w-4 h-4" />
          <span>📝 Assessments &amp; Activities</span>
        </button>
      </nav>

      {/* 4. ACTIVE TAB CONTENT RENDERING */}
      {activeTab === 'rosters' && (
        <TeacherRostersTab
          classes={classes}
          onOpenCreateClass={() => {
            setNewClassForm({
              name: '',
              subject: 'Accounting',
              grade: '10',
              joinCode: generateRandomJoinCode('Accounting', '10')
            });
            setShowQuickCreateModal(true);
          }}
          onLoadSampleRoster={handleLoadSampleRoster}
          onDispatchDrill={handleDispatchDrill}
          onSelectClassForTest={handleSelectClassForTest}
          onNavigate={onNavigate}
          onResetAvatar={handleResetAvatar}
          teacherName={currentUser?.name || 'Your Teacher'}
        />
      )}

      {activeTab === 'analytics' && (
        <TeacherAnalyticsTab
          classes={classes}
          onDispatchDrill={handleDispatchDrill}
        />
      )}

      {activeTab === 'assessments' && (
        <TeacherAssessmentsTab
          classes={classes}
          currentUser={currentUser}
        />
      )}

      {/* MODAL 1: QUICK CREATE CLASS MODAL */}
      {showQuickCreateModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-in fade-in duration-200">
          <div className="bg-white rounded-2xl border border-slate-200/90 shadow-2xl w-full max-w-md overflow-hidden animate-in zoom-in-95 duration-200">
            <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/60">
              <div className="flex items-center gap-2">
                <div className="p-2 rounded-xl bg-blue-50 text-[#13519C]">
                  <Plus className="w-4 h-4" />
                </div>
                <h3 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-lg font-bold text-slate-900"
                >
                  Create New Class Roster
                </h3>
              </div>
              <button 
                onClick={() => setShowQuickCreateModal(false)}
                className="text-slate-400 hover:text-slate-700 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <form onSubmit={handleCreateNewClass} className="p-6 space-y-4">
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Class Name</label>
                <input
                  type="text"
                  required
                  placeholder="e.g. Grade 10 Accounting (Period 3)"
                  value={newClassForm.name}
                  onChange={e => setNewClassForm(prev => ({ ...prev, name: e.target.value }))}
                  className="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 text-sm text-slate-800 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                />
              </div>

              <div className="grid grid-cols-2 gap-3">
                <div>
                  <label className="block text-xs font-semibold text-slate-600 mb-1">Subject</label>
                  <select
                    value={newClassForm.subject}
                    onChange={e => {
                      const newSubj = e.target.value;
                      setNewClassForm(prev => ({
                        ...prev,
                        subject: newSubj,
                        joinCode: generateRandomJoinCode(newSubj, prev.grade)
                      }));
                    }}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                  >
                    <option value="Accounting">Accounting</option>
                    <option value="Mathematics">Mathematics</option>
                    <option value="EMS">EMS (Gr 8-9)</option>
                    <option value="Physical Sciences">Physical Sciences</option>
                  </select>
                </div>

                <div>
                  <label className="block text-xs font-semibold text-slate-600 mb-1">Grade</label>
                  <select
                    value={newClassForm.grade}
                    onChange={e => {
                      const newGrade = e.target.value;
                      setNewClassForm(prev => ({
                        ...prev,
                        grade: newGrade,
                        joinCode: generateRandomJoinCode(prev.subject, newGrade)
                      }));
                    }}
                    className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                  >
                    <option value="8">Grade 8</option>
                    <option value="9">Grade 9</option>
                    <option value="10">Grade 10</option>
                    <option value="11">Grade 11</option>
                    <option value="12">Grade 12</option>
                  </select>
                </div>
              </div>

              {/* Generated 6-Char Join Code */}
              <div className="bg-slate-50 border border-slate-200 rounded-xl p-3 flex items-center justify-between">
                <div>
                  <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Generated Join Code</div>
                  <div className="font-mono text-lg font-black text-[#13519C] tracking-widest">{newClassForm.joinCode}</div>
                </div>
                <button
                  type="button"
                  onClick={() => setNewClassForm(prev => ({ ...prev, joinCode: generateRandomJoinCode(prev.subject, prev.grade) }))}
                  className="p-1.5 rounded-lg bg-white border border-slate-200 text-slate-600 hover:text-[#13519C] transition-colors text-xs flex items-center gap-1 cursor-pointer"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  <span>Regenerate</span>
                </button>
              </div>

              <div className="pt-2 flex items-center justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setShowQuickCreateModal(false)}
                  className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-semibold shadow-xs"
                >
                  Create Class Roster
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* MODAL 2: 3-CLICK PRINTABLE EXAM & MEMO BUILDER MODAL */}
      {showExamGeneratorModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-in fade-in duration-200">
          <div className="bg-white rounded-2xl border border-slate-200/90 shadow-2xl w-full max-w-lg overflow-hidden animate-in zoom-in-95 duration-200">
            <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/60">
              <div className="flex items-center gap-2">
                <div className="p-2 rounded-xl bg-blue-50 text-[#13519C]">
                  <Printer className="w-4 h-4" />
                </div>
                <div>
                  <h3 
                    style={{ fontFamily: "'Afacad', sans-serif" }}
                    className="text-lg font-bold text-slate-900"
                  >
                    3-Click Printable Exam &amp; Memo Generator
                  </h3>
                  <p className="text-[11px] text-slate-500">Unlimited CAPS question papers with complete marking memorandums</p>
                </div>
              </div>
              <button 
                onClick={() => setShowExamGeneratorModal(false)}
                className="text-slate-400 hover:text-slate-700 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="p-6 space-y-5">
              <div className="space-y-1.5">
                <label className="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                  <span className="w-4 h-4 rounded-full bg-[#13519C] text-white text-[10px] flex items-center justify-center font-bold">1</span>
                  <span>Select Subject, Grade &amp; Term</span>
                </label>
                <div className="grid grid-cols-3 gap-2">
                  <select
                    value={examBuilder.subject}
                    onChange={e => setExamBuilder(prev => ({ ...prev, subject: e.target.value }))}
                    className="px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                  >
                    <option value="Accounting">Accounting</option>
                    <option value="Mathematics">Mathematics</option>
                    <option value="EMS">EMS</option>
                  </select>

                  <select
                    value={examBuilder.grade}
                    onChange={e => setExamBuilder(prev => ({ ...prev, grade: e.target.value }))}
                    className="px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                  >
                    <option value="8">Grade 8</option>
                    <option value="9">Grade 9</option>
                    <option value="10">Grade 10</option>
                    <option value="11">Grade 11</option>
                    <option value="12">Grade 12</option>
                  </select>

                  <select
                    value={examBuilder.term}
                    onChange={e => setExamBuilder(prev => ({ ...prev, term: Number(e.target.value) }))}
                    className="px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                  >
                    <option value={1}>Term 1</option>
                    <option value={2}>Term 2</option>
                    <option value={3}>Term 3</option>
                    <option value={4}>Term 4</option>
                  </select>
                </div>
              </div>

              <div className="space-y-1.5">
                <label className="text-xs font-bold text-slate-700 flex items-center gap-1.5">
                  <span className="w-4 h-4 rounded-full bg-[#13519C] text-white text-[10px] flex items-center justify-center font-bold">2</span>
                  <span>Select Assessment Scope &amp; Marks</span>
                </label>
                <div className="grid grid-cols-2 gap-2">
                  {[
                    { marks: 25, label: 'Quick Diagnostic Quiz', duration: 30 },
                    { marks: 50, label: 'Controlled Class Test', duration: 60 },
                    { marks: 75, label: 'Standard Assessment', duration: 90 },
                    { marks: 100, label: 'Full Term Exam', duration: 120 },
                  ].map(option => (
                    <button
                      key={option.marks}
                      type="button"
                      onClick={() => setExamBuilder(prev => ({ ...prev, marks: option.marks, durationMins: option.duration }))}
                      className={`p-3 rounded-xl border text-left transition cursor-pointer ${
                        examBuilder.marks === option.marks
                          ? 'border-[#13519C] bg-blue-50/70 text-[#13519C] ring-2 ring-[#13519C]/20'
                          : 'border-slate-200 hover:border-slate-300 text-slate-700 bg-white'
                      }`}
                    >
                      <div className="font-mono font-bold text-sm">{option.marks} Marks</div>
                      <div className="text-[11px] text-slate-500">{option.label} ({option.duration}m)</div>
                    </button>
                  ))}
                </div>
              </div>

              <div className="pt-3 border-t border-slate-100 flex items-center justify-end gap-2">
                <button
                  type="button"
                  onClick={() => setShowExamGeneratorModal(false)}
                  className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  onClick={handleLaunch3ClickExam}
                  className="px-5 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold shadow-xs inline-flex items-center gap-2 cursor-pointer"
                >
                  <Sparkles className="w-3.5 h-3.5" />
                  <span>Generate Exam &amp; Memo (Unlimited)</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Class Manager Modal Integration */}
      <ClassManagerModal
        isOpen={showClassModal}
        onClose={() => setShowClassModal(false)}
        teacherId={currentUser?.uid || 'tch_demo_101'}
        teacherName={currentUser?.name || 'Mr. Sithole'}
      />

      {/* Printable Test & Memo Modal Integration */}
      <PrintableTestModal
        isOpen={showPrintableModal}
        onClose={() => setShowPrintableModal(false)}
        testTitle={printableProps.title}
        subject={printableProps.subject}
        grade={printableProps.grade}
        term={printableProps.term}
        durationMins={printableProps.durationMins}
        questions={printableProps.questions}
      />

    </div>
  );
}
