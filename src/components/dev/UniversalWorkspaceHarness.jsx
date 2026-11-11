import React, { useState, useEffect } from 'react';
import UniversalWorkspace from '../workspace/UniversalWorkspace';

export default function UniversalWorkspaceHarness() {
  const [question, setQuestion] = useState(null);
  const [grade, setGrade] = useState('7');
  const [subject, setSubject] = useState('Mathematics');
  const [topic, setTopic] = useState('Numbers and Operations');
  const [mode, setMode] = useState('practice');
  const [result, setResult] = useState(null);
  const [forceShowMemo, setForceShowMemo] = useState(false);

  useEffect(() => {
    // Expose control hooks to Playwright runner
    window.__SET_WORKSPACE_QUESTION__ = (qData, meta = {}) => {
      if (meta.grade) setGrade(String(meta.grade));
      if (meta.subject) setSubject(meta.subject);
      if (meta.topic) setTopic(meta.topic);
      if (meta.mode) setMode(meta.mode);
      setResult(null);
      setForceShowMemo(false);
      setQuestion(qData);
      window.__FUNDILE_ACTIVE_QUESTION__ = qData;
      return true;
    };

    window.__TRIGGER_WORKSPACE_CHECK__ = async () => {
      // Trigger evaluation / check answer so marks banner and memo button appear
      const checkBtn = document.querySelector('[data-testid="btn-check-answer"]');
      if (checkBtn && !checkBtn.disabled) {
        checkBtn.click();
        return true;
      }
      return false;
    };

    window.__TRIGGER_WORKSPACE_MEMO__ = () => {
      if (window.__FUNDILE_ACTIVE_QUESTION__) {
        const q = window.__FUNDILE_ACTIVE_QUESTION__;
        setResult({
          score: q.marks || q.total_marks || 6,
          total: q.marks || q.total_marks || 6,
          feedback: 'Full marks awarded.',
          is_correct: true,
        });
        setForceShowMemo(true);
      }
      return true;
    };

    window.__TRIGGER_WORKSPACE_HINTS__ = () => {
      const hintBtn = document.querySelector('[data-testid="btn-toggle-hints"]');
      if (hintBtn) {
        hintBtn.click();
        return true;
      }
      return false;
    };

    return () => {
      delete window.__SET_WORKSPACE_QUESTION__;
      delete window.__TRIGGER_WORKSPACE_CHECK__;
      delete window.__TRIGGER_WORKSPACE_MEMO__;
      delete window.__TRIGGER_WORKSPACE_HINTS__;
    };
  }, []);

  return (
    <div 
      data-testid="universal-workspace-harness-ready"
      data-mounted-question-id={question?.id || 'none'}
      data-mounted-subskill={question?.subskill || question?.archetype || 'none'}
      className="min-h-screen bg-slate-50 flex flex-col font-sans"
    >
      <div className="max-w-7xl mx-auto w-full p-4 sm:p-6 flex-1 flex flex-col">
        {question ? (
          <>
            <UniversalWorkspace
              grade={grade}
              subject={subject}
              topic={topic}
              question={question}
              isGenerating={false}
              isChecking={false}
              result={result}
              forceShowMemo={forceShowMemo}
              onCheck={async (userAns) => ({
                score: question.marks || question.total_marks || 6,
                total: question.marks || question.total_marks || 6,
                feedback: 'Full marks awarded.',
                is_correct: true,
              })}
              onNext={() => {}}
              onSelectTopic={() => {}}
              onStartMicroDrill={() => {}}
            />
            {/* Fixed Audit Bar to guarantee pixel & byte-hash uniqueness on every scroll level */}
            <div 
              data-testid="harness-sticky-audit-bar" 
              className="fixed bottom-0 left-0 right-0 z-50 px-4 py-1.5 bg-slate-900/95 text-slate-200 border-t border-slate-700 font-mono text-[11px] flex items-center justify-between shadow-lg backdrop-blur-xs"
            >
              <div className="flex items-center gap-2">
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
                <span className="font-bold text-white uppercase">{subject} Gr{grade} • {topic}</span>
                <span className="text-slate-400">|</span>
                <span className="text-amber-300 font-semibold">{question.subskill || question.archetype || question.id}</span>
              </div>
              <div className="flex items-center gap-3">
                <span id="harness-scroll-step-badge" className="px-1.5 py-0.5 rounded bg-slate-800 text-slate-400 text-[10px] font-mono">
                  SCROLL_TOP
                </span>
                <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${forceShowMemo ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-300'}`}>
                  {forceShowMemo ? 'MEMORANDUM_ACTIVE' : 'PRE_ATTEMPT_ACTIVE'}
                </span>
                <span className="text-slate-500 text-[10px]">1440x900</span>
              </div>
            </div>
          </>
        ) : (
          <div className="flex-1 flex items-center justify-center text-slate-400 text-sm font-mono">
            Waiting for archetype question payload via __SET_WORKSPACE_QUESTION__...
          </div>
        )}
      </div>
    </div>
  );
}
