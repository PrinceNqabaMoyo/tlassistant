// React imports
import React, { useState, useEffect, useRef, useCallback } from 'react';

// Third-party library imports
import { doc, setDoc, getDoc, collection, onSnapshot, orderBy, addDoc, serverTimestamp, query, where, getDocs, deleteDoc } from 'firebase/firestore';
import { BookOpen, ChevronLeft, User, Target, BarChart2, PenTool, ClipboardEdit, BrainCircuit, FileText, GraduationCap, BookCopy, CheckSquare, Loader2, UserPlus, Edit, Send, FileSignature, Book, Users, Settings, LogOut, Eye, MessageSquare, UserCheck, Briefcase, FunctionSquare, FilePlus, AlertTriangle, PlusCircle, Bell, Rows, MessageCircle, CheckCircle, Trophy, X } from 'lucide-react';
import EnhancedMathKeypad from './components/EnhancedMathKeypad';

// Local imports
import { curriculumData } from './curriculumData';

// Import extracted components
import AdminTokenUsageDisplay from './components/ui/AdminTokenUsageDisplay';
import MessageModal from './components/ui/MessageModal';
import Notifications from './components/ui/Notifications';
import Header from './components/ui/Header';
import AuthScreen from './components/auth/AuthScreen';

// Import extracted form components
import {
  StudentRoleSelector,
  CurriculumSelector,
  GradeSelector,
  SubjectDashboard,
  StudyModeSelector,
  TeacherDashboard,
  StudentManagement,
  QuestionGeneration,
  AdminDashboard,
  UserManagement,
  SystemAnalytics,
  TableRenderer,
  TableInput,
  MoneyInput
} from './components/forms';

// Import extracted source document components
import {
  CashReceiptsJournalInput,
  CashPaymentsJournalInput,
  DebtorsJournalInput,
  CreditorsJournalInput,
  GeneralLedgerInput,
  TrialBalanceInput,
  DebtorsLedgerInput,
  CreditorsLedgerInput,
  AccountingEquationTableInput,
  DepositSlipInput,
  ChequeInput,
  ReceiptInput,
  CashInvoiceInput,
  IncomeStatementInput,
  TradingIncomeStatementInput
} from './components/sourceDocuments';

// Import new math components
import {
  NumberLineInput,
  FractionVisualizer,
  GeometricConstructionInput,
  StatisticalAnalysisInput,
  CoordinatePlaneInput,
  ProbabilitySimulator,
  AlgebraicExpressionBuilder,
  VectorCalculator,
  MatrixCalculator,
  CalculusTools,
  MathematicalInstruments,
  BarChartInput,
  LineGraphInput,
  PieChartInput,
  QuadraticGraphInput,
  HyperbolicFunctionInput,
  CircleInput,
  TrigonometricFunctionInput
} from './components/math';

// Import thumbnail test page
import ThumbnailTestPage from './components/math/ThumbnailTestPage';
// Import integration demo
import IntegrationDemo from './components/math/IntegrationDemo';
// Import geometry backend test
import GeometryTestAccess from './components/math/geometry/GeometryTestAccess';

// Import extracted components
import { Workspace } from './components/workspace';
import { CurriculumHelper } from './components/curriculum';
import { StudentView } from './components/student';
import { TeacherView } from './components/teacher';
import { AdminView } from './components/admin';

// Import custom hooks
import {
  useAuthentication,
  useCoreState,
  useCurriculumNavigation,
  useWorkspaceUI,
  useChatFunctionality,
  useFreeformTopics,
  useTeacherAdminViews,
  useAssignmentsPractice
} from './hooks';

// Import extracted utilities and constants
import { convertJournalToText } from './utils/journalUtils';
import { fallbackSourceDocuments, firebaseConfig } from './constants/sourceDocuments';

// Import new UI components
import FundileLogo from './components/ui/FundileLogo';
import GraduationCapSplash from './components/ui/GraduationCapSplash';
import SplashScreen from './components/ui/SplashScreen';
import LandingPage from './components/ui/LandingPage';

// Import API utilities
import { submitOrderdAnswer, listSubmissions } from './utils/api';

// Import accounting validation utilities
import {
  accountingValidationEngine,
  validateCashReceipts,
  validateCashPayments,
  validateTrialBalance,
  validateDebtorsLedger,
  validateCreditorsLedger
} from './utils/accountingValidation';

// Import curriculum helper utilities
import {
  journalQuestionTemplate,
  questionBank,
  customizeQuestion,
  generateJournalQuestion,
  generateBusinessScenario
} from './utils/curriculumHelpers';


// --- Constants & Configuration ---

// Source Documents Repository - Now imported from constants/sourceDocuments.js

// App Configuration - Now imported from constants/sourceDocuments.js

// API functions have been moved to src/utils/api.js

