import React, { useState, useEffect } from 'react';
import { 
  Users, BookOpen, BarChart3, Plus, Copy, Check, Printer, 
  Send, Sparkles, AlertTriangle, ArrowRight, ShieldCheck, 
  ExternalLink, FileText, CheckCircle2, Clock, ChevronRight, Share2,
  RotateCcw, ShieldAlert
} from 'lucide-react';
import ClassManagerModal from './ClassManagerModal';
import PrintableTestModal from './PrintableTestModal';

/**
 * TeacherDashboard Component (Layer D — Phase D8)
 * Modern teacher LMS cockpit for tracking class rosters, copying 6-char join codes,
 * launching diagnostic heatmaps, dispatching remedial micro-drills, and creating printable tests.
 */
export default function TeacherDashboard({
  currentUser = { name: 'Mr. N. Sithole', email: 'sithole@school.co.za' },
  onNavigate = () => {},
  db = null
}) {
  const [classes, setClasses] = useState([
    {
      classId: 'cls_gr10_acc',
      name: 'Grade 10 Accounting (Period 2)',
      subject: 'Accounting',
      grade: '10',
      joinCode: 'ACC9B2',
      studentCount: 28,
      avgMastery: 78,
      topMisconception: 'net_vs_gross_confusion',
      recentSubmissionCount: 24,
      students: [
        { id: 's1', name: 'Thabo Ndlovu', score: 85, status: 'Mastered' },
        { id: 's2', name: 'Lerato Dlamini', score: 62, status: 'Remedial' },
        { id: 's3', name: 'Sipho Zulu', score: 91, status: 'Mastered' },
        { id: 's4', name: 'Zanele Khumalo', score: 74, status: 'On Track' },
      ]
    },
    {
      classId: 'cls_gr10_math',
      name: 'Grade 10 Mathematics — Alpha',
      subject: 'Mathematics',
      grade: '10',
      joinCode: 'MATH8X',
      studentCount: 32,
      avgMastery: 71,
      topMisconception: 'sign_error_distribution',
      recentSubmissionCount: 29,
      students: [
        { id: 's5', name: 'Kagiso Molefe', score: 68, status: 'On Track' },
        { id: 's6', name: 'Naledi Sithole', score: 55, status: 'Remedial' },
        { id: 's7', name: 'Bongani Nkosi', score: 88, status: 'Mastered' },
      ]
    },
    {
      classId: 'cls_gr9_ems',
      name: 'Grade 9 EMS (Commerce)',
      subject: 'EMS',
      grade: '9',
      joinCode: 'EMS7Q4',
      studentCount: 35,
      avgMastery: 84,
      topMisconception: 'debit_credit_inversion',
      recentSubmissionCount: 33,
      students: [
        { id: 's8', name: 'Andile Mthembu', score: 92, status: 'Mastered' },
        { id: 's9', name: 'Precious Moyo', score: 79, status: 'On Track' },
      ]
    }
  ]);

  const [copiedCode, setCopiedCode] = useState(null);
  const [showClassModal, setShowClassModal] = useState(false);
  const [showPrintableModal, setShowPrintableModal] = useState(false);
  const [selectedClassForPrint, setSelectedClassForPrint] = useState(null);
  const [dispatchedAlert, setDispatchedAlert] = useState(null);
  const [moderatedAvatarToast, setModeratedAvatarToast] = useState(null);

  const handleResetAvatar = (studentName) => {
    setModeratedAvatarToast(`Avatar for ${studentName} reset to initials (POPIA minor safety policy enforced).`);
    setTimeout(() => setModeratedAvatarToast(null), 4000);
  };

  const teacherInitials = (currentUser?.name || 'T L')
    .split(' ')
    .filter(Boolean)
    .map(n => n[0])
    .join('')
    .slice(0, 2)
    .toUpperCase();

  const handleCopyCode = (code) => {
    navigator.clipboard.writeText(code);
    setCopiedCode(code);
    setTimeout(() => setCopiedCode(null), 2500);
  };

  const handleShareWhatsApp = (cls) => {
    const text = encodeURIComponent(
      `📚 *Fundile Class Invite*\n` +
      `Join *${cls.name}* on Fundile:\n` +
      `1. Open Fundile and go to your Student Dashboard\n` +
      `2. Click "Join Class" and enter Code: *${cls.joinCode}*\n` +
      `Instant access to exam-standard practice and homework!`
    );
    window.open(`https://wa.me/?text=${text}`, '_blank');
  };

  const handleDispatchDrill = (misconceptionTag, className) => {
    setDispatchedAlert(`5-Minute Remedial Drill for '${misconceptionTag}' sent to ${className}`);
    setTimeout(() => setDispatchedAlert(null), 4000);
  };

  const totalStudents = classes.reduce((sum, c) => sum + c.studentCount, 0);
  const overallMastery = Math.round(classes.reduce((sum, c) => sum + c.avgMastery, 0) / (classes.length || 1));

  return (
    <div className="w-full min-h-screen bg-slate-950 text-slate-100 p-4 sm:p-6 lg:p-8 space-y-6">
      
      {/* 1. TOP HEADER & TEACHER MONOGRAM */}
      <div className="bg-slate-900/90 border border-slate-800/80 rounded-2xl p-6 backdrop-blur shadow-xl relative overflow-hidden">
        <div className="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-indigo-500/10 via-sky-500/5 to-transparent rounded-full blur-3xl pointer-events-none" />
        
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6 relative z-10">
          <div className="flex items-center gap-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-indigo-500/20 to-sky-500/20 border-2 border-indigo-400/40 flex items-center justify-center shadow-inner relative">
              <span className="text-2xl font-black tracking-tight text-white">{teacherInitials}</span>
              <span className="absolute -bottom-1 -right-1 bg-emerald-500 text-slate-950 text-[9px] font-bold px-1.5 py-0.5 rounded-full uppercase tracking-wider">
                Teacher
              </span>
            </div>

            <div>
              <div className="flex items-center gap-2">
                <h1 className="text-2xl font-bold text-white tracking-tight">{currentUser.name || 'Teacher Portal'}</h1>
                <span className="bg-slate-800 border border-slate-700 text-slate-300 text-xs px-2.5 py-0.5 rounded-md font-medium">
                  LMS Cockpit · National Curriculum Standard
                </span>
              </div>
              <p className="text-sm text-slate-400 mt-1 flex items-center gap-2">
                <span className="text-indigo-400 font-semibold">High School Commerce &amp; STEM</span> · 
                <span className="text-slate-400">{classes.length} Active Rosters</span>
              </p>
            </div>
          </div>

          {/* Quick Cockpit Actions */}
          <div className="flex flex-wrap items-center gap-3">
            <button
              onClick={() => setShowClassModal(true)}
              className="flex items-center gap-2 bg-indigo-600 hover:bg-indigo-500 text-white px-4 py-2.5 rounded-xl font-semibold text-xs transition-all shadow-md shadow-indigo-600/20"
            >
              <Plus className="w-4 h-4" />
              <span>Create Class</span>
            </button>

            <button
              onClick={() => {
                setSelectedClassForPrint(classes[0]);
                setShowPrintableModal(true);
              }}
              className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 px-4 py-2.5 rounded-xl font-semibold text-xs transition-all"
            >
              <Printer className="w-4 h-4 text-sky-400" />
              <span>Print Test &amp; Memo</span>
            </button>

            <button
              onClick={() => onNavigate('classDiagnostics')}
              className="flex items-center gap-2 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 px-4 py-2.5 rounded-xl font-semibold text-xs transition-all"
            >
              <BarChart3 className="w-4 h-4 text-amber-400" />
              <span>Diagnostic Heatmap</span>
            </button>
          </div>
        </div>
      </div>

      {/* Dispatched Notification Banner */}
      {dispatchedAlert && (
        <div className="bg-emerald-950/80 border border-emerald-500/40 text-emerald-200 p-3.5 rounded-xl text-xs font-semibold flex items-center justify-between shadow-lg animate-in fade-in duration-300">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>{dispatchedAlert}</span>
          </div>
          <button onClick={() => setDispatchedAlert(null)} className="text-emerald-400 hover:text-white">✕</button>
        </div>
      )}

      {/* 2. OVERVIEW KPI METRIC CARDS */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Learners</span>
            <Users className="w-4 h-4 text-sky-400" />
          </div>
          <div className="text-2xl font-bold text-white mt-2">{totalStudents}</div>
          <p className="text-xs text-slate-500 mt-1">Across {classes.length} registered classes</p>
        </div>

        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Average Mastery</span>
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
          </div>
          <div className="text-2xl font-bold text-emerald-400 mt-2">{overallMastery}%</div>
          <p className="text-xs text-slate-500 mt-1">National Benchmark: 65% Target</p>
        </div>

        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Homework Due</span>
            <Clock className="w-4 h-4 text-amber-400" />
          </div>
          <div className="text-2xl font-bold text-amber-400 mt-2">86 Submissions</div>
          <p className="text-xs text-slate-500 mt-1">Due Friday 23:59</p>
        </div>

        <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">Active Misconceptions</span>
            <AlertTriangle className="w-4 h-4 text-rose-400" />
          </div>
          <div className="text-2xl font-bold text-rose-400 mt-2">3 Flagged</div>
          <p className="text-xs text-slate-500 mt-1">Ready for 1-tap remedial drill</p>
        </div>
      </div>

      {/* 3. ACTIVE CLASSES ROSTER & CODES */}
      <div className="space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-indigo-400" />
            <h2 className="text-lg font-bold text-white tracking-tight">Active Class Rosters &amp; Join Codes</h2>
          </div>
          <span className="text-xs text-slate-400">Learners use 6-character code to join in 5 seconds</span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {classes.map((cls) => (
            <div 
              key={cls.classId}
              className="bg-slate-900/80 border border-slate-800 rounded-2xl p-5 flex flex-col justify-between hover:border-slate-700 transition-all shadow-lg"
            >
              <div>
                <div className="flex items-start justify-between gap-2 mb-3">
                  <div>
                    <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-400 bg-indigo-950/60 border border-indigo-800/60 px-2 py-0.5 rounded">
                      Grade {cls.grade} · {cls.subject}
                    </span>
                    <h3 className="text-base font-bold text-white mt-1.5">{cls.name}</h3>
                  </div>
                  <div className="text-right">
                    <span className="text-xs font-semibold text-slate-400">{cls.studentCount} Students</span>
                  </div>
                </div>

                {/* 6-Character Join Code Pill */}
                <div className="bg-slate-950 border border-slate-800 rounded-xl p-3 flex items-center justify-between my-3">
                  <div>
                    <div className="text-[10px] uppercase tracking-wider text-slate-500 font-semibold">Join Code</div>
                    <div className="text-lg font-mono font-black text-indigo-300 tracking-wider">{cls.joinCode}</div>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <button
                      onClick={() => handleCopyCode(cls.joinCode)}
                      title="Copy join code"
                      className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors flex items-center gap-1 text-xs"
                    >
                      {copiedCode === cls.joinCode ? <Check className="w-4 h-4 text-emerald-400" /> : <Copy className="w-4 h-4" />}
                    </button>
                    <button
                      onClick={() => handleShareWhatsApp(cls)}
                      title="Share via WhatsApp"
                      className="p-2 rounded-lg bg-emerald-950 hover:bg-emerald-900 border border-emerald-800/60 text-emerald-400 hover:text-emerald-200 transition-colors"
                    >
                      <Share2 className="w-4 h-4" />
                    </button>
                  </div>
                </div>

                {/* Mastery Bar */}
                <div className="space-y-1 my-3">
                  <div className="flex justify-between text-xs text-slate-400">
                    <span>Curriculum Mastery Average</span>
                    <span className="font-bold text-slate-200">{cls.avgMastery}%</span>
                  </div>
                  <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
                    <div 
                      className={`h-full rounded-full transition-all duration-500 ${
                        cls.avgMastery >= 80 ? 'bg-emerald-500' :
                        cls.avgMastery >= 65 ? 'bg-sky-500' : 'bg-amber-500'
                      }`}
                      style={{ width: `${cls.avgMastery}%` }}
                    />
                  </div>
                </div>

                {/* Top Misconception Remedial Trigger */}
                <div className="bg-slate-950/60 border border-rose-900/30 rounded-xl p-2.5 flex items-center justify-between text-xs my-2">
                  <div className="flex items-center gap-2 text-rose-300 truncate mr-2">
                    <AlertTriangle className="w-3.5 h-3.5 text-rose-400 shrink-0" />
                    <span className="truncate font-mono text-[11px]">{cls.topMisconception}</span>
                  </div>
                  <button
                    onClick={() => handleDispatchDrill(cls.topMisconception, cls.name)}
                    className="shrink-0 text-[11px] font-semibold text-rose-400 hover:text-rose-300 underline"
                  >
                    Assign Fix
                  </button>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="pt-4 border-t border-slate-800/80 flex items-center justify-between gap-2 mt-2">
                <button
                  onClick={() => onNavigate('classDiagnostics')}
                  className="flex-1 text-center py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold transition-colors"
                >
                  Diagnostic View
                </button>
                <button
                  onClick={() => onNavigate('assessment_generator')}
                  className="flex-1 text-center py-2 rounded-xl bg-indigo-600/20 hover:bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 text-xs font-semibold transition-colors"
                >
                  Assign Homework
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* 4. RECENT SUBMISSIONS & MARK BOOK PREVIEW */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-6 shadow-xl">
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <FileText className="w-5 h-5 text-sky-400" />
            <h2 className="text-base font-bold text-white tracking-tight">Recent Student Practice Submissions</h2>
          </div>
          <button 
            onClick={() => onNavigate('submissions')}
            className="text-xs font-semibold text-sky-400 hover:text-sky-300 flex items-center gap-1 transition-colors"
          >
            Full Submissions Mark Book <ChevronRight className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* Moderation Toast Banner */}
        {moderatedAvatarToast && (
          <div className="mb-4 p-3 rounded-xl bg-amber-950/70 border border-amber-500/50 text-amber-200 text-xs flex items-center justify-between animate-fadeIn">
            <div className="flex items-center gap-2">
              <ShieldAlert className="w-4 h-4 text-amber-400" />
              <span>{moderatedAvatarToast}</span>
            </div>
            <button onClick={() => setModeratedAvatarToast(null)} className="text-amber-400 hover:text-white">✕</button>
          </div>
        )}

        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-950/60 text-slate-400 uppercase tracking-wider text-[10px] border-b border-slate-800">
              <tr>
                <th className="py-3 px-4">Learner Name</th>
                <th className="py-3 px-4">Class</th>
                <th className="py-3 px-4">Subject &amp; Topic</th>
                <th className="py-3 px-4">Score</th>
                <th className="py-3 px-4">Status</th>
                <th className="py-3 px-4">Olympiad Recognition</th>
                <th className="py-3 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/60">
              <tr className="hover:bg-slate-800/30 transition-colors">
                <td className="py-3 px-4 font-semibold text-white">
                  <div className="flex items-center gap-2.5">
                    <div className="w-6 h-6 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-sky-300">
                      TN
                    </div>
                    <span>Thabo Ndlovu</span>
                  </div>
                </td>
                <td className="py-3 px-4 text-slate-400">Grade 10 Accounting</td>
                <td className="py-3 px-4">Cash Receipts Journal (Trading)</td>
                <td className="py-3 px-4 font-bold text-emerald-400">85%</td>
                <td className="py-3 px-4">
                  <span className="bg-emerald-950 text-emerald-300 border border-emerald-800 px-2 py-0.5 rounded-full text-[10px] font-semibold">
                    Mastered
                  </span>
                </td>
                <td className="py-3 px-4">
                  <span className="bg-amber-950/70 text-amber-300 border border-amber-500/40 px-2 py-0.5 rounded-full text-[10px] font-semibold flex items-center gap-1 w-fit">
                    🥇 SAMO Gold (94%)
                  </span>
                </td>
                <td className="py-3 px-4 text-right">
                  <div className="flex items-center justify-end gap-2">
                    <button onClick={() => onNavigate('submissions')} className="text-indigo-400 hover:text-indigo-300 font-semibold">
                      Inspect
                    </button>
                    <button 
                      onClick={() => handleResetAvatar('Thabo Ndlovu')} 
                      title="POPIA Child Safety: Reset learner avatar to monogram initials" 
                      className="p-1 rounded text-slate-500 hover:text-amber-400 hover:bg-slate-800 transition-colors"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </td>
              </tr>
              <tr className="hover:bg-slate-800/30 transition-colors">
                <td className="py-3 px-4 font-semibold text-white">
                  <div className="flex items-center gap-2.5">
                    <div className="w-6 h-6 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-amber-300">
                      LD
                    </div>
                    <span>Lerato Dlamini</span>
                  </div>
                </td>
                <td className="py-3 px-4 text-slate-400">Grade 10 Accounting</td>
                <td className="py-3 px-4">Cash Receipts Journal (Trading)</td>
                <td className="py-3 px-4 font-bold text-amber-400">62%</td>
                <td className="py-3 px-4">
                  <span className="bg-amber-950 text-amber-300 border border-amber-800 px-2 py-0.5 rounded-full text-[10px] font-semibold">
                    Needs Remedial
                  </span>
                </td>
                <td className="py-3 px-4 text-slate-500 text-[11px]">—</td>
                <td className="py-3 px-4 text-right">
                  <div className="flex items-center justify-end gap-2">
                    <button onClick={() => onNavigate('submissions')} className="text-indigo-400 hover:text-indigo-300 font-semibold">
                      Inspect
                    </button>
                    <button 
                      onClick={() => handleResetAvatar('Lerato Dlamini')} 
                      title="POPIA Child Safety: Reset learner avatar to monogram initials" 
                      className="p-1 rounded text-slate-500 hover:text-amber-400 hover:bg-slate-800 transition-colors"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </td>
              </tr>
              <tr className="hover:bg-slate-800/30 transition-colors">
                <td className="py-3 px-4 font-semibold text-white">
                  <div className="flex items-center gap-2.5">
                    <div className="w-6 h-6 rounded-full bg-slate-800 border border-slate-700 flex items-center justify-center text-[10px] font-bold text-purple-300">
                      KM
                    </div>
                    <span>Kagiso Molefe</span>
                  </div>
                </td>
                <td className="py-3 px-4 text-slate-400">Grade 10 Mathematics</td>
                <td className="py-3 px-4">Algebraic Expressions &amp; Factoring</td>
                <td className="py-3 px-4 font-bold text-sky-400">68%</td>
                <td className="py-3 px-4">
                  <span className="bg-sky-950 text-sky-300 border border-sky-800 px-2 py-0.5 rounded-full text-[10px] font-semibold">
                    On Track
                  </span>
                </td>
                <td className="py-3 px-4">
                  <span className="bg-slate-800 text-sky-300 border border-sky-500/40 px-2 py-0.5 rounded-full text-[10px] font-semibold flex items-center gap-1 w-fit">
                    🥈 SAMO Silver (88%)
                  </span>
                </td>
                <td className="py-3 px-4 text-right">
                  <div className="flex items-center justify-end gap-2">
                    <button onClick={() => onNavigate('submissions')} className="text-indigo-400 hover:text-indigo-300 font-semibold">
                      Inspect
                    </button>
                    <button 
                      onClick={() => handleResetAvatar('Kagiso Molefe')} 
                      title="POPIA Child Safety: Reset learner avatar to monogram initials" 
                      className="p-1 rounded text-slate-500 hover:text-amber-400 hover:bg-slate-800 transition-colors"
                    >
                      <RotateCcw className="w-3.5 h-3.5" />
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Class Manager Modal Integration */}
      <ClassManagerModal
        isOpen={showClassModal}
        onClose={() => setShowClassModal(false)}
        teacherId={currentUser?.uid || 'tch_demo_101'}
        teacherName={currentUser?.name || 'Mr. Sithole'}
      />

      {/* Printable Test Modal Integration */}
      {selectedClassForPrint && (
        <PrintableTestModal
          isOpen={showPrintableModal}
          onClose={() => setShowPrintableModal(false)}
          subject={selectedClassForPrint.subject}
          grade={selectedClassForPrint.grade}
          topic="Cash Receipts Journal &amp; Ledger"
        />
      )}
    </div>
  );
}
