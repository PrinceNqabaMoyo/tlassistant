import React from 'react';
import { 
  Calculator, 
  BookOpen, 
  Briefcase, 
  FlaskConical, 
  Dna, 
  Coins, 
  Flame, 
  Pin, 
  CheckCircle2,
  FileSpreadsheet,
  Cpu,
  Leaf
} from 'lucide-react';

const SUBJECT_CONFIG = [
  { id: 'mathematics', label: 'Mathematics', icon: Calculator, color: 'from-blue-600 to-indigo-600', grades: [7, 8, 9, 10, 11, 12] },
  { id: 'ems', label: 'EMS', icon: Coins, color: 'from-amber-600 to-orange-600', grades: [7, 8, 9] },
  { id: 'natural_sciences', label: 'Natural Sciences', icon: Leaf, color: 'from-emerald-600 to-teal-600', grades: [7, 8, 9] },
  { id: 'accounting', label: 'Accounting', icon: BookOpen, color: 'from-emerald-600 to-teal-600', grades: [10, 11, 12] },
  { id: 'business_studies', label: 'Business Studies', icon: Briefcase, color: 'from-purple-600 to-pink-600', grades: [10, 11, 12] },
  { id: 'physical_sciences', label: 'Physical Sciences', icon: FlaskConical, color: 'from-cyan-600 to-blue-600', grades: [10, 11, 12] },
  { id: 'life_sciences', label: 'Life Sciences', icon: Dna, color: 'from-green-600 to-emerald-600', grades: [10, 11, 12] },
  { id: 'mathematical_literacy', label: 'Mathematical Literacy', icon: FileSpreadsheet, color: 'from-teal-600 to-cyan-600', grades: [10, 11, 12] },
  { id: 'technical_mathematics', label: 'Technical Mathematics', icon: Cpu, color: 'from-violet-600 to-indigo-600', grades: [10, 11, 12] },
];

export default function SubjectShelf({
  currentSubject,
  currentGrade,
  masterySummary = {},
  onSelectSubject,
  hasPendingHomework = {},
}) {
  const getSubjectString = (subj) => {
    if (!subj) return '';
    if (typeof subj === 'string') return subj;
    if (typeof subj === 'object') {
      return subj.name || subj.id || subj.label || subj.title || '';
    }
    return String(subj);
  };

  const subjectStr = getSubjectString(currentSubject);
  const normalizedCurrent = subjectStr.toLowerCase().replace(/\s+/g, '_');

  // Filter subjects strictly by student's active grade
  const numericGrade = parseInt(String(currentGrade || '10').replace(/\D/g, ''), 10);
  const visibleSubjects = Number.isFinite(numericGrade)
    ? SUBJECT_CONFIG.filter((sub) => sub.grades.includes(numericGrade))
    : SUBJECT_CONFIG;

  return (
    <div className="w-full bg-white/95 backdrop-blur border-b border-slate-200 px-4 py-2 overflow-x-auto scrollbar-none flex items-center gap-2.5 z-20 shadow-xs">
      <div className="flex items-center text-xs font-bold text-slate-500 uppercase tracking-wider pr-2.5 border-r border-slate-200 shrink-0">
        Subjects
        {Number.isFinite(numericGrade) && (
          <span className="ml-1.5 px-1.5 py-0.5 rounded bg-slate-100 text-slate-600 font-semibold text-[10px]">
            Gr {numericGrade}
          </span>
        )}
      </div>

      <div className="flex items-center gap-2 shrink-0">
        {visibleSubjects.map((sub) => {
          const Icon = sub.icon;
          const isSelected = normalizedCurrent === sub.id || normalizedCurrent === sub.label.toLowerCase().replace(/\s+/g, '_');
          const subjectMastery = masterySummary[sub.id] || 0;
          const isHomeworkPending = hasPendingHomework[sub.id];

          return (
            <button
              key={sub.id}
              onClick={() => {
                if (onSelectSubject) {
                  onSelectSubject(typeof currentSubject === 'object' && currentSubject !== null ? { ...currentSubject, name: sub.label, id: sub.id } : sub.label);
                }
              }}
              className={`flex items-center gap-2 px-3.5 py-1.5 rounded-full text-xs font-medium transition-all duration-200 shrink-0 cursor-pointer ${
                isSelected
                  ? 'bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-200 scale-105 font-semibold'
                  : 'bg-slate-100 hover:bg-slate-200/90 text-slate-700 hover:text-slate-900 border border-slate-200/80'
              }`}
            >
              <Icon className="w-3.5 h-3.5" />
              <span>{sub.label}</span>

              {/* Status Badges */}
              {isHomeworkPending && (
                <span className="flex items-center text-amber-800 bg-amber-50 px-1 rounded text-[10px] gap-0.5 border border-amber-300">
                  <Pin className="w-2.5 h-2.5" /> Due
                </span>
              )}

              {subjectMastery > 0 && !isHomeworkPending && (
                <span className={`text-[10px] px-1 rounded ${
                  isSelected ? 'bg-indigo-700 text-white' : 'bg-slate-200 text-slate-700 font-semibold'
                }`}>
                  {Math.round(subjectMastery)}%
                </span>
              )}

              {isSelected && (
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-300 animate-pulse" />
              )}
            </button>
          );
        })}
      </div>
    </div>
  );
}
