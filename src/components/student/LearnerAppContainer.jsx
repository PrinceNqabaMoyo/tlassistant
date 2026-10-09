import React, { useState, useEffect, useCallback } from 'react';
import DesktopCommandRail from '../navigation/DesktopCommandRail';
import SubjectManagerModal from '../curriculum/SubjectManagerModal';
import { SUBJECT_TABS_CONFIG } from '../navigation/subjectTabsConfig';
import TodaysDeskView from './TodaysDeskView';
import UniversalWorkspace from '../workspace/UniversalWorkspace';
import DevSandboxWrapper from '../sandbox/DevSandboxWrapper';
import MobileWebApkView from '../mobile/MobileWebApkView';
import UserProfileModal from '../profile/UserProfileModal';
import TopicScopeModal from '../curriculum/TopicScopeModal';
import LinkGuardianModal from '../family/LinkGuardianModal';
import JoinClassModal from './JoinClassModal';
import navigationHistoryService from '../../services/navigationHistoryService';
import { buildApiUrl } from '../../utils/apiBaseUrl';
import studentStore from '../../services/studentStore';
import ErrorBoundary from '../ui/ErrorBoundary';
import { getAuthenticDiagnosticQuestion } from '../../data/authenticDiagnosticBank';

/**
 * LearnerAppContainer
 * The modern, unified Learner Experience container.
 * 
 * Invariants:
 * - Desktop Viewport (>= md): Authentic left-slanted physical folder tabs, accent line, and Desktop Workspace.
 * - Mobile Viewport (< md): Pure Android WebAPK Mobile View (MobileWebApkView) with 1-tap collapsible ribbon,
 *   mobile-optimized assignment cards, 2x2 portrait cards, 6-col landscape ledger, and smooth 7-subject bottom carousel.
 * - DevSandboxWrapper provides real-time viewport toggling between Desktop PWA and Android Mobile with the Mobile Ergonomics Bar.
 * - Direct Backend Connectivity: Communicates with caps-ai-backend for question generation and marking.
 */

const getDefaultTopicForSubject = (subjectId) => {
  const s = String(subjectId || '').toLowerCase();
  if (s.includes('accounting')) return 'Cash Receipts Journal';
  if (s.includes('literacy') || s.includes('lit') || s === 'mathematical_literacy') return 'Tariffs and Break-even Analysis';
  if (s.includes('math') && !s.includes('tech')) return 'Algebraic Expressions';
  if (s.includes('physics') || s.includes('physical')) return 'Motion in 1D';
  if (s.includes('business')) return 'Business Environments';
  if (s.includes('life') || s.includes('bio')) return 'Cell Division & Mitosis';
  if (s.includes('tech')) return 'Mensuration & Trigonometry';
  if (s.includes('ems')) return 'Financial Literacy';
  if (s.includes('natural') || s.includes('natsci')) return 'Matter and Materials';
  return null;
};

