import React, { useState, useEffect } from 'react';
import { Settings, X, Check, RotateCcw, ShieldCheck } from 'lucide-react';
import { getSubjectTheme } from '../../theme/subjectPalette';

/**
 * SubjectManagerModal
 * Allows learners to customize their enrolled phase subjects.
 * 
 * Invariants:
 * - All subjects in the phase are available by default (e.g. 7 FET Phase subjects).
 * - A learner can take both Mathematics and Technical Mathematics (e.g. as a security option).
 * - Learners can eliminate/hide any subject they are not writing exams in.
 * - Restoring all defaults is a single 1-click action.
 */

export const ALL_FET_PHASE_SUBJECTS = [
  { id: 'accounting', name: 'Accounting', short: 'Accounting', domain: 'Commercial Sciences' },
  { id: 'mathematics', name: 'Mathematics', short: 'Maths', domain: 'Mathematical Sciences' },
  { id: 'technical_mathematics', name: 'Technical Mathematics', short: 'Tech Maths', domain: 'Mathematical Sciences' },
  { id: 'mathematical_literacy', name: 'Mathematical Literacy', short: 'Maths Lit', domain: 'Mathematical Sciences' },
  { id: 'physical_sciences', name: 'Physical Sciences', short: 'Physics', domain: 'Natural Sciences' },
  { id: 'life_sciences', name: 'Life Sciences', short: 'Life Sci', domain: 'Natural Sciences' },
  { id: 'business_studies', name: 'Business Studies', short: 'Business', domain: 'Commercial Sciences' },
];

export const ALL_SENIOR_PHASE_SUBJECTS = [
  { id: 'mathematics', name: 'Mathematics', short: 'Maths', domain: 'Mathematical Sciences' },
  { id: 'ems', name: 'Economic & Management Sciences', short: 'EMS', domain: 'Commercial Sciences' },
  { id: 'natural_sciences', name: 'Natural Sciences', short: 'Nat Sci', domain: 'Natural Sciences' },
];

