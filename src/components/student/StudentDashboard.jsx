import React, { useMemo } from 'react';
import { 
  Flame, Trophy, Award, BookOpen, ChevronRight, PlayCircle, 
  Sparkles, CheckCircle2, Shield, Calendar, BarChart2, Zap,
  Users, Clock, FileText, ArrowRight
} from 'lucide-react';
import { isOwnerEmail } from '../../app/constants/access';

const GRADE_SUBJECT_TEMPLATES = {
  7: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Working with whole numbers', progress: 78, color: '#3b82f6' },
    { id: 'ems', name: 'Economic and Management Sciences', icon: '🏦', topic: 'Accounting concepts & Budgets', progress: 84, color: '#f59e0b' },
    { id: 'natural_sciences', name: 'Natural Sciences', icon: '🌿', topic: 'Properties of materials & Periodic Table', progress: 70, color: '#10b981' },
  ],
  8: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Whole numbers, Integers & Exponents', progress: 72, color: '#3b82f6' },
    { id: 'ems', name: 'Economic and Management Sciences', icon: '🏦', topic: 'Cash Receipts & Payments Journals', progress: 80, color: '#f59e0b' },
    { id: 'natural_sciences', name: 'Natural Sciences', icon: '🌿', topic: 'Atoms & Particle model of matter', progress: 75, color: '#10b981' },
  ],
  9: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Algebraic expressions & Pythagoras', progress: 68, color: '#3b82f6' },
    { id: 'ems', name: 'Economic and Management Sciences', icon: '🏦', topic: 'Economic systems & Price Theory', progress: 82, color: '#f59e0b' },
    { id: 'natural_sciences', name: 'Natural Sciences', icon: '🌿', topic: 'Chemical reactions & Cells', progress: 74, color: '#10b981' },
  ],
  10: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Algebraic expressions & Trigonometry', progress: 74, color: '#3b82f6' },
    { id: 'accounting', name: 'Accounting', icon: '📊', topic: 'Sole Trader CRJ/CPJ & 15% VAT', progress: 85, color: '#059669' },
    { id: 'business_studies', name: 'Business Studies', icon: '💼', topic: 'Micro, Market & Macro Environments', progress: 88, color: '#8b5cf6' },
    { id: 'physical_sciences', name: 'Physical Sciences', icon: '⚗️', topic: 'Motion in 1D & Chemical Bonding', progress: 76, color: '#06b6d4' },
    { id: 'life_sciences', name: 'Life Sciences', icon: '🧬', topic: 'Cells, Mitosis & Plant Tissues', progress: 80, color: '#10b981' },
    { id: 'mathematical_literacy', name: 'Mathematical Literacy', icon: '📑', topic: 'Tariffs, PAYE & Measurement', progress: 82, color: '#14b8a6' },
    { id: 'technical_mathematics', name: 'Technical Mathematics', icon: '⚙️', topic: 'Algebraic expressions & Functions', progress: 70, color: '#6366f1' },
  ],
  11: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Exponents, Surds & Functions', progress: 70, color: '#3b82f6' },
    { id: 'accounting', name: 'Accounting', icon: '📊', topic: 'Bank Reconciliation & Partnerships', progress: 78, color: '#059669' },
    { id: 'business_studies', name: 'Business Studies', icon: '💼', topic: 'Influences & Socio-economic issues', progress: 84, color: '#8b5cf6' },
    { id: 'physical_sciences', name: 'Physical Sciences', icon: '⚗️', topic: 'Vectors in 2D & Atomic combinations', progress: 72, color: '#06b6d4' },
    { id: 'life_sciences', name: 'Life Sciences', icon: '🧬', topic: 'Photosynthesis & Respiration', progress: 77, color: '#10b981' },
  ],
  12: [
    { id: 'mathematics', name: 'Mathematics', icon: '📐', topic: 'Sequences & Series, Calculus, Trig', progress: 82, color: '#3b82f6' },
    { id: 'accounting', name: 'Accounting', icon: '📊', topic: 'Company Financial Statements & Audits', progress: 86, color: '#059669' },
    { id: 'business_studies', name: 'Business Studies', icon: '💼', topic: 'Macro Environment Strategies & HR', progress: 90, color: '#8b5cf6' },
    { id: 'physical_sciences', name: 'Physical Sciences', icon: '⚗️', topic: 'Momentum, Impulse & Organic Molecules', progress: 79, color: '#06b6d4' },
    { id: 'life_sciences', name: 'Life Sciences', icon: '🧬', topic: 'DNA, Genetics & Evolution', progress: 84, color: '#10b981' },
  ],
};

