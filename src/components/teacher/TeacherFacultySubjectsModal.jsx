import React, { useState } from 'react';
import { X, Check, BookOpen, AlertCircle, ShieldCheck } from 'lucide-react';
import {
  SENIOR_PHASE_SUBJECTS,
  FET_PHASE_SUBJECTS,
  MAX_SENIOR_PHASE_SUBJECTS,
  MAX_FET_PHASE_SUBJECTS,
  saveTeacherEnrolledSubjects
} from '../../services/teacherSubjectQuotaService';

export default function TeacherFacultySubjectsModal({
  isOpen = false,
  onClose = () => {},
  teacherId = 'default_educator',
  currentAllocation = { seniorPhase: ['EMS', 'Mathematics'], fetPhase: ['Accounting', 'Mathematics', 'Physical Sciences'] },
  onSave = () => {}
}) {
  const [seniorPhase, setSeniorPhase] = useState(currentAllocation?.seniorPhase || ['EMS', 'Mathematics']);
  const [fetPhase, setFetPhase] = useState(currentAllocation?.fetPhase || ['Accounting', 'Mathematics', 'Physical Sciences']);

  if (!isOpen) return null;

  const toggleSeniorSubject = (subjId) => {
    if (seniorPhase.includes(subjId)) {
      setSeniorPhase(seniorPhase.filter(s => s !== subjId));
    } else {
      if (seniorPhase.length >= MAX_SENIOR_PHASE_SUBJECTS) return;
      setSeniorPhase([...seniorPhase, subjId]);
    }
  };

  const toggleFetSubject = (subjId) => {
    if (fetPhase.includes(subjId)) {
      setFetPhase(fetPhase.filter(s => s !== subjId));
    } else {
      if (fetPhase.length >= MAX_FET_PHASE_SUBJECTS) return;
      setFetPhase([...fetPhase, subjId]);
    }
  };

  const handleConfirm = () => {
    const updated = saveTeacherEnrolledSubjects(teacherId, { seniorPhase, fetPhase });
    onSave(updated);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-[140] flex items-center justify-center bg-black/60 backdrop-blur-xs p-3 sm:p-4 select-none animate-in fade-in">
      <div 
        className="w-full max-w-lg bg-white rounded-3xl border border-slate-200 shadow-2xl overflow-hidden flex flex-col max-h-[88vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-[#13519C] text-white px-6 py-4 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center border border-white/20">
              <BookOpen className="w-5 h-5 text-amber-300" />
            </div>
            <div>
              <h3 className="text-lg font-bold text-white leading-tight font-display">
                Faculty Subject Allocation
              </h3>
              <p className="text-xs text-blue-200">
                South African school faculty quota enforcement
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-full text-white/80 hover:text-white hover:bg-white/10 transition cursor-pointer"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Body */}
        <div className="p-6 overflow-y-auto flex-1 font-sans space-y-5">
          {/* Section 1: Senior Phase */}
          <div className="space-y-3">
            <div className="flex items-center justify-between">
              <div>
                <h4 className="text-sm font-bold text-slate-900">
                  Senior Phase (Grades 7–9)
                </h4>
                <p className="text-xs text-slate-500">
                  General junior high faculty curriculum allocation
                </p>
              </div>
              <span className={`px-2.5 py-1 rounded-full text-xs font-bold font-mono ${
                seniorPhase.length === MAX_SENIOR_PHASE_SUBJECTS 
                  ? 'bg-amber-100 text-amber-800' 
                  : 'bg-slate-100 text-slate-700'
              }`}>
                {seniorPhase.length} / {MAX_SENIOR_PHASE_SUBJECTS} Allocated
              </span>
            </div>

            <div className="space-y-2">
              {SENIOR_PHASE_SUBJECTS.map((subj) => {
                const isChecked = seniorPhase.includes(subj.id);
                const isDisabled = !isChecked && seniorPhase.length >= MAX_SENIOR_PHASE_SUBJECTS;
                return (
                  <button
                    key={subj.id}
                    type="button"
                    disabled={isDisabled}
                    onClick={() => toggleSeniorSubject(subj.id)}
                    className={`w-full p-3 rounded-2xl border text-left flex items-center justify-between transition cursor-pointer ${
                      isChecked 
                        ? 'border-[#13519C] bg-blue-50/70 text-[#13519C] font-bold shadow-2xs' 
                        : isDisabled 
                          ? 'border-slate-100 bg-slate-50 text-slate-300 cursor-not-allowed'
                          : 'border-slate-200 hover:bg-slate-50 text-slate-700'
                    }`}
                  >
                    <span className="text-xs">{subj.name}</span>
                    <div className={`w-5 h-5 rounded-md flex items-center justify-center border ${
                      isChecked ? 'bg-[#13519C] border-[#13519C] text-white' : 'border-slate-300'
                    }`}>
                      {isChecked && <Check className="w-3.5 h-3.5" />}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Section 2: FET Phase */}
          <div className="space-y-3 pt-3 border-t border-slate-200">
            <div className="flex items-center justify-between">
              <div>
                <h4 className="text-sm font-bold text-slate-900">
                  FET Phase (Grades 10–12)
                </h4>
                <p className="text-xs text-slate-500">
                  Specialist matric examination stream allocation
                </p>
              </div>
              <span className={`px-2.5 py-1 rounded-full text-xs font-bold font-mono ${
                fetPhase.length === MAX_FET_PHASE_SUBJECTS 
                  ? 'bg-amber-100 text-amber-800' 
                  : 'bg-slate-100 text-slate-700'
              }`}>
                {fetPhase.length} / {MAX_FET_PHASE_SUBJECTS} Allocated
              </span>
            </div>

            <div className="space-y-2">
              {FET_PHASE_SUBJECTS.map((subj) => {
                const isChecked = fetPhase.includes(subj.id);
                const isDisabled = !isChecked && fetPhase.length >= MAX_FET_PHASE_SUBJECTS;
                return (
                  <button
                    key={subj.id}
                    type="button"
                    disabled={isDisabled}
                    onClick={() => toggleFetSubject(subj.id)}
                    className={`w-full p-3 rounded-2xl border text-left flex items-center justify-between transition cursor-pointer ${
                      isChecked 
                        ? 'border-[#13519C] bg-blue-50/70 text-[#13519C] font-bold shadow-2xs' 
                        : isDisabled 
                          ? 'border-slate-100 bg-slate-50 text-slate-300 cursor-not-allowed'
                          : 'border-slate-200 hover:bg-slate-50 text-slate-700'
                    }`}
                  >
                    <span className="text-xs">{subj.name}</span>
                    <div className={`w-5 h-5 rounded-md flex items-center justify-center border ${
                      isChecked ? 'bg-[#13519C] border-[#13519C] text-white' : 'border-slate-300'
                    }`}>
                      {isChecked && <Check className="w-3.5 h-3.5" />}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Footer */}
        <div className="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between shrink-0">
          <span className="text-xs text-slate-500">Max 2 SP • Max 3 FET</span>
          <button
            type="button"
            onClick={handleConfirm}
            className="px-5 py-2 bg-[#13519C] hover:bg-blue-800 text-white font-bold text-xs rounded-xl shadow-xs transition cursor-pointer"
          >
            Save Faculty Subjects
          </button>
        </div>
      </div>
    </div>
  );
}
