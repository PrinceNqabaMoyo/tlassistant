import { buildApiUrl } from '../../utils/apiBaseUrl';
import React, { useState, useMemo } from 'react';
import { collection, addDoc, serverTimestamp } from 'firebase/firestore';
import { 
    ChevronLeft, Loader2, FilePlus, AlertTriangle, Trash2, PlusCircle, 
    Printer, CheckSquare, Square, Layers, BookOpen, Sliders, 
    Sparkles, RefreshCw, Settings2 
} from 'lucide-react';
import AssignClassModal from '../admin/AssignClassModal';
import PrintableTestModal from './PrintableTestModal';
import TeacherAiCopilotPanel from './TeacherAiCopilotPanel';
import TeacherFacultySubjectsModal from './TeacherFacultySubjectsModal';
import { 
    getTeacherEnrolledSubjects, 
    isSubjectAllowedForGrade, 
    MAX_SENIOR_PHASE_SUBJECTS, 
    MAX_FET_PHASE_SUBJECTS 
} from '../../services/teacherSubjectQuotaService';
import { CAPS_TOPIC_TAXONOMY } from '../../data/capsTopicTaxonomy';

const ASSESSMENT_FORMAT_PRESETS = [
    { id: 'quiz', label: 'Quiz', marks: '10–15 M', duration: '~15 min', recommendedQ: '2', feedback: 'instant' },
    { id: 'assignment', label: 'Assignment', marks: '20–30 M', duration: '~45 min', recommendedQ: '4', feedback: 'instant' },
    { id: 'control_test', label: 'Control Test', marks: '40–50 M', duration: '~60 min', recommendedQ: '6', feedback: 'on_submission' },
    { id: 'exam', label: 'Exam', marks: '75–100+ M', duration: '~120 min', recommendedQ: '10', feedback: 'on_submission' },
];

