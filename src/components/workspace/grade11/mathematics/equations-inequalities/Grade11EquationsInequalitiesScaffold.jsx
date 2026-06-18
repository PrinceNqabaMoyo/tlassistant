
 import React from 'react';
 import VisualAidsPanel from '../../../VisualAidsPanel';
 import { renderMathText } from '../../../../../utils/renderMathText.jsx';
 
 const normalizeEqIneq = (value) => {
     if (value === null || value === undefined) return '';
     return String(value)
         .trim()
         .replace(/−/g, '-')
         .replace(/≤/g, '<=')
         .replace(/≥/g, '>=')
         .replace(/\s+/g, '')
         .toLowerCase();
 };
 
 const Grade11EquationsInequalitiesScaffold = ({
     onBack,
     scaffoldSteps,
     g11EqIneqVisualAidsOpen,
     setG11EqIneqVisualAidsOpen,
     g11EqIneqScaffoldDifficulty,
     setG11EqIneqScaffoldDifficulty,
     g11EqIneqScaffoldStepIndex,
     setG11EqIneqScaffoldStepIndex,
     fetchGrade11EqIneqScaffoldQuestion,
     g11EqIneqScaffoldLoading,
     g11EqIneqScaffoldError,
     g11EqIneqScaffoldQuestion,
     g11EqIneqScaffoldCheckpointIndex,
     setG11EqIneqScaffoldCheckpointIndex,
     g11EqIneqScaffoldCheckpointAnswers,
     setG11EqIneqScaffoldCheckpointAnswers,
     g11EqIneqScaffoldCheckpointFeedback,
     setG11EqIneqScaffoldCheckpointFeedback,
     g11EqIneqScaffoldAnswer,
     setG11EqIneqScaffoldAnswer,
     g11EqIneqScaffoldFeedback,
     setG11EqIneqScaffoldFeedback,
     g11EqIneqScaffoldShowHint,
     setG11EqIneqScaffoldShowHint,
     renderGrade11EqIneqVisualAids,
 }) => {
     const question = g11EqIneqScaffoldQuestion;
     const checkpoints = Array.isArray(question?.checkpoints) ? question.checkpoints : [];
     const cpIndex = Math.max(0, Math.min(checkpoints.length - 1, Number(g11EqIneqScaffoldCheckpointIndex) || 0));
     const currentCheckpoint = checkpoints[cpIndex];
 
     const checkAnswer = () => {
         if (!question) return;
         const expected = normalizeEqIneq(question.correct_answer);
         const got = normalizeEqIneq(g11EqIneqScaffoldAnswer);
 
         if (expected && got === expected) {
             setG11EqIneqScaffoldFeedback({ kind: 'success', message: 'Correct.' });
         } else {
             setG11EqIneqScaffoldFeedback({ kind: 'error', message: `Not quite. Expected: ${question.correct_answer}` });
         }
     };
 
     const checkCheckpoint = () => {
         if (!question || !currentCheckpoint) return;
 
         const cpId = currentCheckpoint.id;
         const userValue = g11EqIneqScaffoldCheckpointAnswers?.[cpId] ?? '';
         const expected = normalizeEqIneq(currentCheckpoint.correct_answer);
         const got = normalizeEqIneq(userValue);
 
         const ok = expected && got === expected;
 
         setG11EqIneqScaffoldCheckpointFeedback((prev) => ({
             ...(prev || {}),
             [cpId]: ok
                 ? { kind: 'success', message: 'Correct.' }
                 : { kind: 'error', message: `Not quite. Expected: ${currentCheckpoint.correct_answer}` },
         }));
     };
 
     const goNextCheckpoint = () => {
         if (!question || !currentCheckpoint) return;
         const cpId = currentCheckpoint.id;
         const fb = g11EqIneqScaffoldCheckpointFeedback?.[cpId];
         if (!fb || fb.kind !== 'success') return;
 
         if (cpIndex >= checkpoints.length - 1) {
             setG11EqIneqScaffoldCheckpointIndex(checkpoints.length);
         } else {
             setG11EqIneqScaffoldCheckpointIndex(cpIndex + 1);
         }
     };
 
     const setCheckpointAnswer = (cpId, value) => {
         setG11EqIneqScaffoldCheckpointAnswers((prev) => ({ ...(prev || {}), [cpId]: value }));
         setG11EqIneqScaffoldCheckpointFeedback((prev) => ({ ...(prev || {}), [cpId]: null }));
     };
 
     const newExample = () => {
         const step = scaffoldSteps[g11EqIneqScaffoldStepIndex] || scaffoldSteps[0];
         fetchGrade11EqIneqScaffoldQuestion({ subskill: step.key, difficulty: g11EqIneqScaffoldDifficulty });
     };
 
     const isDone = question?.question_type === 'scaffold' && checkpoints.length > 0
         ? (Number(g11EqIneqScaffoldCheckpointIndex) || 0) >= checkpoints.length
         : false;
 
     return (
         <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
             <div className="flex gap-4">
                 <div className="flex-1 bg-white p-6 rounded-xl shadow-xl">
                     <div className="flex items-center justify-between mb-6">
                         <div>
                             <h2 className="text-2xl font-bold text-gray-900">Grade 11 Mathematics • Equations &amp; inequalities • Scaffold</h2>
                             <p className="text-sm text-gray-600">Step-by-step practice with checkpoints.</p>
                         </div>
                         <div className="flex items-center gap-2">
                             {!g11EqIneqVisualAidsOpen && (
                                 <button
                                     onClick={() => setG11EqIneqVisualAidsOpen(true)}
                                     className="px-4 py-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-800 rounded-lg font-semibold border border-indigo-200"
                                 >
                                     Visual Aids
                                 </button>
                             )}
                             <button
                                 onClick={onBack}
                                 className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-medium"
                             >
                                 Back
                             </button>
                         </div>
                     </div>
 
                     <div className="flex flex-col md:flex-row gap-3 md:items-end md:justify-between mb-6">
                         <div className="w-full md:w-64">
                             <label className="block text-sm font-semibold text-gray-700 mb-1">Difficulty</label>
                             <select
                                 value={g11EqIneqScaffoldDifficulty}
                                 onChange={(e) => setG11EqIneqScaffoldDifficulty(e.target.value)}
                                 className="w-full px-3 py-2 border border-gray-300 rounded-md"
                             >
                                 <option value="easy">Easy</option>
                                 <option value="medium">Medium</option>
                                 <option value="hard">Hard</option>
                             </select>
                         </div>
                         <div className="w-full md:w-72">
                             <label className="block text-sm font-semibold text-gray-700 mb-1">Subskill</label>
                             <select
                                 value={g11EqIneqScaffoldStepIndex}
                                 onChange={(e) => {
                                     const idx = Number(e.target.value);
                                     setG11EqIneqScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                     setG11EqIneqScaffoldFeedback(null);
                                     setG11EqIneqScaffoldShowHint(false);
                                     setG11EqIneqScaffoldCheckpointIndex(0);
                                     setG11EqIneqScaffoldCheckpointAnswers({});
                                     setG11EqIneqScaffoldCheckpointFeedback({});
                                     setG11EqIneqScaffoldAnswer('');
                                 }}
                                 className="w-full px-3 py-2 border border-gray-300 rounded-md"
                             >
                                 {scaffoldSteps.map((s, idx) => (
                                     <option key={s.key} value={idx}>{s.title}</option>
                                 ))}
                             </select>
                         </div>
                         <div className="flex gap-2">
                             <button
                                 onClick={newExample}
                                 disabled={g11EqIneqScaffoldLoading}
                                 className="px-4 py-2 bg-blue-600 text-white rounded-lg font-semibold hover:bg-blue-700 disabled:bg-gray-400"
                             >
                                 {g11EqIneqScaffoldLoading ? 'Loading…' : 'New Example'}
                             </button>
                         </div>
                     </div>
 
                     {g11EqIneqScaffoldError && (
                         <div className="mb-6 p-4 rounded-lg border border-red-200 bg-red-50 text-red-800 text-sm">{g11EqIneqScaffoldError}</div>
                     )}
 
                     <div className="bg-gray-50 p-6 rounded-xl border border-gray-200">
                         {g11EqIneqScaffoldLoading && !question ? (
                             <div className="text-gray-600">Loading question…</div>
                         ) : question ? (
                             <>
                                 <div className="text-gray-900 font-semibold mb-3">Try this:</div>
                                 <div className="text-gray-800 font-medium mb-4">{renderMathText(question.question)}</div>
 
                                 {question.question_type === 'scaffold' && checkpoints.length > 0 ? (
                                     isDone ? (
                                         <div className="bg-white border border-gray-200 rounded-lg p-4">
                                             <div className="text-gray-900 font-semibold">Finished</div>
                                             {question.explanation && (
                                                 <div className="mt-3 text-sm text-gray-700 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                     {renderMathText(question.explanation)}
                                                 </div>
                                             )}
                                         </div>
                                     ) : (
                                         <div className="bg-white border border-gray-200 rounded-lg p-4">
                                             <div className="text-sm font-semibold text-gray-800 mb-2">Checkpoint {cpIndex + 1} / {checkpoints.length}</div>
                                             <div className="text-gray-800 font-medium mb-3">{renderMathText(currentCheckpoint?.prompt || '')}</div>
 
                                             <input
                                                 type="text"
                                                 value={g11EqIneqScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? ''}
                                                 onChange={(e) => setCheckpointAnswer(currentCheckpoint?.id, e.target.value)}
                                                 className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                                 placeholder="Type your answer"
                                             />
 
                                             <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                                 <button
                                                     onClick={checkCheckpoint}
                                                     disabled={String(g11EqIneqScaffoldCheckpointAnswers?.[currentCheckpoint?.id] ?? '').trim() === ''}
                                                     className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                                 >
                                                     Check
                                                 </button>
                                                 <button
                                                     onClick={goNextCheckpoint}
                                                     className="px-4 py-2 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-medium"
                                                 >
                                                     Next
                                                 </button>
 
                                                 {g11EqIneqScaffoldCheckpointFeedback?.[currentCheckpoint?.id] && (
                                                     <div
                                                         className={`text-sm px-3 py-2 rounded-lg border ${
                                                             g11EqIneqScaffoldCheckpointFeedback?.[currentCheckpoint?.id]?.kind === 'success'
                                                                 ? 'bg-green-50 text-green-800 border-green-200'
                                                                 : 'bg-red-50 text-red-800 border-red-200'
                                                         }`}
                                                     >
                                                         {g11EqIneqScaffoldCheckpointFeedback?.[currentCheckpoint?.id]?.message}
                                                     </div>
                                                 )}
                                             </div>
                                         </div>
                                     )
                                 ) : (
                                     <div className="bg-white border border-gray-200 rounded-lg p-4">
                                         <div className="text-gray-800 font-medium mb-3">Your answer:</div>
                                         <input
                                             type="text"
                                             value={g11EqIneqScaffoldAnswer}
                                             onChange={(e) => {
                                                 setG11EqIneqScaffoldAnswer(e.target.value);
                                                 setG11EqIneqScaffoldFeedback(null);
                                             }}
                                             className="w-full px-3 py-2 border border-gray-300 rounded-md"
                                             placeholder="Type your answer"
                                         />
                                         <div className="mt-3 flex flex-col sm:flex-row gap-2 sm:items-center">
                                             <button
                                                 onClick={checkAnswer}
                                                 disabled={String(g11EqIneqScaffoldAnswer || '').trim() === ''}
                                                 className="px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700 disabled:bg-gray-400"
                                             >
                                                 Check
                                             </button>
                                             {g11EqIneqScaffoldFeedback && (
                                                 <div
                                                     className={`text-sm px-3 py-2 rounded-lg border ${
                                                         g11EqIneqScaffoldFeedback.kind === 'success'
                                                             ? 'bg-green-50 text-green-800 border-green-200'
                                                             : 'bg-red-50 text-red-800 border-red-200'
                                                     }`}
                                                 >
                                                     {g11EqIneqScaffoldFeedback.message}
                                                 </div>
                                             )}
                                         </div>
 
                                         {question.explanation && (
                                             <div className="mt-4 text-sm text-gray-700">
                                                 <button
                                                     onClick={() => setG11EqIneqScaffoldShowHint(!g11EqIneqScaffoldShowHint)}
                                                     className="text-indigo-700 font-semibold hover:underline"
                                                 >
                                                     {g11EqIneqScaffoldShowHint ? 'Hide hint' : 'Show hint'}
                                                 </button>
                                                 {g11EqIneqScaffoldShowHint && (
                                                     <div className="mt-2 bg-gray-50 border border-gray-200 rounded-lg p-3">
                                                         {renderMathText(question.explanation)}
                                                     </div>
                                                 )}
                                             </div>
                                         )}
                                     </div>
                                 )}
                             </>
                         ) : (
                             <div className="text-gray-600">Choose a subskill and click “New Example”.</div>
                         )}
                     </div>
                 </div>
 
                 <VisualAidsPanel isOpen={g11EqIneqVisualAidsOpen} setIsOpen={setG11EqIneqVisualAidsOpen}>
                     {renderGrade11EqIneqVisualAids?.()}
                 </VisualAidsPanel>
             </div>
         </div>
     );
 };
 
 export default Grade11EquationsInequalitiesScaffold;

