import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\src\components\workspace\grade11\accounting\Grade11AccountingScaffold.jsx'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Add state for showMemo
content = content.replace(
    'const [showHelpPanel, setShowHelpPanel] = React.useState(false);',
    'const [showHelpPanel, setShowHelpPanel] = React.useState(false);\n    const [showMemo, setShowMemo] = React.useState(false);'
)

# Reset showMemo on new question
content = content.replace(
    'setG11AcctScaffoldShowHint(false);\n            return;',
    'setG11AcctScaffoldShowHint(false);\n            setShowMemo(false);\n            return;'
)

# Replace the actions buttons logic for typed question
content = content.replace(
    '''                                <button
                                    onClick={() => {
                                        setG11AcctScaffoldShowHint(!g11AcctScaffoldShowHint);
                                        if (!g11AcctScaffoldShowHint) setG11AcctScaffoldFeedback(null);
                                    }}
                                    disabled={!question}
                                    className="bg-white text-slate-700 border border-slate-200 px-4 py-2 rounded-xl hover:bg-slate-50 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium"
                                >
                                    {g11AcctScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                </button>
                            </>
                        )}''',
    '''                                <button
                                    onClick={() => {
                                        setG11AcctScaffoldShowHint(!g11AcctScaffoldShowHint);
                                        if (!g11AcctScaffoldShowHint) setG11AcctScaffoldFeedback(null);
                                    }}
                                    disabled={!question}
                                    className="bg-white text-slate-700 border border-slate-200 px-4 py-2 rounded-xl hover:bg-slate-50 transition-colors shadow-sm disabled:opacity-50 disabled:cursor-not-allowed text-sm font-medium"
                                >
                                    {g11AcctScaffoldShowHint ? 'Hide Hint' : 'Show Hint'}
                                </button>
                                {g11AcctScaffoldFeedback && question?.question_type === 'typed' && (
                                    <button
                                        onClick={() => setShowMemo(!showMemo)}
                                        className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-800'}`}
                                    >
                                        {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                    </button>
                                )}
                            </>
                        )}'''
)

# Add the memo display block
content = content.replace(
    '''                    {!isMarkingMode && g11AcctScaffoldShowHint && question && (''',
    '''                    {showMemo && question?.question_type === 'typed' && (
                        <div className="mt-4 p-4 bg-slate-50 border border-slate-200 rounded-xl text-sm text-slate-700">
                            <div className="font-semibold text-slate-900 mb-2">Compare / Memo</div>
                            <div className="whitespace-pre-wrap">
                                {renderQuestion?.sample_answer || renderQuestion?.guidelines?.[0] || 'No sample answer provided.'}
                            </div>
                        </div>
                    )}

                    {!isMarkingMode && g11AcctScaffoldShowHint && question && ('''
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Patched Grade11AccountingScaffold.jsx')