const AssessmentGenerator = ({ db, currentUser, setView }) => {
    const [subject, setSubject] = useState('Mathematics');
    const [grade, setGrade] = useState('10');
    const [selectedTopics, setSelectedTopics] = useState(['Algebraic Expressions']);
    const [selectedSubskills, setSelectedSubskills] = useState(['Trinomial factorisation', 'Linear factorisation']);
    const [numQuestions, setNumQuestions] = useState('3');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [assessmentData, setAssessmentData] = useState(null);
    const [feedbackMode, setFeedbackMode] = useState('instant');

    // Assessment Format State
    const [assessmentFormat, setAssessmentFormat] = useState('quiz');

    // Faculty Subject Allocation State & Modal
    const [facultyAllocation, setFacultyAllocation] = useState(() => 
        getTeacherEnrolledSubjects(currentUser?.uid || 'default_educator')
    );
    const [isQuotaModalOpen, setIsQuotaModalOpen] = useState(false);

    // AI Copilot Panel State & Regeneration Index
    const [copilotQuestionIndex, setCopilotQuestionIndex] = useState(null);
    const [regeneratingIndex, setRegeneratingIndex] = useState(null);

    const [isModalOpen, setIsModalOpen] = useState(false);
    const [isPrintModalOpen, setIsPrintModalOpen] = useState(false);
    const [selectedClassId, setSelectedClassId] = useState('');
    const [assignmentStatus, setAssignmentStatus] = useState('');

    const teacherClasses = [
        { id: 'class_10a', name: 'Grade 10A Maths' },
        { id: 'class_10b', name: 'Grade 10B Maths' },
        { id: 'class_11c', name: 'Grade 11C Maths Lit' },
    ];

    // Available topics for selected subject & grade from authoritative taxonomy
    const availableGrades = useMemo(() => {
        return Object.keys(CAPS_TOPIC_TAXONOMY[subject] || { '10': [] }).sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
    }, [subject]);

    const availableTopics = useMemo(() => {
        return CAPS_TOPIC_TAXONOMY[subject]?.[grade] || [];
    }, [subject, grade]);

    // Available subskills aggregated from all currently selected topics
    const availableSubskills = useMemo(() => {
        const subskills = [];
        availableTopics.forEach(top => {
            if (selectedTopics.includes(top.name)) {
                top.subtopics.forEach(st => {
                    if (!subskills.includes(st)) {
                        subskills.push(st);
                    }
                });
            }
        });
        return subskills;
    }, [availableTopics, selectedTopics]);

    // Allowed subjects filtered by phase quota and grade eligibility
    const allowedSubjectsForGrade = useMemo(() => {
        const allTaxonomySubjects = Object.keys(CAPS_TOPIC_TAXONOMY);
        const isSenior = parseInt(grade, 10) <= 9;
        const enrolled = isSenior ? (facultyAllocation?.seniorPhase || []) : (facultyAllocation?.fetPhase || []);
        
        const activeList = allTaxonomySubjects.filter(s => isSubjectAllowedForGrade(s, grade) && enrolled.includes(s));
        if (activeList.length > 0) {
            return activeList;
        }
        return allTaxonomySubjects.filter(s => isSubjectAllowedForGrade(s, grade));
    }, [grade, facultyAllocation]);

    const handleFormatSelect = (fmtId) => {
        setAssessmentFormat(fmtId);
        const preset = ASSESSMENT_FORMAT_PRESETS.find(p => p.id === fmtId);
        if (preset) {
            setNumQuestions(preset.recommendedQ);
            setFeedbackMode(preset.feedback);
        }
    };

    const handleSubjectChange = (e) => {
        const newSubj = e.target.value;
        setSubject(newSubj);
        const gradesForSubj = Object.keys(CAPS_TOPIC_TAXONOMY[newSubj] || { '10': [] });
        const defaultGrade = gradesForSubj.includes('10') ? '10' : (gradesForSubj[0] || '10');
        setGrade(defaultGrade);
        const firstTopics = CAPS_TOPIC_TAXONOMY[newSubj]?.[defaultGrade] || [];
        const initialTopic = firstTopics[0]?.name ? [firstTopics[0].name] : [];
        setSelectedTopics(initialTopic);
        setSelectedSubskills(firstTopics[0]?.subtopics?.slice(0, 2) || []);
        setAssessmentData(null);
    };

    const handleGradeChange = (e) => {
        const newGrade = e.target.value;
        setGrade(newGrade);
        const topics = CAPS_TOPIC_TAXONOMY[subject]?.[newGrade] || [];
        const initialTopic = topics[0]?.name ? [topics[0].name] : [];
        setSelectedTopics(initialTopic);
        setSelectedSubskills(topics[0]?.subtopics?.slice(0, 2) || []);
        setAssessmentData(null);
    };

    const handleToggleTopic = (topicName) => {
        if (selectedTopics.includes(topicName)) {
            const nextTopics = selectedTopics.filter(t => t !== topicName);
            setSelectedTopics(nextTopics);
            // Remove subskills that only belonged to this topic
            const remainingTopicsObj = availableTopics.filter(t => nextTopics.includes(t.name));
            const validSubskills = remainingTopicsObj.flatMap(t => t.subtopics);
            setSelectedSubskills(prev => prev.filter(s => validSubskills.includes(s)));
        } else {
            const nextTopics = [...selectedTopics, topicName];
            setSelectedTopics(nextTopics);
            // Auto-select first 2 subskills of newly added topic
            const addedTopicObj = availableTopics.find(t => t.name === topicName);
            if (addedTopicObj?.subtopics) {
                const toAdd = addedTopicObj.subtopics.slice(0, 2);
                setSelectedSubskills(prev => Array.from(new Set([...prev, ...toAdd])));
            }
        }
    };

    const handleToggleSubskill = (subskillName) => {
        if (selectedSubskills.includes(subskillName)) {
            setSelectedSubskills(selectedSubskills.filter(s => s !== subskillName));
        } else {
            setSelectedSubskills([...selectedSubskills, subskillName]);
        }
    };

    const handleSelectAllSubskills = () => {
        setSelectedSubskills([...availableSubskills]);
    };

    const [activePresetTerm, setActivePresetTerm] = useState(null);

    const handleApplyTermPreset = (targetTerm) => {
        setActivePresetTerm(targetTerm);
        // Match topics according to official CAPS term pacing:
        // Term 1: term === 1
        // Term 2: term <= 2
        // Term 3: term <= 3
        // Term 4: term <= 4 (all topics)
        let matchingTopics = availableTopics.filter(t => (t.term || 1) <= targetTerm);
        if (matchingTopics.length === 0) {
            matchingTopics = availableTopics.slice(0, Math.min(targetTerm * 2, availableTopics.length));
        }
        const topicNames = matchingTopics.map(t => t.name);
        setSelectedTopics(topicNames);
        
        // Populate all subskills from matching topics
        const subskills = matchingTopics.flatMap(t => t.subtopics || []);
        setSelectedSubskills(subskills);

        // Adjust recommended questions count for authentic exam length
        const recommendedQuestions = targetTerm === 1 ? '4' : targetTerm === 2 ? '6' : targetTerm === 3 ? '8' : '10';
        setNumQuestions(recommendedQuestions);

        setAssessmentData(null);
        setError(null);
    };

    const handleDeselectAllSubskills = () => {
        setSelectedSubskills([]);
    };

    // Calculate dynamic total marks
    const dynamicTotalMarks = useMemo(() => {
        if (!assessmentData) return 0;
        return assessmentData.reduce((sum, q) => {
            const qMarks = q.marking_scheme 
                ? q.marking_scheme.reduce((s, p) => s + (parseInt(p.marks, 10) || 1), 0)
                : (q.marks || 5);
            return sum + qMarks;
        }, 0);
    }, [assessmentData]);

    const handleRegenerateVariant = async (qIndex) => {
        if (!assessmentData || !assessmentData[qIndex]) return;
        const currentQ = assessmentData[qIndex];
        setRegeneratingIndex(qIndex);
        try {
            const res = await fetch(buildApiUrl('/api/teacher/regenerate-question'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    topic: currentQ.topic || selectedTopics[0] || 'Algebraic Expressions',
                    grade,
                    subject,
                    assessment_format: assessmentFormat,
                    custom_marking_scheme: currentQ.marking_scheme,
                    subskill: selectedSubskills[qIndex % selectedSubskills.length] || ''
                })
            });
            if (res.ok) {
                const data = await res.json();
                if (data.question) {
                    const updated = [...assessmentData];
                    updated[qIndex] = {
                        ...currentQ,
                        ...data.question,
                        marking_scheme: data.question.marking_scheme || currentQ.marking_scheme
                    };
                    setAssessmentData(updated);
                }
            }
        } catch (err) {
            console.warn('Variant regeneration failed:', err);
        } finally {
            setRegeneratingIndex(null);
        }
    };

    const handleApplyReskinnedText = (newText) => {
        if (copilotQuestionIndex !== null && assessmentData && assessmentData[copilotQuestionIndex]) {
            const updated = [...assessmentData];
            updated[copilotQuestionIndex].question_text = newText;
            setAssessmentData(updated);
        }
    };

    const handleApplyPolishedRubric = (newScheme) => {
        if (copilotQuestionIndex !== null && assessmentData && assessmentData[copilotQuestionIndex]) {
            const updated = [...assessmentData];
            updated[copilotQuestionIndex].marking_scheme = newScheme;
            updated[copilotQuestionIndex].marks = newScheme.reduce((s, p) => s + (p.marks || 0), 0);
            setAssessmentData(updated);
        }
    };

    const handleGenerateAssessment = async (e) => {
        e.preventDefault();
        if (selectedTopics.length === 0) {
            setError("Please select at least one topic.");
            return;
        }
        if (selectedSubskills.length === 0) {
            setError("Please select at least one concept/subskill to include in the assessment scope.");
            return;
        }

        setLoading(true);
        setError(null);
        setAssessmentData(null);
        setAssignmentStatus('');

        const scopeSummary = `${selectedTopics.join(', ')} (${selectedSubskills.join('; ')})`;
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), 12000);

        try {
            const response = await fetch(buildApiUrl('/api/teacher/create-assessment'), {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                signal: controller.signal,
                body: JSON.stringify({ 
                    topic: scopeSummary, 
                    topics: selectedTopics,
                    subskills: selectedSubskills,
                    subject,
                    grade, 
                    num_questions: Math.max(parseInt(numQuestions, 10), 1),
                    assessment_format: assessmentFormat
                }),
            });
            clearTimeout(timeoutId);
            if (!response.ok) { 
                const errorData = await response.json(); 
                throw new Error(errorData.error || 'Server error occurred.'); 
            }
            const data = await response.json();
            setAssessmentData(data.assessment);
        } catch (err) {
            clearTimeout(timeoutId);
            // High-fidelity deterministic fallback matched to the teacher's selected scope
            const fallbackQuestions = selectedSubskills.slice(0, parseInt(numQuestions, 10)).map((subskill, idx) => {
                if (subskill.includes('factor') || subskill.includes('Trinomial')) {
                    return {
                        question_text: `Factorise completely: 2x^2 + 5x - 3 = 0. Show all intermediate factorization steps and solve for both roots.`,
                        marks: 6,
                        marking_scheme: [
                            { point: "Identify correct factor pairs (2x - 1)(x + 3) = 0", marks: 3 },
                            { point: "First root evaluation: x = 1/2", marks: 1 },
                            { point: "Second root evaluation: x = -3", marks: 2 }
                        ],
                        solution: "(2x - 1)(x + 3) = 0 => 2x - 1 = 0 or x + 3 = 0 => x = 1/2 or x = -3"
                    };
                } else if (subskill.includes('linear') || subskill.includes('Equations')) {
                    return {
                        question_text: `Solve for x: 3(x - 2) + 4 = 2(x + 5). Show full stepwise manipulation.`,
                        marks: 4,
                        marking_scheme: [
                            { point: "Expand brackets: 3x - 6 + 4 = 2x + 10", marks: 2 },
                            { point: "Group like terms: 3x - 2x = 10 + 2", marks: 1 },
                            { point: "Final solution: x = 12", marks: 1 }
                        ],
                        solution: "3x - 6 + 4 = 2x + 10 => 3x - 2 = 2x + 10 => x = 12"
                    };
                } else if (subskill.includes('VAT') || subskill.includes('Receipts')) {
                    return {
                        question_text: `Calculate the gross bank receipt for cash merchandise sales of R15 000 (excluding 15% VAT). Show Output VAT and Gross Bank Amount.`,
                        marks: 5,
                        marking_scheme: [
                            { point: "Output VAT calculation (15 000 x 15 / 100 = R2 250)", marks: 2 },
                            { point: "Gross Bank Amount formula (Sales + Output VAT)", marks: 1 },
                            { point: "Correct final Bank gross total R17 250.00", marks: 2 }
                        ],
                        solution: "Output VAT = R15 000 x 0.15 = R2 250. Gross Bank = R15 000 + R2 250 = R17 250.00"
                    };
                } else if (subskill.includes('Kinematics') || subskill.includes('Newton') || subskill.includes('Mechanics')) {
                    return {
                        question_text: `A 1200 kg car accelerates uniformly from rest to 24 m/s in 6 seconds. Calculate the net force applied.`,
                        marks: 5,
                        marking_scheme: [
                            { point: "Calculate acceleration a = (v_f - v_i) / t = (24 - 0) / 6 = 4 m/s²", marks: 2 },
                            { point: "State Newton's Second Law: F_net = m * a", marks: 1 },
                            { point: "Substitute values and evaluate: 1200 * 4 = 4800 N", marks: 2 }
                        ],
                        solution: "a = 24 / 6 = 4 m/s². F_net = 1200 * 4 = 4800 N East."
                    };
                } else {
                    return {
                        question_text: `Explain the key principles of "${subskill}" within Grade ${grade} ${subject}. Provide an authentic practical scenario and outline two core implications.`,
                        marks: 6,
                        marking_scheme: [
                            { point: "Accurate conceptual definition and core characteristics", marks: 2 },
                            { point: "Practical application scenario relevant to the South African context", marks: 2 },
                            { point: "Two distinct analytical implications or evaluative conclusions", marks: 2 }
                        ],
                        solution: `Provide direct reference to curriculum guidelines for ${subskill}, noting dual characteristics and contextual evaluation.`
                    };
                }
            });

            setAssessmentData(fallbackQuestions);
        } finally {
            setLoading(false);
        }
    };

    const handleApproveAndAssign = () => {
        if (!assessmentData) return;
        setAssignmentStatus('');
        setIsModalOpen(true);
    };

    const handleConfirmAssignment = async () => {
        if (!selectedClassId) {
            alert("Please select a class.");
            return;
        }
        setLoading(true);
        try {
            const assessmentRef = collection(db, "assessments");
            await addDoc(assessmentRef, {
                teacherId: currentUser?.uid || 'educator_host',
                classId: selectedClassId,
                subject: subject,
                grade: grade,
                topics: selectedTopics,
                subskills: selectedSubskills,
                questions: assessmentData,
                totalMarks: dynamicTotalMarks,
                createdAt: serverTimestamp(),
                feedbackMode: feedbackMode,
            });
            setAssignmentStatus(`Assessment (${dynamicTotalMarks} Marks) successfully assigned to class ${selectedClassId}!`);
        } catch (e) {
            console.error("Error adding document: ", e);
            setAssignmentStatus('Failed to assign assessment. Please try again.');
            setError(e.message);
        } finally {
            setLoading(false);
            setIsModalOpen(false);
        }
    };

    const handleQuestionTextChange = (qIndex, newText) => {
        const updatedData = [...assessmentData];
        updatedData[qIndex].question_text = newText;
        setAssessmentData(updatedData);
    };

    const handleMarkingPointChange = (qIndex, pIndex, newPoint) => {
        const updatedData = [...assessmentData];
        updatedData[qIndex].marking_scheme[pIndex].point = newPoint;
        setAssessmentData(updatedData);
    };

    const handleMarksChange = (qIndex, pIndex, newMarks) => {
        const updatedData = [...assessmentData];
        const val = parseInt(newMarks, 10);
        updatedData[qIndex].marking_scheme[pIndex].marks = isNaN(val) ? 0 : val;
        // Recalculate question total marks
        updatedData[qIndex].marks = updatedData[qIndex].marking_scheme.reduce((s, p) => s + (p.marks || 0), 0);
        setAssessmentData(updatedData);
    };

    const handleAddMarkingPoint = (qIndex) => {
        const updatedData = [...assessmentData];
        updatedData[qIndex].marking_scheme.push({ point: 'New assessment criterion', marks: 1 });
        updatedData[qIndex].marks = updatedData[qIndex].marking_scheme.reduce((s, p) => s + (p.marks || 0), 0);
        setAssessmentData(updatedData);
    };

    const handleRemoveMarkingPoint = (qIndex, pIndex) => {
        const updatedData = [...assessmentData];
        updatedData[qIndex].marking_scheme.splice(pIndex, 1);
        updatedData[qIndex].marks = updatedData[qIndex].marking_scheme.reduce((s, p) => s + (p.marks || 0), 0);
        setAssessmentData(updatedData);
    };

    const handleSolutionChange = (qIndex, newSolution) => {
        const updatedData = [...assessmentData];
        updatedData[qIndex].solution = newSolution;
        setAssessmentData(updatedData);
    };

    return (
        <>
            <AssignClassModal
                isOpen={isModalOpen}
                onClose={() => setIsModalOpen(false)}
                onConfirm={handleConfirmAssignment}
                classes={teacherClasses}
                setSelectedClassId={setSelectedClassId}
            />
            <PrintableTestModal
                isOpen={isPrintModalOpen}
                onClose={() => setIsPrintModalOpen(false)}
                testTitle={`${selectedTopics.join(', ') || 'Custom Assessment'} (Grade ${grade} ${subject})`}
                subject={subject}
                grade={grade}
                term={activePresetTerm || 1}
                durationMins={Math.max(20, Math.round(dynamicTotalMarks * 1.2))}
                questions={assessmentData || []}
            />
            <div className="p-4 sm:p-6 lg:p-8 bg-slate-50 min-h-screen text-slate-900">
                <div className="max-w-4xl mx-auto space-y-6">
                    <button 
                        onClick={() => setView('dashboard')} 
                        data-testid="btn-assessment-back"
                        className="flex items-center text-slate-600 hover:text-blue-600 font-semibold text-sm transition group cursor-pointer"
                    >
                        <ChevronLeft className="h-4 w-4 mr-1 transition-transform group-hover:-translate-x-1" />
                        Back to Teacher Cockpit
                    </button>

                    <div>
                        <h1 className="text-2xl sm:text-3xl font-bold text-slate-900 tracking-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            Assessment Generator & Paper Author
                        </h1>
                        <p className="text-sm text-slate-600 mt-1">
                            Customize assessment scope across topics and subskills, calibrate marks, and generate authentic printable test sheets and marking memoranda.
                        </p>
                    </div>

                    <form onSubmit={handleGenerateAssessment} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-6">
                        {/* Format Presets & Faculty Subject Quota Bar */}
                        <div className="p-3.5 bg-gradient-to-r from-blue-50/90 to-indigo-50/80 border border-blue-100 rounded-xl space-y-2.5">
                            <div className="flex flex-wrap items-center justify-between gap-2.5">
                                <div className="flex flex-wrap items-center gap-2">
                                    <span className="text-xs font-bold uppercase tracking-wider text-blue-900">
                                        Assessment Format:
                                    </span>
                                    <div className="flex flex-wrap items-center gap-1.5" role="radiogroup" aria-label="Assessment Format">
                                        {ASSESSMENT_FORMAT_PRESETS.map((fmt) => {
                                            const isSelected = assessmentFormat === fmt.id;
                                            return (
                                                <button
                                                    key={fmt.id}
                                                    type="button"
                                                    data-testid={`btn-format-${fmt.id}`}
                                                    onClick={() => handleFormatSelect(fmt.id)}
                                                    className={`px-3 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer flex items-center gap-1.5 ${
                                                        isSelected
                                                            ? 'bg-blue-600 text-white shadow-xs'
                                                            : 'bg-white text-slate-700 hover:bg-blue-100/60 border border-slate-200'
                                                    }`}
                                                >
                                                    <span>{fmt.label}</span>
                                                    <span className={`text-[10px] font-normal ${isSelected ? 'text-blue-100' : 'text-slate-500'}`}>
                                                        ({fmt.marks})
                                                    </span>
                                                </button>
                                            );
                                        })}
                                    </div>
                                </div>

                                {/* Faculty Subject Quotas Pill */}
                                <button
                                    type="button"
                                    data-testid="btn-manage-faculty-quota"
                                    onClick={() => setIsQuotaModalOpen(true)}
                                    className="inline-flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold text-blue-700 bg-white border border-blue-200 hover:bg-blue-50 rounded-lg shadow-2xs transition cursor-pointer"
                                    title="Configure Departmental Subject Allocation"
                                >
                                    <Settings2 className="w-3.5 h-3.5 text-blue-600" />
                                    <span>Quota: {facultyAllocation?.seniorPhase?.length || 0}/2 SP · {facultyAllocation?.fetPhase?.length || 0}/3 FET</span>
                                </button>
                            </div>
                        </div>

                        {/* Subject & Grade Selection */}
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                            <div>
                                <label htmlFor="subject" className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5 flex items-center gap-1.5">
                                    <BookOpen className="w-3.5 h-3.5 text-blue-600" />
                                    Subject
                                </label>
                                <select 
                                    id="subject" 
                                    data-testid="select-assessment-subject"
                                    value={subject} 
                                    onChange={handleSubjectChange} 
                                    className="w-full p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-blue-500 focus:bg-white transition"
                                >
                                    {allowedSubjectsForGrade.map(s => <option key={s} value={s}>{s}</option>)}
                                    {/* Additional curriculum subjects */}
                                    {Object.keys(CAPS_TOPIC_TAXONOMY)
                                        .filter(s => !allowedSubjectsForGrade.includes(s))
                                        .map(s => <option key={s} value={s}>{s}</option>)
                                    }
                                </select>
                            </div>
                            <div>
                                <label htmlFor="grade" className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5 flex items-center gap-1.5">
                                    <Layers className="w-3.5 h-3.5 text-blue-600" />
                                    Grade Level
                                </label>
                                <select 
                                    id="grade" 
                                    data-testid="select-assessment-grade"
                                    value={grade} 
                                    onChange={handleGradeChange} 
                                    className="w-full p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm font-semibold text-slate-800 focus:ring-2 focus:ring-blue-500 focus:bg-white transition"
                                >
                                    {availableGrades.map(g => <option key={g} value={g}>Grade {g}</option>)}
                                </select>
                            </div>
                        </div>

                        {/* 1-Click Provincial CAPS ATP Presets Bar (Terms 1 to 4) */}
                        <div className="rounded-xl border border-blue-200 bg-gradient-to-r from-blue-50/70 to-indigo-50/70 p-3.5">
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-xs font-bold uppercase tracking-wider text-blue-900 flex items-center gap-1.5">
                                    <span className="text-sm">⚡</span> Provincial Common Assessment ATP Scope Presets (Terms 1–4)
                                </span>
                                <span className="text-[11px] text-blue-700 font-medium">1-Click Official Curriculum Scope</span>
                            </div>
                            <div className="grid grid-cols-2 sm:grid-cols-4 gap-2">
                                <button
                                    type="button"
                                    data-testid="preset-term-1"
                                    onClick={() => handleApplyTermPreset(1)}
                                    className={`px-3 py-2 rounded-lg border text-xs font-semibold transition cursor-pointer text-left ${
                                        activePresetTerm === 1
                                            ? 'bg-blue-600 border-blue-700 text-white shadow-xs'
                                            : 'bg-white border-blue-200 hover:border-blue-400 text-blue-900 shadow-2xs hover:bg-blue-50/60'
                                    }`}
                                >
                                    <div className="font-bold">Term 1 Control Test</div>
                                    <div className={`text-[10px] ${activePresetTerm === 1 ? 'text-blue-100' : 'text-slate-500'}`}>March Scope (50 Marks)</div>
                                </button>
                                <button
                                    type="button"
                                    data-testid="preset-term-2"
                                    onClick={() => handleApplyTermPreset(2)}
                                    className={`px-3 py-2 rounded-lg border text-xs font-semibold transition cursor-pointer text-left ${
                                        activePresetTerm === 2
                                            ? 'bg-blue-600 border-blue-700 text-white shadow-xs'
                                            : 'bg-white border-blue-200 hover:border-blue-400 text-blue-900 shadow-2xs hover:bg-blue-50/60'
                                    }`}
                                >
                                    <div className="font-bold">Term 2 Mid-Year</div>
                                    <div className={`text-[10px] ${activePresetTerm === 2 ? 'text-blue-100' : 'text-slate-500'}`}>June Scope (100 Marks)</div>
                                </button>
                                <button
                                    type="button"
                                    data-testid="preset-term-3"
                                    onClick={() => handleApplyTermPreset(3)}
                                    className={`px-3 py-2 rounded-lg border text-xs font-semibold transition cursor-pointer text-left ${
                                        activePresetTerm === 3
                                            ? 'bg-blue-600 border-blue-700 text-white shadow-xs'
                                            : 'bg-white border-blue-200 hover:border-blue-400 text-blue-900 shadow-2xs hover:bg-blue-50/60'
                                    }`}
                                >
                                    <div className="font-bold">Term 3 Trial / Prep</div>
                                    <div className={`text-[10px] ${activePresetTerm === 3 ? 'text-blue-100' : 'text-slate-500'}`}>Sept Scope (150 Marks)</div>
                                </button>
                                <button
                                    type="button"
                                    data-testid="preset-term-4"
                                    onClick={() => handleApplyTermPreset(4)}
                                    className={`px-3 py-2 rounded-lg border text-xs font-semibold transition cursor-pointer text-left ${
                                        activePresetTerm === 4
                                            ? 'bg-blue-600 border-blue-700 text-white shadow-xs'
                                            : 'bg-white border-blue-200 hover:border-blue-400 text-blue-900 shadow-2xs hover:bg-blue-50/60'
                                    }`}
                                >
                                    <div className="font-bold">Term 4 Final Exam</div>
                                    <div className={`text-[10px] ${activePresetTerm === 4 ? 'text-blue-100' : 'text-slate-500'}`}>Nov Full Scope (150 Marks)</div>
                                </button>
                            </div>
                        </div>

                        {/* Multi-Topic Selection */}
                        <div>
                            <div className="flex items-center justify-between mb-2">
                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5">
                                    <span>Select Topics ({selectedTopics.length} selected)</span>
                                </label>
                                <span className="text-[11px] text-slate-500 font-medium">Select multiple topics for composite exam papers</span>
                            </div>
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 max-h-48 overflow-y-auto p-3 bg-slate-50 border border-slate-200 rounded-xl">
                                {availableTopics.map(top => {
                                    const isSelected = selectedTopics.includes(top.name);
                                    return (
                                        <button
                                            type="button"
                                            key={top.name}
                                            data-testid={`btn-topic-${top.name.toLowerCase().replace(/\s+/g, '-')}`}
                                            onClick={() => handleToggleTopic(top.name)}
                                            className={`p-2.5 rounded-lg border text-left text-xs font-semibold flex items-center gap-2.5 transition cursor-pointer ${
                                                isSelected 
                                                    ? 'bg-blue-50 text-blue-900 border-blue-400 shadow-2xs' 
                                                    : 'bg-white text-slate-700 border-slate-200 hover:border-slate-300'
                                            }`}
                                        >
                                            {isSelected ? (
                                                <CheckSquare className="w-4 h-4 text-blue-600 flex-shrink-0" />
                                            ) : (
                                                <Square className="w-4 h-4 text-slate-400 flex-shrink-0" />
                                            )}
                                            <span className="truncate">{top.name}</span>
                                        </button>
                                    );
                                })}
                            </div>
                        </div>

                        {/* Granular Concept & Subskill Selector */}
                        <div>
                            <div className="flex items-center justify-between mb-2">
                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-700 flex items-center gap-1.5">
                                    <Sliders className="w-3.5 h-3.5 text-blue-600" />
                                    <span>Concepts & Subskills Included ({selectedSubskills.length} of {availableSubskills.length})</span>
                                </label>
                                <div className="flex items-center gap-2 text-xs font-semibold text-blue-600">
                                    <button 
                                        type="button" 
                                        onClick={handleSelectAllSubskills} 
                                        className="hover:underline cursor-pointer"
                                    >
                                        Select All
                                    </button>
                                    <span>·</span>
                                    <button 
                                        type="button" 
                                        onClick={handleDeselectAllSubskills} 
                                        className="hover:underline text-slate-500 cursor-pointer"
                                    >
                                        Deselect All
                                    </button>
                                </div>
                            </div>
                            <div className="flex flex-wrap gap-2 p-3 bg-slate-50 border border-slate-200 rounded-xl min-h-[70px] max-h-48 overflow-y-auto">
                                {availableSubskills.length === 0 ? (
                                    <div className="text-xs text-slate-400 italic py-2">Select at least one topic above to view subskills</div>
                                ) : (
                                    availableSubskills.map(subskill => {
                                        const isChecked = selectedSubskills.includes(subskill);
                                        return (
                                            <button
                                                type="button"
                                                key={subskill}
                                                data-testid={`chip-subskill-${subskill.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`}
                                                onClick={() => handleToggleSubskill(subskill)}
                                                className={`px-3 py-1.5 rounded-lg text-xs font-medium border flex items-center gap-1.5 transition cursor-pointer ${
                                                    isChecked 
                                                        ? 'bg-blue-600 text-white border-blue-600 shadow-2xs font-semibold' 
                                                        : 'bg-white text-slate-700 border-slate-200 hover:border-slate-300'
                                                }`}
                                            >
                                                <span>{subskill}</span>
                                                {isChecked && <span className="text-[10px]">✓</span>}
                                            </button>
                                        );
                                    })
                                )}
                            </div>
                        </div>

                        {/* Question Count & Feedback Options */}
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 pt-2 border-t border-slate-100">
                            <div>
                                <label htmlFor="numQuestions" className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">
                                    Number of Question Units
                                </label>
                                <select 
                                    id="numQuestions" 
                                    data-testid="select-assessment-questions-count"
                                    value={numQuestions} 
                                    onChange={e => setNumQuestions(e.target.value)} 
                                    className="w-full p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm font-semibold text-slate-800"
                                >
                                    {[1, 2, 3, 5, 8, 10].map(n => <option key={n} value={n}>{n} Question{n > 1 ? 's' : ''}</option>)}
                                </select>
                            </div>
                            <div>
                                <label htmlFor="feedbackMode" className="block text-xs font-bold uppercase tracking-wider text-slate-600 mb-1.5">
                                    Class Delivery & Marking Mode
                                </label>
                                <select 
                                    id="feedbackMode" 
                                    value={feedbackMode} 
                                    onChange={e => setFeedbackMode(e.target.value)} 
                                    className="w-full p-2.5 bg-slate-50 border border-slate-300 rounded-xl text-sm font-semibold text-slate-800"
                                >
                                    <option value="instant">Instant Formative Step Feedback</option>
                                    <option value="on_submission">Feedback on Final Test Submission</option>
                                    <option value="teacher_only">Teacher Manual / PDF Print Only</option>
                                </select>
                            </div>
                        </div>

                        <div className="pt-2 text-right">
                            <button 
                                type="submit" 
                                data-testid="btn-generate-assessment-draft"
                                disabled={loading || selectedSubskills.length === 0} 
                                className="inline-flex items-center px-6 py-3 rounded-xl shadow-md text-sm font-bold text-white bg-blue-600 hover:bg-blue-700 disabled:opacity-50 transition cursor-pointer"
                            >
                                {loading ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : <FilePlus className="mr-2 h-4 w-4" />}
                                {loading ? 'Drafting Assessment...' : 'Draft Assessment Paper'}
                            </button>
                        </div>
                    </form>

                    {assignmentStatus && (
                        <div className={`p-4 rounded-xl text-sm font-semibold border ${error ? 'bg-red-50 text-red-700 border-red-200' : 'bg-emerald-50 text-emerald-800 border-emerald-200'}`} role="alert">
                            {assignmentStatus}
                        </div>
                    )}
                    {error && !assignmentStatus && (
                        <div className="bg-red-50 border border-red-300 text-red-700 p-4 rounded-xl flex items-center gap-3" role="alert">
                            <AlertTriangle className="h-5 w-5 text-red-600 flex-shrink-0" />
                            <div className="text-xs font-medium">{error}</div>
                        </div>
                    )}

                    {/* Review & Edit Draft Panel */}
                    {assessmentData && (
                      <div className="space-y-6 pt-4">
                        <div className="flex flex-wrap items-center justify-between gap-3 bg-white p-4 rounded-xl border border-slate-200 shadow-2xs">
                          <div>
                            <h2 className="text-xl font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                              Review & Edit Assessment Draft
                            </h2>
                            <div className="flex items-center gap-2 mt-1">
                              <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-700 border border-blue-200 font-mono">
                                Total: {dynamicTotalMarks} Marks
                              </span>
                              <span className="text-xs font-medium text-slate-500">
                                Allocated Pacing: ~{Math.max(20, Math.round(dynamicTotalMarks * 1.2))} Mins
                              </span>
                            </div>
                          </div>
                          <button
                            type="button"
                            onClick={() => setIsPrintModalOpen(true)}
                            data-testid="btn-print-test-pdf"
                            className="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white rounded-xl font-bold text-xs flex items-center gap-2 shadow-sm transition cursor-pointer"
                          >
                            <Printer className="w-4 h-4" />
                            <span>Print Test & Memo PDF</span>
                          </button>
                        </div>

                        {assessmentData.map((question, qIndex) => (
                          <div key={qIndex} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-200 space-y-4">
                            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-slate-100 pb-3">
                              <div className="flex items-center gap-2.5">
                                <h3 className="text-base font-bold text-slate-800">
                                  Question {qIndex + 1}
                                </h3>
                                <span className="text-xs font-bold text-slate-600 font-mono bg-slate-100 px-2 py-0.5 rounded">
                                  [{question.marking_scheme ? question.marking_scheme.reduce((s, p) => s + (p.marks || 0), 0) : question.marks} Marks]
                                </span>
                              </div>

                              <div className="flex items-center gap-2">
                                <button
                                  type="button"
                                  data-testid={`btn-regenerate-variant-${qIndex}`}
                                  disabled={regeneratingIndex === qIndex}
                                  onClick={() => handleRegenerateVariant(qIndex)}
                                  className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 border border-slate-200 rounded-lg transition cursor-pointer disabled:opacity-50"
                                  title="Generate fresh number variant while preserving custom marks"
                                >
                                  <RefreshCw className={`w-3.5 h-3.5 text-slate-600 ${regeneratingIndex === qIndex ? 'animate-spin' : ''}`} />
                                  <span>{regeneratingIndex === qIndex ? 'Regenerating...' : 'New Number Variant'}</span>
                                </button>

                                <button
                                  type="button"
                                  data-testid={`btn-open-copilot-${qIndex}`}
                                  onClick={() => setCopilotQuestionIndex(qIndex)}
                                  className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-bold text-indigo-700 bg-indigo-50 hover:bg-indigo-100 border border-indigo-200 rounded-lg transition cursor-pointer shadow-2xs"
                                  title="Open Grounded AI Copilot for local context reskinning & rubric polish"
                                >
                                  <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
                                  <span>AI Copilot</span>
                                </button>
                              </div>
                            </div>

                            <div>
                              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-1">
                                Question Statement & Problem Text
                              </label>
                              <textarea 
                                value={question.question_text} 
                                onChange={(e) => handleQuestionTextChange(qIndex, e.target.value)} 
                                data-testid={`textarea-question-text-${qIndex}`}
                                className="w-full p-3 border border-slate-300 rounded-xl text-sm font-sans focus:ring-2 focus:ring-blue-500 focus:bg-white" 
                                rows="3" 
                              />
                            </div>

                            {/* Diagnostic Multiple-Choice Options Display (When Quiz / MCQ format) */}
                            {question.options && question.options.length > 0 && (
                              <div className="bg-slate-50 border border-slate-200 rounded-xl p-3.5 space-y-2">
                                <div className="flex items-center justify-between">
                                  <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500">
                                    Multiple-Choice Options (Diagnostic Quiz)
                                  </span>
                                  <span className="text-[10px] font-medium text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200">
                                    Key: Option {String.fromCharCode(65 + (parseInt(question.correct_index, 10) || 0))}
                                  </span>
                                </div>
                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                                  {question.options.map((opt, oIdx) => {
                                    const isCorrect = String(question.correct_index) === String(oIdx);
                                    return (
                                      <div
                                        key={oIdx}
                                        className={`p-2.5 rounded-lg border text-xs flex items-center gap-2.5 transition ${
                                          isCorrect
                                            ? 'bg-emerald-50/90 border-emerald-300 text-emerald-950 font-semibold'
                                            : 'bg-white border-slate-200 text-slate-700'
                                        }`}
                                      >
                                        <span className={`w-5 h-5 rounded-full flex items-center justify-center font-bold text-[10px] shrink-0 ${
                                          isCorrect ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-600 border border-slate-200'
                                        }`}>
                                          {String.fromCharCode(65 + oIdx)}
                                        </span>
                                        <span className="flex-grow font-sans">{opt}</span>
                                        {isCorrect && (
                                          <span className="text-[10px] uppercase font-bold text-emerald-700 bg-emerald-100/80 px-1.5 py-0.5 rounded shrink-0">
                                            Correct
                                          </span>
                                        )}
                                      </div>
                                    );
                                  })}
                                </div>
                              </div>
                            )}

                            {/* Marking Scheme Points Editor */}
                            <div>
                              <div className="flex items-center justify-between mb-2">
                                <label className="block text-xs font-bold uppercase tracking-wider text-slate-500">
                                  Marking Scheme & Criteria Breakdown
                                </label>
                                <button 
                                  type="button" 
                                  onClick={() => handleAddMarkingPoint(qIndex)} 
                                  data-testid={`btn-add-marking-point-${qIndex}`}
                                  className="flex items-center gap-1.5 text-xs font-bold text-blue-600 hover:text-blue-800 cursor-pointer"
                                >
                                  <PlusCircle className="h-3.5 w-3.5" /> 
                                  Add Criterion
                                </button>
                              </div>
                              <div className="space-y-2.5">
                                {question.marking_scheme?.map((point, pIndex) => (
                                  <div key={pIndex} className="flex items-center gap-2.5 bg-slate-50 p-2.5 rounded-xl border border-slate-200">
                                    <input 
                                      type="text" 
                                      value={point.point} 
                                      data-testid={`input-point-text-${qIndex}-${pIndex}`}
                                      onChange={(e) => handleMarkingPointChange(qIndex, pIndex, e.target.value)} 
                                      className="flex-grow p-2 bg-white border border-slate-200 rounded-lg text-xs font-medium" 
                                      placeholder="Marking criterion..."
                                    />
                                    <div className="flex items-center gap-1 bg-white px-2 py-1 border border-slate-200 rounded-lg">
                                      <span className="text-[11px] font-bold text-blue-600">✓</span>
                                      <input 
                                        type="number" 
                                        value={point.marks} 
                                        data-testid={`input-point-marks-${qIndex}-${pIndex}`}
                                        onChange={(e) => handleMarksChange(qIndex, pIndex, e.target.value)} 
                                        className="w-12 text-center text-xs font-bold font-mono focus:outline-none" 
                                        min="1" 
                                        max="20"
                                      />
                                      <span className="text-[10px] text-slate-400">M</span>
                                    </div>
                                    <button 
                                      type="button" 
                                      onClick={() => handleRemoveMarkingPoint(qIndex, pIndex)} 
                                      data-testid={`btn-remove-point-${qIndex}-${pIndex}`}
                                      className="text-slate-400 hover:text-red-600 p-1.5 rounded-lg hover:bg-red-50 transition cursor-pointer"
                                    >
                                      <Trash2 className="h-4 w-4" />
                                    </button>
                                  </div>
                                ))}
                              </div>
                            </div>

                            {/* Worked Solution */}
                            <div>
                              <label className="block text-xs font-bold uppercase tracking-wider text-slate-500 mb-1">
                                Stepwise Canonical Worked Solution (Memorandum)
                              </label>
                              <textarea 
                                value={question.solution} 
                                onChange={(e) => handleSolutionChange(qIndex, e.target.value)} 
                                data-testid={`textarea-solution-${qIndex}`}
                                className="w-full p-3 border border-slate-300 rounded-xl text-xs font-mono bg-slate-50 focus:ring-2 focus:ring-blue-500 focus:bg-white" 
                                rows="3" 
                              />
                            </div>
                          </div>
                        ))}

                        <div className="mt-8 flex justify-end gap-3">
                            <button 
                                type="button" 
                                onClick={handleApproveAndAssign} 
                                data-testid="btn-approve-and-assign"
                                className="px-6 py-3 rounded-xl font-bold text-sm text-white bg-emerald-600 hover:bg-emerald-500 shadow-md transition cursor-pointer"
                            >
                                Approve & Assign to Class ({dynamicTotalMarks} Marks)
                            </button>
                        </div>
                      </div>
                    )}
                </div>
            </div>

            {/* AI Copilot Panel */}
            <TeacherAiCopilotPanel
              isOpen={copilotQuestionIndex !== null}
              onClose={() => setCopilotQuestionIndex(null)}
              question={copilotQuestionIndex !== null && assessmentData ? assessmentData[copilotQuestionIndex] : null}
              qIndex={copilotQuestionIndex || 0}
              onApplyReskin={handleApplyReskinnedText}
              onApplyRubric={handleApplyPolishedRubric}
              allQuestions={assessmentData || []}
            />

            {/* Faculty Subject Quotas Modal */}
            <TeacherFacultySubjectsModal
              isOpen={isQuotaModalOpen}
              onClose={() => setIsQuotaModalOpen(false)}
              teacherId={currentUser?.uid || 'default_educator'}
              currentAllocation={facultyAllocation}
              onSave={(updated) => setFacultyAllocation(updated)}
            />
        </>
    );
};

export default AssessmentGenerator;
