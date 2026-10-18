import React, { useState } from 'react';
import { BookOpen, Check, ShieldCheck, GraduationCap, X, ChevronRight } from 'lucide-react';
import { WHS_GRADE10_CLASS_OFFERINGS, enrollStudentIntoClasses } from '../../services/schoolEnrollmentService';

export default function SubjectEnrollmentModal({
  isOpen,
  onClose,
  currentUser,
  schoolName = 'Westville High School',
  grade = 10,
  onEnrollmentComplete = () => {}
}) {
  const [selections, setSelections] = useState({
    accounting: 'ACC10A',
    mathematics: 'MATH10B',
    physics: 'none',
    business: 'none'
  });
  const [isSaving, setIsSaving] = useState(false);

  if (!isOpen) return null;

  const handleSelectClass = (subjectKey, value) => {
    setSelections(prev => ({ ...prev, [subjectKey]: value }));
  };

  const handleSave = () => {
    setIsSaving(true);
    try {
      const studentProfile = {
        id: currentUser?.uid || currentUser?.id || `std_${Date.now()}`,
        name: currentUser?.name || 'Lesedi Khumalo',
        email: currentUser?.email || 'lesedi.khumalo@gmail.com',
        photoURL: currentUser?.photoURL || localStorage.getItem('fundile_user_photoURL') || null,
        score: 88
      };

      const result = enrollStudentIntoClasses(studentProfile, selections);
      onEnrollmentComplete(result);
      onClose();
    } catch (e) {
      console.error('Error saving subject enrollments:', e);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div className="bg-white rounded-2xl border border-slate-200/90 shadow-2xl w-full max-w-lg overflow-hidden animate-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="bg-gradient-to-r from-[#13519C] to-[#0f3e77] text-white p-6 relative">
          <button
            onClick={onClose}
            className="absolute top-4 right-4 text-white/70 hover:text-white p-1 rounded-lg"
          >
            <X className="w-5 h-5" />
          </button>

          <div className="flex items-center gap-2 mb-2">
            <span className="px-2.5 py-0.5 rounded-full bg-white/20 text-white text-xs font-bold inline-flex items-center gap-1">
              <ShieldCheck className="w-3.5 h-3.5" />
              Verified Institutional Pass
            </span>
            <span className="text-xs text-blue-100 font-semibold">• Grade {grade} FET</span>
          </div>

          <h2 
            style={{ fontFamily: "'Afacad', sans-serif" }}
            className="text-2xl font-bold tracking-tight"
          >
            {schoolName}
          </h2>
          <p className="text-xs text-blue-100 mt-1">
            Select your subjects and your assigned teachers for this academic year. You can change these later in your settings.
          </p>
        </div>

        {/* Subject & Teacher Selectors */}
        <div className="p-6 space-y-4 max-h-[60vh] overflow-y-auto">
          
          {/* Accounting */}
          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50/60 hover:bg-slate-50 transition">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" />
                <span className="font-bold text-sm text-slate-900">Accounting</span>
              </div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
                Commercial Sciences
              </span>
            </div>
            <select
              value={selections.accounting}
              data-testid="select-enrolled-class-accounting"
              onChange={e => handleSelectClass('accounting', e.target.value)}
              className="w-full text-xs font-medium py-2 px-3 rounded-lg border border-slate-200 bg-white text-slate-800 focus:outline-none focus:border-[#13519C]"
            >
              <option value="none">— Not taking this subject —</option>
              {WHS_GRADE10_CLASS_OFFERINGS.accounting.map(c => (
                <option key={c.joinCode} value={c.joinCode}>
                  {c.teacherName} — {c.name} ({c.joinCode})
                </option>
              ))}
            </select>
          </div>

          {/* Mathematics */}
          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50/60 hover:bg-slate-50 transition">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-blue-500" />
                <span className="font-bold text-sm text-slate-900">Mathematics</span>
              </div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-blue-800 bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">
                Mathematical Sciences
              </span>
            </div>
            <select
              value={selections.mathematics}
              data-testid="select-enrolled-class-mathematics"
              onChange={e => handleSelectClass('mathematics', e.target.value)}
              className="w-full text-xs font-medium py-2 px-3 rounded-lg border border-slate-200 bg-white text-slate-800 focus:outline-none focus:border-[#13519C]"
            >
              <option value="none">— Not taking this subject —</option>
              {WHS_GRADE10_CLASS_OFFERINGS.mathematics.map(c => (
                <option key={c.joinCode} value={c.joinCode}>
                  {c.teacherName} — {c.name} ({c.joinCode})
                </option>
              ))}
            </select>
          </div>

          {/* Physical Sciences */}
          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50/60 hover:bg-slate-50 transition">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-teal-500" />
                <span className="font-bold text-sm text-slate-900">Physical Sciences</span>
              </div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-teal-800 bg-teal-50 px-2 py-0.5 rounded-md border border-teal-200">
                Natural Sciences
              </span>
            </div>
            <select
              value={selections.physics}
              data-testid="select-enrolled-class-physics"
              onChange={e => handleSelectClass('physics', e.target.value)}
              className="w-full text-xs font-medium py-2 px-3 rounded-lg border border-slate-200 bg-white text-slate-800 focus:outline-none focus:border-[#13519C]"
            >
              <option value="none">— Not taking this subject —</option>
              {WHS_GRADE10_CLASS_OFFERINGS.physics.map(c => (
                <option key={c.joinCode} value={c.joinCode}>
                  {c.teacherName} — {c.name} ({c.joinCode})
                </option>
              ))}
            </select>
          </div>

          {/* Business Studies */}
          <div className="p-3.5 rounded-xl border border-slate-200 bg-slate-50/60 hover:bg-slate-50 transition">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-rose-500" />
                <span className="font-bold text-sm text-slate-900">Business Studies</span>
              </div>
              <span className="text-[10px] font-bold uppercase tracking-wider text-rose-800 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">
                Commercial Sciences
              </span>
            </div>
            <select
              value={selections.business}
              data-testid="select-enrolled-class-business"
              onChange={e => handleSelectClass('business', e.target.value)}
              className="w-full text-xs font-medium py-2 px-3 rounded-lg border border-slate-200 bg-white text-slate-800 focus:outline-none focus:border-[#13519C]"
            >
              <option value="none">— Not taking this subject —</option>
              {WHS_GRADE10_CLASS_OFFERINGS.business.map(c => (
                <option key={c.joinCode} value={c.joinCode}>
                  {c.teacherName} — {c.name} ({c.joinCode})
                </option>
              ))}
            </select>
          </div>

        </div>

        {/* Footer */}
        <div className="p-6 border-t border-slate-100 bg-slate-50 flex items-center justify-between gap-3">
          <p className="text-[11px] text-slate-500 leading-snug">
            Your teachers will receive your submissions and diagnostic reports in their class mark books.
          </p>

          <button
            onClick={handleSave}
            disabled={isSaving}
            data-testid="btn-save-subject-enrollment"
            className="inline-flex items-center gap-2 bg-[#13519C] hover:bg-[#0f3e77] text-white px-5 py-2.5 rounded-xl font-bold text-xs transition shadow-xs cursor-pointer shrink-0"
          >
            <span>{isSaving ? 'Enrolling...' : 'Save & Enter Desk'}</span>
            <ChevronRight className="w-4 h-4" />
          </button>
        </div>

      </div>
    </div>
  );
}