export default function SubjectManagerModal({
  isOpen = false,
  onClose = () => {},
  enabledSubjects = ['accounting', 'mathematics', 'technical_mathematics', 'mathematical_literacy', 'physical_sciences', 'life_sciences', 'business_studies'],
  onSaveSubjects = () => {},
  currentGrade = 10,
}) {
  const isSeniorPhase = currentGrade <= 9;
  const phaseList = isSeniorPhase ? ALL_SENIOR_PHASE_SUBJECTS : ALL_FET_PHASE_SUBJECTS;
  
  const [selectedSet, setSelectedSet] = useState(() => new Set(enabledSubjects));

  useEffect(() => {
    setSelectedSet(new Set(enabledSubjects));
  }, [enabledSubjects, isOpen]);

  if (!isOpen) return null;

  const toggleSubject = (id) => {
    const next = new Set(selectedSet);
    if (next.has(id)) {
      // Don't allow deselecting if it's the last remaining subject
      if (next.size <= 1) return;
      next.delete(id);
    } else {
      next.add(id);
    }
    setSelectedSet(next);
  };

  const handleResetAll = () => {
    const allIds = phaseList.map(s => s.id);
    setSelectedSet(new Set(allIds));
  };

  const handleSave = () => {
    onSaveSubjects(Array.from(selectedSet));
    onClose();
  };

  const activeCount = selectedSet.size;
  const totalCount = phaseList.length;

  return (
    <div className="fixed inset-0 bg-slate-950/70 backdrop-blur-xs flex items-center justify-center p-4 z-50 animate-fadeIn select-none font-sans">
      <div 
        className="bg-white text-slate-900 w-full max-w-lg rounded-2xl shadow-2xl border border-slate-200 overflow-hidden flex flex-col max-h-[90vh] animate-scaleIn"
        role="dialog"
        aria-modal="true"
        aria-labelledby="manage-subjects-title"
      >
        {/* Header */}
        <div className="p-5 border-b border-slate-100 flex items-center justify-between bg-slate-50/80">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-600 flex items-center justify-center border border-amber-500/20 shadow-xs">
              <Settings className="w-5 h-5" />
            </div>
            <div>
              <h3 id="manage-subjects-title" className="text-base font-bold text-slate-900 font-display">
                Manage Phase Subjects
              </h3>
              <p className="text-xs text-slate-500">
                Grade {currentGrade} {isSeniorPhase ? 'Senior Phase' : 'FET Phase'} • {activeCount} of {totalCount} Active
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-slate-400 hover:text-slate-700 p-1.5 rounded-lg hover:bg-slate-100 transition cursor-pointer"
            aria-label="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Curricular Alignment Notice */}
        <div className="px-5 pt-4 pb-2 bg-blue-50/60 border-b border-blue-100/80 text-xs text-blue-900 flex items-start gap-2.5">
          <ShieldCheck className="w-4 h-4 text-[#13519C] shrink-0 mt-0.5" />
          <p className="leading-relaxed">
            All curriculum subjects are enabled by default. Taking both <strong>Mathematics</strong> and <strong>Technical Mathematics</strong> is fully supported as an authentic dual-study option. Toggle off any subjects you are not preparing for.
          </p>
        </div>

        {/* Subject Toggles List */}
        <div className="p-5 overflow-y-auto space-y-2.5 flex-1 max-h-[380px]">
          {phaseList.map((subject) => {
            const isEnabled = selectedSet.has(subject.id);
            const theme = getSubjectTheme(subject.id);

            return (
              <div 
                key={subject.id}
                onClick={() => toggleSubject(subject.id)}
                className={`flex items-center justify-between p-3 rounded-xl border transition-all cursor-pointer ${
                  isEnabled 
                    ? 'bg-slate-50/80 border-slate-200 hover:border-slate-300 shadow-2xs' 
                    : 'bg-slate-100/50 border-slate-200 opacity-60 hover:opacity-80'
                }`}
              >
                <div className="flex items-center gap-3">
                  <span 
                    className="w-3.5 h-3.5 rounded-full shrink-0 shadow-xs transition-transform"
                    style={{ 
                      backgroundColor: theme.base,
                      boxShadow: isEnabled ? theme.glowSm : 'none'
                    }}
                  />
                  <div>
                    <span className="font-bold text-xs text-slate-900 block font-display">
                      {subject.name}
                    </span>
                    <span className="text-[11px] text-slate-500 block">
                      {subject.domain}
                    </span>
                  </div>
                </div>

                <div className="flex items-center gap-2">
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                    isEnabled 
                      ? 'bg-emerald-100 text-emerald-800' 
                      : 'bg-slate-200 text-slate-600'
                  }`}>
                    {isEnabled ? 'Active' : 'Hidden'}
                  </span>

                  {/* Toggle switch */}
                  <div 
                    className={`w-10 h-6 rounded-full transition-colors relative flex items-center px-0.5 ${
                      isEnabled ? 'bg-[#13519C]' : 'bg-slate-300'
                    }`}
                  >
                    <div 
                      className={`w-5 h-5 rounded-full bg-white shadow-md transition-transform flex items-center justify-center ${
                        isEnabled ? 'translate-x-4' : 'translate-x-0'
                      }`}
                    >
                      {isEnabled && <Check className="w-3 h-3 text-[#13519C]" />}
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>

        {/* Modal Footer */}
        <div className="p-4 bg-slate-50 border-t border-slate-100 flex items-center justify-between">
          <button 
            type="button"
            onClick={handleResetAll}
            className="text-xs font-bold text-slate-600 hover:text-slate-900 flex items-center gap-1.5 transition cursor-pointer"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span>Enable All ({totalCount})</span>
          </button>
          
          <div className="flex items-center gap-2">
            <button 
              type="button"
              onClick={onClose}
              className="px-4 py-2 text-xs font-bold text-slate-600 hover:text-slate-900 rounded-xl hover:bg-slate-200/60 transition cursor-pointer"
            >
              Cancel
            </button>
            <button 
              type="button"
              onClick={handleSave}
              className="px-5 py-2 bg-[#13519C] hover:bg-[#0F4280] text-white text-xs font-bold rounded-xl shadow-sm hover:shadow transition cursor-pointer active:scale-98"
            >
              Done &amp; Update Studio
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
