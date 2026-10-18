import React, { useState, useEffect, useCallback, useRef } from 'react';
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
import SubjectEnrollmentModal from './SubjectEnrollmentModal';
import navigationHistoryService from '../../services/navigationHistoryService';
import { buildApiUrl } from '../../utils/apiBaseUrl';
import studentStore from '../../services/studentStore';
import ErrorBoundary from '../ui/ErrorBoundary';
import { getAuthenticDiagnosticQuestion } from '../../data/authenticDiagnosticBank';
import OfflineStudyPackModal from './OfflineStudyPackModal';
import offlineStorageService from '../../services/offlineStorageService';

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
  const [enabledSubjects, setEnabledSubjects] = useState(() => studentStore.getEnabledSubjects());
  const [showSubjectManagerModal, setShowSubjectManagerModal] = useState(false);
  const [showProfilePhotoModal, setShowProfilePhotoModal] = useState(false);
  const [showTopicModal, setShowTopicModal] = useState(false);
  const [showLinkGuardianModal, setShowLinkGuardianModal] = useState(false);
  const [showJoinClassModal, setShowJoinClassModal] = useState(false);
  const [showSubjectEnrollmentModal, setShowSubjectEnrollmentModal] = useState(() => {
    try {
      return localStorage.getItem('fundile_pending_subject_enrollment') === 'true';
    } catch {
      return false;
    }
  });
  const [exitToast, setExitToast] = useState('');
  const [consecutiveErrors, setConsecutiveErrors] = useState(0);
  const [prerequisiteBanner, setPrerequisiteBanner] = useState(null);
  const [showOfflinePackModal, setShowOfflinePackModal] = useState(false);
  const [isOfflineWorkspace, setIsOfflineWorkspace] = useState(() => !offlineStorageService.isOnline());

  useEffect(() => {
    const handleOnline = () => {
      setIsOfflineWorkspace(false);
      offlineStorageService.flushOfflineQueue().then(res => {
        if (res?.synced > 0) {
          console.log(`[OfflineSync] Synced ${res.synced} offline attempts.`);
        }
      });
    };
    const handleOffline = () => {
      setIsOfflineWorkspace(true);
    };

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  const [storeState, setStoreState] = useState(() => studentStore.getState());
  useEffect(() => {
    const unsub = studentStore.subscribe((newState) => {
      setStoreState({ ...newState });
      if (newState.enabledSubjects && Array.isArray(newState.enabledSubjects)) {
        setEnabledSubjects(newState.enabledSubjects);
      }
    });
    return unsub;
  }, []);

  const studentName = currentUser?.name || currentUser?.displayName || storeState.studentName || 'Prince Moyo';
  const currentGrade = parseInt(String(currentUser?.grade || storeState.grade || '10').replace(/\D/g, ''), 10) || 10;
  const isIndependent = Boolean(currentUser?.isIndependent ?? storeState?.isIndependent);
  const schoolName = isIndependent 
    ? 'Independent Homeschool' 
    : (currentUser?.school || currentUser?.schoolName || storeState.school || 'Westville High School');

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

  const lastFetchedKeyRef = useRef('');

  // Fetch / Generate a real question from caps-ai-backend or offline pack
  const fetchQuestion = useCallback(async (subjectId, topicName, force = false) => {
    const key = `${subjectId}:${topicName || ''}:${currentGrade}`;
    if (!force && lastFetchedKeyRef.current === key) {
      return;
    }
    lastFetchedKeyRef.current = key;
    setIsGenerating(true);
    setResult(null);

    // If device is offline, pull immediately from local 30-day offline study pack
    if (typeof navigator !== 'undefined' && !navigator.onLine) {
      try {
        const offlineQ = await offlineStorageService.getNextOfflineQuestion(subjectId, currentGrade, 1);
        if (offlineQ) {
          setQuestion(offlineQ);
          setIsOfflineWorkspace(true);
          setIsGenerating(false);
          return;
        }
      } catch (err) {
        console.warn('Offline pack lookup failed:', err);
      }
      generateLocalFallback(subjectId, topicName);
      setIsGenerating(false);
      return;
    }

    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 15000);

    try {
      const url = buildApiUrl(`/api/generate?subject=${encodeURIComponent(subjectId)}&grade=${currentGrade}&topic=${encodeURIComponent(topicName || '')}&seed=${Date.now()}`);
      const res = await fetch(url, { signal: controller.signal });
      if (res.ok) {
        const data = await res.json();
        const extracted = Array.isArray(data?.questions) && data.questions.length > 0 
          ? data.questions[0] 
          : (data?.questions || data);
        setQuestion(extracted);
        setIsOfflineWorkspace(false);
      } else {
        // Network non-OK: attempt offline pack before generic fallback
        const offlineQ = await offlineStorageService.getNextOfflineQuestion(subjectId, currentGrade, 1);
        if (offlineQ) {
          setQuestion(offlineQ);
          setIsOfflineWorkspace(true);
        } else {
          generateLocalFallback(subjectId, topicName);
        }
      }
    } catch (err) {
      console.warn('Backend unavailable or timed out, trying offline study pack', err?.message || err);
      try {
        const offlineQ = await offlineStorageService.getNextOfflineQuestion(subjectId, currentGrade, 1);
        if (offlineQ) {
          setQuestion(offlineQ);
          setIsOfflineWorkspace(true);
          return;
        }
      } catch (_) {}
      generateLocalFallback(subjectId, topicName);
    } finally {
      clearTimeout(timeoutId);
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
    fetchQuestion(activeTab, newTopic, true);
  }, [activeTab, activeReelSubjectId, fetchQuestion]);

  const handleNextQuestion = useCallback(() => {
    fetchQuestion(activeTab, activeTopic, true);
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

  // Handle starting adaptive prerequisite micro-drill
  const handleStartMicroDrill = useCallback((banner) => {
    if (!banner) return;
    const microTopic = banner.target_topic || 'Foundational Micro-Drill';
    setActiveTopic(microTopic);
    setPrerequisiteBanner(null);
    setConsecutiveErrors(0);
    fetchQuestion(activeTab, microTopic, true);
  }, [activeTab, fetchQuestion]);

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

        if (isPass) {
          setConsecutiveErrors(0);
          setPrerequisiteBanner(null);
        } else {
          setConsecutiveErrors((prev) => {
            const next = prev + 1;
            if (next >= 2) {
              setPrerequisiteBanner({
                target_grade: Math.max(8, currentGrade - 2),
                target_topic: activeTab === 'mathematics' ? 'Factorising Trinomials & HCF' : 'VAT Net vs Gross Calculations',
                target_subskill: activeTab === 'mathematics' ? 'common_factor_extraction' : 'net_vs_gross_calculation',
                explanation: `Repeated difficulty detected in ${activeTopic || 'current topic'}. A 5-minute foundational micro-drill in Grade ${Math.max(8, currentGrade - 2)} is recommended to rebuild the prerequisite schema.`,
              });
            }
            return next;
          });
        }
        return markResult;
      } else {
        // Server returned an error — do NOT auto-award marks
        console.warn(`[Mark API] Non-OK response: ${res.status}`);
        setResult({
          score: 0,
          total: question?.marks || 5,
          percentage: 0,
          feedback: 'Could not verify your answer — the marking server returned an error. Please try again.',
          verificationFailed: true,
        });
        studentStore.recordAttempt(activeTab, {
          isCorrect: false,
          score: 0,
          totalMarks: question?.marks || 5,
          xp: 0,
        });
        setConsecutiveErrors((prev) => {
          const next = prev + 1;
          if (next >= 2) {
            setPrerequisiteBanner({
              target_grade: Math.max(8, currentGrade - 2),
              target_topic: activeTab === 'mathematics' ? 'Factorising Trinomials & HCF' : 'VAT Net vs Gross Calculations',
              target_subskill: activeTab === 'mathematics' ? 'common_factor_extraction' : 'net_vs_gross_calculation',
              explanation: `Repeated difficulty detected in ${activeTopic || 'current topic'}. A 5-minute foundational micro-drill in Grade ${Math.max(8, currentGrade - 2)} is recommended to rebuild the prerequisite schema.`,
            });
          }
          return next;
        });
      }
    } catch (err) {
      console.warn('[Mark API] Network error, checking offline validation:', err?.message || err);
      // Offline fallback: Evaluate locally using pre-baked question data
      let isCorrect = false;
      const totalMarks = question?.marks || question?.marking_schema?.total_marks || 5;
      let earnedScore = 0;

      if (question?.correct_index !== undefined) {
        isCorrect = Number(userAnswer) === Number(question.correct_index);
        earnedScore = isCorrect ? totalMarks : 0;
      } else if (question?.correct_answer) {
        const uStr = String(userAnswer || '').trim().toLowerCase();
        const cStr = String(question.correct_answer || '').trim().toLowerCase();
        isCorrect = uStr.length > 0 && (uStr === cStr || cStr.includes(uStr));
        earnedScore = isCorrect ? totalMarks : 0;
      } else {
        isCorrect = String(userAnswer || '').trim().length > 10;
        earnedScore = isCorrect ? Math.round(totalMarks * 0.7) : 0;
      }

      const offlineResult = {
        score: earnedScore,
        total: totalMarks,
        percentage: Math.round((earnedScore / totalMarks) * 100),
        feedback: isCorrect 
          ? '✓ Correct! Offline attempt recorded locally and queued for synchronization.' 
          : 'Offline Review: Compare your working with the sample solution.',
        isOfflineEvaluated: true,
        sampleAnswer: question?.sample_answer || question?.correct_answer
      };

      setResult(offlineResult);
      studentStore.recordAttempt(activeTab, {
        isCorrect,
        score: earnedScore,
        totalMarks,
        xp: isCorrect ? 35 : 10,
      });

      // Queue offline attempt for telemetry synchronization
      offlineStorageService.queueOfflineAttempt({
        studentId: currentUser?.uid || 'local_learner',
        subject: activeTab,
        grade: currentGrade,
        topic: activeTopic,
        questionId: question?.id,
        score: earnedScore,
        totalMarks,
        isPass: isCorrect,
        userAnswer
      }).catch(qErr => console.warn('Failed to queue offline attempt:', qErr));

      return offlineResult;
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
            const normalized = 
              subjId === 'maths' ? 'mathematics' :
              subjId === 'mathslit' || subjId === 'maths_lit' ? 'mathematical_literacy' :
              subjId === 'physics' ? 'physical_sciences' :
              subjId === 'business' ? 'business_studies' :
              subjId === 'lifesci' ? 'life_sciences' :
              subjId === 'techmaths' ? 'technical_mathematics' :
              subjId === 'natsci' ? 'natural_sciences' :
              subjId;
            setActiveReelSubjectId(normalized);
            if (activeTab !== 'desk') {
              handleSelectTab('desk');
            }
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
        isIndependent={isIndependent}
        onOpenManageSubjects={() => setShowSubjectManagerModal(true)}
        onOpenOfflinePacks={() => setShowOfflinePackModal(true)}
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
            isIndependent={isIndependent}
            activeMode={deskMode}
            onChangeActiveMode={setDeskMode}
            activeReelSubjectId={activeReelSubjectId}
            onSelectReelSubject={setActiveReelSubjectId}
            enabledSubjects={enabledSubjects}
            onOpenSubject={handleOpenSubjectFromDesk}
            onOpenJoinClassModal={() => setShowJoinClassModal(true)}
            onOpenLinkGuardian={() => setShowLinkGuardianModal(true)}
            onOpenOfflinePacks={() => setShowOfflinePackModal(true)}
          />
        ) : (
          <div className="p-3 sm:p-5 space-y-3">
            {isOfflineWorkspace && (
              <div 
                data-testid="banner-offline-mode"
                className="bg-violet-50 border border-violet-200/90 text-violet-900 px-4 py-2.5 rounded-xl flex items-center justify-between text-xs animate-fadeIn shadow-2xs"
              >
                <div className="flex items-center gap-2">
                  <span className="w-2.5 h-2.5 rounded-full bg-violet-600 animate-pulse" />
                  <span className="font-bold">Offline Study Pack Active:</span>
                  <span>Practicing questions offline with pre-computed hints. Progress will sync when reconnected.</span>
                </div>
                <button
                  type="button"
                  data-testid="btn-manage-offline-banner"
                  onClick={() => setShowOfflinePackModal(true)}
                  className="font-bold text-violet-700 hover:text-violet-900 underline ml-2 cursor-pointer"
                >
                  Manage Packs &rarr;
                </button>
              </div>
            )}

            <UniversalWorkspace
              grade={currentGrade}
              subject={activeTab}
              topic={activeTopic}
              question={question}
              isGenerating={isGenerating}
              isChecking={isChecking}
              onCheck={handleCheckAnswer}
              onNext={() => fetchQuestion(activeTab, activeTopic, true)}
              onSelectTopic={handleSelectTopic}
              onStartMicroDrill={handleStartMicroDrill}
              prerequisiteBanner={prerequisiteBanner}
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
    onLogout: onLogout || (() => {}),
    enabledSubjects,
    onOpenManageSubjects: () => {
      navigationHistoryService.pushModal('manageSubjects');
      setShowSubjectManagerModal(true);
    },
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
        onSelectGrade={(g) => studentStore.setGrade(g)}
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
          studentStore.setEnabledSubjects(newSubjects);
        }}
        currentGrade={currentGrade}
      />

      {/* Self-Service Subject & Teacher Enrollment Modal */}
      <SubjectEnrollmentModal
        isOpen={showSubjectEnrollmentModal}
        onClose={() => {
          setShowSubjectEnrollmentModal(false);
          try {
            localStorage.removeItem('fundile_pending_subject_enrollment');
          } catch (_) {}
        }}
        currentUser={currentUser}
        schoolName={currentUser?.schoolName || schoolName}
        grade={currentGrade}
        onEnrollmentComplete={() => {
          setShowSubjectEnrollmentModal(false);
          try {
            localStorage.removeItem('fundile_pending_subject_enrollment');
          } catch (_) {}
        }}
      />

      {/* 30-Day Offline Study Pack Modal */}
      <OfflineStudyPackModal
        isOpen={showOfflinePackModal}
        onClose={() => setShowOfflinePackModal(false)}
        grade={currentGrade}
        enabledSubjects={enabledSubjects}
        studentId={currentUser?.uid || 'local_learner'}
        onPackDownloaded={() => {
          if (typeof navigator !== 'undefined' && !navigator.onLine) {
            fetchQuestion(activeTab, activeTopic, true);
          }
        }}
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
