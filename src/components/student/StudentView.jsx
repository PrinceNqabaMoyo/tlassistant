import React, { useCallback, useEffect } from 'react';
import { Workspace } from '../workspace';
import { CurriculumHelper } from '../curriculum';
import { CurriculumSelector } from '../forms/StudentForms';
import { GradeSelector } from '../forms/StudentForms';
import { SubjectDashboard } from '../forms/StudentForms';
import { StudyModeSelector } from '../forms/StudentForms';
import ClassworkView from './ClassworkView';
import { Loader2 } from 'lucide-react';
import { CLASS_ASSIGNMENTS_BLOCKED_MESSAGE } from '../../app/constants/access';

const StudentView = ({
    view, setView, allCurricula, getAgentResponse, navigationStack, setNavigationStack, updateHelperNavigationLabel,
    isCurriculumPageVisible, setIsCurriculumPageVisible, loading, setLoading,
    currentProblemThreadId,
    ...props
}) => {
    const isLockedStudent = (
        props.currentUser?.role === 'student' &&
        !props.currentUser?.isSuperAdmin &&
        props.currentUser?.curriculum &&
        props.currentUser?.grade
    );

    const handleNavigate = useCallback((newView, newLabel, itemData = null) => {
        setNavigationStack(prevStack => {
            let updatedStack = [...prevStack];
            if (prevStack[prevStack.length - 1]?.view === 'curriculum' && newView === 'grade') {
                updatedStack.push({ view: newView, label: newLabel, data: itemData });
                return updatedStack;
            }
            const existingIndex = updatedStack.findIndex(item => {
                if (item.view === newView) {
                    if (newView === 'curriculum') return !item.data;
                    if (newView === 'grade') return item.data?.curriculumKey === itemData?.curriculumKey;
                    if (newView === 'subject') return item.data?.curriculumKey === itemData?.curriculumKey && item.data?.grade === itemData?.grade;
                    if (newView === 'study_mode') return item.data?.curriculumKey === itemData?.curriculumKey && item.data?.grade === itemData?.grade && item.data?.subject?.id === itemData?.subject?.id;
                    if (newView === 'workspace') return item.data?.curriculumKey === itemData?.curriculumKey && item.data?.grade === itemData?.grade && item.data?.subject?.id === itemData?.subject?.id && item.data?.topic?.name === itemData?.topic?.name;
                    if (newView === 'classwork') return true;
                    if (newView === 'curriculum_helper') return item.label === newLabel;
                    return true;
                }
                return false;
            });
            if (existingIndex !== -1) {
                updatedStack = updatedStack.slice(0, existingIndex + 1);
                updatedStack[existingIndex] = { view: newView, label: newLabel, data: itemData };
            } else {
                updatedStack.push({ view: newView, label: newLabel, data: itemData });
            }
            return updatedStack;
        });
        setView(newView);
    }, [setNavigationStack, setView, allCurricula]);

    const handleSelectCurriculum = useCallback((key) => {
        props.setSelectedCurriculumKey(key);
        handleNavigate('grade', `${allCurricula[key].name} Grades`, { curriculumKey: key, grade: null });
    }, [props, allCurricula, handleNavigate]);

    const handleSelectGrade = useCallback((grade) => {
        props.setSelectedGrade(grade);
        handleNavigate('subject', 'Subject', { value: grade, curriculumKey: props.selectedCurriculumKey, grade: grade });
    }, [props, handleNavigate]);

    const handleSelectSubject = useCallback((subject) => {
        props.setSelectedSubject(subject);
        handleNavigate('curriculum_helper', 'Curriculum Helper', { value: 'Curriculum Helper', curriculumKey: props.selectedCurriculumKey, grade: props.selectedGrade, subject: subject });
    }, [props, handleNavigate]);

    const handleSelectStudyMode = useCallback((mode) => {
        if (mode === 'curriculum_helper') {
            handleNavigate('curriculum_helper', 'Curriculum Helper', { value: 'Curriculum Helper', curriculumKey: props.selectedCurriculumKey, grade: props.selectedGrade, subject: props.selectedSubject });
        } else if (mode === 'classwork') {
            props.setMessage?.(CLASS_ASSIGNMENTS_BLOCKED_MESSAGE);
        }
    }, [props, handleNavigate]);

    let currentSelectedCurriculumKey = props.selectedCurriculumKey;
    if (view === 'grade' && !currentSelectedCurriculumKey && navigationStack.length > 0) {
        const currentNavEntry = navigationStack[navigationStack.length - 1];
        if (currentNavEntry.view === 'grade' && currentNavEntry.data && currentNavEntry.data.key) currentSelectedCurriculumKey = currentNavEntry.data.key;
        else if (currentNavEntry.view === 'curriculum' && currentNavEntry.data && currentNavEntry.data.key) currentSelectedCurriculumKey = currentNavEntry.data.key;
    }
    const selectedCurriculum = currentSelectedCurriculumKey ? allCurricula[currentSelectedCurriculumKey] : null;

    const curriculumHelperProps = {
        onClose: () => {
            setIsCurriculumPageVisible(false);
            setNavigationStack(prevStack => {
                const filteredStack = prevStack.filter(item => item.view !== 'curriculum_helper');
                // Use setTimeout to avoid setState during render
                setTimeout(() => {
                    if (filteredStack.length > 0) {
                        setView(filteredStack[filteredStack.length - 1].view);
                    } else if (isLockedStudent) {
                        setView('subject');
                    } else {
                        setView('curriculum');
                    }
                }, 0);
                return filteredStack;
            });
        },
        selectedGrade: props.selectedGrade,
        selectedSubject: props.selectedSubject,
        setWorkspaceMode: props.setWorkspaceMode,
        setActiveTopic: props.setActiveTopic,
        updateHelperNavigationLabel: updateHelperNavigationLabel,
        setView: setView,
        setNavigationStack: setNavigationStack,
        navigationStack: navigationStack,
        onGoToClasswork: () => {
            props.setMessage?.(CLASS_ASSIGNMENTS_BLOCKED_MESSAGE);
        },
        currentUser: props.currentUser,
        db: props.db,
        storage: props.storage,
        onManageSubscriptionPage: props.onManageSubscriptionPage,
    };

    // Move useEffect hooks outside the switch statement to avoid conditional hook calls
    useEffect(() => {
        if (isLockedStudent) {
            props.setSelectedCurriculumKey(props.currentUser.curriculum);
            props.setSelectedGrade(Number(props.currentUser.grade));
        }
    }, [isLockedStudent, props.currentUser?.curriculum, props.currentUser?.grade, props.currentUser?.role]);

    switch (view) {
        case 'dashboard':
        case 'curriculum':
            // For students, use their stored curriculum and grade preferences
            if (isLockedStudent) {
                // Navigate directly to subject selection
                return <SubjectDashboard
                    curriculum={allCurricula[props.currentUser.curriculum]}
                    curriculumKey={props.currentUser.curriculum}
                    grade={Number(props.currentUser.grade)}
                    onSelect={handleSelectSubject}
                    db={props.db}
                    currentUser={props.currentUser}
                    onContinueProblem={props.handleContinueProblem}
                    onMarkSolved={props.handleMarkStrugglingProblemSolved}
                    setMessage={props.setMessage}
                    onManageSubscriptionPage={props.onManageSubscriptionPage}
                />;
            }
            return <CurriculumSelector curricula={allCurricula} onSelect={handleSelectCurriculum} loadingStates={props.loadingStates || {}} userSubscription={props.userSubscription} />;
        case 'grade':
            if (isLockedStudent) {
                return <SubjectDashboard
                    curriculum={allCurricula[props.currentUser.curriculum]}
                    curriculumKey={props.currentUser.curriculum}
                    grade={Number(props.currentUser.grade)}
                    onSelect={handleSelectSubject}
                    db={props.db}
                    currentUser={props.currentUser}
                    onContinueProblem={props.handleContinueProblem}
                    onMarkSolved={props.handleMarkStrugglingProblemSolved}
                    setMessage={props.setMessage}
                    onManageSubscriptionPage={props.onManageSubscriptionPage}
                />;
            }
            if (!selectedCurriculum) {
                return (
                    <div className="flex items-center justify-center p-16">
                        <Loader2 className="h-12 w-12 animate-spin text-blue-600" />
                        <p className="ml-4 text-gray-600">Loading Grades...</p>
                    </div>
                );
            }
            return <GradeSelector curriculum={selectedCurriculum} onSelect={handleSelectGrade} />;
        case 'subject':
            if (!selectedCurriculum || !props.selectedGrade) {
                return (
                    <div className="flex items-center justify-center p-16">
                        <Loader2 className="h-12 w-12 animate-spin text-blue-600" />
                        <p className="ml-4 text-gray-600">Loading Subjects...</p>
                    </div>
                );
            }
            return <SubjectDashboard
                curriculum={selectedCurriculum}
                curriculumKey={currentSelectedCurriculumKey}
                grade={props.selectedGrade}
                onSelect={handleSelectSubject}
                db={props.db}
                currentUser={props.currentUser}
                onContinueProblem={props.handleContinueProblem}
                onMarkSolved={props.handleMarkStrugglingProblemSolved}
                setMessage={props.setMessage}
                onManageSubscriptionPage={props.onManageSubscriptionPage}
            />;
        case 'study_mode':
            return <StudyModeSelector subject={props.selectedSubject} grade={props.selectedGrade} onSelect={handleSelectStudyMode} />;
        case 'curriculum_helper':
            return <CurriculumHelper {...curriculumHelperProps} />;
        case 'workspace':
            if (!props.selectedSubject || !props.selectedGrade) {
                return (
                    <div className="flex items-center justify-center p-16">
                        <Loader2 className="h-12 w-12 animate-spin text-blue-600" />
                        <p className="ml-4 text-gray-600">Loading Workspace...</p>
                    </div>
                );
            }
            return <Workspace
                topic={props.activeTopic}
                getAgentResponse={getAgentResponse}
                loading={loading}
                setLoading={setLoading}
                selectedSubject={props.selectedSubject}
                selectedGrade={props.selectedGrade}
                currentProblemThreadId={currentProblemThreadId}
                practiceQuestions={props.practiceQuestions}
                workspaceMode={props.workspaceMode}
                setWorkspaceMode={props.setWorkspaceMode}
                freeformWorkAreaRef={props.freeformWorkAreaRef}
                currentUser={props.currentUser}
                handleAnswerInput={props.handleAnswerInput}
                handleSubmit={props.handleSubmit}
                setView={setView}
                activeAssignment={props.activeAssignment}
                handleAssignmentSubmit={props.handleAssignmentSubmit}
                addQuestionToChat={props.addQuestionToChat}
                updateAnswerInChat={props.updateAnswerInChat}
                handleSendFreeformQuery={props.handleSendFreeformQuery}
                freeformAnswer={props.freeformAnswer}
                setFreeformAnswer={props.setFreeformAnswer}
                setSelectedFreeformTopic={props.setSelectedFreeformTopic}
            />;
        case 'classwork':
            return <ClassworkView db={props.db} currentUser={props.currentUser} onStartAssignment={props.handleStartAssignment} />;
        default:
            // For students, use their stored curriculum and grade preferences
            if (isLockedStudent) {
                // Navigate directly to subject selection
                return <SubjectDashboard
                    curriculum={allCurricula[props.currentUser.curriculum]}
                    curriculumKey={props.currentUser.curriculum}
                    grade={Number(props.currentUser.grade)}
                    onSelect={handleSelectSubject}
                    db={props.db}
                    currentUser={props.currentUser}
                    onContinueProblem={props.handleContinueProblem}
                    onMarkSolved={props.handleMarkStrugglingProblemSolved}
                    setMessage={props.setMessage}
                    onManageSubscriptionPage={props.onManageSubscriptionPage}
                />;
            }
            return <CurriculumSelector curricula={allCurricula} onSelect={handleSelectCurriculum} loadingStates={props.loadingStates || {}} userSubscription={props.userSubscription} />;
    }
};

export default StudentView;
