// React imports
import React, { useState, useEffect, useCallback, useRef, useMemo } from 'react';

// Third-party library imports
import { applyActionCode } from 'firebase/auth';
import { doc, getDoc, setDoc, updateDoc, serverTimestamp, collection, onSnapshot, orderBy, query, where, getDocs } from 'firebase/firestore';
import { BookOpen, User, Target, BarChart2, PenTool, ClipboardEdit, BrainCircuit, FileText, GraduationCap, BookCopy, CheckSquare, Loader2, UserPlus, Edit, Send, FileSignature, Book, Users, Settings, LogOut, Eye, MessageSquare, UserCheck, Briefcase, FunctionSquare, FilePlus, AlertTriangle, PlusCircle, Bell, MessageCircle, CheckCircle, Trophy, X, Activity, Compass } from 'lucide-react';

// Local imports
import { curriculumData } from './curriculumData';

// Import extracted components
import AuthScreen from './components/auth/AuthScreen';
import VerificationScreen from './components/auth/VerificationScreen';

// Import extracted form components

// Import extracted source document components

// Import new math components

// Import thumbnail test page
// Import integration demo
// Import geometry backend test

// Import extracted components

// Import custom hooks
import {
  useAuthentication,
  useCoreState,
  isStandaloneApp,
  useCurriculumNavigation,
  useWorkspaceUI,
  useChatFunctionality,
  useFreeformTopics,
  useTeacherAdminViews,
  useAssignmentsPractice
} from './hooks';

// Import extracted utilities and constants
import { getCurriculumRootNavigationStack, shouldResetSelectionForView } from './app/utils/navigationReset';
import { useFreeformProblemFlow } from './app/hooks/useFreeformProblemFlow';
import { useAppSessionReset } from './app/hooks/useAppSessionReset';
import { useTopLevelRouting } from './app/hooks/useTopLevelRouting';
import { useWorkspaceSubmissionFlow } from './app/hooks/useWorkspaceSubmissionFlow';
import RenderRoleContent from './app/render/renderRoleContent';
import AppShell from './app/shell/AppShell';

// Import new UI components
import SplashScreen from './components/ui/SplashScreen';
import LandingPage from './components/ui/LandingPage';
import SubscriptionPage from './components/ui/SubscriptionPage';
import PrivacyStatementView from './components/ui/PrivacyStatementView';
import LearnerAppContainer from './components/student/LearnerAppContainer';
import Header from './components/ui/Header';
import PersonaSwitcherModal from './components/dev/PersonaSwitcherModal';
import studentStore from './services/studentStore';

// Import API utilities
import { buildApiUrl } from './utils/apiBaseUrl';

// Import accounting validation utilities

// Import curriculum helper utilities

// --- Constants & Configuration ---

// Source Documents Repository - Now imported from constants/sourceDocuments.js

// App Configuration - Now imported from constants/sourceDocuments.js

// API functions have been moved to src/utils/api.js

// GraduationCapSplash component has been moved to src/components/ui/GraduationCapSplash.jsx

// FundileLogo component has been moved to src/components/ui/FundileLogo.jsx

// Netflix-style Splash Screen Component
// SplashScreen component has been moved to src/components/ui/SplashScreen.jsx

// Landing Page Component
// LandingPage component has been moved to src/components/ui/LandingPage.jsx

// --- AI Workaround Solutions for Journal Components ---

// --- Utility Functions ---

// Journal Conversion Functions
// convertJournalToText function - Now imported from utils/journalUtils.js

// convertCashReceiptsToText function - Now imported from utils/journalUtils.js

// convertCashPaymentsToText function - Now imported from utils/journalUtils.js

// convertDebtorsJournalToText and convertCreditorsJournalToText functions - Now imported from utils/journalUtils.js

// convertGeneralLedgerToText and convertTrialBalanceToText functions - Now imported from utils/journalUtils.js

// convertDebtorsLedgerToText function is now imported from utils/journalUtils.js

// convertCreditorsLedgerToText function is now imported from utils/journalUtils.js

// convertAccountingEquationToText function is now imported from utils/journalUtils.js



// journalQuestionTemplate has been moved to src/utils/curriculumHelpers.js

// Accounting validation functions have been moved to src/utils/accountingValidation.js

// Curriculum helper functions have been moved to src/utils/curriculumHelpers.js

// // --- Text Processing & Mathematical Content Functions (Imported from modular utils) ---
import {
  getPlainTextFromHtml,
  detectMathStructure,
  formatMathematicalContent,
  shouldUseMathStructure,
  formatMathematicalExpressions,
  processMathematicalContent,
} from './utils/mathContentUtils';



// --- Exam Generators (Imported from modular components) ---
import {
  PracticeExamGenerator,
  CompetitionExamGenerator,
} from './components/exam/PracticeExamGenerator';