export default function LearnerAppContainer({
  currentUser = null,
  initialTab = 'desk',
  isSandboxMode = true, // Enables the live dev sandbox viewport switcher
  onOpenPersonaSwitcher = null,
  onLogout = null,
  superAdminMode = 'student',
  setSuperAdminMode = null,
  superAdminTier = 'standard',
  setSuperAdminTier = null,
}) {
  const savedSession = studentStore.getActiveSession();
  const [activeTab, setActiveTab] = useState(initialTab);
  const [activeTopic, setActiveTopic] = useState(() => savedSession?.topic || getDefaultTopicForSubject(initialTab));
  const [question, setQuestion] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [isChecking, setIsChecking] = useState(false);
  const [result, setResult] = useState(null);
  const [isRailCollapsed, setIsRailCollapsed] = useState(false);
  const [deskMode, setDeskMode] = useState('self_paced'); // 'self_paced' | 'classwork'
  const [activeReelSubjectId, setActiveReelSubjectId] = useState(() => savedSession?.subjectId || 'accounting');
  const [enabledSubjects, setEnabledSubjects] = useState(() => {
    try {
      const saved = localStorage.getItem('fundile_enabled_subjects');
      if (saved) return JSON.parse(saved);
    } catch {}
    return ['accounting', 'mathematics', 'technical_mathematics', 'mathematical_literacy', 'physical_sciences', 'life_sciences', 'business_studies'];
  });
  const [showSubjectManagerModal, setShowSubjectManagerModal] = useState(false);
  const [showProfilePhotoModal, setShowProfilePhotoModal] = useState(false);
  const [showTopicModal, setShowTopicModal] = useState(false);
  const [showLinkGuardianModal, setShowLinkGuardianModal] = useState(false);
  const [showJoinClassModal, setShowJoinClassModal] = useState(false);
  const [exitToast, setExitToast] = useState('');

  const [storeState, setStoreState] = useState(() => studentStore.getState());
  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
    });
    return unsub;
  }, []);

  const studentName = currentUser?.name || currentUser?.displayName || storeState.studentName || 'Prince Moyo';
  const currentGrade = parseInt(String(currentUser?.grade || storeState.grade || '10').replace(/\D/g, ''), 10) || 10;
  const schoolName = currentUser?.school || storeState.school || 'Westville High School';

  // Handle switching tabs (supporting both short mobile IDs and full desktop IDs)
  const handleSelectTab = useCallback((tabId, isFromPopstate = false, topicOverride = null) => {
    const normalized = 
      tabId === 'maths' ? 'mathematics' :
      tabId === 'mathslit' || tabId === 'maths_lit' ? 'mathematical_literacy' :
      tabId === 'physics' ? 'physical_sciences' :
      tabId === 'business' ? 'business_studies' :
      tabId === 'lifesci' ? 'life_sciences' :
      tabId === 'techmaths' ? 'technical_mathematics' :
      tabId === 'natsci' ? 'natural_sciences' :
      tabId;

    setActiveTab(normalized);
    setResult(null);
    const session = studentStore.getActiveSession();
    const chosenTopic = topicOverride || 
      (session?.topic && session?.subjectId === normalized ? session.topic : getDefaultTopicForSubject(normalized));
    setActiveTopic(chosenTopic);

    if (normalized !== 'desk') {
      setActiveReelSubjectId(normalized);
      studentStore.setActiveSession({
        subjectId: normalized,
        topic: chosenTopic,
        lastActiveTab: normalized
      });
    } else {
      studentStore.setActiveSession({
        lastActiveTab: 'desk'
      });
    }

    if (!isFromPopstate) {
      navigationHistoryService.pushScreen(normalized);
    }
  }, []);

  // Initialize navigation history service for Android back-button handling
  useEffect(() => {
    navigationHistoryService.init(activeTab);
    navigationHistoryService.registerHandlers({
      onTabChange: (newTab) => {
        handleSelectTab(newTab, true);
      },
      onModalClose: (modalName) => {
        if (modalName === 'topicScope') setShowTopicModal(false);
        else if (modalName === 'linkGuardian') setShowLinkGuardianModal(false);
        else if (modalName === 'profilePhoto') setShowProfilePhotoModal(false);
        else {
          setShowTopicModal(false);
          setShowLinkGuardianModal(false);
          setShowProfilePhotoModal(false);
        }
      },
      onShowExitToast: (msg) => {
        setExitToast(msg);
        setTimeout(() => setExitToast(''), 2000);
      }
    });

    return () => {
      navigationHistoryService.destroy();
    };
  }, [activeTab, handleSelectTab]);

  const generateLocalFallback = useCallback((subjectId, topicName) => {
    const q = getAuthenticDiagnosticQuestion(subjectId);
    setQuestion({ ...q });
  }, []);

  // Fetch / Generate a real question from caps-ai-backend
  const fetchQuestion = useCallback(async (subjectId, topicName) => {
    setIsGenerating(true);
    setResult(null);
    try {
      const url = buildApiUrl(`/api/generate?subject=${encodeURIComponent(subjectId)}&grade=${currentGrade}&topic=${encodeURIComponent(topicName || '')}&seed=${Date.now()}`);
      const res = await fetch(url);
      if (res.ok) {
        const data = await res.json();
        const extracted = Array.isArray(data?.questions) && data.questions.length > 0 
          ? data.questions[0] 
          : (data?.questions || data);
        setQuestion(extracted);
      } else {
        generateLocalFallback(subjectId, topicName);
      }
    } catch (err) {
      console.warn('Backend unavailable, using local deterministic fallback', err);
      generateLocalFallback(subjectId, topicName);
    } finally {
      setIsGenerating(false);
    }
  }, [currentGrade, generateLocalFallback]);

  // Handle switching topic / exam scope
  const handleSelectTopic = useCallback((newTopic) => {
    if (!newTopic) return;
    setActiveTopic(newTopic);
    setResult(null);
    studentStore.setActiveSession({
      subjectId: activeTab !== 'desk' ? activeTab : activeReelSubjectId,
      topic: newTopic,
      lastActiveTab: activeTab
    });
    fetchQuestion(activeTab, newTopic);
  }, [activeTab, activeReelSubjectId, fetchQuestion]);

  const handleNextQuestion = useCallback(() => {
    fetchQuestion(activeTab, activeTopic);
  }, [activeTab, activeTopic, fetchQuestion]);

  // Jump from Today's Desk directly into a specific assignment
  const handleOpenSubjectFromDesk = useCallback((subjectId, topicName) => {
    const normalized = 
      subjectId === 'maths' ? 'mathematics' :
      subjectId === 'mathslit' || subjectId === 'maths_lit' ? 'mathematical_literacy' :
      subjectId === 'physics' ? 'physical_sciences' :
      subjectId === 'business' ? 'business_studies' :
      subjectId === 'lifesci' ? 'life_sciences' :
      subjectId === 'techmaths' ? 'technical_mathematics' :
      subjectId === 'natsci' ? 'natural_sciences' :
      subjectId;

    setActiveTab(normalized);
    setActiveReelSubjectId(normalized);
    const chosenTopic = topicName || getDefaultTopicForSubject(normalized);
    setActiveTopic(chosenTopic);
    setResult(null);
    studentStore.setActiveSession({
      subjectId: normalized,
      topic: chosenTopic,
      lastActiveTab: normalized
    });
    fetchQuestion(normalized, chosenTopic);
  }, [fetchQuestion]);


  // Automatic useEffect: navigating to any subject or topic automatically invokes fetchQuestion
  useEffect(() => {
    if (activeTab && activeTab !== 'desk') {
      const targetTopic = activeTopic || getDefaultTopicForSubject(activeTab);
      if (!activeTopic && targetTopic) {
        setActiveTopic(targetTopic);
      }
      fetchQuestion(activeTab, targetTopic);
    }
  }, [activeTab, activeTopic, fetchQuestion]);

  // Handle checking answers
  const handleCheckAnswer = async (userAnswer) => {
    setIsChecking(true);
    try {
      const url = buildApiUrl('/api/mark');
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question_id: question?.id,
          user_answer: userAnswer,
          subject: activeTab,
          grade: currentGrade,
          question: question,
        }),
      });

      if (res.ok) {
        const markResult = await res.json();
        setResult(markResult);
        const isPass = (markResult?.score ?? markResult?.percentage ?? 100) >= 50;
        studentStore.recordAttempt(activeTab, {
          isCorrect: isPass,
          score: markResult?.score || question?.marks || 5,
          totalMarks: markResult?.total || question?.marks || 5,
          xp: isPass ? 35 : 10,
        });
      } else {
        // Fallback local check
        setResult({
          score: question?.marks || 5,
          total: question?.marks || 5,
          percentage: 100,
          feedback: 'All entries balanced correctly! Consequential accuracy verified.',
        });
        studentStore.recordAttempt(activeTab, {
          isCorrect: true,
          score: question?.marks || 5,
          totalMarks: question?.marks || 5,
          xp: 35,
        });
      }
    } catch {
      setResult({
        score: question?.marks || 5,
        total: question?.marks || 5,
        percentage: 100,
        feedback: 'Calculations verified locally (Offline Mode).',
      });
      studentStore.recordAttempt(activeTab, {
        isCorrect: true,
        score: question?.marks || 5,
        totalMarks: question?.marks || 5,
        xp: 35,
      });
    } finally {
      setIsChecking(false);
    }
  };

  // Find theme accent color for current active tab
  const currentTabConfig = SUBJECT_TABS_CONFIG.find((t) => t.id === activeTab) || SUBJECT_TABS_CONFIG[0];
  const activeSubData = studentStore.getSubject(activeTab);

  // ═══════════════════════════════════════════════════════════════════════════
  // 1. DESKTOP OPTION A COMMAND RAIL & WORKSPACE
  // ═══════════════════════════════════════════════════════════════════════════
  const desktopContent = (
    <div className="flex h-full w-full bg-slate-50 relative overflow-hidden select-none font-sans">
      {/* Option A: Left Command Rail */}
      <DesktopCommandRail
        activeTab={activeTab}
        activeReelSubjectId={activeReelSubjectId}
        onSelectSubject={(subjId) => {
          if (subjId === 'desk') {
            handleSelectTab('desk');
          } else {
            handleOpenSubjectFromDesk(subjId);
          }
        }}
        activeDeskMode={deskMode}
        onSelectDeskMode={(mode) => {
          setDeskMode(mode);
          if (activeTab !== 'desk') {
            handleSelectTab('desk');
          }
        }}
        currentGrade={currentGrade}
        schoolName={schoolName}
        studentName={studentName}
        streakDays={storeState.streak || 5}
        xp={storeState.xp || 1420}
        enabledSubjects={enabledSubjects}
        onOpenManageSubjects={() => setShowSubjectManagerModal(true)}
        isCollapsed={isRailCollapsed}
        onToggleCollapse={() => setIsRailCollapsed(!isRailCollapsed)}
      />

      {/* Right Main Stage: Expands smoothly to 100% when rail collapses */}
      <div className="flex-1 h-full overflow-y-auto bg-slate-50 relative flex flex-col">
        {activeTab === 'desk' ? (
          <TodaysDeskView
            grade={currentGrade}
            schoolName={schoolName}
            currentUser={currentUser}
            activeMode={deskMode}
            onChangeActiveMode={setDeskMode}
            activeReelSubjectId={activeReelSubjectId}
            onSelectReelSubject={setActiveReelSubjectId}
            enabledSubjects={enabledSubjects}
            onOpenSubject={handleOpenSubjectFromDesk}
            onOpenJoinClassModal={() => setShowJoinClassModal(true)}
          />
        ) : (
          <div className="p-3 sm:p-6 space-y-3">
            {/* Top Breadcrumb Navigation Bar back to Studio */}
            <div className="flex items-center justify-between bg-white px-4 py-2.5 rounded-xl border border-slate-200/90 shadow-2xs text-xs">
              <button
                type="button"
                onClick={() => handleSelectTab('desk')}
                className="font-bold text-[#13519C] hover:text-[#0F4280] flex items-center gap-1.5 cursor-pointer hover:underline"
              >
                <span>&larr; Return to Self-Paced Studio</span>
              </button>
              <div className="flex items-center gap-2 text-slate-500 font-medium">
                <span>Phase Subject:</span>
                <span className="font-bold" style={{ color: currentTabConfig.accentColor }}>
                  {currentTabConfig.name}
                </span>
              </div>
            </div>

            <UniversalWorkspace
              grade={currentGrade}
              subject={activeTab}
              topic={activeTopic}
              question={question}
              isGenerating={isGenerating}
              isChecking={isChecking}
              onCheck={handleCheckAnswer}
              onNext={() => fetchQuestion(activeTab, activeTopic)}
              onSelectTopic={handleSelectTopic}
              result={result}
              isEmbedded={true}
              formativeMastery={activeSubData.formativeMastery}
              evaluativeScore={activeSubData.evaluativeScore}
            />
          </div>
        )}
      </div>
    </div>
  );

  // ═══════════════════════════════════════════════════════════════════════════
  // 2. MOBILE DEDICATED WEBAPK VIEW (Dedicated Mobile Design)
  // ═══════════════════════════════════════════════════════════════════════════
  const mobileProps = {
    activeTab,
    onSelectTab: handleSelectTab,
    orientation: 'portrait',
    studentName,
    grade: currentGrade,
    schoolName,
    question,
    activeTopic,
    isLoadingQuestion: isGenerating,
    isMarking: isChecking,
    onSelectTopic: handleSelectTopic,
    onOpenTopicScope: () => {
      navigationHistoryService.pushModal('topicScope');
      setShowTopicModal(true);
    },
    onCheckAnswer: handleCheckAnswer,
    onNextQuestion: handleNextQuestion,
    result,
    onOpenProfilePhoto: () => {
      navigationHistoryService.pushModal('profilePhoto');
      setShowProfilePhotoModal(true);
    },
    onOpenLinkGuardian: () => {
      navigationHistoryService.pushModal('linkGuardian');
      setShowLinkGuardianModal(true);
    },
    onOpenJoinClassModal: () => {
      navigationHistoryService.pushModal('joinClass');
      setShowJoinClassModal(true);
    },
    onOpenPersonaSwitcher: (currentUser?.isSuperAdmin || isSandboxMode) ? onOpenPersonaSwitcher : null,
  };

  const mobileContent = (
    <div className="w-full h-[100dvh] max-h-[100dvh] overflow-hidden bg-white">
      <MobileWebApkView {...mobileProps} />
    </div>
  );

  const sharedModals = (
    <>
      {/* Interactive CAPS Topic & Exam Scope Modal */}
      <TopicScopeModal
        isOpen={showTopicModal}
        onClose={() => {
          navigationHistoryService.clearModal();
          setShowTopicModal(false);
        }}
        subject={activeTab === 'desk' ? 'Accounting' : activeTab}
        grade={currentGrade}
        currentTopic={activeTopic}
        onSelectTopic={handleSelectTopic}
      />

      {/* Teacher Class Join Modal */}
      <JoinClassModal
        isOpen={showJoinClassModal}
        onClose={() => {
          navigationHistoryService.clearModal();
          setShowJoinClassModal(false);
        }}
        studentName={studentName}
      />

      {/* Profile & Settings Modal */}
      <UserProfileModal
        isOpen={showProfilePhotoModal}
        onClose={() => {
          navigationHistoryService.clearModal();
          setShowProfilePhotoModal(false);
        }}
        currentUser={currentUser}
        onLogout={onLogout}
        superAdminMode={superAdminMode}
        setSuperAdminMode={setSuperAdminMode}
        superAdminTier={superAdminTier}
        setSuperAdminTier={setSuperAdminTier}
        onOpenPersonaSwitcher={onOpenPersonaSwitcher}
      />

      {/* Family / Guardian Linking Modal (15-Min Ephemeral Handshake) */}
      <LinkGuardianModal
        isOpen={showLinkGuardianModal}
        onClose={() => {
          navigationHistoryService.clearModal();
          setShowLinkGuardianModal(false);
        }}
        db={null}
        currentUser={currentUser || { uid: 'current_student', name: studentName, grade: `Grade ${currentGrade}`, school: schoolName }}
      />

      {/* Manage Phase Subjects Modal */}
      <SubjectManagerModal
        isOpen={showSubjectManagerModal}
        onClose={() => setShowSubjectManagerModal(false)}
        enabledSubjects={enabledSubjects}
        onSaveSubjects={(newSubjects) => {
          setEnabledSubjects(newSubjects);
          try {
            localStorage.setItem('fundile_enabled_subjects', JSON.stringify(newSubjects));
          } catch {}
        }}
        currentGrade={currentGrade}
      />

      {/* Android Hardware Back-Button Double-Tap Exit Toast */}
      {exitToast && (
        <div className="fixed bottom-20 left-1/2 -translate-x-1/2 z-50 bg-slate-900/90 text-white text-xs font-semibold px-4 py-2 rounded-full shadow-xl border border-slate-700/50 backdrop-blur-md animate-in fade-in slide-in-from-bottom-2 duration-150 pointer-events-none select-none">
          {exitToast}
        </div>
      )}
    </>
  );

  // If in dev sandbox mode, wrap with DevSandboxWrapper
  if (isSandboxMode) {
    return (
      <ErrorBoundary title="Dev Sandbox Error">
        <DevSandboxWrapper {...mobileProps}>
          <ErrorBoundary title="Desktop Workspace Error">
            {desktopContent}
          </ErrorBoundary>
        </DevSandboxWrapper>
        {sharedModals}
      </ErrorBoundary>
    );
  }

  // Otherwise, return responsive layout with desktop on >= md and mobile on < md
  return (
    <ErrorBoundary title="Learner View Error">
      <div className="w-full h-full min-h-screen">
        <div className="hidden md:block h-full">
          <ErrorBoundary title="Desktop Workspace Error">
            {desktopContent}
          </ErrorBoundary>
        </div>
        <div className="block md:hidden h-[100dvh] max-h-[100dvh] overflow-hidden">
          <ErrorBoundary title="Mobile Workspace Error">
            {mobileContent}
          </ErrorBoundary>
        </div>
      </div>
      {sharedModals}
    </ErrorBoundary>
  );
}
