import React, { useState, useEffect, useRef } from 'react';
import MCQOption from '../../../shared/MCQOption';
import EnhancedMathKeypad from '../../../../EnhancedMathKeypad';
import WordBankQuestionUI from '../../../shared/WordBankQuestionUI.jsx';
import MatchQuestionUI from '../../../shared/MatchQuestionUI.jsx';
import InlineFillQuestionUI from '../../../shared/InlineFillQuestionUI.jsx';

const normalizeText = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).trim().replace(/\s+/g, ' ').toLowerCase();
};

const toNumber = (value) => {
    if (value === null || value === undefined) return null;
    let s = String(value).trim();
    if (!s) return null;

    // South African-friendly parsing:
    // - Accept "2400", "2400.00", "2 400,00", "2,400.00"
    // - Allow either ',' or '.' as decimal separator
    // - Ignore spaces and thousands separators
    // - Strip currency symbols like R
    s = s.replace(/\s+/g, '');
    s = s.replace(/[Rr]/g, '');

    const lastDot = s.lastIndexOf('.');
    const lastComma = s.lastIndexOf(',');

    if (lastDot >= 0 && lastComma >= 0) {
        // If both are present, treat the last occurrence as the decimal separator
        const decSep = lastDot > lastComma ? '.' : ',';
        const thouSep = decSep === '.' ? ',' : '.';
        s = s.split(thouSep).join('');
        if (decSep === ',') s = s.replace(',', '.');
    } else if (lastComma >= 0) {
        // Only comma present -> decimal comma, remove any stray dots as thousands separators
        s = s.split('.').join('');
        s = s.replace(',', '.');
    } else {
        // Only dot (or neither) -> decimal dot, remove commas as thousands separators
        s = s.split(',').join('');
    }

    // Keep digits, one dot, and optional leading minus
    s = s.replace(/[^0-9.\-]/g, '');
    const n = Number(s);
    return Number.isFinite(n) ? n : null;
};

const numbersMatch = (actual, expected, { allowRoundedRand = false } = {}) => {
    const actualN = typeof actual === 'number' ? actual : toNumber(actual);
    const expectedN = typeof expected === 'number' ? expected : toNumber(expected);
    if (actualN === null || expectedN === null) return false;
    if (Math.abs(actualN - expectedN) <= 0.01) return true;
    if (allowRoundedRand && Math.round(actualN) === Math.round(expectedN)) return true;
    return false;
};

const clampHintPosition = (x, y, width = 320, height = 240) => {
    if (typeof window === 'undefined') return { x, y };
    const margin = 12;
    const maxX = Math.max(margin, window.innerWidth - width - margin);
    const maxY = Math.max(margin, window.innerHeight - height - margin);
    return {
        x: Math.min(Math.max(margin, x), maxX),
        y: Math.min(Math.max(margin, y), maxY),
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

const buildNonTabularHintItems = (question) => {
    const explicitItems = Array.isArray(question?.answer_part_hints) ? question.answer_part_hints : [];
    const normalizedExplicit = explicitItems
        .map((item, idx) => {
            const label = String(item?.label || `Answer part ${idx + 1}`).trim();
            const value = String(item?.value || '').trim();
            const sections = Array.isArray(item?.sections)
                ? item.sections.filter((section) => String(section?.text || '').trim())
                : [];
            return { label, value, sections };
        })
        .filter((item) => item.value || item.sections.length > 0);
    if (normalizedExplicit.length > 0) return normalizedExplicit;

    if (question?.question_type === 'calc') {
        const calcLines = String(question?.derivation_map?.value || '').split('\n').map((line) => line.trim()).filter(Boolean);
        return calcLines.map((line, idx) => ({
            label: `Step ${idx + 1}`,
            value: line,
            sections: buildHintSections(null, line),
        }));
    }

    const typedLines = String(question?.sample_answer || '').split('\n').map((line) => line.trim()).filter(Boolean);
    const guidelineSections = buildHintSections(null, (Array.isArray(question?.guidelines) ? question.guidelines.join('\n') : ''));
    return typedLines.map((line, idx) => ({
        label: `Memo point ${idx + 1}`,
        value: line,
        sections: guidelineSections.length > 0 ? guidelineSections : buildHintSections(null, line),
    }));
};

const buildEmptyJournalAnswer = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const out = {};
    journals.forEach((j) => {
        const rows = Array.isArray(j?.rows) ? j.rows : [];
        const titleFields = Array.isArray(j?.title_fields) ? j.title_fields : [];
        titleFields.forEach((tf) => {
            const id = tf?.cell_id;
            if (!id) return;
            out[String(id)] = '';
        });
        rows.forEach((row) => {
            (Array.isArray(row) ? row : []).forEach((cell) => {
                if (!cell?.cell_id) return;
                out[String(cell.cell_id)] = cell?.value || '';
            });
        });
    });
    return { cells: out, extra_rows_by_table: {} };
};

const getExpectedByCellId = (question) => (question?.correct_map && typeof question.correct_map === 'object') ? question.correct_map : {};

const isNumericExpected = (expected) => {
    if (expected === null || expected === undefined) return false;
    if (typeof expected === 'number') return true;
    const s = String(expected).trim();
    if (!s) return false;
    return /^-?\d+(?:\.\d+)?$/.test(s);
};

const journalTypeLabel = (journalTypeRaw) => {
    const jt = String(journalTypeRaw || '').trim().toLowerCase();
    if (!jt) return 'Table';
    if (jt === 'crj') return 'Cash Receipts Journal (CRJ)';
    if (jt === 'cpj') return 'Cash Payments Journal (CPJ)';
    if (jt === 'dj') return 'Debtors Journal (DJ)';
    if (jt === 'daj') return 'Debtors Allowances Journal (DAJ)';
    if (jt === 'cj') return 'Creditors Journal (CJ)';
    if (jt === 'caj') return 'Creditors Allowances Journal (CAJ)';
    if (jt === 'pcj') return 'Petty Cash Journal (PCJ)';
    if (jt === 'gj') return 'General Journal (GJ)';
    if (jt === 'trial_balance') return 'Trial Balance';
    if (jt === 'reference_trial_balance') return 'Reference Trial Balance';
    if (jt === 'general_ledger') return 'General Ledger';
    if (jt === 'debtors_ledger') return 'Debtors Ledger';
    if (jt === 'creditors_ledger') return 'Creditors Ledger';
    if (jt === 'trading_stock_account') return 'Trading Stock Account';
    if (jt === 'control_accounts') return 'Control Accounts';
    if (jt === 'control_accounts_reconciliation') return 'Control Accounts & Reconciliation';
    if (jt === 'reconciliation_analysis') return 'Reconciliation analysis';
    if (jt === 'control_account') return 'Control account';
    if (jt === 'list') return 'Debtors/Creditors list';
    if (jt === 'reconciliation_impact') return 'Reconciliation impact table';
    return jt.replace(/_/g, ' ');
};

const stripParenthetical = (value) => {
    if (value === null || value === undefined) return '';
    return String(value).replace(/\([^)]*\)/g, '').trim();
};

const getFirstParenthetical = (value) => {
    if (value === null || value === undefined) return null;
    const s = String(value);
    const m = s.match(/\(([^)]*)\)/);
    return m ? m[1] : null;
};

const evalBracketExpression = (expr) => {
    if (expr === null || expr === undefined) return null;
    const s = String(expr).trim();
    if (!s) return null;

    let total = 0;
    let sign = 1;
    let buf = '';

    const flush = () => {
        const n = toNumber(buf);
        if (n === null) return false;
        total += sign * n;
        buf = '';
        return true;
    };

    for (let i = 0; i < s.length; i += 1) {
        const ch = s[i];
        if (ch === '+' || ch === '-') {
            if (buf.trim().length > 0) {
                if (!flush()) return null;
            }
            sign = ch === '-' ? -1 : 1;
        } else {
            buf += ch;
        }
    }
    if (buf.trim().length > 0) {
        if (!flush()) return null;
    }
    return total;
};

