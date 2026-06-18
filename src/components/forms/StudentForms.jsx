import React, { useState, useEffect, useRef } from 'react';
import { GraduationCap, BookOpen, AlertCircle, Briefcase, BookCopy } from 'lucide-react';
import { collection, query, where, getDocs } from 'firebase/firestore';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { canAccessSavedProblems, canBypassComingSoon, CLASS_ASSIGNMENTS_BLOCKED_MESSAGE, COMING_SOON_SUBJECT_MESSAGE, isLiveLaunchSubject, SAVED_PROBLEMS_PRO_MESSAGE } from '../../app/constants/access';

// Student Role Selection Component
export const StudentRoleSelector = ({ onSelect }) => (
    <div className="p-8 text-center">
        <h1 className="text-4xl font-bold text-gray-800 mb-4">Student Dashboard</h1>
        <p className="text-xl text-gray-600 mb-12">Choose your learning path:</p>
        <div className="grid grid-cols-1 gap-8 max-w-md mx-auto">
            <button onClick={() => onSelect('curriculum')} className="bg-white rounded-xl shadow-lg p-8 hover:shadow-2xl hover:-translate-y-2 transition-all duration-300">
                <BookOpen className="h-16 w-16 mx-auto mb-4 text-green-600" />
                <h2 className="text-2xl font-bold text-gray-800">Curriculum Helper</h2>
                <p className="text-gray-600 mt-2">Structured learning with guided practice</p>
            </button>
        </div>
    </div>
);

// Curriculum Selection Component
export const CurriculumSelector = ({ curricula, onSelect, loadingStates, userSubscription }) => {
    const accessibleCurricula = userSubscription?.accessibleCurricula || Object.keys(curricula || {});

    return (
    <div className="p-4 sm:p-6 lg:p-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Select Curriculum</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {Object.keys(curricula).map(key => (
                <SelectionCard
                    key={key}
                    title={curricula[key].name}
                    description={curricula[key].description}
                    icon={GraduationCap}
                    onSelect={() => onSelect(key)}
                    disabled={!accessibleCurricula.includes(key)}
                    isLoading={loadingStates[key]}
                />
            ))}
        </div>
    </div>
    );
};

// Grade Selection Component
export const GradeSelector = ({ curriculum, onSelect }) => (
    <div className="p-4 sm:p-6 lg:p-8">
        <h2 className="text-3xl font-bold text-gray-900 mb-2">Select {curriculum.name} Grade</h2>
        <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            {curriculum.grades.map(grade => (
                <button key={grade} onClick={() => onSelect(grade)} className="p-6 bg-white rounded-lg shadow-md hover:shadow-xl hover:bg-blue-500 hover:text-white transition-all duration-300 font-bold text-xl text-gray-700">
                    Grade {grade}
                </button>
            ))}
        </div>
    </div>
);

