import React, { useState } from 'react';
import { School, CheckCircle2, AlertCircle, X, ArrowRight, Loader2 } from 'lucide-react';
import studentStore from '../../services/studentStore';
import { redeemSchoolPasskeyForIndependentLearner } from '../../services/schoolEnrollmentService';

/**
 * JoinClassModal Component (Layer D — Phase D4)
 * Allows students to enter a 6-character join code provided by their teacher or tutor
 * or an institutional Grade Master Passkey (e.g. WHS-GR10-8421) to link to their school.
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
  const [result, setResult] = useState(null); // { success: boolean, message: string, class?: object, refundClaim?: object }

  if (!isOpen) return null;

  const handleJoin = async (e) => {
    e.preventDefault();
    const cleanCode = code.trim().toUpperCase();
    if (cleanCode.length < 6) {
      setResult({
        success: false,
        message: 'Codes must be at least 6 characters (e.g. MTH701 or WHS-GR10-8421).',
      });
      return;
    }

    setLoading(true);
    setResult(null);

    try {
      // Check if code is a Grade Master Passkey (e.g. WHS-GR10-8421)
      const isMasterPasskey = cleanCode.includes('-GR') || cleanCode.startsWith('WHS-') || cleanCode.length > 8;
      if (isMasterPasskey) {
        const studentProfile = studentStore.getState();
        const res = redeemSchoolPasskeyForIndependentLearner(cleanCode, studentProfile);
        if (!res.success) {
          setResult({
            success: false,
            message: res.error || 'Invalid or already claimed Master Pass key.',
          });
          return;
        }

        const refund = res.refundClaim;
        setResult({
          success: true,
          isSchoolTransition: true,
          message: `Enrolled at ${res.school.name}!`,
          details: refund?.refundAmountRands > 0
            ? `Retail pass transitioned. Current active month was forfeited; R${refund.refundAmountRands.toFixed(2)} (${refund.unactivatedMonths} un-activated month(s)) queued for refund to guardian.`
            : 'Retail pass transitioned to school license. Current active month was forfeited.',
          refundClaim: refund,
          school: res.school
        });
        onJoinedSuccess(res);
        return;
      }

      const isCapsJoinCode = cleanCode === 'MTH701' || cleanCode.startsWith('MTH') || cleanCode.startsWith('MAT') || cleanCode.startsWith('ACC') || cleanCode.startsWith('SCI') || cleanCode.startsWith('EMS') || cleanCode.startsWith('PHY') || cleanCode.startsWith('BUS') || cleanCode === 'MATH8X';
      if (isCapsJoinCode) {
        studentStore.joinTeacherClass(cleanCode);

        // Dynamically persist enrolled learner to class records
        try {
          const enrolledKey = `fundile_class_enrolled_students_${cleanCode}`;
          const currentEnrolled = JSON.parse(localStorage.getItem(enrolledKey) || '[]');
          const studentProfile = studentStore.getState();
          const effectiveName = studentProfile.studentName || studentName || 'Learner';
          const effectivePhoto = studentProfile.photoURL || localStorage.getItem('fundile_user_photoURL') || null;
          const subKey = cleanCode.startsWith('ACC') ? 'accounting' : cleanCode.startsWith('MAT') ? 'mathematics' : 'ems';
          const subProgress = studentProfile.subjects?.[subKey] || {};
          const score = subProgress.formativeMastery || 88;

          const existingIdx = currentEnrolled.findIndex(s => s.name === effectiveName);
          const record = {
            id: studentProfile.studentId || `std_live_${cleanCode}`,
            name: effectiveName,
            email: studentProfile.email || `${effectiveName.toLowerCase().replace(/\s+/g, '.')}@fundile.co.za`,
            score: score,
            status: score >= 80 ? 'Mastered' : score >= 60 ? 'On Track' : 'In Progress',
            photoURL: effectivePhoto,
            topic: subProgress.lastPracticed ? 'Cash Receipts Journal (VAT 15%)' : 'Cash Receipts & Payments Journals',
            olympiadBadge: score >= 90 ? '🥇 Live Distinction' : null,
            misconception: null,
            lastActive: 'Just now'
          };

          if (existingIdx >= 0) {
            currentEnrolled[existingIdx] = record;
          } else {
            currentEnrolled.unshift(record);
          }
          localStorage.setItem(enrolledKey, JSON.stringify(currentEnrolled));
        } catch (enrollErr) {
          console.warn('Could not persist enrolled student to class roster:', enrollErr);
        }

        let subject = 'Mathematics';
        let teacherName = 'Mr. Sithole';
        let gradeStr = '10';
        if (cleanCode.startsWith('ACC')) {
          subject = 'Accounting';
          teacherName = 'Mr. N. Sithole';
          gradeStr = cleanCode.includes('12') ? '12' : '10';
        } else if (cleanCode.startsWith('MTH7')) {
          subject = 'Mathematics';
          teacherName = 'Mrs. Patience Khumalo';
          gradeStr = '7';
        } else if (cleanCode.startsWith('SCI')) {
          subject = 'Natural Sciences';
          teacherName = 'Mrs. D. Ndlovu';
          gradeStr = '8';
        } else if (cleanCode.startsWith('EMS')) {
          subject = 'EMS';
          teacherName = 'Mr. V. Mokoena';
          gradeStr = '9';
        } else if (cleanCode.startsWith('PHY')) {
          subject = 'Physical Sciences';
          teacherName = 'Dr. H. Botha';
          gradeStr = '11';
        }
        const mockClass = {
          name: `Grade ${gradeStr} ${subject} — Term 1`,
          subject,
          grade: gradeStr,
          teacherName,
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
            data-testid="btn-close-join-class"
            aria-label="Close"
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
                {result.isSchoolTransition && (
                  <div
                    data-testid="box-institutional-transition-refund"
                    className="mt-3 p-3 rounded-lg bg-amber-950/60 border border-amber-500/40 text-amber-200 text-xs text-left space-y-1"
                  >
                    <div className="font-bold text-amber-300 flex items-center gap-1.5">
                      <span>🏛️ Institutional Transition Complete</span>
                    </div>
                    <p data-testid="text-transition-refund-details" className="text-[11px] leading-relaxed text-amber-100">{result.details}</p>
                    <div className="text-[10px] text-amber-400/80 pt-1 border-t border-amber-500/20">
                      Academic mastery, progress history, and guardian links have been 100% preserved.
                    </div>
                  </div>
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
                Enter your 6-character class code (e.g. <span className="font-mono text-amber-300 font-bold">MTH701</span>) or your institutional Grade Master Passkey (e.g. <span className="font-mono text-cyan-300 font-bold">WHS-GR10-8421</span>).
              </p>

              <div>
                <label className="block text-[11px] font-semibold uppercase tracking-wider text-slate-400 mb-1.5">
                  Class Join Code or School Master Passkey
                </label>
                <input
                  type="text"
                  maxLength={20}
                  data-testid="input-join-class-code"
                  value={code}
                  onChange={e => setCode(e.target.value.toUpperCase())}
                  placeholder="e.g. MTH701 or WHS-GR10-8421"
                  className="w-full px-4 py-3 rounded-xl bg-slate-950 border-2 border-slate-700 focus:border-cyan-500 text-center font-mono text-lg font-bold text-amber-300 tracking-wider placeholder:tracking-normal placeholder:font-normal placeholder:text-slate-600 focus:outline-none uppercase"
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
                disabled={loading || code.trim().length < 6}
                className="w-full py-2.5 rounded-xl bg-cyan-600 hover:bg-cyan-500 disabled:opacity-50 text-white font-bold text-xs transition flex items-center justify-center gap-2 shadow-md cursor-pointer"
              >
                {loading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Enrolling...
                  </>
                ) : (
                  <>
                    {code.includes('-GR') || code.length > 8 ? 'Redeem Passkey & Link School' : 'Join Class'}
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
