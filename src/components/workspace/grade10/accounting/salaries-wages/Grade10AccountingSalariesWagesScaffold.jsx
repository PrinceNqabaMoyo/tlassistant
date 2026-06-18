import React, { useEffect, useState } from 'react';
import MCQOption from '../../../shared/MCQOption';
import { useGrade10AccountingMarking } from '../useGrade10AccountingMarking';

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

const toNumber = (value) => {
    if (value === null || value === undefined) return null;
    let s = String(value).trim();
    if (!s) return null;
    s = s.replace(/\s+/g, '');
    s = s.replace(/[Rr]/g, '');
    const lastDot = s.lastIndexOf('.');
    const lastComma = s.lastIndexOf(',');
    if (lastDot >= 0 && lastComma >= 0) {
        const decSep = lastDot > lastComma ? '.' : ',';
        const thouSep = decSep === '.' ? ',' : '.';
        s = s.split(thouSep).join('');
        if (decSep === ',') s = s.replace(',', '.');
    } else if (lastComma >= 0) {
        s = s.split('.').join('');
        s = s.replace(',', '.');
    } else {
        s = s.split(',').join('');
    }
    s = s.replace(/[^0-9.\-]/g, '');
    const n = Number(s);
    return Number.isFinite(n) ? n : null;
};

const numbersMatch = (actual, expected) => {
    const actualN = typeof actual === 'number' ? actual : toNumber(actual);
    const expectedN = typeof expected === 'number' ? expected : toNumber(expected);
    if (actualN === null || expectedN === null) return false;
    return Math.abs(actualN - expectedN) <= 0.01;
};

const getWordBank = (question) => Array.isArray(question?.word_bank) ? question.word_bank : [];

const getCorrectMap = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const buildEmptyJournalAnswer = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const cells = {};
    journals.forEach((journal) => {
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        rows.forEach((row) => {
            (Array.isArray(row) ? row : []).forEach((cell) => {
                if (!cell?.cell_id) return;
                cells[String(cell.cell_id)] = cell?.value || '';
            });
        });
    });
    return { cells, extra_rows_by_table: {} };
};

const buildNonTabularHintItems = (question) => {
    const explicitItems = Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];
    const normalizedExplicit = explicitItems
        .map((item, idx) => ({
            label: String(item?.label || `Answer part ${idx + 1}`).trim(),
            value: String(item?.value || '').trim(),
        }))
        .filter((item) => item.value);
    if (normalizedExplicit.length > 0) return normalizedExplicit;

    if (question?.question_type === 'calc') {
        const items = [];
        const formula = String(question?.working_formula || '').trim();
        if (formula) items.push({ label: 'Working', value: formula });
        if (question?.correct_answer !== null && question?.correct_answer !== undefined && String(question.correct_answer).trim() !== '') {
            const unit = String(question?.unit || '').trim();
            items.push({ label: 'Correct answer', value: `${unit}${question.correct_answer}`.trim() });
        }
        return items;
    }

    return String(question?.sample_answer || '')
        .split('\n')
        .map((line) => line.trim())
        .filter(Boolean)
        .map((line, idx) => ({ label: `Memo point ${idx + 1}`, value: line }));
};