export default function StudentDashboard({
  currentUser = null,
  onNavigateToSubject = () => {},
  onOpenSimuLearn = () => {},
  onOpenReport = () => {},
  onOpenGamification = () => {},
  onOpenOlympiad = () => {},
  onOpenSubscription = () => {},
  onOpenParentLink = () => {},
  onSelectGrade = null,
  subscriptionTier = 'free_trial',
  daysRemaining = 14,
  userStats = {
    xp: 450,
    level: 3,
    streakDays: 5,
    sessionsCompleted: 14,
    recentScores: [70, 75, 82, 80, 88],
  }
}) {
  const isSuperAdmin = Boolean(
    currentUser?.isSuperAdmin ||
    currentUser?.isOwner ||
    (currentUser?.email && isOwnerEmail(currentUser.email)) ||
    (currentUser?.email && currentUser.email.toLowerCase().includes('admin'))
  );

  const studentName = currentUser?.name || currentUser?.displayName || currentUser?.email?.split('@')[0] || 'Learner';
  const numericGrade = parseInt(String(currentUser?.grade || '7').replace(/\D/g, ''), 10) || 7;
  const curriculum = currentUser?.curriculum || 'CAPS';

  const studentInitials = useMemo(() => {
    const parts = studentName.trim().split(/\s+/);
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return (parts[0][0] + parts[parts.length - 1][0]).toUpperCase();
  }, [studentName]);

  const weekDays = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
  const activeDaysIndices = [0, 1, 2, 3, 4]; // Active days

  const subjects = GRADE_SUBJECT_TEMPLATES[numericGrade] || GRADE_SUBJECT_TEMPLATES[7];

  return (
    <div className="w-full max-w-6xl mx-auto p-4 sm:p-6 space-y-6 text-slate-800 animate-fadeIn bg-slate-50 min-h-screen">
      
      {/* Super Admin Quick Testing Cockpit */}
      {isSuperAdmin && (
        <div className="bg-amber-50 border border-amber-200 rounded-2xl p-4 shadow-xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-2.5">
            <span className="px-2.5 py-1 rounded-md bg-amber-200 text-amber-900 text-xs font-bold uppercase tracking-wider">
              ⚡ Super Admin
            </span>
            <span className="text-xs text-amber-900 font-medium">
              Platform Owner access active • Quick Grade Switcher:
            </span>
          </div>
          {onSelectGrade && (
            <div className="flex items-center gap-1.5 flex-wrap">
              {[7, 8, 9, 10, 11, 12].map((g) => (
                <button
                  key={g}
                  onClick={() => onSelectGrade(g)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all cursor-pointer ${
                    numericGrade === g
                      ? 'bg-amber-600 text-white shadow-xs'
                      : 'bg-white hover:bg-amber-100 text-amber-900 border border-amber-300'
                  }`}
                >
                  Gr {g}
                </button>
              ))}
            </div>
          )}
        </div>
      )}

      {/* 1. Profile Header Card */}
      <div className="bg-white border border-slate-200 rounded-2xl p-5 sm:p-6 shadow-xs relative overflow-hidden">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-5 relative z-10">
          <div className="flex items-center gap-4">
            {/* Monogram Avatar */}
            <div className="w-16 h-16 sm:w-18 sm:h-18 rounded-2xl bg-indigo-50 border-2 border-indigo-200 flex items-center justify-center shadow-xs relative shrink-0">
              <span className="text-2xl sm:text-3xl font-black tracking-tight text-indigo-700">{studentInitials}</span>
              <span className="absolute -bottom-1 -right-1 bg-emerald-500 text-white text-[9px] font-bold px-1.5 py-0.5 rounded-full uppercase tracking-wider shadow-xs">
                Active
              </span>
            </div>

            <div>
              <div className="flex items-center gap-2 flex-wrap">
                <h1 className="text-xl sm:text-2xl font-bold text-slate-900 tracking-tight">{studentName}</h1>
                <span className="bg-slate-100 border border-slate-200 text-slate-700 text-xs px-2.5 py-0.5 rounded-md font-semibold">
                  Grade {numericGrade} • {curriculum}
                </span>
                {isSuperAdmin && (
                  <span className="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded border border-amber-300">
                    Admin Privileges
                  </span>
                )}
              </div>
              <p className="text-xs sm:text-sm text-slate-500 mt-1 flex items-center gap-2">
                <span className="text-indigo-600 font-semibold">National Curriculum Standard</span> • 
                <span className="text-slate-600">Deterministic Diagnostic Engine</span>
              </p>
            </div>
          </div>

          {/* Quick Metrics Bar */}
          <div className="flex items-center gap-2.5 w-full md:w-auto justify-between md:justify-end flex-wrap">
            {/* Daily Streak */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2 flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-lg bg-amber-100 text-amber-600 flex items-center justify-center">
                <Flame className="w-5 h-5 fill-amber-500" />
              </div>
              <div>
                <div className="text-[10px] text-slate-500 uppercase tracking-wider font-bold">Streak</div>
                <div className="text-xs sm:text-sm font-bold text-slate-900">{userStats.streakDays} Days</div>
              </div>
            </div>

            {/* Mastery XP */}
            <div className="bg-slate-50 border border-slate-200 rounded-xl px-3.5 py-2 flex items-center gap-2.5 cursor-pointer hover:border-indigo-300 transition-colors" onClick={onOpenGamification}>
              <div className="w-8 h-8 rounded-lg bg-indigo-100 text-indigo-600 flex items-center justify-center">
                <Zap className="w-5 h-5 fill-indigo-500" />
              </div>
              <div>
                <div className="text-[10px] text-slate-500 uppercase tracking-wider font-bold">Mastery XP</div>
                <div className="text-xs sm:text-sm font-bold text-slate-900">{userStats.xp} XP</div>
              </div>
            </div>

            {/* Parent Link Pill */}
            <button 
              onClick={onOpenParentLink}
              className="bg-slate-50 hover:bg-slate-100 border border-slate-200 text-slate-700 text-xs font-semibold px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer shadow-xs"
            >
              <Users className="w-3.5 h-3.5 text-indigo-600" />
              <span>Parent Link</span>
            </button>

            {/* Subscription Pill */}
            <button 
              onClick={onOpenSubscription}
              className="bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 text-xs font-semibold px-3 py-2 rounded-xl transition-all flex items-center gap-1.5 cursor-pointer shadow-xs"
            >
              <Shield className="w-3.5 h-3.5 text-emerald-600" />
              <span>{isSuperAdmin ? 'Full Access' : (subscriptionTier === 'free_trial' ? `${daysRemaining}d Trial` : 'Active Pro')}</span>
            </button>
          </div>
        </div>
      </div>

      {/* 2. Main Grid: Left (Trajectory & Subjects) + Right (Consistency, SimuLearn, Olympiad) */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Left 2 Columns */}
        <div className="lg:col-span-2 space-y-6">
          
          {/* Recent Trajectory Card */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <BarChart2 className="w-5 h-5 text-indigo-600" />
                <h2 className="text-sm sm:text-base font-bold text-slate-900">Mastery Trajectory &amp; Exam Readiness</h2>
              </div>
              <button onClick={onOpenReport} className="text-xs font-semibold text-indigo-600 hover:text-indigo-800 flex items-center gap-1 transition-colors cursor-pointer">
                <span>Diagnostic Academic Report</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>

            {/* Score trend visualization */}
            <div className="h-32 flex items-end justify-between gap-3 pt-4 px-2 border-b border-slate-100">
              {userStats.recentScores.map((score, idx) => (
                <div key={idx} className="flex-1 flex flex-col items-center gap-2 group relative">
                  <span className="text-xs font-bold text-slate-700 group-hover:text-indigo-600 transition-colors">
                    {score}%
                  </span>
                  <div className="w-full max-w-[48px] bg-slate-100 rounded-t-lg overflow-hidden h-20 flex items-end">
                    <div 
                      className={`w-full transition-all duration-700 rounded-t-lg ${
                        score >= 80 ? 'bg-emerald-500' :
                        score >= 60 ? 'bg-indigo-500' :
                        'bg-amber-500'
                      }`}
                      style={{ height: `${score}%` }}
                    />
                  </div>
                  <span className="text-[10px] text-slate-400 font-mono">Test {idx + 1}</span>
                </div>
              ))}
            </div>

            <div className="mt-3 flex items-center justify-between text-xs text-slate-500 pt-1">
              <div className="flex items-center gap-2">
                <span className="inline-block w-2.5 h-2.5 rounded-full bg-emerald-500" />
                <span>National Standards Calibration: <strong>Calibrated</strong></span>
              </div>
              <span className="text-emerald-700 font-semibold">+14% Growth this Term</span>
            </div>
          </div>

          {/* Active Grade-Filtered Subjects */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs">
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-sm sm:text-base font-bold text-slate-900 flex items-center gap-2">
                <BookOpen className="w-5 h-5 text-indigo-600" />
                <span>Grade {numericGrade} Subjects • National Curriculum</span>
              </h2>
              <span className="text-xs font-semibold text-slate-500 bg-slate-100 px-2.5 py-1 rounded-full">
                {subjects.length} Core Subjects
              </span>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3.5">
              {subjects.map((subj) => (
                <div 
                  key={subj.id}
                  onClick={() => onNavigateToSubject(subj.id)}
                  className="bg-slate-50 hover:bg-slate-100/80 border border-slate-200 hover:border-slate-300 rounded-xl p-4 cursor-pointer transition-all group flex flex-col justify-between shadow-2xs"
                >
                  <div className="flex items-start justify-between gap-2 mb-2">
                    <div className="flex items-center gap-3">
                      <span className="text-2xl">{subj.icon}</span>
                      <div>
                        <div className="text-sm font-bold text-slate-900 group-hover:text-indigo-600 transition-colors">
                          {subj.name}
                        </div>
                        <div className="text-xs text-slate-500 line-clamp-1 mt-0.5">
                          {subj.topic}
                        </div>
                      </div>
                    </div>
                    <span className="text-xs font-bold text-slate-700 bg-white px-2 py-0.5 rounded border border-slate-200">
                      {subj.progress}%
                    </span>
                  </div>

                  <div className="w-full bg-slate-200 h-1.5 rounded-full overflow-hidden mt-2">
                    <div 
                      className="h-full rounded-full transition-all duration-500"
                      style={{ width: `${subj.progress}%`, backgroundColor: subj.color }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>

        </div>

        {/* Right Column: Consistency, SimuLearn, Olympiad */}
        <div className="space-y-6">

          {/* Study Consistency Streak */}
          <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Calendar className="w-4 h-4 text-amber-500" />
                <h3 className="text-sm font-bold text-slate-900">Study Consistency</h3>
              </div>
              <span className="text-xs text-amber-700 bg-amber-50 border border-amber-200 px-2 py-0.5 rounded-md font-bold">
                {userStats.streakDays} Day Streak
              </span>
            </div>

            <div className="grid grid-cols-7 gap-1.5 text-center my-3">
              {weekDays.map((day, i) => {
                const isActive = activeDaysIndices.includes(i);
                return (
                  <div key={i} className="flex flex-col items-center gap-1">
                    <span className="text-[10px] text-slate-400 font-semibold">{day}</span>
                    <div className={`w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold transition-all ${
                      isActive 
                        ? 'bg-amber-100 border border-amber-300 text-amber-800 shadow-2xs' 
                        : 'bg-slate-100 text-slate-300'
                    }`}>
                      {isActive ? '✓' : ''}
                    </div>
                  </div>
                );
              })}
            </div>
            <p className="text-[11px] text-slate-500 text-center mt-2">
              Practice 1 problem every day to unlock the <strong>Term Trophy Medal</strong>.
            </p>
          </div>

          {/* SimuLearn Step Player Launch Card */}
          <div className="bg-indigo-50/70 border border-indigo-200 rounded-2xl p-5 shadow-xs relative overflow-hidden">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <PlayCircle className="w-5 h-5 text-indigo-600" />
                <h3 className="text-sm font-bold text-slate-900">SimuLearn Step Replay</h3>
              </div>
              <span className="bg-indigo-100 text-indigo-700 text-[10px] font-bold px-2 py-0.5 rounded-full border border-indigo-200">
                0.1% Mobile Data
              </span>
            </div>
            <p className="text-xs text-slate-600 mt-1 mb-3.5 leading-relaxed">
              Watch pre-animated canonical worked solutions step-by-step without consuming high video bandwidth.
            </p>
            <button 
              onClick={onOpenSimuLearn}
              className="w-full py-2 px-3 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold rounded-xl transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
            >
              <PlayCircle className="w-4 h-4" />
              <span>Watch Step Simulation</span>
            </button>
          </div>

          {/* SAMO Olympiad Track Gate */}
          <div className="bg-amber-50/60 border border-amber-200 rounded-2xl p-5 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <Trophy className="w-5 h-5 text-amber-600" />
                <h3 className="text-sm font-bold text-slate-900">SAMO Olympiad Track</h3>
              </div>
              <span className="bg-amber-100 text-amber-800 text-[10px] font-bold px-2 py-0.5 rounded-full border border-amber-200">
                Enrichment
              </span>
            </div>
            <p className="text-xs text-slate-600 mt-1 mb-3.5 leading-relaxed">
              Stretch problems for curious learners. Gated behind Mathematics Topic Medals.
            </p>
            <button 
              onClick={onOpenOlympiad}
              className="w-full py-2 px-3 bg-amber-600 hover:bg-amber-700 text-white font-bold text-xs rounded-xl transition-all flex items-center justify-center gap-1.5 shadow-sm cursor-pointer"
            >
              <Award className="w-4 h-4" />
              <span>Enter Olympiad Arena</span>
            </button>
          </div>

        </div>

      </div>
    </div>
  );
}