const parseFlexibleNumber = (value) => {
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

const numbersMatchForCurrency = (actual, expected) => {
  const actualN = typeof actual === 'number' ? actual : parseFlexibleNumber(actual);
  const expectedN = typeof expected === 'number' ? expected : parseFlexibleNumber(expected);
  if (!Number.isFinite(actualN) || !Number.isFinite(expectedN)) return false;
  if (Math.abs(actualN - expectedN) <= 0.01) return true;
  return Math.round(actualN) === Math.round(expectedN);
};

const extractJsonFromString = (str) => {
  const jsonRegex = /```json\s*([\s\S]*?)\s*```/;
  const match = str.match(jsonRegex);
  if (match && match[1]) {
    try { return JSON.parse(match[1]); } catch (e) { /* Fallback below */ }
  }
  try { return JSON.parse(str); } catch (e) { return null; }
};
const getRandomColor = () => { const letters = '0123456789ABCDEF'; let color = '#'; for (let i = 0; i < 6; i++) { color += letters[Math.floor(Math.random() * 16)]; } return color; };
const abbreviateSubjectName = (subjectName) => {
  switch (subjectName) {
    case 'Mathematics': return 'Maths';
    case 'Mathematical Literacy': return 'Maths Lit';
    case 'Technical Mathematics': return 'Tec.Maths';
    default: return subjectName;
  }
};
const formatGrade = (grade) => `Gr ${grade}`;



// --- Dynamic Curriculum Data Generation from curriculumData.js ---

// Derive all available grades for CAPS from the curriculumData
const allAvailableCapsGrades = new Set();
Object.values(curriculumData).forEach(subjectGrades => {
  Object.keys(subjectGrades).forEach(grade => allAvailableCapsGrades.add(Number(grade)));
});
const sortedAllAvailableCapsGrades = Array.from(allAvailableCapsGrades).sort((a, b) => a - b);

// Dynamically create the subjects array for CAPS based on curriculumData
const dynamicCapsSubjects = Object.keys(curriculumData).map(subjectName => {
  const gradesData = curriculumData[subjectName];
  const availableGrades = Object.keys(gradesData).map(Number).sort((a, b) => a - b);

  // Default icons and descriptions (can be customized further if needed)
  let IconComponent = Book; // Default icon
  let description = 'Curriculum subject.';
  let color = getRandomColor(); // Assign a random color if not specified

  // Assign specific icons, descriptions, and colors based on subject name
  switch (subjectName) {
    case 'Mathematics':
      IconComponent = Target;
      description = 'Core concepts of algebra, geometry, and calculus.';
      color = 'bg-blue-500';
      break;
    case 'Mathematical Literacy':
      IconComponent = BarChart2;
      description = 'Practical application of math in everyday life.';
      color = 'bg-green-500';
      break;
    case 'Technical Mathematics':
      IconComponent = PenTool;
      description = 'Mathematics for technical and trade fields.';
      color = 'bg-purple-500';
      break;
    case 'Accounting':
      IconComponent = Briefcase;
      description = 'Principles of financial accounting and business transactions.';
      color = 'bg-yellow-500';
      break;
    case 'Business Studies':
      IconComponent = Users;
      description = 'Understanding business principles, management, and economics.';
      color = 'bg-red-500';
      break;
    case 'Economic and Management Sciences': // EMS
      IconComponent = FunctionSquare; // Placeholder icon for EMS
      description = 'Integrated study of economics, business, and accounting.';
      color = 'bg-orange-500';
      break;
    case 'Physical Sciences':
      IconComponent = BrainCircuit; // Placeholder icon for Physical Sciences
      description = 'Study of physics and chemistry concepts.';
      color = 'bg-cyan-500';
      break;
    case 'Life Sciences':
      IconComponent = Activity;
      description = 'Study of living organisms, genetics, and ecology.';
      color = 'bg-emerald-500';
      break;
    case 'Natural Sciences':
      IconComponent = Compass;
      description = 'Foundation science covering matter, energy, and life.';
      color = 'bg-teal-500';
      break;
    default:
      break;
  }

  return {
    id: subjectName.toLowerCase().replace(/\s/g, '-'), // Create a simple ID from the name
    name: subjectName,
    icon: IconComponent, // Use the determined icon component
    description: description,
    color: color,
    availableGrades: availableGrades,
    topicsByGrade: gradesData // Direct reference to the grade-topic structure from curriculumData
  };
});

// The main curriculum shell structure, now dynamically populated for CAPS
const curriculumShell = {
  'CAPS': {
    name: 'South African National Curriculum',
    description: 'The official national curriculum for South Africa.',
    loaded: true,
    grades: sortedAllAvailableCapsGrades, // Use dynamically derived grades
    subjects: dynamicCapsSubjects
  },
  'Cambridge': { name: 'Cambridge Curriculum', description: 'International curriculum offered in over 160 countries.', loaded: false, grades: [10, 11, 12], subjects: [] }
};
const userSubscription = { accessibleCurricula: ['CAPS'] };

// --- UI Components ---

// Netflix-style Background Component for Auth Screenok
const AuthBackground = () => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [isMobile, setIsMobile] = useState(false);

  const desktopImage = '/backgrounds/desktop-bg.jpg';
  const mobileImages = [
    '/backgrounds/mobile-bg-1.jpg',
    '/backgrounds/mobile-bg-2.jpg',
    '/backgrounds/mobile-bg-3.jpg'
  ];

  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth < 768);
    };

    checkMobile();
    window.addEventListener('resize', checkMobile);

    let interval;
    if (isMobile) {
      interval = setInterval(() => {
        setCurrentImageIndex(prev => (prev + 1) % mobileImages.length);
      }, 5000);
    }

    return () => {
      window.removeEventListener('resize', checkMobile);
      if (interval) clearInterval(interval);
    };
  }, [isMobile]);

  useEffect(() => {
    console.log("✅ AuthBackground mounted");
  }, []);

  const getBackgroundImage = () => {
    return isMobile ? mobileImages[currentImageIndex] : desktopImage;
  };

  console.log("📷 Background URL:", getBackgroundImage());

  return (
    <div className="fixed inset-0 overflow-hidden">
      {/* Background image layer */}
      <div
        className="absolute inset-0 z-0 bg-cover bg-center bg-no-repeat transition-all duration-1000 ease-in-out"
        style={{
          backgroundImage: `url(${getBackgroundImage()})`,
        }}
      />

      {/* Slight dark overlay for readability */}
      <div className="absolute inset-0 z-10 bg-black/30" />

      {/* Stylish gradient overlay from bottom */}
      <div className="absolute inset-0 z-20 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
    </div>
  );


};



// RoleSelector component has been extracted to forms/AdminForms.jsx

// CurriculumSelector component has been extracted to forms/StudentForms.jsx
// GradeSelector component has been extracted to forms/StudentForms.jsx
// SubscriptionStatus component has been extracted to forms/StudentForms.jsx
// SubjectDashboard component has been extracted to forms/StudentForms.jsx
// StudyModeSelector component has been extracted to forms/StudentForms.jsx
// --- New/Updated Components for Question/Answer Handling ---
// TableRenderer component has been extracted to forms/TableComponents.jsx
// TableInput component has been extracted to forms/TableComponents.jsx
// MoneyInput component has been extracted to forms/TableComponents.jsx
// CashReceiptsJournalInput component has been extracted to sourceDocuments/CashReceiptsJournalInput.jsx
// CashPaymentsJournalInput component has been extracted to sourceDocuments/CashPaymentsJournalInput.jsx
// Math components have been extracted to src/components/math/
// DebtorsJournalInput component has been extracted to sourceDocuments/DebtorsJournalInput.jsx
// TrialBalanceInput component has been extracted to sourceDocuments/TrialBalanceInput.jsx
// Math components have been extracted to src/components/math/
// GeneralLedgerInput component has been extracted to sourceDocuments/GeneralLedgerInput.jsx
// DebtorsLedgerInput component has been extracted to sourceDocuments/DebtorsLedgerInput.jsx
// AccountingEquationTableInput component has been extracted to sourceDocuments/AccountingEquationTableInput.jsx