const buildWordbankMemoRows = (question) => {
    const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
    const wordBank = getWordBank(question);
    const correctMap = getCorrectMap(question);
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

const buildTypedHintSections = (question) => {
    const sections = [];
    const guidelines = Array.isArray(question?.guidelines) ? question.guidelines.map((item) => String(item || '').trim()).filter(Boolean) : [];
    const memoLabels = Array.isArray(question?.answer_part_hints)
        ? question.answer_part_hints.map((item) => String(item?.label || '').trim()).filter(Boolean)
        : [];

    if (guidelines.length > 0) {
        sections.push({ title: 'What to include', text: guidelines.join('\n') });
    }
    if (memoLabels.length > 0) {
        sections.push({ title: 'Memo structure', text: memoLabels.join('\n') });
    }
    return sections;
};

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

const SCAFFOLD_DIFFICULTY_ORDER = ['easy', 'medium', 'hard'];

const getNextScaffoldDifficulty = (difficultyRaw) => {
    const difficulty = String(difficultyRaw || 'easy').trim().toLowerCase();
    const idx = SCAFFOLD_DIFFICULTY_ORDER.indexOf(difficulty);
    if (idx < 0 || idx >= SCAFFOLD_DIFFICULTY_ORDER.length - 1) return null;
    return SCAFFOLD_DIFFICULTY_ORDER[idx + 1];
};

const shouldHandleEnterCheck = (event) => {
    if (event.key !== 'Enter' || event.nativeEvent?.isComposing) return false;
    const tagName = String(event.target?.tagName || '').toLowerCase();
    if (tagName === 'textarea') return !event.shiftKey;
    return tagName === 'input';
};

const Grade10AccountingSalariesWagesScaffold = ({
    onBack,
    scaffoldSteps,
    g10AcctSWVisualAidsOpen,
    setG10AcctSWVisualAidsOpen,
    g10AcctSWScaffoldDifficulty,
    setG10AcctSWScaffoldDifficulty,
    g10AcctSWScaffoldStepIndex,
    setG10AcctSWScaffoldStepIndex,
    fetchGrade10AcctSWScaffoldQuestion,
    g10AcctSWScaffoldLoading,
    g10AcctSWScaffoldError,
    g10AcctSWScaffoldQuestion,
    g10AcctSWScaffoldAnswer,
    setG10AcctSWScaffoldAnswer,
    g10AcctSWScaffoldFeedback,
    setG10AcctSWScaffoldFeedback,
    g10AcctSWScaffoldShowHint,
    setG10AcctSWScaffoldShowHint,
    renderGrade10AcctSWVisualAids,
    hideConfig,
    evaluationState,
}) => {
    const question = g10AcctSWScaffoldQuestion;
    const [showMemo, setShowMemo] = useState(false);
    const [attemptRecordedForQuestion, setAttemptRecordedForQuestion] = useState(false);
    const [keepCurrentDifficulty, setKeepCurrentDifficulty] = useState(false);
    const [difficultyAttemptCounts, setDifficultyAttemptCounts] = useState({ easy: 0, medium: 0, hard: 0 });
    const [pendingDifficultyPromotion, setPendingDifficultyPromotion] = useState(null);
    const [difficultyNotice, setDifficultyNotice] = useState('');

    const selectedSubtopic = scaffoldSteps[g10AcctSWScaffoldStepIndex] || scaffoldSteps[0];
    const difficultyProgressKey = `g10_acct_sw_scaffold_difficulty_progress_${selectedSubtopic?.key || 'mixed'}`;
    const difficultyKeepKey = `g10_acct_sw_scaffold_keep_mode_${selectedSubtopic?.key || 'mixed'}`;

    const marking = useGrade10AccountingMarking();
    const nonTabularHintItems = question ? buildNonTabularHintItems(question) : [];
    const wordbankMemoRows = question?.question_type === 'table_wordbank' ? buildWordbankMemoRows(question) : [];
    const typedHintSections = question?.question_type === 'typed' ? buildTypedHintSections(question) : [];
    const calcHintText = String(question?.working_formula || '').trim();
    const currentDifficulty = String(g10AcctSWScaffoldDifficulty || 'easy').trim().toLowerCase();
    const nextDifficulty = getNextScaffoldDifficulty(currentDifficulty);
    const currentDifficultyAttempts = Number(difficultyAttemptCounts?.[currentDifficulty]) || 0;
    const attemptsTowardNextLevel = nextDifficulty
        ? (pendingDifficultyPromotion ? 5 : (currentDifficultyAttempts % 5))
        : 0;

    useEffect(() => {
        marking.setMarkingMode('practice');
    }, [g10AcctSWScaffoldStepIndex]);

    useEffect(() => {
        try {
            const savedCounts = JSON.parse(localStorage.getItem(difficultyProgressKey) || '{}');
            setDifficultyAttemptCounts({
                easy: Number(savedCounts?.easy) || 0,
                medium: Number(savedCounts?.medium) || 0,
                hard: Number(savedCounts?.hard) || 0,
            });
        } catch {
            setDifficultyAttemptCounts({ easy: 0, medium: 0, hard: 0 });
        }
        try {
            setKeepCurrentDifficulty(localStorage.getItem(difficultyKeepKey) === 'true');
        } catch {
            setKeepCurrentDifficulty(false);
        }
        setPendingDifficultyPromotion(null);
        setDifficultyNotice('');
    }, [difficultyKeepKey, difficultyProgressKey]);

    useEffect(() => {
        localStorage.setItem(difficultyProgressKey, JSON.stringify(difficultyAttemptCounts));
    }, [difficultyAttemptCounts, difficultyProgressKey]);

    useEffect(() => {
        localStorage.setItem(difficultyKeepKey, keepCurrentDifficulty ? 'true' : 'false');
    }, [difficultyKeepKey, keepCurrentDifficulty]);

    useEffect(() => {
        setShowMemo(false);
        setAttemptRecordedForQuestion(false);
    }, [question?.id]);

    useEffect(() => {
        if (!question) return;
        if ((question.question_type === 'journal' || question.question_type === 'ledger') && (!g10AcctSWScaffoldAnswer || typeof g10AcctSWScaffoldAnswer !== 'object' || !g10AcctSWScaffoldAnswer.cells)) {
            setG10AcctSWScaffoldAnswer(buildEmptyJournalAnswer(question));
        }
        if (question.question_type === 'table_wordbank' && (!g10AcctSWScaffoldAnswer || typeof g10AcctSWScaffoldAnswer !== 'object' || !g10AcctSWScaffoldAnswer.selections)) {
            setG10AcctSWScaffoldAnswer(buildEmptyWordbankAnswer(question));
        }
    }, [question?.id]);

    const registerDifficultyAttempt = () => {
        if (attemptRecordedForQuestion) return;
        setAttemptRecordedForQuestion(true);
        setDifficultyAttemptCounts((prev) => {
            const nextCounts = {
                easy: Number(prev?.easy) || 0,
                medium: Number(prev?.medium) || 0,
                hard: Number(prev?.hard) || 0,
            };
            nextCounts[currentDifficulty] = (Number(nextCounts[currentDifficulty]) || 0) + 1;
            const nextLevel = getNextScaffoldDifficulty(currentDifficulty);
            const reachedThreshold = nextLevel && nextCounts[currentDifficulty] > 0 && nextCounts[currentDifficulty] % 5 === 0;
            if (reachedThreshold) {
                if (keepCurrentDifficulty) {
                    setPendingDifficultyPromotion(null);
                    setDifficultyNotice(`You have completed ${nextCounts[currentDifficulty]} ${currentDifficulty} scaffold questions. Keep ${currentDifficulty} mode is on, so the next question will stay on ${currentDifficulty}.`);
                } else {
                    setPendingDifficultyPromotion(nextLevel);
                    setDifficultyNotice(`You have completed ${nextCounts[currentDifficulty]} ${currentDifficulty} scaffold questions. The next question will move to ${nextLevel} unless you choose Keep ${currentDifficulty} mode.`);
                }
            }
            return nextCounts;
        });
    };

    const newExample = () => {
        let difficultyForNextQuestion = currentDifficulty;
        if (pendingDifficultyPromotion) {
            if (keepCurrentDifficulty) {
                setDifficultyNotice(`Continuing in ${currentDifficulty} because keep mode is on.`);
            } else {
                difficultyForNextQuestion = pendingDifficultyPromotion;
                if (difficultyForNextQuestion !== currentDifficulty) {
                    setG10AcctSWScaffoldDifficulty(difficultyForNextQuestion);
                }
                setDifficultyNotice(`Difficulty moved to ${difficultyForNextQuestion} for the next scaffold question.`);
            }
            setPendingDifficultyPromotion(null);
        }
        fetchGrade10AcctSWScaffoldQuestion({
            subskill: selectedSubtopic?.key || 'salary_scales',
            difficulty: difficultyForNextQuestion,
        });
        setShowMemo(false);
    };

    const checkAnswer = () => {
        if (!question) return;

        if (question.question_type === 'mcq') {
            if (g10AcctSWScaffoldAnswer === null || g10AcctSWScaffoldAnswer === undefined || String(g10AcctSWScaffoldAnswer).trim() === '') {
                setG10AcctSWScaffoldFeedback({ kind: 'error', message: 'Choose an option, then check.' });
                return;
            }
            const ok = String(g10AcctSWScaffoldAnswer) === String(question.correct_index);
            setG10AcctSWScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.options?.[question.correct_index] || ''}` });
            registerDifficultyAttempt();
            return;
        }

        if (question.question_type === 'calc') {
            const expected = parseFloat(question.correct_answer);
            const got = parseFloat(g10AcctSWScaffoldAnswer);
            if (isNaN(got)) {
                setG10AcctSWScaffoldFeedback({ kind: 'error', message: 'Enter a number.' });
                return;
            }
            const ok = Math.abs(expected - got) < 0.01;
            setG10AcctSWScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct!' }
                : { kind: 'error', message: `Not quite. Expected: ${question.unit || 'R'}${expected.toFixed(2)}` });
            registerDifficultyAttempt();
            return;
        }

        if (question.question_type === 'table_wordbank') {
            const correctMap = getCorrectMap(question);
            const ans = (g10AcctSWScaffoldAnswer && typeof g10AcctSWScaffoldAnswer === 'object')
                ? g10AcctSWScaffoldAnswer
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
            setG10AcctSWScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You matched ${hit}/${total} correctly.` });
            registerDifficultyAttempt();
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(g10AcctSWScaffoldAnswer);
            if (!user) {
                setG10AcctSWScaffoldFeedback({ kind: 'error', message: 'Write an answer, then check.' });
                return;
            }
            setG10AcctSWScaffoldFeedback({ kind: 'info', message: 'Answer submitted. Use Compare / Memo to review the memo and guidance.' });
            registerDifficultyAttempt();
            return;
        }

        if (question.question_type === 'journal' || question.question_type === 'ledger') {
            const expectedMap = getCorrectMap(question);
            const ans = (g10AcctSWScaffoldAnswer && typeof g10AcctSWScaffoldAnswer === 'object')
                ? g10AcctSWScaffoldAnswer
                : buildEmptyJournalAnswer(question);
            const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
            const keys = Object.keys(expectedMap);
            let hit = 0;
            keys.forEach((key) => {
                const expected = expectedMap[key];
                const got = cells[key];
                if (normalizeText(got) === normalizeText(expected)) {
                    hit += 1;
                    return;
                }
                if (numbersMatch(got, expected)) {
                    hit += 1;
                }
            });
            const ok = keys.length > 0 && hit === keys.length;
            setG10AcctSWScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You completed ${hit}/${keys.length} cells correctly.` });
            registerDifficultyAttempt();
            return;
        }

        setG10AcctSWScaffoldFeedback({ kind: 'info', message: 'Answer saved.' });
        registerDifficultyAttempt();
    };

    const handleAnswerKeyDown = (event) => {
        if (!marking.isPracticeMode || !shouldHandleEnterCheck(event)) return;
        event.preventDefault();
        checkAnswer();
    };

    const setAnswerValue = (value) => {
        setG10AcctSWScaffoldAnswer(value);
        if (question) {
            marking.registerAnswer(question.id, value);
        }
        setG10AcctSWScaffoldFeedback(null);
        setShowMemo(false);
    };

    const renderWordbankTable = () => {
        if (!question) return null;

        const ans = (g10AcctSWScaffoldAnswer && typeof g10AcctSWScaffoldAnswer === 'object')
            ? g10AcctSWScaffoldAnswer
            : buildEmptyWordbankAnswer(question);

        const wordBank = getWordBank(question);
        const used = getUsedTokenIds(ans);

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

        const rows = Array.isArray(question?.table?.rows) ? question.table.rows : [];
        const headers = Array.isArray(question?.table?.headers) ? question.table.headers : [];

        return (
            <div className="mt-3">
                <div className="mb-3">
                    <div className="text-sm font-semibold text-slate-800 mb-2">Word bank</div>
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
                                    className={`px-3 py-1 rounded-full text-sm font-semibold border ${isUsed ? 'bg-slate-100 text-slate-400 border-slate-200' : isActive ? 'bg-slate-700 text-white border-slate-700' : 'bg-white text-slate-700 border-slate-300 hover:bg-slate-50'}`}
                                    title={isUsed ? 'Already used' : 'Click, then click a row cell to place'}
                                >
                                    {t.label}
                                </button>
                            );
                        })}
                    </div>
                    <div className="text-xs text-slate-500 mt-2">Click a word, then click a row's cell to place it.</div>
                </div>

                <div className="overflow-x-auto">
                    <table className="min-w-full border border-slate-200 text-sm">
                        <thead className="bg-slate-50">
                            <tr>
                                {headers.map((h, i) => (
                                    <th key={i} className="px-3 py-2 border-b border-slate-200 text-left font-semibold text-slate-800">{h}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {rows.map((row, rowIndex) => {
                                const selectedId = ans?.selections?.[String(rowIndex)]?.['2'];
                                const label = selectedId ? tokenLabelById[String(selectedId)] : '';
                                return (
                                    <tr key={rowIndex} className={rowIndex % 2 === 0 ? 'bg-white' : 'bg-slate-50'}>
                                        <td className="px-3 py-2 border-b border-slate-200 whitespace-nowrap">{row[0]}</td>
                                        <td className="px-3 py-2 border-b border-slate-200 min-w-[320px]">{row[1]}</td>
                                        <td className="px-3 py-2 border-b border-slate-200">
                                            <button
                                                type="button"
                                                onClick={() => placeActive(rowIndex)}
                                                className={`w-full text-left px-3 py-2 rounded-md border ${label ? 'bg-white border-slate-300' : 'bg-white border-slate-200 hover:bg-slate-50'}`}
                                                title="Click to place selected word"
                                            >
                                                {label ? (
                                                    <span className="inline-flex items-center gap-2">
                                                        <span className="font-semibold text-slate-800">{label}</span>
                                                        <span className="text-xs text-slate-500">(clear to change)</span>
                                                    </span>
                                                ) : (
                                                    <span className="text-slate-400">Click to place...</span>
                                                )}
                                            </button>
                                            <div className="mt-1">
                                                <button
                                                    type="button"
                                                    onClick={() => clearCell(rowIndex)}
                                                    className="text-xs font-semibold text-slate-600 hover:text-slate-900"
                                                >
                                                    Clear
                                                </button>
                                            </div>
                                        </td>
                                        {row[3] !== undefined && <td className="px-3 py-2 border-b border-slate-200">{row[3] || ''}</td>}
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>

                {Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                    <div className="mt-3 bg-slate-50 border border-slate-200 rounded-xl p-3">
                        <div className="text-sm font-semibold text-slate-800 mb-1">Guidelines</div>
                        <ul className="list-disc pl-5 space-y-1 text-sm text-slate-700">
                            {question.guidelines.map((g, idx) => (
                                <li key={idx}>{g}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        );
    };

    const renderCalcInput = () => (
        <div className="mt-3">
            <div className="flex items-center gap-2">
                {question.unit && <span className="text-slate-500 font-medium">{question.unit}</span>}
                <input
                    type="number"
                    step="0.01"
                    className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400"
                    placeholder="0.00"
                    value={g10AcctSWScaffoldAnswer || ''}
                    onChange={(e) => setAnswerValue(e.target.value)}
                />
            </div>
        </div>
    );

    const renderOneJournalTable = (journal, tableIndex, { readOnly = false } = {}) => {
        if (!journal) return null;
        const headers = Array.isArray(journal?.headers) ? journal.headers : [];
        const headerRows = Array.isArray(journal?.header_rows) ? journal.header_rows : [];
        const rows = Array.isArray(journal?.rows) ? journal.rows : [];
        const ans = (g10AcctSWScaffoldAnswer && typeof g10AcctSWScaffoldAnswer === 'object')
            ? g10AcctSWScaffoldAnswer
            : buildEmptyJournalAnswer(question);
        const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};

        const tableStyle = { width: '100%', minWidth: `${Math.max(headers.length * 112, 720)}px`, borderCollapse: 'collapse', tableLayout: 'fixed' };
        const headerStyle = { border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', verticalAlign: 'middle' };
        const bodyStyle = { border: '1px solid #000', padding: 0, verticalAlign: 'top' };

        return (
            <div className="mt-3 overflow-x-auto">
                <table style={tableStyle}>
                    <thead>
                        {headerRows.length > 0 ? headerRows.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {row.map((cell, cellIndex) => {
                                    const label = (cell && typeof cell === 'object') ? cell.label : String(cell ?? '');
                                    const colSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.colSpan))) ? Number(cell.colSpan) : 1;
                                    const rowSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.rowSpan))) ? Number(cell.rowSpan) : 1;
                                    return <th key={cellIndex} colSpan={colSpan} rowSpan={rowSpan} style={headerStyle}>{label}</th>;
                                })}
                            </tr>
                        )) : (
                            <tr>
                                {headers.map((header, headerIndex) => <th key={headerIndex} style={headerStyle}>{header}</th>)}
                            </tr>
                        )}
                    </thead>
                    <tbody>
                        {rows.map((row, rowIndex) => (
                            <tr key={rowIndex}>
                                {(Array.isArray(row) ? row : []).map((cell, cellIndex) => {
                                    const cellId = cell?.cell_id || `t${tableIndex}_r${rowIndex}_c${cellIndex}`;
                                    const editable = !readOnly && Boolean(cell?.editable);
                                    const headerLabel = String(headers[cellIndex] || '').toLowerCase();
                                    const textAlign = /(amount|salary|wage|gross|paye|pension|medical|uif|bonus|commission|overtime|bank)/.test(headerLabel) ? 'right' : 'center';
                                    const value = editable ? (cells[String(cellId)] ?? '') : (cell?.value || '');
                                    return (
                                        <td key={cellIndex} style={bodyStyle}>
                                            {editable ? (
                                                <input
                                                    value={value}
                                                    onChange={(e) => setAnswerValue({
                                                        ...ans,
                                                        cells: {
                                                            ...cells,
                                                            [String(cellId)]: e.target.value,
                                                        },
                                                    })}
                                                    style={{ width: '100%', padding: '6px', border: 'none', outline: 'none', boxSizing: 'border-box', textAlign, fontFamily: textAlign === 'right' ? 'ui-monospace, monospace' : 'inherit' }}
                                                />
                                            ) : (
                                                <div style={{ width: '100%', padding: '6px', boxSizing: 'border-box', textAlign, fontFamily: textAlign === 'right' ? 'ui-monospace, monospace' : 'inherit', color: /month/.test(headerLabel) ? '#6b7280' : '#111827' }}>
                                                    {cell?.value || ''}
                                                </div>
                                            )}
                                        </td>
                                    );
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        );
    };

    const renderPromptTables = () => {
        const promptTables = Array.isArray(question?.prompt_journals)
            ? question.prompt_journals
            : (question?.prompt_journal ? [question.prompt_journal] : []);
        if (!promptTables.length) return null;
        return (
            <div className="space-y-4">
                {promptTables.map((journal, idx) => (
                    <div key={`prompt-${idx}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">{journal?.heading || 'Source information'}</div>
                        {renderOneJournalTable(journal, -100 - idx, { readOnly: true })}
                    </div>
                ))}
            </div>
        );
    };

    const renderJournalTables = () => {
        const journals = Array.isArray(question?.journals)
            ? question.journals
            : (question?.journal ? [question.journal] : []);
        return (
            <div className="space-y-4">
                {journals.map((journal, idx) => (
                    <div key={`journal-${idx}`}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-800">{journal?.heading || 'Accounting table'}</div>
                        {renderOneJournalTable(journal, idx)}
                    </div>
                ))}
            </div>
        );
    };

    return (
        <div className="w-full">
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Scaffold Mode</h3>
            </div>

            {marking.markingError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {marking.markingError}
                </div>
            )}

            {!hideConfig && (
                <div className="grid grid-cols-1 lg:grid-cols-3 gap-4 mb-6">
                    <div className="lg:col-span-2">
                        <div className="flex flex-col sm:flex-row sm:items-end gap-3">
                            <div className="flex-1">
                                <label className="text-sm font-semibold text-slate-700">Subtopic</label>
                                <select
                                    value={g10AcctSWScaffoldStepIndex}
                                    onChange={(e) => {
                                        const idx = Number(e.target.value);
                                        setG10AcctSWScaffoldStepIndex(Number.isFinite(idx) ? idx : 0);
                                        setG10AcctSWScaffoldFeedback(null);
                                        setG10AcctSWScaffoldShowHint(false);
                                        setG10AcctSWScaffoldAnswer(null);
                                    }}
                                    className="mt-1 w-full p-2 border rounded-lg">
                                    {scaffoldSteps.map((s, i) => (
                                        <option key={s.key} value={i}>{s.title}</option>
                                    ))}
                                </select>
                            </div>
                            <div>
                                <label className="text-sm font-semibold text-slate-700">Difficulty</label>
                                <select
                                    value={g10AcctSWScaffoldDifficulty}
                                    onChange={(e) => {
                                        setG10AcctSWScaffoldDifficulty(e.target.value);
                                        setPendingDifficultyPromotion(null);
                                        setDifficultyNotice(`Difficulty set to ${e.target.value}.`);
                                    }}
                                    className="mt-1 p-2 border rounded-lg"
                                >
                                    <option value="easy">Easy</option>
                                    <option value="medium">Medium</option>
                                    <option value="hard">Hard</option>
                                </select>
                            </div>
                            <button
                                onClick={newExample}
                                className="px-4 py-2 bg-slate-900 text-white rounded-lg font-semibold hover:bg-slate-800"
                                disabled={g10AcctSWScaffoldLoading}
                            >
                                {g10AcctSWScaffoldLoading ? 'Loading…' : 'New Example'}
                            </button>
                        </div>
                        <div className="mt-3 flex flex-wrap items-center gap-3 text-sm">
                            <button
                                type="button"
                                onClick={() => {
                                    const nextValue = !keepCurrentDifficulty;
                                    setKeepCurrentDifficulty(nextValue);
                                    setPendingDifficultyPromotion(null);
                                    setDifficultyNotice(nextValue
                                        ? `Keep ${currentDifficulty} mode is on. Automatic promotion is paused.`
                                        : `Keep mode is off. Scaffold can auto-progress from ${currentDifficulty} after every 5 checked questions.`);
                                }}
                                className={`px-3 py-1.5 rounded-lg text-sm font-semibold border transition-colors ${keepCurrentDifficulty ? 'bg-amber-50 border-amber-300 text-amber-800 hover:bg-amber-100' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-100'}`}
                            >
                                {keepCurrentDifficulty ? `Keep ${currentDifficulty.charAt(0).toUpperCase()}${currentDifficulty.slice(1)} Mode` : 'Allow Auto Progression'}
                            </button>
                            <div className="text-xs text-slate-500">
                                {nextDifficulty
                                    ? `${attemptsTowardNextLevel}/5 checked ${currentDifficulty} scaffold questions toward ${nextDifficulty}.`
                                    : `You are on the highest scaffold difficulty for this subtopic.`}
                            </div>
                        </div>
                        {difficultyNotice && (
                            <div className="mt-3 text-sm text-indigo-800 bg-indigo-50 border border-indigo-200 rounded-lg px-3 py-2">
                                {difficultyNotice}
                            </div>
                        )}
                    </div>
                </div>
            )}

            {g10AcctSWScaffoldError && (
                <div className="mb-3 p-3 bg-red-50 border border-red-200 text-red-800 rounded-lg text-sm break-words">
                    {g10AcctSWScaffoldError}
                </div>
            )}

            {g10AcctSWScaffoldLoading && (
                <div className="text-sm text-slate-500">Loading...</div>
            )}

            {question && (
                <div className="space-y-4" onKeyDown={handleAnswerKeyDown}>

                    {question.question_type === 'mcq' && (
                        <div className="mt-3 grid grid-cols-1 gap-2">
                            {(question.options || []).map((opt, idx) => (
                                <MCQOption
                                    key={idx}
                                    selected={String(g10AcctSWScaffoldAnswer) === String(idx)}
                                    onClick={() => setAnswerValue(String(idx))}
                                    label={opt}
                                />
                            ))}
                        </div>
                    )}

                    {question.question_type === 'calc' && renderCalcInput()}

                    {question.question_type === 'typed' && (
                        <div className="mt-3">
                            <textarea
                                value={g10AcctSWScaffoldAnswer || ''}
                                onChange={(e) => setAnswerValue(e.target.value)}
                                placeholder="Write your answer..."
                                className="w-full min-h-[120px] p-3 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-slate-300"
                                title="Press Enter to check, or Shift+Enter for a new line."
                            />
                        </div>
                    )}

                    {question.question_type === 'table_wordbank' && renderWordbankTable()}

                    {(question.question_type === 'journal' || question.question_type === 'ledger') && renderPromptTables()}

                    {(question.question_type === 'journal' || question.question_type === 'ledger') && renderJournalTables()}

                    <div className="mt-4 flex flex-wrap gap-2">
                        {marking.isPracticeMode ? (
                            <>
                                <button
                                    type="button"
                                    onClick={checkAnswer}
                                    className="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-sm font-semibold transition-all"
                                >
                                    {g10AcctSWScaffoldFeedback ? 'Checked' : 'Check'}
                                </button>
                                <button
                                    type="button"
                                    onClick={() => setG10AcctSWScaffoldShowHint(!g10AcctSWScaffoldShowHint)}
                                    className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-xl text-sm font-semibold transition-all"
                                >
                                    Hint
                                </button>
                                {g10AcctSWScaffoldFeedback && ['typed', 'calc', 'table_wordbank'].includes(String(question?.question_type || '')) && (
                                    <button
                                        type="button"
                                        onClick={() => setShowMemo(!showMemo)}
                                        className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all border ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700' : 'bg-white border-slate-200 text-slate-800 hover:bg-slate-50'}`}
                                    >
                                        {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                    </button>
                                )}
                                <button
                                    type="button"
                                    onClick={() => {
                                        setG10AcctSWScaffoldFeedback(null);
                                        setShowMemo(false);
                                    }}
                                    className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-600 rounded-xl text-sm font-semibold transition-all"
                                >
                                    Clear feedback
                                </button>
                            </>
                        ) : (
                            !marking.isMarkingSubmitted && (
                                <button
                                    type="button"
                                    onClick={() => marking.submitAssessment([question])}
                                    disabled={marking.isSubmitting}
                                    className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors disabled:opacity-50"
                                >
                                    {marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}
                                </button>
                            )
                        )}
                    </div>

                    {g10AcctSWScaffoldShowHint && question?.question_type === 'typed' && typedHintSections.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Typed-answer hint</div>
                            <div className="mt-3 space-y-3 text-sm text-yellow-900">
                                {typedHintSections.map((section, idx) => (
                                    <div key={`${section.title}-${idx}`} className="space-y-1">
                                        <div className="font-semibold text-yellow-950">{section.title}</div>
                                        <div className="whitespace-pre-line">{section.text}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {g10AcctSWScaffoldShowHint && question?.question_type === 'calc' && calcHintText && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Calculation hint</div>
                            <div className="mt-2 text-sm text-yellow-900 whitespace-pre-line">{calcHintText}</div>
                        </div>
                    )}

                    {g10AcctSWScaffoldShowHint && question?.question_type === 'table_wordbank' && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Word-bank hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                {question.guidelines.map((item, idx) => (
                                    <li key={idx}>{item}</li>
                                ))}
                            </ul>
                        </div>
                    )}

                    {g10AcctSWScaffoldShowHint && (question?.question_type === 'journal' || question?.question_type === 'ledger') && Array.isArray(question?.guidelines) && question.guidelines.length > 0 && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Table hint</div>
                            <ul className="mt-2 list-disc pl-5 space-y-1 text-sm text-yellow-900">
                                {question.guidelines.map((item, idx) => (
                                    <li key={idx}>{item}</li>
                                ))}
                            </ul>
                        </div>
                    )}

                    {g10AcctSWScaffoldShowHint && question?.question_type !== 'typed' && question?.question_type !== 'calc' && question?.question_type !== 'table_wordbank' && marking.isPracticeMode && (
                        <div className="mt-3 p-3 bg-yellow-50 border border-yellow-200 text-yellow-900 rounded-xl text-sm">
                            Use the visual aids panel for formulas and key terms related to salaries, wages and deductions.
                        </div>
                    )}

                    {g10AcctSWScaffoldFeedback && marking.isPracticeMode && (
                        <div className={`mt-3 p-3 rounded-xl text-sm border ${g10AcctSWScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : g10AcctSWScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                            {g10AcctSWScaffoldFeedback.message}
                        </div>
                    )}

                    {question?.question_type === 'typed' && marking.isPracticeMode && (
                        <div className="mt-4 p-3 rounded-xl text-sm border bg-slate-50 border-slate-200 text-slate-600">
                            ⭐ AI-graded feedback available in Pro subscription
                        </div>
                    )}

                    {showMemo && question?.question_type === 'typed' && nonTabularHintItems.length > 0 && (
                        <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Sample answer</div>
                            <div className="mt-3 space-y-3 text-sm text-slate-700">
                                {nonTabularHintItems.map((item, itemIdx) => (
                                    <div key={`${item.label}-${itemIdx}`} className="space-y-1">
                                        <div className="font-semibold text-slate-900">{item.label}</div>
                                        <div className="whitespace-pre-line">{item.value}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'calc' && nonTabularHintItems.length > 0 && (
                        <div className="p-3 bg-indigo-50 border border-indigo-200 rounded-xl">
                            <div className="font-semibold text-indigo-900">Compare / Memo</div>
                            <div className="mt-3 space-y-3 text-sm text-indigo-900">
                                {nonTabularHintItems.map((item, itemIdx) => (
                                    <div key={`${item.label}-${itemIdx}`} className="space-y-1">
                                        <div className="font-semibold text-indigo-950">{item.label}</div>
                                        <div className="whitespace-pre-line">{item.value}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {showMemo && question?.question_type === 'table_wordbank' && wordbankMemoRows.length > 0 && (
                        <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Compare / Memo</div>
                            <div className="mt-3 space-y-3 text-sm text-slate-700">
                                {wordbankMemoRows.map((item, itemIdx) => (
                                    <div key={`${item.rowLabel}-${itemIdx}`} className="space-y-1">
                                        <div className="font-semibold text-slate-900">Row {item.rowLabel}</div>
                                        <div className="text-slate-600 whitespace-pre-line">{item.definition}</div>
                                        <div className="whitespace-pre-line">{item.answer}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}
                </div>
            )}

            {marking.isMarkingSubmitted && marking.markingResults && (
                <div className="mt-6 p-6 bg-indigo-50 border border-indigo-200 rounded-2xl">
                    <h4 className="text-xl font-bold text-indigo-900 mb-2">Assessment Results</h4>
                    <div className="flex items-end gap-2 mb-4">
                        <span className="text-4xl font-black text-indigo-700">
                            {Math.round((marking.markingResults.total_score / marking.markingResults.max_score) * 100)}%
                        </span>
                        <span className="text-sm font-medium text-indigo-600 mb-1">
                            ({marking.markingResults.total_score} / {marking.markingResults.max_score} marks)
                        </span>
                    </div>
                    {marking.getFeedbackForQuestion(question.id) && (
                        <div className={`mt-4 p-4 rounded-xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                            {marking.getFeedbackForQuestion(question.id).message}
                        </div>
                    )}
                </div>
            )}
        </div>
    );
};

export default Grade10AccountingSalariesWagesScaffold;

