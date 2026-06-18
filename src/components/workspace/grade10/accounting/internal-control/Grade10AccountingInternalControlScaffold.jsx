import React, { useMemo, useEffect, useRef, useState } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const clampHintPosition = (x, y, width = 320, height = 240) => {
    if (typeof window === 'undefined') return { x, y };
    const margin = 12;
    const maxX = Math.max(margin, window.innerWidth - width - margin);
    const maxY = Math.max(margin, window.innerHeight - height - margin);
    return {
        x: Math.min(Math.max(margin, Number(x) || margin), maxX),
        y: Math.min(Math.max(margin, Number(y) || margin), maxY),
    };
};

const buildHintSections = (teachingHint, fallbackText) => {
    const sections = [];
    if (teachingHint && typeof teachingHint === 'object') {
        const labels = [
            ['role_in_requirement', 'What this cell is asking'],
            ['evidence_from_question', 'Where to look in the question'],
            ['rule_or_principle', 'Rule / principle'],
            ['how_to_derive', 'How to derive it'],
            ['transfer_tip', 'Use this in similar questions'],
        ];
        labels.forEach(([key, title]) => {
            const text = String(teachingHint[key] || '').trim();
            if (text) sections.push({ title, text });
        });
    }
    if (!sections.length) {
        const text = String(fallbackText || '').trim();
        if (text) sections.push({ title: 'Hint', text });
    }
    return sections;
};

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];

const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const buildEmptyWordbankAnswer = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const selections = {};
    for (let i = 0; i < rows.length; i += 1) {
        selections[String(i)] = { '2': null };
    }
    return { selections, activeTokenId: null };
};

const getUsedTokenIds = (ans) => {
    const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};
    const used = new Set();
    Object.values(selections).forEach((row) => {
        if (!row) return;
        const v = row['2'];
        if (v) used.add(String(v));
    });
    return used;
};