// This component displays a list of struggling problems saved by the user.
// It allows the user to view the problem details, continue the conversation,
// or mark a problem as solved (which deletes it from storage).
// --- MySavedProblemsView Component (Now defined within App.jsx) ---
const MySavedProblemsView = ({
  db, // Firestore database instance
  currentUser, // Current authenticated user
  onContinueProblem, // Function to load a problem into the workspace
  onMarkSolved, // Function to mark a problem as solved (deletes it)
  setMessage // Function to display messages/notifications
}) => {
  const [strugglingProblems, setStrugglingProblems] = useState([]);
  const [loadingProblems, setLoadingProblems] = useState(true);
  const [error, setError] = useState(null);

  // Effect to fetch struggling problems from Firestore in real-time
  useEffect(() => {
    if (!db || !currentUser?.uid) {
      setLoadingProblems(false);
      return;
    }

    const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';
    const problemsCollectionRef = collection(db, 'artifacts', appId, 'users', currentUser.uid, 'struggling_problems');

    // Order by lastUpdated to show most recent struggling problems first
    const q = query(problemsCollectionRef, orderBy('lastUpdated', 'desc'));

    const unsubscribe = onSnapshot(q, (snapshot) => {
      const fetchedProblems = snapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }));
      setStrugglingProblems(fetchedProblems);
      setLoadingProblems(false);
      setError(null); // Clear any previous errors on successful fetch
    }, (err) => {
      console.error("Error fetching struggling problems:", err);
      setError("Failed to load your saved problems. Please try again.");
      setLoadingProblems(false);
    });

    // Cleanup listener on component unmount
    return () => unsubscribe();
  }, [db, currentUser?.uid]);

  // Handler for when a user clicks to continue a struggling problem
  const handleContinueClick = useCallback((problem) => {
    // Call the prop function to load this problem into the main workspace
    onContinueProblem(problem);
  }, [onContinueProblem]);

  // Handler for when a user clicks to mark a problem as solved
  const handleMarkSolvedClick = useCallback((threadId) => {
    // Call the prop function to delete this problem from storage
    onMarkSolved(threadId);
  }, [onMarkSolved]);

  if (loadingProblems) {
    return (
      <div className="flex items-center justify-center h-full p-8">
        <Loader2 className="h-12 w-12 animate-spin text-blue-600" />
        <p className="ml-4 text-gray-600">Loading your saved problems...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full p-8 text-red-600">
        <AlertTriangle className="h-12 w-12 mb-4" />
        <p className="text-lg text-center">{error}</p>
      </div>
    );
  }

  return (
    <div className="p-4 sm:p-6 lg:p-8 bg-gray-50 min-h-screen">
      <h2 className="text-3xl font-extrabold text-gray-900 mb-8 text-center">My Saved Problems</h2>

      {strugglingProblems.length === 0 ? (
        <div className="bg-white p-8 rounded-xl shadow-lg text-center text-gray-600">
          <p className="text-lg">You haven't saved any struggling problems yet.</p>
          <p className="mt-2 text-sm">When you struggle with a problem in the Freeform Workspace, you can save it here to revisit later.</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {strugglingProblems.map((problem) => (
            <div key={problem.id} className="bg-white rounded-xl shadow-lg p-6 border border-gray-200 flex flex-col justify-between transition-all duration-200 hover:shadow-xl hover:border-blue-300">
              <div>
                <h3 className="text-lg font-semibold text-gray-800 mb-2 flex items-center">
                  <MessageCircle className="h-5 w-5 text-blue-500 mr-2 flex-shrink-0" />
                  {problem.topic || 'General Problem'}
                </h3>
                <p className="text-sm text-gray-600 mb-4">
                  Subject: <span className="font-medium">{problem.subject || 'N/A'}</span> |
                  Grade: <span className="font-medium">{problem.grade || 'N/A'}</span>
                </p>
                <div className="text-gray-700 text-sm max-h-24 overflow-hidden mb-4 border-t pt-4 border-gray-100">
                  {/* Display a snippet of the last message or the first question */}
                  {problem.chatHistory && problem.chatHistory.length > 0 ? (
                    <>
                      <p className="font-semibold mb-1">Last Interaction:</p>
                      <p className="line-clamp-3">{problem.chatHistory[problem.chatHistory.length - 1].question || problem.chatHistory[problem.chatHistory.length - 1].answer}</p>
                    </>
                  ) : (
                    <p>No chat history available for this problem.</p>
                  )}
                </div>
              </div>
              <div className="mt-4 flex flex-col space-y-2">
                <button
                  onClick={() => handleContinueClick(problem)}
                  className="w-full flex items-center justify-center px-4 py-2 bg-blue-600 text-white rounded-lg shadow-md hover:bg-blue-700 transition-colors duration-200 text-sm font-medium"
                >
                  <MessageCircle className="h-4 w-4 mr-2" /> Continue Working
                </button>
                <button
                  onClick={() => handleMarkSolvedClick(problem.id)}
                  className="w-full flex items-center justify-center px-4 py-2 bg-green-100 text-green-800 rounded-lg shadow-md hover:bg-green-200 transition-colors duration-200 text-sm font-medium"
                >
                  <CheckCircle className="h-4 w-4 mr-2" /> Mark as Solved
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};


// ... (Keep all your imports and helper functions above this) ...

// CurriculumHelper component has been extracted to src/components/curriculum/CurriculumHelper.jsx
// const CurriculumHelper = React.memo(({ onClose, getAgentResponse, setPracticeQuestions, selectedGrade, selectedSubject, setWorkspaceMode, currentMode, updateHelperNavigationLabel, setView, setNavigationStack, navigationStack, loading, setLoading, chatHistory, setChatHistory }) => { 
// CurriculumHelper component has been extracted to src/components/curriculum/CurriculumHelper.jsx

// ClassworkView component has been extracted to src/components/student/ClassworkView.jsx


// AssignClassModal component has been extracted to src/components/admin/AssignClassModal.jsx


// AssessmentGenerator component has been extracted to src/components/teacher/AssessmentGenerator.jsx

// TeacherView component has been extracted to src/components/teacher/TeacherView.jsx

// SubmissionsDashboard component has been extracted to src/components/teacher/SubmissionsDashboard.jsx



// AdminView component has been extracted to src/components/admin/AdminView.jsx


// Custom hooks have been moved to src/hooks/ directory

const stripFirebaseActionParamsFromUrl = () => {
  if (typeof window === 'undefined') return;

  const url = new URL(window.location.href);
  ['mode', 'oobCode', 'apiKey', 'lang', 'continueUrl'].forEach((key) => {
    url.searchParams.delete(key);
  });

  const nextUrl = `${url.pathname}${url.search}${url.hash}`;
  window.history.replaceState({}, document.title, nextUrl || '/');
};

const getEmailActionErrorMessage = (error) => {
  switch (error?.code) {
    case 'auth/invalid-action-code':
      return 'This verification link is invalid or has already been used.';
    case 'auth/expired-action-code':
      return 'This verification link has expired. Please request a new verification email.';
    case 'auth/user-disabled':
      return 'This account has been disabled. Please contact support.';
    default:
      return error?.message || 'We could not complete email verification from this link.';
  }
};

// --- Main App Component ---
export default function App() {
  // Use custom hooks to organize state
  const authHook = useAuthentication();
  const core = useCoreState();
  const curriculum = useCurriculumNavigation();
  const assignments = useAssignmentsPractice();
  const workspace = useWorkspaceUI();
  const teacherAdmin = useTeacherAdminViews();
  const chat = useChatFunctionality();
  const freeform = useFreeformTopics();

  // Destructure for easier access
  const {
    auth, db, storage, dbService, currentUser, authLoading, handleLogout, refreshCurrentUser
  } = authHook;

  const {
    loading, setLoading, message, setMessage, showSplash, setShowSplash,
    setShowLandingPage, chatRoomId, setChatRoomId,
    chatPermissionsAvailable, setChatPermissionsAvailable,
    messages, setMessages
  } = core;

  const {
    view, setView, allCurricula, setAllCurricula, selectedCurriculumKey,
    setSelectedCurriculumKey, selectedGrade, setSelectedGrade, selectedSubject,
    setSelectedSubject, activeTopic, setActiveTopic, isCurriculumPageVisible,
    setIsCurriculumPageVisible, navigationStack, setNavigationStack
  } = curriculum;

  const {
    pendingAssignments, setPendingAssignments, activeAssignment,
    setActiveAssignment,
    practiceQuestions, setPracticeQuestions
  } = assignments;

  const {
    isKeypadVisible, setIsKeypadVisible, activeEditableRef,
    setActiveEditableRef, workspaceMode, setWorkspaceMode, freeformWorkAreaRef
  } = workspace;

  const {
    teacherView, setTeacherView, adminView, setAdminView, schoolAdminView, setSchoolAdminView
  } = teacherAdmin;

  const {
    freeformAnswer, setFreeformAnswer, chatHistories, setChatHistories,
    chatHistory, setChatHistory
  } = chat;

  const {
    selectedFreeformTopic, setSelectedFreeformTopic,
    currentProblemThreadId, setCurrentProblemThreadId
  } = freeform;

  const [superAdminMode, setSuperAdminMode] = useState('student');
  const [superAdminTier, setSuperAdminTier] = useState('standard');
  const [activePersona, setActivePersona] = useState(null);
  const [showPersonaSwitcher, setShowPersonaSwitcher] = useState(false);
  const [authStatusMessage, setAuthStatusMessage] = useState('');
  const [brandPalette, setBrandPalette] = useState(() => {
    if (typeof window === 'undefined') return 'light';
    return window.sessionStorage.getItem('fundileBrandPalette') === 'dark' ? 'dark' : 'light';
  });
  const [studentNotifications, setStudentNotifications] = useState([]);
  const processedEmailActionRef = useRef('');

  const handleSwitchPersona = useCallback((persona) => {
    setActivePersona(persona);
    if (persona.role === 'student') {
      setSuperAdminMode('student');
      studentStore.setStudentProfile(persona.name, persona.grade, persona.school);
      studentStore.setState({ deskDues: persona.assignedTasks?.length || 0, currentUser: persona });
    } else if (persona.role === 'teacher') {
      setSuperAdminMode('teacher');
    } else if (persona.role === 'parent') {
      setSuperAdminMode('parent');
    } else if (persona.role === 'school' || persona.role === 'school_admin') {
      setSuperAdminMode('school');
    } else if (persona.role === 'admin') {
      setSuperAdminMode('admin');
    }
  }, []);

  const handleSetSuperAdminMode = useCallback((mode) => {
    setSuperAdminMode(mode);
    if (activePersona) {
      setActivePersona((prev) => prev ? { ...prev, role: mode } : null);
    }
  }, [activePersona]);

  const [parentDualUseChild, setParentDualUseChild] = useState(null);

  const handleLaunchLearnerWorkspace = useCallback((childProfile) => {
    if (!childProfile) return;
    const numericGrade = Number(String(childProfile.grade || '10').replace(/\D/g, '')) || 10;
    studentStore.setStudentProfile(childProfile.name, numericGrade, childProfile.school || 'High School');
    setSelectedGrade(numericGrade);
    setParentDualUseChild(childProfile);
  }, [setSelectedGrade]);

  const handleExitParentDualUse = useCallback(() => {
    setParentDualUseChild(null);
  }, []);

  const effectiveRole = parentDualUseChild
    ? 'student'
    : (activePersona ? activePersona.role : (currentUser?.isSuperAdmin ? superAdminMode : currentUser?.role));
  const effectiveTier = currentUser?.isSuperAdmin || currentUser?.isOwner ? superAdminTier : currentUser?.tier;
  const effectiveCurrentUser = useMemo(
    () => {
      if (parentDualUseChild) {
        const numericGrade = Number(String(parentDualUseChild.grade || '10').replace(/\D/g, '')) || 10;
        return {
          ...currentUser,
          uid: currentUser?.uid,
          name: parentDualUseChild.name,
          displayName: parentDualUseChild.name,
          grade: numericGrade,
          school: parentDualUseChild.school || 'High School',
          role: 'student',
          tier: effectiveTier,
          isParentDualUse: true,
          parentDualUseChild,
          parentUser: currentUser,
        };
      }
      if (activePersona) {
        return {
          ...currentUser,
          ...activePersona,
          role: activePersona.role,
          tier: effectiveTier,
          isSuperAdmin: true,
        };
      }
      return currentUser ? { ...currentUser, role: effectiveRole, tier: effectiveTier } : null;
    },
    [currentUser, activePersona, effectiveRole, effectiveTier, parentDualUseChild]
  );
  const isWithin48hGrace = useMemo(() => {
    if (!effectiveCurrentUser) return false;
    if (effectiveCurrentUser.emailVerified) return true;
    const graceTimestamp = effectiveCurrentUser.emailVerificationGraceUntil || effectiveCurrentUser.createdAt;
    if (!graceTimestamp) return false;
    const graceDate = graceTimestamp?.toDate ? graceTimestamp.toDate() : new Date(graceTimestamp);
    if (Number.isNaN(graceDate.getTime())) return false;
    const cutoff = effectiveCurrentUser.emailVerificationGraceUntil
      ? graceDate.getTime()
      : graceDate.getTime() + 48 * 60 * 60 * 1000;
    return Date.now() < cutoff;
  }, [effectiveCurrentUser]);

  const hasVerifiedAccess = Boolean(
    effectiveCurrentUser?.isOwner ||
    effectiveCurrentUser?.isSuperAdmin ||
    effectiveCurrentUser?.emailVerified ||
    isWithin48hGrace
  );
  const {
    authMode,
    handleNavigateHome,
    handleNavigateSignIn,
    handleNavigateSignUp,
    handleNavigatePrivacy,
    handleNavigateToDashboard,
    handleNavigateToSubscriptionPage,
    handleSplashComplete,
    navigateToRoutePage,
    resetTopLevelRouting,
    shouldRenderStandaloneLandingPage,
    topLevelPage,
  } = useTopLevelRouting({
    authLoading,
    hasVerifiedAccess,
    isAuthenticated: Boolean(effectiveCurrentUser),
    isAnonymous: Boolean(effectiveCurrentUser?.isAnonymous),
    setShowLandingPage,
    setShowSplash,
    showSplash,
  });
  const { handleAppLogout } = useAppSessionReset({
    handleLogout,
    resetTopLevelRouting,
    setMessage,
    setShowSplash,
    setView,
    setNavigationStack,
    setSelectedCurriculumKey,
    setSelectedGrade,
    setSelectedSubject,
    setActiveTopic,
    setActiveAssignment,
    setPracticeQuestions,
    setPendingAssignments,
    setSelectedFreeformTopic,
    setCurrentProblemThreadId,
    setChatHistory,
    setFreeformAnswer,
  });

  useEffect(() => {
    if (currentUser?.isSuperAdmin) {
      setSuperAdminMode('student');
    }
  }, [currentUser?.isSuperAdmin]);

  useEffect(() => {
    if (!auth || typeof window === 'undefined') {
      return undefined;
    }

    const searchParams = new URLSearchParams(window.location.search);
    const mode = searchParams.get('mode');
    const oobCode = searchParams.get('oobCode');

    if (mode !== 'verifyEmail' || !oobCode) {
      return undefined;
    }

    const actionKey = `${mode}:${oobCode}`;
    if (processedEmailActionRef.current === actionKey) {
      return undefined;
    }
    processedEmailActionRef.current = actionKey;

    let cancelled = false;

    const handleEmailVerificationAction = async () => {
      try {
        await applyActionCode(auth, oobCode);

        if (cancelled) return;

        if (auth.currentUser) {
          const result = await refreshCurrentUser();
          if (!cancelled && result?.success === false) {
            setAuthStatusMessage('Email verified successfully. Please sign in again if your session does not refresh automatically.');
          } else if (!cancelled) {
            setAuthStatusMessage('Email verified successfully. You can continue into Fundile.');
          }
        } else {
          setAuthStatusMessage('Email verified successfully. Please sign in to continue.');
        }
      } catch (error) {
        if (!cancelled) {
          setAuthStatusMessage(getEmailActionErrorMessage(error));
        }
      } finally {
        if (!cancelled) {
          stripFirebaseActionParamsFromUrl();
        }
      }
    };

    handleEmailVerificationAction();

    return () => {
      cancelled = true;
    };
  }, [auth, refreshCurrentUser]);

  useEffect(() => {
    if (!effectiveCurrentUser?.uid || !dbService || !hasVerifiedAccess || effectiveCurrentUser.role !== 'student') {
      setStudentNotifications([]);
      return undefined;
    }

    const notificationsRef = collection(dbService, 'users', effectiveCurrentUser.uid, 'notifications');
    const notificationsQuery = query(notificationsRef, orderBy('createdAt', 'desc'));

    const unsubscribe = onSnapshot(
      notificationsQuery,
      (snapshot) => {
        setStudentNotifications(snapshot.docs.map((snapshotDoc) => ({
          id: snapshotDoc.id,
          ...snapshotDoc.data(),
        })));
      },
      (error) => {
        console.error('Error fetching student notifications:', error);
        setStudentNotifications([]);
      }
    );

    return () => unsubscribe();
  }, [dbService, effectiveCurrentUser?.role, effectiveCurrentUser?.uid, hasVerifiedAccess]);

  useEffect(() => {
    if (!effectiveCurrentUser?.uid || !dbService || !hasVerifiedAccess || effectiveCurrentUser.role !== 'student') {
      return undefined;
    }

    let cancelled = false;

    const ensureWelcomeNotification = async () => {
      try {
        const welcomeNotificationRef = doc(dbService, 'users', effectiveCurrentUser.uid, 'notifications', 'welcome_v1');
        const welcomeNotificationDoc = await getDoc(welcomeNotificationRef);

        if (welcomeNotificationDoc.exists() || cancelled) {
          return;
        }

        await setDoc(welcomeNotificationRef, {
          type: 'welcome',
          title: 'Welcome to Fundile',
          message: effectiveCurrentUser.grade
            ? `Welcome to Fundile. Your live path currently starts with Grade ${effectiveCurrentUser.grade} Accounting, and more grades and subjects will be added as rollout expands.`
            : 'Welcome to Fundile. Start with the live Accounting experience now, and watch for future rollout updates as more grades and subjects become available.',
          isRead: false,
          source: 'system',
          userId: effectiveCurrentUser.uid,
          createdAt: serverTimestamp(),
          readAt: null,
        });

        try {
          await updateDoc(doc(dbService, 'users', effectiveCurrentUser.uid), {
            welcomeNotificationCreatedAt: serverTimestamp(),
          });
        } catch (error) {
          console.warn('Could not persist welcome notification audit field:', error);
        }
      } catch (error) {
        console.error('Error creating welcome notification:', error);
      }
    };

    ensureWelcomeNotification();

    return () => {
      cancelled = true;
    };
  }, [dbService, effectiveCurrentUser?.grade, effectiveCurrentUser?.role, effectiveCurrentUser?.uid, hasVerifiedAccess]);

  const handleVerificationComplete = useCallback(async () => {
    const result = await refreshCurrentUser();

    if (result?.success) {
      navigateToRoutePage('dashboard');
    }

    return result;
  }, [navigateToRoutePage, refreshCurrentUser]);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      window.sessionStorage.setItem('fundileBrandPalette', brandPalette);
    }
  }, [brandPalette]);

  useEffect(() => {
    if (typeof document === 'undefined') {
      return;
    }

    const titleCurriculum = selectedCurriculumKey || effectiveCurrentUser?.curriculum || (effectiveRole === 'teacher' ? 'CAPS' : null);
    const isCAPSContext = titleCurriculum === 'CAPS';

    if (isCAPSContext && effectiveRole === 'teacher') {
      document.title = 'Fundile | Curriculum-Aligned Teaching Assistant';
      return;
    }

    if (isCAPSContext && effectiveRole === 'student') {
      document.title = 'Fundile | Curriculum-Aligned Learning Assistant';
      return;
    }

    if (isCAPSContext && effectiveRole === 'parent') {
      document.title = 'Fundile | Parent Portal';
      return;
    }

    if (isCAPSContext && (effectiveRole === 'school' || effectiveRole === 'school_admin')) {
      document.title = 'Fundile | School Administration';
      return;
    }

    document.title = 'Fundile | Curriculum-Aligned Learning Assistant';
  }, [effectiveCurrentUser?.curriculum, effectiveRole, selectedCurriculumKey]);

  // Add custom CSS for scrollbar hiding
  useEffect(() => {
    const style = document.createElement('style');
    style.textContent = `
            .scrollbar-hide {
                -ms-overflow-style: none;
                scrollbar-width: none;
            }
            .scrollbar-hide::-webkit-scrollbar {
                display: none;
            }
        `;
    document.head.appendChild(style);
    return () => document.head.removeChild(style);
  }, []);

  // Initialize hooks with data from App.jsx
  useEffect(() => {
    setAllCurricula(curriculumShell);
  }, [setAllCurricula]);


  const updateHelperNavigationLabel = useCallback((newLabel) => {
    setNavigationStack(prevStack => prevStack.map(item =>
      item.view === 'curriculum_helper' ? { ...item, label: newLabel } : item
    ));
  }, [setNavigationStack]);

  // --- getAgentResponse (LLM disabled until backend provider is configured) ---
  const getAgentResponse = useCallback(async (input, history) => {
    // The LLM agent is not active yet. Return a friendly message so the UI
    // does not break, and log the request for later review.
    console.log('[getAgentResponse] LLM not configured. Input:', input);
    return 'The AI tutor is not available right now. Please review the memo and marking points shown after you submit your answer.';
  }, []);


  // --- Navigation Helper Functions ---
  const addViewToStack = useCallback((newView, label, data = {}) => {
    setNavigationStack(prev => [...prev, { view: newView, label: label, data: data }]);
    setView(newView);
  }, []);
  const {
    handleAnswerInput,
    handleAssignmentSubmit,
    handleAttempt,
    handleMathInput,
    handleStartAssignment,
    handleSubmit,
    handleToggleMathStructure,
  } = useWorkspaceSubmissionFlow({
    activeAssignment,
    activeEditableRef,
    activeTopic,
    addViewToStack,
    allCurricula,
    chatHistory,
    currentUser,
    dbService,
    getAgentResponse,
    numbersMatchForCurrency,
    parseFlexibleNumber,
    practiceQuestions,
    processMathematicalContent,
    selectedGrade,
    selectedSubject,
    setActiveAssignment,
    setActiveEditableRef,
    setActiveTopic,
    setChatHistory,
    setLoading,
    setMessage,
    setPracticeQuestions,
    setSelectedCurriculumKey,
    setSelectedGrade,
    setSelectedSubject,
    setView,
    setWorkspaceMode,
    shouldUseMathStructure,
  });
  const {
    addQuestionToChat,
    handleContinueProblem,
    handleMarkStrugglingProblemSolved,
    handleSendFreeformQuery,
    handleStrugglingProblem,
    updateAnswerInChat,
  } = useFreeformProblemFlow({
    addViewToStack,
    allCurricula,
    chatHistories,
    currentProblemThreadId,
    currentUser,
    dbService,
    getAgentResponse,
    loading,
    selectedCurriculumKey,
    selectedFreeformTopic,
    selectedGrade,
    selectedSubject,
    setChatHistories,
    setCurrentProblemThreadId,
    setFreeformAnswer,
    setLoading,
    setMessage,
    setSelectedCurriculumKey,
    setSelectedFreeformTopic,
    setSelectedGrade,
    setSelectedSubject,
    setWorkspaceMode,
  });

  const handleExplainMistake = useCallback(async (question) => {
    if (!getAgentResponse || !addQuestionToChat || !updateAnswerInChat) return;

    const contextMessage = `I got this question wrong. Please explain my mistake.\n\nQuestion: "${question.question_text}"\n\nMy Answer: ${JSON.stringify(question.studentAnswer || question.answer)}\n\nFeedback: ${question.feedback?.content || 'No feedback provided.'}`;

    const questionId = addQuestionToChat(contextMessage);
    setWorkspaceMode('freeform');

    try {
      const newAIAnswer = await getAgentResponse(contextMessage, []);
      updateAnswerInChat(questionId, newAIAnswer, false);
    } catch (error) {
      console.error('Error explaining mistake:', error);
      updateAnswerInChat(questionId, 'Sorry, I could not generate an explanation right now.', false);
    }
  }, [addQuestionToChat, getAgentResponse, setWorkspaceMode, updateAnswerInChat]);

  const handleNavigateBack = useCallback(() => {
    if (navigationStack.length > 1) {
      const newStack = navigationStack.slice(0, navigationStack.length - 1);
      setNavigationStack(newStack);
      const newView = newStack[newStack.length - 1].view;
      setView(newView);
      if (shouldResetSelectionForView(newView)) {
        setSelectedCurriculumKey(null);
        setSelectedGrade(null);
        setSelectedSubject(null);
        setActiveTopic(null);
      }
    } else {
      setView('curriculum');
      setNavigationStack(getCurriculumRootNavigationStack());
      setSelectedCurriculumKey(null);
      setSelectedGrade(null);
      setSelectedSubject(null);
      setActiveTopic(null);
    }

    if (isCurriculumPageVisible && navigationStack[navigationStack.length - 2]?.view !== 'curriculum_helper') {
      setIsCurriculumPageVisible(false);
    }
  }, [
    isCurriculumPageVisible,
    navigationStack,
    setActiveTopic,
    setIsCurriculumPageVisible,
    setNavigationStack,
    setSelectedCurriculumKey,
    setSelectedGrade,
    setSelectedSubject,
    setView,
  ]);

  const studentContentProps = {
    components: {
      MySavedProblemsViewComponent: MySavedProblemsView,
    },
    data: {
      activeAssignment,
      activeEditableRef,
      activeTopic,
      allCurricula,
      chatHistories,
      currentProblemThreadId,
      freeformAnswer,
      freeformWorkAreaRef,
      isCurriculumPageVisible,
      isKeypadVisible,
      loading,
      navigationStack,
      practiceQuestions,
      selectedCurriculumKey,
      selectedFreeformTopic,
      selectedGrade,
      selectedSubject,
      view,
      workspaceMode,
    },
    actions: {
      setActiveEditableRef,
      setActiveTopic,
      setFreeformAnswer,
      setIsCurriculumPageVisible,
      setIsKeypadVisible,
      setLoading,
      setMessage,
      setNavigationStack,
      setPracticeQuestions,
      setSelectedCurriculumKey,
      setSelectedFreeformTopic,
      setSelectedGrade,
      setSelectedSubject,
      setView,
      setWorkspaceMode,
      updateHelperNavigationLabel,
    },
    handlers: {
      addQuestionToChat,
      handleAnswerInput,
      handleAssignmentSubmit,
      handleAttempt,
      handleContinueProblem,
      handleExplainMistake,
      handleMarkStrugglingProblemSolved,
      handleSendFreeformQuery,
      handleStartAssignment,
      handleStrugglingProblem,
      handleSubmit,
      handleToggleMathStructure,
      onManageSubscriptionPage: handleNavigateToSubscriptionPage,
      updateAnswerInChat,
    },
    services: {
      currentUser: effectiveCurrentUser,
      dbService,
      getAgentResponse,
      storage,
    },
  };

  const roleContentProps = {
    auth: {
      auth,
      authLoading,
    },
    routing: {
      effectiveCurrentUser,
      effectiveRole,
    },
    parentProps: {
      onLaunchLearnerWorkspace: handleLaunchLearnerWorkspace,
    },
    roleState: {
      adminView,
      setAdminView,
      setTeacherView,
      teacherView,
      schoolAdminView,
      setSchoolAdminView,
    },
    services: {
      db,
      dbService,
    },
    studentContentProps,
  };

  const shellProps = {
    brandPalette,
    currentUser: effectiveCurrentUser,
    currentView: view,
    handleMathInput,
    isKeypadVisible,
    message,
    navigationStack,
    onCloseMessage: () => setMessage(''),
    onMarkAllNotificationsRead: async () => {
      if (!dbService || !effectiveCurrentUser?.uid) {
        return;
      }

      const unreadNotifications = studentNotifications.filter((notification) => !notification.isRead);
      if (!unreadNotifications.length) {
        return;
      }

      try {
        await Promise.all(
          unreadNotifications.map((notification) => updateDoc(
            doc(dbService, 'users', effectiveCurrentUser.uid, 'notifications', notification.id),
            {
              isRead: true,
              readAt: serverTimestamp(),
            }
          ))
        );
      } catch (error) {
        console.error('Error marking notifications as read:', error);
      }
    },
    onLogout: handleAppLogout,
    onNavigateHome: handleNavigateHome,
    onMarkNotificationRead: async (notificationId) => {
      if (!dbService || !effectiveCurrentUser?.uid || !notificationId) {
        return;
      }

      try {
        await updateDoc(doc(dbService, 'users', effectiveCurrentUser.uid, 'notifications', notificationId), {
          isRead: true,
          readAt: serverTimestamp(),
        });
      } catch (error) {
        console.error('Error marking notification as read:', error);
      }
    },
    onNavigateBack: handleNavigateBack,
    onStartAssignment: handleStartAssignment,
    pendingAssignments,
    studentNotifications,
    setBrandPalette,
    setCurrentView: setView,
    setIsKeypadVisible,
    setSuperAdminMode: handleSetSuperAdminMode,
    superAdminMode,
    setSuperAdminTier,
    superAdminTier,
  };


  // --- useEffect for Student-Specific Logic After Authentication ---
  useEffect(() => {
    // This effect runs when authentication state changes
    if (effectiveCurrentUser && dbService && hasVerifiedAccess) {
      // Handle student navigation after login
      if (effectiveCurrentUser.role === 'student' && !effectiveCurrentUser.isSuperAdmin) {
        // Set curriculum and grade from user preferences
        if (effectiveCurrentUser.curriculum && effectiveCurrentUser.grade) {
          setSelectedCurriculumKey(effectiveCurrentUser.curriculum);
          setSelectedGrade(Number(effectiveCurrentUser.grade));
          // Navigate directly to subject selection
          setView('subject');
          setNavigationStack([
            { view: 'subject', label: 'Subjects', data: { curriculumKey: effectiveCurrentUser.curriculum, grade: Number(effectiveCurrentUser.grade) } }
          ]);
        }

        setPendingAssignments([]);
      }
    } else if (effectiveCurrentUser && !hasVerifiedAccess) {
      setPendingAssignments([]);
    } else if (!effectiveCurrentUser) {
      // User is signed out
      setPendingAssignments([]);
    }
  }, [effectiveCurrentUser, dbService, hasVerifiedAccess, setSelectedCurriculumKey, setSelectedGrade, setView, setNavigationStack, setPendingAssignments]);

  // --- useEffect for Fetching General Chat History (from chat_rooms) ---
  useEffect(() => {
    // Only run this hook if the database service is available, a chatRoomId is set, and chat permissions are available
    if (!dbService || !chatRoomId || !chatPermissionsAvailable) {
      return;
    }

    console.log(`Fetching messages for chat room: ${chatRoomId}`);

    const messagesCollection = collection(dbService, 'chat_rooms', chatRoomId, 'messages');
    const q = query(messagesCollection, orderBy("timestamp"));

    const unsubscribe = onSnapshot(q, (querySnapshot) => {
      const fetchedMessages = querySnapshot.docs.map(doc => ({
        id: doc.id,
        ...doc.data()
      }));
      setMessages(fetchedMessages);
    }, (error) => {
      console.error("Error fetching messages:", error);
      // Handle Firebase permissions error gracefully
      if (error.code === 'permission-denied') {
        console.warn("Chat functionality is not available due to permissions. Continuing without chat.");
        setMessages([]);
        setChatPermissionsAvailable(false);
      } else {
        console.error("Unexpected error fetching messages:", error);
      }
    });

    return () => unsubscribe();
  }, [dbService, chatRoomId, chatPermissionsAvailable]); // This hook now depends on dbService, chatRoomId, and chatPermissionsAvailable


  // --- Other Handlers ---

  // Show splash screen first
  if (showSplash) {
    return <SplashScreen onComplete={handleSplashComplete} />;
  }

  if (topLevelPage === 'sandbox' || (typeof window !== 'undefined' && (window.location.search.includes('sandbox') || window.location.pathname === '/sandbox'))) {
    if (!isStandaloneApp() && effectiveCurrentUser) {
      return (
        <div className="h-[100dvh] md:min-h-screen flex flex-col bg-slate-900 overflow-hidden md:overflow-visible">
          <div className="hidden md:block">
            <Header
              currentUser={effectiveCurrentUser}
              onLogout={handleAppLogout}
              onNavigateToSubscription={handleNavigateToSubscriptionPage}
              onStartTrial={handleNavigateToSubscriptionPage}
              onMarkAllNotificationsRead={shellProps.onMarkAllNotificationsRead}
              onMarkNotificationRead={shellProps.onMarkNotificationRead}
              pendingAssignments={pendingAssignments}
              studentNotifications={studentNotifications}
              superAdminMode={superAdminMode}
              setSuperAdminMode={setSuperAdminMode}
              superAdminTier={superAdminTier}
              setSuperAdminTier={setSuperAdminTier}
              brandPalette={brandPalette}
              setBrandPalette={setBrandPalette}
              onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
            />
          </div>
          <div className="flex-1 min-h-0">
            <LearnerAppContainer 
              isSandboxMode={true} 
              currentUser={effectiveCurrentUser} 
              onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
            />
          </div>
          <PersonaSwitcherModal
            isOpen={showPersonaSwitcher}
            onClose={() => setShowPersonaSwitcher(false)}
            currentUser={effectiveCurrentUser}
            onSwitchPersona={handleSwitchPersona}
          />
        </div>
      );
    }
    return (
      <>
        <LearnerAppContainer 
          isSandboxMode={true} 
          currentUser={effectiveCurrentUser} 
          onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
          onLogout={handleAppLogout}
          superAdminMode={superAdminMode}
          setSuperAdminMode={setSuperAdminMode}
          superAdminTier={superAdminTier}
          setSuperAdminTier={setSuperAdminTier}
        />
        <PersonaSwitcherModal
          isOpen={showPersonaSwitcher}
          onClose={() => setShowPersonaSwitcher(false)}
          currentUser={effectiveCurrentUser}
          onSwitchPersona={handleSwitchPersona}
        />
      </>
    );
  }

  if (topLevelPage === 'subscribe') {
    return <SubscriptionPage currentUser={effectiveCurrentUser} storage={storage} db={db} targetGrade={selectedGrade || effectiveCurrentUser?.grade} onNavigateHome={effectiveCurrentUser ? handleNavigateToDashboard : handleNavigateHome} onNavigateSignIn={handleNavigateSignIn} onNavigateSignUp={handleNavigateSignUp} onNavigateApp={handleNavigateToDashboard} />;
  }

  if (topLevelPage === 'privacy') {
    return <PrivacyStatementView onBackToLanding={handleNavigateHome} />;
  }

  if (shouldRenderStandaloneLandingPage) {
    return <LandingPage db={db} onGetStarted={handleNavigateSignUp} onSignIn={handleNavigateSignIn} onViewSubscription={handleNavigateToSubscriptionPage} onNavigatePrivacy={handleNavigatePrivacy} palette={brandPalette} authService={authHook.authService} currentUser={effectiveCurrentUser} />;
  }

  if (!effectiveCurrentUser) {
    return (
      <AuthScreen 
        auth={auth} 
        db={db} 
        initialMode={authMode} 
        onNavigateHome={handleNavigateHome} 
        onToggleMode={() => navigateToRoutePage(authMode === 'signin' ? 'signup' : 'signin')} 
        onNavigateToSubscription={handleNavigateToSubscriptionPage} 
        statusMessage={authStatusMessage} 
      />
    );
  }

  if (!hasVerifiedAccess) {
    return <VerificationScreen auth={auth} currentUser={effectiveCurrentUser} onContinueToDashboard={handleVerificationComplete} onLogout={handleAppLogout} statusMessage={authStatusMessage} />;
  }

  // If student: render the modern unified LearnerAppContainer (desktop folder tabs on PC, mobile bottom carousel on phone)
  if (effectiveRole === 'student' || !effectiveRole) {
    const parentReturnRibbon = parentDualUseChild ? (
      <aside aria-label="Dual-Use Mode Active" className="bg-gradient-to-r from-[#13519C] via-[#0f4280] to-[#13519C] border-b border-blue-400/40 text-white px-4 py-2 flex items-center justify-between shadow-md text-xs shrink-0 z-50">
        <div className="flex items-center gap-2">
          <span className="bg-[#FF9100] text-slate-950 font-extrabold px-2 py-0.5 rounded text-[10px] uppercase tracking-wider shadow-xs">
            Dual-Use Account Active
          </span>
          <span className="font-medium text-slate-100 hidden sm:inline">
            Guardian Account hosting learner:
          </span>
          <span className="font-bold text-white bg-white/20 px-2 py-0.5 rounded text-xs">
            {parentDualUseChild.name} ({parentDualUseChild.grade})
          </span>
        </div>
        <button
          type="button"
          data-testid="btn-return-guardian-portal"
          onClick={handleExitParentDualUse}
          className="bg-white text-[#13519C] hover:bg-slate-100 font-bold px-3 py-1.5 rounded-xl text-xs flex items-center gap-1.5 transition shadow-xs cursor-pointer active:scale-95"
        >
          <span>👨‍👩‍👧 Return to Guardian Portal</span>
        </button>
      </aside>
    ) : null;

    if (!isStandaloneApp()) {
      return (
        <div className="h-[100dvh] md:min-h-screen flex flex-col bg-slate-900 overflow-hidden md:overflow-visible">
          {parentReturnRibbon}
          <div className="hidden md:block">
            <Header
              currentUser={effectiveCurrentUser}
              onLogout={handleAppLogout}
              onNavigateHome={handleNavigateHome}
              onNavigateToSubscription={handleNavigateToSubscriptionPage}
              onStartTrial={handleNavigateToSubscriptionPage}
              onMarkAllNotificationsRead={shellProps.onMarkAllNotificationsRead}
              onMarkNotificationRead={shellProps.onMarkNotificationRead}
              pendingAssignments={pendingAssignments}
              studentNotifications={studentNotifications}
              superAdminMode={superAdminMode}
              setSuperAdminMode={handleSetSuperAdminMode}
              superAdminTier={superAdminTier}
              setSuperAdminTier={setSuperAdminTier}
              brandPalette={brandPalette}
              setBrandPalette={setBrandPalette}
              onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
            />
          </div>
          <div className="flex-1 min-h-0">
            <LearnerAppContainer 
              isSandboxMode={false} 
              currentUser={effectiveCurrentUser} 
              onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
              onLogout={handleAppLogout}
              superAdminMode={superAdminMode}
              setSuperAdminMode={handleSetSuperAdminMode}
              superAdminTier={superAdminTier}
              setSuperAdminTier={setSuperAdminTier}
            />
          </div>
          <PersonaSwitcherModal
            isOpen={showPersonaSwitcher}
            onClose={() => setShowPersonaSwitcher(false)}
            currentUser={effectiveCurrentUser}
            onSwitchPersona={handleSwitchPersona}
          />
        </div>
      );
    }

    return (
      <div className="h-[100dvh] flex flex-col overflow-hidden">
        {parentReturnRibbon}
        <div className="flex-1 min-h-0">
          <LearnerAppContainer 
            isSandboxMode={false} 
            currentUser={effectiveCurrentUser} 
            onOpenPersonaSwitcher={() => setShowPersonaSwitcher(true)}
            onLogout={handleAppLogout}
            superAdminMode={superAdminMode}
            setSuperAdminMode={handleSetSuperAdminMode}
            superAdminTier={superAdminTier}
            setSuperAdminTier={setSuperAdminTier}
          />
        </div>
        <PersonaSwitcherModal
          isOpen={showPersonaSwitcher}
          onClose={() => setShowPersonaSwitcher(false)}
          currentUser={effectiveCurrentUser}
          onSwitchPersona={handleSwitchPersona}
        />
      </div>
    );
  }

  return (
    <>
      <AppShell 
        shellProps={{ 
          ...shellProps, 
          onOpenPersonaSwitcher: () => setShowPersonaSwitcher(true),
          children: <RenderRoleContent roleContentProps={roleContentProps} /> 
        }} 
      />
      <PersonaSwitcherModal
        isOpen={showPersonaSwitcher}
        onClose={() => setShowPersonaSwitcher(false)}
        currentUser={effectiveCurrentUser}
        onSwitchPersona={handleSwitchPersona}
      />
    </>
  );
}
