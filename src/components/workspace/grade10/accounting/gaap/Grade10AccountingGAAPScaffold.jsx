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

const buildWordbankMemoRows = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const wordBank = Array.isArray(question?.word_bank) ? question.word_bank : [];
    const correctMap = (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};
    const labelById = {};
    wordBank.forEach((token) => {
        labelById[String(token.id)] = String(token.label || '').trim();
    });
    return Object.keys(correctMap)
        .sort((a, b) => Number(a) - Number(b))
        .map((rowKey) => {
            const row = rows[Number(rowKey)] || [];
            const tokenId = correctMap?.[rowKey]?.['2'];
            return {
                rowLabel: String(row?.[0] || Number(rowKey) + 1),
                definition: String(row?.[1] || '').trim(),
                answer: labelById[String(tokenId)] || '',
            };
        })
        .filter((item) => item.answer);
};

const buildNonTabularMemoItems = (question) => {
    const explicitItems = Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];
    const normalizedExplicit = explicitItems
        .map((item, idx) => ({
            label: String(item?.label || `Answer part ${idx + 1}`).trim(),
            value: String(item?.value || '').trim(),
        }))
        .filter((item) => item.value);
    if (normalizedExplicit.length > 0) return normalizedExplicit;

    return String(question?.sample_answer || '')
        .split('\n')
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line, idx) => ({ label: `Memo point ${idx + 1}`, value: line }));
};

