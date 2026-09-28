import React, { useState, useMemo } from 'react';
import {
  Users, BookOpen, Plus, Copy, Check, Share2, AlertTriangle,
  CheckCircle2, Search, Award, RotateCcw, ExternalLink, Sparkles
} from 'lucide-react';

/**
 * Avatar with fallback monogram and POPIA-compliant profile support
 */
export function AvatarWithFallback({ src, name, size = 'md' }) {
  const [hasError, setHasError] = useState(false);

  const sizeClass = {
    sm: 'w-7 h-7 text-[10px]',
    md: 'w-9 h-9 text-xs',
    lg: 'w-12 h-12 text-sm',
  }[size] || 'w-9 h-9 text-xs';

  const initials = (name || 'Learner')
    .split(' ')
    .filter(Boolean)
    .map(p => p[0])
    .join('')
    .slice(0, 2)
    .toUpperCase();

  if (src && !hasError) {
    return (
      <img
        src={src}
        alt={name}
        onError={() => setHasError(true)}
        className={`${sizeClass} rounded-full object-cover border border-slate-200 shadow-xs shrink-0`}
      />
    );
  }

  const colorVariants = [
    'bg-blue-50 text-[#13519C] border-blue-200',
    'bg-emerald-50 text-emerald-800 border-emerald-200',
    'bg-amber-50 text-amber-900 border-amber-200',
    'bg-purple-50 text-purple-800 border-purple-200',
    'bg-sky-50 text-sky-800 border-sky-200',
  ];
  const charCode = (name || 'L').charCodeAt(0) % colorVariants.length;
  const colorClass = colorVariants[charCode];

  return (
    <div
      className={`${sizeClass} rounded-full ${colorClass} border flex items-center justify-center font-mono font-bold shrink-0 shadow-xs`}
    >
      {initials}
    </div>
  );
}

/**
 * Status Badge Component with verified Option 1 light colors
 */
export function StatusBadge({ status }) {
  switch (status) {
    case 'Mastered':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-blue-50 text-[#13519C] border border-blue-200/90 font-mono">
          <span className="w-1.5 h-1.5 rounded-full bg-[#13519C]" />
          Mastered
        </span>
      );
    case 'On Track':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-50 text-emerald-800 border border-emerald-200/90 font-mono">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" />
          On Track
        </span>
      );
    case 'In Progress':
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-50 text-amber-900 border border-amber-200/90 font-mono">
          <span className="w-1.5 h-1.5 rounded-full bg-[#FF9100]" />
          In Progress
        </span>
      );
    case 'Remedial':
    default:
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-rose-50 text-rose-700 border border-rose-200/90 font-mono">
          <span className="w-1.5 h-1.5 rounded-full bg-rose-500" />
          Remedial
        </span>
      );
  }
}