// --- Example usage in component ---
function SubmissionPanel({ studentId, assignmentId, questionId, answerSequence, authToken }) {
  const [submitResult, setSubmitResult] = useState(null);
  const [submissions, setSubmissions] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    const result = await submitOrderdAnswer({ studentId, assignmentId, questionId, answerSequence, authToken });
    setSubmitResult(result);
    setLoading(false);
  };

  const handleListSubmissions = async () => {
    setLoading(true);
    const result = await listSubmissions({ assignmentId, studentId, authToken });
    setSubmissions(result.submissions || []);
    setLoading(false);
  };

  return (
    <div>
      <button onClick={handleSubmit} disabled={loading}>Submit Answer</button>
      {submitResult && (
        <div>
          <h4>Submission Result</h4>
          <pre>{JSON.stringify(submitResult, null, 2)}</pre>
        </div>
      )}
      <button onClick={handleListSubmissions} disabled={loading}>List My Submissions</button>
      {submissions.length > 0 && (
        <div>
          <h4>My Submissions</h4>
          <ul>
            {submissions.map(sub => (
              <li key={sub.submissionId}>
                <pre>{JSON.stringify(sub, null, 2)}</pre>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

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

// --- Text Processing & Mathematical Content Functions ---
const getPlainTextFromHtml = (htmlString) => {
  if (!htmlString) return "";
  const tempDiv = document.createElement('div');
  tempDiv.innerHTML = htmlString
    .replace(/<br\s*\/?>/gi, ", ") // Flatten line breaks to comma and space
    .replace(/<p>|<\/p>|<div>|<\/div>/g, ", ")
    .replace(/&nbsp;/g, ' ');
  let text = tempDiv.textContent || tempDiv.innerText || "";
  return text.replace(/\s+/g, ' ').trim(); // Clean up extra spaces
};

// Enhanced mathematical content detection and formatting
const detectMathStructure = (content) => {
  if (typeof content !== 'string') return false;

  const mathPatterns = [
    /[=+\-*/^√∫∑∏]/g,           // Mathematical operators
    /[a-zA-Z]\d+/g,              // Variables with subscripts
    /\([^)]*\)/g,                // Parentheses expressions
    /\d+\.\d+/g,                 // Decimal numbers
    /[≤≥≠≈]/g,                   // Mathematical symbols
    /\b\d+\b/g,                  // Whole numbers
    /[a-zA-Z]\s*[=]\s*[a-zA-Z0-9]/g, // Variable assignments
    /\b(sin|cos|tan|log|ln|exp)\b/gi, // Mathematical functions
    /\b(area|perimeter|volume|surface area|circumference)\b/gi, // Mathematical concepts
    /\b(percentage|ratio|proportion|fraction)\b/gi, // Mathematical terms
    /\b(profit|loss|cost|price|discount|tax)\b/gi, // Business math terms
    /\b(velocity|acceleration|force|mass|energy)\b/gi, // Physics math terms
    /\b(concentration|molarity|density|pressure)\b/gi, // Chemistry math terms
    /\b(cell|organism|population|growth rate)\b/gi, // Biology math terms
    /\b(historical|period|century|decade|era)\b/gi, // History math terms
    /\b(latitude|longitude|distance|scale|map)\b/gi, // Geography math terms
    /\b(economic|GDP|inflation|interest rate|exchange rate)\b/gi // Economics math terms
  ];

  const mathScore = mathPatterns.reduce((score, pattern) => {
    return score + (content.match(pattern) || []).length;
  }, 0);

  // Lower threshold since all subjects have math content
  return mathScore > 1;
};

const formatMathematicalContent = (content) => {
  if (!detectMathStructure(content)) {
    return content; // Return as-is for non-math content
  }

  // Enhanced formatting for mathematical expressions
  let formatted = content
    // Mathematical operations and expressions
    .replace(/([=+\-*/^])/g, '\n$1 ')           // New line before operators
    .replace(/([a-zA-Z]\d+)/g, '\n$1')          // New line for variables
    .replace(/(\d+\.\d+)/g, '\n$1')             // New line for decimals
    .replace(/(\([^)]*\))/g, '\n$1')            // New line for expressions
    .replace(/(\b\d+\b)/g, '\n$1')              // New line for whole numbers

    // Mathematical functions and concepts
    .replace(/\b(sin|cos|tan|log|ln|exp)\b/gi, '\n$1') // Math functions
    .replace(/\b(area|perimeter|volume|surface area|circumference)\b/gi, '\n$1') // Math concepts
    .replace(/\b(percentage|ratio|proportion|fraction)\b/gi, '\n$1') // Math terms

    // Business and economics terms
    .replace(/\b(profit|loss|cost|price|discount|tax)\b/gi, '\n$1') // Business terms
    .replace(/\b(GDP|inflation|interest rate|exchange rate)\b/gi, '\n$1') // Economics terms

    // Science terms
    .replace(/\b(velocity|acceleration|force|mass|energy)\b/gi, '\n$1') // Physics terms
    .replace(/\b(concentration|molarity|density|pressure)\b/gi, '\n$1') // Chemistry terms
    .replace(/\b(cell|organism|population|growth rate)\b/gi, '\n$1') // Biology terms

    // Other subject terms
    .replace(/\b(historical|period|century|decade|era)\b/gi, '\n$1') // History terms
    .replace(/\b(latitude|longitude|distance|scale|map)\b/gi, '\n$1') // Geography terms

    // Comma and list formatting
    .replace(/, /g, '\n')                        // Comma to line break
    .replace(/;\s*/g, '\n')                      // Semicolon to line break
    .replace(/\.\s+/g, '.\n')                    // Period to line break for new thoughts

    // Clean up formatting
    .replace(/\n+/g, '\n')                       // Clean up multiple line breaks
    .replace(/\n\s*\n\s*\n/g, '\n\n')           // Limit consecutive empty lines
    .trim();

  return formatted;
};

const shouldUseMathStructure = (subject, content) => {
  // All subjects have mathematical content to some degree
  const hasMathContent = detectMathStructure(content);

  // Always use math structure if mathematical content is detected
  return hasMathContent;
};

const applyAllTextFormatting = (text, subject = null) => {
  if (typeof text !== 'string') return '';

  // Use enhanced mathematical formatting with subject awareness
  return processMathematicalContent(text, subject);
};

// --- Caching & Performance Functions ---

// Token usage tracking and optimization
const tokenUsageTracker = {
  totalTokens: 0,
  aiCalls: 0,
  cachedResponses: 0,

  logAICall: (tokens) => {
    tokenUsageTracker.totalTokens += tokens || 0;
    tokenUsageTracker.aiCalls += 1;
    console.log(`AI Call #${tokenUsageTracker.aiCalls}: ${tokens || 'unknown'} tokens. Total: ${tokenUsageTracker.totalTokens}`);
  },

  logCachedResponse: () => {
    tokenUsageTracker.cachedResponses += 1;
    console.log(`Cached response used. Total cached: ${tokenUsageTracker.cachedResponses}`);
  },

  getStats: () => ({
    totalTokens: tokenUsageTracker.totalTokens,
    aiCalls: tokenUsageTracker.aiCalls,
    cachedResponses: tokenUsageTracker.cachedResponses,
    savings: tokenUsageTracker.cachedResponses * 100 // Estimated token savings
  }),

  reset: () => {
    tokenUsageTracker.totalTokens = 0;
    tokenUsageTracker.aiCalls = 0;
    tokenUsageTracker.cachedResponses = 0;
  }
};

// Tutor Content Cache and Generator
const tutorContentCache = new Map();

const tutorContentGenerator = {
  generateTutorStructure: async (subject, grade, topic, subtopic, getAgentResponse) => {
    const cacheKey = `tutor_${subject}_${grade}_${topic}_${subtopic || 'main'}`;

    // Check cache first
    const cached = tutorContentCache.get(cacheKey);
    if (cached && Date.now() < cached.expiryDate) {
      tokenUsageTracker.logCachedResponse();
      return cached.content;
    }

    // Generate new structured tutoring content
    const prompt = `Create a structured tutoring guide for Grade ${grade} ${subject} on "${topic}${subtopic ? ': ' + subtopic : ''}". Include:
    1. Step-by-step explanation
    2. 3-5 worked examples
    3. Practice problems with solutions
    4. Common misconceptions
    5. Key formulas/concepts
    Return as structured JSON.`;

    const aiResponse = await getAgentResponse(prompt, []);
    const tutorContent = JSON.parse(aiResponse);

    // Cache for 3 months
    const threeMonthsFromNow = Date.now() + (90 * 24 * 60 * 60 * 1000);
    tutorContentCache.set(cacheKey, {
      content: tutorContent,
      expiryDate: threeMonthsFromNow,
      generationDate: Date.now()
    });

    return tutorContent;
  },

  getCachedTutorContent: (subject, grade, topic, subtopic) => {
    const cacheKey = `tutor_${subject}_${grade}_${topic}_${subtopic || 'main'}`;
    const cached = tutorContentCache.get(cacheKey);

    if (cached && Date.now() < cached.expiryDate) {
      return cached.content;
    }

    return null;
  }
};

// Scheduled Generation System
const scheduledGenerationSystem = {
  lastGenerationDate: new Map(),

  needsInitialGeneration: (subject, grade, topic, subtopic) => {
    const key = `${subject}_${grade}_${topic}_${subtopic || 'main'}`;
    const lastGen = scheduledGenerationSystem.lastGenerationDate.get(key);

    if (!lastGen) return true;

    // Check if it's been more than a month since last generation
    const oneMonthAgo = Date.now() - (30 * 24 * 60 * 60 * 1000);
    return lastGen < oneMonthAgo;
  },

  markGenerated: (subject, grade, topic, subtopic) => {
    const key = `${subject}_${grade}_${topic}_${subtopic || 'main'}`;
    scheduledGenerationSystem.lastGenerationDate.set(key, Date.now());
  },

  // Auto-generate questions for all active subjects/topics
  generateAllActiveQuestions: async (getAgentResponse) => {
    const activeSubjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Accounting', 'Economics', 'History', 'Geography'];
    const activeGrades = [10, 11, 12];
    const activeTopics = {
      'Mathematics': ['Algebra', 'Geometry', 'Calculus', 'Statistics'],
      'Physics': ['Mechanics', 'Electricity', 'Waves', 'Thermodynamics'],
      'Chemistry': ['Organic Chemistry', 'Inorganic Chemistry', 'Physical Chemistry'],
      'Biology': ['Cell Biology', 'Genetics', 'Ecology', 'Human Biology'],
      'Accounting': ['Financial Accounting', 'Cost Accounting', 'Management Accounting'],
      'Economics': ['Microeconomics', 'Macroeconomics', 'International Trade'],
      'History': ['World History', 'African History', 'Modern History'],
      'Geography': ['Physical Geography', 'Human Geography', 'Environmental Geography']
    };

    for (const subject of activeSubjects) {
      for (const grade of activeGrades) {
        for (const topic of activeTopics[subject] || []) {
          if (scheduledGenerationSystem.needsInitialGeneration(subject, grade, topic)) {
            try {
              await curriculumQuestionGenerator.generateCurriculumQuestions(subject, grade, topic, null, getAgentResponse);
              scheduledGenerationSystem.markGenerated(subject, grade, topic);
              console.log(`Generated questions for ${grade} ${subject} - ${topic}`);
            } catch (error) {
              console.error(`Failed to generate questions for ${grade} ${subject} - ${topic}:`, error);
            }
          }
        }
      }
    }
  }
};

// --- UI Components ---

// --- Curriculum Question Management System ---

// Shared Curriculum Question Bank System
const curriculumQuestionBank = new Map();

// Question metadata structure
const questionMetadata = {
  generationDate: null,
  expiryDate: null,
  questionCount: 0,
  topics: [],
  lastRefreshed: null
};

// Generate cache key for shared curriculum questions
const generateCurriculumCacheKey = (subject, grade, topic, subtopic = null) => {
  return `curriculum_${subject}_${grade}_${topic}_${subtopic || 'main'}`;
};

// Get shared curriculum questions (available to all students)
const getCurriculumQuestions = (subject, grade, topic, subtopic = null) => {
  const cacheKey = generateCurriculumCacheKey(subject, grade, topic, subtopic);
  const cached = curriculumQuestionBank.get(cacheKey);

  if (cached && Date.now() < cached.expiryDate) {
    tokenUsageTracker.logCachedResponse();
    return cached.questions;
  }

  return null;
};

// Cache curriculum questions for all students
const cacheCurriculumQuestions = (subject, grade, topic, subtopic, questions) => {
  const cacheKey = generateCurriculumCacheKey(subject, grade, topic, subtopic);
  const now = Date.now();
  const threeMonthsFromNow = now + (90 * 24 * 60 * 60 * 1000); // 3 months

  curriculumQuestionBank.set(cacheKey, {
    questions: questions,
    generationDate: now,
    expiryDate: threeMonthsFromNow,
    questionCount: questions.length,
    topics: [topic, subtopic].filter(Boolean),
    lastRefreshed: now
  });
}

// Helper function to check admin and email verification
function isAdmin(user) {
  return (
    user &&
    user.email === "admin@fundile.com" &&
    user.emailVerified
  );
}

// Check if questions need refresh (monthly)
const needsQuestionRefresh = (subject, grade, topic, subtopic = null) => {
  // Only show for verified admin
  if (!isAdmin(currentUser)) {
    return null;
  }

  const oneMonthAgo = Date.now() - (30 * 24 * 60 * 60 * 1000);
  return cached.lastRefreshed < oneMonthAgo;
};

// Scheduled question generation system
const scheduledQuestionGenerator = {
  // Generate questions for all active subjects/topics
  generateAllActiveQuestions: async (getAgentResponse) => {
    console.log('Starting scheduled question generation for all active curricula...');

    try {
      const activeCurricula = Object.keys(curriculumData);
      let totalGenerated = 0;

      for (const subject of activeCurricula) {
        for (const grade of Object.keys(curriculumData[subject])) {
          for (const topic of Object.keys(curriculumData[subject][grade])) {
            // Check if questions need generation
            if (needsQuestionRefresh(subject, grade, topic)) {
              console.log(`Generating questions for ${subject} Grade ${grade} - ${topic}`);

              const questions = await curriculumQuestionGenerator.generateCurriculumQuestions(
                subject, grade, topic, null, getAgentResponse
              );

              if (questions && questions.length > 0) {
                totalGenerated += questions.length;
                console.log(`Generated ${questions.length} questions for ${subject} Grade ${grade} - ${topic}`);
              }
            }
          }
        }
      }

      console.log(`Scheduled generation complete. Total questions generated: ${totalGenerated}`);
      return totalGenerated;
    } catch (error) {
      console.error('Error in scheduled question generation:', error);
      return 0;
    }
  },

  // Schedule monthly generation
  scheduleMonthlyGeneration: (getAgentResponse) => {
    // Run initial generation
    scheduledQuestionGenerator.generateAllActiveQuestions(getAgentResponse);

    // Set up monthly interval (30 days)
    setInterval(() => {
      scheduledQuestionGenerator.generateAllActiveQuestions(getAgentResponse);
    }, 30 * 24 * 60 * 60 * 1000);
  }
};

// Legacy individual caching (keeping for backward compatibility)
const questionCache = new Map();
const aiResponseCache = new Map();

const generateCacheKey = (subject, grade, topic, subtopic = null, difficulty = 'medium', type = 'questions') => {
  return `${type}_${subject}_${grade}_${topic}_${subtopic || 'main'}_${difficulty}`;
};

const getCachedQuestions = (subject, grade, topic, subtopic = null, difficulty = 'medium') => {
  const cacheKey = generateCacheKey(subject, grade, topic, subtopic, difficulty, 'questions');
  const cached = questionCache.get(cacheKey);

  if (cached && Date.now() - cached.timestamp < 24 * 60 * 60 * 1000) { // 24 hour cache
    tokenUsageTracker.logCachedResponse();
    return cached.questions;
  }

  return null;
};

const cacheQuestions = (subject, grade, topic, subtopic, difficulty, questions) => {
  const cacheKey = generateCacheKey(subject, grade, topic, subtopic, difficulty, 'questions');
  questionCache.set(cacheKey, {
    questions: questions,
    timestamp: Date.now(),
    metadata: { subject, grade, topic, subtopic, difficulty }
  });
};

const getCachedAIResponse = (prompt, context) => {
  const cacheKey = `ai_${prompt.substring(0, 100)}_${JSON.stringify(context).substring(0, 100)}`;
  const cached = aiResponseCache.get(cacheKey);

  if (cached && Date.now() - cached.timestamp < 60 * 60 * 1000) { // 1 hour cache
    tokenUsageTracker.logCachedResponse();
    return cached.response;
  }

  return null;
};

const cacheAIResponse = (prompt, context, response) => {
  const cacheKey = `ai_${prompt.substring(0, 100)}_${JSON.stringify(context).substring(0, 100)}`;
  aiResponseCache.set(cacheKey, {
    response: response,
    timestamp: Date.now(),
    metadata: { prompt: prompt.substring(0, 100), context: context }
  });
};

// Pre-built question templates to reduce AI calls
const questionTemplates = {
  mathematics: {
    algebra: [
      {
        question_text: "Solve the equation: 2x + 5 = 13",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Factorize the expression: x² - 4",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Simplify the expression: 3(x + 2) - 2(x - 1)",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Solve the quadratic equation: x² - 5x + 6 = 0",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ],
    geometry: [
      {
        question_text: "Calculate the area of a rectangle with length 8cm and width 6cm",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Find the circumference of a circle with radius 7cm",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Calculate the volume of a cube with side length 4cm",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ],
    trigonometry: [
      {
        question_text: "Find the value of sin(30°)",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "Calculate tan(45°)",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ]
  },
  accounting: {
    journals: [
      {
        question_text: "Record the following cash receipts in the cash receipts journal: Received R500 from customer A for services rendered",
        expected_answer_type: "cash_receipts_journal_data",
        table: null,
        shape: null,
        graph: null,
        journal_data: {
          companyName: "ABC Company",
          month: "January",
          journalNumber: "CR001"
        }
      },
      {
        question_text: "Record the following cash payment in the cash payments journal: Paid R300 to supplier B for office supplies",
        expected_answer_type: "cash_payments_journal_data",
        table: null,
        shape: null,
        graph: null,
        journal_data: {
          companyName: "ABC Company",
          month: "January",
          journalNumber: "CP001"
        }
      }
    ],
    trial_balance: [
      {
        question_text: "Prepare a trial balance from the following ledger balances",
        expected_answer_type: "table_data",
        table: {
          headers: ["Account", "Debit", "Credit"],
          rows: [
            ["Cash", "5000", ""],
            ["Accounts Receivable", "3000", ""],
            ["Accounts Payable", "", "2000"],
            ["Capital", "", "6000"]
          ]
        },
        shape: null,
        graph: null,
        journal_data: null
      }
    ]
  },
  "physical sciences": {
    mechanics: [
      {
        question_text: "Calculate the velocity of an object that travels 100m in 20 seconds",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      },
      {
        question_text: "A car accelerates from 0 to 60 km/h in 10 seconds. Calculate the acceleration",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ],
    electricity: [
      {
        question_text: "Calculate the current flowing through a circuit with voltage 12V and resistance 6Ω",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ]
  },
  "business studies": {
    marketing: [
      {
        question_text: "Explain the 4Ps of marketing with examples",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ],
    finance: [
      {
        question_text: "Calculate the profit margin if revenue is R1000 and costs are R700",
        expected_answer_type: "text",
        table: null,
        shape: null,
        graph: null,
        journal_data: null
      }
    ]
  }
};

// Smart curriculum question generator with shared caching
const curriculumQuestionGenerator = {
  // Generate questions for curriculum helper (shared across all students)
  generateCurriculumQuestions: async (subject, grade, topic, subtopic, getAgentResponse) => {
    // Check if we need to refresh questions (monthly)
    if (!needsQuestionRefresh(subject, grade, topic, subtopic)) {
      const existingQuestions = getCurriculumQuestions(subject, grade, topic, subtopic);
      if (existingQuestions) {
        return existingQuestions;
      }
    }

    // PRIORITY 1: Generate new questions via AI + RAG (15 questions per topic)
    try {
      const prompt = `Generate exactly 15 practice questions for Grade ${grade} ${subject} on "${topic}${subtopic ? ': ' + subtopic : ''}". Each question should specify its expected answer type: 'text', 'table_data', 'bar_chart_data', 'line_graph_data', 'pie_chart_data', 'quadratic_graph_data', 'hyperbolic_function_data', 'circle_data', or 'trigonometric_function_data'. If a structured data type is expected, provide data for it. Return only valid JSON array with exactly 15 questions.`;

      const aiResponse = await getAgentResponse(prompt, []);
      const questions = JSON.parse(aiResponse);

      // Process and cache the questions for all students
      const processedQuestions = questions.map((q, index) => ({
        ...q,
        id: `curriculum-${subject}-${grade}-${topic}-${Date.now()}-${index}`,
        answer: '',
        isSubmitted: false,
        isAttempted: false,
        feedback: null
      }));

      // Cache in shared curriculum bank
      cacheCurriculumQuestions(subject, grade, topic, subtopic, processedQuestions);

      return processedQuestions;
    } catch (error) {
      console.error('Error generating curriculum questions via AI:', error);

      // PRIORITY 2: Fallback to pre-built templates only if AI fails
      const templateQuestions = questionTemplates[subject.toLowerCase()]?.[topic.toLowerCase()];
      if (templateQuestions && templateQuestions.length >= 15) {
        console.log(`Using template questions for ${subject} - ${topic} as AI fallback`);
        const questions = templateQuestions.slice(0, 15).map((q, index) => ({
          ...q,
          id: `template-fallback-${subject}-${grade}-${topic}-${Date.now()}-${index}`,
          answer: '',
          isSubmitted: false,
          isAttempted: false,
          feedback: null
        }));

        // Cache the template questions
        cacheCurriculumQuestions(subject, grade, topic, subtopic, questions);
        return questions;
      }

      // PRIORITY 3: Final fallback to basic questions
      return generateFallbackQuestions(subject, topic, 15);
    }
  },

  // Get questions for students (from shared cache)
  getQuestionsForStudent: (subject, grade, topic, subtopic, numQuestions = 15) => {
    const questions = getCurriculumQuestions(subject, grade, topic, subtopic);
    if (questions) {
      return questions.slice(0, numQuestions);
    }
    return null;
  },

  // Generate practice exam with selected topics
  generatePracticeExam: (selectedTopics, questionsPerTopic = 5) => {
    const examQuestions = [];

    selectedTopics.forEach(topicData => {
      const questions = getCurriculumQuestions(
        topicData.subject,
        topicData.grade,
        topicData.topic,
        topicData.subtopic
      );

      if (questions) {
        // Randomly select questions for variety
        const shuffled = questions.sort(() => 0.5 - Math.random());
        const selected = shuffled.slice(0, questionsPerTopic);
        examQuestions.push(...selected);
      }
    });

    return examQuestions;
  }
};

// Legacy individual question generator (keeping for backward compatibility)
const smartQuestionGenerator = {
  generateQuestions: async (subject, grade, topic, subtopic, numQuestions, difficulty, getAgentResponse) => {
    // First, try to get from shared curriculum cache
    const curriculumQuestions = curriculumQuestionGenerator.getQuestionsForStudent(subject, grade, topic, subtopic, numQuestions);
    if (curriculumQuestions) {
      return curriculumQuestions;
    }

    // Fallback to individual caching
    const cachedQuestions = getCachedQuestions(subject, grade, topic, subtopic, difficulty);
    if (cachedQuestions) {
      return cachedQuestions.slice(0, numQuestions);
    }

    // Try to use pre-built templates
    const templateQuestions = questionTemplates[subject.toLowerCase()]?.[topic.toLowerCase()];
    if (templateQuestions && templateQuestions.length >= numQuestions) {
      const questions = templateQuestions.slice(0, numQuestions).map((q, index) => ({
        ...q,
        id: `template-${Date.now()}-${index}`,
        answer: '',
        isSubmitted: false,
        isAttempted: false,
        feedback: null
      }));

      // Cache the template questions
      cacheQuestions(subject, grade, topic, subtopic, difficulty, questions);
      return questions;
    }

    // Fallback to AI generation (with caching)
    try {
      const prompt = `Generate ${numQuestions} practice questions for Grade ${grade} ${subject} on "${topic}${subtopic ? ': ' + subtopic : ''}". Expected answer types: 'text', 'table_data', 'bar_chart_data', 'line_graph_data', 'pie_chart_data'. Return only valid JSON array.`;

      // Check AI response cache
      const cachedAIResponse = getCachedAIResponse(prompt, { subject, grade, topic, subtopic });
      if (cachedAIResponse) {
        const questions = JSON.parse(cachedAIResponse);
        cacheQuestions(subject, grade, topic, subtopic, difficulty, questions);
        return questions;
      }

      // Generate new AI response
      const aiResponse = await getAgentResponse(prompt, []);
      const questions = JSON.parse(aiResponse);

      // Cache both the AI response and the processed questions
      cacheAIResponse(prompt, { subject, grade, topic, subtopic }, aiResponse);
      cacheQuestions(subject, grade, topic, subtopic, difficulty, questions);

      return questions;
    } catch (error) {
      console.error('Error generating questions:', error);
      // Return fallback questions
      return generateFallbackQuestions(subject, topic, numQuestions);
    }
  }
};

const generateFallbackQuestions = (subject, topic, numQuestions) => {
  const fallbacks = [
    {
      question_text: `Explain the concept of ${topic} in ${subject}`,
      expected_answer_type: "text",
      table: null,
      shape: null,
      graph: null,
      journal_data: null
    },
    {
      question_text: `What are the key principles of ${topic}?`,
      expected_answer_type: "text",
      table: null,
      shape: null,
      graph: null,
      journal_data: null
    }
  ];

  return fallbacks.slice(0, numQuestions).map((q, index) => ({
    ...q,
    id: `fallback-${Date.now()}-${index}`,
    answer: '',
    isSubmitted: false,
    isAttempted: false,
    feedback: null
  }));
};

// Practice Exam Generator Component
const PracticeExamGenerator = ({ selectedSubject, selectedGrade, onGenerateExam }) => {
  const [selectedTopics, setSelectedTopics] = useState([]);
  const [questionsPerTopic, setQuestionsPerTopic] = useState(5);
  const [availableTopics, setAvailableTopics] = useState([]);

  useEffect(() => {
    // Get available topics from curriculum
    if (selectedSubject && selectedGrade) {
      // This would be populated from your curriculum data
      setAvailableTopics([
        { name: 'Algebra', subtopics: ['Linear Equations', 'Quadratic Equations'] },
        { name: 'Geometry', subtopics: ['Area', 'Perimeter', 'Volume'] },
        { name: 'Trigonometry', subtopics: ['Sine', 'Cosine', 'Tangent'] }
      ]);
    }
  }, [selectedSubject, selectedGrade]);

  const handleTopicToggle = (topic, subtopic = null) => {
    const topicKey = subtopic ? `${topic}:${subtopic}` : topic;
    setSelectedTopics(prev => {
      if (prev.find(t => t.key === topicKey)) {
        return prev.filter(t => t.key !== topicKey);
      } else {
        return [...prev, {
          key: topicKey,
          topic,
          subtopic,
          subject: selectedSubject?.name,
          grade: selectedGrade
        }];
      }
    });
  };

  const handleGenerateExam = () => {
    if (selectedTopics.length === 0) return;

    const examQuestions = curriculumQuestionGenerator.generatePracticeExam(selectedTopics, questionsPerTopic);
    onGenerateExam(examQuestions);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md">
      <h3 className="text-xl font-semibold mb-4">Generate Practice Exam</h3>

      <div className="mb-4">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Questions per topic: {questionsPerTopic}
        </label>
        <input
          type="range"
          min="1"
          max="10"
          value={questionsPerTopic}
          onChange={(e) => setQuestionsPerTopic(parseInt(e.target.value))}
          className="w-full"
        />
      </div>

      <div className="mb-4">
        <h4 className="font-medium mb-2">Select Topics:</h4>
        <div className="space-y-2">
          {availableTopics.map((topic) => (
            <div key={topic.name} className="border rounded p-3">
              <label className="flex items-center">
                <input
                  type="checkbox"
                  checked={selectedTopics.some(t => t.topic === topic.name && !t.subtopic)}
                  onChange={() => handleTopicToggle(topic.name)}
                  className="mr-2"
                />
                <span className="font-medium">{topic.name}</span>
              </label>

              {topic.subtopics && (
                <div className="ml-6 mt-2 space-y-1">
                  {topic.subtopics.map((subtopic) => (
                    <label key={subtopic} className="flex items-center">
                      <input
                        type="checkbox"
                        checked={selectedTopics.some(t => t.topic === topic.name && t.subtopic === subtopic)}
                        onChange={() => handleTopicToggle(topic.name, subtopic)}
                        className="mr-2"
                      />
                      <span className="text-sm">{subtopic}</span>
                    </label>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>

      <button
        onClick={handleGenerateExam}
        disabled={selectedTopics.length === 0}
        className="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        Generate Practice Exam ({selectedTopics.length * questionsPerTopic} questions)
      </button>
    </div>
  );
};

// Competition Exam Generator (Admin/Teacher Only)
const CompetitionExamGenerator = ({ selectedSubject, selectedGrade, onGenerateExam, currentUser }) => {
  const [selectedTopics, setSelectedTopics] = useState([]);
  const [questionsPerTopic, setQuestionsPerTopic] = useState(5);
  const [examTitle, setExamTitle] = useState('');
  const [examDuration, setExamDuration] = useState(60);

  // Only show for admins/teachers
  if (!currentUser || (currentUser.role !== 'admin' && currentUser.role !== 'teacher')) {
    return null;
  }

  const handleGenerateCompetitionExam = () => {
    if (selectedTopics.length === 0 || !examTitle.trim()) return;

    const examQuestions = curriculumQuestionGenerator.generatePracticeExam(selectedTopics, questionsPerTopic);
    onGenerateExam(examQuestions, {
      title: examTitle,
      duration: examDuration,
      type: 'competition',
      topics: selectedTopics
    });
  };

  return (
    <div className="bg-purple-50 border border-purple-200 p-6 rounded-lg shadow-md">
      <h3 className="text-xl font-semibold mb-4 text-purple-800">Generate Competition Exam</h3>

      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Exam Title</label>
          <input
            type="text"
            value={examTitle}
            onChange={(e) => setExamTitle(e.target.value)}
            placeholder="e.g., Mathematics Olympiad 2024"
            className="w-full p-2 border rounded-md"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Duration (minutes)</label>
          <input
            type="number"
            value={examDuration}
            onChange={(e) => setExamDuration(parseInt(e.target.value))}
            min="15"
            max="180"
            className="w-full p-2 border rounded-md"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">Questions per topic: {questionsPerTopic}</label>
          <input
            type="range"
            min="1"
            max="15"
            value={questionsPerTopic}
            onChange={(e) => setQuestionsPerTopic(parseInt(e.target.value))}
            className="w-full"
          />
        </div>
      </div>

      <button
        onClick={handleGenerateCompetitionExam}
        disabled={selectedTopics.length === 0 || !examTitle.trim()}
        className="w-full mt-4 bg-purple-500 text-white py-2 px-4 rounded-md hover:bg-purple-600 disabled:bg-gray-400 disabled:cursor-not-allowed"
      >
        Generate Competition Exam ({selectedTopics.length * questionsPerTopic} questions)
      </button>
    </div>
  );
};





// Format structured tutor content into readable response
const formatStructuredTutorContent = (tutorContent, subject, topic, subtopic) => {
  if (!tutorContent || typeof tutorContent !== 'object') {
    return "Error: Could not load structured tutor content.";
  }

  let formatted = `# 📚 **${subject} - ${topic}${subtopic ? `: ${subtopic}` : ''}**\n\n`;

  // Step-by-step explanation
  if (tutorContent.explanation) {
    formatted += `## 📖 **Step-by-Step Explanation**\n\n${tutorContent.explanation}\n\n`;
  }

  // Worked examples
  if (tutorContent.examples && tutorContent.examples.length > 0) {
    formatted += `## 💡 **Worked Examples**\n\n`;
    tutorContent.examples.forEach((example, index) => {
      formatted += `### Example ${index + 1}\n`;
      if (example.question) formatted += `**Question:** ${example.question}\n`;
      if (example.solution) formatted += `**Solution:** ${example.solution}\n`;
      if (example.explanation) formatted += `**Explanation:** ${example.explanation}\n`;
      formatted += `\n`;
    });
  }

  // Practice problems
  if (tutorContent.practiceProblems && tutorContent.practiceProblems.length > 0) {
    formatted += `## 🎯 **Practice Problems**\n\n`;
    tutorContent.practiceProblems.forEach((problem, index) => {
      formatted += `### Problem ${index + 1}\n`;
      if (problem.question) formatted += `**Question:** ${problem.question}\n`;
      if (problem.hint) formatted += `**Hint:** ${problem.hint}\n`;
      if (problem.solution) formatted += `**Solution:** ${problem.solution}\n`;
      formatted += `\n`;
    });
  }

  // Common misconceptions
  if (tutorContent.misconceptions && tutorContent.misconceptions.length > 0) {
    formatted += `## ⚠️ **Common Misconceptions**\n\n`;
    tutorContent.misconceptions.forEach((misconception, index) => {
      formatted += `${index + 1}. **${misconception.title || `Misconception ${index + 1}`}**\n`;
      formatted += `   ${misconception.description}\n\n`;
    });
  }

  // Key formulas/concepts
  if (tutorContent.keyConcepts && tutorContent.keyConcepts.length > 0) {
    formatted += `## 🔑 **Key Formulas & Concepts**\n\n`;
    tutorContent.keyConcepts.forEach((concept, index) => {
      formatted += `${index + 1}. **${concept.name}**\n`;
      if (concept.formula) formatted += `   Formula: ${concept.formula}\n`;
      if (concept.description) formatted += `   ${concept.description}\n`;
      formatted += `\n`;
    });
  }

  return formatted;
};

// Additional mathematical formatting utilities
const formatMathematicalExpressions = (text) => {
  if (!text || typeof text !== 'string') return text;

  // Format common mathematical patterns
  return text
    // Equations and formulas
    .replace(/(\w+)\s*=\s*(\w+)/g, '$1 = $2')           // Variable assignments
    .replace(/(\d+)\s*\+\s*(\d+)/g, '$1 + $2')           // Addition
    .replace(/(\d+)\s*-\s*(\d+)/g, '$1 - $2')           // Subtraction
    .replace(/(\d+)\s*\*\s*(\d+)/g, '$1 × $2')           // Multiplication
    .replace(/(\d+)\s*\/\s*(\d+)/g, '$1 ÷ $2')           // Division
    .replace(/(\w+)\^(\d+)/g, '$1^$2')                   // Exponents
    .replace(/\b(sin|cos|tan|log|ln)\b/gi, '$1')         // Math functions

    // Units and measurements
    .replace(/(\d+)\s*(cm|m|km|mm)/g, '$1 $2')           // Length units
    .replace(/(\d+)\s*(g|kg|mg)/g, '$1 $2')              // Weight units
    .replace(/(\d+)\s*(ml|l|cl)/g, '$1 $2')              // Volume units
    .replace(/(\d+)\s*(°C|°F|K)/g, '$1 $2')              // Temperature units

    // Currency and percentages
    .replace(/(\d+)\s*%/g, '$1%')                         // Percentages
    .replace(/R\s*(\d+)/g, 'R$1')                         // South African Rand
    .replace(/\$(\d+)/g, '$$1')                           // Dollar amounts

    // Clean up extra spaces
    .replace(/\s+/g, ' ')
    .trim();
};

// Enhanced mathematical content processor
const processMathematicalContent = (content, subject) => {
  if (!content || typeof content !== 'string') return content;

  // First detect if math structure is needed
  const needsMathStructure = detectMathStructure(content);

  if (!needsMathStructure) {
    return content; // Return as-is for non-math content
  }

  // Apply subject-specific formatting
  let formatted = content;

  if (subject?.name === 'Mathematics' || subject?.name === 'Mathematical Literacy' || subject?.name === 'Technical Mathematics') {
    // Pure math subjects - more aggressive formatting
    formatted = formatMathematicalContent(content);
  } else if (subject?.name === 'Physical Sciences' || subject?.name === 'Chemistry' || subject?.name === 'Biology') {
    // Science subjects - format scientific notation and units
    formatted = formatMathematicalContent(content)
      .replace(/(\d+\.\d+e[+-]\d+)/g, '\n$1')            // Scientific notation
      .replace(/(\d+)\s*(mol|g\/mol|L\/mol)/g, '\n$1 $2'); // Chemistry units
  } else if (subject?.name === 'Accounting' || subject?.name === 'Business Studies' || subject?.name === 'Economic and Management Sciences') {
    // Business subjects - format financial expressions
    formatted = formatMathematicalContent(content)
      .replace(/(\d+)\s*(profit|loss|cost|price)/gi, '\n$1 $2') // Business terms
      .replace(/(\d+)\s*%/g, '\n$1%');                    // Percentages
  } else {
    // Other subjects - standard mathematical formatting
    formatted = formatMathematicalContent(content);
  }

  return formatted;
};


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

const formatQuestionText = (text) => {
  if (typeof text !== 'string') return text;
  // Automatically format multi-part questions for vertical display
  return text.replace(/(\s?\(?[a-z]\)|\s?[ivx]+\.)/g, '<br />$1');
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
    // Add more cases for other subjects as they appear in curriculumData
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
    name: 'South African CAPS',
    description: 'The national curriculum for South Africa.',
    loaded: true,
    grades: sortedAllAvailableCapsGrades, // Use dynamically derived grades
    subjects: dynamicCapsSubjects
  },
  'Cambridge': { name: 'Cambridge Curriculum', description: 'International curriculum offered in over 160 countries.', loaded: false, grades: [10, 11, 12], subjects: [] }
};
const userSubscription = { accessibleCurricula: ['CAPS'] };

// Simple function to add days to a date.
const addDays = (date, days) => {
  const newDate = new Date(date);
  newDate.setDate(date.getDate() + days);
  return newDate;
};

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

const SelectionCard = ({ title, description, icon, onSelect, disabled = false, isLoading = false, color = 'bg-gray-200' }) => {
  const Icon = icon;
  return (
    <div
      onClick={!disabled && !isLoading ? onSelect : undefined}
      className={`bg-white rounded-xl shadow-lg transform transition-all duration-300 overflow-hidden group relative ${disabled ? 'opacity-50 cursor-not-allowed' : 'hover:shadow-2xl hover:-translate-y-2 cursor-pointer'}`}
    >
      {isLoading && (
        <div className="absolute inset-0 bg-white/80 flex items-center justify-center z-10">
          <Loader2 className="h-8 w-8 text-blue-600 animate-spin" />
        </div>
      )}
      <div className={`h-24 ${color} flex items-center justify-center`}>
        <Icon className={`h-12 w-12 ${disabled ? 'text-gray-400' : 'text-blue-600'} transition-transform duration-300 group-hover:scale-110`} />
      </div>
      <div className="p-6">
        <h3 className="text-xl font-bold text-gray-800 mb-2">{title}</h3>
        <p className="text-gray-600 text-sm">{description}</p>
      </div>
    </div>
  );
};

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


const QuestionBlock = React.memo(({ question, onAttempt, onAnswerInput, onSubmit, setActiveEditableRef, handleToggleMathStructure, selectedSubject }) => {
  const textAnswerRef = useRef(null);
  const expectedAnswerType = question.expected_answer_type;
  const handleAnswerDataChange = useCallback((data) => { onAnswerInput(question.id, data); }, [question.id, onAnswerInput]);

  const isStructuredAnswerValid = () => {
    const answer = question.answer;
    if (!answer) return false;
    switch (expectedAnswerType) {
      case 'table_data': return answer.rows && answer.rows.length > 0 && answer.rows.flat().some(cell => cell.trim() !== '');
      case 'cash_receipts_journal_data': return answer.rows && answer.rows.length > 0;
      case 'cash_payments_journal_data': return answer.rows && answer.rows.length > 0;
      case 'bar_chart_data':
      case 'line_graph_data': return answer.points && answer.points.length > 0 && answer.points.some(p => (p.label && p.label.trim() !== '') || (p.x !== '' && p.y !== ''));
      case 'pie_chart_data': return answer.slices && answer.slices.length > 0 && answer.slices.some(s => s.label.trim() !== '' && s.value !== '');
      case 'quadratic_graph_data': return (question.answer.a !== '' && question.answer.b !== '' && question.answer.c !== '') && (Number(question.answer.x_range[0]) < Number(question.answer.x_range[1]));
      case 'hyperbolic_function_data': return (question.answer.a !== '' && question.answer.b !== '') && (Number(question.answer.x_range[0]) < Number(question.answer.x_range[1]));
      case 'circle_data': return (question.answer.h !== '' && question.answer.k !== '' && question.answer.r !== '') && Number(question.answer.r) > 0;
      case 'trigonometric_function_data': return (question.answer.A !== '' && question.answer.B !== '' && question.answer.C !== '' && question.answer.D !== '') && (Number(question.answer.x_range[0]) < Number(question.answer.x_range[1]));
      default: return true;
    }
  };

  const structuredAnswerTypes = [
    'table_data', 'cash_receipts_journal_data', 'cash_payments_journal_data', 'cheque_data', 'receipt_data', 'cash_invoice_data', 'income_statement_data', 'trading_income_statement_data', 'bar_chart_data', 'line_graph_data', 'pie_chart_data',
    'quadratic_graph_data', 'hyperbolic_function_data', 'circle_data',
    'trigonometric_function_data', 'number_line_data', 'fraction_data', 'geometric_construction_data', 'statistical_analysis_data',
    'coordinate_plane_data', 'probability_simulation_data', 'algebraic_expression_data', 'vector_calculation_data',
    'matrix_calculation_data', 'calculus_tools_data', 'mathematical_instruments_data'
  ];

  return (
    <div className="bg-white p-4 rounded-lg shadow-md mb-4 border border-gray-200">
      <div className="flex justify-between items-start">
        <div className="flex-1 font-semibold text-gray-800 mr-4">
          <p>Q: <span dangerouslySetInnerHTML={{ __html: formatQuestionText(question.text) }} /></p>
          {question.table && <TableRenderer table={question.table} />}
          {question.shape && <ShapeRenderer shape={question.shape} />}
          {question.graph && <GraphRenderer graph={question.graph} />}
        </div>
        <div className="flex flex-col space-y-2">
          <button onClick={() => onAttempt(question.id, textAnswerRef)} disabled={question.isAttempted} className={`px-3 py-1 text-sm font-semibold rounded-md text-white ${question.isAttempted ? 'bg-gray-400 cursor-not-allowed' : 'bg-blue-500 hover:bg-blue-600'}`}>{question.isAttempted ? 'Attempting' : 'Attempt'}</button>
          <button onClick={() => onSubmit(question.id)} disabled={question.isSubmitted || (expectedAnswerType !== 'text' ? !isStructuredAnswerValid() : !question.answer?.trim())} className={`px-3 py-1 text-sm font-semibold rounded-md text-white ${(question.isSubmitted || (expectedAnswerType !== 'text' ? !isStructuredAnswerValid() : !question.answer?.trim())) ? 'bg-gray-400 cursor-not-allowed' : 'bg-green-500 hover:bg-green-600'}`}>{question.isSubmitted ? 'Submitted' : 'Submit'}</button>
        </div>
      </div>
      {question.isAttempted && (
        <>
          {expectedAnswerType === 'table_data' && <TableInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'cash_receipts_journal_data' && ['Accounting', 'Economic and Management Sciences', 'Business Studies'].includes(selectedSubject?.name) && <CashReceiptsJournalInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'cash_payments_journal_data' && ['Accounting', 'Economic and Management Sciences', 'Business Studies'].includes(selectedSubject?.name) && <CashPaymentsJournalInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'cheque_data' && ['Accounting', 'Economic and Management Sciences', 'Business Studies'].includes(selectedSubject?.name) && <ChequeInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'receipt_data' && ['Accounting', 'Economic and Management Sciences', 'Business Studies'].includes(selectedSubject?.name) && <ReceiptInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'cash_invoice_data' && ['Accounting', 'Economic and Management Sciences', 'Business Studies'].includes(selectedSubject?.name) && <CashInvoiceInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'income_statement_data' && ['Business Studies', 'Accounting'].includes(selectedSubject?.name) && parseInt(selectedGrade) >= 10 && <IncomeStatementInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'trading_income_statement_data' && ['Business Studies', 'Accounting'].includes(selectedSubject?.name) && parseInt(selectedGrade) >= 10 && <TradingIncomeStatementInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'number_line_data' && <NumberLineInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'fraction_data' && <FractionVisualizer initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'geometric_construction_data' && <GeometricConstructionInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'statistical_analysis_data' && <StatisticalAnalysisInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'coordinate_plane_data' && <CoordinatePlaneInput initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'probability_simulation_data' && <ProbabilitySimulator initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'algebraic_expression_data' && <AlgebraicExpressionBuilder initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'geometry_backend_test' && <GeometryBackendTest />}
          {expectedAnswerType === 'vector_calculation_data' && <VectorCalculator initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'matrix_calculation_data' && <MatrixCalculator initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'calculus_tools_data' && <CalculusTools initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'mathematical_instruments_data' && <MathematicalInstruments initialData={question.answer} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'bar_chart_data' && <BarChartInput initialData={question.answer || { type: "bar_chart", x_axis_label: "", y_axis_label: "", points: [{ label: '', y: '' }] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'line_graph_data' && <LineGraphInput initialData={question.answer || { type: "line_graph", x_axis_label: "", y_axis_label: "", points: [{ x: '', y: '' }] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'pie_chart_data' && <PieChartInput initialData={question.answer || { type: "pie_chart", title: "", slices: [{ label: '', value: '' }] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'quadratic_graph_data' && <QuadraticGraphInput initialData={question.answer || { type: "quadratic_graph", a: '', b: '', c: '', x_range: ['-5', '5'] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'hyperbolic_function_data' && <HyperbolicFunctionInput initialData={question.answer || { type: "hyperbolic_function", a: '1', b: '0', x_range: ['-5', '5'] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'circle_data' && <CircleInput initialData={question.answer || { type: "circle", h: '0', k: '0', r: '5' }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}
          {expectedAnswerType === 'trigonometric_function_data' && <TrigonometricFunctionInput initialData={question.answer || { type: "trigonometric_function", func_type: 'sin', A: '1', B: '1', C: '0', D: '0', x_range: ['0', `${2 * Math.PI}`] }} onChange={handleAnswerDataChange} isSubmitted={question.isSubmitted} />}

          {!structuredAnswerTypes.includes(expectedAnswerType) && (
            <div
              ref={textAnswerRef}
              contentEditable={!question.isSubmitted}
              onFocus={() => setActiveEditableRef(textAnswerRef)}
              onBlur={(e) => onAnswerInput(question.id, e.currentTarget.innerHTML)}
              className={`mt-4 p-3 border rounded-md min-h-[50px] outline-none focus:ring-2 focus:ring-blue-400 ${question.isSubmitted ? 'bg-gray-100' : 'bg-white'}`}
              dangerouslySetInnerHTML={{ __html: question.answer }}
            />
          )}
        </>
      )}
      {question.feedback && (
        <div className="mt-4 p-3 bg-green-100 rounded-lg border border-green-200">
          <p className="font-semibold text-green-800 mb-2">AI Feedback:</p>
          <p className="text-sm text-gray-800 whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: question.feedback.mathStructureEnabled ? applyAllTextFormatting(question.feedback.content, selectedSubject) : question.feedback.content }} />

          {/* Show auto-detection status */}
          {question.feedback.autoDetected && (
            <div className="mt-2 flex items-center gap-2">
              <span className="text-xs text-green-600 font-medium">
                ✓ Auto-detected mathematical content
              </span>
              {question.feedback.mathStructureEnabled && (
                <span className="text-xs text-blue-600 font-medium">
                  (Math structure enabled)
                </span>
              )}
            </div>
          )}

          <button onClick={() => handleToggleMathStructure(question.id)} className="mt-2 flex items-center gap-1 text-xs text-blue-600 hover:text-blue-800 font-semibold">
            <Rows size={12} />
            {question.feedback.mathStructureEnabled ? 'Disable Math Structure' : 'Enable Math Structure'}
          </button>
        </div>
      )}
    </div>
  )
});

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


// Basic Keypad component replaced with EnhancedMathKeypad import above

// Simple Back Button Component
const BackButton = ({ navigationStack, onNavigateBack, currentView }) => {
  // Only show back button if there's navigation history and we're not at the root
  if (navigationStack.length <= 1 || currentView === 'curriculum') {
    return null;
  }

  return (
    <button
      onClick={onNavigateBack}
      className="fixed top-20 left-4 z-50 bg-white hover:bg-gray-100 text-gray-700 rounded-full p-3 shadow-lg border border-gray-200 transition-all duration-200 hover:shadow-xl"
      title="Go back"
    >
      <ChevronLeft className="h-6 w-6" />
    </button>
  );
};





// ClassworkView component has been extracted to src/components/student/ClassworkView.jsx


// AssignClassModal component has been extracted to src/components/admin/AssignClassModal.jsx


// AssessmentGenerator component has been extracted to src/components/teacher/AssessmentGenerator.jsx

// TeacherView component has been extracted to src/components/teacher/TeacherView.jsx

// SubmissionsDashboard component has been extracted to src/components/teacher/SubmissionsDashboard.jsx



// AdminView component has been extracted to src/components/admin/AdminView.jsx


// Custom hooks have been moved to src/hooks/ directory

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
    auth, db, storage, authService, dbService, currentUser, authLoading, userRole, handleLogout
  } = authHook;

  const {
    loading, setLoading, message, setMessage, showSplash, setShowSplash,
    showLandingPage, setShowLandingPage, chatRoomId, setChatRoomId,
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
    setActiveAssignment, activeQuestionId, setActiveQuestionId,
    practiceQuestions, setPracticeQuestions
  } = assignments;

  const {
    isKeypadVisible, setIsKeypadVisible, activeEditableRef,
    setActiveEditableRef, workspaceMode, setWorkspaceMode, freeformWorkAreaRef
  } = workspace;

  const {
    teacherView, setTeacherView, adminView, setAdminView
  } = teacherAdmin;

  const {
    chatInput, setChatInput, isChatLoading, setIsChatLoading,
    freeformAnswer, setFreeformAnswer, chatHistories, setChatHistories,
    chatHistory, setChatHistory
  } = chat;

  const {
    selectedFreeformTopic, setSelectedFreeformTopic,
    currentProblemThreadId, setCurrentProblemThreadId
  } = freeform;

  const [superAdminMode, setSuperAdminMode] = useState('student');

  const effectiveRole = currentUser?.isSuperAdmin ? superAdminMode : currentUser?.role;
  const effectiveCurrentUser = currentUser ? { ...currentUser, role: effectiveRole } : null;

  useEffect(() => {
    if (currentUser?.isSuperAdmin) {
      setSuperAdminMode('student');
    }
  }, [currentUser?.isSuperAdmin]);

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


  // --- Chat Helper Functions ---
  const getSubjectKey = useCallback(() => {
    // Ensure selectedSubject is an object with a 'name' property
    const subjectName = selectedSubject?.name || 'all';
    return `${selectedCurriculumKey || 'all'}_${selectedGrade || 'all'}_${subjectName}`;
  }, [selectedCurriculumKey, selectedGrade, selectedSubject]);

  // NEW: Function to save successful freeform problems
  const saveSuccessfulProblem = useCallback(async (question, answer, topic, subject, grade, userId) => {
    if (!dbService) {
      console.error("Database service not available for saving successful problem.");
      return;
    }
    const problemId = `solved-${Date.now()}`;
    const docRef = doc(dbService, 'artifacts', appId, 'users', userId, 'solved_freeform_problems', problemId);
    try {
      await setDoc(docRef, {
        question: question,
        answer: answer,
        topic: topic,
        subject: subject,
        grade: grade,
        timestamp: serverTimestamp(),
        retentionDate: addDays(new Date(), 90), // 90 days retention
        isSolved: true, // Explicitly mark as solved
      });
      console.log("Successful problem saved:", problemId);
    } catch (e) {
      console.error("Error saving successful problem: ", e);
    }
  }, [dbService]);

  // NEW: Function to save struggling freeform problems
  const saveStrugglingProblem = useCallback(async (threadId, history, topic, subject, grade, userId) => {
    if (!dbService) {
      console.error("Database service not available for saving struggling problem.");
      return;
    }
    const docRef = doc(dbService, 'artifacts', appId, 'users', userId, 'struggling_problems', threadId);
    try {
      // Save the entire thread history
      await setDoc(docRef, {
        threadId: threadId,
        chatHistory: history, // Save the full history of the thread
        topic: topic,
        subject: subject,
        grade: grade,
        lastUpdated: serverTimestamp(),
        isSolved: false, // Explicitly mark as not solved
      }, { merge: true }); // Merge to update existing thread or create new
      console.log("Struggling problem saved/updated:", threadId);
    } catch (e) {
      console.error("Error saving struggling problem: ", e);
    }
  }, [dbService]);

  // NEW: Function to mark a struggling problem as solved and delete it
  const handleMarkStrugglingProblemSolved = useCallback(async (threadId) => {
    if (!dbService || !currentUser) {
      console.error("Database or user not available for marking problem as solved.");
      setMessage("Error: Could not mark problem as solved. Please try again.");
      return;
    }

    const docRef = doc(dbService, 'artifacts', appId, 'users', currentUser.uid, 'struggling_problems', threadId);
    try {
      await deleteDoc(docRef);
      console.log(`Struggling problem with threadId ${threadId} marked as solved and deleted.`);
      setMessage("Problem marked as solved and removed from your struggling problems.");
      // Optionally, you might want to clear the currentProblemThreadId if it matches
      if (currentProblemThreadId === threadId) {
        setCurrentProblemThreadId(null);
      }
      // You might also want to refresh the list of struggling problems if a dedicated view exists
    } catch (e) {
      console.error("Error marking struggling problem as solved: ", e);
      setMessage("Failed to mark problem as solved. Please try again.");
    }
  }, [dbService, currentUser, currentProblemThreadId]);


  const addQuestionToChat = useCallback((question) => {
    const subjectKey = getSubjectKey();
    const newQuestion = {
      id: Date.now(),
      question: question,
      answer: null,
      loading: true,
      timestamp: new Date().toISOString(),
      topic: selectedFreeformTopic, // Use selectedFreeformTopic here
      threadId: currentProblemThreadId || `thread-${Date.now()}`, // Ensure threadId is set
      isSuccessful: false // Default to false, updated by AI response
    };

    setChatHistories(prevHistories => {
      const currentHistory = prevHistories[subjectKey] || [];
      const updatedHistory = [...currentHistory, newQuestion];
      return {
        ...prevHistories,
        [subjectKey]: updatedHistory,
      };
    });
    // Return the ID for the AI response to target
    return newQuestion.id;
  }, [getSubjectKey, selectedFreeformTopic, currentProblemThreadId]);


  const updateAnswerInChat = useCallback((questionId, answer, isCorrect = false) => {
    const subjectKey = getSubjectKey();

    setChatHistories(prevHistories => {
      const currentHistory = prevHistories[subjectKey] || [];
      let updatedHistory = currentHistory.map(message =>
        message.id === questionId ? { ...message, answer, loading: false, isSuccessful: isCorrect } : message
      );

      const currentThreadId = updatedHistory.find(msg => msg.id === questionId)?.threadId;
      // Filter to get only messages for the current thread
      const currentThreadHistory = updatedHistory.filter(msg => msg.threadId === currentThreadId);

      // Truncate local history for active threads if needed (for performance, not storage)
      const maxHistoryLength = 10;
      let truncatedThreadHistory = currentThreadHistory;
      if (currentThreadHistory.length > maxHistoryLength) {
        truncatedThreadHistory = currentThreadHistory.slice(-maxHistoryLength);
      }

      // Update the full history by replacing the old thread with the truncated one
      updatedHistory = updatedHistory.filter(msg => msg.threadId !== currentThreadId).concat(truncatedThreadHistory);

      // Manage currentProblemThreadId based on success
      if (isCorrect) {
        setCurrentProblemThreadId(null); // Problem solved, clear thread
      } else {
        setCurrentProblemThreadId(currentThreadId); // Still struggling, keep thread active
      }

      // IMPORTANT: The actual saving to Firestore for freeform problems
      // is now handled in handleSendFreeformQuery, not here.
      // This function only updates the local state and thread ID.

      return {
        ...prevHistories,
        [subjectKey]: updatedHistory,
      };
    });
  }, [getSubjectKey]);


  const updateHelperNavigationLabel = useCallback((newLabel) => {
    setNavigationStack(prevStack => prevStack.map(item =>
      item.view === 'curriculum_helper' ? { ...item, label: newLabel } : item
    ));
  }, [setNavigationStack]);

  // handleStrugglingProblem is now primarily a UI trigger,
  // the saving logic is in saveStrugglingProblem called by handleSendFreeformQuery
  const handleStrugglingProblem = useCallback((problemItem) => {
    // This function is now more of a signal or a trigger for the UI
    // to indicate a problem is being struggled with, and ensures a threadId exists.
    // It's called from Workspace with the specific problem item.
    if (!currentProblemThreadId) {
      setCurrentProblemThreadId(`thread-${Date.now()}`);
    } else {
      setCurrentProblemThreadId(problemItem.threadId);
    }
    setMessage("Problem marked as struggling. You can continue the conversation or revisit it later.");
  }, [currentProblemThreadId]);

  // --- Enhanced getAgentResponse function with token tracking and caching ---
  const getAgentResponse = useCallback(async (input, history) => {
    setLoading(true);

    // Check cache first for common requests
    const cacheKey = `api_${input.substring(0, 100)}_${JSON.stringify(history).substring(0, 100)}`;
    const cachedResponse = aiResponseCache.get(cacheKey);

    if (cachedResponse && Date.now() - cachedResponse.timestamp < 30 * 60 * 1000) { // 30 min cache for API calls
      tokenUsageTracker.logCachedResponse();
      setLoading(false);
      return cachedResponse.response;
    }

    const apiUrl = 'https://snombi-tlassistant.hf.space/api/agent'; // Ensure this is your actual API endpoint
    const sanitizedHistory = history.map(msg => ({
      role: msg.role,
      content: typeof msg.content === 'string' ? getPlainTextFromHtml(msg.content) : JSON.stringify(msg.content)
    }));
    const payload = { input: input, chat_history: sanitizedHistory, user_role: effectiveRole || 'student' }; // Added nullish coalescing for safety

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ error: 'Unknown error' }));
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorData.error || 'No error message provided'}`);
      }
      const result = await response.json();

      // Estimate token usage (rough approximation)
      const estimatedTokens = Math.ceil((input.length + JSON.stringify(history).length + result.output.length) / 4);
      tokenUsageTracker.logAICall(estimatedTokens);

      // Cache the response
      aiResponseCache.set(cacheKey, {
        response: result.output,
        timestamp: Date.now(),
        metadata: { input: input.substring(0, 100), history: history.length }
      });

      return result.output;
    } catch (error) {
      console.error("Error communicating with AI agent:", error);
      return `Sorry, there was an error communicating with the AI. Please try again. ${error.message}`;
    } finally {
      setLoading(false);
    }
  }, [currentUser]);


  // --- Navigation Helper Functions ---
  const addViewToStack = useCallback((newView, label, data = {}) => {
    setNavigationStack(prev => [...prev, { view: newView, label: label, data: data }]);
    setView(newView);
  }, []);

  // REFINED: handleSendFreeformQuery for distinct saving of successful/struggling problems
  const handleSendFreeformQuery = useCallback(async (queryText) => { // Now accepts queryText as an argument
    if (!queryText.trim() || loading || !selectedFreeformTopic || !currentUser || !dbService) {
      // Added checks for currentUser and dbService
      console.warn("Cannot send query: Missing input, loading, topic, user, or dbService.");
      return;
    }

    setLoading(true);
    const question = queryText; // Use the passed queryText
    const questionId = addQuestionToChat(question); // Add to local chatHistories state
    setFreeformAnswer(''); // Clear input immediately

    try {
      const subjectKey = getSubjectKey();
      // Get the current chat history for RAG, including the newly added question
      const currentChatHistoryForRAG = [...(chatHistories[subjectKey] || [])];

      // Call AI agent with the full chat history for context
      const newAIAnswer = await getAgentResponse(question, currentChatHistoryForRAG.map(item => ({
        role: "user", // Assuming all history items are user questions for RAG
        content: item.question
      })));

      // Determine if the answer is correct based on AI's response
      const isCorrect = newAIAnswer.toLowerCase().includes('correct');

      // Update local chat history with AI's answer and success status
      updateAnswerInChat(questionId, newAIAnswer, isCorrect);

      // Get the updated chat history after local state has been set (important for saving the correct thread)
      const updatedLocalChatHistory = chatHistories[subjectKey] || [];
      const threadIdForSaving = updatedLocalChatHistory.find(msg => msg.id === questionId)?.threadId;

      if (isCorrect) {
        // If successful, save only the question-answer pair to solved_freeform_problems
        saveSuccessfulProblem(
          question,
          newAIAnswer,
          selectedFreeformTopic,
          selectedSubject?.name,
          selectedGrade,
          currentUser.uid
        );
        // After a successful answer, reset the current problem thread
        setCurrentProblemThreadId(null);
      } else {
        // If struggling, save the entire thread to struggling_problems
        const fullThreadHistory = updatedLocalChatHistory.filter(msg => msg.threadId === threadIdForSaving);
        saveStrugglingProblem(
          threadIdForSaving, // Use the specific thread ID
          fullThreadHistory,
          selectedFreeformTopic,
          selectedSubject?.name,
          selectedGrade,
          currentUser.uid
        );
        // Ensure the currentProblemThreadId is set for continued struggle
        setCurrentProblemThreadId(threadIdForSaving);
      }

    } catch (error) {
      console.error('Error sending query to AI or saving problem:', error);
      updateAnswerInChat(questionId, 'Error fetching AI response or saving problem.');
    } finally {
      setLoading(false);
    }
  }, [loading, selectedFreeformTopic, addQuestionToChat, getAgentResponse, updateAnswerInChat, getSubjectKey, chatHistories, currentUser, dbService, selectedSubject, selectedGrade, saveSuccessfulProblem, saveStrugglingProblem, setCurrentProblemThreadId]);

  // NEW: Function to handle continuing a struggling problem from MySavedProblemsView
  const handleContinueProblem = useCallback((problem) => {
    // Set the context for the workspace
    setSelectedCurriculumKey(problem.curriculumKey || 'all');
    setSelectedGrade(problem.grade);
    // Find the full subject object from allCurricula for consistency
    let subjectObject = null;
    for (const key in allCurricula) {
      const curriculum = allCurricula[key];
      const foundSubject = curriculum.subjects.find(s => s.name === problem.subject);
      if (foundSubject) {
        subjectObject = foundSubject;
        break;
      }
    }
    setSelectedSubject(subjectObject);
    setSelectedFreeformTopic(problem.topic);
    setCurrentProblemThreadId(problem.threadId);

    // Load the chat history for this problem into the local state for the current subjectKey
    const problemSubjectKey = `${problem.curriculumKey || 'all'}_${problem.grade || 'all'}_${problem.subject || 'all'}`;
    setChatHistories(prevHistories => ({
      ...prevHistories,
      [problemSubjectKey]: problem.chatHistory || []
    }));

    // Navigate to the workspace in freeform mode
    setWorkspaceMode('freeform');
    addViewToStack('workspace', `Continuing: ${problem.topic}`, {
      view: 'workspace',
      curriculumKey: problem.curriculumKey,
      grade: problem.grade,
      subject: problem.subject,
      topic: problem.topic,
      threadId: problem.threadId
    });
    setMessage(`Loaded problem: ${problem.topic}. You can continue the conversation.`);
  }, [allCurricula, setSelectedCurriculumKey, setSelectedGrade, setSelectedSubject, setSelectedFreeformTopic, setCurrentProblemThreadId, setChatHistories, setWorkspaceMode, addViewToStack]);


  // --- useEffect for Student-Specific Logic After Authentication ---
  useEffect(() => {
    // This effect runs when authentication state changes
    if (effectiveCurrentUser && dbService) {
      // Handle student navigation after login
      if (effectiveCurrentUser.role === 'student' && !effectiveCurrentUser.isSuperAdmin) {
        // Set curriculum and grade from user preferences
        if (effectiveCurrentUser.curriculum && effectiveCurrentUser.grade) {
          setSelectedCurriculumKey(effectiveCurrentUser.curriculum);
          setSelectedGrade(Number(effectiveCurrentUser.grade));
          // Navigate directly to subject selection
          setView('subject');
          setNavigationStack([
            { view: 'curriculum', label: 'Curricula' },
            { view: 'subject', label: 'Subject', data: { curriculumKey: effectiveCurrentUser.curriculum, grade: Number(effectiveCurrentUser.grade) } }
          ]);
        }

        // Fetch assignments for students
        const studentClassId = effectiveCurrentUser.classId || 'class_10a'; // Default classId
        const q = query(collection(dbService, "assessments"), where("classId", "==", studentClassId));
        getDocs(q).then(querySnapshot => {
          const fetchedAssignments = querySnapshot.docs.map(d => ({ id: d.id, ...d.data() }));
          setPendingAssignments(fetchedAssignments);
        }).catch(error => {
          console.error("Error fetching assignments:", error);
        });
      }
    } else if (!effectiveCurrentUser) {
      // User is signed out
      setPendingAssignments([]);
    }
  }, [effectiveCurrentUser, dbService, setSelectedCurriculumKey, setSelectedGrade, setView, setNavigationStack, setPendingAssignments]);

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

  const handleToggleMathStructure = (questionId) => {
    setPracticeQuestions(prev => prev.map(q => {
      if (q.id === questionId) {
        const needsMathStructure = shouldUseMathStructure(selectedSubject?.name, q.feedback.content);
        return {
          ...q,
          feedback: {
            ...q.feedback,
            mathStructureEnabled: !q.feedback.mathStructureEnabled,
            autoDetected: needsMathStructure
          }
        };
      }
      return q;
    }));
  };

  const handleAttempt = useCallback((questionId, ref) => {
    setPracticeQuestions(prev => {
      const updatedQuestions = prev.map(q => q.id === questionId ? { ...q, isAttempted: true } : q);
      const question = updatedQuestions.find(q => q.id === questionId);
      if (question && question.expected_answer_type === 'text') setActiveEditableRef(ref);
      else setActiveEditableRef(null);
      return updatedQuestions;
    });
  }, [setActiveEditableRef]);

  const handleAnswerInput = useCallback((questionId, answer) => {
    setPracticeQuestions(prev => prev.map(q => q.id === questionId ? { ...q, answer } : q));
  }, []);

  // --- Deterministic evaluation helpers (no API call needed) ---
  const evaluateDeterministic = useCallback((questionToSubmit, studentAnswer) => {
    const qType = questionToSubmit.question_type || questionToSubmit.expected_answer_type;

    // MCQ: compare selected index to correct_index
    if (qType === 'mcq') {
      const correctIdx = questionToSubmit.correct_index;
      const studentIdx = typeof studentAnswer === 'number' ? studentAnswer : parseInt(studentAnswer, 10);
      const isCorrect = studentIdx === correctIdx;
      const correctOption = questionToSubmit.options?.[correctIdx] || '';
      return {
        is_correct: isCorrect,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect
          ? `Correct! ${questionToSubmit.explanation || ''}`
          : `Incorrect. The correct answer is: "${correctOption}". ${questionToSubmit.explanation || ''}`,
      };
    }

    // CALC: compare numeric value within tolerance
    if (qType === 'calc' || questionToSubmit.expected_answer_type === 'number') {
      const correctVal = parseFloat(questionToSubmit.correct_value);
      const studentVal = parseFlexibleNumber(studentAnswer);
      const unit = questionToSubmit.unit || '';
      const allowRoundedCurrency = String(unit).toUpperCase().includes('R');
      const isCorrect = Number.isFinite(correctVal) && studentVal !== null && (
        allowRoundedCurrency
          ? numbersMatchForCurrency(studentVal, correctVal)
          : Math.abs(studentVal - correctVal) <= 0.01
      );
      return {
        is_correct: isCorrect,
        score: isCorrect ? 100 : 0,
        feedback: isCorrect
          ? `Correct! The answer is ${unit}${correctVal.toFixed(2)}.`
          : `Incorrect. The correct answer is ${unit}${correctVal.toFixed(2)}. You answered ${unit}${studentVal === null ? studentAnswer : studentVal.toFixed(2)}.`,
      };
    }

    // TABLE_WORDBANK: compare placed word IDs to correct_map
    if (qType === 'table_wordbank') {
      const correctMap = questionToSubmit.correct_map || {};
      let totalCells = 0;
      let correctCells = 0;
      const mistakes = [];

      for (const [rowIdx, cols] of Object.entries(correctMap)) {
        for (const [colIdx, expectedId] of Object.entries(cols)) {
          totalCells++;
          const studentPlaced = studentAnswer?.[rowIdx]?.[colIdx];
          if (studentPlaced === expectedId) {
            correctCells++;
          } else {
            mistakes.push(`Row ${parseInt(rowIdx) + 1}, Column ${parseInt(colIdx) + 1}`);
          }
        }
      }

      const score = totalCells > 0 ? Math.round((correctCells / totalCells) * 100) : 0;
      const isCorrect = score >= 50;
      return {
        is_correct: isCorrect,
        score,
        feedback: score === 100
          ? 'Excellent! All items placed correctly.'
          : `You got ${correctCells} out of ${totalCells} correct (${score}%).${mistakes.length > 0 ? ` Check: ${mistakes.join(', ')}.` : ''}`,
      };
    }

    // Fallback: not deterministic
    return null;
  }, []);

  const handleSubmit = useCallback(async (questionId, questionText, expectedAnswerType, studentAnswer, questionSolution, currentQuestionBlockRef) => {
    const questionToSubmit = practiceQuestions.find(q => q.id === questionId);
    if (!questionToSubmit) return;

    if (activeAssignment?.feedbackMode !== 'instant') {
      setPracticeQuestions(prev => prev.map(q => q.id === questionId ? { ...q, isSubmitted: true } : q));
      return;
    }

    // --- Try deterministic evaluation first (no API call) ---
    const deterministicResult = evaluateDeterministic(questionToSubmit, studentAnswer);
    if (deterministicResult) {
      const feedbackContent = deterministicResult.feedback;
      setPracticeQuestions(prev => prev.map(q =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: feedbackContent,
            is_correct: deterministicResult.is_correct,
            score: deterministicResult.score,
            mathStructureEnabled: false,
            autoDetected: false,
            processedContent: feedbackContent,
          }
        } : q
      ));
      setChatHistory(prev => [...prev,
      { role: 'user', content: `Student's answer for "${questionText}": ${typeof studentAnswer === 'object' ? JSON.stringify(studentAnswer) : studentAnswer}` },
      { role: 'ai', content: feedbackContent },
      ]);
      return;
    }

    // --- LLM evaluation for typed / open-ended questions ---
    setLoading(true);

    let userMessageContent;
    if (typeof studentAnswer === 'object' && studentAnswer !== null) {
      userMessageContent = `Student's structured answer for "${questionText}":\n\`\`\`json\n${JSON.stringify(studentAnswer, null, 2)}\n\`\`\``;
    } else {
      userMessageContent = `Student's answer for "${questionText}":\n${studentAnswer}`;
    }
    setChatHistory(prev => [...prev, { role: 'user', content: userMessageContent }]);

    const loadingMessageId = `loading-feedback-${Date.now()}`;
    setChatHistory(prev => [...prev, { id: loadingMessageId, role: 'ai', content: 'Evaluating...', isLoading: true }]);

    try {
      // Use the lightweight /api/evaluate-typed endpoint if sample_answer exists
      const sampleAnswer = questionToSubmit.sample_answer || questionSolution || '';
      const evalResponse = await fetch('https://snombi-tlassistant.hf.space/api/evaluate-typed', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question_prompt: questionText,
          sample_answer: sampleAnswer,
          student_answer: typeof studentAnswer === 'object' ? JSON.stringify(studentAnswer) : studentAnswer,
          subject: selectedSubject?.name || '',
          grade: selectedGrade || '',
        }),
      });

      let feedbackContent;
      let isCorrect = false;
      let score = 0;

      if (evalResponse.ok) {
        const evalData = await evalResponse.json();
        const evaluation = evalData.evaluation || {};
        isCorrect = evaluation.is_correct || false;
        score = evaluation.score || 0;
        feedbackContent = evaluation.feedback || 'No feedback available.';
        if (evaluation.key_points_hit?.length > 0) {
          feedbackContent += '\n\nKey points covered: ' + evaluation.key_points_hit.join('; ');
        }
        if (evaluation.key_points_missed?.length > 0) {
          feedbackContent += '\nPoints to improve: ' + evaluation.key_points_missed.join('; ');
        }
        feedbackContent += `\n\nScore: ${score}/100`;
      } else {
        // Fallback to full agent if evaluate-typed fails
        const payload = {
          question: questionText,
          expected_answer_type: expectedAnswerType,
          student_answer: studentAnswer,
          solution: questionSolution,
          context: {
            subject: selectedSubject?.name,
            grade: selectedGrade,
            topic: activeTopic?.name,
            document_type: 'question_feedback'
          }
        };
        feedbackContent = await getAgentResponse(payload, chatHistory);
      }

      setPracticeQuestions(prev => prev.map(q =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: feedbackContent,
            is_correct: isCorrect,
            score: score,
            mathStructureEnabled: shouldUseMathStructure(selectedSubject?.name, feedbackContent),
            autoDetected: shouldUseMathStructure(selectedSubject?.name, feedbackContent),
            processedContent: processMathematicalContent(feedbackContent, selectedSubject)
          }
        } : q
      ));

      setChatHistory(prev => prev.map(msg =>
        msg.id === loadingMessageId ? { ...msg, content: feedbackContent, isLoading: false } : msg
      ));

      if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
        window.MathJax.typesetPromise();
      }

    } catch (error) {
      console.error("Error getting feedback:", error);
      setChatHistory(prev => prev.map(msg =>
        msg.id === loadingMessageId ? { ...msg, content: "Error: Could not get feedback.", isLoading: false } : msg
      ));
      setPracticeQuestions(prev => prev.map(q =>
        q.id === questionId ? {
          ...q,
          isSubmitted: true,
          feedback: {
            content: "Error: Failed to get feedback. Please try again.",
            mathStructureEnabled: false,
            autoDetected: false,
            processedContent: "Error: Failed to get feedback. Please try again."
          }
        } : q
      ));
    } finally {
      setLoading(false);
    }
  }, [practiceQuestions, activeAssignment, evaluateDeterministic, getAgentResponse, selectedSubject, selectedGrade, activeTopic, chatHistory, setLoading]);

  const handleMathInput = useCallback((symbol) => {
    const targetElement = activeEditableRef?.current;
    if (targetElement && targetElement.isContentEditable) {
      targetElement.focus();
      if (symbol === 'x²') document.execCommand('insertHTML', false, '<sup>2</sup>');
      else if (symbol === 'x₂') document.execCommand('insertHTML', false, '<sub>2</sub>');
      else document.execCommand('insertHTML', false, symbol);
    }
  }, [activeEditableRef]);

  const handleStartAssignment = useCallback((assignment) => {
    let subjectObject = null;
    let curriculumKey = null;

    for (const key in allCurricula) {
      const curriculum = allCurricula[key];
      const foundSubject = curriculum.subjects.find(s => s.name === assignment.subject);
      if (foundSubject) {
        subjectObject = foundSubject;
        curriculumKey = key;
        break;
      }
    }

    if (!subjectObject) {
      console.error("Could not find matching subject for assignment:", assignment);
      return;
    }

    setActiveAssignment(assignment);
    setSelectedCurriculumKey(curriculumKey);
    setSelectedSubject(subjectObject);
    setSelectedGrade(assignment.grade);
    setActiveTopic({ name: assignment.topic });

    const questions = assignment.questions.map((q, index) => ({
      id: `q-${Date.now()}-${index}`,
      text: q.question_text,
      table: null,
      shape: null,
      graph: null,
      expected_answer_type: q.question_type,
      solution: q.solution,
      answer: '',
      isSubmitted: false,
      isAttempted: false,
      feedback: null,
    }));
    setPracticeQuestions(questions);
    setWorkspaceMode('practice');

    addViewToStack('workspace', `Assignment: ${assignment.topic}`, {
      value: 'Class Assignment',
      curriculumKey: curriculumKey,
      grade: assignment.grade,
      subject: subjectObject,
      topic: { name: assignment.topic }
    });
  }, [allCurricula, setPracticeQuestions, setWorkspaceMode, setSelectedSubject, setSelectedGrade, setActiveTopic, setSelectedCurriculumKey, addViewToStack]);

  const handleAssignmentSubmit = useCallback(async () => {
    if (!activeAssignment || !currentUser) return;
    setLoading(true);

    const answers = practiceQuestions.map(q => ({
      questionId: q.id,
      questionText: q.text,
      answer: q.answer
    }));

    try {
      await addDoc(collection(dbService, "submissions"), {
        studentId: currentUser.uid,
        studentName: currentUser.name,
        assessmentId: activeAssignment.id,
        classId: activeAssignment.classId,
        answers: answers,
        submittedAt: serverTimestamp(),
        status: 'submitted'
      });

      if (activeAssignment.feedbackMode === 'on_submission') {
        setPracticeQuestions(prev => prev.map((q) => ({
          ...q,
          feedback: {
            content: q.solution,
            mathStructureEnabled: shouldUseMathStructure(selectedSubject?.name, q.solution),
            autoDetected: shouldUseMathStructure(selectedSubject?.name, q.solution),
            processedContent: processMathematicalContent(q.solution, selectedSubject)
          }
        })));
        setMessage('Assignment submitted successfully! Feedback is now available.');
      } else {
        setMessage('Assignment submitted successfully for teacher review!');
        setView('classwork');
        setActiveAssignment(null);
      }

    } catch (e) {
      console.error("Error submitting assignment: ", e);
      setMessage('Failed to submit assignment. Please try again.');
    } finally {
      setLoading(false);
    }
  }, [activeAssignment, practiceQuestions, currentUser, dbService, setView, setActiveAssignment]);

  const renderContent = () => {
    const getSubjectKey = () => {
      // Ensure selectedSubject is an object with a 'name' property
      const subjectName = selectedSubject?.name || 'all';
      return `${selectedCurriculumKey || 'all'}_${selectedGrade || 'all'}_${subjectName}`;
    };

    const subjectKey = getSubjectKey();

    if (authLoading) return <div className="flex items-center justify-center h-screen"><Loader2 className="h-12 w-12 animate-spin text-blue-600" /></div>;
    if (!effectiveCurrentUser) {
      if (showLandingPage) {
        return <LandingPage onGetStarted={() => setShowLandingPage(false)} />;
      }
      return <AuthScreen auth={auth} db={db} />;
    }
    if (effectiveCurrentUser.isSuperAdmin) {
      if (effectiveRole === 'admin') return <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />;
      if (effectiveRole === 'teacher') return <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />;
    }
    if (effectiveRole === 'admin') return <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />;
    if (effectiveRole === 'teacher') return <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />;
    if (effectiveRole === 'student') {
      switch (view) {
        case 'my_saved_problems':
          return (
            <MySavedProblemsView
              db={dbService}
              currentUser={effectiveCurrentUser}
              onContinueProblem={handleContinueProblem}
              onMarkSolved={handleMarkStrugglingProblemSolved}
              setMessage={setMessage}
            />
          );
        case 'workspace':
          console.log('[App Debug] Rendering Workspace. activeTopic:', activeTopic);
          return (
            <Workspace
              topic={activeTopic?.name}
              practiceQuestions={practiceQuestions}
              workspaceMode={workspaceMode}
              setWorkspaceMode={setWorkspaceMode}
              freeformWorkAreaRef={freeformWorkAreaRef}
              currentUser={effectiveCurrentUser}
              getAgentResponse={getAgentResponse}
              handleAnswerInput={handleAnswerInput}
              handleSubmit={handleSubmit}
              setView={setView}
              activeAssignment={activeAssignment}
              handleAssignmentSubmit={handleAssignmentSubmit}
              loading={loading}
              setLoading={setLoading}
              selectedSubject={selectedSubject}
              selectedGrade={selectedGrade}
              addQuestionToChat={addQuestionToChat}
              updateAnswerInChat={updateAnswerInChat}
              handleSendFreeformQuery={handleSendFreeformQuery}
              freeformAnswer={freeformAnswer}
              setFreeformAnswer={setFreeformAnswer}
              currentProblemThreadId={currentProblemThreadId}
              setSelectedFreeformTopic={setSelectedFreeformTopic}
            />
          );
        case 'thumbnail_test':
          return <ThumbnailTestPage setView={setView} />;
        case 'integration_demo':
          return <IntegrationDemo />;
        case 'geometry_backend_test':
          return <GeometryTestAccess setView={setView} />;
        default:
          return <StudentView
            view={view} setView={setView}
            allCurricula={allCurricula}
            selectedCurriculumKey={selectedCurriculumKey}
            setSelectedCurriculumKey={setSelectedCurriculumKey}
            selectedGrade={selectedGrade}
            setSelectedGrade={setSelectedGrade}
            selectedSubject={selectedSubject}
            setSelectedSubject={setSelectedSubject}
            activeTopic={activeTopic}
            setActiveTopic={setActiveTopic}
            practiceQuestions={practiceQuestions}
            setPracticeQuestions={setPracticeQuestions}
            isCurriculumPageVisible={isCurriculumPageVisible}
            setIsCurriculumPageVisible={setIsCurriculumPageVisible}
            isKeypadVisible={isKeypadVisible}
            setIsKeypadVisible={setIsKeypadVisible}
            activeEditableRef={activeEditableRef}
            setActiveEditableRef={setActiveEditableRef}
            workspaceMode={workspaceMode}
            setWorkspaceMode={setWorkspaceMode}
            freeformWorkAreaRef={freeformWorkAreaRef}
            currentUser={effectiveCurrentUser}
            getAgentResponse={getAgentResponse}
            handleAttempt={handleAttempt}
            handleAnswerInput={handleAnswerInput}
            handleSubmit={handleSubmit}
            navigationStack={navigationStack}
            setNavigationStack={setNavigationStack}
            updateHelperNavigationLabel={updateHelperNavigationLabel}
            db={dbService}
            storage={storage}
            handleStartAssignment={handleStartAssignment}
            activeAssignment={activeAssignment}
            handleAssignmentSubmit={handleAssignmentSubmit}
            handleToggleMathStructure={handleToggleMathStructure}
            loading={loading} setLoading={setLoading}
            chatHistory={chatHistories[subjectKey] || []} // Pass the correct subject-specific chat history
            addQuestionToChat={addQuestionToChat}
            updateAnswerInChat={updateAnswerInChat}
            applyAllTextFormatting={(text) => text}
            handleSendFreeformQuery={handleSendFreeformQuery}
            freeformAnswer={freeformAnswer}
            setFreeformAnswer={setFreeformAnswer}
            selectedFreeformTopic={selectedFreeformTopic}
            setSelectedFreeformTopic={setSelectedFreeformTopic}
            currentProblemThreadId={currentProblemThreadId}
            handleStrugglingProblem={handleStrugglingProblem}
            handleMarkStrugglingProblemSolved={handleMarkStrugglingProblemSolved} // Pass the new handler
            handleContinueProblem={handleContinueProblem} // Pass the new handler
            curriculumData={allCurricula[selectedCurriculumKey]?.topicsByGrade || {}} // Pass the relevant part of curriculumData
          />;
      }
    }
    return <div className="p-8 text-center">Loading user profile or role not assigned.</div>;
  };

  // Show splash screen first
  if (showSplash) {
    return <SplashScreen onComplete={() => {
      setShowSplash(false);
      setShowLandingPage(true);
    }} />;
  }

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <BackButton
        navigationStack={navigationStack}
        onNavigateBack={() => {
          if (navigationStack.length > 1) {
            const newStack = navigationStack.slice(0, navigationStack.length - 1);
            setNavigationStack(newStack);
            const newView = newStack[newStack.length - 1].view;
            setView(newView);
            // --- UPDATED LOGIC HERE ---
            // If we are navigating back to the main curriculum selection, reset the selection state
            if (newView === 'curriculum') {
              setSelectedCurriculumKey(null);
              setSelectedGrade(null);
              setSelectedSubject(null);
              setActiveTopic(null);
            }
          } else {
            // This case handles trying to go back from the root 'curriculum' view
            setView('curriculum');
            setNavigationStack([{ view: 'curriculum', label: 'Curricula' }]);
            setSelectedCurriculumKey(null);
            setSelectedGrade(null);
            setSelectedSubject(null);
            setActiveTopic(null);
          }

          if (isCurriculumPageVisible && navigationStack[navigationStack.length - 2]?.view !== 'curriculum_helper') {
            setIsCurriculumPageVisible(false);
          }
        }}
        currentView={view}
      />
      <Header currentUser={effectiveCurrentUser} onLogout={handleLogout} pendingAssignments={pendingAssignments} onStartAssignment={handleStartAssignment} setView={setView} superAdminMode={superAdminMode} setSuperAdminMode={setSuperAdminMode} />
      <main className="max-w-7xl mx-auto">
        {renderContent()}
      </main>
      <EnhancedMathKeypad
        isVisible={isKeypadVisible}
        onClose={() => setIsKeypadVisible(false)}
        onKeyClick={handleMathInput}
      />
      <footer className="bg-white mt-12 border-t">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 text-center text-gray-500">
          <p>&copy; {new Date().getFullYear()} Fundile. All rights reserved.</p>
        </div>
      </footer>
      <MessageModal message={message} onClose={() => setMessage('')} />
      <AdminTokenUsageDisplay currentUser={effectiveCurrentUser} />
    </div>
  );
}
