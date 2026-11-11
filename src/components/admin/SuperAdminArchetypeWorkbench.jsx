import React, { useState, useEffect, useRef, useMemo } from 'react';

import { getAuth } from 'firebase/auth';

import { 

    ChevronLeft, ChevronRight, CheckCircle2, AlertTriangle, XCircle, RefreshCw, 

    Layers, Search, Sliders, Eye, Sparkles, ShieldCheck, Check, 

    BookOpen, HelpCircle, FileCheck, Award, Tag, Filter, Grid, Code

} from 'lucide-react';

import { buildApiUrl } from '../../utils/apiBaseUrl';

import DiagramRenderer from '../workspace/shared/mathx/DiagramRenderer';

import MathText from '../workspace/shared/mathx/MathText';



const OWNER_EMAILS = ['princenqaba@gmail.com', 'princenqabamoyo@outlook.com'];



function formatQuestionSolutionText(q) {

    if (!q) return 'N/A';

    const base = q.worked_solution || q.explanation || (typeof q.canonical_solution === 'string' ? q.canonical_solution : '') || q.sample_answer || (typeof q.canonical_solution === 'string' ? q.canonical_solution : '') || q.correct_answer || '';

    const steps = q.canonical_solution && typeof q.canonical_solution === 'object' && Array.isArray(q.canonical_solution.steps)

        ? q.canonical_solution.steps

        : [];

    if (steps.length > 0) {

        const stepsFormatted = steps

            .map((s, idx) => {

                const expr = s.to_latex ? `$${s.to_latex}$` : (s.text || '');

                const reason = s.reason ? ` (${s.reason})` : '';

                return `Step ${s.step || idx + 1}: ${expr}${reason}`;

            })

            .join('\n');

        return base ? `${base}\n\n${stepsFormatted}` : stepsFormatted;

    }

    return String(base || 'N/A');

}



