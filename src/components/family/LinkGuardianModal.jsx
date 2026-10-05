import React, { useState, useEffect } from 'react';
import { 
  ShieldCheck, 
  Clock, 
  Copy, 
  Check, 
  X, 
  AlertTriangle, 
  Sparkles, 
  RefreshCw, 
  UserCheck, 
  Users,
  Lock,
  Info
} from 'lucide-react';
import { 
  createTemporaryLinkCode, 
  getActiveLinkCode, 
  cancelLinkCode 
} from '../../services/familyLinkService';

const LinkGuardianModal = ({ isOpen, onClose, db, currentUser }) => {
  const [activeCodeData, setActiveCodeData] = useState(null);
  const [remainingSeconds, setRemainingSeconds] = useState(0);
  const [isGenerating, setIsGenerating] = useState(false);
  const [isCopied, setIsCopied] = useState(false);
  const [error, setError] = useState(null);

  // Mock linked guardians for demo/student display
  const [linkedGuardians, setLinkedGuardians] = useState(() => {
    try {
      const stored = localStorage.getItem('fundile_linked_guardians');
      return stored ? JSON.parse(stored) : [];
    } catch (e) {
      return [];
    }
  });

  // Check for active code when modal opens
  useEffect(() => {
    if (!isOpen || !currentUser) return;
    
    let isMounted = true;
    const fetchCurrent = async () => {
      try {
        const studentId = currentUser.uid || currentUser.id || 'current_student';
        const code = await getActiveLinkCode(db, studentId);
        if (isMounted && code) {
          setActiveCodeData(code);
          setRemainingSeconds(code.remainingSeconds || 900);
        }
      } catch (err) {
        console.warn('Error fetching active link code:', err);
      }
    };

    fetchCurrent();
    return () => { isMounted = false; };
  }, [isOpen, db, currentUser]);

  // Second-by-second countdown timer
  useEffect(() => {
    if (!activeCodeData || remainingSeconds <= 0) return;

    const timer = setInterval(() => {
      setRemainingSeconds((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          setActiveCodeData(null);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [activeCodeData, remainingSeconds]);

  if (!isOpen) return null;

  const formatTimer = (seconds) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins}:${secs.toString().padStart(2, '0')}`;
  };

  const handleGenerate = async () => {
    setIsGenerating(true);
    setError(null);
    try {
      const student = {
        uid: currentUser?.uid || currentUser?.id || 'learner_01',
        name: currentUser?.name || currentUser?.displayName || 'Learner',
        grade: currentUser?.grade || 'Grade 10 FET',
        school: currentUser?.school || 'High School',
      };
      const newCode = await createTemporaryLinkCode(db, student);
      setActiveCodeData(newCode);
      setRemainingSeconds(newCode.remainingSeconds || 900);
    } catch (err) {
      setError(err.message || 'Failed to generate code. Please try again.');
    } finally {
      setIsGenerating(false);
    }
  };

  const handleCancel = async () => {
    if (!activeCodeData) return;
    const studentId = currentUser?.uid || currentUser?.id || 'current_student';
    await cancelLinkCode(db, activeCodeData.code, studentId);
    setActiveCodeData(null);
    setRemainingSeconds(0);
  };

  const handleCopy = () => {
    if (!activeCodeData?.code) return;
    navigator.clipboard.writeText(activeCodeData.code);
    setIsCopied(true);
    setTimeout(() => setIsCopied(false), 2500);
  };

  const handleRevokeGuardian = (guardianId) => {
    const confirmed = window.confirm('Are you sure you want to disconnect this parent/guardian? They will no longer receive your weekly progress reports.');
    if (!confirmed) return;
    
    setLinkedGuardians((prev) => {
      const next = prev.filter((g) => g.id !== guardianId);
      try {
        localStorage.setItem('fundile_linked_guardians', JSON.stringify(next));
      } catch (e) {}
      return next;
    });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs animate-in fade-in duration-200">
      <div className="bg-white border border-slate-200 rounded-2xl shadow-2xl max-w-lg w-full overflow-hidden text-slate-900 flex flex-col">
        
        {/* Modal Header */}
        <div className="p-4 sm:p-5 border-b border-slate-200 flex items-center justify-between bg-slate-50">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-xl bg-blue-100 flex items-center justify-center text-[#13519C]">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-base text-slate-900 font-afacad">
                Family &amp; Guardian Link
              </h3>
              <p className="text-[11px] text-slate-500 font-medium">
                POPIA Section 35 Ephemeral Security Handshake
              </p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-slate-600 p-1.5 rounded-lg hover:bg-slate-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-5 sm:p-6 space-y-5 overflow-y-auto max-h-[80vh]">

          {/* Active Code or Generation Trigger */}
          {activeCodeData && remainingSeconds > 0 ? (
            <div className="p-5 rounded-2xl bg-blue-50/70 border border-blue-200 text-center space-y-4">
              <div className="flex items-center justify-center gap-1.5 text-xs font-semibold text-[#13519C] uppercase tracking-wider">
                <Clock className="w-4 h-4 animate-pulse" />
                <span>Single-Use Passcode Active</span>
              </div>

              {/* Code Display */}
              <div className="flex items-center justify-center gap-3">
                <div className="px-5 py-3 rounded-xl bg-white border-2 border-[#13519C] shadow-xs">
                  <span className="font-mono text-3xl sm:text-4xl font-black tracking-widest text-[#13519C]">
                    {activeCodeData.code}
                  </span>
                </div>
                <button
                  type="button"
                  onClick={handleCopy}
                  className="p-3 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white shadow-xs transition-colors flex items-center justify-center"
                  title="Copy Passcode"
                >
                  {isCopied ? <Check className="w-5 h-5 text-emerald-300" /> : <Copy className="w-5 h-5" />}
                </button>
              </div>

              {/* Countdown Timer */}
              <div className="flex items-center justify-center gap-2 text-sm font-bold text-slate-700">
                <span className="text-slate-500 font-normal">Expires in:</span>
                <span className="font-mono px-2 py-0.5 rounded bg-blue-100 text-[#13519C] font-extrabold">
                  {formatTimer(remainingSeconds)}
                </span>
              </div>

              {/* Confidentiality Warning */}
              <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 text-left flex items-start gap-2.5">
                <Lock className="w-4 h-4 text-amber-700 shrink-0 mt-0.5" />
                <p className="text-[11px] text-amber-900 leading-relaxed">
                  <strong className="font-bold">Keep this code strictly confidential:</strong> Only share this code directly with your parent or legal guardian. It expires in 15 minutes and works only once. Never share this code with classmates or strangers.
                </p>
              </div>

              {/* Action Buttons */}
              <div className="flex items-center justify-center gap-3 pt-1">
                <button
                  type="button"
                  onClick={handleCancel}
                  className="px-3.5 py-1.5 rounded-lg border border-slate-300 text-xs font-semibold text-slate-600 hover:bg-slate-100 transition-colors"
                >
                  Cancel Code
                </button>
                <button
                  type="button"
                  onClick={handleGenerate}
                  className="px-3.5 py-1.5 rounded-lg bg-[#13519C] text-xs font-semibold text-white hover:bg-[#0f3e77] transition-colors flex items-center gap-1.5"
                >
                  <RefreshCw className="w-3.5 h-3.5" />
                  Generate Fresh Code
                </button>
              </div>
            </div>
          ) : (
            <div className="p-5 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-4">
              <div className="w-12 h-12 rounded-2xl bg-blue-100 text-[#13519C] mx-auto flex items-center justify-center">
                <Sparkles className="w-6 h-6" />
              </div>
              <div>
                <h4 className="font-bold text-base text-slate-900">
                  Connect Your Parent or Guardian
                </h4>
                <p className="text-xs text-slate-600 mt-1 max-w-sm mx-auto">
                  Generate a temporary 15-minute passcode to give to your parent. Once linked, they can view your weekly study focus times and sponsor your subscription.
                </p>
              </div>

              <div className="p-3 rounded-xl bg-blue-50/70 border border-blue-100 text-left text-[11px] text-slate-600 space-y-1.5">
                <div className="flex items-center gap-1.5 text-slate-800 font-semibold">
                  <ShieldCheck className="w-3.5 h-3.5 text-[#13519C]" />
                  <span>Privacy-First Architecture</span>
                </div>
                <p>• Your personal messages and tutor chats are <strong>never shared</strong>.</p>
                <p>• Only high-level study times and mastered topics are included in weekly summaries.</p>
                <p>• You can disconnect a guardian at any time with 1 tap.</p>
              </div>

              {error && <p className="text-xs text-rose-600 font-medium">{error}</p>}

              <button
                type="button"
                onClick={handleGenerate}
                disabled={isGenerating}
                className="w-full py-3 px-4 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white font-bold text-sm shadow-xs transition-colors flex items-center justify-center gap-2 cursor-pointer disabled:bg-slate-400"
              >
                {isGenerating ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    Generating Secure Code...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-4 h-4" />
                    Generate 15-Minute Link Code
                  </>
                )}
              </button>
            </div>
          )}

          {/* Connected Guardians List */}
          <div className="border-t border-slate-100 pt-4 space-y-3">
            <h5 className="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
              <Users className="w-4 h-4 text-[#13519C]" />
              <span>Currently Linked Guardians ({linkedGuardians.length})</span>
            </h5>

            {linkedGuardians.length > 0 ? (
              <div className="space-y-2">
                {linkedGuardians.map((guardian) => (
                  <div 
                    key={guardian.id}
                    className="p-3 rounded-xl bg-slate-50 border border-slate-200 flex items-center justify-between"
                  >
                    <div className="flex items-center gap-2.5">
                      <div className="w-8 h-8 rounded-full bg-[#13519C] text-white font-bold text-xs flex items-center justify-center">
                        {guardian.name?.slice(0, 2).toUpperCase() || 'GD'}
                      </div>
                      <div>
                        <div className="text-xs font-bold text-slate-900">{guardian.name}</div>
                        <div className="text-[10px] text-slate-500">{guardian.email || 'Parent/Guardian'}</div>
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={() => handleRevokeGuardian(guardian.id)}
                      className="text-xs font-semibold text-rose-600 hover:text-rose-800 hover:underline cursor-pointer"
                    >
                      Disconnect
                    </button>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-xs text-slate-500 italic">
                No guardians currently linked to this account.
              </p>
            )}
          </div>
        </div>

        {/* Modal Footer */}
        <div className="p-4 border-t border-slate-200 flex justify-end bg-slate-50">
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-2 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-700 text-xs font-bold transition-colors cursor-pointer"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};

export default LinkGuardianModal;
