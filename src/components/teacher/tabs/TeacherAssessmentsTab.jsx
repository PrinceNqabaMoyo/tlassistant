import React, { useState, useMemo } from 'react';
import {
  FileText, Sparkles, Check, CheckCircle2, Lock, Unlock,
  Printer, Send, Clock, AlertTriangle, ShieldCheck, ChevronDown,
  ChevronUp, CheckSquare, Square, Eye, Edit3, ArrowRight, RefreshCw
} from 'lucide-react';
import { generateCapsTestQuestions } from '../sampleClassesData';
import PrintableTestModal from '../PrintableTestModal';

// Anatomical parts for Life Sciences / Natural Sciences Alimentary Canal Diagram
const ALIMENTARY_CANAL_PARTS = [
  { id: 'mouth', label: 'A: Mouth & Salivary Glands', organ: 'Mouth / Salivary Glands', defaultBlank: true, functionText: 'Mechanical mastication and secretion of salivary amylase (starch digestion).' },
  { id: 'oesophagus', label: 'B: Oesophagus', organ: 'Oesophagus', defaultBlank: false, functionText: 'Transports bolus to stomach via involuntary peristaltic muscular contractions.' },
  { id: 'stomach', label: 'C: Stomach', organ: 'Stomach', defaultBlank: true, functionText: 'Secretes hydrochloric acid (pH 2) and pepsinogen to digest proteins into peptides.' },
  { id: 'liver', label: 'D: Liver & Gallbladder', organ: 'Liver', defaultBlank: true, functionText: 'Produces bile which is stored in gallbladder to emulsify fats and neutralise acidic chyme.' },
  { id: 'pancreas', label: 'E: Pancreas', organ: 'Pancreas', defaultBlank: true, functionText: 'Secretes pancreatic juice containing trypsin, lipase, and amylase into duodenum.' },
  { id: 'small_intestine', label: 'F: Small Intestine (Duodenum/Ileum)', organ: 'Small Intestine', defaultBlank: true, functionText: 'Primary site of chemical digestion and villi-mediated nutrient absorption into bloodstream.' },
  { id: 'large_intestine', label: 'G: Large Intestine (Colon)', organ: 'Large Intestine', defaultBlank: false, functionText: 'Reabsorbs water, mineral salts, and vitamins, forming compacted faeces.' }
];

// Mock Student Submissions
const INITIAL_SUBMISSIONS = [
  {
    id: 'sub_1',
    studentId: 's2',
    studentName: 'Lerato Dlamini',
    studentPhoto: 'https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=120&q=80',
    className: 'Grade 10 Accounting (Period 2)',
    assessmentTitle: 'VAT Output & Input Calculation Assessment',
    assessmentType: 'Controlled Test',
    submittedAt: 'Today, 14:15',
    status: 'pending_review', // pending_review | released
    releasePolicy: 'review_first', // instant | review_first
    autoScore: 11,
    teacherAdjustedScore: 11,
    totalMarks: 15,
    percentage: 73,
    answers: [
      { qNum: 1, type: 'calculation', studentAnswer: 'Output VAT = R4 500, Exclusive Sales = R30 000', expectedAnswer: 'Output VAT = R4 500, Exclusive Sales = R30 000', marksAwarded: 5, maxMarks: 5, autoCorrect: true },
      { qNum: 2, type: 'calculation', studentAnswer: 'Input VAT = R2 760 (used 15% instead of 15/115)', expectedAnswer: 'Input VAT = R2 400', marksAwarded: 2, maxMarks: 5, autoCorrect: false, misconception: 'net_vs_gross_confusion' },
      { qNum: 3, type: 'stepwise', studentAnswer: 'Owes SARS R1 740', expectedAnswer: 'Apex owes SARS R2 100', marksAwarded: 4, maxMarks: 5, autoCorrect: false }
    ],
    teacherNote: 'Careful with VAT inclusive purchase: always divide by 115, not 100.'
  },
  {
    id: 'sub_2',
    studentId: 's7',
    studentName: 'Naledi Sithole',
    studentPhoto: 'https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=120&q=80',
    className: 'Grade 10 Mathematics — Alpha',
    assessmentTitle: 'Term 1 Algebraic Factoring & Trinomials Quiz',
    assessmentType: 'Quiz',
    submittedAt: 'Today, 11:30',
    status: 'pending_review',
    releasePolicy: 'review_first',
    autoScore: 18,
    teacherAdjustedScore: 18,
    totalMarks: 25,
    percentage: 72,
    answers: [
      { qNum: 1, type: 'mcq', studentAnswer: 'Option B: 3(x - 2)(x + 2)', expectedAnswer: 'Option B: 3(x - 2)(x + 2)', marksAwarded: 4, maxMarks: 4, autoCorrect: true },
      { qNum: 2, type: 'stepwise', studentAnswer: '2x² + 5x - 3 = (2x - 3)(x + 1)', expectedAnswer: '(2x - 1)(x + 3)', marksAwarded: 2, maxMarks: 6, autoCorrect: false, misconception: 'sign_error_distribution' },
      { qNum: 3, type: 'stepwise', studentAnswer: 'x = 3/2 or x = -4', expectedAnswer: 'x = 3/2 or x = -4', marksAwarded: 12, maxMarks: 15, autoCorrect: true }
    ],
    teacherNote: 'Check the signs of the cross terms before expanding!'
  },
  {
    id: 'sub_3',
    studentId: 's18',
    studentName: 'Khaya Cele',
    studentPhoto: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=120&q=80',
    className: 'Grade 10 Physical Sciences (Physics & Chem)',
    assessmentTitle: 'Digestive Anatomy & Waves Joint Assessment',
    assessmentType: 'Assignment',
    submittedAt: 'Yesterday, 16:45',
    status: 'released',
    releasePolicy: 'instant',
    autoScore: 14,
    teacherAdjustedScore: 14,
    totalMarks: 15,
    percentage: 93,
    answers: [
      { qNum: 1, type: 'diagram', studentAnswer: 'A: Mouth, C: Stomach, D: Liver, E: Pancreas, F: Small Intestine', expectedAnswer: 'All 5 blanks correct', marksAwarded: 10, maxMarks: 10, autoCorrect: true },
      { qNum: 2, type: 'stepwise', studentAnswer: 'v = fλ => 12 = f(0,8) => f = 15 Hz', expectedAnswer: '15 Hz', marksAwarded: 4, maxMarks: 5, autoCorrect: true }
    ],
    teacherNote: 'Excellent precision on anatomical labeling.'
  }
];