const buildTypedHintSections = (question) => {
    const sections = [];
    const guidelines = Array.isArray(question?.guidelines) ? question.guidelines.map((item) => String(item || '').trim()).filter(Boolean) : [];
    const memoLabels = Array.isArray(question?.answer_part_hints)
        ? question.answer_part_hints.map((item) => String(item?.label || '').trim()).filter(Boolean)
        : [];
    if (guidelines.length > 0) sections.push({ title: 'What to include', text: guidelines.join('\n') });
    if (memoLabels.length > 0) sections.push({ title: 'Memo structure', text: memoLabels.join('\n') });
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

const Grade10AccountingGAAPScaffold = ({
    onBack,
    scaffoldSteps,
    g10AcctGAAPVisualAidsOpen,
    setG10AcctGAAPVisualAidsOpen,
    g10AcctGAAPScaffoldDifficulty,
    setG10AcctGAAPScaffoldDifficulty,
    g10AcctGAAPScaffoldStepIndex,
    setG10AcctGAAPScaffoldStepIndex,
    fetchGrade10AcctGAAPScaffoldQuestion,
    g10AcctGAAPScaffoldLoading,
    g10AcctGAAPScaffoldError,
    g10AcctGAAPScaffoldQuestion,
    g10AcctGAAPScaffoldAnswer,
    setG10AcctGAAPScaffoldAnswer,
    g10AcctGAAPScaffoldFeedback,
    setG10AcctGAAPScaffoldFeedback,
    g10AcctGAAPScaffoldShowHint,
    setG10AcctGAAPScaffoldShowHint,
    renderGrade10AcctGAAPVisualAids,
    hideConfig,
}) => {
    const question = g10AcctGAAPScaffoldQuestion;
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [showCheckHighlights, setShowCheckHighlights] = useState(false);
    const [showMemo, setShowMemo] = useState(false);
    const cellHintPopupRef = useRef(null);

    const selectedSubtopic = scaffoldSteps[g10AcctGAAPScaffoldStepIndex] || scaffoldSteps[0];

    const marking = useGrade10AccountingMarking();

    const nonTabularMemoItems = question && question?.question_type !== 'table_wordbank' ? buildNonTabularMemoItems(question) : [];
    const wordbankMemoRows = question?.question_type === 'table_wordbank' ? buildWordbankMemoRows(question) : [];
    const typedHintSections = question?.question_type === 'typed' ? buildTypedHintSections(question) : [];

    useEffect(() => {
        setShowMemo(false);
        setShowCheckHighlights(false);
        setActiveCellHint(null);
    }, [question?.id]);

    useEffect(() => {
        if (!activeCellHint || !cellHintPopupRef.current) return;
        const width = cellHintPopupRef.current.offsetWidth || 320;
        const height = cellHintPopupRef.current.offsetHeight || 240;
        const next = clampHintPosition(activeCellHint.x, activeCellHint.y, width, height);
        if (next.x !== activeCellHint.x || next.y !== activeCellHint.y) {
            setActiveCellHint((prev) => (prev ? { ...prev, x: next.x, y: next.y } : prev));
        }
    }, [activeCellHint]);

    // Reset marking state when new subtopic selected
    useEffect(() => {
        marking.setMarkingMode('practice');
    }, [g10AcctGAAPScaffoldStepIndex]);

    const newExample = () => {
        fetchGrade10AcctGAAPScaffoldQuestion({
            subskill: selectedSubtopic?.key || 'intro',
            difficulty: g10AcctGAAPScaffoldDifficulty,
        });
    };

    const checkAnswer = () => {
        if (!question) return;

        if (question.question_type === 'mcq') {
            const ok = String(g10AcctGAAPScaffoldAnswer) === String(question.correct_index);
            setShowCheckHighlights(true);
            setG10AcctGAAPScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.options?.[question.correct_index] || ''}` });
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctGAAPScaffoldAnswer && typeof g10AcctGAAPScaffoldAnswer === 'object')
                ? g10AcctGAAPScaffoldAnswer
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
            setShowCheckHighlights(true);
            setG10AcctGAAPScaffoldFeedback(ok
                ? { kind: 'success', message: 'All matches are correct!' }
                : { kind: 'error', message: `You matched ${hit}/${total} correctly. Keep trying!` });
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(g10AcctGAAPScaffoldAnswer);
            if (!user) {
                setG10AcctGAAPScaffoldFeedback({ kind: 'error', message: 'Write an answer first.' });
                return;
            }
            setShowCheckHighlights(true);
            setShowMemo(true);
            setG10AcctGAAPScaffoldFeedback({ kind: 'info', message: 'Compare your answer to the memo / guidelines below.' });
            return;
        }

        setG10AcctGAAPScaffoldFeedback({ kind: 'error', message: `Unsupported question type: ${question.question_type}` });
    };

    const setAnswerValue = (value) => {
        setG10AcctGAAPScaffoldAnswer(value);
        if (question) {
            marking.registerAnswer(question.id, value);
        }
        setG10AcctGAAPScaffoldFeedback(null);
        setShowCheckHighlights(false);
    };

    const handleWordbankCellHint = (e, hintText) => {
        e.preventDefault();
        e.stopPropagation();
        if (activeCellHint && activeCellHint.text === hintText) {
            setActiveCellHint(null);
            return;
        }
        const rect = e.currentTarget.getBoundingClientRect();
        setActiveCellHint({
            x: rect.right + 10,
            y: rect.top,
            text: hintText,
            sections: buildHintSections(null, hintText),
        });
    };

    const renderWordbankTable = () => {
        const q = question;
        const ans = (g10AcctGAAPScaffoldAnswer && typeof g10AcctGAAPScaffoldAnswer === 'object')
            ? g10AcctGAAPScaffoldAnswer
            : buildEmptyWordbankAnswer(q);

        const wordBank = getWordBank(q);
        const used = showMemo ? new Set() : getUsedTokenIds(ans);

        const tokenLabelById = {};
        wordBank.forEach((t) => { tokenLabelById[String(t.id)] = String(t.label || '').trim(); });

        const setActiveTokenId = (tokenId) => {
            if (showMemo) return;
            setAnswerValue({
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
            setAnswerValue(next);
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
            setAnswerValue(next);
        };

        const rows = Array.isArray(q?.table?.rows) ? q.table.rows : [];
        const headers = Array.isArray(q?.table?.headers) ? q.table.headers : [];
        const correctMap = getCorrectMap(q);
        const effectiveSelections = showMemo ? correctMap : (ans?.selections || {});

        return (
            <div className="mt-3 relative">
                {!showMemo && (
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
                                    disabled={isUsed || !marking.isPracticeMode}
                                    onClick={() => setActiveTokenId(String(t.id))}
                                    className={`px-3 py-1.5 rounded-lg text-sm font-semibold border transition-all ${isUsed ? 'bg-slate-100 text-slate-400 border-slate-200 opacity-50' : isActive ? 'bg-indigo-600 text-white border-indigo-600 shadow-md ring-2 ring-indigo-300 ring-offset-1' : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-50 hover:border-slate-400 shadow-sm'}`}
                                >
                                    {t.label}
                                </button>
                            );
                        })}
                    </div>
                </div>
                )}

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
                                const selectedId = effectiveSelections?.[String(rowIndex)]?.['2'];
                                const expectedId = correctMap?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';
                                const isRowCorrect = (showCheckHighlights || showMemo) && String(selectedId) === String(expectedId);
                                const isRowIncorrect = showCheckHighlights && !showMemo && selectedId && String(selectedId) !== String(expectedId);

                                return (
                                    <tr key={rowIndex} className={`transition-colors ${rowIndex % 2 === 0 ? 'bg-white' : 'bg-slate-50/50'} hover:bg-indigo-50/30`}>
                                        <td className="px-4 py-3 align-top font-medium text-slate-700">{row[0]}</td>
                                        <td className="px-4 py-3 align-top text-slate-600">{row[1] || ''}</td>
                                        <td className="px-4 py-3 align-top">
                                            <div className="flex gap-2">
                                                <div className="flex-1">
                                                    <button
                                                        type="button"
                                                        onClick={() => placeActive(rowIndex)}
                                                        disabled={!marking.isPracticeMode}
                                                        className={`w-full text-left px-3 py-2.5 rounded-lg border transition-all ${isRowCorrect ? 'bg-emerald-50 border-emerald-300 ring-1 ring-emerald-200' : isRowIncorrect ? 'bg-red-50 border-red-300 ring-1 ring-red-200' : label ? 'bg-indigo-50 border-indigo-200 shadow-inner text-indigo-900' : 'bg-white border-slate-200 hover:bg-slate-50 text-slate-400 border-dashed'}`}
                                                    >
                                                        {label ? (
                                                            <span className="font-semibold">{label}</span>
                                                        ) : (
                                                            <span>Click to place...</span>
                                                        )}
                                                    </button>
                                                    {label && marking.isPracticeMode && !showMemo && (
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
                                                <button
                                                    type="button"
                                                    onClick={(e) => handleWordbankCellHint(e, q?.teaching_hints?.[String(rowIndex)]?.['2']?.fallback || 'Review the definition carefully and compare it to the principles in the word bank.')}
                                                    className="w-8 h-8 flex items-center justify-center rounded-full bg-indigo-50 text-indigo-600 hover:bg-indigo-100 hover:text-indigo-800 transition-colors flex-shrink-0 mt-1"
                                                    title="Get a hint for this row"
                                                >
                                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                    </svg>
                                                </button>
                                            </div>
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>

                {activeCellHint && (
                    <div
                        ref={cellHintPopupRef}
                        className="fixed z-50 w-72 bg-white rounded-xl shadow-xl border border-indigo-100 overflow-hidden"
                        style={{ left: activeCellHint.x, top: activeCellHint.y }}
                    >
                        <div className="bg-indigo-600 px-4 py-2 flex justify-between items-center">
                            <span className="text-white font-semibold text-sm">Cell Hint</span>
                            <button
                                onClick={() => setActiveCellHint(null)}
                                className="text-indigo-100 hover:text-white"
                            >
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
                            </button>
                        </div>
                        <div className="p-4 max-h-[300px] overflow-y-auto bg-indigo-50/50">
                            {activeCellHint.sections && activeCellHint.sections.length > 0 ? (
                                <div className="space-y-3">
                                    {activeCellHint.sections.map((sec, idx) => (
                                        <div key={idx}>
                                            <span className="font-semibold text-indigo-900 block text-xs uppercase tracking-wider mb-1">{sec.title}</span>
                                            <span className="text-indigo-800 text-sm">{sec.text}</span>
                                        </div>
                                    ))}
                                </div>
                            ) : (
                                <p className="text-sm text-indigo-800">{activeCellHint.text}</p>
                            )}
                        </div>
                    </div>
                )}
            </div>
        );
    };

    const hasInput = useMemo(() => {
        if (!question) return false;
        const ans = g10AcctGAAPScaffoldAnswer;
        if (question.question_type === 'mcq') return ans !== null && ans !== undefined && String(ans).trim() !== '';
        if (question.question_type === 'typed') return String(ans || '').trim().length > 0;
        if (question.question_type === 'table_wordbank') {
            const wbAns = g10AcctGAAPScaffoldAnswer;
            return (wbAns && wbAns.selections) ? Object.values(wbAns.selections).some(row => row && Object.values(row).some(v => v !== null && v !== undefined)) : false;
        }
        if (question.question_type === 'table') {
            return (ans && ans.rows) ? ans.rows.some(r => (r || []).some(c => String(c || '').trim().length > 0)) : false;
        }
        if (question.question_type === 'calc') {
            return ans && Object.values(ans).some(val => String(val || '').trim().length > 0);
        }
        return false;
    }, [question, g10AcctGAAPScaffoldAnswer]);

    return (
        <div className="w-full relative">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-4">
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
                                value={g10AcctGAAPScaffoldDifficulty}
                                onChange={(e) => setG10AcctGAAPScaffoldDifficulty(e.target.value)}
                                className="text-sm border border-slate-300 rounded-lg px-2 py-1.5 bg-white text-slate-700 font-medium focus:ring-2 focus:ring-indigo-500 outline-none"
                            >
                                <option value="easy">Easy</option>
                                <option value="medium">Medium</option>
                                <option value="hard">Hard</option>
                            </select>
                            <button
                                onClick={() => setG10AcctGAAPVisualAidsOpen(!g10AcctGAAPVisualAidsOpen)}
                                className={`px-3 py-1.5 text-sm font-semibold rounded-lg border transition-colors ${g10AcctGAAPVisualAidsOpen ? 'bg-indigo-50 text-indigo-700 border-indigo-200' : 'bg-white text-slate-600 border-slate-300 hover:bg-slate-50'}`}
                            >
                                Visual Aids
                            </button>
                        </div>
                    )}
                </div>
            </div>

            <div className="flex flex-col lg:flex-row gap-6 items-start">
                <div className={`flex-1 min-w-0 transition-all duration-300 ${g10AcctGAAPVisualAidsOpen ? 'lg:w-2/3' : 'w-full'}`}>
                    
                    {!hideConfig && scaffoldSteps.length > 0 && (
                        <div className="mb-6 flex flex-wrap gap-2">
                            {scaffoldSteps.map((step, idx) => (
                                <button
                                    key={step.key}
                                    onClick={() => setG10AcctGAAPScaffoldStepIndex(idx)}
                                    className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${idx === g10AcctGAAPScaffoldStepIndex ? 'bg-slate-800 text-white shadow-md' : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-50 hover:text-slate-900'}`}
                                >
                                    {step.title}
                                </button>
                            ))}
                        </div>
                    )}

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

                    <div className="bg-white rounded-2xl shadow-sm border border-slate-200 overflow-hidden">
                        <div className="bg-slate-50/50 border-b border-slate-100 px-5 py-4 flex items-center justify-between">
                            <div className="flex items-center gap-3">
                                <span className="flex items-center justify-center w-8 h-8 rounded-full bg-indigo-100 text-indigo-700 font-bold text-sm">
                                    Q
                                </span>
                                <h4 className="font-semibold text-slate-800">{selectedSubtopic.title}</h4>
                            </div>
                            <button
                                onClick={newExample}
                                className="text-sm font-semibold text-indigo-600 hover:text-indigo-800 flex items-center gap-1.5 px-3 py-1.5 rounded-lg hover:bg-indigo-50 transition-colors"
                            >
                                <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                                </svg>
                                New Example
                            </button>
                        </div>

                        <div className="p-5">
                            {g10AcctGAAPScaffoldLoading ? (
                                <div className="flex flex-col items-center justify-center py-12 text-slate-400">
                                    <svg className="animate-spin h-8 w-8 mb-4 text-indigo-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                    </svg>
                                    <p className="font-medium">Generating question...</p>
                                </div>
                            ) : g10AcctGAAPScaffoldError ? (
                                <div className="p-4 bg-red-50 text-red-700 rounded-xl border border-red-100 break-words">
                                    {g10AcctGAAPScaffoldError}
                                </div>
                            ) : !question ? (
                                <div className="text-center py-8 text-slate-500 font-medium">
                                    Click "New Example" to generate a question.
                                </div>
                            ) : (
                                <div>
                                    {question.question_type === 'mcq' && (
                                        <div className="mt-6 grid grid-cols-1 gap-2.5">
                                            {(question.options || []).map((opt, idx) => {
                                                const isSelected = String(g10AcctGAAPScaffoldAnswer) === String(idx);
                                                const isCorrect = showCheckHighlights && String(idx) === String(question.correct_index);
                                                const isWrongSelected = showCheckHighlights && isSelected && String(idx) !== String(question.correct_index);

                                                let stateClass = 'hover:border-indigo-300 hover:bg-indigo-50/30';
                                                if (isCorrect) stateClass = 'bg-emerald-50 border-emerald-400 ring-1 ring-emerald-400 shadow-sm';
                                                else if (isWrongSelected) stateClass = 'bg-red-50 border-red-300 ring-1 ring-red-300';
                                                else if (isSelected) stateClass = 'border-indigo-500 ring-1 ring-indigo-500 bg-indigo-50/50 shadow-sm';

                                                return (
                                                    <button
                                                        key={idx}
                                                        disabled={!marking.isPracticeMode}
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
                                    )}

                                    {question.question_type === 'typed' && (
                                        <div className="mt-6">
                                            <textarea
                                                value={typeof g10AcctGAAPScaffoldAnswer === 'string' ? g10AcctGAAPScaffoldAnswer : ''}
                                                onChange={(e) => setAnswerValue(e.target.value)}
                                                disabled={!marking.isPracticeMode}
                                                className={`w-full min-h-[140px] p-4 border-2 rounded-xl text-slate-700 focus:outline-none transition-all ${showCheckHighlights ? 'border-slate-200 bg-slate-50' : 'border-slate-200 focus:border-indigo-400 focus:ring-4 focus:ring-indigo-50'}`}
                                                placeholder={marking.isPracticeMode ? "Type your explanation or answer here..." : "Answer locked for marking"}
                                            />
                                        </div>
                                    )}

                                    {question.question_type === 'table_wordbank' && renderWordbankTable()}

                                    <div className="mt-6 flex flex-wrap gap-2 pt-4 border-t border-slate-100">
                                        {marking.isPracticeMode ? (
                                            <>
                                                <button
                                                    type="button"
                                                    onClick={checkAnswer}
                                                    className="px-5 py-2.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl font-semibold transition-all shadow-sm flex items-center gap-2"
                                                >
                                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                                                    </svg>
                                                    Check
                                                </button>
                                                <button
                                                    type="button"
                                                    onClick={() => setG10AcctGAAPScaffoldShowHint(!g10AcctGAAPScaffoldShowHint)}
                                                    className={`px-5 py-2.5 border-2 rounded-xl font-semibold transition-all flex items-center gap-2 ${g10AcctGAAPScaffoldShowHint ? 'bg-amber-100 border-amber-300 text-amber-900' : 'bg-white border-slate-200 hover:bg-slate-50 hover:border-slate-300 text-slate-700'}`}
                                                >
                                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                                                    </svg>
                                                    Hint
                                                </button>
                                                <button
                                                    type="button"
                                                    disabled={!hasInput}
                                                    onClick={() => setShowMemo(!showMemo)}
                                                    className={`px-5 py-2.5 border-2 rounded-xl font-semibold transition-all flex items-center gap-2 ${showMemo ? 'bg-indigo-100 border-indigo-300 text-indigo-900' : 'bg-white border-slate-200 hover:bg-slate-50 hover:border-slate-300 text-slate-700'} ${!hasInput ? 'opacity-50 cursor-not-allowed' : ''}`}
                                                >
                                                    <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                                    </svg>
                                                    {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                                </button>
                                                {(showCheckHighlights || g10AcctGAAPScaffoldFeedback) && (
                                                    <button
                                                        type="button"
                                                        onClick={() => {
                                                            setShowCheckHighlights(false);
                                                            setG10AcctGAAPScaffoldFeedback(null);
                                                        }}
                                                        className="px-4 py-2.5 ml-auto bg-white border border-slate-200 hover:bg-slate-50 text-slate-500 hover:text-slate-700 rounded-xl text-sm font-semibold transition-all"
                                                    >
                                                        Clear feedback
                                                    </button>
                                                )}
                                            </>
                                        ) : (
                                            !marking.isMarkingSubmitted && (
                                                <button
                                                    type="button"
                                                    onClick={() => marking.submitAssessment([question])}
                                                    disabled={marking.isSubmitting}
                                                    className="px-6 py-3 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 shadow-md transition-colors disabled:opacity-50 flex items-center gap-2"
                                                >
                                                    {marking.isSubmitting ? (
                                                        <>
                                                            <svg className="animate-spin w-5 h-5 text-white" fill="none" viewBox="0 0 24 24">
                                                                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                                                                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
                                                            </svg>
                                                            Submitting...
                                                        </>
                                                    ) : 'Submit Assessment'}
                                                </button>
                                            )
                                        )}
                                    </div>

                                    {g10AcctGAAPScaffoldShowHint && marking.isPracticeMode && (
                                        <div className="mt-5 p-5 bg-amber-50 rounded-xl border border-amber-200">
                                            <h4 className="font-bold text-amber-900 mb-3 flex items-center gap-2">
                                                <svg className="w-5 h-5 text-amber-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                                </svg>
                                                Hints & Guidelines
                                            </h4>
                                            {typedHintSections.length > 0 ? (
                                                <div className="space-y-4">
                                                    {typedHintSections.map((sec, idx) => (
                                                        <div key={idx}>
                                                            <span className="font-semibold text-amber-900 block text-sm uppercase tracking-wider mb-1">{sec.title}</span>
                                                            <span className="text-amber-800 text-sm whitespace-pre-wrap">{sec.text}</span>
                                                        </div>
                                                    ))}
                                                </div>
                                            ) : (
                                                <p className="text-amber-800 text-sm">
                                                    {question?.teaching_hint?.fallback || 'Review the curriculum guidelines for this topic.'}
                                                </p>
                                            )}
                                        </div>
                                    )}

                                    {showMemo && marking.isPracticeMode && (
                                        <div className="mt-5 p-6 bg-indigo-50 border border-indigo-200 rounded-xl shadow-sm">
                                            <h4 className="text-base font-bold text-indigo-900 mb-4 flex items-center gap-2">
                                                <svg className="w-5 h-5 text-indigo-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
                                                </svg>
                                                Correct Memo Answers
                                            </h4>
                                            {question?.question_type === 'table_wordbank' ? (
                                                <div className="space-y-3">
                                                    {wordbankMemoRows.map((r, i) => (
                                                        <div key={i} className="flex flex-col sm:flex-row gap-2 sm:gap-4 text-sm pb-3 border-b border-indigo-100 last:border-0 last:pb-0">
                                                            <span className="font-bold text-indigo-900 min-w-[30px]">{r.rowLabel}.</span>
                                                            <span className="text-indigo-800 flex-1 leading-relaxed">{r.definition}</span>
                                                            <span className="font-semibold text-emerald-800 bg-emerald-100/50 border border-emerald-200 px-3 py-1 rounded-lg ml-auto mt-2 sm:mt-0 shadow-sm">{r.answer}</span>
                                                        </div>
                                                    ))}
                                                </div>
                                            ) : question?.question_type === 'mcq' ? (
                                                <p className="text-sm text-emerald-800 font-semibold bg-emerald-100/50 border border-emerald-200 p-3 rounded-lg inline-block">
                                                    Correct option: {question.options?.[question.correct_index]}
                                                </p>
                                            ) : (
                                                <div className="space-y-3">
                                                    {nonTabularMemoItems.map((item, idx) => (
                                                        <div key={idx} className="flex flex-col sm:flex-row gap-2 sm:gap-4 text-sm pb-3 border-b border-indigo-100 last:border-0 last:pb-0">
                                                            <span className="font-bold text-indigo-900 sm:w-1/4 shrink-0">{item.label}</span>
                                                            <span className="text-indigo-800 flex-1 whitespace-pre-wrap leading-relaxed">{item.value}</span>
                                                        </div>
                                                    ))}
                                                </div>
                                            )}
                                        </div>
                                    )}

                                    {g10AcctGAAPScaffoldFeedback && marking.isPracticeMode && (
                                        <div className={`mt-5 p-4 rounded-xl text-sm border font-medium flex items-start gap-3 ${g10AcctGAAPScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-300 text-emerald-900' : g10AcctGAAPScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-300 text-red-900' : 'bg-blue-50 border-blue-300 text-blue-900'}`}>
                                            <div className="mt-0.5">
                                                {g10AcctGAAPScaffoldFeedback.kind === 'success' && (
                                                    <svg className="w-5 h-5 text-emerald-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" /></svg>
                                                )}
                                                {g10AcctGAAPScaffoldFeedback.kind === 'error' && (
                                                    <svg className="w-5 h-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" /></svg>
                                                )}
                                                {g10AcctGAAPScaffoldFeedback.kind === 'info' && (
                                                    <svg className="w-5 h-5 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                                                )}
                                            </div>
                                            <div>{g10AcctGAAPScaffoldFeedback.message}</div>
                                        </div>
                                    )}
                                </div>
                            )}
                        </div>
                    </div>

                    {marking.isMarkingSubmitted && marking.markingResults && (
                        <div className="mt-8 p-8 bg-gradient-to-br from-indigo-50 to-white border border-indigo-200 rounded-3xl shadow-sm">
                            <h4 className="text-2xl font-bold text-indigo-900 mb-3">Assessment Results</h4>
                            <div className="flex items-baseline gap-3 mb-6">
                                <span className="text-5xl font-black text-transparent bg-clip-text bg-gradient-to-r from-indigo-600 to-indigo-400">
                                    {Math.round((marking.markingResults.total_score / marking.markingResults.max_score) * 100)}%
                                </span>
                                <span className="text-base font-semibold text-indigo-600">
                                    ({marking.markingResults.total_score} / {marking.markingResults.max_score} marks)
                                </span>
                            </div>
                            
                            {marking.getFeedbackForQuestion(question?.id) && (
                                <div className={`p-5 rounded-2xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : 'bg-amber-50 border-amber-200 text-amber-900'}`}>
                                    <h5 className="font-bold mb-2 flex items-center gap-2">
                                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                                        </svg>
                                        Backend Feedback
                                    </h5>
                                    <div className="text-sm whitespace-pre-wrap leading-relaxed">
                                        {marking.getFeedbackForQuestion(question.id).message}
                                    </div>
                                </div>
                            )}
                        </div>
                    )}
                </div>

                {g10AcctGAAPVisualAidsOpen && (
                    <div className="hidden lg:block w-1/3 sticky top-4">
                        {renderGrade10AcctGAAPVisualAids && renderGrade10AcctGAAPVisualAids()}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Grade10AccountingGAAPScaffold;

