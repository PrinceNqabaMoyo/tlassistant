import React from 'react';
import { buildEmptyWordbankAnswer, getWordBank, getUsedTokenIds } from '../utils/accountingHelpers';

const WordbankTableRenderer = ({ question, answer, setAnswer, feedback, isMarkingEnv = false, showMemo = false, showCheckHighlights = false }) => {
    if (!question || question.question_type !== 'table_wordbank') return null;

    const ans = (answer && typeof answer === 'object') ? answer : buildEmptyWordbankAnswer(question);
    const wordBank = getWordBank(question);
    const correctMap = question?.correct_map || {};
    // In memo mode, use correctMap for display instead of user selections
    const effectiveSelections = showMemo ? correctMap : (ans?.selections || {});
    const used = showMemo ? new Set(Object.values(correctMap).flatMap(v => typeof v === 'object' ? Object.values(v).filter(Boolean) : [v].filter(Boolean))) : getUsedTokenIds(ans);

    const tokenLabelById = {};
    wordBank.forEach((t) => { tokenLabelById[String(t.id)] = t.label; });

    const setActiveTokenId = (tokenId) => {
        if (showMemo) return;
        setAnswer({
            ...(ans || {}),
            activeTokenId: tokenId,
        });
    };

    const clearCell = (rowIndex) => {
        if (showMemo) return;
        const next = {
            ...(ans || {}),
            selections: {
                ...(ans?.selections || {}),
                [String(rowIndex)]: {
                    ...((ans?.selections || {})[String(rowIndex)] || {}),
                    '2': null,
                },
            },
        };
        setAnswer(next);
    };

    const placeActive = (rowIndex) => {
        if (showMemo) return;
        const tokenId = ans?.activeTokenId;
        if (!tokenId) return;
        if (used.has(String(tokenId))) return;

        const next = {
            ...(ans || {}),
            selections: {
                ...(ans?.selections || {}),
                [String(rowIndex)]: {
                    ...((ans?.selections || {})[String(rowIndex)] || {}),
                    '2': String(tokenId),
                },
            },
            activeTokenId: null,
        };
        setAnswer(next);
    };

    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];

    return (
        <div className="space-y-4">
            {!showMemo && (
                <div className="mb-3">
                    <div className="text-sm font-semibold text-gray-900 mb-2">Word bank</div>
                    <div className="flex flex-wrap gap-2">
                        {wordBank.map((t) => {
                            const isUsed = used.has(String(t.id));
                            const isActive = String(ans?.activeTokenId) === String(t.id);
                            return (
                                <button
                                    key={t.id}
                                    type="button"
                                    disabled={isUsed}
                                    onClick={() => setActiveTokenId(String(t.id))}
                                    className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-gray-100 text-gray-400 border-gray-200' :
                                        isActive ? 'bg-indigo-600 text-white border-indigo-600' :
                                            'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'
                                        }`}
                                >
                                    {t.label}
                                </button>
                            );
                        })}
                    </div>
                    <div className="text-xs text-gray-600 mt-2">Click a word, then click a row's "Term" cell to place it.</div>
                </div>
            )}

            <div className="overflow-x-auto">
                <table style={{ width: '100%', borderCollapse: 'collapse', tableLayout: 'fixed' }}>
                    <thead>
                        <tr>
                            {headers.map((h, i) => (
                                <th key={i} style={{ border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', fontSize: '0.75rem' }}>{h}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {rows.map((row, rowIndex) => {
                            const selectedId = effectiveSelections?.[String(rowIndex)]?.['2'];
                            const label = selectedId ? tokenLabelById[String(selectedId)] : '';
                            const expectedId = correctMap?.[String(rowIndex)]?.['2'];
                            const isCorrectCell = showMemo && selectedId && String(selectedId) === String(expectedId);
                            const isIncorrectCell = showCheckHighlights && selectedId && String(selectedId) !== String(expectedId);

                            let cellBg = 'bg-white';
                            let cellBorder = 'border-gray-200';
                            if (isCorrectCell) { cellBg = 'bg-emerald-50'; cellBorder = 'border-emerald-400'; }
                            if (isIncorrectCell) { cellBg = 'bg-red-50'; cellBorder = 'border-red-400'; }

                            return (
                                <tr key={rowIndex}>
                                    {/* Concept */}
                                    <td style={{ border: '1px solid #000', padding: '6px', fontSize: '0.875rem', whiteSpace: 'nowrap' }}>{row[0]}</td>
                                    {/* Definition / Scenario */}
                                    <td style={{ border: '1px solid #000', padding: '6px', fontSize: '0.875rem', minWidth: '420px' }}>{row[1]}</td>
                                    {/* Interaction Cell */}
                                    <td style={{ border: '1px solid #000', padding: '6px' }}>
                                        <button
                                            type="button"
                                            onClick={() => placeActive(rowIndex)}
                                            disabled={showMemo}
                                            className={`w-full text-left px-3 py-2 rounded-md border ${cellBg} ${cellBorder} ${showMemo ? 'cursor-default' : 'hover:bg-gray-50'}`}
                                        >
                                            {label ? (
                                                <span className={`font-semibold ${isCorrectCell ? 'text-emerald-800' : isIncorrectCell ? 'text-red-800' : 'text-gray-900'}`}>{label}</span>
                                            ) : (
                                                <span className="text-gray-400">{showMemo ? '—' : 'Click to place...'}</span>
                                            )}
                                        </button>
                                        {!showMemo && (
                                            <div className="mt-1">
                                                <button
                                                    type="button"
                                                    onClick={() => clearCell(rowIndex)}
                                                    className="text-xs font-semibold text-gray-600 hover:text-gray-900"
                                                >
                                                    Clear
                                                </button>
                                            </div>
                                        )}
                                    </td>
                                    {/* Optional 4th column */}
                                    <td style={{ border: '1px solid #000', padding: '6px', fontSize: '0.875rem' }}>{row[3] || ''}</td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            </div>

            {feedback && (
                <div className={`mt-3 p-3 rounded-lg text-sm ${feedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' :
                    feedback.kind === 'error' ? 'bg-red-50 text-red-800 border border-red-200' :
                        'bg-blue-50 text-blue-800 border border-blue-200'
                    }`}>
                    {feedback.message}
                </div>
            )}
        </div>
    );
};

export default WordbankTableRenderer;