export default function TeacherAssessmentsTab({
  classes = [],
  currentUser = { name: 'Mr. N. Sithole' }
}) {
  // Top-level mode inside this tab: 'author' | 'submissions'
  const [activeSubMode, setActiveSubMode] = useState('author');

  // Assessment Builder State
  const [assessmentScope, setAssessmentScope] = useState({
    title: 'Term 1 Controlled Assessment',
    type: 'Controlled Test', // Exam | Controlled Test | Quiz | Assignment
    subject: 'Accounting',
    grade: '10',
    term: 1,
    marks: 50,
    durationMins: 60,
    targetClassId: classes[0]?.classId || 'all',
    releasePolicy: 'review_first' // 'instant' | 'review_first'
  });

  // Generated Questions in Inspector
  const [questions, setQuestions] = useState(() => {
    return generateCapsTestQuestions('Accounting', '10', 1, 50).map((q, idx) => ({
      ...q,
      questionNum: idx + 1,
      format: q.type === 'diagram' ? 'diagram' : 'stepwise', // 'mcq' | 'stepwise' | 'fill_in' | 'diagram'
      lockedMarks: true,
      userAllocatedMarks: q.marks,
      suggestedMarks: q.marks,
      memoVisible: true
    }));
  });

  // Diagram Blanking State for Digestive System
  const [blankedParts, setBlankedParts] = useState({
    mouth: true,
    oesophagus: false,
    stomach: true,
    liver: true,
    pancreas: true,
    small_intestine: true,
    large_intestine: false
  });

  // Submissions State
  const [submissions, setSubmissions] = useState(INITIAL_SUBMISSIONS);
  const [submissionFilter, setSubmissionFilter] = useState('all');
  const [inspectingSub, setInspectingSub] = useState(null);
  const [feedbackToast, setFeedbackToast] = useState(null);
  const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);

  // Regenerate questions when subject/grade/marks change
  const handleRegenerateQuestions = (newSubject, newGrade, newTerm, newMarks) => {
    const raw = generateCapsTestQuestions(newSubject, newGrade, newTerm, newMarks);
    setQuestions(raw.map((q, idx) => ({
      ...q,
      questionNum: idx + 1,
      format: q.type === 'diagram' ? 'diagram' : 'stepwise',
      lockedMarks: true,
      userAllocatedMarks: q.marks,
      suggestedMarks: q.marks,
      memoVisible: true
    })));
  };

  // Toggle blanking on a diagram part
  const togglePartBlank = (partId) => {
    setBlankedParts(prev => {
      const next = { ...prev, [partId]: !prev[partId] };
      // Recalculate suggested marks for any diagram question
      const blankCount = Object.values(next).filter(Boolean).length;
      const newSuggested = (blankCount * 2) + 2; // 2 marks per blank + 2 function marks
      setQuestions(qList => qList.map(q => {
        if (q.format === 'diagram') {
          return {
            ...q,
            suggestedMarks: newSuggested,
            userAllocatedMarks: q.lockedMarks ? q.userAllocatedMarks : newSuggested
          };
        }
        return q;
      }));
      return next;
    });
  };

  // Count active blanks
  const activeBlankCount = useMemo(() => {
    return Object.values(blankedParts).filter(Boolean).length;
  }, [blankedParts]);

  // Lock / Unlock marks for a question
  const toggleLockMarks = (qIndex) => {
    setQuestions(prev => prev.map((q, idx) => {
      if (idx === qIndex) {
        return { ...q, lockedMarks: !q.lockedMarks };
      }
      return q;
    }));
  };

  // Change question format (MCQ, Stepwise, Fill-in, Diagram)
  const handleChangeFormat = (qIndex, newFormat) => {
    setQuestions(prev => prev.map((q, idx) => {
      if (idx === qIndex) {
        let suggested = q.suggestedMarks;
        if (newFormat === 'mcq') suggested = 4;
        else if (newFormat === 'fill_in') suggested = 6;
        else if (newFormat === 'diagram') suggested = (activeBlankCount * 2) + 2;
        else suggested = 15;

        return {
          ...q,
          format: newFormat,
          suggestedMarks: suggested,
          userAllocatedMarks: q.lockedMarks ? q.userAllocatedMarks : suggested
        };
      }
      return q;
    }));
  };

  // Publish assessment action
  const handlePublishAssessment = () => {
    const totalMarks = questions.reduce((sum, q) => sum + (Number(q.userAllocatedMarks) || 0), 0);
    const targetClass = classes.find(c => c.classId === assessmentScope.targetClassId)?.name || 'all registered classes';
    const authorName = currentUser?.name || 'Educator';
    setFeedbackToast(`Successfully published "${assessmentScope.title}" (${totalMarks} Marks by ${authorName}) to ${targetClass}!`);
    setTimeout(() => setFeedbackToast(null), 4500);
  };

  // Release student marks
  const handleReleaseMarks = (submissionId) => {
    setSubmissions(prev => prev.map(s => {
      if (s.id === submissionId) {
        return { ...s, status: 'released' };
      }
      return s;
    }));
    if (inspectingSub?.id === submissionId) {
      setInspectingSub(prev => ({ ...prev, status: 'released' }));
    }
    setFeedbackToast('Marks approved and released! Learner and parents can now view the official score and worked memo.');
    setTimeout(() => setFeedbackToast(null), 4000);
  };

  // Filtered submissions
  const filteredSubmissions = useMemo(() => {
    return submissions.filter(s => {
      if (submissionFilter === 'pending') return s.status === 'pending_review';
      if (submissionFilter === 'released') return s.status === 'released';
      return true;
    });
  }, [submissions, submissionFilter]);

  const pendingCount = submissions.filter(s => s.status === 'pending_review').length;

  return (
    <div className="space-y-6 animate-in fade-in duration-200">

      {/* Sub-Mode Toggle Switcher */}
      <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 bg-white p-2 rounded-2xl border border-slate-200/90 shadow-xs">
        <div className="flex items-center gap-2">
          <button
            onClick={() => setActiveSubMode('author')}
            className={`flex-1 sm:flex-initial inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-bold transition cursor-pointer ${
              activeSubMode === 'author'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
            }`}
          >
            <Edit3 className="w-4 h-4" />
            <span>Author &amp; Generate Assessment</span>
          </button>

          <button
            onClick={() => setActiveSubMode('submissions')}
            className={`flex-1 sm:flex-initial inline-flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-bold transition cursor-pointer relative ${
              activeSubMode === 'submissions'
                ? 'bg-[#13519C] text-white shadow-xs'
                : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
            }`}
          >
            <FileText className="w-4 h-4" />
            <span>Submissions &amp; Mark Review</span>
            {pendingCount > 0 && (
              <span className="ml-1.5 px-2 py-0.5 rounded-full text-[10px] font-black bg-[#FF9100] text-white font-mono shadow-xs">
                {pendingCount}
              </span>
            )}
          </button>
        </div>

        <div className="flex items-center gap-2 px-2">
          <span className="text-xs text-slate-500 font-sans hidden md:inline">
            Formal Assessment Task (FAT) Engine
          </span>
        </div>
      </div>

      {/* Feedback Toast */}
      {feedbackToast && (
        <div className="bg-emerald-50 border border-emerald-200 text-emerald-900 p-3.5 rounded-xl text-xs font-semibold flex items-center justify-between shadow-xs animate-in fade-in duration-300">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>{feedbackToast}</span>
          </div>
          <button onClick={() => setFeedbackToast(null)} className="text-emerald-700 hover:text-emerald-950 font-bold p-1">
            ✕
          </button>
        </div>
      )}

      {/* ───────────────────────────────────────────────────────────── */}
      {/* SUB-MODE 1: AUTHOR & GENERATE ASSESSMENT                      */}
      {/* ───────────────────────────────────────────────────────────── */}
      {activeSubMode === 'author' && (
        <div className="space-y-6">

          {/* 1. Assessment Parameters & Scope Bar */}
          <section className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200">
            <div className="flex items-center justify-between mb-4 border-b border-slate-100 pb-3">
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-[#13519C]" />
                <h3 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-lg font-bold text-slate-900 tracking-tight"
                >
                  Assessment Scope &amp; Target Specifications
                </h3>
              </div>
              <span className="text-xs font-semibold text-[#13519C] bg-blue-50 border border-blue-200/80 px-2.5 py-0.5 rounded-full">
                Grades 7–12 Curriculum Standards
              </span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {/* Title */}
              <div className="md:col-span-2">
                <label className="block text-xs font-semibold text-slate-600 mb-1">Assessment Title</label>
                <input
                  type="text"
                  value={assessmentScope.title}
                  onChange={e => setAssessmentScope(prev => ({ ...prev, title: e.target.value }))}
                  className="w-full px-3.5 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                />
              </div>

              {/* Assessment Type */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Assessment Type</label>
                <select
                  value={assessmentScope.type}
                  onChange={e => setAssessmentScope(prev => ({ ...prev, type: e.target.value }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                >
                  <option value="Exam">📝 Full Term Exam</option>
                  <option value="Controlled Test">⏱️ Controlled Test</option>
                  <option value="Quiz">⚡ Quick Diagnostic Quiz</option>
                  <option value="Assignment">📋 Homework / Assignment</option>
                </select>
              </div>

              {/* Subject */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Subject</label>
                <select
                  value={assessmentScope.subject}
                  onChange={e => {
                    const nextSubj = e.target.value;
                    setAssessmentScope(prev => ({ ...prev, subject: nextSubj }));
                    handleRegenerateQuestions(nextSubj, assessmentScope.grade, assessmentScope.term, assessmentScope.marks);
                  }}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                >
                  <option value="Accounting">Accounting</option>
                  <option value="Mathematics">Mathematics</option>
                  <option value="EMS">EMS (Gr 8–9)</option>
                  <option value="Physical Sciences">Physical Sciences</option>
                  <option value="Life Sciences">Life Sciences</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
              {/* Grade */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Grade</label>
                <select
                  value={assessmentScope.grade}
                  onChange={e => {
                    const nextGr = e.target.value;
                    setAssessmentScope(prev => ({ ...prev, grade: nextGr }));
                    handleRegenerateQuestions(assessmentScope.subject, nextGr, assessmentScope.term, assessmentScope.marks);
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

              {/* Term */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Term</label>
                <select
                  value={assessmentScope.term}
                  onChange={e => {
                    const nextT = Number(e.target.value);
                    setAssessmentScope(prev => ({ ...prev, term: nextT }));
                    handleRegenerateQuestions(assessmentScope.subject, assessmentScope.grade, nextT, assessmentScope.marks);
                  }}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C]"
                >
                  <option value={1}>Term 1</option>
                  <option value={2}>Term 2</option>
                  <option value={3}>Term 3</option>
                  <option value={4}>Term 4</option>
                </select>
              </div>

              {/* Target Marks */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Target Marks</label>
                <select
                  value={assessmentScope.marks}
                  onChange={e => {
                    const nextM = Number(e.target.value);
                    setAssessmentScope(prev => ({ ...prev, marks: nextM, durationMins: nextM === 25 ? 30 : nextM === 50 ? 60 : 90 }));
                    handleRegenerateQuestions(assessmentScope.subject, assessmentScope.grade, assessmentScope.term, nextM);
                  }}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C] font-mono"
                >
                  <option value={25}>25 Marks (Diagnostic)</option>
                  <option value={50}>50 Marks (Controlled)</option>
                  <option value={75}>75 Marks (Standard)</option>
                  <option value={100}>100 Marks (Full Exam)</option>
                </select>
              </div>

              {/* Duration */}
              <div>
                <label className="block text-xs font-semibold text-slate-600 mb-1">Duration (Mins)</label>
                <input
                  type="number"
                  value={assessmentScope.durationMins}
                  onChange={e => setAssessmentScope(prev => ({ ...prev, durationMins: Number(e.target.value) }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-[#13519C] font-mono"
                />
              </div>
            </div>

            {/* 2. Mark Release Policy Toggle (Item 6) */}
            <div className="mt-5 pt-4 border-t border-slate-100">
              <label className="block text-xs font-bold text-slate-800 mb-2">
                Mark Release Policy (Control how and when learners see marks):
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <button
                  type="button"
                  onClick={() => setAssessmentScope(prev => ({ ...prev, releasePolicy: 'instant' }))}
                  className={`p-3.5 rounded-xl border text-left transition cursor-pointer flex items-start gap-3 ${
                    assessmentScope.releasePolicy === 'instant'
                      ? 'border-[#13519C] bg-blue-50/70 ring-2 ring-[#13519C]/20'
                      : 'border-slate-200 hover:border-slate-300 bg-white'
                  }`}
                >
                  <div className="p-2 rounded-lg bg-emerald-50 text-emerald-700 shrink-0 mt-0.5">
                    <Sparkles className="w-4 h-4" />
                  </div>
                  <div>
                    <div className="font-bold text-xs text-slate-900">⚡ Instant Release (Automated)</div>
                    <div className="text-[11px] text-slate-500 mt-0.5">
                      Learners receive immediate marks &amp; worked memos upon submission. Best for formative quizzes &amp; practice.
                    </div>
                  </div>
                </button>

                <button
                  type="button"
                  onClick={() => setAssessmentScope(prev => ({ ...prev, releasePolicy: 'review_first' }))}
                  className={`p-3.5 rounded-xl border text-left transition cursor-pointer flex items-start gap-3 ${
                    assessmentScope.releasePolicy === 'review_first'
                      ? 'border-[#13519C] bg-blue-50/70 ring-2 ring-[#13519C]/20'
                      : 'border-slate-200 hover:border-slate-300 bg-white'
                  }`}
                >
                  <div className="p-2 rounded-lg bg-amber-50 text-amber-700 shrink-0 mt-0.5">
                    <ShieldCheck className="w-4 h-4" />
                  </div>
                  <div>
                    <div className="font-bold text-xs text-slate-900">📋 Teacher Review First (Held for Approval)</div>
                    <div className="text-[11px] text-slate-500 mt-0.5">
                      Engine marks in background, but marks stay locked until teacher inspects, adjusts, and approves them.
                    </div>
                  </div>
                </button>
              </div>
            </div>
          </section>

          {/* 3. Question-by-Question Inspector */}
          <section className="space-y-4">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <FileText className="w-5 h-5 text-[#13519C]" />
                <h3 
                  style={{ fontFamily: "'Afacad', sans-serif" }}
                  className="text-xl font-bold text-slate-900 tracking-tight"
                >
                  Question-by-Question Inspector &amp; Modality Customiser
                </h3>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs text-slate-500 font-mono">
                  Total Allocated: {questions.reduce((sum, q) => sum + (Number(q.userAllocatedMarks) || 0), 0)} Marks
                </span>
              </div>
            </div>

            {questions.map((q, qIdx) => (
              <div
                key={q.id || qIdx}
                className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200 space-y-4"
              >
                {/* Question Header & Format Switcher */}
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-slate-100 pb-4">
                  <div className="flex items-center gap-3">
                    <span className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] border border-blue-200/80 flex items-center justify-center font-bold text-sm font-mono shrink-0">
                      Q{q.questionNum}
                    </span>
                    <div>
                      <h4 className="font-bold text-slate-900 text-sm">
                        Question {q.questionNum}
                      </h4>
                      <p className="text-[11px] text-slate-500">
                        {q.format === 'diagram' ? 'Diagram Labeling & Anatomy' : 'Procedural Working & Rubric'}
                      </p>
                    </div>
                  </div>

                  {/* Format Pills: MCQ | Stepwise | Fill-in | Diagram */}
                  <div className="flex flex-wrap items-center gap-1.5 bg-slate-50 p-1 rounded-xl border border-slate-200/70">
                    {[
                      { id: 'mcq', label: '🔘 MCQ' },
                      { id: 'stepwise', label: '✍️ Stepwise' },
                      { id: 'fill_in', label: '📝 Fill-in' },
                      { id: 'diagram', label: '🏷️ Diagram Labeling' },
                    ].map(fmt => (
                      <button
                        key={fmt.id}
                        type="button"
                        onClick={() => handleChangeFormat(qIdx, fmt.id)}
                        className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                          q.format === fmt.id
                            ? 'bg-white text-[#13519C] shadow-2xs border border-slate-200/80 font-bold'
                            : 'text-slate-600 hover:text-slate-900'
                        }`}
                      >
                        {fmt.label}
                      </button>
                    ))}
                  </div>

                  {/* Intelligent Suggested Mark Allocation & Lock-in (Item 5) */}
                  <div className="flex items-center gap-2">
                    <div className="flex items-center gap-1.5 bg-amber-50 border border-amber-200/90 px-2.5 py-1 rounded-lg text-xs text-amber-900 font-mono">
                      <Sparkles className="w-3.5 h-3.5 text-[#FF9100]" />
                      <span>Suggested: {q.suggestedMarks} Marks</span>
                    </div>

                    <div className="flex items-center gap-1">
                      <input
                        type="number"
                        disabled={q.lockedMarks}
                        value={q.userAllocatedMarks}
                        onChange={e => {
                          const val = Number(e.target.value);
                          setQuestions(prev => prev.map((item, idx) => idx === qIdx ? { ...item, userAllocatedMarks: val } : item));
                        }}
                        className={`w-16 px-2 py-1 rounded-lg border text-center font-mono font-bold text-xs ${
                          q.lockedMarks
                            ? 'bg-slate-50 border-slate-200 text-slate-700'
                            : 'bg-white border-[#13519C] text-[#13519C] focus:ring-1 focus:ring-[#13519C]'
                        }`}
                      />
                      <button
                        type="button"
                        onClick={() => toggleLockMarks(qIdx)}
                        className={`p-1.5 rounded-lg border text-xs font-semibold transition cursor-pointer flex items-center gap-1 ${
                          q.lockedMarks
                            ? 'bg-emerald-50 border-emerald-200 text-emerald-800'
                            : 'bg-amber-50 border-amber-200 text-amber-900'
                        }`}
                        title={q.lockedMarks ? 'Click to edit mark allocation' : 'Click to lock marks'}
                      >
                        {q.lockedMarks ? (
                          <>
                            <Lock className="w-3.5 h-3.5 text-emerald-600" />
                            <span className="text-[10px]">Locked</span>
                          </>
                        ) : (
                          <>
                            <Unlock className="w-3.5 h-3.5 text-[#FF9100]" />
                            <span className="text-[10px]">Lock</span>
                          </>
                        )}
                      </button>
                    </div>
                  </div>
                </div>

                {/* Question Prompt */}
                <div className="bg-slate-50/70 border border-slate-200/80 rounded-xl p-4 text-xs text-slate-800 leading-relaxed font-sans whitespace-pre-line">
                  {q.question_text}
                </div>

                {/* ───────────────────────────────────────────────────────── */}
                {/* INTERACTIVE DIAGRAM BLANKING MODULE (Item 5)               */}
                {/* ───────────────────────────────────────────────────────── */}
                {q.format === 'diagram' && (
                  <div className="border border-blue-200/80 bg-blue-50/30 rounded-xl p-5 space-y-4">
                    <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-blue-100 pb-3">
                      <div>
                        <div className="text-xs font-bold text-[#13519C] uppercase tracking-wider flex items-center gap-1.5">
                          <CheckSquare className="w-4 h-4 text-[#13519C]" />
                          <span>Interactive Diagram Blanking (Alimentary Canal / Digestive Tract)</span>
                        </div>
                        <p className="text-[11px] text-slate-500 mt-0.5">
                          Check parts to <strong>Leave Blank for Students to Label</strong>. Uncheck to provide as given clues.
                        </p>
                      </div>

                      {/* Presets */}
                      <div className="flex items-center gap-1.5">
                        <button
                          type="button"
                          onClick={() => {
                            const all = {};
                            ALIMENTARY_CANAL_PARTS.forEach(p => { all[p.id] = true; });
                            setBlankedParts(all);
                          }}
                          className="px-2 py-1 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 text-[10px] font-bold rounded-md transition cursor-pointer"
                        >
                          Blank All (7)
                        </button>
                        <button
                          type="button"
                          onClick={() => {
                            setBlankedParts({
                              mouth: false,
                              oesophagus: false,
                              stomach: true,
                              liver: true,
                              pancreas: true,
                              small_intestine: false,
                              large_intestine: false
                            });
                          }}
                          className="px-2 py-1 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 text-[10px] font-bold rounded-md transition cursor-pointer"
                        >
                          Core Glands Only (3)
                        </button>
                      </div>
                    </div>

                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-5 items-start">
                      {/* Interactive Anatomical Checklist */}
                      <div className="space-y-2">
                        {ALIMENTARY_CANAL_PARTS.map((part) => {
                          const isBlank = blankedParts[part.id];
                          return (
                            <div
                              key={part.id}
                              onClick={() => togglePartBlank(part.id)}
                              className={`p-2.5 rounded-xl border text-xs transition cursor-pointer flex items-center justify-between ${
                                isBlank
                                  ? 'bg-amber-50/70 border-amber-200 text-amber-950 font-semibold'
                                  : 'bg-white border-slate-200 text-slate-600 hover:bg-slate-50'
                              }`}
                            >
                              <div className="flex items-center gap-2.5">
                                {isBlank ? (
                                  <CheckSquare className="w-4 h-4 text-[#FF9100] shrink-0" />
                                ) : (
                                  <Square className="w-4 h-4 text-slate-300 shrink-0" />
                                )}
                                <div>
                                  <div className="font-bold text-slate-900">{part.label}</div>
                                  <div className="text-[10px] text-slate-500 font-sans font-normal truncate max-w-xs">
                                    {part.functionText}
                                  </div>
                                </div>
                              </div>

                              <span className={`px-2 py-0.5 rounded-full text-[10px] font-bold uppercase tracking-wider shrink-0 ${
                                isBlank
                                  ? 'bg-[#FF9100] text-white'
                                  : 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                              }`}>
                                {isBlank ? 'Blanked [?]' : 'Given Clue'}
                              </span>
                            </div>
                          );
                        })}
                      </div>

                      {/* Visual SVG Diagram Canvas Preview */}
                      <div className="bg-white border border-slate-200/90 rounded-xl p-4 flex flex-col items-center justify-center relative shadow-xs min-h-[320px]">
                        <div className="text-[11px] font-bold text-slate-500 uppercase tracking-wider mb-2 text-center">
                          Student Exam View Preview (Live Diagram Callouts)
                        </div>

                        {/* Interactive Vector Anatomy Illustration */}
                        <div className="relative w-full max-w-sm h-64 border border-slate-100 rounded-lg p-2 flex flex-col justify-between bg-slate-50/40">
                          {/* Top: Mouth & Oesophagus */}
                          <div className="flex justify-between items-center text-xs">
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.mouth ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              A: {blankedParts.mouth ? '[ ? Blank Label ]' : 'Mouth & Salivary Glands'}
                            </span>
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.oesophagus ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              B: {blankedParts.oesophagus ? '[ ? Blank Label ]' : 'Oesophagus'}
                            </span>
                          </div>

                          {/* Middle: Stomach & Liver */}
                          <div className="flex justify-between items-center text-xs">
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.liver ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              D: {blankedParts.liver ? '[ ? Blank Label ]' : 'Liver & Gallbladder'}
                            </span>
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.stomach ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              C: {blankedParts.stomach ? '[ ? Blank Label ]' : 'Stomach'}
                            </span>
                          </div>

                          {/* Pancreas */}
                          <div className="text-center">
                            <span className={`px-2.5 py-1 rounded-md border text-[11px] font-mono font-bold inline-block ${
                              blankedParts.pancreas ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              E: {blankedParts.pancreas ? '[ ? Blank Label ]' : 'Pancreas'}
                            </span>
                          </div>

                          {/* Bottom: Small & Large Intestine */}
                          <div className="flex justify-between items-center text-xs">
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.small_intestine ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              F: {blankedParts.small_intestine ? '[ ? Blank Label ]' : 'Small Intestine'}
                            </span>
                            <span className={`px-2 py-1 rounded-md border text-[11px] font-mono font-bold ${
                              blankedParts.large_intestine ? 'border-dashed border-amber-400 bg-amber-50 text-amber-900' : 'bg-emerald-50 text-emerald-800 border-emerald-200'
                            }`}>
                              G: {blankedParts.large_intestine ? '[ ? Blank Label ]' : 'Large Intestine'}
                            </span>
                          </div>
                        </div>

                        <div className="mt-3 text-[11px] text-slate-500 font-mono text-center">
                          {activeBlankCount} blanks selected • Suggested: {(activeBlankCount * 2) + 2} Marks
                        </div>
                      </div>
                    </div>
                  </div>
                )}

                {/* Worked Memorandum & Rubric */}
                <div className="border border-slate-200/80 rounded-xl overflow-hidden">
                  <div className="bg-slate-50 px-4 py-2.5 flex items-center justify-between border-b border-slate-200/80">
                    <span className="text-xs font-bold text-slate-700 uppercase tracking-wider flex items-center gap-1.5">
                      <ShieldCheck className="w-4 h-4 text-emerald-600" />
                      <span>Worked Memorandum &amp; Marking Points</span>
                    </span>
                    <button
                      type="button"
                      onClick={() => setQuestions(prev => prev.map((item, idx) => idx === qIdx ? { ...item, memoVisible: !item.memoVisible } : item))}
                      className="text-slate-500 hover:text-slate-800 text-xs font-semibold flex items-center gap-1 cursor-pointer"
                    >
                      {q.memoVisible ? <ChevronUp className="w-4 h-4" /> : <ChevronDown className="w-4 h-4" />}
                      <span>{q.memoVisible ? 'Collapse Memo' : 'Expand Memo'}</span>
                    </button>
                  </div>

                  {q.memoVisible && (
                    <div className="p-4 space-y-3 bg-white text-xs text-slate-700">
                      <div className="p-3 bg-emerald-50/50 border border-emerald-200/70 rounded-lg text-emerald-900 whitespace-pre-line font-mono">
                        {q.solution}
                      </div>

                      {q.marking_scheme && (
                        <div className="space-y-1.5 pt-2">
                          <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500">NSC Method &amp; Accuracy Breakdown:</span>
                          <div className="divide-y divide-slate-100 border border-slate-200 rounded-lg overflow-hidden">
                            {q.marking_scheme.map((pt, ptIdx) => (
                              <div key={ptIdx} className="px-3 py-2 flex items-center justify-between bg-white text-xs">
                                <span>{pt.point}</span>
                                <span className="font-mono font-bold text-[#13519C] bg-blue-50 px-2 py-0.5 rounded text-[11px]">
                                  {pt.marks} Marks
                                </span>
                              </div>
                            ))}
                          </div>
                        </div>
                      )}
                    </div>
                  )}
                </div>

              </div>
            ))}
          </section>

          {/* Assessment Bottom Actions */}
          <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div className="text-xs text-slate-500">
              Ready to deploy to enrolled classes or export as official print-ready exam paper.
            </div>

            <div className="flex flex-wrap items-center gap-3">
              <button
                type="button"
                onClick={() => setIsPrintModalOpen(true)}
                className="px-4 py-2.5 bg-white hover:bg-slate-50 border border-slate-200 text-slate-700 text-xs font-bold rounded-xl shadow-xs transition flex items-center gap-2 cursor-pointer"
              >
                <Printer className="w-4 h-4 text-[#13519C]" />
                <span>Printable Test &amp; Memo</span>
              </button>

              <button
                type="button"
                onClick={handlePublishAssessment}
                className="px-5 py-2.5 bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold rounded-xl shadow-xs transition flex items-center gap-2 cursor-pointer"
              >
                <Send className="w-4 h-4" />
                <span>Publish Assessment to Class</span>
              </button>
            </div>
          </div>

        </div>
      )}

      {/* ───────────────────────────────────────────────────────────── */}
      {/* SUB-MODE 2: STUDENT SUBMISSIONS & MARK REVIEW (Item 6)        */}
      {/* ───────────────────────────────────────────────────────────── */}
      {activeSubMode === 'submissions' && (
        <div className="space-y-6">

          {/* Submissions Filter Toolbar */}
          <div className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h3 
                style={{ fontFamily: "'Afacad', sans-serif" }}
                className="text-lg font-bold text-slate-900 tracking-tight"
              >
                Student Assessment Submissions
              </h3>
              <p className="text-xs text-slate-500">
                Review automated grades, inspect student diagram label inputs, adjust discretionary marks, and release results.
              </p>
            </div>

            <div className="flex items-center gap-2">
              {[
                { id: 'all', label: 'All Submissions' },
                { id: 'pending', label: `Pending Review (${pendingCount})` },
                { id: 'released', label: 'Released' }
              ].map(f => (
                <button
                  key={f.id}
                  onClick={() => setSubmissionFilter(f.id)}
                  className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition cursor-pointer ${
                    submissionFilter === f.id
                      ? 'bg-[#13519C] text-white shadow-2xs font-bold'
                      : 'bg-slate-50 text-slate-600 hover:bg-slate-100 border border-slate-200'
                  }`}
                >
                  {f.label}
                </button>
              ))}
            </div>
          </div>

          {/* Submissions List */}
          <div className="grid grid-cols-1 gap-4">
            {filteredSubmissions.map((sub) => (
              <div
                key={sub.id}
                className="bg-white border border-slate-200/90 rounded-2xl p-5 shadow-xs hover:shadow-md transition-all duration-200 flex flex-col lg:flex-row lg:items-center justify-between gap-4"
              >
                <div className="flex items-start gap-4">
                  <img
                    src={sub.studentPhoto}
                    alt={sub.studentName}
                    className="w-11 h-11 rounded-full object-cover border border-slate-200 shadow-2xs shrink-0"
                  />
                  <div>
                    <div className="flex items-center gap-2">
                      <span className="font-bold text-slate-900 text-sm">{sub.studentName}</span>
                      <span className="text-slate-300">•</span>
                      <span className="text-xs text-slate-500 font-medium">{sub.className}</span>
                    </div>

                    <div className="text-xs font-semibold text-[#13519C] mt-0.5">
                      {sub.assessmentTitle}
                    </div>

                    <div className="flex flex-wrap items-center gap-2 text-[11px] text-slate-400 mt-1 font-mono">
                      <span>Submitted: {sub.submittedAt}</span>
                      <span>•</span>
                      <span>Policy: {sub.releasePolicy === 'instant' ? '⚡ Instant' : '📋 Review First'}</span>
                    </div>
                  </div>
                </div>

                {/* Score & Release Action */}
                <div className="flex items-center gap-4 border-t lg:border-t-0 pt-3 lg:pt-0 justify-between lg:justify-end">
                  <div className="text-right">
                    <div className="text-lg font-mono font-black text-slate-900">
                      {sub.teacherAdjustedScore} / {sub.totalMarks}
                    </div>
                    <div className="text-[11px] text-slate-500 font-mono">
                      {Math.round((sub.teacherAdjustedScore / sub.totalMarks) * 100)}% Overall
                    </div>
                  </div>

                  <div>
                    {sub.status === 'released' ? (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200 font-mono">
                        <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                        Released
                      </span>
                    ) : (
                      <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-semibold bg-amber-50 text-amber-900 border border-amber-200 font-mono">
                        <Clock className="w-3.5 h-3.5 text-[#FF9100]" />
                        Pending Review
                      </span>
                    )}
                  </div>

                  <div className="flex items-center gap-2">
                    <button
                      onClick={() => setInspectingSub(sub)}
                      className="px-3 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-semibold text-slate-700 transition flex items-center gap-1 cursor-pointer"
                    >
                      <Eye className="w-3.5 h-3.5 text-[#13519C]" />
                      <span>Inspect</span>
                    </button>

                    {sub.status === 'pending_review' && (
                      <button
                        onClick={() => handleReleaseMarks(sub.id)}
                        className="px-3.5 py-1.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold shadow-xs transition flex items-center gap-1.5 cursor-pointer"
                      >
                        <Check className="w-3.5 h-3.5" />
                        <span>Release Marks</span>
                      </button>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Modal / Inspector Drawer for Selected Submission */}
          {inspectingSub && (
            <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-xs animate-in fade-in duration-200">
              <div className="bg-white rounded-2xl border border-slate-200/90 shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-y-auto animate-in zoom-in-95 duration-200">
                <div className="px-6 py-4 border-b border-slate-100 flex items-center justify-between bg-slate-50/60 sticky top-0 z-10">
                  <div className="flex items-center gap-3">
                    <img
                      src={inspectingSub.studentPhoto}
                      alt={inspectingSub.studentName}
                      className="w-9 h-9 rounded-full object-cover border border-slate-200"
                    />
                    <div>
                      <h4 
                        style={{ fontFamily: "'Afacad', sans-serif" }}
                        className="text-lg font-bold text-slate-900"
                      >
                        {inspectingSub.studentName} — Submission Detail
                      </h4>
                      <p className="text-[11px] text-slate-500 font-mono">
                        {inspectingSub.assessmentTitle} • {inspectingSub.className}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => setInspectingSub(null)}
                    className="text-slate-400 hover:text-slate-700 p-1 rounded-lg"
                  >
                    ✕
                  </button>
                </div>

                <div className="p-6 space-y-5 text-xs">
                  {/* Score Summary */}
                  <div className="bg-slate-50 border border-slate-200 rounded-xl p-4 flex items-center justify-between">
                    <div>
                      <div className="text-[10px] uppercase font-bold text-slate-500 tracking-wider">Engine Grade</div>
                      <div className="text-2xl font-mono font-black text-slate-900">
                        {inspectingSub.teacherAdjustedScore} / {inspectingSub.totalMarks} Marks
                      </div>
                    </div>
                    <div>
                      <span className={`px-3 py-1 rounded-full text-xs font-bold ${
                        inspectingSub.status === 'released'
                          ? 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                          : 'bg-amber-50 text-amber-900 border border-amber-200'
                      }`}>
                        {inspectingSub.status === 'released' ? 'Marks Released to Learner' : 'Held (Pending Approval)'}
                      </span>
                    </div>
                  </div>

                  {/* Answers Inspector */}
                  <div className="space-y-3">
                    <div className="font-bold text-slate-800 uppercase tracking-wider text-[11px]">
                      Student Responses &amp; Auto-Marking Breakdown:
                    </div>

                    {inspectingSub.answers.map((ans, aIdx) => (
                      <div key={aIdx} className="p-3.5 border border-slate-200 rounded-xl bg-white space-y-2">
                        <div className="flex items-center justify-between">
                          <span className="font-bold text-slate-900">Question {ans.qNum}</span>
                          <span className={`px-2 py-0.5 rounded text-[10px] font-bold font-mono ${
                            ans.autoCorrect ? 'bg-emerald-50 text-emerald-800' : 'bg-rose-50 text-rose-700'
                          }`}>
                            {ans.marksAwarded} / {ans.maxMarks} Marks
                          </span>
                        </div>

                        <div className="p-2.5 rounded-lg bg-slate-50 border border-slate-100 font-mono text-[11px] text-slate-800">
                          <span className="text-slate-400 font-sans block text-[10px] uppercase font-bold">Learner Response:</span>
                          {ans.studentAnswer}
                        </div>

                        <div className="text-[11px] text-slate-500 flex items-center gap-1">
                          <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                          <span>Expected: {ans.expectedAnswer}</span>
                        </div>

                        {ans.misconception && (
                          <div className="p-2 rounded bg-rose-50 border border-rose-200 text-rose-700 text-[10px] flex items-center gap-1 font-mono">
                            <AlertTriangle className="w-3.5 h-3.5 shrink-0" />
                            <span>Diagnostic Barrier Flagged: {ans.misconception}</span>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>

                  {/* Teacher Note & Override Input */}
                  <div className="space-y-2 pt-2 border-t border-slate-100">
                    <label className="block font-bold text-slate-800 text-xs">
                      Teacher Adjust Score &amp; Feedback:
                    </label>
                    <div className="flex items-center gap-3">
                      <div className="w-32">
                        <label className="block text-[10px] text-slate-500 mb-0.5">Final Mark</label>
                        <input
                          type="number"
                          value={inspectingSub.teacherAdjustedScore}
                          onChange={e => {
                            const val = Number(e.target.value);
                            setInspectingSub(prev => ({ ...prev, teacherAdjustedScore: val }));
                            setSubmissions(list => list.map(item => item.id === inspectingSub.id ? { ...item, teacherAdjustedScore: val } : item));
                          }}
                          className="w-full px-3 py-1.5 rounded-lg border border-slate-200 font-mono font-bold text-sm"
                        />
                      </div>
                      <div className="flex-1">
                        <label className="block text-[10px] text-slate-500 mb-0.5">Feedback Note</label>
                        <input
                          type="text"
                          value={inspectingSub.teacherNote || ''}
                          onChange={e => {
                            const val = e.target.value;
                            setInspectingSub(prev => ({ ...prev, teacherNote: val }));
                            setSubmissions(list => list.map(item => item.id === inspectingSub.id ? { ...item, teacherNote: val } : item));
                          }}
                          placeholder="Feedback message to learner..."
                          className="w-full px-3 py-1.5 rounded-lg border border-slate-200 text-xs"
                        />
                      </div>
                    </div>
                  </div>

                  {/* Modal Action Buttons */}
                  <div className="pt-4 flex items-center justify-end gap-2 border-t border-slate-100">
                    <button
                      type="button"
                      onClick={() => setInspectingSub(null)}
                      className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-600 hover:bg-slate-50"
                    >
                      Close
                    </button>
                    {inspectingSub.status === 'pending_review' && (
                      <button
                        type="button"
                        onClick={() => handleReleaseMarks(inspectingSub.id)}
                        className="px-5 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold shadow-xs flex items-center gap-1.5 cursor-pointer"
                      >
                        <Check className="w-3.5 h-3.5" />
                        <span>Approve &amp; Release Marks</span>
                      </button>
                    )}
                  </div>
                </div>
              </div>
            </div>
          )}

        </div>
      )}

      {/* Printable Test & Memo Modal Integration */}
      <PrintableTestModal
        isOpen={isPrintModalOpen}
        onClose={() => setIsPrintModalOpen(false)}
        testTitle={assessmentScope.title}
        subject={assessmentScope.subject}
        grade={assessmentScope.grade}
        term={assessmentScope.term}
        durationMins={assessmentScope.durationMins}
        questions={questions}
      />

    </div>
  );
}