const parseSignedTokenSet = (value) => {
    if (value === null || value === undefined) return null;
    const raw = String(value).trim();
    if (!raw) return null;
    // Split on common separators used by learners: slash, newline, comma, semicolon.
    const parts = raw.split(/[\/\n,;]+/g).map((p) => p.trim()).filter(Boolean);
    const tokens = new Set();
    parts.forEach((p) => {
        // Accept forms like +450, -450, ±450 (treated as both), +-450, -+450.
        const s = p.replace(/\s+/g, '');
        const m = s.match(/^([+\-±]{1,2})?(.+)$/);
        if (!m) return;
        const signRaw = m[1] || '';
        const numRaw = m[2] || '';
        const n = toNumber(numRaw);
        if (n === null) return;
        const amt = Math.abs(n);
        if (signRaw.includes('±') || signRaw === '+-' || signRaw === '-+') {
            tokens.add(`+${amt.toFixed(2)}`);
            tokens.add(`-${amt.toFixed(2)}`);
            return;
        }
        const sign = signRaw.startsWith('-') ? '-' : '+';
        tokens.add(`${sign}${amt.toFixed(2)}`);
    });
    return tokens.size ? tokens : null;
};

const isMultiValueExpected = (expected) => {
    if (expected === null || expected === undefined) return false;
    const s = String(expected);
    // Heuristic: multi-value cells include a separator and at least one sign.
    return (s.includes('/') || s.includes('\n')) && /[+\-±]/.test(s);
};

const isControlAccountsReconciliationQuestion = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const types = new Set(['control_accounts_reconciliation', 'control_account', 'list', 'reconciliation_impact']);
    return journals.some((j) => types.has(String(j?.journal_type || '').toLowerCase()));
};

const isTotalsRow = (row) => {
    if (!Array.isArray(row) || row.length === 0) return false;
    const getVal = (i) => String(row?.[i]?.value ?? '').trim().toLowerCase();
// Heuristic: totals rows are usually labeled in Doc or Details.
return getVal(0) === 'total' || getVal(0) === 'totals' || getVal(2) === 'total' || getVal(2) === 'totals';
};

const TRIAL_BALANCE_SECTION_LABELS = new Set(['balance sheet accounts', 'nominal accounts']);

const getTrialBalanceCellTextAlign = ({ journalType, headers, row, colIndex }) => {
    if (String(journalType || '').toLowerCase() !== 'trial_balance') return undefined;
    const headerLabel = String(headers?.[colIndex] ?? '').trim().toLowerCase();
    if (headerLabel === 'fol.' || headerLabel === 'fol') return 'center';
    if (headerLabel === 'debit' || headerLabel === 'credit') return 'right';
    if (colIndex !== 0) return undefined;
    const firstCellValue = String(row?.[0]?.value ?? '').trim().toLowerCase();
    return TRIAL_BALANCE_SECTION_LABELS.has(firstCellValue) ? 'left' : 'center';
};