export default function SuperAdminArchetypeWorkbench({ currentUser, onBack, initialTab = 'iteration' }) {

    const isOwner = OWNER_EMAILS.includes(currentUser?.email?.toLowerCase()) || Boolean(currentUser?.isOwner);



    // Primary Workbench Tab: 'iteration' (Archetype Iteration Studio) vs 'diagrams' (Diagram Visual Desk)

    const [workbenchTab, setWorkbenchTab] = useState(initialTab || 'iteration');



    // Catalog & Curriculum data

    const [catalog, setCatalog] = useState([]);

    const [curriculumTopics, setCurriculumTopics] = useState([]);

    const [archetypes, setArchetypes] = useState([]);

    const [diagramMasters, setDiagramMasters] = useState([]);

    const [summary, setSummary] = useState(null);

    const [recentReviews, setRecentReviews] = useState([]);

    const [loadingCatalog, setLoadingCatalog] = useState(true);



    // Iteration Selection Filters

    const [iterationSubject, setIterationSubject] = useState('Mathematical Literacy');

    const [iterationGrade, setIterationGrade] = useState('10');

    const [iterationTopicName, setIterationTopicName] = useState('Conversions and time');



    // Diagram filter states

    const [selectedSubject, setSelectedSubject] = useState('ALL');

    const [selectedGrade, setSelectedGrade] = useState('ALL');

    const [selectedDiagramMaster, setSelectedDiagramMaster] = useState('ALL');

    const [selectedTopicFilter, setSelectedTopicFilter] = useState('ALL');

    const [searchQuery, setSearchQuery] = useState('');

    const [selectedTopic, setSelectedTopic] = useState('grade10_mathlit_conversions_and_time');

    const [selectedArchetype, setSelectedArchetype] = useState(null);



    // PRNG Generator states

    const [seed, setSeed] = useState(() => Math.floor(Math.random() * 900000) + 100000);

    const [generatingKey, setGeneratingKey] = useState(null);

    const genSeqRef = useRef(0);

    const [currentQuestions, setCurrentQuestions] = useState([]);

    const [errorMsg, setErrorMsg] = useState(null);

    const [activeQuestionIdx, setActiveQuestionIdx] = useState(0);

    const [workbenchAllowViewSwitch, setWorkbenchAllowViewSwitch] = useState(false);

    const [showRawJson, setShowRawJson] = useState(false);



    // Archetype Iteration state (Phase 4 Workflow)

    const [isIterationMode, setIsIterationMode] = useState(true);

    const [iterationIndex, setIterationIndex] = useState(0);

    const [iterationCycle, setIterationCycle] = useState(1);

    const [iterationSubskills, setIterationSubskills] = useState([]);
    const [selectedLearnerOption, setSelectedLearnerOption] = useState(null);
    const [showDiagnosticHints, setShowDiagnosticHints] = useState(false);

    const [loadingSubskills, setLoadingSubskills] = useState(false);



    // Diagram review desk states

    const [verdict, setVerdict] = useState('CERTIFIED');

    const [notes, setNotes] = useState('');

    const [diagramRating, setDiagramRating] = useState(5);

    const [rubricRating, setRubricRating] = useState(5);

    const [hintsRating, setHintsRating] = useState(5);

    const [savingReview, setSavingReview] = useState(false);

    const [saveSuccess, setSaveSuccess] = useState(false);



    // Load catalog on mount

    useEffect(() => {

        if (!isOwner) return;



        const fetchCatalog = async () => {

            setLoadingCatalog(true);

            try {

                const auth = getAuth();

                const token = await auth.currentUser?.getIdToken();

                const res = await fetch(buildApiUrl('/api/admin/vet/catalog'), {

                    headers: {

                        'Authorization': `Bearer ${token}`

                    }

                });

                if (!res.ok) throw new Error(`HTTP ${res.status}`);

                const data = await res.json();

                setCatalog(data.catalog || []);

                const cTopics = data.curriculum_topics || [];

                setCurriculumTopics(cTopics);

                const archs = data.archetypes || [];

                setArchetypes(archs);

                setDiagramMasters(data.diagram_masters || []);

                setSummary(data.summary || null);

                setRecentReviews(data.recent_reviews || []);



                // If in iteration tab, auto-load Grade 10 Mathematical Literacy: Conversions and time

                const defaultTopic = cTopics.find(

                    t => t.subject === 'Mathematical Literacy' && String(t.grade) === '10' && t.name.toLowerCase().includes('conversion')

                ) || cTopics.find(t => t.subject === 'Mathematical Literacy') || cTopics[0];



                if (initialTab === 'iteration' && defaultTopic) {

                    setIterationSubject(defaultTopic.subject);

                    setIterationGrade(String(defaultTopic.grade));

                    setIterationTopicName(defaultTopic.name);

                    const topicKey = defaultTopic.generator_key || defaultTopic.name;

                    setSelectedTopic(topicKey);



                    const subs = await fetchTopicArchetypes(topicKey, String(defaultTopic.grade), defaultTopic.subject);

                    if (subs && subs.length > 0) {

                        const initSeed = Math.floor(Math.random() * 900000) + 100000;
                        setSeed(initSeed);
                        handleGenerate(initSeed, null, topicKey, subs[0], String(defaultTopic.grade), defaultTopic.subject);

                    }

                } else if (archs.length > 0) {

                    setSelectedArchetype(archs[0]);

                }

            } catch (err) {

                console.error('[Workbench] Catalog fetch error:', err);

                setErrorMsg('Failed to fetch generator catalog: ' + err.message);

            } finally {

                setLoadingCatalog(false);

            }

        };



        fetchCatalog();

    }, [isOwner, initialTab]);



    // Fetch topic archetypes for linear iteration mode

    const fetchTopicArchetypes = async (topicKey, gradeVal = iterationGrade, subjectVal = iterationSubject) => {

        if (!topicKey) return [];

        setLoadingSubskills(true);

        try {

            const auth = getAuth();

            const token = await auth.currentUser?.getIdToken();

            const res = await fetch(

                buildApiUrl(`/api/admin/vet/topic-archetypes?topic=${encodeURIComponent(topicKey)}&grade=${encodeURIComponent(gradeVal || '10')}&subject=${encodeURIComponent(subjectVal || 'Mathematical Literacy')}`),

                {

                    headers: {

                        'Authorization': `Bearer ${token}`

                    }

                }

            );

            if (res.ok) {

                const data = await res.json();

                const archs = data.archetypes || [];

                setIterationSubskills(archs);

                return archs;

            }

        } catch (err) {

            console.error('[Workbench] Archetypes fetch error:', err);

        } finally {

            setLoadingSubskills(false);

        }

        return [];

    };



    // Handle question generation with explicit subskill target

    const generationKeyFor = (arch, topic) => (arch ? arch.archetype_id : `topic:${topic}`);

    const handleGenerate = async (

        targetSeed = seed,

        targetArch = selectedArchetype,

        targetTopic = selectedTopic,

        targetSubskill = null,

        targetGrade = iterationGrade,

        targetSubject = iterationSubject

    ) => {

        const topicToUse = targetArch ? targetArch.topic : targetTopic;

        if (!topicToUse && !targetArch) return;

        const genKey = generationKeyFor(targetArch, targetTopic);

        const seq = ++genSeqRef.current;

        setGeneratingKey(genKey);

        setErrorMsg(null);
        setSelectedLearnerOption(null);
        setShowDiagnosticHints(false);

        setSaveSuccess(false);



        try {

            const auth = getAuth();

            const token = await auth.currentUser?.getIdToken();

            const bodyPayload = targetArch ? {

                archetype_id: targetArch.archetype_id,

                topic: targetArch.topic,

                subskill: targetSubskill || targetArch.subskill_param,

                view: targetArch.view,

                seed: targetSeed,

                count: 1

            } : {

                topic: targetTopic,

                subskill: targetSubskill,

                seed: targetSeed,

                count: 1,

                grade: targetGrade || '10',

                subject: targetSubject || 'Mathematical Literacy'

            };



            const res = await fetch(buildApiUrl('/api/admin/vet/generate'), {

                method: 'POST',

                headers: {

                    'Content-Type': 'application/json',

                    'Authorization': `Bearer ${token}`

                },

                body: JSON.stringify(bodyPayload)

            });



            const data = await res.json();

            if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);



            if (seq !== genSeqRef.current) return;

            setCurrentQuestions(data.questions || []);

            setActiveQuestionIdx(0);

        } catch (err) {

            if (seq !== genSeqRef.current) return;

            console.error('[Workbench] Generation error:', err);

            setErrorMsg(err.message);

        } finally {

            if (seq === genSeqRef.current) setGeneratingKey(null);

        }

    };



    // Save review verdict to Firestore (Diagram Desk)

    const handleSaveReview = async () => {

        if (!selectedArchetype && !selectedTopic) return;

        setSavingReview(true);

        setErrorMsg(null);

        setSaveSuccess(false);



        try {

            const auth = getAuth();

            const token = await auth.currentUser?.getIdToken();

            const res = await fetch(buildApiUrl('/api/admin/vet/save-review'), {

                method: 'POST',

                headers: {

                    'Content-Type': 'application/json',

                    'Authorization': `Bearer ${token}`

                },

                body: JSON.stringify({

                    archetype_id: selectedArchetype?.archetype_id,

                    topic: selectedArchetype?.topic || selectedTopic,

                    seed,

                    verdict,

                    notes,

                    diagram_rating: diagramRating,

                    rubric_rating: rubricRating,

                    hints_rating: hintsRating

                })

            });



            const data = await res.json();

            if (!res.ok) throw new Error(data.error || `HTTP ${res.status}`);



            setSaveSuccess(true);

            if (selectedArchetype) {

                setArchetypes(prev => prev.map(a => 

                    a.archetype_id === selectedArchetype.archetype_id ? { ...a, verdict, last_review: data.record } : a

                ));

            }

        } catch (err) {

            console.error('[Workbench] Save review error:', err);

            setErrorMsg('Failed to save review: ' + err.message);

        } finally {

            setSavingReview(false);

        }

    };



    // Archetype Iteration toggle & stepper controls (Phase 4 Workflow)

    const toggleIterationMode = async () => {

        const nextMode = !isIterationMode;

        setIsIterationMode(nextMode);

        if (nextMode) {

            let subs = iterationSubskills;

            if (!subs || subs.length === 0) {

                subs = await fetchTopicArchetypes(selectedTopic, iterationGrade, iterationSubject);

            }

            if (subs && subs.length > 0) {

                setIterationIndex(0);

                setIterationCycle(1);

                const newSeed = Math.floor(Math.random() * 900000) + 100000;
                setSeed(newSeed);
                handleGenerate(newSeed, null, selectedTopic, subs[0], iterationGrade, iterationSubject);

            }

        }

    };



    const handleNextIteration = () => {

        if (!iterationSubskills.length) return;

        let nextIdx = iterationIndex + 1;

        let nextCycle = iterationCycle;

        if (nextIdx >= iterationSubskills.length) {

            nextIdx = 0;

            nextCycle = iterationCycle + 1;

            setIterationCycle(nextCycle);

        }

        setIterationIndex(nextIdx);

        const nextSeed = Math.floor(Math.random() * 900000) + 100000;

        setSeed(nextSeed);

        handleGenerate(nextSeed, null, selectedTopic, iterationSubskills[nextIdx], iterationGrade, iterationSubject);

    };



    const handlePrevIteration = () => {

        if (!iterationSubskills.length) return;

        let prevIdx = iterationIndex - 1;

        let currentCycle = iterationCycle;

        if (prevIdx < 0) {

            prevIdx = iterationSubskills.length - 1;

        }

        setIterationIndex(prevIdx);

        const prevSeed = Math.floor(Math.random() * 900000) + 100000;

        setSeed(prevSeed);

        handleGenerate(prevSeed, null, selectedTopic, iterationSubskills[prevIdx], iterationGrade, iterationSubject);

    };



    // Derived subject & grade lists from authoritative manifest

    const distinctSubjects = useMemo(() => {

        const set = new Set((curriculumTopics || []).map(t => t.subject).filter(Boolean));

        const list = Array.from(set).sort();

        return list.length > 0 ? list : [

            'Mathematical Literacy', 'Mathematics', 'Technical Mathematics',

            'Physical Sciences', 'Life Sciences', 'Natural Sciences',

            'Accounting', 'Economic and Management Sciences', 'Business Studies'

        ];

    }, [curriculumTopics]);



    const distinctGradesForSubject = useMemo(() => {

        const set = new Set(

            (curriculumTopics || [])

                .filter(t => t.subject === iterationSubject)

                .map(t => String(t.grade))

        );

        const list = Array.from(set).sort((a, b) => Number(a) - Number(b));

        return list.length > 0 ? list : ['7', '8', '9', '10', '11', '12'];

    }, [curriculumTopics, iterationSubject]);



    const distinctTopicsForSubjectAndGrade = useMemo(() => {

        return (curriculumTopics || []).filter(

            t => t.subject === iterationSubject && String(t.grade) === String(iterationGrade)

        );

    }, [curriculumTopics, iterationSubject, iterationGrade]);



    // Handle Subject Dropdown Change

    const handleSubjectChange = async (newSubject) => {

        setIterationSubject(newSubject);

        const gradesForNewSubject = Array.from(new Set(

            (curriculumTopics || [])

                .filter(t => t.subject === newSubject)

                .map(t => String(t.grade))

        )).sort((a, b) => Number(a) - Number(b));



        const targetGrade = gradesForNewSubject.includes(iterationGrade)

            ? iterationGrade

            : (gradesForNewSubject[0] || '10');

        setIterationGrade(targetGrade);



        const topics = (curriculumTopics || []).filter(

            t => t.subject === newSubject && String(t.grade) === String(targetGrade)

        );

        if (topics.length > 0) {

            const firstTopic = topics[0];

            setIterationTopicName(firstTopic.name);

            const key = firstTopic.generator_key || firstTopic.name;

            setSelectedTopic(key);

            setIterationIndex(0);

            setIterationCycle(1);

            const subs = await fetchTopicArchetypes(key, targetGrade, newSubject);

            if (subs && subs.length > 0) {

                const sSeed = Math.floor(Math.random() * 900000) + 100000;
                setSeed(sSeed);
                handleGenerate(sSeed, null, key, subs[0], targetGrade, newSubject);

            }

        }

    };



    // Handle Grade Dropdown Change

    const handleGradeChange = async (newGrade) => {

        setIterationGrade(newGrade);

        const topics = (curriculumTopics || []).filter(

            t => t.subject === iterationSubject && String(t.grade) === String(newGrade)

        );

        if (topics.length > 0) {

            const firstTopic = topics[0];

            setIterationTopicName(firstTopic.name);

            const key = firstTopic.generator_key || firstTopic.name;

            setSelectedTopic(key);

            setIterationIndex(0);

            setIterationCycle(1);

            const subs = await fetchTopicArchetypes(key, newGrade, iterationSubject);

            if (subs && subs.length > 0) {

                const gSeed = Math.floor(Math.random() * 900000) + 100000;
                setSeed(gSeed);
                handleGenerate(gSeed, null, key, subs[0], newGrade, iterationSubject);

            }

        }

    };



    // Handle Topic Dropdown Change

    const handleTopicChange = async (newTopicName) => {

        setIterationTopicName(newTopicName);

        const topicObj = distinctTopicsForSubjectAndGrade.find(t => t.name === newTopicName);

        if (topicObj) {

            const key = topicObj.generator_key || topicObj.name;

            setSelectedTopic(key);

            setIterationIndex(0);

            setIterationCycle(1);

            const subs = await fetchTopicArchetypes(key, iterationGrade, iterationSubject);

            if (subs && subs.length > 0) {

                const tSeed = Math.floor(Math.random() * 900000) + 100000;
                setSeed(tSeed);
                handleGenerate(tSeed, null, key, subs[0], iterationGrade, iterationSubject);

            }

        }

    };



    // Filtered lists for Diagram Visual Desk

    const filteredArchetypes = archetypes.filter(item => {

        if (selectedTopicFilter !== 'ALL' && item.topic !== selectedTopicFilter) return false;

        if (selectedSubject !== 'ALL' && item.subject !== selectedSubject) return false;

        if (selectedGrade !== 'ALL' && String(item.grade) !== String(selectedGrade)) return false;

        if (selectedDiagramMaster !== 'ALL' && item.diagram_id !== selectedDiagramMaster) return false;

        if (searchQuery.trim()) {

            const q = searchQuery.toLowerCase();

            const matchId = (item.archetype_id || '').toLowerCase().includes(q);

            const matchTitle = (item.title || '').toLowerCase().includes(q);

            const matchDiag = (item.diagram_id || '').toLowerCase().includes(q);

            const matchTopic = (item.topic || '').toLowerCase().includes(q);

            if (!matchId && !matchTitle && !matchDiag && !matchTopic) return false;

        }

        return true;

    });



    const activeQuestion = currentQuestions[activeQuestionIdx] || null;



    if (!isOwner) {

        return (

            <div className="min-h-screen bg-slate-50 flex items-center justify-center p-6">

                <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8 border border-red-200 text-center">

                    <div className="w-14 h-14 bg-red-100 text-red-600 rounded-full flex items-center justify-center mx-auto mb-4">

                        <AlertTriangle className="w-7 h-7" />

                    </div>

                    <h1 className="text-xl font-bold text-slate-900 mb-2">Access Denied</h1>

                    <p className="text-sm text-slate-600 mb-6">

                        The Super Admin Archetype Workbench is restricted to verified platform owners.

                    </p>

                    {onBack && (

                        <button

                            type="button"

                            onClick={onBack}

                            className="w-full py-2.5 px-4 bg-slate-800 text-white rounded-xl text-sm font-semibold hover:bg-slate-700 transition"

                        >

                            Return to Dashboard

                        </button>

                    )}

                </div>

            </div>

        );

    }



    return (

        <div data-testid="super-admin-archetype-workbench" className="min-h-screen bg-slate-100 text-slate-800">

            {/* TOP APPLICATION HEADER */}

            <header className="sticky top-0 z-30 bg-white border-b border-slate-200 shadow-2xs">

                <div className="max-w-7xl mx-auto px-6 py-3 flex flex-wrap items-center justify-between gap-4">

                    <div className="flex items-center gap-3">

                        {onBack && (

                            <button

                                type="button"

                                onClick={onBack}

                                className="p-2 rounded-lg hover:bg-slate-100 text-slate-600 transition"

                                title="Return to Super Admin Desk"

                            >

                                <ChevronLeft className="w-5 h-5" />

                            </button>

                        )}

                        <div>

                            <div className="flex items-center gap-2">

                                <h1 className="text-base font-bold text-slate-900 tracking-tight">Super Admin Archetype Workbench</h1>

                                <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-blue-100 text-blue-800 border border-blue-200">

                                    Authoritative Engine

                                </span>

                            </div>

                            <p className="text-[11px] text-slate-500 mt-0.5">

                                Linear 50+ Archetype Iteration & Visual Diagram Vetting Studios

                            </p>

                        </div>

                    </div>



                    {/* Primary Studio Switcher Tabs */}

                    <div className="flex items-center gap-2">

                        <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200">

                            <button

                                type="button"

                                data-testid="tab-archetype-iteration"

                                onClick={() => {

                                    setWorkbenchTab('iteration');

                                    setIsIterationMode(true);

                                }}

                                className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${

                                    workbenchTab === 'iteration'

                                        ? 'bg-purple-600 text-white shadow-xs'

                                        : 'text-slate-600 hover:text-slate-900 hover:bg-white/60'

                                }`}

                            >

                                <Sparkles className="w-4 h-4 text-amber-300" />

                                <span>Archetype Iteration Studio</span>

                            </button>

                            <button

                                type="button"

                                data-testid="tab-diagram-vetting"

                                onClick={() => {

                                    setWorkbenchTab('diagrams');

                                    setIsIterationMode(false);

                                }}

                                className={`px-4 py-2 rounded-lg text-xs font-bold transition flex items-center gap-2 cursor-pointer ${

                                    workbenchTab === 'diagrams'

                                        ? 'bg-blue-600 text-white shadow-xs'

                                        : 'text-slate-600 hover:text-slate-900 hover:bg-white/60'

                                }`}

                            >

                                <Eye className="w-4 h-4 text-blue-600" />

                                <span>Diagram Visual Desk</span>

                            </button>

                        </div>



                        {/* Iteration Mode Toggle */}

                        {workbenchTab === 'iteration' && (

                            <button

                                type="button"

                                data-testid="btn-archetype-iteration"

                                onClick={toggleIterationMode}

                                className={`px-3.5 py-1.5 rounded-xl text-xs font-black transition flex items-center gap-1.5 shadow-xs border cursor-pointer ${

                                    isIterationMode 

                                        ? 'bg-purple-600 text-white border-purple-700 ring-2 ring-purple-300' 

                                        : 'bg-white text-purple-700 border-purple-300 hover:bg-purple-50'

                                }`}

                                title="Toggle Linear Archetype Iteration Mode (Bypass Adaptive Progression)"

                            >

                                <RefreshCw className={`w-3.5 h-3.5 ${isIterationMode ? 'animate-spin' : ''}`} />

                                <span>{isIterationMode ? 'ITERATION: ON' : 'ITERATION: OFF'}</span>

                            </button>

                        )}

                    </div>

                </div>

            </header>



            {/* TAB 1: DEDICATED ARCHETYPE ITERATION STUDIO (UNCRAMPED & FOCUSED) */}

            {workbenchTab === 'iteration' && (

                <div className="max-w-7xl mx-auto px-6 py-6 space-y-6">

                    {/* Top Subject, Grade & Topic Selector Bar */}

                    <div className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4">

                        <div className="flex flex-wrap items-center justify-between gap-3 pb-3 border-b border-slate-100">

                            <div className="flex items-center gap-2">

                                <Sparkles className="w-5 h-5 text-purple-600" />

                                <span className="font-bold text-sm text-slate-900">Curriculum Topic & Archetype Selection</span>

                                <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-purple-100 text-purple-800">

                                    {distinctTopicsForSubjectAndGrade.length} Topics in Syllabus

                                </span>

                            </div>

                            <div className="flex items-center gap-3">

                                <span className="text-xs text-slate-500 font-medium">PRNG Deterministic Seed:</span>

                                <input

                                    type="number"

                                    data-testid="input-workbench-seed"

                                    value={seed}

                                    onChange={(e) => setSeed(Number(e.target.value))}

                                    className="w-24 px-2.5 py-1.5 text-xs font-mono font-bold rounded-lg border border-slate-200 focus:outline-none focus:ring-2 focus:ring-purple-500 bg-slate-50"

                                />

                                <button

                                    type="button"

                                    onClick={() => {

                                        const nextSeed = Math.floor(Math.random() * 90000) + 1000;

                                        setSeed(nextSeed);

                                        const currentSub = iterationSubskills[iterationIndex] || null;

                                        handleGenerate(nextSeed, null, selectedTopic, currentSub, iterationGrade, iterationSubject);

                                    }}

                                    className="px-3 py-1.5 bg-slate-100 hover:bg-slate-200 text-slate-700 rounded-lg text-xs font-semibold transition cursor-pointer"

                                >

                                    🎲 Random Seed

                                </button>

                                <button

                                    type="button"

                                    data-testid="btn-iteration-generate"

                                    onClick={() => {

                                        const currentSub = iterationSubskills[iterationIndex] || null;

                                        handleGenerate(seed, null, selectedTopic, currentSub, iterationGrade, iterationSubject);

                                    }}

                                    disabled={generatingKey != null}

                                    className="px-4 py-1.5 bg-purple-600 hover:bg-purple-700 text-white rounded-lg text-xs font-bold transition flex items-center gap-1.5 cursor-pointer shadow-xs disabled:opacity-50"

                                >

                                    <RefreshCw className={`w-3.5 h-3.5 ${generatingKey != null ? 'animate-spin' : ''}`} />

                                    {generatingKey != null ? 'Generating...' : 'Regenerate'}

                                </button>

                            </div>

                        </div>



                        {/* 3 Clear Dropdowns: Subject, Grade, Topic */}

                        <div className="grid grid-cols-1 md:grid-cols-12 gap-4">

                            {/* 1. Subject Dropdown */}

                            <div className="md:col-span-4">

                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">

                                    1. Subject

                                </label>

                                <select

                                    data-testid="select-iteration-subject"

                                    value={iterationSubject}

                                    onChange={(e) => handleSubjectChange(e.target.value)}

                                    className="w-full text-xs font-semibold rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-slate-900 focus:outline-none focus:ring-2 focus:ring-purple-500 shadow-2xs"

                                >

                                    {distinctSubjects.map(s => (

                                        <option key={s} value={s}>{s}</option>

                                    ))}

                                </select>

                            </div>



                            {/* 2. Grade Dropdown */}

                            <div className="md:col-span-2">

                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">

                                    2. Grade

                                </label>

                                <select

                                    data-testid="select-iteration-grade"

                                    value={iterationGrade}

                                    onChange={(e) => handleGradeChange(e.target.value)}

                                    className="w-full text-xs font-semibold rounded-xl border border-slate-300 bg-white px-3.5 py-2.5 text-slate-900 focus:outline-none focus:ring-2 focus:ring-purple-500 shadow-2xs"

                                >

                                    {distinctGradesForSubject.map(g => (

                                        <option key={g} value={g}>Grade {g}</option>

                                    ))}

                                </select>

                            </div>



                            {/* 3. Topic Dropdown */}

                            <div className="md:col-span-6">

                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">

                                    3. Topic in Curriculum

                                </label>

                                <select

                                    data-testid="select-iteration-topic"

                                    value={iterationTopicName}

                                    onChange={(e) => handleTopicChange(e.target.value)}

                                    className="w-full text-xs font-semibold rounded-xl border border-purple-300 bg-purple-50/50 px-3.5 py-2.5 text-purple-950 focus:outline-none focus:ring-2 focus:ring-purple-500 shadow-2xs"

                                >

                                    {distinctTopicsForSubjectAndGrade.length === 0 ? (

                                        <option value="">No topics registered</option>

                                    ) : (

                                        distinctTopicsForSubjectAndGrade.map(t => (

                                            <option key={`${t.name}_${t.term}`} value={t.name}>

                                                Term {t.term || 1}: {t.name}

                                            </option>

                                        ))

                                    )}

                                </select>

                            </div>

                        </div>

                    </div>



                    {/* Stepper Ribbon & Navigation */}

                    <div className="bg-purple-950 text-white rounded-2xl p-5 shadow-lg border border-purple-800 space-y-4">

                        <div className="flex flex-wrap items-center justify-between gap-4">

                            <div>

                                <div className="flex items-center gap-2">

                                    <span className="font-black text-sm uppercase tracking-wider text-amber-300">

                                        ARCHETYPE ITERATION ACTIVE

                                    </span>

                                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase bg-emerald-400 text-black">

                                        Adaptive Gating Bypassed

                                    </span>

                                    <span className="px-2.5 py-0.5 rounded-full text-[11px] font-mono font-bold bg-purple-800 text-purple-200 border border-purple-700">

                                        Cycle {iterationCycle} (Infinite PRNG Entropy)

                                    </span>

                                </div>

                                <div className="text-sm text-purple-100 mt-1">

                                    Step <strong>{iterationIndex + 1}</strong> of <strong>{iterationSubskills.length || 1}</strong>: <code className="font-mono text-amber-300 font-bold bg-purple-900/80 px-2 py-0.5 rounded">{iterationSubskills[iterationIndex] || 'default'}</code>

                                </div>

                            </div>



                            {/* Stepper Navigation Buttons */}

                            <div className="flex items-center gap-2.5">

                                <button

                                    type="button"

                                    data-testid="btn-iteration-prev"

                                    onClick={handlePrevIteration}

                                    disabled={!iterationSubskills.length}

                                    className="px-4 py-2 bg-purple-800 hover:bg-purple-700 text-white rounded-xl text-xs font-bold transition flex items-center gap-1.5 border border-purple-600 disabled:opacity-50 cursor-pointer shadow-xs"

                                >

                                    <ChevronLeft className="w-4 h-4" /> Previous

                                </button>

                                <button

                                    type="button"

                                    data-testid="btn-iteration-next"

                                    onClick={handleNextIteration}

                                    disabled={!iterationSubskills.length}

                                    className="px-5 py-2 bg-amber-400 hover:bg-amber-300 text-purple-950 rounded-xl text-xs font-black shadow-md transition flex items-center gap-1.5 disabled:opacity-50 cursor-pointer"

                                >

                                    Next Archetype <ChevronRight className="w-4 h-4" />

                                </button>



                                {/* Direct Jump Dropdown */}

                                {iterationSubskills.length > 0 && (

                                    <select

                                        data-testid="select-iteration-archetype"

                                        value={iterationIndex}

                                        onChange={(e) => {

                                            const newIdx = Number(e.target.value);

                                            setIterationIndex(newIdx);

                                            const nextSeed = (Number(seed) || 1) + (iterationCycle - 1) * 1000 + newIdx * 7;

                                            setSeed(nextSeed);

                                            handleGenerate(nextSeed, null, selectedTopic, iterationSubskills[newIdx], iterationGrade, iterationSubject);

                                        }}

                                        className="text-xs font-mono rounded-xl border border-purple-600 bg-purple-900 text-white px-3 py-2 focus:outline-none focus:ring-2 focus:ring-amber-400"

                                    >

                                        {iterationSubskills.map((sub, idx) => (

                                            <option key={sub} value={idx}>

                                                {idx + 1}. {sub}

                                            </option>

                                        ))}

                                    </select>

                                )}

                            </div>

                        </div>



                        {/* Progress Bar */}

                        <div className="w-full bg-purple-900 h-2 rounded-full overflow-hidden border border-purple-800">

                            <div 

                                className="bg-gradient-to-r from-purple-400 to-amber-300 h-full rounded-full transition-all duration-300"

                                style={{ width: `${iterationSubskills.length ? ((iterationIndex + 1) / iterationSubskills.length) * 100 : 0}%` }}

                            />

                        </div>

                    </div>



                    {/* FULL-WIDTH UNCLUTTERED QUESTION CARD */}

                    {errorMsg && (

                        <div className="p-4 bg-red-50 border border-red-200 rounded-xl text-red-800 text-sm flex items-start gap-2">

                            <AlertTriangle className="w-5 h-5 shrink-0 text-red-600 mt-0.5" />

                            <div>

                                <div className="font-semibold">Generator Execution Notice:</div>

                                <div>{errorMsg}</div>

                            </div>

                        </div>

                    )}



                    {!activeQuestion ? (

                        <div className="bg-white rounded-2xl border border-slate-200 p-12 text-center shadow-sm">

                            <RefreshCw className="w-8 h-8 text-purple-600 animate-spin mx-auto mb-3" />

                            <h3 className="text-base font-bold text-slate-800 mb-1">Generating Question...</h3>

                            <p className="text-xs text-slate-500">

                                Executing deterministic generator for <code className="font-mono text-purple-700">{iterationTopicName}</code> ({iterationSubskills[iterationIndex] || 'default'})

                            </p>

                        </div>

                    ) : (

                        <div data-testid="workbench-question-card" className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">

                            {/* Card Status Header */}

                            <div data-testid="iteration-status-badge" className="bg-purple-50/80 border-b border-purple-100 p-4 flex flex-wrap items-center justify-between gap-3">

                                <div className="flex flex-wrap items-center gap-2">

                                    <span className="px-2.5 py-1 rounded-md bg-purple-200/70 text-purple-900 font-mono text-xs font-bold">

                                        Step {iterationIndex + 1} of {iterationSubskills.length || 1}

                                    </span>

                                    <span className="px-2.5 py-1 rounded-md bg-white border border-purple-200 text-purple-800 font-mono text-xs font-semibold">

                                        {activeQuestion.subskill || iterationSubskills[iterationIndex] || 'default'}

                                    </span>

                                    <span className="px-2.5 py-1 rounded-md bg-white border border-slate-200 text-slate-700 font-mono text-xs">

                                        Seed: {seed}

                                    </span>

                                    <span className="px-2 py-0.5 rounded text-[11px] bg-purple-100 text-purple-900 font-bold">

                                        Cycle {iterationCycle}

                                    </span>

                                </div>

                                <div className="flex items-center gap-2">

                                    <span className="px-3 py-1 rounded-full text-xs font-bold bg-blue-100 text-blue-900">

                                        {activeQuestion.marks || 2} Marks

                                    </span>

                                    <span className="px-2.5 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-600 uppercase tracking-wider text-[10px]">

                                        {activeQuestion.question_type || 'Multiple Choice'}

                                    </span>

                                    <button

                                        type="button"

                                        onClick={() => setShowRawJson(!showRawJson)}

                                        className="px-2.5 py-1 rounded-lg text-xs font-medium text-slate-500 hover:text-slate-800 hover:bg-slate-100 transition flex items-center gap-1 cursor-pointer"

                                        title="Toggle Raw JSON Payload"

                                    >

                                        <Code className="w-3.5 h-3.5" />

                                        <span>JSON</span>

                                    </button>

                                </div>

                            </div>



                            <div className="p-8 space-y-8">

                                {/* Question Prompt */}

                                <div>

                                    <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2">Question Prompt</span>

                                    <div

                                        data-testid="workbench-question-prompt"

                                        className="text-base leading-relaxed text-slate-900 font-sans whitespace-pre-line p-5 rounded-xl bg-slate-50/70 border border-slate-200"

                                    >

                                        <MathText text={activeQuestion.prompt || activeQuestion.question || 'No prompt available'} />

                                    </div>

                                </div>

                                {/* Attached Diagram Stimulus (Static Examination Vector / Orthogonal Figure) */}
                                {Boolean(activeQuestion.diagram_spec || activeQuestion.diagram || activeQuestion.svg_data) && (
                                    <div data-testid="workbench-iteration-diagram-container" className="p-4 rounded-xl bg-white border border-slate-200 shadow-2xs flex flex-col items-center justify-center">
                                        <DiagramRenderer
                                            spec={activeQuestion.diagram_spec || activeQuestion.diagram || { kind: 'inline_svg', svg: activeQuestion.svg_data }}
                                            interactive={false}
                                        />
                                    </div>
                                )}



                                {/* Options Matrix (if options present) */}

                                {Array.isArray(activeQuestion.options) && activeQuestion.options.length > 0 && (

                                    <div>

                                        <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2.5">

                                            Multiple Choice Options (4 Distractors Calibrated)

                                        </span>

                                        <div className="grid grid-cols-1 md:grid-cols-2 gap-3">

                                            {activeQuestion.options.map((opt, idx) => {

                                                const isCorrect = (activeQuestion.correct_answer && String(opt).trim() === String(activeQuestion.correct_answer).trim()) || (activeQuestion.correct_index === idx);

                                                return (

                                                    <div

                                                        key={idx}

                                                        className={`p-3.5 rounded-xl border text-sm font-medium flex items-center justify-between transition ${

                                                            isCorrect

                                                                ? 'bg-emerald-50 border-emerald-300 text-emerald-950 font-bold ring-1 ring-emerald-400 shadow-2xs'

                                                                : 'bg-white border-slate-200 text-slate-700'

                                                        }`}

                                                    >

                                                        <div className="flex items-center gap-2.5">

                                                            <span className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center shrink-0 ${

                                                                isCorrect ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-600'

                                                            }`}>

                                                                {String.fromCharCode(65 + idx)}

                                                            </span>

                                                            <MathText text={String(opt)} />

                                                        </div>

                                                        {isCorrect && (

                                                            <span className="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-200/80 text-emerald-900 flex items-center gap-1">

                                                                <Check className="w-3 h-3" /> Correct Answer

                                                            </span>

                                                        )}

                                                    </div>

                                                );

                                            })}

                                        </div>

                                    </div>

                                )}



                                {/* Expected Answer Badge */}

                                <div>

                                    <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2">Expected Correct Answer</span>

                                    <div className="inline-flex items-center gap-2 p-3 rounded-xl bg-emerald-100/70 border border-emerald-300 text-emerald-950 font-mono text-sm font-bold shadow-2xs">

                                        <CheckCircle2 className="w-4 h-4 text-emerald-700" />

                                        <MathText text={String(activeQuestion.correct_answer || activeQuestion.expected_answer || 'N/A')} />

                                    </div>

                                </div>



                                {/* Unified Official Examination Memo: Step-by-Step Worked Procedure & Mark Breakdown */}
                                <div>
                                    <div className="flex items-center justify-between mb-2">
                                        <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider flex items-center gap-1.5">
                                            <BookOpen className="w-3.5 h-3.5 text-amber-600" />
                                            Official Memorandum: Step-by-Step Worked Procedure & Mark Breakdown
                                        </span>
                                        <span className="px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-amber-100 text-amber-900 border border-amber-200">
                                            Total: {activeQuestion.marks || activeQuestion.total_marks || 2} Marks
                                        </span>
                                    </div>

                                    {/* Worked Solution with calculations & thought process */}
                                    <div className="p-5 rounded-xl bg-slate-50 border border-slate-200 text-sm leading-relaxed text-slate-900 whitespace-pre-line shadow-2xs font-sans">
                                        <MathText text={formatQuestionSolutionText(activeQuestion)} />
                                    </div>

                                    {/* Itemized Marking Rubric */}
                                    {(() => {
                                        const rawRubric = activeQuestion.grading_rubric || activeQuestion.marking_schema;
                                        let items = [];
                                        if (Array.isArray(rawRubric)) {
                                            items = rawRubric;
                                        } else if (rawRubric && Array.isArray(rawRubric.marking_points)) {
                                            items = rawRubric.marking_points.map(mp => `${mp.desc || mp.criterion} [${mp.marks || 1} Mark]`);
                                        } else if (typeof rawRubric === 'string') {
                                            items = [rawRubric];
                                        }

                                        if (!items.length) return null;

                                        return (
                                            <div className="mt-3 p-4 rounded-xl bg-amber-50/70 border border-amber-200 space-y-2">
                                                <span className="text-[10px] font-bold text-amber-900 uppercase tracking-wider block">
                                                    Mark Allocation Rubric (Assessment Guide)
                                                </span>
                                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                                    {items.map((crit, idx) => {
                                                        const critStr = typeof crit === 'object' ? (crit.desc || crit.criterion || JSON.stringify(crit)) : String(crit);
                                                        const isMethod = critStr.toLowerCase().includes('method') || critStr.includes('[M]');
                                                        const isAccuracy = critStr.toLowerCase().includes('accuracy') || critStr.includes('[A]');
                                                        return (
                                                            <div key={idx} className="flex items-center justify-between p-2 rounded-lg bg-white border border-amber-200 text-xs text-amber-950 shadow-2xs">
                                                                <div className="flex items-center gap-2">
                                                                    <span className="w-5 h-5 rounded bg-amber-200 text-amber-900 font-bold text-[10px] flex items-center justify-center shrink-0">
                                                                        {idx + 1}
                                                                    </span>
                                                                    <span className="font-medium">{critStr}</span>
                                                                </div>
                                                                {isMethod && (
                                                                    <span className="px-1.5 py-0.5 rounded text-[9px] font-bold bg-blue-100 text-blue-800 shrink-0">Method</span>
                                                                )}
                                                                {isAccuracy && (
                                                                    <span className="px-1.5 py-0.5 rounded text-[9px] font-bold bg-emerald-100 text-emerald-800 shrink-0">Accuracy</span>
                                                                )}
                                                            </div>
                                                        );
                                                    })}
                                                </div>
                                            </div>
                                        );
                                    })()}
                                </div>

                                {/* 3-Tier Pre-baked Hints */}

                                {activeQuestion.hints && (

                                    <div>

                                        <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2.5">

                                            3-Tier Diagnostic Hints (Pedagogical Scaffolding)

                                        </span>

                                        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">

                                            <div className="p-4 rounded-xl bg-blue-50/60 border border-blue-200 text-xs">

                                                <span className="font-bold text-blue-900 block mb-1">Tier 1: Conceptual</span>

                                                <p className="text-slate-700 leading-relaxed">{activeQuestion.hints.tier_1 || 'N/A'}</p>

                                            </div>

                                            <div className="p-4 rounded-xl bg-indigo-50/60 border border-indigo-200 text-xs">

                                                <span className="font-bold text-indigo-900 block mb-1">Tier 2: Operational</span>

                                                <p className="text-slate-700 leading-relaxed">{activeQuestion.hints.tier_2 || 'N/A'}</p>

                                            </div>

                                            <div className="p-4 rounded-xl bg-purple-50/60 border border-purple-200 text-xs">

                                                <span className="font-bold text-purple-900 block mb-1">Tier 3: Step-by-Step</span>

                                                <p className="text-slate-700 leading-relaxed">{activeQuestion.hints.tier_3 || 'N/A'}</p>

                                            </div>

                                        </div>

                                    </div>

                                )}



                                {/* Collapsible JSON Inspector */}

                                {showRawJson && (

                                    <div>

                                        <span className="text-[11px] font-bold text-slate-400 uppercase tracking-wider block mb-2">Raw Question Contract Payload</span>

                                        <pre className="p-4 rounded-xl bg-slate-900 text-emerald-400 font-mono text-xs overflow-x-auto max-h-96">

                                            {JSON.stringify(activeQuestion, null, 2)}

                                        </pre>

                                    </div>

                                )}

                            </div>

                        </div>

                    )}

                </div>

            )}



            {/* TAB 2: SPECIALIZED DIAGRAM VISUAL DESK (HEART STANDARD & SVG PLATES) */}

            {workbenchTab === 'diagrams' && (

                <main className="max-w-7xl mx-auto px-6 py-6 grid grid-cols-1 lg:grid-cols-12 gap-6">

                    {/* LEFT COLUMN: Diagram Catalogue & Review Desk (4 cols) */}

                    <div className="lg:col-span-4 space-y-5">

                        <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-sm">

                            <div className="flex items-center justify-between mb-3 border-b border-slate-100 pb-2">

                                <span className="font-bold text-xs text-slate-800">Visual Diagram Catalogue</span>

                                <span className="text-[11px] font-mono text-slate-500">{filteredArchetypes.length} plates</span>

                            </div>



                            {/* Grade filter buttons (AUD-04 verified) */}

                            <div className="mb-2.5">

                                <label className="block text-xs font-medium text-slate-600 mb-1">Grade Filter</label>

                                <div className="grid grid-cols-7 gap-1">

                                    {['all', '7', '8', '9', '10', '11', '12'].map(g => (

                                        <button

                                            key={g}

                                            type="button"

                                            data-testid={`btn-workbench-grade-${g}`}

                                            onClick={() => setSelectedGrade(g === 'all' ? 'ALL' : g)}

                                            className={`py-1 text-xs rounded font-medium transition cursor-pointer ${

                                                selectedGrade === (g === 'all' ? 'ALL' : g) 

                                                    ? 'bg-blue-600 text-white shadow-2xs font-bold' 

                                                    : 'bg-slate-100 text-slate-700 hover:bg-slate-200'

                                            }`}

                                        >

                                            {g === 'all' ? 'All' : `G${g}`}

                                        </button>

                                    ))}

                                </div>

                            </div>



                            <div className="mb-2.5">

                                <label className="block text-xs font-medium text-slate-600 mb-1">Diagram Master Plate</label>

                                <select

                                    value={selectedDiagramMaster}

                                    onChange={(e) => setSelectedDiagramMaster(e.target.value)}

                                    className="w-full text-xs rounded-lg border border-slate-200 bg-white px-3 py-2 text-slate-800 focus:outline-none focus:ring-2 focus:ring-blue-500"

                                >

                                    <option value="ALL">All 47 Diagram Masters</option>

                                    {diagramMasters.map(m => (

                                        <option key={m.diagram_id} value={m.diagram_id}>

                                            {m.title} ({m.archetypes?.length || 1} arch)

                                        </option>

                                    ))}

                                </select>

                            </div>



                            <div className="max-h-80 overflow-y-auto space-y-1.5 pr-1 border-t border-slate-100 pt-2">

                                {loadingCatalog ? (

                                    <div className="py-8 text-center text-xs text-slate-500">Loading catalog...</div>

                                ) : filteredArchetypes.length === 0 ? (

                                    <div className="py-6 text-center text-xs text-slate-500">No matching archetypes found</div>

                                ) : (

                                    filteredArchetypes.map(item => {

                                        const isSelected = selectedArchetype?.archetype_id === item.archetype_id;

                                        return (

                                            <button

                                                key={item.archetype_id}

                                                data-testid={`archetype-item-${item.archetype_id}`}

                                                type="button"

                                                onClick={() => {

                                                    setSelectedArchetype(item);

                                                    setSelectedTopic(item.topic);

                                                    handleGenerate(seed, item);

                                                }}

                                                className={`w-full text-left p-2.5 rounded-lg text-xs transition border cursor-pointer ${isSelected ? 'bg-blue-50/80 border-blue-300 ring-1 ring-blue-400 shadow-xs' : 'border-slate-100 hover:bg-slate-50 text-slate-700'}`}

                                            >

                                                <div className="flex items-center justify-between gap-1 mb-1">

                                                    <span className="font-mono font-bold text-blue-900 truncate">{item.archetype_id}</span>

                                                    <span className="px-1.5 py-0.2 rounded text-[10px] font-semibold bg-slate-100 text-slate-500">{item.verdict || 'PENDING'}</span>

                                                </div>

                                                <div className="font-medium text-slate-800 line-clamp-1 mb-1">{item.title}</div>

                                                <div className="flex flex-wrap items-center gap-1.5 text-[10px] text-slate-500">

                                                    <span className="px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 font-medium">{item.subject} Gr {item.grade}</span>

                                                    <span className="px-1.5 py-0.5 rounded bg-blue-50 text-blue-700 font-mono">{item.view} view</span>

                                                </div>

                                            </button>

                                        );

                                    })

                                )}

                            </div>

                        </div>



                        {/* Seed Controls in Diagram Desk */}

                        <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-sm space-y-3">

                            <label className="block text-xs font-medium text-slate-600">PRNG Seed</label>

                            <input

                                type="number"

                                value={seed}

                                onChange={(e) => setSeed(Number(e.target.value))}

                                className="w-full px-3 py-2 text-xs font-mono rounded-lg border border-slate-200"

                            />

                            <button

                                type="button"

                                data-testid="btn-vet-generate"
                                onClick={() => handleGenerate(seed, selectedArchetype, selectedTopic)}

                                className="w-full py-2 bg-blue-600 text-white rounded-lg text-xs font-semibold hover:bg-blue-700 transition"

                            >

                                {selectedArchetype ? `Generate ${selectedArchetype.archetype_id}` : 'Generate Live Question'}

                            </button>

                        </div>



                        {/* Super Admin Vetting Verdict Desk */}

                        <div className="bg-white rounded-xl border border-slate-200 p-4 shadow-sm space-y-3.5">

                            <h2 className="text-sm font-semibold uppercase tracking-wider text-slate-600 flex items-center gap-1.5">

                                <FileCheck className="w-4 h-4 text-emerald-600" /> Super Admin Vetting Verdict

                            </h2>

                            <div className="grid grid-cols-3 gap-1.5">

                                {[

                                    { id: 'CERTIFIED', label: 'Certified', bg: 'bg-emerald-600', active: verdict === 'CERTIFIED' },

                                    { id: 'NEEDS_ADJUSTMENT', label: 'Needs Fix', bg: 'bg-amber-600', active: verdict === 'NEEDS_ADJUSTMENT' },

                                    { id: 'REJECTED', label: 'Rejected', bg: 'bg-red-600', active: verdict === 'REJECTED' }

                                ].map(btn => (

                                    <button

                                        key={btn.id}

                                        type="button"

                                        onClick={() => setVerdict(btn.id)}

                                        className={`py-1.5 text-xs rounded-lg font-medium transition text-center ${btn.active ? `${btn.bg} text-white shadow-sm` : 'bg-slate-100 text-slate-700 hover:bg-slate-200'}`}

                                    >

                                        {btn.label}

                                    </button>

                                ))}

                            </div>

                            <button

                                type="button"

                                data-testid="btn-save-vetting"

                                onClick={handleSaveReview}

                                disabled={savingReview || (!selectedArchetype && !selectedTopic)}

                                className="w-full py-2 px-4 bg-emerald-600 hover:bg-emerald-700 text-white rounded-lg text-xs font-semibold shadow-sm transition flex items-center justify-center gap-1.5 disabled:opacity-50"

                            >

                                <Check className="w-4 h-4" />

                                {savingReview ? 'Persisting to Firestore...' : 'Save Vetting Verdict'}

                            </button>

                        </div>

                    </div>



                    {/* RIGHT COLUMN: Question & Diagram Canvas (8 cols) */}

                    <div className="lg:col-span-8 space-y-6">

                        {activeQuestion && (

                            <div className="bg-white rounded-xl border border-slate-200 p-5 shadow-sm space-y-4">

                                <div className="flex items-center justify-between pb-3 border-b border-slate-100">

                                    <span className="font-mono text-xs font-bold text-blue-900">{selectedArchetype?.archetype_id || selectedTopic}</span>

                                    <div className="flex items-center gap-2">

                                        <button

                                            type="button"

                                            data-testid="btn-toggle-workbench-view-mode"

                                            onClick={() => setWorkbenchAllowViewSwitch(!workbenchAllowViewSwitch)}

                                            className="px-2.5 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-700 text-xs font-medium transition cursor-pointer"

                                        >

                                            {workbenchAllowViewSwitch ? 'Lock View' : 'Multi-View Switcher'}

                                        </button>

                                        <span className="px-2.5 py-1 rounded bg-blue-50 text-blue-700 text-xs font-semibold">Seed: {seed}</span>

                                    </div>

                                </div>

                                <div className="text-sm leading-relaxed text-slate-800">

                                    <MathText text={activeQuestion.prompt || activeQuestion.question || ''} />

                                </div>

                                {(activeQuestion.diagram_spec || activeQuestion.diagram) && (

                                    <div data-testid="workbench-diagram-container" className="mt-4 pt-4 border-t border-slate-100">

                                        <DiagramRenderer

                                            spec={activeQuestion.diagram_spec || activeQuestion.diagram}

                                            selectedPin={null}

                                            onPinClick={() => {}}

                                            allowViewSwitch={workbenchAllowViewSwitch}

                                        />

                                    </div>

                                )}

                            </div>

                        )}

                    </div>

                </main>

            )}

        </div>

    );

}

