import React, { useState, useEffect } from 'react';
import {
    ChevronLeft,
    CheckCircle2,
    ArrowLeftRight,
    ArrowRight,
    Loader2,
    GraduationCap,
    GitBranch,
    X,
    Lightbulb,
    Clock,
    ShieldCheck,
    AlertTriangle,
    Sparkles,
    Settings,
    Lock,
    CheckSquare,
    ChevronDown,
    ChevronUp,
    Activity
} from 'lucide-react';
import MathText from './shared/mathx/MathText';
import MathModalityRenderer from './modalities/MathModalityRenderer';
import LedgerModalityRenderer from './modalities/LedgerModalityRenderer';
import RubricModalityRenderer from './modalities/RubricModalityRenderer';
import DiagramModalityRenderer from './modalities/DiagramModalityRenderer';
import ArithmeticGridModalityRenderer from './modalities/ArithmeticGridModalityRenderer';
import MasteryDial from '../student/MasteryDial';
import TopicScopeModal from '../curriculum/TopicScopeModal';
import studentStore from '../../services/studentStore';

const GeometricNets3DViewer = React.lazy(() => import('./modalities/GeometricNets3DViewer'));
const ElectrodynamicsMotorViewer = React.lazy(() => import('./modalities/ElectrodynamicsMotorViewer'));
const OrganicChemistry3DViewer = React.lazy(() => import('./modalities/OrganicChemistry3DViewer'));
const SuperAdminProgressResetModal = React.lazy(() => import('../admin/SuperAdminProgressResetModal'));
const SimuLearnPlayer = React.lazy(() => import('../simulearn/SimuLearnPlayer'));
const PostExamTriageModal = React.lazy(() => import('../exam/PostExamTriageModal'));

/**
 * UniversalWorkspace — Single unified cognitive question workspace for all Grades 7–12.
 * 
 * Option 1 Dual-Font System & Exact Simulation Box Palette:
 * - Display titles/headings: Afacad (`fontFamily: 'Afacad, sans-serif'`)
 * - Workspace cards, progression ribbon, hints, buttons, inputs: Crisp System Sans-Serif (`font-sans`)
 * - Tabular numbers, ledger coordinates, math procedures, timers: Strict `font-mono`
 * 
 * Color Palette:
 * - 60% `bg-slate-50` backdrop with pure `bg-white` cards and `border-slate-200`
 * - 30% `#13519C` Brand Blue for active progression pills, selected states, and primary brand indicators
 * - 10% purposeful cognitive feedback:
 *   * `#FF9100` / `bg-amber-50` / `border-amber-300` / `text-amber-900` for hints and diagnostic callouts
 *   * `#10B981` / `bg-emerald-50` / `border-emerald-300` / `text-emerald-800` for verified answers, marks credit
 *   * `#E11D48` / `bg-rose-50` / `border-rose-200` / `text-rose-700` for exam timer and error flags
 * 
 * Progression Hierarchy:
 * - [ 0. Diagnostic ] [ 1. Scaffold ] [ 2. Practice ] [ 3. Exam Mode ]
 * - When isDiagnosticRequired is true, active stage MUST BE '0. Diagnostic (Required)'.
 *   Stages 1, 2, 3 are clearly gated/locked with subtle 🔒 icon.
 */
/**
 * Renders multi-line prompt text cleanly:
 * - Splits into paragraphs / lines
 * - Highlights numbered transactions (e.g. "1. ", "Day 4: ") with font-mono badges & indentation
 * - Highlights bullet points ("- ", "• ") with clear indentation
 * - Formats sub-headings (e.g. "Required:", "Information:") with uppercase tracking
 * - Uses KaTeX via MathText for math expressions (\(... \) or $...$)
 * - Option 1 typography (crisp sans-serif, font-mono for monetary amounts)
 */
function formatTextWithMarkBadges(text) {
    if (!text || typeof text !== 'string') return text;
    // Match mark tokens: [M], [A], [CA], [X marks], [X mark], [1], [2]
    const parts = text.split(/(\[(?:M|A|CA|\d+\s*(?:marks?|mark)?|\d+)\])/g);
    if (parts.length === 1) return <MathText text={text} />;

    return (
        <span>
            {parts.map((part, pIdx) => {
                if (part === '[M]') {
                    return (
                        <span key={pIdx} className="inline-flex items-center px-1.5 py-0.2 mx-1 rounded bg-indigo-100 text-indigo-800 text-[11px] font-mono font-bold border border-indigo-200">
                            [M] Method
                        </span>
                    );
                }
                if (part === '[A]') {
                    return (
                        <span key={pIdx} className="inline-flex items-center px-1.5 py-0.2 mx-1 rounded bg-emerald-100 text-emerald-800 text-[11px] font-mono font-bold border border-emerald-200">
                            [A] Accuracy
                        </span>
                    );
                }
                if (part === '[CA]') {
                    return (
                        <span key={pIdx} className="inline-flex items-center px-1.5 py-0.2 mx-1 rounded bg-purple-100 text-purple-800 text-[11px] font-mono font-bold border border-purple-200">
                            [CA] Consequential
                        </span>
                    );
                }
                const markNumMatch = part.match(/^\[(\d+)\s*(?:marks?|mark)?\]$/i);
                if (markNumMatch) {
                    const mCount = markNumMatch[1];
                    return (
                        <span key={pIdx} className="inline-flex items-center px-1.5 py-0.2 mx-1 rounded bg-blue-100 text-[#13519C] text-[11px] font-mono font-bold border border-blue-200">
                            [{mCount} mark{Number(mCount) > 1 ? 's' : ''}]
                        </span>
                    );
                }
                return <MathText key={pIdx} text={part} />;
            })}
        </span>
    );
}