const Grade10AccountingInternalControlScaffold = ({
    onBack,
    scaffoldSteps,
    g10AcctICVisualAidsOpen,
    setG10AcctICVisualAidsOpen,
    g10AcctICScaffoldDifficulty,
    setG10AcctICScaffoldDifficulty,
    g10AcctICScaffoldStepIndex,
    setG10AcctICScaffoldStepIndex,
    fetchGrade10AcctICScaffoldQuestion,
    g10AcctICScaffoldLoading,
    g10AcctICScaffoldError,
    g10AcctICScaffoldQuestion,
    g10AcctICScaffoldAnswer,
    setG10AcctICScaffoldAnswer,
    g10AcctICScaffoldFeedback,
    setG10AcctICScaffoldFeedback,
    g10AcctICScaffoldShowHint,
    setG10AcctICScaffoldShowHint,
    renderGrade10AcctICVisualAids,
    hideConfig,
}) => {
    const question = g10AcctICScaffoldQuestion;
    const selectedSubtopic = scaffoldSteps[g10AcctICScaffoldStepIndex] || scaffoldSteps[0];
    const marking = useGrade10AccountingMarking();

    const tableRef = useRef(null);
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [hintPosition, setHintPosition] = useState({ x: 0, y: 0 });

    const isCompareMode = g10AcctICScaffoldShowHint === 'compare';
    const isHintMode = g10AcctICScaffoldShowHint === 'hint';
    const hasCheckedRef = useRef(false);

    useEffect(() => {
        marking.setMarkingMode('practice');
        hasCheckedRef.current = false;
    }, [g10AcctICScaffoldStepIndex, question?.id, marking]);

    const newExample = () => {
        fetchGrade10AcctICScaffoldQuestion({
            subskill: selectedSubtopic?.key || 'mixed',
            difficulty: g10AcctICScaffoldDifficulty,
        });
    };

    const checkAnswer = () => {
        if (!question) return;
        hasCheckedRef.current = true;

        if (question.question_type === 'mcq') {
            const ok = String(g10AcctICScaffoldAnswer) === String(question.correct_index);
            setG10AcctICScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct!' }
                : { kind: 'error', message: 'Not quite. Check your answer.' });
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctICScaffoldAnswer && typeof g10AcctICScaffoldAnswer === 'object')
                ? g10AcctICScaffoldAnswer
                : buildEmptyWordbankAnswer(question);
            const selections = ans?.selections && typeof ans.selections === 'object' ? ans.selections : {};

            let total = 0;
            let hit = 0;
            Object.keys(correctMap).forEach((rowKey) => {
                const expected = correctMap?.[rowKey]?.['2'];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = selections?.[rowKey]?.['2'];
                if (String(got) === String(expected)) hit += 1;
            });

            const ok = total > 0 && hit === total;
            setG10AcctICScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct! Great job matching.' }
                : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.` });
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(g10AcctICScaffoldAnswer);
            if (!user) {
                setG10AcctICScaffoldFeedback({ kind: 'error', message: 'Write an answer first before checking.' });
                return;
            }
            setG10AcctICScaffoldShowHint('compare');
            setG10AcctICScaffoldFeedback({ kind: 'info', message: 'Compare your answer to the sample memo.' });
            return;
        }

        setG10AcctICScaffoldFeedback({ kind: 'error', message: `Unsupported question type: ${question.question_type}` });
    };

    const setAnswerValue = (value) => {
        setG10AcctICScaffoldAnswer(value);
        if (question) {
            marking.registerAnswer(question.id, value);
        }
        setG10AcctICScaffoldFeedback(null);
        hasCheckedRef.current = false;
        setActiveCellHint(null);
    };

    const handleCellClick = (e, rowKey, colKey, hintContent) => {
        if (!isHintMode) return;
        const rect = e.currentTarget.getBoundingClientRect();
        setHintPosition(clampHintPosition(rect.left + window.scrollX, rect.bottom + window.scrollY + 8));
        setActiveCellHint({ rowKey, colKey, hintContent });
    };

    const renderWordbankTable = (q) => {
        const ans = (g10AcctICScaffoldAnswer && typeof g10AcctICScaffoldAnswer === 'object')
            ? g10AcctICScaffoldAnswer
            : buildEmptyWordbankAnswer(q);

        const wordBank = getWordBank(q);
        const used = getUsedTokenIds(ans);
        const correctMap = getCorrectMap(q);

        const tokenLabelById = {};
        wordBank.forEach((t) => { tokenLabelById[String(t.id)] = t.label; });

        const setActiveTokenId = (tokenId) => {
            setAnswerValue({
                ...(ans || {}),
                activeTokenId: tokenId,
            });
        };

        const clearCell = (rowIndex) => {
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
            setAnswerValue(next);
        };

        const placeActive = (rowIndex) => {
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
            setAnswerValue(next);
        };

        const rows = Array.isArray(q?.table?.rows) ? q.table.rows : [];
        const headers = Array.isArray(q?.table?.headers) ? q.table.headers : [];

        return (
            <div className="mt-3 relative" ref={tableRef}>
                <div className="mb-4">
                    <div className="text-sm font-semibold text-slate-800 mb-2">Word bank (Click to select, then click a slot to place)</div>
                    <div className="flex flex-wrap gap-2">
                        {wordBank.map((t) => {
                            const isUsed = used.has(String(t.id));
                            const isActive = String(ans?.activeTokenId) === String(t.id);
                            return (
                                <button
                                    key={t.id}
                                    type="button"
                                    disabled={isUsed || isCompareMode || !marking.isPracticeMode}
                                    onClick={() => setActiveTokenId(String(t.id))}
                                    className={`px-3 py-1.5 rounded-lg text-sm font-semibold border transition-all ${isUsed ? 'bg-slate-100 text-slate-400 border-slate-200 opacity-50' : isActive ? 'bg-indigo-600 text-white border-indigo-600 shadow-md ring-2 ring-indigo-300 ring-offset-1' : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-50 hover:border-slate-400 shadow-sm'}`}
                                >
                                    {t.label}
                                </button>
                            );
                        })}
                    </div>
                </div>

                <div className="overflow-x-auto bg-white rounded-xl border border-slate-200 shadow-sm">
                    <table className="min-w-full text-sm">
                        <thead className="bg-slate-50 border-b border-slate-200">
                            <tr>
                                {headers.map((h, i) => (
                                    <th key={i} className="px-4 py-3 text-left font-semibold text-slate-800">{h}</th>
                                ))}
                                <th className="px-4 py-3 text-left font-semibold text-slate-800 w-[240px] sm:w-[320px]">Your match</th>
                            </tr>
                        </thead>
                        <tbody className="divide-y divide-slate-100">
                            {rows.map((row, rowIndex) => {
                                const selectedId = ans?.selections?.[String(rowIndex)]?.['2'];
                                const expectedId = correctMap?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';

                                const isChecked = hasCheckedRef.current;
                                const isRowCorrect = isChecked && String(selectedId) === String(expectedId);
                                const isRowIncorrect = isChecked && selectedId && String(selectedId) !== String(expectedId);

                                const hintContent = q.guidelines?.[0] || 'Consider what control area this specific action addresses.';
                                const isHintActive = isHintMode && activeCellHint?.rowKey === String(rowIndex);

                                let cellClass = 'bg-white border-slate-200 hover:bg-slate-50 text-slate-400 border-dashed';
                                if (isCompareMode) {
                                    cellClass = 'bg-slate-50 border-slate-200 cursor-default';
                                } else if (isRowCorrect) {
                                    cellClass = 'bg-emerald-50 border-emerald-300 ring-1 ring-emerald-200';
                                } else if (isRowIncorrect) {
                                    cellClass = 'bg-red-50 border-red-300 ring-1 ring-red-200';
                                } else if (label) {
                                    cellClass = 'bg-indigo-50 border-indigo-200 shadow-inner text-indigo-900';
                                }

                                if (isHintMode) {
                                    cellClass = isHintActive ? 'bg-amber-100 border-amber-400 ring-2 ring-amber-400 cursor-help' : 'bg-white border-slate-200 cursor-help hover:bg-amber-50';
                                }

                                return (
                                    <tr key={rowIndex} className={`transition-colors ${rowIndex % 2 === 0 ? 'bg-white' : 'bg-slate-50/50'} hover:bg-indigo-50/30`}>
                                        <td className="px-4 py-3 align-top font-medium text-slate-700">{row[0]}</td>
                                        <td className="px-4 py-3 align-top text-slate-600">{row[1] || ''}</td>
                                        <td className="px-4 py-3 align-top relative">
                                            <div className="flex gap-2">
                                                <div className="flex-1">
                                                    <button
                                                        type="button"
                                                        onClick={(e) => {
                                                            if (isHintMode) handleCellClick(e, String(rowIndex), '2', hintContent);
                                                            else if (!isCompareMode) placeActive(rowIndex);
                                                        }}
                                                        disabled={isCompareMode || (!isHintMode && !marking.isPracticeMode)}
                                                        className={`w-full text-left px-3 py-2.5 rounded-lg border transition-all ${cellClass} ${isCompareMode ? 'cursor-default' : ''}`}
                                                    >
                                                        {isCompareMode ? (
                                                            <span className="font-semibold text-emerald-800">{tokenLabelById[String(expectedId)] || ''}</span>
                                                        ) : label ? (
                                                            <span className={`font-semibold ${isRowCorrect ? 'text-emerald-800' : isRowIncorrect ? 'text-red-800' : ''}`}>{label}</span>
                                                        ) : (
                                                            <span>{isHintMode ? 'Click for hint' : 'Click to place...'}</span>
                                                        )}
                                                    </button>
                                                    {label && !isCompareMode && !isHintMode && marking.isPracticeMode && !isRowCorrect && (
                                                        <div className="mt-1.5 flex justify-end">
                                                            <button
                                                                type="button"
                                                                onClick={() => clearCell(rowIndex)}
                                                                className="text-xs font-semibold text-slate-500 hover:text-red-600 transition-colors px-2 py-0.5 rounded hover:bg-red-50"
                                                            >
                                                                Clear
                                                            </button>
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>

                {activeCellHint && isHintMode && (
                    <div
                        style={{ position: 'fixed', left: hintPosition.x, top: hintPosition.y, zIndex: 1000 }}
                        className="bg-white border-2 border-amber-300 shadow-xl rounded-xl p-4 w-72 pointer-events-none"
                    >
                        <div className="flex items-center gap-2 mb-2 text-amber-700">
                            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <span className="font-bold text-sm">Hint</span>
                        </div>
                        <div className="text-sm text-slate-700">{activeCellHint.hintContent}</div>
                    </div>
                )}
            </div>
        );
    };

    const renderQuestion = () => {
        if (!question) return null;

        if (question.question_type === 'mcq') {
            return (
                <div className="mt-4">
                    <div className="grid grid-cols-1 gap-3">
                        {(question.options || []).map((opt, idx) => {
                            const isSelected = String(g10AcctICScaffoldAnswer) === String(idx);
                            const isCorrect = isCompareMode && String(idx) === String(question.correct_index);
                            const isWrongSelected = hasCheckedRef.current && isSelected && String(idx) !== String(question.correct_index);

                            let stateClass = 'hover:border-indigo-300 hover:bg-indigo-50/30';
                            if (isCompareMode) {
                                stateClass = isCorrect ? 'bg-emerald-50 border-emerald-400 ring-1 ring-emerald-400 shadow-sm cursor-default' :
                                             'bg-slate-50 border-slate-200 opacity-70 cursor-default';
                            } else if (isWrongSelected) {
                                stateClass = 'bg-red-50 border-red-300 ring-1 ring-red-300';
                            } else if (isSelected) {
                                stateClass = 'border-indigo-500 ring-1 ring-indigo-500 bg-indigo-50/50 shadow-sm';
                            }

                            return (
                                <button
                                    key={idx}
                                    disabled={isCompareMode || !marking.isPracticeMode}
                                    onClick={() => setAnswerValue(String(idx))}
                                    className={`w-full text-left p-4 rounded-xl border-2 transition-all flex items-start gap-3 ${stateClass}`}
                                >
                                    <div className={`w-5 h-5 rounded-full border flex-shrink-0 mt-0.5 flex items-center justify-center transition-colors ${isCorrect ? 'border-emerald-500 bg-emerald-500' : isWrongSelected ? 'border-red-500 bg-red-500' : isSelected ? 'border-indigo-600 bg-indigo-600' : 'border-slate-300 bg-white'}`}>
                                        {(isCorrect || isSelected) && !isWrongSelected && <div className="w-2 h-2 rounded-full bg-white" />}
                                        {isWrongSelected && (
                                            <svg className="w-3 h-3 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M6 18L18 6M6 6l12 12" />
                                            </svg>
                                        )}
                                    </div>
                                    <span className={`font-medium ${isCorrect ? 'text-emerald-900' : isWrongSelected ? 'text-red-900' : isSelected ? 'text-indigo-900' : 'text-slate-700'}`}>
                                        {opt}
                                    </span>
                                </button>
                            );
                        })}
                    </div>
                    {isCompareMode && question.explanation && (
                        <div className="mt-4 p-4 bg-emerald-50 border border-emerald-200 rounded-xl text-sm text-emerald-900">
                            <span className="font-bold">Explanation: </span>{question.explanation}
                        </div>
                    )}
                </div>
            );
        }

        if (question.question_type === 'typed') {
            return (
                <div className="mt-4">
                    <textarea
                        value={typeof g10AcctICScaffoldAnswer === 'string' ? g10AcctICScaffoldAnswer : ''}
                        onChange={(e) => setAnswerValue(e.target.value)}
                        disabled={isCompareMode || !marking.isPracticeMode}
                        placeholder={isCompareMode ? '' : 'Type your answer here...'}
                        className={`w-full min-h-[140px] p-4 border-2 rounded-xl text-slate-700 focus:outline-none transition-all ${isCompareMode ? 'bg-slate-50 border-slate-200 cursor-default' : 'border-slate-200 focus:border-indigo-400 focus:ring-4 focus:ring-indigo-50 bg-white'}`}
                    />
                    {isCompareMode && question.sample_answer && marking.isPracticeMode && (
                        <div className="mt-4 p-5 bg-indigo-50 border border-indigo-200 rounded-xl shadow-sm">
                            <h4 className="text-sm font-bold text-indigo-900 mb-2 flex items-center gap-2">
                                <svg className="w-4 h-4 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                                </svg>
                                Correct Memo Answer
                            </h4>
                            <div className="text-sm text-indigo-800 mt-1 whitespace-pre-wrap leading-relaxed">{question.sample_answer}</div>
                            {Array.isArray(question.guidelines) && question.guidelines.length > 0 && (
                                <div className="mt-3 pt-3 border-t border-indigo-100">
                                    <div className="font-semibold text-indigo-900 text-sm mb-1">Key points:</div>
                                    <ul className="list-disc pl-5 space-y-1">
                                        {question.guidelines.map((g, gi) => <li key={gi} className="text-sm text-indigo-800">{g}</li>)}
                                    </ul>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            );
        }

        if (question.question_type === 'table_wordbank') {
            return renderWordbankTable(question);
        }

        return (
            <div className="mt-4 text-sm text-red-700 break-words">
                Unsupported question type: {String(question.question_type)}
            </div>
        );
    };

    const hasInput = useMemo(() => {
        if (!question) return false;
        const ans = g10AcctICScaffoldAnswer;
        if (question.question_type === 'mcq') return ans !== null && ans !== undefined && String(ans).trim() !== '';
        if (question.question_type === 'typed') return String(ans || '').trim().length > 0;
        if (question.question_type === 'table_wordbank') {
            const wbAns = g10AcctICScaffoldAnswer;
            return (wbAns && wbAns.selections) ? Object.values(wbAns.selections).some(row => row && Object.values(row).some(v => v !== null && v !== undefined)) : false;
        }
        if (question.question_type === 'table') {
            return (ans && ans.rows) ? ans.rows.some(r => (r || []).some(c => String(c || '').trim().length > 0)) : false;
        }
        if (question.question_type === 'calc') {
            return ans && Object.values(ans).some(val => String(val || '').trim().length > 0);
        }
        return false;
    }, [question, g10AcctICScaffoldAnswer]);

    return (
        <div className="w-full relative">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6">
                <div className="flex items-center gap-3">
                    {onBack && (
                        <button
                            onClick={onBack}
                            className="p-2 -ml-2 text-slate-400 hover:text-slate-600 rounded-lg hover:bg-slate-100 transition-colors"
                            title="Back to topics"
                        >
                            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                            </svg>
                        </button>
                    )}
                    <h3 className="text-xl font-bold text-slate-800">Scaffold Mode</h3>
                </div>

                <div className="flex flex-wrap items-center gap-2">
                    {question && !hideConfig && (
                        <div className="flex items-center gap-3 bg-white px-3 py-1.5 rounded-lg border border-slate-200 shadow-sm">
                            <span className="text-sm font-medium text-slate-600">Mode:</span>
                            <button
                                onClick={marking.toggleMarkingMode}
                                disabled={marking.isSubmitting}
                                className={`relative inline-flex h-5 w-9 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-1 ${!marking.isPracticeMode ? 'bg-indigo-600' : 'bg-slate-300'}`}
                            >
                                <span className={`inline-block h-3.5 w-3.5 transform rounded-full bg-white transition-transform ${!marking.isPracticeMode ? 'translate-x-4.5' : 'translate-x-1'}`} />
                            </button>
                            <span className={`text-sm font-semibold ${!marking.isPracticeMode ? 'text-indigo-700' : 'text-slate-700'}`}>
                                {!marking.isPracticeMode ? 'Marking' : 'Practice'}
                            </span>
                        </div>
                    )}
                    {!hideConfig && (
                        <div className="flex items-center gap-2">
                            <select
                                value={g10AcctICScaffoldDifficulty}
                                onChange={(e) => setG10AcctICScaffoldDifficulty(e.target.value)}
                                className="text-sm border border-slate-300 rounded-lg px-2 py-1.5 bg-white text-slate-700 font-medium focus:ring-2 focus:ring-indigo-500 outline-none"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                            <button
                                onClick={() => setG10AcctICVisualAidsOpen(!g10AcctICVisualAidsOpen)}
                                className={`px-3 py-1.5 text-sm font-semibold rounded-lg border transition-colors ${g10AcctICVisualAidsOpen ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50'}`}
                            >
                                Visual Aids
                            </button>
                        </div>
                    )}
                </div>
            </div>

            <div className="flex flex-col lg:flex-row gap-6 items-start">
                <div className={`flex-1 min-w-0 transition-all duration-300 ${g10AcctICVisualAidsOpen ? 'lg:w-2/3' : 'w-full'}`}>
                    
                    {marking.markingError && (
                        <div className="mb-4 p-4 bg-red-50 border-l-4 border-red-500 text-red-800 rounded-r-lg flex items-start gap-3 break-words">
                            <svg className="w-5 h-5 text-red-500 mt-0.5 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                            </svg>
                            <div>
                                <h4 className="font-semibold">Marking Error</h4>
                                <p className="text-sm mt-1">{marking.markingError}</p>
                            </div>
                        </div>
                    )}

                    {/* Step Navigation */}
                    <div className="bg-white p-2 rounded-xl border border-slate-200 shadow-sm flex flex-wrap gap-1 mb-6">
                        {scaffoldSteps.map((step, idx) => {
                            const isSelected = idx === g10AcctICScaffoldStepIndex;
                            return (
                                <button
                                    key={step.key}
                                    onClick={() => setG10AcctICScaffoldStepIndex(idx)}
                                    className={`px-4 py-2 text-sm font-semibold rounded-lg transition-all ${isSelected ? 'bg-indigo-600 text-white shadow-md' : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'}`}
                                >
                                    {step.title}
                                </button>
                            );
                        })}
                    </div>

                    <div className="flex justify-between items-center mb-4">
                        <h4 className="text-lg font-bold text-slate-800 flex items-center gap-2">
                            <span className="w-8 h-8 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-sm">
                                {g10AcctICScaffoldStepIndex + 1}
                            </span>
                            {selectedSubtopic?.title}
                        </h4>
                        <button
                            onClick={newExample}
                            className="px-4 py-2 bg-white border border-slate-200 text-slate-700 font-semibold rounded-lg hover:bg-slate-50 transition-colors shadow-sm flex items-center gap-2 text-sm"
                        >
                            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                            </svg>
                            Generate new example
                        </button>
                    </div>

                    {g10AcctICScaffoldLoading && (
                        <div className="flex flex-col items-center justify-center py-12 text-slate-400 bg-white rounded-2xl border border-slate-200">
                            <svg className="animate-spin h-8 w-8 mb-4 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                            </svg>
                            <p className="font-medium">Loading question...</p>
                        </div>
                    )}
                    {g10AcctICScaffoldError && (
                        <div className="p-4 bg-red-50 text-red-700 rounded-xl border border-red-100 break-words">
                            {g10AcctICScaffoldError}
                        </div>
                    )}

                    {question && !g10AcctICScaffoldLoading && (
                        <div className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
                            {renderQuestion()}

                            {/* Hint Display Area */}
                            {isHintMode && !activeCellHint && (
                                <div className="mt-6 p-5 bg-amber-50 border border-amber-200 rounded-xl shadow-sm relative overflow-hidden">
                                    <div className="absolute top-0 left-0 w-1 h-full bg-amber-400"></div>
                                    <h4 className="text-sm font-bold text-amber-900 mb-3 flex items-center gap-2">
                                        <svg className="w-5 h-5 text-amber-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                        </svg>
                                        Helpful Hint
                                    </h4>
                                    <div className="space-y-3">
                                        {buildHintSections(question.teaching_hint, question.hint_trigger).map((sec, idx) => (
                                            <div key={idx}>
                                                <div className="text-xs font-bold uppercase tracking-wider text-amber-700/80 mb-1">{sec.title}</div>
                                                <div className="text-sm text-amber-900">{sec.text}</div>
                                            </div>
                                        ))}
                                    </div>
                                </div>
                            )}

                            {/* Action Buttons */}
                            <div className="mt-8 flex flex-wrap gap-3 pt-6 border-t border-slate-100">
                                {marking.isPracticeMode ? (
                                    <>
                                        <div className="flex gap-2 bg-slate-100 p-1 rounded-xl">
                                            <button
                                                onClick={() => setG10AcctICScaffoldShowHint(isHintMode ? false : 'hint')}
                                                className={`px-4 py-2 rounded-lg text-sm font-bold transition-all flex items-center gap-2 ${isHintMode ? 'bg-white text-amber-600 shadow-sm' : 'text-slate-600 hover:text-slate-800 hover:bg-slate-200'}`}
                                            >
                                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                                                </svg>
                                                {isHintMode ? 'Hide Hint' : 'Get a Hint'}
                                            </button>
                                            <button
                                                disabled={!hasInput}
                                                onClick={() => setG10AcctICScaffoldShowHint(isCompareMode ? false : 'compare')}
                                                className={`px-4 py-2 rounded-lg text-sm font-bold transition-all flex items-center gap-2 ${isCompareMode ? 'bg-white text-indigo-600 shadow-sm' : 'text-slate-600 hover:text-slate-800 hover:bg-slate-200'} ${!hasInput ? 'opacity-50 cursor-not-allowed' : ''}`}
                                            >
                                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                                                </svg>
                                                {isCompareMode ? 'Hide Memo' : 'Compare to Memo'}
                                            </button>
                                        </div>
                                        <div className="flex-1"></div>
                                        <button
                                            onClick={checkAnswer}
                                            disabled={isCompareMode}
                                            className="px-6 py-2 bg-emerald-600 text-white rounded-xl font-bold hover:bg-emerald-700 transition-all shadow-md shadow-emerald-600/20 disabled:opacity-50 flex items-center gap-2"
                                        >
                                            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                                            </svg>
                                            Check Answer
                                        </button>
                                    </>
                                ) : (
                                    !marking.isMarkingSubmitted && question && (
                                        <button
                                            onClick={() => marking.submitAssessment([question])}
                                            disabled={marking.isSubmitting}
                                            className="ml-auto px-6 py-2.5 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transition-colors disabled:opacity-50 shadow-md flex items-center gap-2"
                                        >
                                            {marking.isSubmitting ? (
                                                <>
                                                    <svg className="animate-spin w-5 h-5 text-white" fill="none" viewBox="0 0 24 24">
                                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
                                                    </svg>
                                                    Submitting...
                                                </>
                                            ) : 'Submit for Marking'}
                                        </button>
                                    )
                                )}
                            </div>

                            {/* Check Feedback */}
                            {g10AcctICScaffoldFeedback && marking.isPracticeMode && !isCompareMode && (
                                <div className={`mt-5 p-4 rounded-xl border text-sm font-medium flex items-start gap-3 ${g10AcctICScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-300 text-emerald-900' : g10AcctICScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-300 text-red-900' : 'bg-blue-50 border-blue-300 text-blue-900'}`}>
                                    <div className="mt-0.5">
                                        {g10AcctICScaffoldFeedback.kind === 'success' ? (
                                            <svg className="w-5 h-5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                        ) : g10AcctICScaffoldFeedback.kind === 'error' ? (
                                            <svg className="w-5 h-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                        ) : (
                                            <svg className="w-5 h-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                            </svg>
                                        )}
                                    </div>
                                    <div>
                                        <div className={`text-xs font-bold uppercase tracking-wider mb-0.5 ${g10AcctICScaffoldFeedback.kind === 'success' ? 'text-emerald-700' : g10AcctICScaffoldFeedback.kind === 'error' ? 'text-red-700' : 'text-blue-700'}`}>
                                            {g10AcctICScaffoldFeedback.kind === 'success' ? 'Correct' : g10AcctICScaffoldFeedback.kind === 'error' ? 'Needs Revision' : 'Information'}
                                        </div>
                                        <div>{g10AcctICScaffoldFeedback.message}</div>
                                    </div>
                                </div>
                            )}

                            {/* Marking Results */}
                            {marking.isMarkingSubmitted && marking.markingResults && question && (
                                <div className="mt-8 p-6 bg-gradient-to-br from-indigo-50 to-white border border-indigo-200 rounded-2xl shadow-sm">
                                    <h4 className="text-xl font-bold text-indigo-900 mb-4 flex items-center gap-2">
                                        <svg className="w-6 h-6 text-indigo-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
                                        </svg>
                                        Assessment Results
                                    </h4>
                                    <div className="flex items-end gap-3 mb-6">
                                        <span className="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-indigo-400">
                                            {Math.round((marking.markingResults.total_score / marking.markingResults.max_score) * 100)}%
                                        </span>
                                        <span className="text-lg font-semibold text-indigo-600 mb-1">
                                            ({marking.markingResults.total_score} / {marking.markingResults.max_score} marks)
                                        </span>
                                    </div>
                                    
                                    {marking.getFeedbackForQuestion(question.id) && (
                                        <div className={`mt-4 p-5 rounded-xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : 'bg-amber-50 border-amber-200 text-amber-900'}`}>
                                            <div className="font-bold mb-2 flex items-center gap-2">
                                                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 8h10M7 12h4m1 8l-4-4H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-3l-4 4z" />
                                                </svg>
                                                Backend Feedback
                                            </div>
                                            <div className="text-sm whitespace-pre-wrap leading-relaxed">
                                                {marking.getFeedbackForQuestion(question.id).message}
                                            </div>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    )}
                </div>

                {g10AcctICVisualAidsOpen && (
                    <div className="hidden lg:block w-1/3 sticky top-4">
                        {renderGrade10AcctICVisualAids && renderGrade10AcctICVisualAids()}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Grade10AccountingInternalControlScaffold;

