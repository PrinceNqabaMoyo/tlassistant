import { useState, useCallback, useMemo } from 'react';

/**
 * useEvaluationCheck — shared hook for deterministic Check/Compare evaluation.
 *
 * How it works:
 *   1. "Check" compares user answers to correct_map values
 *   2. Incorrect cells get flagged → clickable for rubric_map breakdown
 *   3. "Compare" swaps cell values between user input and correct answers
 *
 * @param {Object} params
 * @param {Object} params.question — backend question with correct_map + rubric_map
 * @param {Object} params.userAnswers — { cellId: userValue } map
 * @returns evaluation state and handlers
 */

// ── Normalisation helpers (shared with scaffolds) ──

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

const isNumericExpected = (expected) => {
    if (expected === null || expected === undefined) return false;
    if (typeof expected === 'number') return true;
    const s = String(expected).trim();
    if (!s) return false;
    return /^-?\d+(?:\.\d+)?$/.test(s.replace(/\s/g, '').replace(/[Rr]/g, ''));
};

/**
 * Compare a single user value against the expected (correct) value.
 * Supports numeric tolerance and text normalisation.
 */
const compareValues = (userValue, expectedValue, tolerance = 0.01) => {
    const userStr = normalizeText(userValue);
    const expectedStr = normalizeText(expectedValue);

    // Empty check — if user hasn't typed anything
    if (!userStr && expectedStr) return false;
    if (!userStr && !expectedStr) return true;

    // Exact text match
    if (userStr === expectedStr) return true;

    // Numeric comparison with tolerance
    if (isNumericExpected(expectedValue)) {
        const userNum = toNumber(userValue);
        const expectedNum = toNumber(expectedValue);
        if (userNum !== null && expectedNum !== null) {
            return Math.abs(userNum - expectedNum) <= tolerance;
        }
    }

    // Strip parentheticals for partial match
    // e.g. "Bank (CRJ)" matches "bank (crj)" or "bank"
    const expectedBase = expectedStr.replace(/\([^)]*\)/g, '').trim();
    const userBase = userStr.replace(/\([^)]*\)/g, '').trim();
    if (expectedBase && userBase === expectedBase) return true;

    return false;
};

// ── Hook ──

export const useEvaluationCheck = ({ question, userAnswers }) => {
    const [checkResults, setCheckResults] = useState(null);    // { cellId: { correct, expected, userValue, rubric } }
    const [isChecked, setIsChecked] = useState(false);
    const [isComparing, setIsComparing] = useState(false);
    const [selectedCell, setSelectedCell] = useState(null);     // cellId for rubric overlay

    // Extract maps from question
    const correctMap = useMemo(() => {
        return (question?.correct_map && typeof question.correct_map === 'object')
            ? question.correct_map
            : {};
    }, [question]);

    const rubricMap = useMemo(() => {
        return (question?.rubric_map && typeof question.rubric_map === 'object')
            ? question.rubric_map
            : {};
    }, [question]);

    /**
     * handleCheck — evaluate all user answers against correct_map
     */
    const handleCheck = useCallback(() => {
        const results = {};
        let totalCells = 0;
        let correctCount = 0;

        for (const [cellId, expectedValue] of Object.entries(correctMap)) {
            const userValue = userAnswers?.[cellId] ?? '';
            const correct = compareValues(userValue, expectedValue);
            totalCells++;
            if (correct) correctCount++;

            results[cellId] = {
                correct,
                expected: expectedValue,
                userValue,
                rubric: rubricMap[cellId] || null,
            };
        }

        setCheckResults(results);
        setIsChecked(true);
        setIsComparing(false);

        return { results, totalCells, correctCount, score: totalCells > 0 ? correctCount / totalCells : 0 };
    }, [correctMap, rubricMap, userAnswers]);

    /**
     * handleCompare — toggle between showing user answers and correct answers
     */
    const handleCompare = useCallback(() => {
        setIsComparing(prev => !prev);
    }, []);

    /**
     * handleCellClick — open rubric overlay for a specific incorrect cell
     */
    const handleCellClick = useCallback((cellId) => {
        if (!checkResults?.[cellId]) return;
        if (checkResults[cellId].correct) return; // no overlay for correct cells
        setSelectedCell(cellId === selectedCell ? null : cellId);
    }, [checkResults, selectedCell]);

    /**
     * closeOverlay — dismiss the rubric overlay
     */
    const closeOverlay = useCallback(() => {
        setSelectedCell(null);
    }, []);

    /**
     * getCellStatus — returns styling hints for a cell
     * @returns {{ isCorrect: boolean|null, isIncorrect: boolean|null, displayValue: string }}
     */
    const getCellStatus = useCallback((cellId, originalValue) => {
        if (!isChecked || !checkResults) {
            return { isCorrect: null, isIncorrect: null, displayValue: originalValue ?? '' };
        }

        const result = checkResults[cellId];
        if (!result) {
            return { isCorrect: null, isIncorrect: null, displayValue: originalValue ?? '' };
        }

        // In compare mode, swap values
        const displayValue = isComparing ? String(result.expected ?? '') : (originalValue ?? '');

        return {
            isCorrect: result.correct,
            isIncorrect: !result.correct,
            displayValue,
            hasRubric: !!result.rubric,
        };
    }, [isChecked, isComparing, checkResults]);

    /**
     * Reset evaluation state (e.g. when generating a new question)
     */
    const resetEvaluation = useCallback(() => {
        setCheckResults(null);
        setIsChecked(false);
        setIsComparing(false);
        setSelectedCell(null);
    }, []);

    // Summary stats
    const summary = useMemo(() => {
        if (!checkResults) return null;
        const entries = Object.values(checkResults);
        const total = entries.length;
        const correct = entries.filter(e => e.correct).length;
        return {
            total,
            correct,
            incorrect: total - correct,
            percentage: total > 0 ? Math.round((correct / total) * 100) : 0,
        };
    }, [checkResults]);

    return {
        // State
        checkResults,
        isChecked,
        isComparing,
        selectedCell,
        summary,

        // Handlers
        handleCheck,
        handleCompare,
        handleCellClick,
        closeOverlay,
        resetEvaluation,

        // Cell helpers
        getCellStatus,
    };
};

export default useEvaluationCheck;