function renderFormattedPrompt(promptText) {
    if (!promptText || !promptText.trim()) {
        return (
            <p className="text-sm sm:text-base text-slate-500 italic font-sans">
                No question prompt loaded.
            </p>
        );
    }

    const lines = promptText.split(/\r?\n/);
    const blocks = [];
    let currentTable = null;

    for (let i = 0; i < lines.length; i++) {
        const rawLine = lines[i];
        const trimmed = rawLine.trim();

        // Check if line is part of a markdown table (starts and contains pipe, or is separator line)
        const isTableLine = trimmed.startsWith('|') && trimmed.endsWith('|') && trimmed.includes('|');
        const isSeparator = /^\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?$/.test(trimmed);

        if (isTableLine || (currentTable && isSeparator)) {
            if (!currentTable) {
                currentTable = [];
            }
            currentTable.push(trimmed);
        } else {
            if (currentTable) {
                blocks.push({ type: 'table', lines: currentTable });
                currentTable = null;
            }
            blocks.push({ type: 'text', raw: rawLine, trimmed });
        }
    }

    if (currentTable) {
        blocks.push({ type: 'table', lines: currentTable });
    }

    return (
        <div className="space-y-2 text-sm sm:text-base text-slate-800 leading-relaxed font-sans">
            {blocks.map((block, idx) => {
                if (block.type === 'table') {
                    const tableLines = block.lines;
                    if (tableLines.length === 0) return null;

                    // Parse header row
                    const headerRaw = tableLines[0];
                    const headers = headerRaw
                        .split('|')
                        .map((c) => c.trim())
                        .filter((_, cIdx, arr) => cIdx > 0 && cIdx < arr.length - 1);

                    // Determine row index where data starts
                    let dataStartIndex = 1;
                    const alignments = [];
                    if (tableLines.length > 1 && /^\|?(\s*:?-+:?\s*\|)+\s*:?-+:?\s*\|?$/.test(tableLines[1])) {
                        dataStartIndex = 2;
                        const sepCols = tableLines[1]
                            .split('|')
                            .map((c) => c.trim())
                            .filter((_, cIdx, arr) => cIdx > 0 && cIdx < arr.length - 1);

                        sepCols.forEach((col) => {
                            const left = col.startsWith(':');
                            const right = col.endsWith(':');
                            if (left && right) alignments.push('center');
                            else if (right) alignments.push('right');
                            else alignments.push('left');
                        });
                    }

                    const rows = [];
                    for (let r = dataStartIndex; r < tableLines.length; r++) {
                        const rowCols = tableLines[r]
                            .split('|')
                            .map((c) => c.trim())
                            .filter((_, cIdx, arr) => cIdx > 0 && cIdx < arr.length - 1);
                        if (rowCols.length > 0) {
                            rows.push(rowCols);
                        }
                    }

                    return (
                        <div key={idx} className="my-3 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-2xs">
                            <table className="min-w-full divide-y divide-slate-200 text-xs sm:text-sm font-sans">
                                {headers.length > 0 && (
                                    <thead className="bg-slate-100 text-slate-700 font-bold uppercase tracking-wider text-[11px]">
                                        <tr>
                                            {headers.map((h, hIdx) => {
                                                const align = alignments[hIdx] || 'left';
                                                return (
                                                    <th
                                                        key={hIdx}
                                                        className={`px-3.5 py-2.5 ${
                                                            align === 'right'
                                                                ? 'text-right'
                                                                : align === 'center'
                                                                    ? 'text-center'
                                                                    : 'text-left'
                                                        }`}
                                                    >
                                                        <MathText text={h} />
                                                    </th>
                                                );
                                            })}
                                        </tr>
                                    </thead>
                                )}
                                <tbody className="divide-y divide-slate-100 bg-white">
                                    {rows.map((row, rIdx) => (
                                        <tr key={rIdx} className="odd:bg-white even:bg-slate-50/70 hover:bg-blue-50/40 transition-colors">
                                            {row.map((cell, cIdx) => {
                                                const align = alignments[cIdx] || 'left';
                                                const isNumeric = /^(R|\$|-|\+)?\s*\d/.test(cell.trim());
                                                return (
                                                    <td
                                                        key={cIdx}
                                                        className={`px-3.5 py-2 text-slate-800 ${
                                                            align === 'right' || isNumeric
                                                                ? 'text-right font-mono font-medium'
                                                                : align === 'center'
                                                                    ? 'text-center font-mono'
                                                                    : 'text-left'
                                                        }`}
                                                    >
                                                        <MathText text={cell} />
                                                    </td>
                                                );
                                            })}
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    );
                }

                // Text line handling
                const line = block.trimmed;

                // Blank line spacer
                if (!line) {
                    return <div key={idx} className="h-1.5" />;
                }

                // Horizontal divider (e.g. "---")
                if (/^---+$/.test(line)) {
                    return <hr key={idx} className="my-2 border-t border-blue-200/80" />;
                }

                // Section header (e.g. "Required:", "Information:", "Transactions:", "The following balances...")
                const isHeading =
                    /^(required|information|transactions|balances|instructions|note|statement|details):?$/i.test(line) ||
                    (/^(\*\*|#+)?[A-Z][A-Za-z0-9\s—\-&]+:?(\*\*)?$/.test(line) && line.length < 50);

                if (isHeading) {
                    return (
                        <div key={idx} className="pt-2 pb-0.5 border-b border-slate-200">
                            <h5 className="font-bold text-slate-900 text-xs uppercase tracking-wider font-sans">
                                {line.replace(/\*\*/g, '').replace(/^#+\s*/, '')}
                            </h5>
                        </div>
                    );
                }

                // Numbered transaction or day item (e.g. "1. ", "2) ", "Day 4:", "14. ")
                const numberedMatch = line.match(/^(\d+[.)]|\bDay\s+\d+:?)\s+(.*)$/i);
                if (numberedMatch) {
                    const [, numPrefix, content] = numberedMatch;
                    return (
                        <div key={idx} className="flex items-start gap-2.5 my-1 pl-1">
                            <span className="shrink-0 px-2 py-0.5 rounded-md bg-slate-100 text-slate-700 text-xs font-mono font-bold border border-slate-200 mt-0.5 shadow-2xs">
                                {numPrefix}
                            </span>
                            <div className="text-slate-800 text-sm leading-relaxed flex-1">
                                {formatTextWithMarkBadges(content)}
                            </div>
                        </div>
                    );
                }

                // Bullet item (e.g. "- Bank: R22 400.00", "• Trading stock...")
                const bulletMatch = line.match(/^([-•*])\s+(.*)$/);
                if (bulletMatch) {
                    const [, , content] = bulletMatch;
                    return (
                        <div key={idx} className="flex items-start gap-2.5 my-1 pl-2">
                            <span className="shrink-0 text-[#13519C] font-bold text-base leading-none mt-0.5">•</span>
                            <div className="text-slate-800 text-sm leading-relaxed flex-1">
                                {formatTextWithMarkBadges(content)}
                            </div>
                        </div>
                    );
                }

                // Standard paragraph / line
                return (
                    <p key={idx} className="text-slate-800 text-sm sm:text-base leading-relaxed">
                        {formatTextWithMarkBadges(line)}
                    </p>
                );
            })}
        </div>
    );
}

function extractMemorandumContent(question) {
    if (!question) return '';
    const sections = [];

    // 1. Step-by-step mathematical / logical procedure (Canonical SymPy solution)
    if (question.canonical_solution && typeof question.canonical_solution === 'object') {
        const cs = question.canonical_solution;
        const steps = [];
        if (Array.isArray(cs.steps) && cs.steps.length > 0) {
            steps.push('**Step-by-Step Procedure & Symbolic Transitions:**');
            cs.steps.forEach((st, idx) => {
                const stepLatex = st.to_latex || st.latex || st.step || '';
                const opDesc = st.op ? ` *(${st.op})*` : '';
                const markTag = st.mark_type ? ` [${st.mark_type}]` : (idx === cs.steps.length - 1 ? ' [A]' : ' [M]');
                steps.push(`${idx + 1}. $${stepLatex}$${opDesc} ${markTag}`);
            });
        }
        if (cs.final_latex) {
            steps.push(`**Final Evaluated Answer:** $${cs.final_latex}$ [A]`);
        }
        if (steps.length > 0) sections.push(steps.join('\n\n'));
    } else if (Array.isArray(question.steps) && question.steps.length > 0) {
        const formattedSteps = question.steps.map((s, idx) => {
            if (typeof s === 'string') return `${idx + 1}. ${s}`;
            return `${idx + 1}. ${s.explanation || s.step || s.rule || JSON.stringify(s)}`;
        }).join('\n\n');
        sections.push(formattedSteps);
    }

    // 2. Primary narrative/semantic solution or worked solution
    const primarySolution = (
        (typeof question.worked_solution === 'string' && question.worked_solution.trim() && question.worked_solution) ||
        (typeof question.solution === 'string' && question.solution.trim() && question.solution) ||
        (typeof question.model_answer === 'string' && question.model_answer.trim() && question.model_answer) ||
        (typeof question.ideal_answer === 'string' && question.ideal_answer.trim() && question.ideal_answer) ||
        (typeof question.memo === 'string' && question.memo.trim() && question.memo) ||
        (typeof question.explanation === 'string' && question.explanation.trim() && question.explanation) ||
        (question.correct_answer ? `**Expected Answer:** ${question.correct_answer}` : '')
    );
    if (primarySolution && !sections.includes(primarySolution)) {
        sections.push(primarySolution);
    }

    // 3. Official CAPS Marking Points Allocation & Schema Breakdown (Semantic / Logic Solutions)
    const markingPoints = (
        (Array.isArray(question.marking_schema?.marking_points) && question.marking_schema.marking_points) ||
        (Array.isArray(question.marking_points) && question.marking_points) ||
        null
    );
    if (markingPoints && markingPoints.length > 0) {
        const schemaLines = ['**Official Marking Points Allocation:**'];
        markingPoints.forEach((mp, idx) => {
            if (typeof mp === 'string') {
                schemaLines.push(`• Point ${idx + 1}: ${mp}`);
            } else {
                const desc = mp.desc || mp.point || mp.name || '';
                const marks = mp.marks || 1;
                schemaLines.push(`• Point ${idx + 1} [${marks} marks]: ${desc}`);
            }
        });
        sections.push(schemaLines.join('\n'));
    } else if (Array.isArray(question.content_rubric) && question.content_rubric.length > 0) {
        const rubricLines = ['**Official Content Rubric Criteria:**'];
        question.content_rubric.forEach((cr, idx) => {
            const criterion = cr.criterion || `Criterion ${idx + 1}`;
            const maxMarks = cr.max_marks || 2;
            const concepts = Array.isArray(cr.key_concepts) ? ` *(Target concepts: ${cr.key_concepts.join(', ')})*` : '';
            rubricLines.push(`• ${criterion} [${maxMarks} marks]${concepts}`);
        });
        sections.push(rubricLines.join('\n'));
    }

    // 4. Marking guidelines fallback
    if (Array.isArray(question.guidelines) && question.guidelines.length > 0) {
        sections.push('**Marking Guidelines:**\n' + question.guidelines.join('\n'));
    }

    return sections.length > 0 ? sections.join('\n\n---\n\n') : 'Complete standard marking steps.';
}

export default function UniversalWorkspace({
    grade,
    subject,
    topic,
    question,
    isGenerating = false,
    isChecking = false,
    onBack,
    onCheck,
    onCompare,
    onNext,
    onStartMicroDrill,
    onSelectTopic,
    prerequisiteBanner,
    generationError,
    result,
    isEmbedded = false,
    formativeMastery = 0,
    evaluativeScore = 0,
    initialProgressionMode,
    onProgressionModeChange,
}) {
    const subjectTitle = typeof subject === 'string' ? subject : subject?.name || 'Subject';
    const normalizedSubId = String(subjectTitle).toLowerCase().replace(/\s+/g, '_');

    // Subscribe to studentStore to reflect active live mastery
    const [storeState, setStoreState] = useState(() => studentStore.getState());
    useEffect(() => {
        const unsub = studentStore.subscribe((newState) => {
            setStoreState({ ...newState });
        });
        return unsub;
    }, []);

    const subData = storeState?.subjects?.[normalizedSubId] || studentStore.getSubject(normalizedSubId);
    const currentFormative = subData.formativeMastery ?? formativeMastery;
    const currentEvaluative = subData.evaluativeScore ?? evaluativeScore;
    
    // Diagnostic requirement check: status is 'diagnostic_required' AND 0 attempts
    const isDiagnosticRequired = subData.status === 'diagnostic_required' && (subData.questionsAttempted || 0) === 0;

    // Initial progression mode resolution:
    // If diagnostic is required, active mode MUST be 'diagnostic', NOT 'practice'
    const getComputedProgressionMode = () => {
        if (isDiagnosticRequired) return 'diagnostic';
        if (initialProgressionMode && initialProgressionMode !== 'diagnostic') return initialProgressionMode;
        if (currentFormative >= 80) return 'assessment';
        if (currentFormative >= 60) return 'practice';
        return 'scaffold';
    };

    const [progressionMode, setProgressionMode] = useState(getComputedProgressionMode);
    const [gateNotice, setGateNotice] = useState(null);
    const [showAdminResetModal, setShowAdminResetModal] = useState(false);
    const [showTopicModal, setShowTopicModal] = useState(false);
    const [isChecked, setIsChecked] = useState(false);
    const [isComparing, setIsComparing] = useState(false);
    const [showHints, setShowHints] = useState(false);
    const [showGuidelines, setShowGuidelines] = useState(false);
    const [diagnosticIndex, setDiagnosticIndex] = useState(1); // 1, 2, or 3 of 3-question diagnostic cluster
    const [diagnosticScores, setDiagnosticScores] = useState([]);
    const [activeHintTier, setActiveHintTier] = useState(1);
    const [examTimer, setExamTimer] = useState(600); // 10 minutes in seconds
    const [showMasteryDial, setShowMasteryDial] = useState(false);
    const [showSimuLearn, setShowSimuLearn] = useState(false);
    const [showTriageModal, setShowTriageModal] = useState(false);
    const [remedialRepaired, setRemedialRepaired] = useState(false);
    const [showFullMemo, setShowFullMemo] = useState(false);

    // Resolve canonical SimuLearn script based on subject and topic
    const getSimuLearnKey = () => {
        const s = String(normalizedSubId).toLowerCase();
        const t = String(topic || '').toLowerCase();
        if (s.includes('acc') || s.includes('ems') || t.includes('crj') || t.includes('vat')) return 'accounting_crj_vat';
        if (s.includes('phys') || s.includes('chem') || t.includes('kinematic')) return 'physics_kinematics_dx';
        if (s.includes('life')) return 'lifesci_genetics_punnett';
        if (s.includes('tech')) return 'techmaths_mensuration_circle';
        return 'math_quadratic_trinomial';
    };

    // Desktop ergonomics: during active problem solving, keep question surface clean & full-width.
    const isAnswered = isChecked || Boolean(result);

    // Synchronize mode whenever subject changes
    useEffect(() => {
        if (isDiagnosticRequired) {
            setProgressionMode('diagnostic');
            setShowHints(false);
            setDiagnosticIndex(1);
            setDiagnosticScores([]);
        }
    }, [normalizedSubId, isDiagnosticRequired]);

    useEffect(() => {
        setIsChecked(false);
        setIsComparing(false);
        setShowHints(false);
        setShowGuidelines(false);
        setShowMasteryDial(false);
        setShowFullMemo(false);
        setRemedialRepaired(false);
    }, [question?.id]);

    // Exam countdown timer
    useEffect(() => {
        if (progressionMode !== 'assessment') return;
        const interval = setInterval(() => {
            setExamTimer((prev) => (prev > 0 ? prev - 1 : 0));
        }, 1000);
        return () => clearInterval(interval);
    }, [progressionMode]);

    const formatTimer = (seconds) => {
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    };

    const handleCheckWrapper = async (userAnswer) => {
        let evalResult = null;
        if (onCheck) {
            evalResult = await onCheck(userAnswer);
            setIsChecked(true);
        }
        // If in diagnostic mode, calibrate baseline across 3-question cluster
        if (isDiagnosticRequired) {
            const rawScore = typeof evalResult?.score === 'number' 
                ? evalResult.score 
                : (typeof result?.score === 'number' ? result.score : null);
            const rawTotal = evalResult?.total || result?.total || question?.marks || 10;
            const currentItemPct = (rawScore !== null && rawScore >= 0) 
                ? Math.round((rawScore / rawTotal) * 100) 
                : 85;
            
            if (diagnosticIndex >= 3) {
                // Completed the full 3-question diagnostic probe! Aggregate all 3 items.
                const allScores = [...diagnosticScores, currentItemPct];
                const aggregatedScorePct = Math.round(allScores.reduce((acc, val) => acc + val, 0) / allScores.length);
                studentStore.completeDiagnostic(normalizedSubId, aggregatedScorePct);
                setGateNotice(null);
            } else {
                setDiagnosticScores((prev) => [...prev, currentItemPct]);
            }
        }
    };

    const handleCompareToggle = () => {
        if (onCompare) {
            onCompare();
        }
        setIsComparing((prev) => !prev);
    };

    const handleModeSwitch = (modeId) => {
        if (isGenerating) return;
        // If diagnostic is required, gated stages 1, 2, 3 show gentle guidance
        if (isDiagnosticRequired && modeId !== 'diagnostic') {
            setGateNotice("Complete your diagnostic baseline first to calibrate your learning path.");
            setTimeout(() => setGateNotice(null), 4500);
            return;
        }

        // If exam mode is selected before reaching 80% BKT mastery
        if (modeId === 'assessment' && currentFormative < 80) {
            setGateNotice("Reach 80% Topic Mastery in Practice to unlock Timed Exam Mode.");
            setTimeout(() => setGateNotice(null), 4500);
            return;
        }

        setGateNotice(null);
        setProgressionMode(modeId);
        if (onProgressionModeChange) onProgressionModeChange(modeId);
        setShowHints(false);
    };

    const handleCalibrateBaseline = (startingScore = 55) => {
        studentStore.completeDiagnostic(normalizedSubId, startingScore);
        setGateNotice(null);
        setProgressionMode(startingScore >= 60 ? 'practice' : 'scaffold');
    };

    // Extract deterministic 3-tier hints
    const rawHints = question?.hints;
    const hints = {
        tier_1: (typeof rawHints === 'object' && rawHints?.tier_1) || rawHints?.[0] || 'Carefully inspect the parameters given in the question and identify the required formula or accounting columns.',
        tier_2: (typeof rawHints === 'object' && rawHints?.tier_2) || rawHints?.[1] || question?.explanation || 'Apply standard procedural steps: isolate the unknowns and check directional signs or contra accounts.',
        tier_3: (typeof rawHints === 'object' && rawHints?.tier_3) || rawHints?.[2] || question?.worked_solution || 'Refer to the memo calculation to verify your step.'
    };

    // Determine cognitive modality from question payload or subject domain
    const modality = (() => {
        const topLower = String(topic || '').toLowerCase();
        const subLower = String(subjectTitle || '').toLowerCase();

        // 1. SOTA Visual Modalities (AI Blackboard showcase)
        if (
            question?.modality === 'geometric_nets' ||
            topLower.includes('geometry of 3d') ||
            topLower.includes('geometric net') ||
            topLower.includes('3d object') ||
            topLower.includes('platonic solid')
        ) return 'geometric_nets';

        if (
            question?.modality === 'electrodynamics' ||
            topLower.includes('electrodynamics') ||
            topLower.includes('ac generator') ||
            topLower.includes('dc motor') ||
            topLower.includes('armature')
        ) return 'electrodynamics';

        if (
            question?.modality === 'organic_chemistry' ||
            topLower.includes('organic chemistry') ||
            topLower.includes('isomer') ||
            topLower.includes('homologous series')
        ) return 'organic_chemistry';

        // 2. Fundamental & Standard Modalities
        if (
            question?.modality === 'arithmetic_grid' || 
            question?.arithmetic_grid || 
            question?.subskill === 'long_division' ||
            topLower.includes('whole numbers') ||
            topLower.includes('long division')
        ) return 'arithmetic_grid';
        if (question?.modality === 'ledger' || question?.journal || question?.table_schema) return 'ledger';
        if (question?.options || question?.options_latex || question?.question_type === 'mcq') return 'math';
        if (question?.modality === 'diagram' || question?.diagram_spec || question?.diagram) return 'diagram';

        // 3. Explicit Archetype Semantic Modality
        if (
            question?.modality === 'semantic' ||
            question?.modality === 'rubric' ||
            ['rubric', 'essay', 'short_answer', 'typed', 'conceptual'].includes(question?.question_type) ||
            Boolean(question?.content_rubric || question?.marking_points || question?.marking_schema?.marking_points)
        ) {
            return 'semantic';
        }

        if (question?.modality) return question.modality;
        return 'math';
    })();

    // Extract authentic prompt text across all backend generator schemas
    const promptText = question?.prompt || question?.question || question?.question_text || question?.instruction || question?.prompt_latex || '';

    const isExamReady = currentFormative >= 80;

    return (
        <div className={isEmbedded ? "w-full h-full relative font-sans" : "min-h-screen bg-slate-50 relative font-sans"}>
            
            {/* ── UNIFIED 1-LINE WORKSPACE HEADER (Prominent Question & Answer Layout) ── */}
            <div className="bg-white rounded-xl border border-slate-200/90 px-3.5 py-2 flex flex-wrap items-center justify-between gap-2.5 shadow-2xs text-xs font-sans">
                
                {/* Left: Studio Navigation & Topic Scope Selector */}
                <div className="flex items-center gap-2 min-w-0">
                    {onBack && (
                        <button
                            type="button"
                            data-testid="tab-desk"
                            onClick={onBack}
                            className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100 text-[#13519C] hover:text-[#0F4280] transition font-bold text-xs cursor-pointer shrink-0"
                            title="Return to Self-Paced Studio"
                        >
                            <ChevronLeft className="w-3.5 h-3.5" />
                            <span>Studio</span>
                        </button>
                    )}

                    <button
                        type="button"
                        data-testid="btn-topic-scope"
                        onClick={() => setShowTopicModal(true)}
                        className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg border border-slate-200 hover:border-[#13519C] bg-white hover:bg-blue-50/60 text-slate-900 transition cursor-pointer font-bold truncate max-w-[220px] sm:max-w-xs text-xs"
                        title="Click to Change Topic or Scope"
                    >
                        <span className="truncate">{topic || 'Problem Solving'}</span>
                        <ChevronDown className="w-3 h-3 text-slate-500 shrink-0" />
                    </button>

                    {isDiagnosticRequired && (
                        <div className="flex items-center gap-1.5 shrink-0">
                            <span className="hidden md:inline-flex items-center gap-1 px-2 py-0.5 rounded-full bg-amber-100 text-amber-900 border border-amber-300 font-extrabold text-[10px] font-mono">
                                Diagnostic ({diagnosticIndex}/3)
                            </span>
                            <button
                                type="button"
                                data-testid="btn-calibrate-baseline"
                                onClick={() => handleCalibrateBaseline(55)}
                                className="px-2 py-0.5 rounded-md bg-amber-600 hover:bg-amber-700 text-white font-bold text-[10px] transition cursor-pointer shadow-2xs"
                                title="Calibrate diagnostic baseline (55%)"
                            >
                                Calibrate
                            </button>
                        </div>
                    )}
                </div>

                {/* Center: Progression Mode Switcher (0. Diag, 1. Scaffold, 2. Practice, 3. Exam) */}
                <div className={`flex items-center gap-1 p-0.5 bg-slate-100 rounded-lg border border-slate-200 text-[11px] font-bold shadow-2xs ${isGenerating ? 'opacity-70 pointer-events-none' : ''}`}>
                    <button
                        type="button"
                        disabled={isGenerating}
                        data-testid="btn-mode-diagnostic"
                        onClick={() => handleModeSwitch('diagnostic')}
                        className={`px-2 py-0.5 rounded-md transition cursor-pointer flex items-center gap-1 ${
                            progressionMode === 'diagnostic'
                                ? 'bg-[#13519C] text-white shadow-2xs'
                                : isDiagnosticRequired
                                ? 'bg-amber-100 text-amber-900'
                                : 'text-slate-600 hover:text-slate-900'
                        }`}
                        title="Diagnostic Mode"
                    >
                        <span>0. Diag</span>
                        {isDiagnosticRequired ? (
                            <span className="text-[8px] bg-[#FF9100] text-white px-1 rounded font-extrabold">Req</span>
                        ) : (
                            <span className="text-emerald-600">✓</span>
                        )}
                    </button>

                    <button
                        type="button"
                        data-testid="btn-mode-scaffold"
                        onClick={() => handleModeSwitch('scaffold')}
                        className={`px-2 py-0.5 rounded-md transition flex items-center gap-1 cursor-pointer ${
                            progressionMode === 'scaffold'
                                ? 'bg-[#13519C] text-white shadow-2xs'
                                : isDiagnosticRequired
                                ? 'text-slate-400 opacity-60'
                                : 'text-slate-600 hover:text-slate-900'
                        }`}
                        title="1. Scaffold Mode: Step-by-step guidance"
                    >
                        <span>1. Scaffold</span>
                        {isDiagnosticRequired && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                    </button>

                    <button
                        type="button"
                        data-testid="btn-mode-practice"
                        onClick={() => handleModeSwitch('practice')}
                        className={`px-2 py-0.5 rounded-md transition flex items-center gap-1 cursor-pointer ${
                            progressionMode === 'practice'
                                ? 'bg-[#13519C] text-white shadow-2xs'
                                : isDiagnosticRequired
                                ? 'text-slate-400 opacity-60'
                                : 'text-slate-600 hover:text-slate-900'
                        }`}
                        title="2. Practice Mode: Autonomous problem solving"
                    >
                        <span>2. Practice</span>
                        {isDiagnosticRequired && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                    </button>

                    <button
                        type="button"
                        data-testid="btn-mode-assessment"
                        onClick={() => handleModeSwitch('assessment')}
                        className={`px-2 py-0.5 rounded-md transition flex items-center gap-1 cursor-pointer ${
                            progressionMode === 'assessment'
                                ? 'bg-rose-600 text-white shadow-2xs'
                                : isDiagnosticRequired || currentFormative < 80
                                ? 'text-slate-400 opacity-60'
                                : 'text-slate-600 hover:text-slate-900'
                        }`}
                        title="3. Exam Mode: Timed formal assessment"
                    >
                        <span>3. Exam</span>
                        {(isDiagnosticRequired || currentFormative < 80) && <Lock className="w-2.5 h-2.5 text-slate-400" />}
                    </button>
                </div>

                {/* Right: Marks, Mastery & Hints Toggle / Timer */}
                <div className="flex items-center gap-2.5 shrink-0">
                    {progressionMode === 'assessment' ? (
                        <div data-testid="exam-timer-display" className="flex items-center gap-1 px-2.5 py-0.5 rounded-lg bg-rose-50 border border-rose-200 text-rose-700 font-bold font-mono text-xs">
                            <Clock className="w-3 h-3 text-rose-600 animate-pulse" />
                            <span>{formatTimer(examTimer)}</span>
                        </div>
                    ) : (
                        progressionMode !== 'diagnostic' && (
                            <button
                                type="button"
                                data-testid="btn-toggle-hints"
                                onClick={() => setShowHints(!showHints)}
                                className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-lg text-xs font-bold transition cursor-pointer ${
                                    showHints
                                        ? 'bg-[#FF9100] text-white shadow-2xs'
                                        : 'bg-amber-50 text-amber-900 border border-amber-300 hover:bg-amber-100'
                                }`}
                                title="Toggle 3-Tier Pre-calculated Hints"
                            >
                                <Lightbulb className="w-3 h-3 text-amber-600" />
                                <span>{showHints ? 'Hide Hints' : '💡 Hints'}</span>
                            </button>
                        )
                    )}

                    <div className="flex items-center gap-2 pl-1 border-l border-slate-200 text-xs">
                        <span className="font-bold text-amber-700 font-mono">
                            {question?.marks || 6} Marks
                        </span>
                        <span className="text-[11px] font-semibold text-slate-500 font-mono hidden sm:inline">
                            • {currentFormative}% Mastery
                        </span>
                    </div>
                </div>
            </div>

            {/* ── Gated Stage Notification Banner ── */}
            {gateNotice && (
                <div className="mt-2 px-4 py-2 bg-amber-50 border border-amber-300 rounded-xl flex items-center justify-between text-xs text-amber-900 shadow-2xs animate-in fade-in">
                    <div className="flex items-center gap-2">
                        <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
                        <span className="font-semibold">{gateNotice}</span>
                    </div>
                    <button
                        type="button"
                        onClick={() => setGateNotice(null)}
                        className="text-amber-700 hover:text-amber-900 font-bold cursor-pointer text-xs"
                    >
                        Dismiss
                    </button>
                </div>
            )}

            {/* ── 3-TIER PRE-BAKED HINTS DRAWER (Scaffold & Practice Mode) ── */}
            {showHints && progressionMode !== 'assessment' && progressionMode !== 'diagnostic' && (
                <div className="mt-2 px-4 py-3 bg-amber-50/80 border border-amber-300 rounded-xl space-y-2 text-xs font-sans animate-in fade-in">
                    <div className="flex items-center justify-between">
                        <div className="flex items-center gap-2">
                            <span className="text-[10px] font-bold uppercase tracking-wider text-amber-900 bg-amber-200/60 border border-amber-300 px-2 py-0.5 rounded font-mono">
                                DETERMINISTIC 3-TIER HINT ENGINE
                            </span>
                            <span className="text-amber-800 text-[11px] hidden sm:inline">
                                Pre-calculated ahead of time with zero token cost
                            </span>
                        </div>
                        <div className="flex gap-1 bg-white p-0.5 rounded-lg border border-amber-200 text-[10px] font-bold shadow-2xs">
                            {[1, 2, 3].map((tier) => (
                                <button
                                    key={tier}
                                    type="button"
                                    data-testid={`btn-hint-tier-${tier}`}
                                    onClick={() => setActiveHintTier(tier)}
                                    className={`px-2.5 py-0.5 rounded transition cursor-pointer ${
                                        activeHintTier === tier
                                            ? 'bg-[#13519C] text-white font-bold'
                                            : 'text-slate-600 hover:text-slate-900'
                                    }`}
                                >
                                    Tier {tier}: {tier === 1 ? 'Nudge' : tier === 2 ? 'Rule' : 'Worked Step'}
                                </button>
                            ))}
                        </div>
                    </div>

                    <div className="p-3 bg-white border border-amber-200 rounded-xl text-slate-800 text-xs leading-relaxed shadow-2xs">
                        {activeHintTier === 1 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 1 (Location / Nudge):</strong> {hints.tier_1}
                            </div>
                        )}
                        {activeHintTier === 2 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 2 (Directional Rule):</strong> {hints.tier_2}
                            </div>
                        )}
                        {activeHintTier === 3 && (
                            <div>
                                <strong className="text-amber-800 font-bold">Tier 3 (Worked Step Calculation):</strong> {hints.tier_3}
                            </div>
                        )}
                        <div className="flex flex-wrap items-center justify-between gap-2 pt-2 border-t border-amber-200/60 mt-2 text-[11px]">
                            <span className="text-slate-600 font-medium">Stuck on this concept? Watch step-by-step vector replay:</span>
                            <button
                                type="button"
                                data-testid="btn-launch-simulearn"
                                onClick={() => setShowSimuLearn(true)}
                                className="text-indigo-700 hover:text-indigo-900 font-bold flex items-center gap-1 cursor-pointer bg-indigo-50 border border-indigo-200 px-2.5 py-0.5 rounded shadow-2xs"
                            >
                                ▶ Watch SimuLearn Worked Solution
                            </button>
                        </div>
                    </div>
                </div>
            )}

            {/* Prerequisite Regression Banner (If triggered) */}
            {prerequisiteBanner && (
                <div data-testid="banner-prerequisite-gap" className="mt-2 rounded-2xl border border-amber-300 bg-amber-50/80 p-4 space-y-2 text-xs shadow-xs font-sans">
                    <div className="flex items-center gap-2">
                        <GitBranch className="w-4 h-4 text-amber-600" />
                        <span className="font-bold text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                            Prerequisite Gap Identified (Grade {prerequisiteBanner.target_grade})
                        </span>
                    </div>
                    <p className="text-slate-600 leading-relaxed">
                        {prerequisiteBanner.explanation || 'Step down recommended to master foundational rules.'}
                    </p>
                    <div className="flex flex-wrap items-center gap-3 pt-1">
                        <button
                            type="button"
                            data-testid="btn-start-micro-drill"
                            onClick={() => onStartMicroDrill && onStartMicroDrill(prerequisiteBanner)}
                            className="text-xs font-bold text-[#13519C] hover:underline flex items-center gap-1 cursor-pointer"
                        >
                            Start 5-Min Prerequisite Drill →
                        </button>
                        <button
                            type="button"
                            data-testid="btn-launch-simulearn"
                            onClick={() => setShowSimuLearn(true)}
                            className="text-xs font-bold text-indigo-700 bg-indigo-100/90 hover:bg-indigo-200/90 px-2.5 py-1 rounded-md flex items-center gap-1 cursor-pointer transition shadow-2xs"
                        >
                            ▶ Watch SimuLearn Worked Solution
                        </button>
                    </div>
                </div>
            )}

            {/* ── MAIN QUESTION WORKSPACE (Front and Center Prominence) ── */}
            <div className="mt-3 w-full space-y-4">
                <div 
                    data-testid="question-surface"
                    data-source={question?.source || (question ? 'deterministic_generator' : 'none')}
                    className="rounded-2xl border border-slate-200 bg-white p-4 sm:p-6 space-y-4 shadow-xs font-sans"
                >

                        {/* Question Prompt */}
                        {isGenerating ? (
                            <div className="rounded-xl border border-blue-200 bg-blue-50 px-6 py-8 flex flex-col items-center justify-center text-center space-y-3">
                                <Loader2 className="w-8 h-8 text-[#13519C] animate-spin" />
                                <p className="text-sm font-semibold text-slate-900">Generating authentic question...</p>
                                <p className="text-xs text-slate-600">Deterministic values calibrated to your mastery level.</p>
                            </div>
                        ) : generationError ? (
                            <div className="rounded-xl border border-rose-200 bg-rose-50 p-4 text-xs font-semibold text-rose-800">
                                {generationError}
                            </div>
                        ) : (
                            <div className="rounded-xl border border-slate-200/90 bg-slate-50/70 p-4 sm:p-5 shadow-2xs font-sans transition-all space-y-3">
                                <div className="pb-2 border-b border-slate-200/70">
                                    <span className="text-xs font-bold text-slate-800 uppercase tracking-wider font-mono">
                                        Question
                                    </span>
                                </div>

                                {renderFormattedPrompt(promptText)}

                                {Array.isArray(question?.guidelines) && question.guidelines.length > 0 && (
                                    <div className="rounded-xl border border-slate-200 bg-white p-3 space-y-2 mt-3 font-sans shadow-2xs">
                                        <div className="flex items-center justify-between">
                                            <div className="flex items-center gap-2">
                                                <span className="w-5 h-5 rounded-md bg-[#13519C]/10 text-[#13519C] flex items-center justify-center text-xs font-bold font-mono">
                                                    📋
                                                </span>
                                                <span className="text-xs font-bold text-slate-800 uppercase tracking-wide font-sans">
                                                    Exam Guidelines &amp; Criteria
                                                </span>
                                                <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-blue-100 text-[#13519C] font-mono">
                                                    {question.guidelines.length} {question.guidelines.length === 1 ? 'rule' : 'rules'}
                                                </span>
                                            </div>
                                            <button
                                                type="button"
                                                data-testid="btn-toggle-guidelines"
                                                onClick={() => setShowGuidelines((prev) => !prev)}
                                                className="text-xs font-semibold text-[#13519C] hover:underline cursor-pointer flex items-center gap-1 font-sans"
                                            >
                                                {showGuidelines ? (
                                                    <>Hide Criteria <ChevronUp className="w-3.5 h-3.5" /></>
                                                ) : (
                                                    <>View Criteria <ChevronDown className="w-3.5 h-3.5" /></>
                                                )}
                                            </button>
                                        </div>

                                        {showGuidelines && (
                                            <div className="pt-2 border-t border-slate-200/60 grid sm:grid-cols-2 gap-2 text-xs text-slate-700">
                                                {question.guidelines.map((guideline, gIdx) => (
                                                    <div key={gIdx} className="flex items-start gap-2 bg-slate-50 p-2.5 rounded-lg border border-slate-200/60 shadow-2xs">
                                                        <CheckSquare className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                                                        <span className="leading-snug flex-1">
                                                            <MathText text={guideline} />
                                                        </span>
                                                    </div>
                                                ))}
                                            </div>
                                        )}
                                    </div>
                                )}
                            </div>
                        )}

                        {/* Modality Interaction Slot (Ledger, Math, Rubric, Diagram) */}
                        {!isGenerating && question && (
                            <div className="rounded-xl border border-slate-200/90 bg-white p-4 sm:p-5 shadow-2xs font-sans transition-all space-y-4">
                                <div className="pb-2 border-b border-slate-200/70">
                                    <span className="text-xs font-bold text-slate-800 uppercase tracking-wider font-mono">
                                        Answer
                                    </span>
                                </div>
                                {modality === 'ledger' && (
                                    <LedgerModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {(modality === 'rubric' || modality === 'semantic') && (
                                    <RubricModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'diagram' && (
                                    <DiagramModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'arithmetic_grid' && (
                                    <ArithmeticGridModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}
                                {modality === 'geometric_nets' && (
                                    <div className="space-y-4">
                                        <React.Suspense fallback={<div className="h-64 flex items-center justify-center bg-slate-100 rounded-xl animate-pulse"><Loader2 className="w-6 h-6 animate-spin text-[#13519C]" /></div>}>
                                            <GeometricNets3DViewer />
                                        </React.Suspense>
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'electrodynamics' && (
                                    <div className="space-y-4">
                                        <React.Suspense fallback={<div className="h-64 flex items-center justify-center bg-slate-100 rounded-xl animate-pulse"><Loader2 className="w-6 h-6 animate-spin text-[#13519C]" /></div>}>
                                            <ElectrodynamicsMotorViewer />
                                        </React.Suspense>
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'organic_chemistry' && (
                                    <div className="space-y-4">
                                        <React.Suspense fallback={<div className="h-64 flex items-center justify-center bg-slate-100 rounded-xl animate-pulse"><Loader2 className="w-6 h-6 animate-spin text-[#13519C]" /></div>}>
                                            <OrganicChemistry3DViewer />
                                        </React.Suspense>
                                        <MathModalityRenderer
                                            question={question}
                                            topic={topic}
                                            onCheck={handleCheckWrapper}
                                            result={result}
                                            isChecking={isChecking}
                                            showDynamicScaffold={showHints}
                                            onToggleScaffold={() => setShowHints((prev) => !prev)}
                                        />
                                    </div>
                                )}
                                {modality === 'math' && (
                                    <MathModalityRenderer
                                        question={question}
                                        topic={topic}
                                        onCheck={handleCheckWrapper}
                                        result={result}
                                        isChecking={isChecking}
                                        showDynamicScaffold={showHints}
                                        onToggleScaffold={() => setShowHints((prev) => !prev)}
                                    />
                                )}

                                {/* Verified Consequential Marks Banner */}
                                {(isChecked || Boolean(result)) && (
                                    <div className="p-3 bg-emerald-50 border border-emerald-300 rounded-xl flex flex-wrap items-center justify-between gap-2 text-xs text-emerald-900 shadow-2xs animate-in fade-in">
                                        <div className="flex items-center gap-2">
                                            <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
                                            <span>
                                                {result?.score ?? question?.marks ?? 6} / {result?.total ?? question?.marks ?? 6} Marks Awarded • Schema Verified: {result?.feedback || 'Net calculation and entry extracted accurately.'}
                                            </span>
                                        </div>
                                        <div className="flex items-center gap-2">
                                            {remedialRepaired ? (
                                                <div data-testid="badge-remedial-repaired" className="px-2.5 py-0.5 rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-300 text-xs font-bold flex items-center gap-1 font-mono">
                                                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" />
                                                    <span>Concept Repaired</span>
                                                </div>
                                            ) : (
                                                (progressionMode === 'assessment' && isChecked && ((result?.score ?? 0) < (result?.total ?? question?.marks ?? 6))) && (
                                                    <button
                                                        type="button"
                                                        data-testid="btn-open-triage-modal"
                                                        onClick={() => setShowTriageModal(true)}
                                                        className="inline-flex items-center gap-1 px-2.5 py-1 rounded-lg bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs shadow-2xs transition cursor-pointer"
                                                        title="Launch 5-min cognitive triage and repair for missed marks"
                                                    >
                                                        <Sparkles className="w-3.5 h-3.5" />
                                                        <span>5-Min Triage &amp; Repair</span>
                                                    </button>
                                                )
                                            )}

                                            {(question?.solution ||
                                              question?.worked_solution ||
                                              question?.memo ||
                                              question?.model_answer ||
                                              question?.canonical_solution ||
                                              question?.explanation ||
                                              question?.ideal_answer ||
                                              question?.correct_answer ||
                                              (Array.isArray(question?.steps) && question.steps.length > 0) ||
                                              (Array.isArray(question?.guidelines) && question.guidelines.length > 0)) && (
                                                <button
                                                    type="button"
                                                    data-testid="btn-view-full-memo"
                                                    onClick={() => setShowFullMemo((prev) => !prev)}
                                                    className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-lg text-xs font-bold transition cursor-pointer ${
                                                        showFullMemo
                                                            ? 'bg-blue-600 text-white shadow-2xs'
                                                            : 'bg-white text-[#13519C] border border-[#13519C]/40 hover:bg-blue-50'
                                                    }`}
                                                >
                                                    <span>{showFullMemo ? 'Hide Solution Memo' : '📖 View Memorandum'}</span>
                                                </button>
                                            )}
                                        </div>
                                    </div>
                                )}

                                {/* Full Memorandum Panel */}
                                {showFullMemo && (
                                    <div data-testid="panel-full-memo" className="p-4 rounded-xl border border-blue-200 bg-blue-50/70 space-y-2 text-xs text-slate-800 font-sans shadow-2xs animate-in fade-in">
                                        <div className="flex items-center justify-between pb-1.5 border-b border-blue-200">
                                            <span className="font-bold text-[#13519C] uppercase tracking-wider flex items-center gap-1.5">
                                                📖 Official Marking Memorandum &amp; Worked Solution
                                            </span>
                                            <button
                                                type="button"
                                                onClick={() => setShowFullMemo(false)}
                                                className="text-slate-400 hover:text-slate-600 font-bold cursor-pointer"
                                            >
                                                ✕
                                            </button>
                                        </div>
                                        <div className="leading-relaxed">
                                            {renderFormattedPrompt(extractMemorandumContent(question))}
                                        </div>
                                    </div>
                                )}

                                {/* Interactive Action Footer */}
                                <div className="border-t border-slate-100 pt-3 flex flex-wrap items-center justify-between gap-3">
                                    <div>
                                        {onCompare && isChecked && (
                                            <button
                                                type="button"
                                                onClick={handleCompareToggle}
                                                className={`flex items-center gap-2 px-3.5 py-2 rounded-xl text-xs font-semibold transition cursor-pointer ${
                                                    isComparing
                                                        ? 'bg-amber-600 text-white'
                                                        : 'bg-white text-[#13519C] border border-[#13519C]/30 hover:bg-blue-50'
                                                }`}
                                            >
                                                <ArrowLeftRight className="w-3.5 h-3.5" />
                                                <span>{isComparing ? 'Hide Memo' : 'Compare Memo'}</span>
                                            </button>
                                        )}
                                    </div>

                                    {onNext && (
                                        <button
                                            type="button"
                                            data-testid="btn-next-question"
                                            onClick={() => {
                                                 setIsChecked(false);
                                                 setIsComparing(false);
                                                 setShowHints(false);
                                                 setShowFullMemo(false);
                                                 if (isDiagnosticRequired && diagnosticIndex < 3) {
                                                     setDiagnosticIndex((prev) => prev + 1);
                                                 }
                                                 onNext();
                                            }}
                                            className="ml-auto flex items-center gap-2 px-5 py-2 rounded-xl text-xs font-bold bg-[#FF9100] text-white hover:bg-amber-600 transition shadow-xs cursor-pointer active:scale-98"
                                        >
                                            <span>
                                                {isDiagnosticRequired && diagnosticIndex < 3
                                                    ? `Next Diagnostic Item (${diagnosticIndex + 1} of 3)`
                                                    : 'Next Problem'}
                                            </span>
                                            <ArrowRight className="w-3.5 h-3.5" />
                                        </button>
                                    )}
                                </div>
                            </div>
                        )}
                    </div>
                </div>

            {/* Super Admin Reset Modal */}
            <React.Suspense fallback={null}>
                {showAdminResetModal && (
                    <SuperAdminProgressResetModal
                        isOpen={showAdminResetModal}
                        onClose={() => setShowAdminResetModal(false)}
                        activeSubject={normalizedSubId}
                    />
                )}
            </React.Suspense>

            {/* Interactive CAPS Topic & Exam Scope Modal */}
            <TopicScopeModal
                isOpen={showTopicModal}
                onClose={() => setShowTopicModal(false)}
                subject={subjectTitle}
                grade={grade}
                currentTopic={topic}
                onSelectTopic={(newTopic) => {
                    if (onSelectTopic) {
                        onSelectTopic(newTopic);
                    }
                }}
            />

            {/* SimuLearn Step Replay Modal */}
            <React.Suspense fallback={null}>
                {showSimuLearn && (
                    <SimuLearnPlayer
                        isOpen={showSimuLearn}
                        archetypeKey={getSimuLearnKey()}
                        onClose={() => setShowSimuLearn(false)}
                        onComplete={() => setShowSimuLearn(false)}
                    />
                )}
            </React.Suspense>

            {/* Post-Exam Triage & 3-Step Cognitive Repair Modal */}
            <React.Suspense fallback={null}>
                {showTriageModal && (
                    <PostExamTriageModal
                        isOpen={showTriageModal}
                        onClose={() => setShowTriageModal(false)}
                        examTitle={`${subjectTitle} • ${topic || 'Assessment'}`}
                        earnedMarks={result?.score ?? 4}
                        totalMarks={result?.total ?? question?.marks ?? 6}
                        missedQuestions={[
                            {
                                id: question?.id || 'q-eval-1',
                                text: promptText || 'Calculations and journal entries',
                                lostMarks: Math.max(1, (result?.total ?? question?.marks ?? 6) - (result?.score ?? 4)),
                                misconceptionTag: question?.misconception_tags?.[0] || question?.misconception_tag || 'net_vs_gross_confusion',
                                topic: topic || 'Core Methodology',
                            }
                        ]}
                        onRemedialComplete={(repairData) => {
                            setRemedialRepaired(true);
                            studentStore.awardXP(repairData?.xpAwarded || 50);
                        }}
                    />
                )}
            </React.Suspense>

        </div>
    );
}
