import React, { useEffect, useMemo, useRef, useState } from 'react';
import MCQOption from '../../shared/MCQOption';
import { useGrade9EmsMarking } from './useGrade9EmsMarking';
import { getEvalCellStyle } from '../../shared/evalCellStyle';
import EnhancedMathKeypad from '../../../EnhancedMathKeypad';
import WordBankQuestionUI from '../../shared/WordBankQuestionUI.jsx';
import MatchQuestionUI from '../../shared/MatchQuestionUI.jsx';
import InlineFillQuestionUI from '../../shared/InlineFillQuestionUI.jsx';

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
    const parts = raw.split(/[\/\n,;]+/g).map((p) => p.trim()).filter(Boolean);
    const tokens = new Set();
    parts.forEach((p) => {
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
    return (s.includes('/') || s.includes('\n')) && /[+\-±]/.test(s);
};

const isControlAccountsReconciliationQuestion = (question) => {
    const journals = Array.isArray(question?.journals)
        ? question.journals
        : (question?.journal ? [question.journal] : []);
    const types = new Set(['control_accounts_reconciliation', 'control_account', 'list', 'reconciliation_impact']);
    return journals.some((j) => types.has(String(j?.journal_type || '').toLowerCase()));
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

const SCAFFOLD_DIFFICULTY_ORDER = ['easy', 'medium', 'hard'];

const getNextScaffoldDifficulty = (difficultyRaw) => {
    const difficulty = String(difficultyRaw || 'easy').trim().toLowerCase();
    const idx = SCAFFOLD_DIFFICULTY_ORDER.indexOf(difficulty);
    if (idx < 0 || idx >= SCAFFOLD_DIFFICULTY_ORDER.length - 1) return null;
    return SCAFFOLD_DIFFICULTY_ORDER[idx + 1];
};

const formatDifficultyLabel = (difficultyRaw) => {
    const difficulty = String(difficultyRaw || '').trim().toLowerCase();
    if (!difficulty) return 'Easy';
    return `${difficulty.charAt(0).toUpperCase()}${difficulty.slice(1)}`;
};

const buildTypedHintSections = (question) => {
    const sections = [];
    const guidelines = Array.isArray(question?.guidelines) ? question.guidelines : [];
    if (guidelines.length > 0) {
        sections.push({
            title: 'How to approach it',
            text: guidelines.map((line, idx) => `${idx + 1}. ${line}`).join('\n'),
        });
    }
    const sampleAnswer = String(question?.sample_answer || '').trim();
    if (sampleAnswer) {
        sections.push({
            title: 'Memo layout example',
            text: sampleAnswer,
        });
    }
    return sections;
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

const Grade9EmsScaffold = ({
    onBack,
    scaffoldSteps,
    subskills,
    g9EmsVisualAidsOpen,
    setg9EmsVisualAidsOpen,
    g9EmsScaffoldDifficulty,
    setg9EmsScaffoldDifficulty,
    g9EmsSubskill,
    setg9EmsSubskill,
    g9EmsScaffoldSeed,
    setg9EmsScaffoldSeed,
    g9EmsScaffoldStepIndex,
    setg9EmsScaffoldStepIndex,
    fetchGrade9EmsScaffoldQuestion,
    g9EmsScaffoldLoading,
    g9EmsScaffoldError,
    g9EmsScaffoldQuestion,
    g9EmsScaffoldAnswer,
    setg9EmsScaffoldAnswer,
    g9EmsScaffoldFeedback,
    setg9EmsScaffoldFeedback,
    g9EmsScaffoldShowHint,
    setg9EmsScaffoldShowHint,
    renderGrade9EmsVisualAids,
    evaluationState,
    isSuperAdmin,
}) => {
    const [activeHeaderHelp, setActiveHeaderHelp] = useState(null);
    const [activeCellHint, setActiveCellHint] = useState(null);
    const [crjTourIndex, setCrjTourIndex] = useState(-1);
    const crjTourTimerRef = useRef(null);
    const cellHintPopupRef = useRef(null);
    
    // Check/Compare, TTC, and Admin Format State
    const [showCheckHighlights, setShowCheckHighlights] = useState(false);
    const [showMemo, setShowMemo] = useState(false);
    const attemptStartTimeRef = useRef(null);
    const [adminPanelOpen, setAdminPanelOpen] = useState(false);
    const [adminFormat, setAdminFormat] = useState('mixed');
    const [attemptRecordedForQuestion, setAttemptRecordedForQuestion] = useState(false);
    const [keepCurrentDifficulty, setKeepCurrentDifficulty] = useState(false);
    const [difficultyAttemptCounts, setDifficultyAttemptCounts] = useState({ easy: 0, medium: 0, hard: 0 });
    const [pendingDifficultyPromotion, setPendingDifficultyPromotion] = useState(null);
    const [difficultyNotice, setDifficultyNotice] = useState('');

    // Keypad State
    const activeInputRef = useRef(null);
    const [isKeypadVisible, setIsKeypadVisible] = useState(false);

    useEffect(() => {
        // Reset check/compare state when question changes
        setShowCheckHighlights(false);
        setShowMemo(false);
        setActiveCellHint(null);
        setAttemptRecordedForQuestion(false);
        attemptStartTimeRef.current = Date.now();
    }, [g9EmsScaffoldQuestion]);

    useEffect(() => {
        if (!activeCellHint || !cellHintPopupRef.current) return;
        const width = cellHintPopupRef.current.offsetWidth || 320;
        const height = cellHintPopupRef.current.offsetHeight || 240;
        const next = clampHintPosition(activeCellHint.x, activeCellHint.y, width, height);
        if (next.x !== activeCellHint.x || next.y !== activeCellHint.y) {
            setActiveCellHint((prev) => (prev ? { ...prev, x: next.x, y: next.y } : prev));
        }
    }, [activeCellHint]);

    // ── Spaced Repetition (Finding 4) ──
    // Flagged questions are stored locally per-subskill. Every 5 answers, the next
    // "Next Question" call will inject the oldest flagged question instead of fetching a new one.
    const SR_KEY = `g10_acct_st_sr_queue_${(scaffoldSteps[g9EmsScaffoldStepIndex] || scaffoldSteps[0])?.key || 'mixed'}`;
    const [srQueue, setSrQueue] = useState(() => {
        try { return JSON.parse(localStorage.getItem(SR_KEY) || '[]'); }
        catch { return []; }
    });
    const [answerCount, setAnswerCount] = useState(0);
    // When true, the current question being shown is a spaced-repetition replay
    const [isReplayQuestion, setIsReplayQuestion] = useState(false);

    const addToSrQueue = (q) => {
        setSrQueue(prev => {
            // Avoid duplicate flags for the same question id
            if (prev.some(item => item.id === q.id)) return prev;
            const next = [...prev, q];
            localStorage.setItem(SR_KEY, JSON.stringify(next));
            return next;
        });
    };

    const removeFromSrQueue = (qId) => {
        setSrQueue(prev => {
            const next = prev.filter(item => item.id !== qId);
            localStorage.setItem(SR_KEY, JSON.stringify(next));
            return next;
        });
    };

    // ── Redo State (Finding 3) ──
    // Snapshot of the user's answer at the moment they pressed Check, used to restore on Redo
    const [preCheckAnswer, setPreCheckAnswer] = useState(null);


    useEffect(() => {
        return () => {
            if (crjTourTimerRef.current) {
                clearInterval(crjTourTimerRef.current);
                crjTourTimerRef.current = null;
            }
        };
    }, []);
    const question = g9EmsScaffoldQuestion;
    const selectedSubtopic = scaffoldSteps[g9EmsScaffoldStepIndex] || scaffoldSteps[0];
    const difficultyProgressKey = useMemo(
        () => `g10_acct_st_scaffold_difficulty_progress_${selectedSubtopic?.key || 'mixed'}`,
        [selectedSubtopic?.key],
    );
    const difficultyKeepKey = useMemo(
        () => `g10_acct_st_scaffold_keep_mode_${selectedSubtopic?.key || 'mixed'}`,
        [selectedSubtopic?.key],
    );

    const marking = useGrade9EmsMarking();

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

    // Reset marking state when a new subtopic is selected
    useEffect(() => {
        marking.setMarkingMode('practice');
    }, [g9EmsScaffoldStepIndex]);

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
    const currentDifficulty = String(g9EmsScaffoldDifficulty || 'easy').trim().toLowerCase();
    const nextDifficulty = getNextScaffoldDifficulty(currentDifficulty);
    const currentDifficultyAttempts = Number(difficultyAttemptCounts?.[currentDifficulty]) || 0;
    const attemptsTowardNextLevel = nextDifficulty
        ? (pendingDifficultyPromotion ? 5 : (currentDifficultyAttempts % 5))
        : 0;

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
        // Spaced repetition injection: every 5 answered questions, replay the oldest flagged item
        const shouldIncrementAnswerCount = Boolean(question) && attemptRecordedForQuestion;
        const nextCount = shouldIncrementAnswerCount ? (answerCount + 1) : answerCount;
        if (shouldIncrementAnswerCount) setAnswerCount(nextCount);
        setPreCheckAnswer(null);

        if (shouldIncrementAnswerCount && nextCount % 5 === 0 && srQueue.length > 0) {
            // Inject the oldest flagged question as a replay
            const replayQ = srQueue[0];
            setIsReplayQuestion(true);
            // Directly set the scaffold question state by calling the setter from props
            // We trigger a fake fetch by passing the question via a wrapper
            setg9EmsScaffoldAnswer(null);
            setg9EmsScaffoldFeedback(null);
            setg9EmsScaffoldShowHint(false);
            // Use fetchGrade9EmsScaffoldQuestion trick: we override with a known question
            // Since we can't set it directly, call fetch normally then override in a setTimeout
            // The cleanest approach: store the override and render it conditionally
            setSrQueue(prev => prev); // force re-render with replay flag set
            fetchGrade9EmsScaffoldQuestion({ _srOverride: replayQ });
            return;
        }

        setIsReplayQuestion(false);
        let difficultyForNextQuestion = currentDifficulty;
        if (pendingDifficultyPromotion) {
            if (keepCurrentDifficulty) {
                setDifficultyNotice(`Continuing in ${currentDifficulty} because keep mode is on.`);
            } else {
                difficultyForNextQuestion = pendingDifficultyPromotion;
                if (difficultyForNextQuestion !== currentDifficulty) {
                    setg9EmsScaffoldDifficulty(difficultyForNextQuestion);
                }
                setDifficultyNotice(`Difficulty moved to ${difficultyForNextQuestion} for the next scaffold question.`);
            }
            setPendingDifficultyPromotion(null);
        }
        const chosen = (g9EmsSubskill || '').trim();
        const effectiveSubskill = chosen && chosen !== 'auto'
            ? chosen
            : (selectedSubtopic?.key || 'mixed');
        fetchGrade9EmsScaffoldQuestion({
            subskill: effectiveSubskill,
            difficulty: difficultyForNextQuestion,
            seed: g9EmsScaffoldSeed,
        });
    };

    const setAnswerValue = (value) => {
        setg9EmsScaffoldAnswer(value);
        if (question) {
            marking.registerAnswer(question.id, value);
        }
        setg9EmsScaffoldFeedback(null);
    };

    const checkAnswer = () => {
        if (!question) return;

        if (question.question_type === 'mcq') {
            const ok = String(g9EmsScaffoldAnswer) === String(question.correct_index);
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.options?.[question.correct_index] || ''}` });
            if (ok && attemptStartTimeRef.current) {
                const ttcSeconds = (Date.now() - attemptStartTimeRef.current) / 1000;
                console.log(`[TTC METRIC] Attempt completed in ${ttcSeconds.toFixed(1)} seconds`);
                attemptStartTimeRef.current = null;
            }
            return;
        }

        if (question.question_type === 'typed') {
            const user = normalizeText(g9EmsScaffoldAnswer);
            if (!user) {
                setg9EmsScaffoldFeedback({ kind: 'error', message: 'Write an answer first.' });
                return;
            }
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback({ kind: 'info', message: 'AI-graded feedback available in Pro subscription.' });
            return;
        }

        if (question.question_type === 'calc') {
            const userN = toNumber(g9EmsScaffoldAnswer);
            if (userN === null) {
                setg9EmsScaffoldFeedback({ kind: 'error', message: 'Enter a number first.' });
                return;
            }
            const correct = Number(question.correct_value);
            const ok = Number.isFinite(correct) && numbersMatch(userN, correct, {
                allowRoundedRand: String(question.unit || '').toUpperCase().includes('R'),
            });
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback(ok
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. Correct answer: ${question.unit || ''}${correct.toFixed(2)}` });
            if (ok && attemptStartTimeRef.current) {
                const ttcSeconds = (Date.now() - attemptStartTimeRef.current) / 1000;
                console.log(`[TTC METRIC] Attempt completed in ${ttcSeconds.toFixed(1)} seconds`);
                attemptStartTimeRef.current = null;
            }
            return;
        }

        if (question.question_type === 'match') {
            const expectedMap = question.correct_map || {};
            const userMap = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object') ? g9EmsScaffoldAnswer : {};
            let hit = 0;
            let total = 0;
            for (const [lId, rId] of Object.entries(expectedMap)) {
                total++;
                if (userMap[lId] === rId) hit++;
            }
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback(hit === total 
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You got ${hit} out of ${total} correct.` });
            return;
        }

        if (question.question_type === 'word_bank' || question.question_type === 'inline_fill') {
            const expectedMap = question.correct_map || {};
            const userMap = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object') ? g9EmsScaffoldAnswer : {};
            let hit = 0;
            let total = 0;
            for (const [bId, ans] of Object.entries(expectedMap)) {
                total++;
                if (normalizeText(userMap[bId]) === normalizeText(ans)) hit++;
            }
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback(hit === total 
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You got ${hit} out of ${total} correct.` });
            return;
        }

        if (question.question_type === 'journal' || question.question_type === 'ledger') {
            const expectedMap = getExpectedByCellId(question);
            const ans = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object')
                ? g9EmsScaffoldAnswer
                : buildEmptyJournalAnswer(question);
            const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};

            const allowBracketWorkings = isControlAccountsReconciliationQuestion(question);
            const workingMap = (question?.working_map && typeof question.working_map === 'object') ? question.working_map : {};

            const keys = Object.keys(expectedMap);
            if (!keys.length) {
                setg9EmsScaffoldFeedback({ kind: 'error', message: 'Nothing to mark for this journal question.' });
                return;
            }

            let total = 0;
            let hit = 0;
            keys.forEach((cellId) => {
                const expected = expectedMap[cellId];
                if (expected === null || expected === undefined) return;
                total += 1;
                const got = cells[cellId];

                if (Array.isArray(expected)) {
                    const gotNorm = normalizeText(got);
                    const ok = expected.some((x) => normalizeText(x) === gotNorm);
                    if (ok) hit += 1;
                    return;
                }

                if (isNumericExpected(expected)) {
                    const gotN = toNumber(got);
                    const expN = typeof expected === 'number' ? expected : toNumber(expected);
                    if (gotN !== null && expN !== null && numbersMatch(gotN, expN, { allowRoundedRand: true })) hit += 1;
                    return;
                }

                if (isMultiValueExpected(expected)) {
                    const expSet = parseSignedTokenSet(expected);
                    const gotSet = parseSignedTokenSet(got);
                    if (expSet && gotSet && expSet.size === gotSet.size) {
                        const ok = Array.from(expSet).every((x) => gotSet.has(x));
                        if (ok) hit += 1;
                    }
                    return;
                }

                if (allowBracketWorkings) {
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

                        if (hasParens && outsideOk && workingOk) {
                            hit += 1;
                            return;
                        }
                        return;
                    }

                    const gotNoBrackets = stripParenthetical(got);
                    if (normalizeText(gotNoBrackets) === normalizeText(expected)) {
                        hit += 1;
                        return;
                    }
                }

                if (normalizeText(got) === normalizeText(expected)) hit += 1;
            });

            if (total === 0) {
                setg9EmsScaffoldFeedback({ kind: 'error', message: 'Nothing to mark for this journal question.' });
                return;
            }

            const isPerfect = hit === total;
            setShowCheckHighlights(true);
            setg9EmsScaffoldFeedback(isPerfect
                ? { kind: 'success', message: 'Correct.' }
                : { kind: 'error', message: `Not quite. You got ${hit}/${total} correct.` });
            if (isPerfect && attemptStartTimeRef.current) {
                const ttcSeconds = (Date.now() - attemptStartTimeRef.current) / 1000;
                console.log(`[TTC METRIC] Attempt completed in ${ttcSeconds.toFixed(1)} seconds`);
                attemptStartTimeRef.current = null;
            }
            return;
        }

        setg9EmsScaffoldFeedback({ kind: 'error', message: `Unsupported question type: ${question.question_type}` });
    };

    // Wrap checkAnswer to add SR flagging + preCheckAnswer snapshot
    const checkAnswerWithFlagging = () => {
        // Snapshot the current answer before checking (used by Redo button)
        setPreCheckAnswer(g9EmsScaffoldAnswer);
        checkAnswer();
        registerDifficultyAttempt();
        // After checking, inspect the feedback result to decide flagging
        // We use a micro-timeout so that setg9EmsScaffoldFeedback has settled
        setTimeout(() => {
            if (!question) return;
            // If the feedback kind is 'error', it means they got it wrong -> flag it
            // Note: fb here is the OLD value (pre-setState). We re-read via a ref trick.
            // Instead, we mimic the same result check inline:
            const isCorrect = (() => {
                const qt = question.question_type;
                if (qt === 'typed') return null;
                if (qt === 'mcq') return String(g9EmsScaffoldAnswer) === String(question.correct_index);
                if (qt === 'calc') {
                    const userN = toNumber(g9EmsScaffoldAnswer);
                    const correct = Number(question.correct_value);
                    return userN !== null && Number.isFinite(correct) && numbersMatch(userN, correct, {
                        allowRoundedRand: String(question.unit || '').toUpperCase().includes('R'),
                    });
                }
                if (qt === 'match') {
                    const expectedMap = question.correct_map || {};
                    const userMap = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object') ? g9EmsScaffoldAnswer : {};
                    return Object.entries(expectedMap).every(([lId, rId]) => userMap[lId] === rId);
                }
                if (qt === 'word_bank' || qt === 'inline_fill') {
                    const expectedMap = question.correct_map || {};
                    const userMap = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object') ? g9EmsScaffoldAnswer : {};
                    return Object.entries(expectedMap).every(([bId, ans]) => normalizeText(userMap[bId]) === normalizeText(ans));
                }
                if (qt === 'journal' || qt === 'ledger') {
                    const expectedMap = getExpectedByCellId(question);
                    const ans = (g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object')
                        ? g9EmsScaffoldAnswer
                        : buildEmptyJournalAnswer(question);
                    const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
                    const allowBracketWorkings = isControlAccountsReconciliationQuestion(question);
                    const workingMap = (question?.working_map && typeof question.working_map === 'object') ? question.working_map : {};
                    return Object.keys(expectedMap).every((cellId) => {
                        const expected = expectedMap[cellId];
                        if (expected === null || expected === undefined) return true;
                        const got = cells[cellId];
                        if (Array.isArray(expected)) return expected.some((x) => normalizeText(x) === normalizeText(got));
                        if (isNumericExpected(expected)) {
                            const expN = typeof expected === 'number' ? expected : toNumber(expected);
                            return expN !== null && numbersMatch(got, expN, { allowRoundedRand: true });
                        }
                        if (isMultiValueExpected(expected)) {
                            const expSet = parseSignedTokenSet(expected);
                            const gotSet = parseSignedTokenSet(got);
                            return Boolean(expSet && gotSet && expSet.size === gotSet.size && Array.from(expSet).every((x) => gotSet.has(x)));
                        }
                        if (allowBracketWorkings) {
                            const linkedAmountCellId = workingMap?.[cellId];
                            if (linkedAmountCellId) {
                                const outside = stripParenthetical(got);
                                const inner = getFirstParenthetical(got);
                                const expectedAmount = expectedMap?.[linkedAmountCellId];
                                const expectedAmountN = toNumber(expectedAmount);
                                const innerTotal = evalBracketExpression(inner);
                                return normalizeText(outside) === normalizeText(expected)
                                    && expectedAmountN !== null
                                    && innerTotal !== null
                                    && numbersMatch(innerTotal, expectedAmountN, { allowRoundedRand: true });
                            }
                            return normalizeText(stripParenthetical(got)) === normalizeText(expected);
                        }
                        return normalizeText(got) === normalizeText(expected);
                    });
                }
                return false;
            })();

            if (isCorrect === null) {
                return;
            }
            if (isCorrect) {
                // If user aced it on a replay, remove from queue
                if (isReplayQuestion) removeFromSrQueue(question.id);
            } else {
                // Wrong answer — flag it for later repetition
                addToSrQueue(question);
            }
        }, 100);
    };

    const handleAnswerKeyDown = (event) => {
        if (!marking.isPracticeMode) return;
        if (event.key !== 'Enter' || event.nativeEvent?.isComposing) return;
        const tagName = String(event.target?.tagName || '').toLowerCase();
        const shouldHandle = tagName === 'input' || (tagName === 'textarea' && !event.shiftKey);
        if (!shouldHandle) return;
        event.preventDefault();
        checkAnswerWithFlagging();
    };

    const renderOneJournalTable = ({
        journal,
        q,
        tableIndex,
        isLastTable,
        isReference = false,
    }) => {
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

        const journalType = String(journal?.journal_type || '').toLowerCase();
        const columnHelp = (journal?.column_help && typeof journal.column_help === 'object') ? journal.column_help : {};

        const crjHelpHeaders = journalType !== 'crj'
            ? []
            : headers.filter((h) => String(columnHelp[h] || '').trim().length > 0);

        const startCrjTour = () => {
            if (journalType !== 'crj') return;
            if (!crjHelpHeaders.length) return;

            if (crjTourTimerRef.current) {
                clearInterval(crjTourTimerRef.current);
                crjTourTimerRef.current = null;
            }

            setCrjTourIndex(0);
            crjTourTimerRef.current = setInterval(() => {
                setCrjTourIndex((prev) => {
                    const next = prev + 1;
                    if (next >= crjHelpHeaders.length) {
                        clearInterval(crjTourTimerRef.current);
                        crjTourTimerRef.current = null;
                        return -1;
                    }
                    return next;
                });
            }, 900);
        };

        const ans = g9EmsScaffoldAnswer && typeof g9EmsScaffoldAnswer === 'object'
            ? g9EmsScaffoldAnswer
            : buildEmptyJournalAnswer(q);
        const cells = ans?.cells && typeof ans.cells === 'object' ? ans.cells : {};
        const cellHints = (q?.cell_hints && typeof q.cell_hints === 'object') ? q.cell_hints : {};
        const cellTeachingMap = (q?.cell_teaching_map && typeof q.cell_teaching_map === 'object') ? q.cell_teaching_map : {};
        const extraRowsByTable = (ans?.extra_rows_by_table && typeof ans?.extra_rows_by_table === 'object') ? ans.extra_rows_by_table : {};
        const extraRows = Array.isArray(extraRowsByTable[String(tableIndex)]) ? extraRowsByTable[String(tableIndex)] : [];

        const rows = allowExtraRows ? [...baseRows, ...extraRows] : baseRows;

        const setCell = (cellId, value) => {
            setAnswerValue({
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
                if (prev?.cellId === cellId) return null;
                return {
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
            const newRowIndex = baseRows.length + extraRows.length;
            const newRow = Array.from({ length: totalCols }).map((_, cIdx) => ({
                cell_id: `t${tableIndex}_r${newRowIndex}_c${cIdx}`,
                value: '',
                editable: true,
            }));
            setAnswerValue({
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
                                    <div className="text-xs font-semibold text-slate-700 mb-1">{label}</div>
                                    <input
                                        value={value}
                                        onChange={(e) => {
                                            if (!isReference) setCell(id, e.target.value);
                                        }}
                                        className="w-full p-2 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-300"
                                        placeholder=""
                                        readOnly={isReference}
                                    />
                                </label>
                            );
                        })}
                    </div>
                )}
                {allowExtraRows && !isReference && (
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
                                        const helpText = String(columnHelp[label] || '').trim();
                                        const isHelpable = journalType === 'crj' && helpText.length > 0;
                                        const tourActiveLabel = (journalType === 'crj' && crjTourIndex >= 0 && crjHelpHeaders[crjTourIndex]) ? crjHelpHeaders[crjTourIndex] : null;
                                        const isGlowing = isHelpable && tourActiveLabel === label;
                                        return (
                                            <th
                                                key={cIdx}
                                                colSpan={colSpan}
                                                rowSpan={rowSpan}
                                                style={journalHeaderCellStyle}
                                            >
                                                <div className="flex items-center gap-2 relative" style={{ justifyContent: 'center' }}>
                                                    <span>{label}</span>
                                                    {isHelpable && (
                                                        <button
                                                            type="button"
                                                            onClick={(e) => {
                                                                e.preventDefault();
                                                                e.stopPropagation();
                                                                setActiveHeaderHelp({ label, text: helpText });
                                                                startCrjTour();
                                                            }}
                                                            className={
                                                                isGlowing
                                                                    ? 'inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-indigo-300 text-indigo-700 bg-indigo-50 animate-pulse ring-2 ring-indigo-400'
                                                                    : 'inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-gray-300 text-gray-600 bg-white hover:bg-gray-100'
                                                            }
                                                            aria-label={`Info: ${label}`}
                                                        >
                                                            i
                                                        </button>
                                                    )}
                                                    {activeHeaderHelp?.label === label && (
                                                        <div className="absolute z-20 top-full mt-2 left-0 w-72 p-3 rounded-lg border border-gray-200 bg-white shadow-lg text-xs text-gray-700">
                                                            <div className="flex items-start justify-between gap-2">
                                                                <div className="font-semibold text-gray-900">{activeHeaderHelp.label}</div>
                                                                <button
                                                                    type="button"
                                                                    onClick={(e) => {
                                                                        e.preventDefault();
                                                                        e.stopPropagation();
                                                                        setActiveHeaderHelp(null);
                                                                    }}
                                                                    className="text-gray-500 hover:text-gray-800"
                                                                    aria-label="Close"
                                                                >
                                                                    ✕
                                                                </button>
                                                            </div>
                                                            <div className="mt-2 leading-snug">{activeHeaderHelp.text}</div>
                                                        </div>
                                                    )}
                                                </div>
                                            </th>
                                        );
                                    })}
                                </tr>
                            ))
                        ) : (
                            <tr>
                                {headers.map((h, idx) => (
                                    (() => {
                                        const helpText = String(columnHelp[h] || '').trim();
                                        const isHelpable = journalType === 'crj' && helpText.length > 0;
                                        const tourActiveLabel = (journalType === 'crj' && crjTourIndex >= 0 && crjHelpHeaders[crjTourIndex]) ? crjHelpHeaders[crjTourIndex] : null;
                                        const isGlowing = isHelpable && tourActiveLabel === h;
                                        return (
                                            <th key={idx} style={journalHeaderCellStyle}>
                                                <div className="flex items-center gap-2 relative" style={{ justifyContent: 'center' }}>
                                                    <span>{h}</span>
                                                    {isHelpable && (
                                                        <button
                                                            type="button"
                                                            onClick={(e) => {
                                                                e.preventDefault();
                                                                e.stopPropagation();
                                                                setActiveHeaderHelp({ label: h, text: helpText });
                                                                startCrjTour();
                                                            }}
                                                            className={
                                                                isGlowing
                                                                    ? 'inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-indigo-300 text-indigo-700 bg-indigo-50 animate-pulse ring-2 ring-indigo-400'
                                                                    : 'inline-flex items-center justify-center w-5 h-5 rounded-full text-[11px] font-bold border border-gray-300 text-gray-600 bg-white hover:bg-gray-100'
                                                            }
                                                            aria-label={`Info: ${h}`}
                                                        >
                                                            i
                                                        </button>
                                                    )}
                                                    {activeHeaderHelp?.label === h && (
                                                        <div className="absolute z-20 top-full mt-2 left-0 w-72 p-3 rounded-lg border border-gray-200 bg-white shadow-lg text-xs text-gray-700">
                                                            <div className="flex items-start justify-between gap-2">
                                                                <div className="font-semibold text-gray-900">{activeHeaderHelp.label}</div>
                                                                <button
                                                                    type="button"
                                                                    onClick={(e) => {
                                                                        e.preventDefault();
                                                                        e.stopPropagation();
                                                                        setActiveHeaderHelp(null);
                                                                    }}
                                                                    className="text-gray-500 hover:text-gray-800"
                                                                    aria-label="Close"
                                                                >
                                                                    ✕
                                                                </button>
                                                            </div>
                                                            <div className="mt-2 leading-snug">{activeHeaderHelp.text}</div>
                                                        </div>
                                                    )}
                                                </div>
                                            </th>
                                        );
                                    })()
                                ))}
                            </tr>
                        )}
                    </thead>
                    <tbody>
                        {rows.map((row, rIdx) => (
                            <tr key={rIdx}>
                                {(Array.isArray(row) ? row : []).map((cell, cIdx) => {
                                    const cellId = cell?.cell_id || `t${tableIndex}_r${rIdx}_c${cIdx}`;
                                    const editable = isReference ? false : Boolean(cell?.editable);
                                    const evalStyle = getEvalCellStyle(evaluationState, cellId);
                                    const rawValue = isReference ? (cell?.value || '') : (cells[String(cellId)] ?? (cell?.value || ''));
                                    const value = (evalStyle.displayValue != null && editable) ? evalStyle.displayValue : rawValue;
                                    const displayValue = value;

                                    const expectedMap = getExpectedByCellId(q);
                                    const derivationMap = q?.derivation_map || {};
                                    const expected = expectedMap[cellId];
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
                                    const showCellHintButton = g9EmsScaffoldShowHint && marking.isPracticeMode && editable && cellHintSections.length > 0;
                                    const cellTextAlign = getTrialBalanceCellTextAlign({
                                        journalType,
                                        headers,
                                        row,
                                        colIndex: cIdx,
                                    });
                                    
                                    let cellBorder = 'none';
                                    let cellBg = '';
                                    let isIncorrect = false;

                                    if (showCheckHighlights && editable && expected !== undefined) {
                                        let hit = false;
                                        const got = value;
                                        if (normalizeText(got) === normalizeText(expected)) hit = true;
                                        else if (isNumericExpected(expected) && numbersMatch(got, (typeof expected === 'number' ? expected : toNumber(expected)), { allowRoundedRand: true })) hit = true;
                                        
                                        if (!hit && String(got).trim() !== String(expected).trim()) {
                                            cellBorder = '2px solid #ef4444';
                                            cellBg = '#fef2f2';
                                            isIncorrect = true;
                                        } else if (hit && String(got).trim() !== '') {
                                            cellBorder = '2px solid #10b981';
                                            cellBg = '#ecfdf5';
                                        }
                                    }

                                    const isActiveMemo = showMemo && isIncorrect && editable;
                                    const finalInputVal = Array.isArray(isActiveMemo ? expected : value)
                                        ? (isActiveMemo ? expected : value).join(' / ')
                                        : (isActiveMemo ? expected : value);
                                    const memoTooltip = derivationMap[cellId] || `Expected: ${expected}`;

                                    return (
                                        <td key={cIdx} style={journalBodyCellStyle}>
                                            {editable ? (
                                                <div className="relative h-full w-full flex items-stretch">
                                                    <textarea
                                                        ref={autoResizeJournalTextarea}
                                                        value={finalInputVal}
                                                        onChange={(e) => {
                                                            setCell(cellId, e.target.value);
                                                            autoResizeJournalTextarea(e.target);
                                                        }}
                                                        onInput={(e) => autoResizeJournalTextarea(e.target)}
                                                        rows={1}
                                                        style={{ width: '100%', minHeight: '2.25rem', padding: '6px', border: cellBorder, outline: 'none', boxSizing: 'border-box', textAlign: cellTextAlign || 'center', fontSize: '0.875rem', backgroundColor: cellBg, resize: 'none', overflow: 'hidden', whiteSpace: 'pre-wrap', overflowWrap: 'anywhere', wordBreak: 'break-word', ...evalStyle.input }}
                                                        placeholder=""
                                                        readOnly={evaluationState?.isComparing || showMemo}
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

    const renderJournal = (q) => {
        const journals = Array.isArray(q?.journals)
            ? q.journals
            : (q?.journal ? [q.journal] : []);
        const expectedMap = getExpectedByCellId(q);
        const editableJournals = journals.filter((journal) => {
            const titleFields = Array.isArray(journal?.title_fields) ? journal.title_fields : [];
            const rows = Array.isArray(journal?.rows) ? journal.rows : [];
            const hasEditableTitleField = titleFields.some((field) => {
                const cellId = field?.cell_id;
                if (!cellId) return false;
                if (field?.editable === true) return true;
                return Object.prototype.hasOwnProperty.call(expectedMap, String(cellId));
            });
            const hasEditableCell = rows.some((row) => (Array.isArray(row) ? row : []).some((cell) => Boolean(cell?.editable)));
            return journal?.allow_extra_rows === true || hasEditableTitleField || hasEditableCell;
        });

        return (
            <div>
                {editableJournals.map((j, tIdx) => (
                    <div key={tIdx}>
                        <div className="mt-4 mb-2 text-sm font-semibold text-slate-700">
                            {j?.heading || journalTypeLabel(j?.journal_type)}
                        </div>
                        {renderOneJournalTable({
                            journal: j,
                            q,
                            tableIndex: tIdx,
                            isLastTable: tIdx === editableJournals.length - 1,
                        })}
                    </div>
                ))}
            </div>
        );
    };

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

    const openNonTabularHint = ({ hintKey, label, sections, triggerEl }) => {
        if (!Array.isArray(sections) || sections.length === 0) return;
        const rect = triggerEl?.getBoundingClientRect?.();
        const anchorX = rect ? rect.left : 24;
        const anchorY = rect ? rect.bottom + 10 : 24;
        const next = clampHintPosition(anchorX, anchorY, 320, 240);
        const cellId = `memo_${hintKey}`;
        setActiveCellHint((prev) => {
            if (prev?.cellId === cellId) return null;
            return {
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

    const typedHintSections = question?.question_type === 'typed' ? buildTypedHintSections(question) : [];
    const calcHintText = String(question?.derivation_map?.value || '').trim();
    const nonTabularHintItems = question && (
        question.question_type === 'typed'
        || question.question_type === 'calc'
        || question.question_type === 'journal'
        || question.question_type === 'ledger'
    )
        ? buildNonTabularHintItems(question)
        : [];

    return (
        <div className="w-full">
            <div className="flex items-center justify-between mb-4">
                <h3 className="text-xl font-bold text-slate-800">Scaffold Mode</h3>

                {question && (
                    <div className="flex flex-wrap items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200 opacity-80">
                        <span className="text-sm font-semibold text-slate-700">Assessment:</span>
                        <button
                            type="button"
                            disabled
                            className="relative inline-flex h-6 w-11 items-center rounded-full bg-slate-200 cursor-not-allowed"
                        >
                            <span className="inline-block h-4 w-4 transform rounded-full bg-white translate-x-1" />
                        </button>
                        <span className="text-sm text-slate-600">Scaffold only</span>
                        <span className="text-xs text-slate-500">Assessment available in Pro package</span>
                    </div>
                )}
            </div>

            <div className="mb-4 p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-3">
                <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
                    <div>
                        <div className="text-xs font-semibold uppercase tracking-wide text-slate-500">Scaffold difficulty</div>
                        <div className="mt-2 flex flex-wrap items-center gap-2">
                            {SCAFFOLD_DIFFICULTY_ORDER.map((level) => {
                                const isActive = currentDifficulty === level;
                                return (
                                    <button
                                        key={level}
                                        type="button"
                                        onClick={() => {
                                            setg9EmsScaffoldDifficulty(level);
                                            setPendingDifficultyPromotion(null);
                                            setDifficultyNotice(`Difficulty set to ${level}.`);
                                        }}
                                        className={`px-3 py-1.5 rounded-lg text-sm font-semibold border transition-colors ${isActive ? 'bg-indigo-600 border-indigo-600 text-white' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-100'}`}
                                    >
                                        {formatDifficultyLabel(level)}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                    <div className="flex flex-col gap-2 items-start lg:items-end">
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
                            {keepCurrentDifficulty ? `Keep ${formatDifficultyLabel(currentDifficulty)} Mode` : 'Allow Auto Progression'}
                        </button>
                        <div className="text-xs text-slate-500">
                            {nextDifficulty
                                ? `${attemptsTowardNextLevel}/5 checked questions at ${currentDifficulty} before the next automatic move to ${nextDifficulty}.`
                                : 'Hard is the highest difficulty level.'}
                        </div>
                    </div>
                </div>
                {difficultyNotice && (
                    <div className="text-sm text-indigo-800 bg-indigo-50 border border-indigo-200 rounded-lg px-3 py-2">
                        {difficultyNotice}
                    </div>
                )}
            </div>

            {marking.markingError && (
                <div className="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg break-words">
                    {marking.markingError}
                </div>
            )}

            {/* Super Admin Seed Input — only visible to owner accounts */}
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
                            value={g9EmsScaffoldSeed || ''}
                            onChange={(e) => setg9EmsScaffoldSeed(e.target.value)}
                            className="w-32 px-2 py-1 border border-amber-300 rounded-lg text-sm bg-white focus:outline-none focus:ring-2 focus:ring-amber-400"
                            placeholder="e.g. 42"
                        />
                    </label>
                    <button
                        onClick={() => {
                            const chosen = (g9EmsSubskill || '').trim();
                            const effectiveSubskill = chosen && chosen !== 'auto'
                                ? chosen
                                : (selectedSubtopic?.key || 'mixed');
                            fetchGrade9EmsScaffoldQuestion({
                                subskill: effectiveSubskill,
                                difficulty: g9EmsScaffoldDifficulty,
                                seed: g9EmsScaffoldSeed,
                                question_type: adminFormat,
                            });
                        }}
                        className="px-4 py-1.5 bg-amber-600 text-white text-sm rounded-lg font-semibold shadow-sm hover:bg-amber-700 hover:shadow transition-all"
                    >
                        Generate Validation Test
                    </button>
                    <button
                        onClick={() => {
                            setg9EmsScaffoldSeed('');
                            setAdminFormat('mixed');
                        }}
                        className="px-3 py-1.5 bg-white border border-amber-300 text-amber-700 text-sm rounded-lg font-medium hover:bg-amber-100 transition-colors"
                    >
                        Clear
                    </button>
                    {(g9EmsScaffoldSeed || adminFormat !== 'mixed') && (
                        <span className="text-xs text-amber-700 font-mono bg-amber-100/80 border border-amber-200 px-2 py-0.5 rounded shadow-sm">
                            config={adminFormat}:seed={g9EmsScaffoldSeed || 'rand'}
                        </span>
                    )}
                </div>
            )}

            {g9EmsScaffoldError && (
                <div className="mt-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-xl text-sm break-words">
                    {g9EmsScaffoldError}
                </div>
            )}

            {!question && !g9EmsScaffoldLoading && (
                <div className="mt-6 space-y-3">
                    <div className="text-slate-500 text-sm">Click "New Example" to load a question for this step.</div>
                    <button
                        type="button"
                        onClick={newExample}
                        className="px-5 py-2 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 transition-colors shadow-sm"
                    >
                        New Example
                    </button>
                </div>
            )}

            {question && (
                <div className="space-y-4" onKeyDown={handleAnswerKeyDown}>

                    {g9EmsScaffoldShowHint && (question?.question_type === 'journal' || question?.question_type === 'ledger') && question?.journal?.column_help && Object.keys(question.journal.column_help).length > 0 && marking.isPracticeMode && (
                        <div className="p-3 bg-white border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Table guide</div>
                            <div className="mt-1 text-xs text-slate-500">What each column means for this table format.</div>
                            <div className="mt-2 grid grid-cols-1 sm:grid-cols-2 gap-2">
                                {Object.entries(question.journal.column_help).map(([k, v]) => (
                                    <div key={k} className="text-sm">
                                        <div className="font-semibold text-slate-700">{k}</div>
                                        <div className="text-slate-500">{v}</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    )}

                    {g9EmsScaffoldShowHint && (question?.question_type === 'journal' || question?.question_type === 'ledger') && question?.cell_hints && Object.keys(question.cell_hints).length > 0 && marking.isPracticeMode && (
                        <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-xl text-sm text-yellow-900">
                            Cell hints are available directly on supported table inputs via the `i` badges.
                        </div>
                    )}

                    {g9EmsScaffoldShowHint && question?.question_type === 'typed' && typedHintSections.length > 0 && marking.isPracticeMode && (
                        <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
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

                    {g9EmsScaffoldShowHint && question?.question_type === 'calc' && calcHintText && marking.isPracticeMode && (
                        <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-xl">
                            <div className="font-semibold text-yellow-900">Calculation hint</div>
                            <div className="mt-2 text-sm text-yellow-900 whitespace-pre-line">{calcHintText}</div>
                        </div>
                    )}

                    {question.question_type === 'mcq' && (
                        <div className="grid grid-cols-1 gap-2">
                            {(Array.isArray(question.options) ? question.options : []).map((opt, idx) => {
                                const isSelected = String(g9EmsScaffoldAnswer) === String(idx);
                                const isCorrect = String(question.correct_index) === String(idx);
                                let overrideStyle = "";
                                if (showCheckHighlights && isSelected && !isCorrect) overrideStyle = "ring-2 ring-red-500 bg-red-50 rounded-xl";
                                if (showCheckHighlights && isCorrect) overrideStyle = "ring-2 ring-emerald-500 bg-emerald-50 rounded-xl";
                                return (
                                    <div key={idx} className={overrideStyle}>
                                        <MCQOption
                                            selected={isSelected}
                                            onClick={() => setAnswerValue(String(idx))}
                                            label={opt}
                                        />
                                    </div>
                                );
                            })}
                        </div>
                    )}

                    {question.question_type === 'typed' && (
                        <div className="space-y-3">
                            <textarea
                                ref={activeInputRef}
                                value={g9EmsScaffoldAnswer || ''}
                                onFocus={() => { if (localStorage.getItem('mathKeypadSettings_disableAutoPopup') !== 'true') setIsKeypadVisible(true); }}
                                onChange={(e) => setAnswerValue(e.target.value)}
                                className="w-full min-h-[140px] p-4 text-slate-700 bg-slate-50 border border-slate-200 rounded-xl text-base focus:outline-none focus:ring-2 focus:ring-indigo-500/50 focus:bg-white transition-colors"
                                placeholder="Type your explanation here..."
                            />
                            <div className="flex justify-end">
                                <button 
                                    onClick={() => setIsKeypadVisible(!isKeypadVisible)}
                                    className="px-3 py-1.5 text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-200 rounded-lg hover:bg-indigo-100 transition-colors"
                                >
                                    {isKeypadVisible ? 'Hide Keypad' : 'Show Math Keypad'}
                                </button>
                            </div>
                        </div>
                    )}

                    {question.question_type === 'calc' && (() => {
                        const gotN = toNumber(g9EmsScaffoldAnswer);
                        const expN = Number(question.correct_value);
                        const isIncorrect = showCheckHighlights && (gotN === null || !numbersMatch(gotN, expN, {
                            allowRoundedRand: String(question.unit || '').toUpperCase().includes('R'),
                        }));
                        return (
                            <div className="space-y-3">
                                <input
                                    ref={activeInputRef}
                                    value={showMemo ? question.correct_value : (g9EmsScaffoldAnswer || '')}
                                    onFocus={() => { if (localStorage.getItem('mathKeypadSettings_disableAutoPopup') !== 'true') setIsKeypadVisible(true); }}
                                    onChange={(e) => setAnswerValue(e.target.value)}
                                    className={`w-full p-4 border rounded-xl text-lg font-medium tracking-wide focus:outline-none focus:ring-2 transition-all ${isIncorrect ? 'bg-red-50 border-red-300 text-red-900 focus:ring-red-400' : 'bg-slate-50 border-slate-200 text-slate-800 focus:bg-white focus:ring-indigo-500/50'}`}
                                    placeholder="Enter numerical amount..."
                                    readOnly={showMemo}
                                />
                                <div className="flex justify-end">
                                    <button 
                                        onClick={() => setIsKeypadVisible(!isKeypadVisible)}
                                        className="px-3 py-1.5 text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-200 rounded-lg hover:bg-indigo-100 transition-colors"
                                    >
                                        {isKeypadVisible ? 'Hide Keypad' : 'Show Math Keypad'}
                                    </button>
                                </div>
                                {showMemo && nonTabularHintItems.length > 0 && (
                                    <div className="mt-3 p-3 bg-indigo-50/80 border border-indigo-100 rounded-lg text-sm text-indigo-800 space-y-3 relative z-50">
                                        {nonTabularHintItems.map((item, itemIdx) => (
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
                    })()}

                    {(question?.question_type === 'journal' || question?.question_type === 'ledger') && renderJournal(question)}

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

                    {question?.question_type === 'match' && (
                        <MatchQuestionUI 
                            question={question}
                            answer={g9EmsScaffoldAnswer}
                            setAnswer={(newAns) => setAnswerValue(newAns)}
                            readOnly={showMemo}
                            showCheckHighlights={showCheckHighlights}
                        />
                    )}

                    {question?.question_type === 'word_bank' && (
                        <WordBankQuestionUI 
                            question={question}
                            answer={g9EmsScaffoldAnswer}
                            setAnswer={(newAns) => setAnswerValue(newAns)}
                            readOnly={showMemo}
                            showCheckHighlights={showCheckHighlights}
                        />
                    )}

                    {question?.question_type === 'inline_fill' && (
                        <InlineFillQuestionUI 
                            question={question}
                            answer={g9EmsScaffoldAnswer}
                            setAnswer={(newAns) => setAnswerValue(newAns)}
                            readOnly={showMemo}
                            showCheckHighlights={showCheckHighlights}
                        />
                    )}

                    {/* Scaffold Answer Validation Result */}
                    <div className="mt-6 flex items-center justify-between">
                        <div className="flex items-center gap-3">
                            {/* Redo button: available only after check, resets answer to pre-check state */}
                            {showCheckHighlights && preCheckAnswer !== null && (
                                <button
                                    onClick={() => {
                                        setAnswerValue(preCheckAnswer);
                                        setShowCheckHighlights(false);
                                        setShowMemo(false);
                                        setg9EmsScaffoldFeedback(null);
                                    }}
                                    className="px-4 py-2 text-sm font-medium text-amber-700 hover:text-amber-900 border border-amber-200 hover:border-amber-400 bg-amber-50 hover:bg-amber-100 rounded-lg transition-colors"
                                >
                                    ↺ Redo
                                </button>
                            )}
                            {(showCheckHighlights || question?.question_type === 'typed') && question?.question_type !== 'mcq' && (
                                <button
                                    onClick={() => setShowMemo(!showMemo)}
                                    className={`px-4 py-2 text-sm font-medium rounded-lg border transition-colors ${showMemo ? 'bg-indigo-50 border-indigo-200 text-indigo-700 hover:bg-indigo-100/50' : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'}`}
                                >
                                    {showMemo ? 'Hide Memo' : 'Compare / Memo'}
                                </button>
                            )}
                        </div>
                        <div className="flex items-center gap-3">
                            <button
                                type="button"
                                onClick={newExample}
                                className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-lg text-sm font-medium transition-colors"
                            >
                                {question ? 'Next Question' : 'New Example'}
                            </button>
                            {marking.isPracticeMode ? (
                                question && (
                                    <button
                                    onClick={checkAnswerWithFlagging}
                                        disabled={question?.question_type === 'typed'
                                            ? String(g9EmsScaffoldAnswer || '').trim() === ''
                                            : (!g9EmsScaffoldAnswer || String(g9EmsScaffoldAnswer).trim() === '')}
                                        className="px-6 py-2 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm"
                                    >
                                        Check
                                    </button>
                                )
                            ) : (
                                !marking.isMarkingSubmitted && question && (
                                    <button
                                        onClick={() => marking.submitAssessment([question])}
                                        disabled={marking.isSubmitting}
                                        className="px-6 py-2 bg-indigo-600 text-white text-sm font-medium rounded-lg hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-sm"
                                    >
                                        {marking.isSubmitting ? 'Submitting...' : 'Submit Assessment'}
                                    </button>
                                )
                            )}
                            <button
                                onClick={() => setg9EmsScaffoldShowHint(!g9EmsScaffoldShowHint)}
                                className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-800 rounded-lg text-sm font-medium transition-colors"
                            >
                                {g9EmsScaffoldShowHint ? 'Hide hint' : 'Hint'}
                            </button>
                            <button
                                onClick={() => setg9EmsScaffoldFeedback(null)}
                                className="px-4 py-2 bg-white border border-slate-200 hover:bg-slate-50 text-slate-600 rounded-lg text-sm font-medium transition-colors"
                            >
                                Clear feedback
                            </button>
                        </div>
                    </div>

                    {g9EmsScaffoldFeedback && marking.isPracticeMode && question?.question_type !== 'typed' && (
                        <div className={`rounded-xl p-3 border text-sm ${g9EmsScaffoldFeedback.kind === 'success' ? 'bg-emerald-50 border-emerald-200 text-emerald-900' : g9EmsScaffoldFeedback.kind === 'error' ? 'bg-red-50 border-red-200 text-red-900' : 'bg-slate-50 border-slate-200 text-slate-800'}`}>
                            <div className="font-semibold">Feedback</div>
                            <div className="text-sm mt-1">{g9EmsScaffoldFeedback.message}</div>
                        </div>
                    )}
                    {g9EmsScaffoldFeedback && marking.isPracticeMode && question?.question_type === 'typed' && (
                        <div className="rounded-xl p-3 border text-sm bg-slate-50 border-slate-200 text-slate-800">
                            <div className="font-semibold">Feedback</div>
                            <div className="text-sm mt-1">{g9EmsScaffoldFeedback.message}</div>
                        </div>
                    )}
                    {question?.question_type === 'typed' && marking.isPracticeMode && (
                        <div className="mt-4 p-3 rounded-xl text-sm border bg-slate-50 border-slate-200 text-slate-600">
                            ⭐ AI-graded feedback available in Pro subscription
                        </div>
                    )}

                    {question.question_type === 'typed' && showMemo && nonTabularHintItems.length > 0 && (
                        <div className="p-3 bg-slate-50 border border-slate-200 rounded-xl">
                            <div className="font-semibold text-slate-800">Sample answer</div>
                            <div className="mt-3 space-y-3 text-sm text-slate-700">
                                {nonTabularHintItems.map((item, itemIdx) => (
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
                        </div>
                    )}
                </div>
            )}

            {/* Marking Results Overlay/Summary */}
            {marking.isMarkingSubmitted && marking.markingResults && question && (
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
                    <p className="text-indigo-800 text-sm">
                        Review your specific section answer. The feedback is now displayed securely from the backend!
                    </p>

                    {/* Specific question feedback from backend */}
                    {marking.getFeedbackForQuestion(question.id) && (
                        <div className={`mt-4 p-4 rounded-xl border ${marking.getFeedbackForQuestion(question.id).kind === 'success' ? 'bg-green-50 border-green-200 text-green-800' : 'bg-red-50 border-red-200 text-red-800'}`}>
                            {marking.getFeedbackForQuestion(question.id).message}
                        </div>
                    )}
                </div>
            )}
            
            <EnhancedMathKeypad 
                isVisible={isKeypadVisible}
                onClose={() => setIsKeypadVisible(false)}
                inputRef={activeInputRef}
                onExpressionChange={(val) => {
                    setAnswerValue(val);
                }}
            />
        </div>
    );
};

export default Grade9EmsScaffold;


