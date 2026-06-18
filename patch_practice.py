import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade11\accounting\Grade11AccountingPractice.jsx'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add state for memoOpenById
content = content.replace(
    'const questions = Array.isArray(g11AcctPracticeQuestions) ? g11AcctPracticeQuestions : [];',
    'const questions = Array.isArray(g11AcctPracticeQuestions) ? g11AcctPracticeQuestions : [];\n    const [memoOpenById, setMemoOpenById] = React.useState({});'
)

# For bundles, replace check button area:
content = content.replace(
    '''                                                {!isMarkingMode && (
                                                    <div className="mt-3">
                                                        <button
                                                            onClick={() => checkBundlePart(currentIndex, pIdx)}
                                                            className="px-3 py-1.5 bg-emerald-600 text-white rounded-lg text-sm font-semibold hover:bg-emerald-700"
                                                        >
                                                            Check Part
                                                        </button>
                                                    </div>
                                                )}''',
    '''                                                {!isMarkingMode && (
                                                    <div className="mt-3 flex items-center gap-3">
                                                        <button
                                                            onClick={() => checkBundlePart(currentIndex, pIdx)}
                                                            className="px-3 py-1.5 bg-emerald-600 text-white rounded-lg text-sm font-semibold hover:bg-emerald-700"
                                                        >
                                                            Check Part
                                                        </button>
                                                        {fb && part.question_type === 'typed' && (
                                                            <button
                                                                onClick={() => setMemoOpenById(prev => ({ ...prev, [part.id]: !prev[part.id] }))}
                                                                className={`px-3 py-1.5 rounded-lg text-sm font-semibold transition-all border ${memoOpenById[part.id] ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-800'}`}
                                                            >
                                                                {memoOpenById[part.id] ? 'Hide Memo' : 'Compare / Memo'}
                                                            </button>
                                                        )}
                                                    </div>
                                                )}
                                                {memoOpenById[part.id] && part.question_type === 'typed' && (
                                                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                                        <div className="font-semibold text-slate-900 mb-2">Compare / Memo</div>
                                                        <div className="whitespace-pre-wrap">
                                                            {part.sample_answer || part.guidelines?.[0] || 'No sample answer provided.'}
                                                        </div>
                                                    </div>
                                                )}'''
)

# For single questions, replace check button area:
content = content.replace(
    '''                                <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                                    {marking.isPracticeMode ? (
                                        <button
                                            onClick={() => checkOne(currentIndex)}
                                            className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors"
                                        >
                                            Check Answer
                                        </button>
                                    ) : (''',
    '''                                {memoOpenById[q.id] && q.question_type === 'typed' && (
                                    <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                                        <div className="font-semibold text-slate-900 mb-2">Compare / Memo</div>
                                        <div className="whitespace-pre-wrap">
                                            {q.sample_answer || q.guidelines?.[0] || 'No sample answer provided.'}
                                        </div>
                                    </div>
                                )}
                                <div className="mt-8 flex justify-end gap-3 pt-4 border-t border-slate-100">
                                    {marking.isPracticeMode ? (
                                        <>
                                            {displayFeedback && q.question_type === 'typed' && (
                                                <button
                                                    onClick={() => setMemoOpenById(prev => ({ ...prev, [q.id]: !prev[q.id] }))}
                                                    className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all border ${memoOpenById[q.id] ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-800'}`}
                                                >
                                                    {memoOpenById[q.id] ? 'Hide Memo' : 'Compare / Memo'}
                                                </button>
                                            )}
                                            <button
                                                onClick={() => checkOne(currentIndex)}
                                                className="px-6 py-2 bg-indigo-50 text-indigo-700 rounded-xl font-semibold hover:bg-indigo-100 transition-colors"
                                            >
                                                Check Answer
                                            </button>
                                        </>
                                    ) : ('''
)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched Grade11AccountingPractice.jsx')
