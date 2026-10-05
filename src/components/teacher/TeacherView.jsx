import React from 'react';
import { ChevronLeft } from 'lucide-react';
import AssessmentGenerator from './AssessmentGenerator';
import SubmissionsDashboard from './SubmissionsDashboard';
import ClassManager from './ClassManager';
import HomeworkManager from './HomeworkManager';
import AssessmentManager from './AssessmentManager';
import ClassDiagnosticHeatmap from './ClassDiagnosticHeatmap';
import TeacherDashboard from './TeacherDashboard';
import { StudentManagement, QuestionGeneration } from '../forms/TeacherForms';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { CLASS_ASSIGNMENTS_BLOCKED_MESSAGE } from '../../app/constants/access';

const TeacherView = ({ view, setView, db, currentUser }) => {
    const canAccessTeacherMode = !!(currentUser?.isOwner || currentUser?.isSuperAdmin || currentUser?.role === 'teacher' || currentUser?.isTeacher);

    if (!canAccessTeacherMode) {
        return (
            <div className="p-4 sm:p-6 lg:p-8">
                <FeatureGatePanel
                    title="Teacher Mode"
                    description={CLASS_ASSIGNMENTS_BLOCKED_MESSAGE}
                    badge="Coming soon"
                />
            </div>
        );
    }

    const handleDashboardSelect = (target) => {
        switch (target) {
            case 'studentManagement':
                setView('studentManagement');
                break;
            case 'questionGeneration':
                setView('questionGeneration');
                break;
            case 'assignmentManagement':
                setView('assessment_generator');
                break;
            case 'analytics':
                setView('submissions');
                break;
            case 'classManagement':
                setView('classManagement');
                break;
            case 'homework':
                setView('homework');
                break;
            case 'assessments':
                setView('assessments');
                break;
            case 'classDiagnostics':
                setView('classDiagnostics');
                break;
            case 'submissions':
                setView('submissions');
                break;
            case 'curriculumManagement':
            case 'reports':
            default:
                setView('dashboard');
                break;
        }
    };

    const renderTeacherContent = () => { 
        switch(view) { 
            case 'lesson_planner': 
                return (
                    <div className="p-4 sm:p-6 lg:p-8 max-w-4xl mx-auto space-y-4">
                        <button
                            onClick={() => setView('dashboard')}
                            className="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-600 hover:text-[#13519C] transition-colors cursor-pointer"
                        >
                            <ChevronLeft className="w-4 h-4" /> Back to Teacher Dashboard
                        </button>
                        <div className="bg-white rounded-2xl border border-slate-200/90 p-8 shadow-xs text-center space-y-3">
                            <h2 style={{ fontFamily: "'Afacad', sans-serif" }} className="text-2xl font-bold text-slate-900">
                                CAPS Lesson Planner &amp; ATP Schedules
                            </h2>
                            <p className="text-sm text-slate-500 max-w-lg mx-auto">
                                Generate and synchronize term-by-term lesson plans, curriculum pacing guides, and homework sequences directly aligned with the official South African CAPS Annual Teaching Plans.
                            </p>
                            <div className="pt-4 flex justify-center gap-3">
                                <button
                                    onClick={() => setView('assessments')}
                                    className="px-4 py-2.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold transition shadow-xs cursor-pointer"
                                >
                                    Open Assessment Generator
                                </button>
                                <button
                                    onClick={() => setView('dashboard')}
                                    className="px-4 py-2.5 rounded-xl border border-slate-200 hover:bg-slate-50 text-slate-700 text-xs font-semibold transition cursor-pointer"
                                >
                                    Return to Cockpit
                                </button>
                            </div>
                        </div>
                    </div>
                ); 
            case 'assessment_generator': 
                return <AssessmentGenerator db={db} currentUser={currentUser} setView={setView} />;
            case 'submissions': 
                return <SubmissionsDashboard db={db} currentUser={currentUser} setView={setView} />; 
            case 'studentManagement':
                return <StudentManagement currentUser={currentUser} db={db} onBack={() => setView('dashboard')} />;
            case 'questionGeneration':
                return <QuestionGeneration currentUser={currentUser} db={db} onBack={() => setView('dashboard')} />;
            case 'classManagement':
                return <ClassManager db={db} currentUser={currentUser} onBack={() => setView('dashboard')} />;
            case 'homework':
                return <HomeworkManager db={db} currentUser={currentUser} onBack={() => setView('dashboard')} />;
            case 'assessments':
                return <AssessmentManager db={db} currentUser={currentUser} onBack={() => setView('dashboard')} />;
            case 'classDiagnostics':
                return (
                    <div className="p-4 sm:p-6 max-w-5xl mx-auto space-y-4">
                        <button
                            onClick={() => setView('dashboard')}
                            className="inline-flex items-center gap-1.5 text-xs font-semibold text-slate-600 hover:text-[#13519C] transition-colors cursor-pointer"
                        >
                            <ChevronLeft className="w-4 h-4" /> Back to Teacher Dashboard
                        </button>
                        <ClassDiagnosticHeatmap
                            onAssignRemedialDrill={(diag) => {
                                console.log('[Teacher LMS] Dispatched remedial drill for:', diag.misconception);
                            }}
                        />
                    </div>
                );
            case 'dashboard': 
            default: 
                return <TeacherDashboard currentUser={currentUser} db={db} onNavigate={handleDashboardSelect} />; 
        } 
    }; 
    
    return <div>{renderTeacherContent()}</div>; 
};

export default TeacherView;