// Subject Dashboard Component
export const SubjectDashboard = ({ curriculum, curriculumKey, grade, onSelect, db, currentUser, onContinueProblem, setMessage, onManageSubscriptionPage }) => {
    const availableSubjects = curriculum.subjects.filter(s => s.availableGrades.includes(grade));
    const [savedProblems, setSavedProblems] = useState({});
    const [loading, setLoading] = useState(true);
    const [showSubscriptionPrompt, setShowSubscriptionPrompt] = useState(false);
    // Guarantee setMessage is always a function
    const safeSetMessage = typeof setMessage === 'function' ? setMessage : () => {};
    const hasSavedProblemsAccess = canAccessSavedProblems(currentUser);

    const hasActiveSubscription = () => {
        if (!currentUser || currentUser.isOwner || currentUser.isSuperAdmin) {
            return true;
        }

        if (currentUser.subscriptionExpired) {
            return false;
        }

        const subscribedGrades = currentUser.subscribedGrades || [];
        return subscribedGrades.length > 0;
    };

    const handleManageSubscription = () => {
        setShowSubscriptionPrompt(false);
        onManageSubscriptionPage?.();
    };

    const handleSubjectClick = (subject) => {
        if (isDragging) {
            return;
        }

        if (!hasActiveSubscription()) {
            setShowSubscriptionPrompt(true);
            return;
        }

        if (!isLiveLaunchSubject({ curriculumKey, grade, subject }) && !canBypassComingSoon(currentUser)) {
            safeSetMessage(COMING_SOON_SUBJECT_MESSAGE);
            return;
        }

        onSelect(subject);
    };

    // Mouse drag functionality for horizontal scrolling
    const [isDragging, setIsDragging] = useState(false);
    const [startX, setStartX] = useState(0);
    const [scrollLeft, setScrollLeft] = useState(0);
    
    // Refs for scroll containers
    const subjectsContainerRef = useRef(null);
    const savedProblemsContainerRef = useRef(null);
    const assignmentsContainerRef = useRef(null);

    const handleMouseDown = (e, containerRef) => {
        setIsDragging(true);
        setStartX(e.pageX - containerRef.current.offsetLeft);
        setScrollLeft(containerRef.current.scrollLeft);
        containerRef.current.style.cursor = 'grabbing';
        containerRef.current.style.userSelect = 'none';
    };

    const handleMouseMove = (e, containerRef) => {
        if (!isDragging) return;
        e.preventDefault();
        const x = e.pageX - containerRef.current.offsetLeft;
        const walk = (x - startX) * 2; // Scroll speed multiplier
        containerRef.current.scrollLeft = scrollLeft - walk;
    };

    const handleMouseUp = (containerRef) => {
        setIsDragging(false);
        containerRef.current.style.cursor = 'grab';
        containerRef.current.style.userSelect = 'auto';
    };

    const handleMouseLeave = (containerRef) => {
        if (isDragging) {
            setIsDragging(false);
            containerRef.current.style.cursor = 'grab';
            containerRef.current.style.userSelect = 'auto';
        }
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                if (hasSavedProblemsAccess) {
                    const problemsData = {};
                    for (const subject of availableSubjects) {
                        const problemsRef = collection(db, 'users', currentUser.uid, 'savedProblems');
                        const q = query(problemsRef, where('subject', '==', subject.name));
                        const snapshot = await getDocs(q);
                        problemsData[subject.name] = snapshot.docs.map(doc => ({
                            id: doc.id,
                            ...doc.data()
                        }));
                    }
                    setSavedProblems(problemsData);
                } else {
                    setSavedProblems({});
                }
            } catch (error) {
                console.error('Error fetching dashboard data:', error);
                safeSetMessage('Error loading dashboard data');
            } finally {
                setLoading(false);
            }
        };

        if (currentUser) {
            fetchData();
        }
    }, [currentUser, availableSubjects, db, hasSavedProblemsAccess, safeSetMessage]);

    if (loading) {
        return (
            <div className="flex items-center justify-center h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gray-50">
            {/* Subscription Status Section */}
            <section className="px-6 pt-6">
                <SubscriptionStatus 
                    currentUser={currentUser}
                    onSubscriptionChange={(subscription) => {
                        // Here you would update the user's subscription in the database
                        console.log('Subscription changed to:', subscription);
                    }}
                    onManageSubscription={handleManageSubscription}
                />
            </section>

            {/* Subjects Section */}
            <section className="mb-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-4 px-6">Subjects</h2>
                <div className="relative">
                    <div 
                        ref={subjectsContainerRef}
                        className="flex overflow-x-auto scrollbar-hide px-6 space-x-4 pb-4 cursor-grab active:cursor-grabbing"
                        onMouseDown={(e) => handleMouseDown(e, subjectsContainerRef)}
                        onMouseMove={(e) => handleMouseMove(e, subjectsContainerRef)}
                        onMouseUp={() => handleMouseUp(subjectsContainerRef)}
                        onMouseLeave={() => handleMouseLeave(subjectsContainerRef)}
                    >
                        {availableSubjects.map(subject => {
                            const SubjectIcon = subject.icon;
                            const isLiveSubject = isLiveLaunchSubject({ curriculumKey, grade, subject });
                            const showComingSoonBadge = !isLiveSubject && !canBypassComingSoon(currentUser);
                            return (
                                <div 
                                    key={subject.id} 
                                    onClick={() => handleSubjectClick(subject)}
                                    className="flex-shrink-0 w-64 bg-white rounded-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 cursor-pointer overflow-hidden group"
                                >
                                    <div className={`h-32 ${subject.color} flex items-center justify-center`}>
                                        <SubjectIcon className="h-16 w-16 text-white/90 transition-transform duration-300 group-hover:scale-110" />
                                    </div>
                                    <div className="p-4">
                                        <div className="mb-2 flex items-center justify-between gap-2">
                                            <h3 className="text-lg font-bold text-gray-800">{subject.name}</h3>
                                            {showComingSoonBadge && (
                                                <span className="rounded-full bg-amber-100 px-2 py-1 text-[10px] font-semibold uppercase tracking-[0.2em] text-amber-700">
                                                    Coming soon
                                                </span>
                                            )}
                                        </div>
                                        <p className="text-gray-600 text-sm">{subject.description}</p>
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            </section>

            {/* My Saved Problems Section */}
            <section className="mb-8">
                <div className="mb-4 px-6">
                    <div className="flex items-center gap-3">
                        <h2 className="text-2xl font-bold text-gray-900">My Saved Problems</h2>
                        {!hasSavedProblemsAccess && (
                            <button
                                type="button"
                                onClick={onManageSubscriptionPage}
                                className="rounded-full bg-violet-100 px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-violet-700"
                            >
                                Pro package only
                            </button>
                        )}
                    </div>
                </div>
                {hasSavedProblemsAccess ? (
                    <div className="relative">
                        <div 
                            ref={savedProblemsContainerRef}
                            className="flex overflow-x-auto scrollbar-hide px-6 space-x-4 pb-4 cursor-grab active:cursor-grabbing"
                            onMouseDown={(e) => handleMouseDown(e, savedProblemsContainerRef)}
                            onMouseMove={(e) => handleMouseMove(e, savedProblemsContainerRef)}
                            onMouseUp={() => handleMouseUp(savedProblemsContainerRef)}
                            onMouseLeave={() => handleMouseLeave(savedProblemsContainerRef)}
                        >
                            {availableSubjects.map(subject => {
                                const subjectProblems = savedProblems[subject.name] || [];
                                if (subjectProblems.length === 0) return null;
                                
                                return (
                                    <div key={subject.name} className="flex-shrink-0 w-80 bg-white rounded-lg shadow-lg">
                                        <div className="p-4">
                                            <h3 className="text-lg font-bold text-gray-800 mb-3">{subject.name} Problems</h3>
                                            <div className="space-y-2">
                                                {subjectProblems.slice(0, 3).map(problem => (
                                                    <div key={problem.id} className="flex items-center justify-between p-2 bg-gray-50 rounded">
                                                        <span className="text-sm text-gray-700 truncate">{problem.question}</span>
                                                        <button 
                                                            onClick={() => onContinueProblem(problem)}
                                                            className="text-blue-600 hover:text-blue-800 text-xs font-medium"
                                                        >
                                                            Continue
                                                        </button>
                                                    </div>
                                                ))}
                                                {subjectProblems.length > 3 && (
                                                    <div className="text-center pt-2">
                                                        <span className="text-sm text-gray-500">+{subjectProblems.length - 3} more</span>
                                                    </div>
                                                )}
                                            </div>
                                        </div>
                                    </div>
                                );
                            })}
                        </div>
                    </div>
                ) : (
                    <div className="px-6">
                        <FeatureGatePanel
                            title="My Saved Problems"
                            description={SAVED_PROBLEMS_PRO_MESSAGE}
                            badge="Pro package only"
                            buttonLabel="View subscription options"
                            onButtonClick={onManageSubscriptionPage}
                        />
                    </div>
                )}
            </section>

            {/* Class Assignments Section */}
            <section className="mb-8">
                <h2 className="text-2xl font-bold text-gray-900 mb-4 px-6">Class Assignments</h2>
                <div className="px-6">
                    <FeatureGatePanel
                        title="Class assignments"
                        description={CLASS_ASSIGNMENTS_BLOCKED_MESSAGE}
                        badge="Unavailable"
                    />
                </div>
            </section>

            {showSubscriptionPrompt && (
                <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 p-4 backdrop-blur-sm">
                    <div className="w-full max-w-md rounded-2xl bg-white p-6 shadow-2xl">
                        <div className="flex items-start gap-3">
                            <div className="rounded-full bg-amber-100 p-2 text-amber-700">
                                <AlertCircle className="h-5 w-5" />
                            </div>
                            <div>
                                <h3 className="text-lg font-semibold text-slate-900">Please subscribe to gain access</h3>
                                <p className="mt-2 text-sm text-slate-600">
                                    Upload your EFT proof of payment to request access.
                                </p>
                            </div>
                        </div>
                        <div className="mt-6 flex justify-end gap-3">
                            <button
                                onClick={() => setShowSubscriptionPrompt(false)}
                                className="rounded-lg border border-slate-200 px-4 py-2 text-sm font-medium text-slate-600 transition hover:bg-slate-50"
                            >
                                Not now
                            </button>
                            <button
                                onClick={handleManageSubscription}
                                className="rounded-lg bg-[#13519C] px-4 py-2 text-sm font-semibold text-white transition hover:bg-[#0f3e77]"
                            >
                                Manage Subscription
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};

// Study Mode Selector Component
export const StudyModeSelector = ({ subject, grade, onSelect }) => (
    <div className="p-8">
        <div className="text-center">
            <h2 className="text-3xl font-extrabold text-gray-800 mb-2">
                {subject.name} - Grade {grade}
            </h2>
            <p className="text-lg text-gray-600 mb-8">How would you like to proceed?</p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-4xl mx-auto">
                <div className="bg-white p-6 rounded-xl shadow-lg border border-gray-200">
                    <div className="text-center mb-2">
                        <h3 className="text-xl font-semibold text-gray-800">Personal Study</h3>
                    </div>
                    <p className="text-gray-600 mb-6">Practice at your own pace, with help from Fundile.</p>
                    <div className="flex flex-col space-y-4">
                        <button 
                            onClick={() => onSelect('curriculum_helper')}
                            className="w-full py-3 px-4 rounded-lg bg-purple-600 text-white font-medium shadow-md hover:bg-purple-700 transition-colors duration-200 flex items-center justify-center space-x-2"
                            title="Start with topics and choose Scaffold or Practice"
                        >
                            <BookCopy size={20} />
                            <span>Topic Launchpad (Scaffold / Practice)</span>
                        </button>
                    </div>
                </div>
                <SelectionCard
                    title="Class Work"
                    description="View and complete assignments set by your teacher."
                    icon={Briefcase}
                    onSelect={() => onSelect('classwork')}
                />
            </div>
        </div>
    </div>
);

// Subscription Status Component
export const SubscriptionStatus = ({ currentUser, onManageSubscription }) => {
    const getSubscriptionStatus = () => {
        if (currentUser?.isOwner || currentUser?.isSuperAdmin) {
            return {
                status: 'active',
                color: 'text-green-600',
                bgColor: 'bg-green-50',
                borderColor: 'border-green-200',
                label: 'Owner access active'
            };
        }

        const subscribedGrades = currentUser?.subscribedGrades || [];
        const expiryValue = currentUser?.subscriptionExpiry;
        const expiryDate = expiryValue?.toDate ? expiryValue.toDate() : (expiryValue ? new Date(expiryValue) : null);

        if (currentUser?.subscriptionExpired || subscribedGrades.length === 0) {
            return {
                status: 'none',
                color: 'text-red-600',
                bgColor: 'bg-red-50',
                borderColor: 'border-red-200',
                label: 'No active subscription'
            };
        }

        const expiryLabel = expiryDate && !Number.isNaN(expiryDate.getTime())
            ? `Active until ${expiryDate.toLocaleDateString()}`
            : 'Subscription active';

        return {
            status: 'active',
            color: 'text-green-600',
            bgColor: 'bg-green-50',
            borderColor: 'border-green-200',
            label: expiryLabel
        };
    };

    const status = getSubscriptionStatus();

    return (
        <div className={`${status.bgColor} ${status.borderColor} border rounded-lg p-4 mb-6`}>
            <div className="flex items-center justify-between">
                <div className="flex items-center space-x-3">
                    <div className={`w-3 h-3 rounded-full ${status.color.replace('text-', 'bg-')}`}></div>
                    <div>
                        <h3 className="font-semibold text-gray-900">Subscription Status</h3>
                        <p className={`text-sm ${status.color}`}>
                            {status.label}
                        </p>
                    </div>
                </div>
                <button
                    onClick={onManageSubscription}
                    className="text-sm text-blue-600 hover:text-blue-800 font-medium"
                >
                    Manage Subscription
                </button>
            </div>
        </div>
    );
};

// Selection Card Component
const SelectionCard = ({ title, description, icon: Icon, onSelect, disabled = false, isLoading = false }) => (
    <button
        onClick={onSelect}
        disabled={disabled || isLoading}
        className={`relative p-6 bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 ${
            disabled ? 'opacity-50 cursor-not-allowed' : 'hover:-translate-y-1 cursor-pointer'
        }`}
    >
        {isLoading && (
            <div className="absolute inset-0 bg-white/80 rounded-xl flex items-center justify-center">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
            </div>
        )}
        <div className="text-center">
            <Icon className="h-12 w-12 mx-auto mb-4 text-blue-600" />
            <h3 className="text-xl font-bold text-gray-800 mb-2">{title}</h3>
            <p className="text-gray-600">{description}</p>
        </div>
    </button>
);