export default function TeacherRostersTab({
  classes = [],
  onOpenCreateClass = () => {},
  onLoadSampleRoster = () => {},
  onDispatchDrill = () => {},
  onSelectClassForTest = () => {},
  onNavigate = () => {},
  onResetAvatar = () => {},
  teacherName = 'Teacher'
}) {
  const [copiedCode, setCopiedCode] = useState(null);
  const [copiedNudge, setCopiedNudge] = useState(null);
  const [activeClassFilter, setActiveClassFilter] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [statusFilter, setStatusFilter] = useState('all');

  // Aggregate All Students Dynamically Across Active Classes
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

  // Filtered Student List for the Mark Book
  const filteredStudents = useMemo(() => {
    return allStudents.filter(student => {
      const matchesClass = activeClassFilter === 'all' || student.classId === activeClassFilter;
      const matchesStatus = statusFilter === 'all' || student.status === statusFilter;
      const q = searchQuery.toLowerCase().trim();
      const matchesSearch = !q || 
        student.name.toLowerCase().includes(q) ||
        (student.topic && student.topic.toLowerCase().includes(q)) ||
        (student.email && student.email.toLowerCase().includes(q));
      return matchesClass && matchesStatus && matchesSearch;
    });
  }, [allStudents, activeClassFilter, statusFilter, searchQuery]);

  // 1-Click Join Code Copying with 2.5s Tooltip Feedback
  const handleCopyCode = (code) => {
    if (navigator?.clipboard?.writeText) {
      navigator.clipboard.writeText(code);
    }
    setCopiedCode(code);
    setTimeout(() => setCopiedCode(null), 2500);
  };

  // 1-Click WhatsApp Class Invite Generator
  const handleShareWhatsApp = (cls) => {
    const message = 
      `📚 *Fundile Class Invite*\n` +
      `Join *${cls.name}* on Fundile:\n` +
      `1. Open Fundile and go to your Student Dashboard\n` +
      `2. Click "Join Class" and enter Code: *${cls.joinCode}*\n` +
      `Instant access to authentic CAPS exam practice!`;
    const url = `https://wa.me/?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank');
  };

  // 1-Click Student Nudge (Encouragement message)
  const handleSendNudge = (student) => {
    const text = 
      `📚 *Fundile Practice Nudge*\n` +
      `Hi ${student.name}! ${teacherName} noticed you are making great progress in ${student.classSubject || 'class'} on "${student.topic || 'current topics'}".\n` +
      `Complete today's 5-minute Fundile micro-drill to strengthen your mastery!`;
    
    if (navigator?.clipboard?.writeText) {
      navigator.clipboard.writeText(text);
    }
    setCopiedNudge(student.id);
    setTimeout(() => setCopiedNudge(null), 2500);

    const url = `https://wa.me/?text=${encodeURIComponent(text)}`;
    window.open(url, '_blank');
  };

  return (
    <div className="space-y-8 animate-in fade-in duration-200">
      
      {/* 1. ACTIVE CLASS CARDS SECTION */}
      <section className="space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div className="flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-[#13519C]" />
            <h2 
              style={{ fontFamily: "'Afacad', sans-serif" }}
              className="text-xl font-bold text-slate-900 tracking-tight"
            >
              Class Rosters &amp; 6-Character Join Codes
            </h2>
          </div>
          <p className="text-xs text-slate-500">Learners use 6-character code to enroll into live analytics in 5 seconds</p>
        </div>

        {/* EMPTY STATE OR CLASS CARDS GRID */}
        {classes.length === 0 ? (
          <div className="bg-white border-2 border-dashed border-slate-200 rounded-2xl p-10 sm:p-14 text-center max-w-2xl mx-auto shadow-xs">
            <div className="w-16 h-16 rounded-2xl bg-blue-50 text-[#13519C] flex items-center justify-center mx-auto mb-4 border border-blue-100">
              <BookOpen className="w-8 h-8" />
            </div>
            <h3 
              style={{ fontFamily: "'Afacad', sans-serif" }}
              className="text-2xl font-bold text-slate-900"
            >
              No classes created yet
            </h3>
            <p className="text-sm text-slate-500 mt-2 max-w-md mx-auto">
              Click <strong className="text-[#13519C]">Create Class</strong> to start managing your learner roster, or load our pre-populated CAPS demo class to explore instant analytics, join codes, and remedial micro-drills.
            </p>
            <div className="flex flex-wrap items-center justify-center gap-3 mt-6">
              <button
                onClick={onOpenCreateClass}
                className="inline-flex items-center gap-2 bg-[#13519C] hover:bg-[#0f3e77] text-white px-5 py-2.5 rounded-xl font-semibold text-sm shadow-xs transition cursor-pointer"
              >
                <Plus className="w-4 h-4" />
                <span>Create Class</span>
              </button>
              <button
                onClick={onLoadSampleRoster}
                className="inline-flex items-center gap-2 bg-amber-50 hover:bg-amber-100 border border-amber-200 text-amber-900 px-5 py-2.5 rounded-xl font-semibold text-sm transition cursor-pointer"
              >
                <Sparkles className="w-4 h-4 text-[#FF9100]" />
                <span>Load Sample CAPS Class Roster</span>
              </button>
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {classes.map((cls) => (
              <div
                key={cls.classId}
                className="bg-white border border-slate-200/90 rounded-2xl p-5 flex flex-col justify-between shadow-xs hover:shadow-md transition-all duration-200 group"
              >
                <div>
                  {/* Card Header */}
                  <div className="flex items-start justify-between gap-2 mb-3">
                    <div>
                      <span className="text-[11px] font-bold uppercase tracking-wider text-[#13519C] bg-blue-50 border border-blue-200/70 px-2.5 py-0.5 rounded-md inline-block">
                        Grade {cls.grade} • {cls.subject}
                      </span>
                      <h3 
                        style={{ fontFamily: "'Afacad', sans-serif" }}
                        className="text-lg font-bold text-slate-900 mt-1.5 leading-snug group-hover:text-[#13519C] transition-colors"
                      >
                        {cls.name}
                      </h3>
                    </div>
                    <div className="text-right shrink-0">
                      <span className="text-xs font-semibold text-slate-500 bg-slate-100 px-2 py-0.5 rounded-md font-mono">
                        {cls.students?.length ?? cls.studentCount} Students
                      </span>
                    </div>
                  </div>

                  {/* 6-Character Join Code Pill */}
                  <div className="bg-slate-50 border border-slate-200/90 rounded-xl p-3 flex items-center justify-between my-3">
                    <div>
                      <div className="text-[10px] uppercase tracking-wider text-slate-500 font-semibold">Join Code</div>
                      <div className="text-xl font-mono font-black text-[#13519C] tracking-widest">{cls.joinCode}</div>
                    </div>
                    <div className="flex items-center gap-1.5 relative">
                      {/* Copy Button with Tooltip */}
                      <button
                        onClick={() => handleCopyCode(cls.joinCode)}
                        title="Copy 6-char join code"
                        className="p-2 rounded-lg bg-white hover:bg-slate-100 border border-slate-200 text-slate-700 hover:text-slate-900 transition-colors flex items-center gap-1 text-xs cursor-pointer shadow-2xs"
                      >
                        {copiedCode === cls.joinCode ? (
                          <>
                            <Check className="w-4 h-4 text-emerald-600" />
                            <span className="text-[11px] font-semibold text-emerald-700 font-mono">Copied!</span>
                          </>
                        ) : (
                          <Copy className="w-4 h-4 text-slate-600" />
                        )}
                      </button>

                      {/* WhatsApp Share Button */}
                      <button
                        onClick={() => handleShareWhatsApp(cls)}
                        title="Share invite via WhatsApp"
                        className="p-2 rounded-lg bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-700 hover:text-emerald-900 transition-colors cursor-pointer shadow-2xs"
                      >
                        <Share2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>

                  {/* Curriculum Mastery Progress Bar */}
                  <div className="space-y-1.5 my-3">
                    <div className="flex justify-between text-xs text-slate-500">
                      <span>Curriculum Mastery Average</span>
                      <span className="font-bold text-slate-800 font-mono">{cls.avgMastery}%</span>
                    </div>
                    <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
                      <div 
                        className={`h-full rounded-full transition-all duration-500 ${
                          cls.avgMastery >= 80 ? 'bg-emerald-500' :
                          cls.avgMastery >= 65 ? 'bg-[#13519C]' : 'bg-[#FF9100]'
                        }`}
                        style={{ width: `${cls.avgMastery}%` }}
                      />
                    </div>
                  </div>

                  {/* Top Misconception Remedial Trigger */}
                  {cls.topMisconception ? (
                    <div className="bg-rose-50 border border-rose-200/80 rounded-xl p-2.5 flex items-center justify-between text-xs my-2 gap-2">
                      <div className="flex items-center gap-2 text-rose-800 truncate">
                        <AlertTriangle className="w-3.5 h-3.5 text-rose-500 shrink-0" />
                        <span className="truncate font-mono text-[11px]">
                          {cls.misconceptionLabel || cls.topMisconception}
                        </span>
                      </div>
                      <button
                        onClick={() => onDispatchDrill(cls.topMisconception, cls.name, cls.students?.length || cls.studentCount)}
                        className="shrink-0 text-[11px] font-bold text-rose-700 hover:text-rose-900 underline cursor-pointer"
                      >
                        Assign Fix
                      </button>
                    </div>
                  ) : (
                    <div className="bg-emerald-50 border border-emerald-200/80 rounded-xl p-2.5 flex items-center text-xs my-2 text-emerald-800">
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 mr-2 shrink-0" />
                      <span className="text-[11px] font-medium">All core CAPS objectives on track</span>
                    </div>
                  )}
                </div>

                {/* Card Action Buttons */}
                <div className="pt-4 border-t border-slate-100 flex items-center justify-between gap-2 mt-2">
                  <button
                    onClick={() => onNavigate('classDiagnostics')}
                    className="flex-1 text-center py-2 px-3 rounded-xl bg-slate-50 hover:bg-slate-100 border border-slate-200 text-slate-700 text-xs font-semibold transition-colors cursor-pointer"
                  >
                    Diagnostic View
                  </button>
                  <button
                    onClick={() => onSelectClassForTest(cls)}
                    className="flex-1 text-center py-2 px-3 rounded-xl bg-blue-50 hover:bg-blue-100 border border-blue-200/80 text-[#13519C] text-xs font-semibold transition-colors cursor-pointer"
                  >
                    Generate Test
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* 2. HUMANIZED LEARNER ROSTER & MARK BOOK TABLE */}
      <section className="bg-white border border-slate-200/90 rounded-2xl p-6 shadow-xs hover:shadow-md transition-all duration-200">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-5">
          <div className="flex items-center gap-2">
            <Users className="w-5 h-5 text-[#13519C]" />
            <div>
              <h2 
                style={{ fontFamily: "'Afacad', sans-serif" }}
                className="text-lg font-bold text-slate-900 tracking-tight"
              >
                Learner Roster &amp; Mastery Mark Book
              </h2>
              <p className="text-xs text-slate-500">Live individual mastery, authentic avatars, POPIA safety, and 1-click targeted remedial nudges</p>
            </div>
          </div>
        </div>

        {/* Filter Toolbar */}
        <div className="flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 mb-4 bg-slate-50 p-3 rounded-xl border border-slate-200/80">
          <div className="flex flex-wrap items-center gap-2">
            {/* Class Filter Pills */}
            <button
              onClick={() => setActiveClassFilter('all')}
              className={`px-3 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                activeClassFilter === 'all'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'
              }`}
            >
              All Classes ({allStudents.length})
            </button>
            {classes.map(c => (
              <button
                key={c.classId}
                onClick={() => setActiveClassFilter(c.classId)}
                className={`px-3 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                  activeClassFilter === c.classId
                    ? 'bg-[#13519C] text-white shadow-2xs'
                    : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'
                }`}
              >
                {c.subject} Gr {c.grade}
              </button>
            ))}
          </div>

          <div className="flex items-center gap-2">
            {/* Search Input */}
            <div className="relative flex-1 sm:w-56">
              <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                value={searchQuery}
                onChange={e => setSearchQuery(e.target.value)}
                placeholder="Search learner or topic..."
                className="w-full pl-8 pr-3 py-1.5 rounded-lg bg-white border border-slate-200 text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
              />
            </div>

            {/* Status Filter */}
            <select
              value={statusFilter}
              onChange={e => setStatusFilter(e.target.value)}
              className="px-2.5 py-1.5 rounded-lg bg-white border border-slate-200 text-xs text-slate-700 focus:outline-none focus:border-[#13519C] cursor-pointer"
            >
              <option value="all">All Statuses</option>
              <option value="Mastered">Mastered (80%+)</option>
              <option value="On Track">On Track (65-79%)</option>
              <option value="In Progress">In Progress (60-64%)</option>
              <option value="Remedial">Remedial (&lt;60%)</option>
            </select>
          </div>
        </div>

        {/* Mark Book Table */}
        <div className="overflow-x-auto rounded-xl border border-slate-200/90">
          <table className="w-full text-left text-xs text-slate-600">
            <thead className="bg-slate-50 text-slate-500 uppercase tracking-wider text-[10px] border-b border-slate-200 font-semibold font-sans">
              <tr>
                <th className="py-3 px-4">Learner Profile</th>
                <th className="py-3 px-4">Class</th>
                <th className="py-3 px-4">Active CAPS Topic</th>
                <th className="py-3 px-4">Score</th>
                <th className="py-3 px-4">Live Status</th>
                <th className="py-3 px-4">Olympiad / Honors</th>
                <th className="py-3 px-4 text-right">Interactive Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 bg-white">
              {filteredStudents.length === 0 ? (
                <tr>
                  <td colSpan={7} className="py-8 text-center text-slate-400 text-xs">
                    No learners match the current filter.
                  </td>
                </tr>
              ) : (
                filteredStudents.map((student) => (
                  <tr key={student.id} className="hover:bg-slate-50/80 transition-colors">
                    {/* Learner Avatar & Name */}
                    <td className="py-3 px-4 font-semibold text-slate-900">
                      <div className="flex items-center gap-3">
                        <AvatarWithFallback
                          src={student.photoURL}
                          name={student.name}
                          size="md"
                        />
                        <div>
                          <div className="font-semibold text-slate-900 leading-tight">{student.name}</div>
                          <div className="text-[11px] text-slate-400 font-mono">{student.email || `${student.id}@fundile.co.za`}</div>
                        </div>
                      </div>
                    </td>

                    {/* Class Name */}
                    <td className="py-3 px-4 text-slate-600">
                      <span className="font-medium text-slate-700">{student.className}</span>
                    </td>

                    {/* Active Topic & Misconception Warning */}
                    <td className="py-3 px-4">
                      <div>
                        <span className="font-medium text-slate-800">{student.topic || 'General Practice'}</span>
                        {student.misconceptionDesc && (
                          <div className="text-[10px] text-rose-600 flex items-center gap-1 mt-0.5">
                            <AlertTriangle className="w-3 h-3 text-rose-500 shrink-0" />
                            <span className="truncate">{student.misconceptionDesc}</span>
                          </div>
                        )}
                      </div>
                    </td>

                    {/* Score */}
                    <td className="py-3 px-4">
                      <span className={`font-mono font-bold text-sm ${
                        student.score >= 80 ? 'text-emerald-600' :
                        student.score >= 65 ? 'text-[#13519C]' :
                        student.score >= 50 ? 'text-amber-600' : 'text-rose-600'
                      }`}>
                        {student.score}%
                      </span>
                    </td>

                    {/* Live Status Badge */}
                    <td className="py-3 px-4">
                      <StatusBadge status={student.status} />
                    </td>

                    {/* Olympiad Recognition */}
                    <td className="py-3 px-4">
                      {student.olympiadBadge ? (
                        <span className="bg-amber-50 text-amber-900 border border-amber-200/90 px-2.5 py-0.5 rounded-full text-[10px] font-semibold inline-flex items-center gap-1 shadow-2xs font-mono">
                          <Award className="w-3 h-3 text-[#FF9100]" />
                          {student.olympiadBadge}
                        </span>
                      ) : (
                        <span className="text-slate-400 text-[11px] font-mono">—</span>
                      )}
                    </td>

                    {/* Interactive 1-Click Actions */}
                    <td className="py-3 px-4 text-right">
                      <div className="flex items-center justify-end gap-1.5">
                        {/* 1-Click Remedial Drill Button */}
                        {student.status === 'Remedial' && (
                          <button
                            onClick={() => onDispatchDrill(student.misconception || 'Foundational Revision', student.className, 1)}
                            title="Assign 5-minute remedial micro-drill"
                            className="px-2 py-1 bg-rose-50 hover:bg-rose-100 border border-rose-200 text-rose-700 rounded-md text-[10px] font-bold transition-colors cursor-pointer"
                          >
                            Assign Fix
                          </button>
                        )}

                        {/* 1-Click WhatsApp Nudge */}
                        <button
                          onClick={() => handleSendNudge(student)}
                          title="Send learner practice nudge via WhatsApp"
                          className="px-2 py-1 bg-emerald-50 hover:bg-emerald-100 border border-emerald-200 text-emerald-800 rounded-md text-[10px] font-semibold transition-colors flex items-center gap-1 cursor-pointer"
                        >
                          <Share2 className="w-3 h-3 text-emerald-600" />
                          <span>{copiedNudge === student.id ? 'Nudge Copied!' : 'Send Nudge'}</span>
                        </button>

                        {/* POPIA Avatar Reset */}
                        {student.photoURL && (
                          <button
                            onClick={() => onResetAvatar(student.id, student.name)}
                            title="POPIA Minor Safety: Reset avatar to monogram initials"
                            className="p-1 rounded-md text-slate-400 hover:text-amber-700 hover:bg-amber-50 border border-transparent hover:border-amber-200 transition-colors cursor-pointer"
                          >
                            <RotateCcw className="w-3.5 h-3.5" />
                          </button>
                        )}

                        {/* Full Inspect */}
                        <button
                          onClick={() => onNavigate('submissions')}
                          title="Inspect learner submissions"
                          className="p-1 text-slate-400 hover:text-[#13519C] hover:bg-blue-50 rounded-md transition-colors cursor-pointer"
                        >
                          <ExternalLink className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </section>

    </div>
  );
}
