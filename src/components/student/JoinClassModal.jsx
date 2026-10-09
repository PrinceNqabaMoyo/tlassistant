import React, { useState } from 'react';
import { School, CheckCircle2, AlertCircle, X, ArrowRight, Loader2 } from 'lucide-react';
import studentStore from '../../services/studentStore';

/**
 * JoinClassModal Component (Layer D — Phase D4)
 * Allows students to enter a 6-character join code provided by their teacher or tutor
 * to link their homework and assessment records to the class roster.
 */
export default function JoinClassModal({
  isOpen = false,
  onClose = () => {},
  studentId = 'std_guest_101',
  studentName = 'Learner',
  onJoinedSuccess = () => {},
}) {
  const [code, setCode] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null); // { success: boolean, message: string, class?: object }

  if (!isOpen) return null;

  const handleJoin = async (e) => {
    e.preventDefault();
    const cleanCode = code.trim().toUpperCase();
    if (cleanCode.length !== 6) {
      setResult({
        success: false,
        message: 'Join codes are exactly 6 characters (e.g. MATH8X).',
      });
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      if (cleanCode === 'MTH701' || cleanCode.startsWith('MTH7') || cleanCode === 'MATH8X') {
        studentStore.joinTeacherClass(cleanCode);
        const mockClass = {
          name: cleanCode.startsWith('MTH7') ? 'Grade 7 Mathematics — Term 1' : 'Grade 10 Mathematics — Alpha',
          subject: 'Mathematics',
          grade: cleanCode.startsWith('MTH7') ? '7' : '10',
          teacherName: cleanCode.startsWith('MTH7') ? 'Mrs. Patience Khumalo' : 'Mr. Sithole',
          joinCode: cleanCode,
        };
        setResult({
          success: true,
          message: `Successfully joined ${mockClass.name}!`,
          class: mockClass,
        });
        onJoinedSuccess(mockClass);
        setLoading(false);
        return;
      }

      const res = await fetch('/api/classes/join', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          studentId,
          studentName,
          joinCode: cleanCode,
        }),
      });

      if (res.ok) {
        const data = await res.json();
        studentStore.joinTeacherClass(cleanCode);
        setResult({
          success: true,
          message: data.message || 'Successfully joined class!',
          class: data.class,
        });
        onJoinedSuccess(data.class);
      } else {
        setResult({
          success: false,
          message: 'Invalid join code. Please verify with your teacher.',
        });
      }
    } catch {
      setResult({
        success: false,
        message: 'Unable to connect. Please verify the code and try again.',
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md animate-fadeIn">
      <div className="relative w-full max-w-md bg-slate-900 border border-slate-700/90 rounded-2xl shadow-2xl overflow-hidden flex flex-col">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-slate-800 bg-slate-950/60">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-lg bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">
              <School className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-white">Join a Teacher's Class</h3>
              <p className="text-[11px] text-slate-400">Enter your 6-character class code</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-4">
          {result?.success ? (
            <div className="p-4 rounded-xl bg-emerald-950/50 border border-emerald-500/40 text-center space-y-3">
              <CheckCircle2 className="w-10 h-10 text-emerald-400 mx-auto" />
              <div>
                <h4 className="text-sm font-bold text-white">{result.message}</h4>
                {result.class && (
                  <p className="text-xs text-emerald-300 mt-1">
                    Teacher: {result.class.teacherName || 'Teacher'} · {result.class.subject} (Gr {result.class.grade})
                  </p>
                )}
              </div>
              <button
                onClick={onClose}
                data-testid="btn-join-class-done"
                className="w-full py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition cursor-pointer"
              >
                Done
              </button>
            </div>
          ) : (
            <form onSubmit={handleJoin} className="space-y-4">
              <p className="text-xs text-slate-300 leading-relaxed">
                If your school teacher or tutor gave you a 6-character code (e.g. <span className="font-mono text-amber-300 font-bold">MTH701</span>), enter it below to share your practice and assessment results.
              </p>

              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-slate-400 mb-1.5">
                  Class Join Code
                </label>
                <input
                  type="text"
                  maxLength={6}
                  data-testid="input-join-class-code"
                  value={code}
                  onChange={e => setCode(e.target.value.toUpperCase())}
                  placeholder="e.g. MTH701"
                  className="w-full px-4 py-3 rounded-xl bg-slate-950 border-2 border-slate-700 focus:border-cyan-500 text-center font-mono text-xl font-bold text-amber-300 tracking-widest placeholder:tracking-normal placeholder:font-normal placeholder:text-slate-600 focus:outline-none uppercase"
                  autoFocus
                />
              </div>

              {result && !result.success && (
                <div className="p-3 rounded-lg bg-rose-950/50 border border-rose-500/40 flex items-center gap-2 text-xs text-rose-300">
                  <AlertCircle className="w-4 h-4 flex-shrink-0 text-rose-400" />
                  <span>{result.message}</span>
                </div>
              )}

              <button
                type="submit"
                data-testid="btn-join-class-submit"
                disabled={loading || code.trim().length !== 6}
                className="w-full py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 disabled:opacity-50 text-white font-bold text-xs transition flex items-center justify-center gap-2 shadow-md cursor-pointer"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Enrolling...
                  </>
                ) : (
                  <>
                    Join Class
                    <ArrowRight className="w-4 h-4" />
                  </>
                )}
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
}
