import { useEffect, useState } from 'react';

const GENERATE = '/api/mathematics/grade10/generate';
const SECTIONS = '/api/mathematics/grade10/sections';
const MARK = '/api/mathematics/grade10/mark';

/**
 * Controller for a Grade 10 Mathematics topic. Handles scaffold (one question
 * per curriculum section) and practice (a mixed batch), plus marking via the
 * SymPy-backed ``/mark`` endpoint (which routes to the procedure tracker for
 * step questions).
 */
export const createMathController = ({ topicKey, scaffoldMode }) => ({ workspaceMode, buildApiUrl }) => {
    const isScaffold = workspaceMode === scaffoldMode;

    const [sections, setSections] = useState([]);
    const [scaffoldStepIndex, setScaffoldStepIndex] = useState(0);
    const [scaffoldDifficulty, setScaffoldDifficulty] = useState('medium');
    const [practiceDifficulty, setPracticeDifficulty] = useState('medium');

    const [question, setQuestion] = useState(null);
    const [practiceQuestions, setPracticeQuestions] = useState([]);
    const [practiceIndex, setPracticeIndex] = useState(0);

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);
    const [marking, setMarking] = useState(false);

    useEffect(() => {
        if (!isScaffold) return;
        let cancelled = false;
        (async () => {
            try {
                const res = await fetch(buildApiUrl(`${SECTIONS}?topic=${encodeURIComponent(topicKey)}`));
                const data = await res.json();
                if (!cancelled) setSections(data?.steps || []);
            } catch {
                if (!cancelled) setSections([]);
            }
        })();
        return () => { cancelled = true; };
    }, [isScaffold, topicKey, buildApiUrl]);

    const _generate = async (body) => {
        const res = await fetch(buildApiUrl(GENERATE), {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topicKey, ...body }),
        });
        if (!res.ok) throw new Error(`Generation failed: HTTP ${res.status}`);
        const data = await res.json();
        if (!data?.questions) throw new Error(data?.error || 'Generation failed');
        return data.questions;
    };

    const fetchScaffoldQuestion = async ({ subskill, difficulty } = {}) => {
        setLoading(true); setError(null); setResult(null);
        try {
            const sub = subskill || sections?.[scaffoldStepIndex]?.key || 'concepts';
            const qs = await _generate({ subskill: sub, difficulty: difficulty || scaffoldDifficulty, count: 1 });
            setQuestion(qs[0] || null);
        } catch (err) {
            setError(err?.message || String(err));
        } finally {
            setLoading(false);
        }
    };

    const fetchPractice = async ({ difficulty } = {}) => {
        setLoading(true); setError(null); setResult(null);
        try {
            const qs = await _generate({ subskill: 'mixed', difficulty: difficulty || practiceDifficulty, count: 5 });
            setPracticeQuestions(qs);
            setPracticeIndex(0);
            setQuestion(qs[0] || null);
        } catch (err) {
            setError(err?.message || String(err));
        } finally {
            setLoading(false);
        }
    };

    const gotoPractice = (idx) => {
        const clamped = Math.max(0, Math.min(idx, practiceQuestions.length - 1));
        setPracticeIndex(clamped);
        setQuestion(practiceQuestions[clamped] || null);
        setResult(null);
    };

    const check = async (answer) => {
        if (!question) return;
        setMarking(true);
        try {
            const res = await fetch(buildApiUrl(MARK), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ questions: [question], answers: { [question.id]: answer } }),
            });
            const data = await res.json();
            setResult(data?.results?.[question.id] || null);
        } catch (err) {
            setError(err?.message || String(err));
        } finally {
            setMarking(false);
        }
    };

    return {
        isScaffold,
        sections,
        scaffoldStepIndex, setScaffoldStepIndex,
        scaffoldDifficulty, setScaffoldDifficulty,
        practiceDifficulty, setPracticeDifficulty,
        question,
        practiceQuestions, practiceIndex, gotoPractice,
        loading, error, result, marking,
        fetchScaffoldQuestion, fetchPractice, check,
    };
};