const Grade10AccountingSoleTraderPractice = ({
    onBack,
    g10AcctSTVisualAidsOpen,
    setG10AcctSTVisualAidsOpen,
    g10AcctSTPracticeDifficulty,
    setG10AcctSTPracticeDifficulty,
    g10AcctSTPracticeSubskill,
    setG10AcctSTPracticeSubskill,
    g10AcctSTPracticeSeed,
    setG10AcctSTPracticeSeed,
    subskills,
    fetchGrade10AcctSTPractice,
    g10AcctSTPracticeLoading,
    g10AcctSTPracticeError,
    g10AcctSTPracticeQuestions,
    g10AcctSTPracticeAnswers,
    setG10AcctSTPracticeAnswers,
    g10AcctSTPracticeFeedback,
    setG10AcctSTPracticeFeedback,
    renderGrade10AcctSTVisualAids,
    hideConfig,
    isSuperAdmin,
}) => {
    const questions = Array.isArray(g10AcctSTPracticeQuestions) ? g10AcctSTPracticeQuestions : [];
    const [currentIndex, setCurrentIndex] = useState(0);
    const [reviewMode, setReviewMode] = useState(false);
    const [activeReviewMemoIndex, setActiveReviewMemoIndex] = useState(null);
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [showHintsByQuestion, setShowHintsByQuestion] = useState({});
    const [elapsedSecondsByIndex, setElapsedSecondsByIndex] = useState({});
    const [liveElapsedSeconds, setLiveElapsedSeconds] = useState(0);
    const attemptStartTimeRef = useRef(null);
    const timerIntervalRef = useRef(null);
    const cellHintPopupRef = useRef(null);

    const [adminFormat, setAdminFormat] = useState('mixed');

    const activeInputRef = useRef(null);
    const [isKeypadVisible, setIsKeypadVisible] = useState(false);

    const FLAG_KEY = `g10_acct_st_flagged_${g10AcctSTPracticeSubskill || 'mixed'}`;
    const [flaggedIds, setFlaggedIds] = useState(() => {
        try { return new Set(JSON.parse(localStorage.getItem(FLAG_KEY) || '[]')); } 
        catch { return new Set(); }
    });

    const flagQuestion = (qId) => {
        setFlaggedIds(prev => {
            const next = new Set(prev);
            next.add(qId);
            localStorage.setItem(FLAG_KEY, JSON.stringify([...next]));
            return next;
        });
    };

    const unflagQuestion = (qId) => {
        setFlaggedIds(prev => {
            const next = new Set(prev);
            next.delete(qId);
            localStorage.setItem(FLAG_KEY, JSON.stringify([...next]));
            return next;
        });
    };

    useEffect(() => {
        setCurrentIndex(0);
        setReviewMode(false);
        setActiveReviewMemoIndex(null);
        setActiveCellHint(null);
        setShowHintsByQuestion({});
        setElapsedSecondsByIndex({});
        setLiveElapsedSeconds(0);
        setIsKeypadVisible(false);
        setG10AcctSTPracticeFeedback([]);
    }, [questions]);

    useEffect(() => {
        if (!activeCellHint || !cellHintPopupRef.current) return;
        const width = cellHintPopupRef.current.offsetWidth || 320;
        const height = cellHintPopupRef.current.offsetHeight || 240;
        const next = clampHintPosition(activeCellHint.x, activeCellHint.y, width, height);
        if (next.x !== activeCellHint.x || next.y !== activeCellHint.y) {
            setActiveCellHint((prev) => (prev ? { ...prev, x: next.x, y: next.y } : prev));
        }
    }, [activeCellHint]);

    useEffect(() => {
        if (!questions.length) {
            setCurrentIndex(0);
            return;
        }
        if (currentIndex > questions.length - 1) {
            setCurrentIndex(questions.length - 1);
        }
    }, [currentIndex, questions.length]);

    useEffect(() => {
        if (timerIntervalRef.current) {
            clearInterval(timerIntervalRef.current);
            timerIntervalRef.current = null;
        }

        if (reviewMode || !questions[currentIndex]) {
            attemptStartTimeRef.current = null;
            setLiveElapsedSeconds(elapsedSecondsByIndex[currentIndex] || 0);
            return;
        }

        const baseSeconds = elapsedSecondsByIndex[currentIndex] || 0;
        const startedAt = Date.now();
        attemptStartTimeRef.current = startedAt;
        setLiveElapsedSeconds(baseSeconds);
        timerIntervalRef.current = setInterval(() => {
            setLiveElapsedSeconds(baseSeconds + Math.floor((Date.now() - startedAt) / 1000));
        }, 1000);

        return () => {
            if (timerIntervalRef.current) {
                clearInterval(timerIntervalRef.current);
                timerIntervalRef.current = null;
            }
            const spentSeconds = baseSeconds + Math.floor((Date.now() - startedAt) / 1000);
            setElapsedSecondsByIndex(prev => prev[currentIndex] === spentSeconds ? prev : {
                ...prev,
                [currentIndex]: spentSeconds,
            });
        };
    }, [currentIndex, reviewMode, questions]);

    const handleNext = () => {
        if (!reviewMode && currentIndex < questions.length - 1) {
            setCurrentIndex((prev) => prev + 1);
        }
    };

    const handlePrev = () => {
        if (!reviewMode && currentIndex > 0) {
            setCurrentIndex((prev) => prev - 1);
        }
    };

    const ALL_KEYS = new Set(['mixed']);
    const FINANCIAL_ACCOUNTING_KEYS = new Set(['concepts', 'accounting_cycle']);
    const ACCOUNTING_EQUATION_KEYS = new Set(['equation']);
    const BOOKKEEPING_KEYS = new Set([
        'journals', 'crj', 'cpj', 'dj', 'daj', 'cj', 'caj', 'pcj', 'gj',
        'general_ledger', 'debtors_ledger', 'creditors_ledger',
        'trial_balance',
        'full_accounting_cycle_bookkeeping',
        'trading_stock_account',
        'control_accounts', 'control_accounts_reconciliation', 'reconciliation_analysis',
    ]);

    const allSubskills = Array.isArray(subskills) ? subskills : [];
    const allGroup = allSubskills.filter((s) => ALL_KEYS.has(s.key));
    const financialGroup = allSubskills.filter((s) => FINANCIAL_ACCOUNTING_KEYS.has(s.key));
    const equationGroup = allSubskills.filter((s) => ACCOUNTING_EQUATION_KEYS.has(s.key));
    const bookkeepingGroup = allSubskills.filter((s) => BOOKKEEPING_KEYS.has(s.key));

    const setAnswer = (idx, value) => {
        const answers = Array.isArray(g10AcctSTPracticeAnswers) ? [...g10AcctSTPracticeAnswers] : [];
        answers[idx] = value;
        setG10AcctSTPracticeAnswers(answers);

        const feedback = Array.isArray(g10AcctSTPracticeFeedback) ? [...g10AcctSTPracticeFeedback] : [];
        feedback[idx] = null;
        setG10AcctSTPracticeFeedback(feedback);
    };

    const buildReviewResult = ({
        kind,
        message,
        isCorrect,
        correctCount,
        totalCount,
        wrongCells = [],
        cellResults = {},
    }) => ({
        kind,
        message,
        isCorrect,
        correctCount,
        totalCount,
        wrongCount: Math.max(0, (Number(totalCount) || 0) - (Number(correctCount) || 0)),
        wrongCells,
        cellResults,
    });

    const evaluateQuestion = (q, userValue) => {
        if (!q) {
            return buildReviewResult({
                kind: 'error',
                message: 'Unable to review this answer.',
                isCorrect: false,
                correctCount: 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'mcq') {
            const ok = String(userValue) === String(q.correct_index);
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok
                    ? '0 of 1 responses incorrect.'
                    : `1 of 1 responses incorrect. Correct answer: ${q.options?.[q.correct_index] || ''}`,
                isCorrect: ok,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'typed') {
            const ok = normalizeText(userValue).length > 0;
            return buildReviewResult({
                kind: ok ? 'info' : 'error',
                message: ok
                    ? '0 of 1 responses missing. Compare with the memo below.'
                    : '1 of 1 responses missing. Write an answer first.',
                isCorrect: ok ? null : false,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'calc') {
            const userN = toNumber(userValue);
            if (userN === null) {
                return buildReviewResult({
                    kind: 'error',
                    message: '1 of 1 responses incorrect. Enter a number first.',
                    isCorrect: false,
                    correctCount: 0,
                    totalCount: 1,
                });
            }
            const correct = Number(q.correct_value);
            const ok = Number.isFinite(correct) && numbersMatch(userN, correct, {
                allowRoundedRand: String(q.unit || '').toUpperCase().includes('R'),
            });
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok
                    ? '0 of 1 responses incorrect.'
                    : `1 of 1 responses incorrect. Correct answer: ${q.unit || ''}${correct.toFixed(2)}`,
                isCorrect: ok,
                correctCount: ok ? 1 : 0,
                totalCount: 1,
            });
        }

        if (q.question_type === 'match') {
            const expectedMap = q.correct_map || {};
            const userMap = (userValue && typeof userValue === 'object') ? userValue : {};
            let hit = 0;
            let total = 0;
            for (const [lId, rId] of Object.entries(expectedMap)) {
                total++;
                if (userMap[lId] === rId) hit++;
            }
            const ok = hit === total && total > 0;
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok
                    ? `0 of ${total} responses incorrect.`
                    : `${total - hit} of ${total} responses incorrect.`,
                isCorrect: ok,
                correctCount: hit,
                totalCount: total,
            });
        }

        if (q.question_type === 'word_bank' || q.question_type === 'inline_fill') {
            const expectedMap = q.correct_map || {};
            const userMap = (userValue && typeof userValue === 'object') ? userValue : {};
            let hit = 0;
            let total = 0;
            for (const [bId, ans] of Object.entries(expectedMap)) {
                total++;
                if (normalizeText(userMap[bId]) === normalizeText(ans)) hit++;
            }
            const ok = hit === total && total > 0;
            return buildReviewResult({
                kind: ok ? 'success' : 'error',
                message: ok
                    ? `0 of ${total} responses incorrect.`
                    : `${total - hit} of ${total} responses incorrect.`,
                isCorrect: ok,
                correctCount: hit,
                totalCount: total,
            });
        }

        if (q.question_type === 'journal' || q.question_type === 'ledger') {
            const expectedMap = getExpectedByCellId(q);
            const ans = (userValue && typeof userValue === 'object') ? userValue : buildEmptyJournalAnswer(q);
            const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
            const keys = Object.keys(expectedMap);

            const allowBracketWorkings = isControlAccountsReconciliationQuestion(q);
            const workingMap = (q?.working_map && typeof q.working_map === 'object') ? q.working_map : {};

            let total = 0;
            let hit = 0;
            const wrong = [];
            const cellResults = {};
            keys.forEach((cellId) => {
                const expected = expectedMap[cellId];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = cells[cellId];
                let matched = false;

                if (Array.isArray(expected)) {
                    const gotNorm = normalizeText(got);
                    matched = expected.some((x) => normalizeText(x) === gotNorm);
                } else if (isNumericExpected(expected)) {
                    const gotN = toNumber(got);
                    const expN = typeof expected === 'number' ? expected : toNumber(expected);
                    matched = gotN !== null && expN !== null && numbersMatch(gotN, expN, { allowRoundedRand: true });
                } else if (isMultiValueExpected(expected)) {
                    const expSet = parseSignedTokenSet(expected);
                    const gotSet = parseSignedTokenSet(got);
                    matched = Boolean(expSet && gotSet && expSet.size === gotSet.size && Array.from(expSet).every((x) => gotSet.has(x)));
                } else if (allowBracketWorkings) {
                    const linkedAmountCellId = workingMap?.[cellId];
                    if (linkedAmountCellId) {
                        const outside = stripParenthetical(got);
                        const inner = getFirstParenthetical(got);
                        const expectedAmount = expectedMap?.[linkedAmountCellId];
                        const expectedAmountN = toNumber(expectedAmount);
                        const innerTotal = evalBracketExpression(inner);

                        const hasParens = inner !== null && inner !== undefined && String(inner).trim().length > 0;
                        const outsideOk = normalizeText(outside) === normalizeText(expected);
                        const workingOk = expectedAmountN !== null && innerTotal !== null && numbersMatch(innerTotal, expectedAmountN, { allowRoundedRand: true });
                        matched = hasParens && outsideOk && workingOk;
                        if (!matched) {
                            wrong.push({ cellId, expected: `${expected} (show working in brackets that totals to ${expectedAmount})`, got });
                        }
                    } else {
                        const gotNoBrackets = stripParenthetical(got);
                        matched = normalizeText(gotNoBrackets) === normalizeText(expected);
                    }
                } else {
                    matched = normalizeText(got) === normalizeText(expected);
                }

                if (matched) {
                    hit += 1;
                } else if (!(allowBracketWorkings && workingMap?.[cellId])) {
                    wrong.push({ cellId, expected, got });
                }

                cellResults[cellId] = {
                    correct: matched,
                    expected,
                    userValue: got,
                };
            });

            if (!total) {
                return buildReviewResult({
                    kind: 'error',
                    message: 'Nothing to mark for this journal question.',
                    isCorrect: false,
                    correctCount: 0,
                    totalCount: 0,
                });
            }

            if (hit === total) {
                return buildReviewResult({
                    kind: 'success',
                    message: `0 of ${total} cells incorrect.`,
                    isCorrect: true,
                    correctCount: hit,
                    totalCount: total,
                    cellResults,
                });
            }

            const details = wrong
                .slice(0, 12)
                .map((w) => {
                    const exp = Array.isArray(w.expected) ? w.expected.join(' / ') : String(w.expected);
                    const gotStr = (w.got === null || w.got === undefined || String(w.got).trim() === '') ? '(blank)' : String(w.got);
                    return `${w.cellId}: expected ${exp} (you entered ${gotStr})`;
                })
                .join('\n');

            return buildReviewResult({
                kind: 'error',
                message: `${total - hit} of ${total} cells incorrect.${details ? `\n\nIncorrect cells:\n${details}` : ''}`,
                isCorrect: false,
                correctCount: hit,
                totalCount: total,
                wrongCells: wrong,
                cellResults,
            });
        }

        return buildReviewResult({
            kind: 'error',
            message: 'Unsupported question type.',
            isCorrect: false,
            correctCount: 0,
            totalCount: 1,
        });
    };

    const handleFinishAndReview = () => {
        const answers = Array.isArray(g10AcctSTPracticeAnswers) ? g10AcctSTPracticeAnswers : [];
        const feedback = questions.map((question, idx) => {
            const result = evaluateQuestion(question, answers[idx]);
            if (question?.id) {
                if (result?.isCorrect === true) unflagQuestion(question.id);
                else if (result?.isCorrect === false) flagQuestion(question.id);
            }
            return result;
        });
        setG10AcctSTPracticeFeedback(feedback);
        setActiveReviewMemoIndex(null);
        setActiveCellHint(null);
        setShowHintsByQuestion({});
        setIsKeypadVisible(false);
        setReviewMode(true);
    };

    const renderOneJournalTable = ({ journal, q, idx, tableIndex = 0, showHighlights = false, memoEnabled = false, readOnlyMode = false, isReference = false }) => {
        const headers = Array.isArray(journal?.headers) ? journal.headers : [];
        const titleFields = Array.isArray(journal?.title_fields) ? journal.title_fields : [];
        const headerRowsRaw = Array.isArray(journal?.header_rows) ? journal.header_rows : null;
        const headerRows = Array.isArray(headerRowsRaw)
            ? headerRowsRaw
                .map((row) => Array.isArray(row) ? row : [])
                .filter((row) => row.length > 0)
            : [];
        const baseRows = Array.isArray(journal?.rows) ? journal.rows : [];

        const allowExtraRows = journal?.allow_extra_rows === true;
        const cellHints = (q?.cell_hints && typeof q.cell_hints === 'object') ? q.cell_hints : {};
        const cellTeachingMap = (q?.cell_teaching_map && typeof q.cell_teaching_map === 'object') ? q.cell_teaching_map : {};
        const reviewResult = Array.isArray(g10AcctSTPracticeFeedback) ? g10AcctSTPracticeFeedback[idx] : null;
        const cellResults = (reviewResult?.cellResults && typeof reviewResult.cellResults === 'object') ? reviewResult.cellResults : {};
        const hintsEnabled = reviewMode && showHintsByQuestion[idx] === true && reviewResult?.kind !== 'success';

        const ans = (g10AcctSTPracticeAnswers?.[idx] && typeof g10AcctSTPracticeAnswers[idx] === 'object')
            ? g10AcctSTPracticeAnswers[idx]
            : buildEmptyJournalAnswer(q);
        const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
        const extraRowsByTable = (ans?.extra_rows_by_table && typeof ans.extra_rows_by_table === 'object') ? ans.extra_rows_by_table : {};
        const extraRows = Array.isArray(extraRowsByTable[String(tableIndex)]) ? extraRowsByTable[String(tableIndex)] : [];

        const maybeTotals = baseRows.length > 0 ? baseRows[baseRows.length - 1] : null;
        const hasTotals = isTotalsRow(maybeTotals);
        const totalsRow = hasTotals ? maybeTotals : null;
        const bodyRows = hasTotals ? baseRows.slice(0, baseRows.length - 1) : baseRows;
        const rows = totalsRow ? [...bodyRows, ...extraRows, totalsRow] : [...bodyRows, ...extraRows];

        const setCell = (cellId, value) => {
            setAnswer(idx, {
                ...ans,
                cells: {
                    ...cells,
                    [String(cellId)]: value,
                },
            });
        };

        const openCellHint = (cellId, label, text, sections, triggerEl) => {
            const rect = triggerEl?.getBoundingClientRect?.();
            const anchorX = rect ? rect.left : 24;
            const anchorY = rect ? rect.bottom + 10 : 24;
            const next = clampHintPosition(anchorX, anchorY, 320, 240);
            setActiveCellHint((prev) => {
                if (prev?.cellId === cellId && prev?.questionIndex === idx) return null;
                return {
                    questionIndex: idx,
                    cellId,
                    label,
                    text,
                    sections,
                    x: next.x,
                    y: next.y,
                    anchorX,
                    anchorY,
                };
            });
        };

        const addRow = () => {
            const totalCols = headers.length;
            if (!totalCols) return;

            const newRowIndex = bodyRows.length + extraRows.length;
            const newRow = Array.from({ length: totalCols }).map((_, cIdx) => ({
                cell_id: `t${tableIndex}_r${newRowIndex}_c${cIdx}`,
                value: '',
                editable: true,
            }));

            setAnswer(idx, {
                ...ans,
                extra_rows_by_table: {
                    ...extraRowsByTable,
                    [String(tableIndex)]: [...extraRows, newRow],
                },
            });
        };

        const tableMinWidthPx = Math.max(headers.length * 112, 720);
        const journalTableStyle = { width: '100%', minWidth: `${tableMinWidthPx}px`, borderCollapse: 'collapse', tableLayout: 'fixed' };
        const journalHeaderCellStyle = { border: '1px solid #000', padding: '6px', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', fontSize: '0.75rem', minWidth: '7rem', verticalAlign: 'middle' };
        const journalBodyCellStyle = { border: '1px solid #000', padding: 0, verticalAlign: 'top', position: 'relative', minWidth: '7rem' };
        const autoResizeJournalTextarea = (node) => {
            if (!node) return;
            node.style.height = 'auto';
            node.style.height = `${Math.max(node.scrollHeight, 36)}px`;
        };

        return (
            <div className="mt-3 overflow-x-auto" style={{ WebkitOverflowScrolling: 'touch' }}>
                {titleFields.length > 0 && (
                    <div className="mb-3 grid grid-cols-1 md:grid-cols-2 gap-3">
                        {titleFields.map((tf) => {
                            const id = tf?.cell_id;
                            if (!id) return null;
                            const label = String(tf?.label || id);
                            const value = isReference ? (tf?.value ?? '') : (cells[String(id)] ?? '');
                            return (
                                <label key={id} className="block">
                                    <div className="text-xs font-semibold text-gray-700 mb-1">{label}</div>
                                    <input
                                        value={value}
                                        onChange={(e) => {
                                            if (!readOnlyMode) setCell(id, e.target.value);
                                        }}
                                        className="w-full p-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-400"
                                        placeholder=""
                                        readOnly={readOnlyMode}
                                    />
                                </label>
                            );
                        })}
                    </div>
                )}

                {allowExtraRows && !readOnlyMode && (
                    <div style={{ marginBottom: '8px' }}>
                        <button
                            type="button"
                            onClick={addRow}
                            style={{ padding: '6px 12px', border: '1px solid #000', background: 'white', cursor: 'pointer', fontWeight: 600 }}
                        >
                            + Add row
                        </button>
                    </div>
                )}

                <table style={journalTableStyle}>
                    <thead>
                        {headerRows.length > 0 ? (
                            headerRows.map((row, rIdx) => (
                                <tr key={rIdx}>
                                    {row.map((cell, cIdx) => {
                                        const label = (cell && typeof cell === 'object') ? cell.label : String(cell ?? '');
                                        const colSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.colSpan))) ? Number(cell.colSpan) : 1;
                                        const rowSpan = (cell && typeof cell === 'object' && Number.isFinite(Number(cell.rowSpan))) ? Number(cell.rowSpan) : 1;
                                        return (
                                            <th
                                                key={cIdx}
                                                colSpan={colSpan}
                                                rowSpan={rowSpan}
                                                style={journalHeaderCellStyle}
                                            >
                                                {label}
                                            </th>
                                        );
                                    })}
                                </tr>
                            ))
                        ) : (
                            <tr>
                                {headers.map((h, hIdx) => (
                                    <th key={hIdx} style={journalHeaderCellStyle}>
                                        {h}
                                    </th>
                                ))}
                            </tr>
                        )}
                    </thead>
                    <tbody>
                        {rows.map((row, rIdx) => (
                            <tr key={rIdx}>
                                {(Array.isArray(row) ? row : []).map((cell, cIdx) => {
                                    const cellId = cell?.cell_id || `t${tableIndex}_r${rIdx}_c${cIdx}`;
                                    const value = isReference ? (cell?.value || '') : (cells[String(cellId)] ?? (cell?.value || ''));
                                    const editable = isReference ? false : Boolean(cell?.editable);
                                    const displayValue = value;

                                    const expectedMap = getExpectedByCellId(q);
                                    const derivationMap = q?.derivation_map || {};
                                    const expected = expectedMap[cellId];
                                    const result = cellResults[cellId];
                                    const rowHintKey = `t${tableIndex}_r${rIdx}_c0`;
                                    const rowHint = String(cellHints[rowHintKey] || '').trim();
                                    const exactCellHint = String(cellHints[cellId] || '').trim();
                                    const derivationHint = String(derivationMap[cellId] || '').trim();
                                    const hintParts = [];
                                    if (exactCellHint) hintParts.push(exactCellHint);
                                    else if (rowHint) hintParts.push(rowHint);
                                    if (derivationHint) hintParts.push(derivationHint);
                                    const cellHintText = hintParts.join('\n\n').trim();
                                    const teachingHint = cellTeachingMap[cellId];
                                    const cellHintSections = buildHintSections(teachingHint, cellHintText);
                                    const cellHintLabel = String(headers[cIdx] || cellId);
                                    
                                    let cellBorder = 'none';
                                    let cellBg = '';
                                    let isIncorrect = false;

                                    if (showHighlights && editable && expected !== undefined) {
                                        let hit = Boolean(result?.correct);
                                        if (!result) {
                                            const got = value;
                                            if (normalizeText(got) === normalizeText(expected)) hit = true;
                                            else if (isNumericExpected(expected) && numbersMatch(got, (typeof expected === 'number' ? expected : toNumber(expected)), { allowRoundedRand: true })) hit = true;
                                        }
                                        
                                        if (!hit && String(value).trim() !== String(expected).trim()) {
                                            cellBorder = '2px solid #ef4444';
                                            cellBg = '#fef2f2';
                                            isIncorrect = true;
                                        } else if (hit && String(value).trim() !== '') {
                                            cellBorder = '2px solid #10b981';
                                            cellBg = '#ecfdf5';
                                        }
                                    }

                                    const isActiveMemo = memoEnabled && isIncorrect && editable;
                                    const finalInputVal = Array.isArray(isActiveMemo ? expected : value)
                                        ? (isActiveMemo ? expected : value).join(' / ')
                                        : (isActiveMemo ? expected : value);
                                    const memoTooltip = derivationMap[cellId] || `Expected: ${expected}`;
                                    const showCellHintButton = hintsEnabled && editable && isIncorrect && cellHintSections.length > 0;
                                    const cellTextAlign = getTrialBalanceCellTextAlign({
                                        journalType: journal?.journal_type,
                                        headers,
                                        row,
                                        colIndex: cIdx,
                                    });

                                    return (
                                        <td key={cIdx} style={journalBodyCellStyle}>
                                            {editable ? (
                                                <div className="relative group/memo h-full w-full flex items-stretch">
                                                    <textarea
                                                        ref={autoResizeJournalTextarea}
                                                        value={finalInputVal}
                                                        onChange={(e) => {
                                                            if (!readOnlyMode) setCell(cellId, e.target.value);
                                                            autoResizeJournalTextarea(e.target);
                                                        }}
                                                        onInput={(e) => autoResizeJournalTextarea(e.target)}
                                                        rows={1}
                                                        style={{ width: '100%', minHeight: '2.25rem', padding: '6px', border: cellBorder, outline: 'none', boxSizing: 'border-box', textAlign: cellTextAlign || 'center', fontSize: '0.875rem', backgroundColor: cellBg, resize: 'none', overflow: 'hidden', whiteSpace: 'pre-wrap', overflowWrap: 'anywhere', wordBreak: 'break-word' }}
                                                        placeholder=""
                                                        readOnly={readOnlyMode || memoEnabled}
                                                    />
                                                    {showCellHintButton && (
                                                        <button
                                                            type="button"
                                                            onClick={(e) => {
                                                                e.preventDefault();
                                                                e.stopPropagation();
                                                                openCellHint(cellId, cellHintLabel, cellHintText, cellHintSections, e.currentTarget);
                                                            }}
                                                            className="absolute top-1 right-1 inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-yellow-300 text-yellow-800 bg-yellow-50 hover:bg-yellow-100"
                                                            aria-label={`Hint: ${cellHintLabel}`}
                                                        >
                                                            i
                                                        </button>
                                                    )}
                                                    {isActiveMemo && (
                                                        <div className="absolute opacity-0 pointer-events-none group-hover/memo:opacity-100 transition-opacity z-50 bottom-full mb-1 left-1/2 -translate-x-1/2 w-48 p-2 bg-indigo-900 text-white text-xs rounded-lg shadow-xl text-center">
                                                           {memoTooltip}
                                                           <div className="absolute top-full left-1/2 -translate-x-1/2 w-2 h-2 bg-indigo-900 rotate-45 -mt-1"></div>
                                                        </div>
                                                    )}
                                                </div>
                                            ) : (
                                                <div style={{ padding: '6px', minHeight: '2.25rem', fontSize: '0.875rem', color: '#1f2937', fontStyle: 'normal', whiteSpace: 'pre-wrap', overflowWrap: 'anywhere', wordBreak: 'break-word', textAlign: cellTextAlign }}>{displayValue}</div>
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

    const openNonTabularHint = ({ idx, hintKey, label, sections, triggerEl }) => {
        if (!Array.isArray(sections) || sections.length === 0) return;
        const rect = triggerEl?.getBoundingClientRect?.();
        const anchorX = rect ? rect.left : 24;
        const anchorY = rect ? rect.bottom + 10 : 24;
        const next = clampHintPosition(anchorX, anchorY, 320, 240);
        const cellId = `memo_${idx}_${hintKey}`;
        setActiveCellHint((prev) => {
            if (prev?.cellId === cellId && prev?.questionIndex === idx) return null;
            return {
                questionIndex: idx,
                cellId,
                label,
                text: '',
                sections,
                x: next.x,
                y: next.y,
                anchorX,
                anchorY,
            };
        });
    };

    const renderJournal = (q, idx, options = {}) => {
        const journals = Array.isArray(q?.journals)
            ? q.journals
            : (q?.journal ? [q.journal] : []);

        return (
            <div>
                {journals.map((j, tIdx) => (
                    <div key={tIdx}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-gray-800">
                            {j?.heading || journalTypeLabel(j?.journal_type)}
                        </div>
                        {renderOneJournalTable({
                            journal: j,
                            q,
                            idx,
                            tableIndex: tIdx,
                            isLastTable: tIdx === journals.length - 1,
                            showHighlights: options.showHighlights === true,
                            memoEnabled: options.memoEnabled === true,
                            readOnlyMode: options.readOnlyMode === true || j?.journal_type === 'reference_trial_balance',
                            isReference: false,
                        })}
                    </div>
                ))}
            </div>
        );
    };

    const renderPromptTables = (question, idx) => {
        const promptJournals = Array.isArray(question?.prompt_journals)
            ? question.prompt_journals
            : (question?.prompt_journal ? [question.prompt_journal] : []);
        if (!promptJournals.length) return null;

        return (
            <div className="mb-6">
                {promptJournals.map((journal, promptIdx) => (
                    <div key={`prompt-${promptIdx}`} className="mb-4 last:mb-0">
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">
                            {journal?.heading || journal?.header_rows?.[0]?.[0]?.label || 'Source information'}
                        </div>
                        {renderOneJournalTable({
                            journal,
                            q: question,
                            idx,
                            tableIndex: -100 - promptIdx,
                            readOnlyMode: true,
                            isReference: true,
                        })}
                    </div>
                ))}
            </div>
        );
    };

    const q = questions[currentIndex];

    const renderCellHintPopupContent = (hint) => {
        const sections = Array.isArray(hint?.sections) ? hint.sections : [];
        return (
            <div className="p-3 max-h-[60vh] overflow-y-auto leading-snug space-y-3">
                {sections.map((section, idx) => (
                    <div key={`${section.title}-${idx}`} className="space-y-1">
                        <div className="font-semibold text-yellow-950">{section.title}</div>
                        <div className="text-yellow-900 whitespace-pre-line">{section.text}</div>
                    </div>
                ))}
            </div>
        );
    };

    const formatElapsedTime = (seconds) => {
        const safeSeconds = Math.max(0, Number.isFinite(Number(seconds)) ? Math.floor(Number(seconds)) : 0);
        const minutes = Math.floor(safeSeconds / 60);
        const remainingSeconds = safeSeconds % 60;
        return minutes > 0
            ? `${minutes}m ${String(remainingSeconds).padStart(2, '0')}s`
            : `${remainingSeconds}s`;
    };

    const getQuestionPrompt = (question) => {
        const raw = question?.question_text || question?.prompt || question?.question || '';
        return String(raw).trim();
    };

    const renderQuestionContent = (question, idx, options = {}) => {
        const showHighlights = options.showHighlights === true;
        const memoEnabled = options.memoEnabled === true;
        const readOnlyMode = options.readOnlyMode === true;
        const questionAnswer = g10AcctSTPracticeAnswers?.[idx];
        const freezeInteractions = readOnlyMode && !memoEnabled;

        if (question.question_type === 'mcq') {
            return (
                <div className="grid grid-cols-1 gap-2">
                    {(Array.isArray(question.options) ? question.options : []).map((opt, oIdx) => {
                        const isSelected = String(questionAnswer) === String(oIdx);
                        const isCorrect = String(question.correct_index) === String(oIdx);
                        let overrideStyle = '';
                        if (showHighlights && isSelected && !isCorrect) overrideStyle = 'ring-2 ring-red-500 bg-red-50 rounded-xl';
                        if (showHighlights && isCorrect) overrideStyle = 'ring-2 ring-emerald-500 bg-emerald-50 rounded-xl';
                        return (
                            <div key={oIdx} className={overrideStyle}>
                                <MCQOption
                                    selected={isSelected}
                                    onClick={() => {
                                        if (!readOnlyMode) setAnswer(idx, String(oIdx));
                                    }}
                                    label={opt}
                                />
                            </div>
                        );
                    })}
                </div>
            );
        }

        if (question.question_type === 'typed') {
            const memoHintItems = buildNonTabularHintItems(question);
            return (
                <div className="space-y-3">
                    <textarea
                        ref={!readOnlyMode ? activeInputRef : undefined}
                        value={questionAnswer || ''}
                        onFocus={() => {
                            if (!readOnlyMode && localStorage.getItem('mathKeypadSettings_disableAutoPopup') !== 'true') setIsKeypadVisible(true);
                        }}
                        onChange={(e) => {
                            if (!readOnlyMode) setAnswer(idx, e.target.value);
                        }}
                        className={`w-full min-h-[140px] p-4 border rounded-xl text-base focus:outline-none focus:ring-2 transition-colors ${showHighlights && !normalizeText(questionAnswer).length ? 'bg-red-50 border-red-300 text-red-900 focus:ring-red-400' : 'text-slate-700 bg-slate-50 border-slate-200 focus:ring-indigo-500/50 focus:bg-white'}`}
                        placeholder="Type your explanation here..."
                        readOnly={readOnlyMode}
                    />
                    {!readOnlyMode && (
                        <div className="flex justify-end">
                            <button
                                onClick={() => setIsKeypadVisible(!isKeypadVisible)}
                                className="px-3 py-1.5 text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-200 rounded-lg hover:bg-indigo-100 transition-colors"
                            >
                                {isKeypadVisible ? 'Hide Keypad' : 'Show Math Keypad'}
                            </button>
                        </div>
                    )}
                    {memoEnabled && (
                        <div className="mt-6 text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                            {memoHintItems.length > 0 ? (
                                <div className="space-y-3">
                                    <div className="font-semibold text-slate-900">Guideline answer</div>
                                    {memoHintItems.map((item, itemIdx) => (
                                        <div key={`${item.label}-${itemIdx}`} className="flex items-start gap-3">
                                            <div className="flex-1 min-w-0">
                                                <div className="font-semibold text-slate-900">{item.label}</div>
                                                <div className="whitespace-pre-line">{item.value}</div>
                                            </div>
                                            {item.sections.length > 0 && (
                                                <button
                                                    type="button"
                                                    onClick={(e) => {
                                                        e.preventDefault();
                                                        e.stopPropagation();
                                                        openNonTabularHint({
                                                            idx,
                                                            hintKey: `typed_${itemIdx}`,
                                                            label: item.label,
                                                            sections: item.sections,
                                                            triggerEl: e.currentTarget,
                                                        });
                                                    }}
                                                    className="inline-flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold border border-yellow-300 text-yellow-800 bg-yellow-50 hover:bg-yellow-100 shrink-0"
                                                    aria-label={`Hint: ${item.label}`}
                                                >
                                                    i
                                                </button>
                                            )}
                                        </div>
                                    ))}
                                </div>
                            ) : question.sample_answer && (
                                <div className="mb-2"><span className="font-semibold text-slate-900">Guideline answer: </span><span className="whitespace-pre-line">{question.sample_answer}</span></div>
                            )}
                            {Array.isArray(question.guidelines) && question.guidelines.length > 0 && (
                                <div>
                                    <div className="font-semibold text-slate-900 mb-1">Guidelines:</div>
                                    <ul className="list-disc pl-5 space-y-1">
                                        {question.guidelines.map((g, gi) => <li key={gi}>{g}</li>)}
                                    </ul>
                                </div>
                            )}
                        </div>
                    )}
                </div>
            );
        }

        if (question.question_type === 'calc') {
            const gotN = questionAnswer !== null && questionAnswer !== undefined && String(questionAnswer).trim() !== '' ? toNumber(questionAnswer) : null;
            const correctValue = Number(question.correct_value);
            const isCorrect = gotN !== null && Number.isFinite(correctValue) && numbersMatch(gotN, correctValue, {
                allowRoundedRand: String(question.unit || '').toUpperCase().includes('R'),
            });
            const isIncorrect = showHighlights && !isCorrect;
            const memoHintItems = buildNonTabularHintItems(question);

            return (
                <div className="space-y-3">
                    <input
                        ref={!readOnlyMode ? activeInputRef : undefined}
                        value={memoEnabled ? (question.correct_value || '') : (questionAnswer || '')}
                        onFocus={() => {
                            if (!readOnlyMode && localStorage.getItem('mathKeypadSettings_disableAutoPopup') !== 'true') setIsKeypadVisible(true);
                        }}
                        onChange={(e) => {
                            if (!readOnlyMode) setAnswer(idx, e.target.value);
                        }}
                        className={`w-full p-4 border rounded-xl text-lg font-medium tracking-wide focus:outline-none focus:ring-2 transition-all ${isIncorrect ? 'bg-red-50 border-red-300 text-red-900 focus:ring-red-400' : showHighlights && isCorrect ? 'bg-emerald-50 border-emerald-300 text-emerald-900 focus:ring-emerald-400' : 'bg-slate-50 border-slate-200 text-slate-800 focus:bg-white focus:ring-indigo-500/50'}`}
                        placeholder="Enter numerical amount..."
                        readOnly={readOnlyMode || memoEnabled}
                    />
                    {!readOnlyMode && (
                        <div className="flex justify-end">
                            <button
                                onClick={() => setIsKeypadVisible(!isKeypadVisible)}
                                className="px-3 py-1.5 text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-200 rounded-lg hover:bg-indigo-100 transition-colors"
                            >
                                {isKeypadVisible ? 'Hide Keypad' : 'Show Math Keypad'}
                            </button>
                        </div>
                    )}
                    {memoEnabled && memoHintItems.length > 0 && (
                        <div className="mt-3 p-3 bg-indigo-50/80 border border-indigo-100 rounded-lg text-sm text-indigo-800 space-y-3">
                            {memoHintItems.map((item, itemIdx) => (
                                <div key={`${item.label}-${itemIdx}`} className="flex items-start gap-3">
                                    <span className="text-xl leading-none">💡</span>
                                    <div className="flex-1 min-w-0">
                                        <div className="font-semibold text-indigo-900">{item.label}</div>
                                        <div className="font-mono whitespace-pre-line">{item.value}</div>
                                    </div>
                                    {item.sections.length > 0 && (
                                        <button
                                            type="button"
                                            onClick={(e) => {
                                                e.preventDefault();
                                                e.stopPropagation();
                                                openNonTabularHint({
                                                    idx,
                                                    hintKey: `calc_${itemIdx}`,
                                                    label: item.label,
                                                    sections: item.sections,
                                                    triggerEl: e.currentTarget,
                                                });
                                            }}
                                            className="inline-flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold border border-yellow-300 text-yellow-800 bg-yellow-50 hover:bg-yellow-100 shrink-0"
                                            aria-label={`Hint: ${item.label}`}
                                        >
                                            i
                                        </button>
                                    )}
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            );
        }

        if (question.question_type === 'journal' || question.question_type === 'ledger') {
            const memoHintItems = buildNonTabularHintItems(question);
            return (
                <div className="space-y-3">
                    {renderJournal(question, idx, {
                        showHighlights,
                        memoEnabled,
                        readOnlyMode,
                    })}
                    {memoEnabled && memoHintItems.length > 0 && (
                        <div className="mt-3 p-3 bg-indigo-50/80 border border-indigo-100 rounded-lg text-sm text-indigo-800 space-y-3">
                            {memoHintItems.map((item, itemIdx) => (
                                <div key={`${item.label}-${itemIdx}`} className="flex items-start gap-3">
                                    <span className="text-xl leading-none">💡</span>
                                    <div className="flex-1 min-w-0">
                                        <div className="font-semibold text-indigo-900">{item.label}</div>
                                        <div className="font-mono whitespace-pre-line">{item.value}</div>
                                    </div>
                                    {item.sections.length > 0 && (
                                        <button
                                            type="button"
                                            onClick={(e) => {
                                                e.preventDefault();
                                                e.stopPropagation();
                                                openNonTabularHint({
                                                    idx,
                                                    hintKey: `journal_${itemIdx}`,
                                                    label: item.label,
                                                    sections: item.sections,
                                                    triggerEl: e.currentTarget,
                                                });
                                            }}
                                            className="inline-flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold border border-yellow-300 text-yellow-800 bg-yellow-50 hover:bg-yellow-100 shrink-0"
                                            aria-label={`Hint: ${item.label}`}
                                        >
                                            i
                                        </button>
                                    )}
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            );
        }

        if (question.question_type === 'match') {
            return (
                <div className={freezeInteractions ? 'pointer-events-none' : ''}>
                    <MatchQuestionUI
                        question={question}
                        answer={questionAnswer}
                        setAnswer={readOnlyMode ? (() => {}) : ((newAns) => setAnswer(idx, newAns))}
                        readOnly={memoEnabled}
                        showCheckHighlights={showHighlights}
                    />
                </div>
            );
        }

        if (question.question_type === 'word_bank') {
            return (
                <div className={freezeInteractions ? 'pointer-events-none' : ''}>
                    <WordBankQuestionUI
                        question={question}
                        answer={questionAnswer}
                        setAnswer={readOnlyMode ? (() => {}) : ((newAns) => setAnswer(idx, newAns))}
                        readOnly={memoEnabled}
                        showCheckHighlights={showHighlights}
                    />
                </div>
            );
        }

        if (question.question_type === 'inline_fill') {
            return (
                <div className={freezeInteractions ? 'pointer-events-none' : ''}>
                    <InlineFillQuestionUI
                        question={question}
                        answer={questionAnswer}
                        setAnswer={readOnlyMode ? (() => {}) : ((newAns) => setAnswer(idx, newAns))}
                        readOnly={memoEnabled}
                        showCheckHighlights={showHighlights}
                    />
                </div>
            );
        }

        return null;
    };

    const feedbackByQuestion = Array.isArray(g10AcctSTPracticeFeedback) ? g10AcctSTPracticeFeedback : [];
    const correctCount = feedbackByQuestion.filter((item) => item?.isCorrect === true).length;

    return (
        <div className="w-full">
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Practice Mode</h3>

                {questions.length > 0 && (
                    <div className="flex flex-wrap items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200 opacity-80">
                        <span className="text-sm font-semibold text-slate-700">Assessment:</span>
                        <button
                            type="button"
                            disabled
                            className="relative inline-flex h-6 w-11 items-center rounded-full bg-slate-200 cursor-not-allowed"
                        >
                            <span className="inline-block h-4 w-4 transform rounded-full bg-white translate-x-1" />
                        </button>
                        <span className="text-sm text-slate-600">Practice only</span>
                        <span className="text-xs text-slate-500">Assessment available in Pro package</span>
                    </div>
                )}
            </div>

            {isSuperAdmin && (
                <div className="mb-4 p-3 bg-amber-50 border border-amber-300 rounded-xl flex items-center gap-3 flex-wrap">
                    <span className="text-xs font-bold text-amber-800 uppercase tracking-wide">🔒 Admin</span>
                    <label className="flex items-center gap-2 text-sm text-amber-900 font-medium">
                        Format:
                        <select
                            value={adminFormat}
                            onChange={(e) => setAdminFormat(e.target.value)}
                            className="px-2 py-1 border border-amber-300 rounded-lg text-sm bg-white focus:outline-none focus:ring-2 focus:ring-amber-400"
                        >
                            <option value="mixed">Mixed Random</option>
                            <option value="journal">Journal Table</option>
                            <option value="mcq">Multiple Choice</option>
                            <option value="calc">Calculation</option>
                            <option value="typed">Typed Answer</option>
                        </select>
                    </label>
                    <label className="flex items-center gap-2 text-sm text-amber-900 font-medium">
                        Seed:
                        <input
                            type="number"
                            value={g10AcctSTPracticeSeed || ''}
                            onChange={(e) => setG10AcctSTPracticeSeed(e.target.value)}
                            className="w-32 px-2 py-1 border border-amber-300 rounded-lg text-sm bg-white focus:outline-none focus:ring-2 focus:ring-amber-400"
                            placeholder="e.g. 42"
                        />
                    </label>
                    <button
                        onClick={() => {
                            fetchGrade10AcctSTPractice({
                                subskill: g10AcctSTPracticeSubskill,
                                difficulty: g10AcctSTPracticeDifficulty,
                                seed: g10AcctSTPracticeSeed,
                                question_type: adminFormat,
                            });
                        }}
                        className="px-4 py-1.5 bg-amber-600 text-white text-sm rounded-lg font-semibold shadow-sm hover:bg-amber-700 hover:shadow transition-all"
                    >
                        Generate Validation Test
                    </button>
                    <button
                        onClick={() => {
                            setG10AcctSTPracticeSeed('');
                            setAdminFormat('mixed');
                        }}
                        className="px-3 py-1.5 bg-white border border-amber-300 text-amber-700 text-sm rounded-lg font-medium hover:bg-amber-100 transition-colors"
                    >
                        Clear
                    </button>
                    {(g10AcctSTPracticeSeed || adminFormat !== 'mixed') && (
                        <span className="text-xs text-amber-700 font-mono bg-amber-100/80 border border-amber-200 px-2 py-0.5 rounded shadow-sm">
                            config={adminFormat}:seed={g10AcctSTPracticeSeed || 'rand'}
                        </span>
                    )}
                </div>
            )}

            {g10AcctSTPracticeLoading && (
                <div className="text-sm text-slate-500">Loading…</div>
            )}
            {g10AcctSTPracticeError && (
                <div className="text-sm text-red-700 break-words">{g10AcctSTPracticeError}</div>
            )}

            {!g10AcctSTPracticeLoading && questions.length === 0 && (
                <div className="text-sm text-slate-500">Click "Generate Question" to start.</div>
            )}

            {q && !reviewMode && (
                <div key={`${q?.id || q?.question_type || 'question'}-${currentIndex}`} className="space-y-4">
                    <div className="flex flex-wrap items-center justify-between gap-3 bg-white px-4 py-3 rounded-xl border border-slate-200">
                        <div className="text-sm font-semibold text-slate-800">Question {currentIndex + 1} of {questions.length}</div>
                        <div className="text-sm text-slate-600">Time on this question: {formatElapsedTime(liveElapsedSeconds)}</div>
                    </div>
                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        {getQuestionPrompt(q) && (
                            <div className="mb-4 text-[15px] leading-7 text-slate-800 whitespace-pre-wrap">{getQuestionPrompt(q)}</div>
                        )}
                        {renderPromptTables(q, currentIndex)}
                        {q?.reference_journal && (
                            <div className="mb-6">
                                <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">
                                    {q?.reference_journal?.heading || 'Reference Trial Balance'}
                                </div>
                                {renderOneJournalTable({
                                    journal: q.reference_journal,
                                    q,
                                    tableIndex: -1,
                                    readOnlyMode: true,
                                    isReference: true,
                                })}
                            </div>
                        )}
                        {renderQuestionContent(q, currentIndex, { showHighlights: false, memoEnabled: false, readOnlyMode: false })}
                        <div className="mt-8 flex flex-wrap items-center justify-between gap-3 pt-4 border-t border-slate-100">
                            <button
                                onClick={handlePrev}
                                disabled={currentIndex === 0}
                                className="px-6 py-2 bg-white border border-slate-200 text-slate-700 rounded-xl font-semibold hover:bg-slate-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
                            >
                                Previous Question
                            </button>
                            {currentIndex < questions.length - 1 ? (
                                <button
                                    onClick={handleNext}
                                    className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors"
                                >
                                    Next Question
                                </button>
                            ) : (
                                <button
                                    onClick={handleFinishAndReview}
                                    className="px-6 py-2 bg-indigo-600 text-white rounded-xl font-semibold hover:bg-indigo-700 transition-colors"
                                >
                                    Finish & Review
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            )}

            {reviewMode && questions.length > 0 && (
                <div className="space-y-4">
                    <div className="p-5 bg-white border border-slate-200 rounded-xl shadow-sm">
                        <div className="flex flex-wrap items-end justify-between gap-4">
                            <div>
                                <div className="text-xl font-bold text-slate-800">Practice Review</div>
                                <div className="text-sm text-slate-600 mt-1">All questions are shown below in a single scrollable review page.</div>
                            </div>
                            <div className="text-right">
                                <div className="text-3xl font-black text-indigo-700">{correctCount}/{questions.length}</div>
                                <div className="text-sm text-slate-600">correct</div>
                            </div>
                        </div>
                    </div>

                    <div className="max-h-[70vh] overflow-y-auto pr-2 space-y-4">
                        {questions.map((question, idx) => {
                            const feedback = feedbackByQuestion[idx];
                            const memoEnabled = activeReviewMemoIndex === idx;
                            const supportsMemo = ['calc', 'typed', 'match', 'word_bank', 'inline_fill', 'journal', 'ledger'].includes(question?.question_type);
                            const canToggleMemo = supportsMemo && feedback?.kind !== 'success';
                            const hintsEnabled = showHintsByQuestion[idx] === true;
                            const canToggleHints = ['journal', 'ledger'].includes(question?.question_type) && feedback?.wrongCount > 0;

                            return (
                                <div
                                    key={question?.id || idx}
                                    className={`p-5 border rounded-xl shadow-sm ${feedback?.kind === 'success' ? 'bg-emerald-50/50 border-emerald-200' : 'bg-white border-slate-200'}`}
                                >
                                    <div className="flex flex-wrap items-start justify-between gap-4 mb-4">
                                        <div>
                                            <div className="text-xs font-semibold uppercase tracking-wide text-slate-500">Question {idx + 1}</div>
                                            {getQuestionPrompt(question) && (
                                                <div className="mt-2 text-[15px] leading-7 text-slate-800 whitespace-pre-wrap">{getQuestionPrompt(question)}</div>
                                            )}
                                            {renderPromptTables(question, idx)}
                                            {feedback && Number.isFinite(feedback.totalCount) && feedback.totalCount > 0 && (
                                                <div className={`mt-3 inline-flex items-center rounded-full px-3 py-1 text-xs font-semibold border ${feedback.wrongCount > 0 ? 'bg-red-50 border-red-200 text-red-800' : 'bg-emerald-50 border-emerald-200 text-emerald-800'}`}>
                                                    {feedback.wrongCount} of {feedback.totalCount} {question?.question_type === 'journal' || question?.question_type === 'ledger' ? 'cells' : 'responses'} incorrect
                                                </div>
                                            )}
                                        </div>
                                        <div className="text-sm text-slate-600">Time: {formatElapsedTime(elapsedSecondsByIndex[idx] || 0)}</div>
                                    </div>

                                    {renderQuestionContent(question, idx, {
                                        showHighlights: true,
                                        memoEnabled,
                                        readOnlyMode: true,
                                    })}

                                    <div className="mt-4 flex flex-wrap items-start justify-between gap-3">
                                        {feedback && (
                                            <div className={`flex-1 min-w-[240px] p-3 rounded-xl text-sm border ${feedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : feedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                                                {feedback.message}
                                            </div>
                                        )}
                                        <div className="flex flex-wrap items-center gap-3">
                                            {canToggleMemo && (
                                                <button
                                                    onClick={() => setActiveReviewMemoIndex(memoEnabled ? null : idx)}
                                                    className="px-6 py-2 bg-purple-600 text-white rounded-xl font-semibold hover:bg-purple-700 transition-colors shadow-sm"
                                                >
                                                    {memoEnabled ? 'Hide Memo' : 'Compare / Memo'}
                                                </button>
                                            )}
                                            {canToggleHints && (
                                                <button
                                                    onClick={() => {
                                                        setShowHintsByQuestion((prev) => ({ ...prev, [idx]: !prev[idx] }));
                                                        setActiveCellHint(null);
                                                    }}
                                                    className="px-6 py-2 bg-yellow-500 text-white rounded-xl font-semibold hover:bg-yellow-600 transition-colors shadow-sm"
                                                >
                                                    {hintsEnabled ? 'Hide Hints' : 'Show Hints'}
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            )}

            {activeCellHint && (
                <div
                    ref={cellHintPopupRef}
                    className="fixed z-[80] w-80 max-w-[calc(100vw-24px)] rounded-lg border border-yellow-200 bg-yellow-50 shadow-xl text-xs text-yellow-900 whitespace-pre-line"
                    style={{ left: activeCellHint.x, top: activeCellHint.y }}
                >
                    <div className="flex items-start justify-between gap-2 p-3 border-b border-yellow-200 bg-yellow-100/70 rounded-t-lg">
                        <div className="font-semibold pr-2">{activeCellHint.label}</div>
                        <div className="flex items-center gap-1">
                            <button
                                type="button"
                                onClick={() => setActiveCellHint((prev) => prev ? { ...prev, ...clampHintPosition(prev.x - 32, prev.y, cellHintPopupRef.current?.offsetWidth || 320, cellHintPopupRef.current?.offsetHeight || 240) } : prev)}
                                className="px-1.5 py-0.5 rounded border border-yellow-300 bg-white hover:bg-yellow-100"
                                aria-label="Move hint left"
                            >
                                ←
                            </button>
                            <button
                                type="button"
                                onClick={() => setActiveCellHint((prev) => prev ? { ...prev, ...clampHintPosition(prev.x, prev.y - 32, cellHintPopupRef.current?.offsetWidth || 320, cellHintPopupRef.current?.offsetHeight || 240) } : prev)}
                                className="px-1.5 py-0.5 rounded border border-yellow-300 bg-white hover:bg-yellow-100"
                                aria-label="Move hint up"
                            >
                                ↑
                            </button>
                            <button
                                type="button"
                                onClick={() => setActiveCellHint((prev) => prev ? { ...prev, ...clampHintPosition(prev.x, prev.y + 32, cellHintPopupRef.current?.offsetWidth || 320, cellHintPopupRef.current?.offsetHeight || 240) } : prev)}
                                className="px-1.5 py-0.5 rounded border border-yellow-300 bg-white hover:bg-yellow-100"
                                aria-label="Move hint down"
                            >
                                ↓
                            </button>
                            <button
                                type="button"
                                onClick={() => setActiveCellHint((prev) => prev ? { ...prev, ...clampHintPosition(prev.x + 32, prev.y, cellHintPopupRef.current?.offsetWidth || 320, cellHintPopupRef.current?.offsetHeight || 240) } : prev)}
                                className="px-1.5 py-0.5 rounded border border-yellow-300 bg-white hover:bg-yellow-100"
                                aria-label="Move hint right"
                            >
                                →
                            </button>
                            <button
                                type="button"
                                onClick={() => setActiveCellHint((prev) => prev ? { ...prev, ...clampHintPosition(prev.anchorX, prev.anchorY, cellHintPopupRef.current?.offsetWidth || 320, cellHintPopupRef.current?.offsetHeight || 240) } : prev)}
                                className="px-2 py-0.5 rounded border border-yellow-300 bg-white hover:bg-yellow-100"
                            >
                                Reset
                            </button>
                            <button
                                type="button"
                                onClick={() => setActiveCellHint(null)}
                                className="text-yellow-700 hover:text-yellow-900 px-1"
                                aria-label="Close cell hint"
                            >
                                ✕
                            </button>
                        </div>
                    </div>
                    {renderCellHintPopupContent(activeCellHint)}
                </div>
            )}
            
            <EnhancedMathKeypad 
                isVisible={isKeypadVisible && !reviewMode}
                onClose={() => setIsKeypadVisible(false)}
                inputRef={activeInputRef}
                onExpressionChange={(val) => {
                    if (!reviewMode) setAnswer(currentIndex, val);
                }}
            />
        </div>
    );
};

export default Grade10AccountingSoleTraderPractice;

