import React, { useState } from 'react';
import {
  Users,
  UserPlus,
  Clock,
  CheckCircle2,
  Sparkles,
  Smartphone,
  TrendingUp,
  Award,
  Zap,
  ShieldCheck,
  AlertTriangle,
  Calendar,
  Download,
  Printer,
  Copy,
  Check,
  X,
  ChevronRight,
  Info,
  CreditCard,
  FileText,
  Lightbulb,
  Target,
  Flame,
  ArrowUpRight,
  BarChart3,
  MessageSquare,
  RefreshCw,
  Share2
} from 'lucide-react';
import MasteryDial from '../student/MasteryDial';
import InAppPaymentModal from '../subscription/InAppPaymentModal';

// Initial dataset for learners
const INITIAL_LEARNERS = {
  nqobile: {
    id: 'nqobile',
    name: 'Nqobile Dlamini',
    grade: 'Grade 10 FET',
    school: 'Phakamani Secondary School',
    avatar: 'ND',
    linkCode: 'PAR8M4',
    focusTime: '3h 45m',
    focusTimeMinutes: 225,
    questionsCompleted: 48,
    accuracyRate: 82,
    streakDays: 6,
    ungameableXP: 1840,
    dataUsedMB: 1.6,
    videoEquivalentMB: 450,
    savedRands: 95,
    masteredTopics: [
      { name: 'Depreciation: Straight-line vs Reducing Balance', subject: 'Accounting', score: 94 },
      { name: 'Cash Receipts Journal: Sales & Cost of Sales', subject: 'Accounting', score: 91 },
      { name: 'Pythagoras in Analytical Geometry', subject: 'Mathematics', score: 82 },
      { name: 'Newton\'s First Law & Inertia Principles', subject: 'Physical Sciences', score: 78 }
    ],
    repairedMisconceptions: [
      {
        topic: 'Accounting: Value-Added Tax (VAT)',
        issue: 'Confusing 15% Exclusive with 115% Inclusive formula',
        resolution: 'Multiplied gross inclusive Bank receipt (R2,300) by 15/100 instead of 15/115. Resolved in 5-min targeted prerequisite drill.',
        timestamp: 'Thursday 17:15',
        status: 'Resolved (100% Mastery in Follow-up)'
      },
      {
        topic: 'Mathematics: Quadratic Equations',
        issue: 'Distributing negative signs across parentheses in binomials',
        resolution: 'Sign inversion rule reinforced through step-by-step Socratic breakdown.',
        timestamp: 'Tuesday 16:30',
        status: 'Resolved'
      }
    ],
    coachingTips: [
      {
        id: 'tip-n1',
        icon: '💡',
        category: 'Confidence Builder',
        badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
        prompt: 'Today Nqobile mastered 94% on Depreciation! Ask her how reducing balance differs from straight-line depreciation at dinner tonight.',
        rationale: 'Encourages her to explain the concept in her own words, cementing active recall without feeling quizzed.'
      },
      {
        id: 'tip-n2',
        icon: '🎯',
        category: 'Light Encouragement',
        badgeColor: 'bg-blue-50 text-blue-700 border-blue-200',
        prompt: 'Encourage a quick 10-minute session on Tariffs and Exchange Rates before Tuesday.',
        rationale: 'Micro-sessions eliminate homework dread while building steady exam momentum.'
      },
      {
        id: 'tip-n3',
        icon: '🌟',
        category: 'Growth Mindset',
        badgeColor: 'bg-amber-50 text-amber-700 border-amber-200',
        prompt: 'Praise her 6-day streak: "I saw you tackled that tricky VAT 15/115 calculation on Thursday and sorted it out in 5 minutes flat!"',
        rationale: 'Highlights resilience and targeted diagnostic recovery rather than mere natural talent.'
      }
    ],
    subjects: [
      {
        id: 'acc',
        name: 'Accounting',
        code: 'ACC10',
        formativeMastery: 94,
        evaluativeScore: 84,
        level: 'Level 7',
        rating: 'Outstanding Achievement',
        recentTopics: ['Depreciation (94%)', 'Cash Receipts Journal (91%)', 'Bank Reconciliation Intro (80%)'],
        streak: '6-day active',
        needsRefresh: false
      },
      {
        id: 'math',
        name: 'Mathematics',
        code: 'MTH10',
        formativeMastery: 82,
        evaluativeScore: 78,
        level: 'Level 6',
        rating: 'Meritorious Achievement',
        recentTopics: ['Analytical Geometry (82%)', 'Quadratic Factorisation (85%)', 'Exponents Laws (79%)'],
        streak: '5-day active',
        needsRefresh: false
      },
      {
        id: 'phys',
        name: 'Physical Sciences',
        code: 'PHY10',
        formativeMastery: 76,
        evaluativeScore: 70,
        level: 'Level 6',
        rating: 'Meritorious Achievement',
        recentTopics: ['Vectors in 1D (78%)', 'Newton\'s Laws (75%)', 'Stoichiometry Moles (68%)'],
        streak: '4-day active',
        needsRefresh: true
      },
      {
        id: 'life',
        name: 'Life Sciences',
        code: 'LIF10',
        formativeMastery: 88,
        evaluativeScore: 82,
        level: 'Level 7',
        rating: 'Outstanding Achievement',
        recentTopics: ['Cell Division & Mitosis (90%)', 'Plant Tissues (86%)', 'Animal Tissues (84%)'],
        streak: '5-day active',
        needsRefresh: false
      }
    ]
  },
  sipho: {
    id: 'sipho',
    name: 'Sipho Dlamini',
    grade: 'Grade 8 Senior Phase',
    school: 'Phakamani Secondary School',
    avatar: 'SD',
    linkCode: 'GR8SIP',
    focusTime: '4h 10m',
    focusTimeMinutes: 250,
    questionsCompleted: 56,
    accuracyRate: 86,
    streakDays: 5,
    ungameableXP: 1620,
    dataUsedMB: 1.8,
    videoEquivalentMB: 520,
    savedRands: 110,
    masteredTopics: [
      { name: 'Pythagoras Theorem: Right-Angled Triangles', subject: 'Mathematics', score: 88 },
      { name: 'Integers & Rules for Exponent Calculations', subject: 'Mathematics', score: 84 },
      { name: 'Financial Literacy: Cash Receipts Journal entries', subject: 'EMS', score: 90 },
      { name: 'Photosynthesis & Respiration in Plants', subject: 'Natural Sciences', score: 85 }
    ],
    repairedMisconceptions: [
      {
        topic: 'Mathematics: Negative Integers',
        issue: 'Sign rules for subtracting negative integers (-(-a) = +a)',
        resolution: 'Used number line visual representation to clarify direction reversal. Scored 100% on immediate retry.',
        timestamp: 'Wednesday 15:40',
        status: 'Resolved'
      },
      {
        topic: 'Natural Sciences: Particle Model',
        issue: 'Thinking gas particles completely freeze/stop moving when chilled',
        resolution: 'Interactive kinetic model reinforced continuous particle motion down to absolute zero.',
        timestamp: 'Monday 18:10',
        status: 'Resolved'
      }
    ],
    coachingTips: [
      {
        id: 'tip-s1',
        icon: '💡',
        category: 'Curiosity Spark',
        badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
        prompt: 'Sipho scored 88% on the Pythagorean Theorem! Ask him why builders always use 3m-4m-5m triangles to check if a corner wall is square.',
        rationale: 'Connects classroom geometry to real-world trades, sparking engaging discussion without homework tension.'
      },
      {
        id: 'tip-s2',
        icon: '🎯',
        category: 'Micro-Target',
        badgeColor: 'bg-blue-50 text-blue-700 border-blue-200',
        prompt: 'Suggest an 8-minute micro-sprint on EMS Cash Receipts Journal before Thursday.',
        rationale: 'A bite-sized challenge keeps him in the sweet spot of high focus and low anxiety.'
      },
      {
        id: 'tip-s3',
        icon: '🌟',
        category: 'Resilience Shoutout',
        badgeColor: 'bg-amber-50 text-amber-700 border-amber-200',
        prompt: 'Celebrate his persistence: "You tackled that minus-minus rule until you mastered it 100% — proud of your effort!"',
        rationale: 'Reinforces that asking questions and repairing errors is what authentic mastery is all about.'
      }
    ],
    subjects: [
      {
        id: 'math8',
        name: 'Mathematics',
        code: 'MTH08',
        formativeMastery: 88,
        evaluativeScore: 82,
        level: 'Level 7',
        rating: 'Outstanding Achievement',
        recentTopics: ['Pythagorean Theorem (88%)', 'Integers Operations (84%)', 'Fractions & Percentages (80%)'],
        streak: '5-day active',
        needsRefresh: false
      },
      {
        id: 'ems8',
        name: 'Economic & Management Sciences',
        code: 'EMS08',
        formativeMastery: 90,
        evaluativeScore: 86,
        level: 'Level 7',
        rating: 'Outstanding Achievement',
        recentTopics: ['Cash Receipts Journal (90%)', 'Factors of Production (88%)', 'Forms of Ownership (84%)'],
        streak: '5-day active',
        needsRefresh: false
      },
      {
        id: 'ns8',
        name: 'Natural Sciences',
        code: 'NAT08',
        formativeMastery: 85,
        evaluativeScore: 79,
        level: 'Level 6',
        rating: 'Meritorious Achievement',
        recentTopics: ['Photosynthesis (85%)', 'Particle Model of Matter (82%)', 'Acids, Bases & pH (78%)'],
        streak: '4-day active',
        needsRefresh: false
      },
      {
        id: 'eng8',
        name: 'English First Additional Language',
        code: 'ENG08',
        formativeMastery: 80,
        evaluativeScore: 75,
        level: 'Level 6',
        rating: 'Meritorious Achievement',
        recentTopics: ['Comprehension Analysis (80%)', 'Direct & Indirect Speech (78%)', 'Punctuation Rules (76%)'],
        streak: '3-day active',
        needsRefresh: true
      }
    ]
  }
};

export default function ParentDashboard({
  initialLearnerId = 'nqobile',
  parentName = 'Mrs. Nomvula Dlamini',
  parentPhone = '+27 82 555 4192',
  className = ''
}) {
  const [learners, setLearners] = useState(INITIAL_LEARNERS);
  const [selectedLearnerId, setSelectedLearnerId] = useState(initialLearnerId);
  const [isAddChildModalOpen, setIsAddChildModalOpen] = useState(false);
  const [isInvoiceModalOpen, setIsInvoiceModalOpen] = useState(false);
  const [copiedTipId, setCopiedTipId] = useState(null);
  const [copiedPulseText, setCopiedPulseText] = useState(false);
  const [pulseToastMessage, setPulseToastMessage] = useState('');
  const [pulseViewMode, setPulseViewMode] = useState('bubble'); // 'bubble' | 'table'
  const [isPaymentModalOpen, setIsPaymentModalOpen] = useState(false);
  const [paymentPlan, setPaymentPlan] = useState(null);
  const [householdBilling, setHouseholdBilling] = useState({
    planName: 'Fundile Household Plan',
    cycle: 'Monthly (R149 / mo)',
    price: 149,
    method: 'Debit Card •••• 4192 (PayFast)',
    renewalDate: '15 October 2026',
    status: 'Active • 2 Learners Linked',
  });

  const handlePaymentSuccess = (result) => {
    setIsPaymentModalOpen(false);
    const updatedMethod =
      result.method === 'manual_eft_pop'
        ? `Manual EFT (${result.reference || 'POP Verified'})`
        : result.method === 'school_voucher'
        ? `School License (${result.voucher})`
        : result.method === 'capitec'
        ? 'Capitec Pay'
        : result.method === 'ozow'
        ? 'Ozow Instant EFT'
        : 'Bank Card •••• 4192';

    setHouseholdBilling((prev) => ({
      ...prev,
      method: updatedMethod,
      status: `Active (${result.tier?.toUpperCase()} Tier)`,
    }));
    setPulseToastMessage('💳 Payment method & subscription updated successfully!');
    setTimeout(() => setPulseToastMessage(''), 4000);
  };

  // Add child modal form state
  const [addChildForm, setAddChildForm] = useState({
    name: '',
    grade: 'Grade 10 FET',
    school: '',
    linkCode: ''
  });
  const [addChildError, setAddChildError] = useState('');

  // Selected child object
  const activeLearner = learners[selectedLearnerId] || learners.nqobile;

  // Household data calculation
  const totalMBUsed = Object.values(learners).reduce((sum, l) => sum + (l.dataUsedMB || 0), 0).toFixed(1);
  const totalVideoEquivalentMB = Object.values(learners).reduce((sum, l) => sum + (l.videoEquivalentMB || 0), 0);
  const totalSavedRands = Object.values(learners).reduce((sum, l) => sum + (l.savedRands || 0), 0);

  // Copy dinner-table question
  const handleCopyTip = (tipId, text) => {
    navigator.clipboard?.writeText(text);
    setCopiedTipId(tipId);
    setTimeout(() => setCopiedTipId(null), 2500);
  };

  // WhatsApp raw pulse text generator
  const generatePulseRawText = () => {
    return `📲 *FUNDILE ACADEMIC PULSE • SUNDAY REPORT*\n` +
      `👤 Learner: *${activeLearner.name}* (${activeLearner.grade})\n` +
      `📅 Period: Mon 22 Sep – Sun 28 Sep 2026\n\n` +
      `⏱️ *Focus Time:* ${activeLearner.focusTime} (${activeLearner.streakDays}-day streak 🔥)\n` +
      `🎯 *Questions Solved:* ${activeLearner.questionsCompleted} questions • ${activeLearner.accuracyRate}% accuracy\n` +
      `🏆 *Mastered CAPS Topics:*\n` +
      activeLearner.masteredTopics.map(t => `  • ${t.name} (${t.score}%)`).join('\n') + `\n\n` +
      `🛠️ *Repaired Misconception:*\n` +
      `  • ${activeLearner.repairedMisconceptions[0]?.topic}: ${activeLearner.repairedMisconceptions[0]?.issue} (${activeLearner.repairedMisconceptions[0]?.status})\n\n` +
      `💡 *Dinner Conversation Starter:*\n` +
      `  "${activeLearner.coachingTips[0]?.prompt}"\n\n` +
      `📶 *Cellular Data Used:* ${activeLearner.dataUsedMB} MB (< 2 MB offline PWA)\n` +
      `🔗 *Open Guardian Portal:* https://fundile.app/parent`;
  };

  const handleCopyPulse = () => {
    navigator.clipboard?.writeText(generatePulseRawText());
    setCopiedPulseText(true);
    setTimeout(() => setCopiedPulseText(false), 2500);
  };

  const handleSendTestPulse = () => {
    setPulseToastMessage(`✅ WhatsApp Academic Pulse dispatched to ${parentPhone}! Check your phone in a few seconds.`);
    setTimeout(() => setPulseToastMessage(''), 4500);
  };

  // Handle Add Child Form Submission
  const handleAddChildSubmit = (e) => {
    e.preventDefault();
    if (!addChildForm.name.trim()) {
      setAddChildError('Please enter the learner\'s full name.');
      return;
    }
    if (!addChildForm.linkCode.trim()) {
      setAddChildError('Please enter the 6-character link code from your child\'s phone.');
      return;
    }

    const newId = addChildForm.name.toLowerCase().replace(/\s+/g, '-').slice(0, 15);
    const initials = addChildForm.name
      .split(' ')
      .map(p => p[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);

    const newLearnerObj = {
      id: newId,
      name: addChildForm.name.trim(),
      grade: addChildForm.grade,
      school: addChildForm.school.trim() || 'Secondary School',
      avatar: initials || 'ST',
      linkCode: addChildForm.linkCode.toUpperCase().trim(),
      focusTime: '1h 15m',
      focusTimeMinutes: 75,
      questionsCompleted: 18,
      accuracyRate: 78,
      streakDays: 2,
      ungameableXP: 450,
      dataUsedMB: 0.9,
      videoEquivalentMB: 310,
      savedRands: 65,
      masteredTopics: [
        { name: 'Foundational Baseline Assessment', subject: 'Mathematics', score: 80 },
        { name: 'Diagnostic Readiness Check', subject: 'Sciences', score: 75 }
      ],
      repairedMisconceptions: [
        {
          topic: 'Foundations Diagnostic',
          issue: 'Baseline topic review initiated',
          resolution: 'Scored 80% on welcome calibration diagnostic.',
          timestamp: 'Just now',
          status: 'Active'
        }
      ],
      coachingTips: [
        {
          id: `tip-${newId}-1`,
          icon: '💡',
          category: 'Welcome Starter',
          badgeColor: 'bg-emerald-50 text-emerald-700 border-emerald-200',
          prompt: `Ask ${addChildForm.name} what interesting concept they explored during their calibration assessment today!`,
          rationale: 'Shows supportive enthusiasm without any pressure.'
        },
        {
          id: `tip-${newId}-2`,
          icon: '🎯',
          category: 'Target',
          badgeColor: 'bg-blue-50 text-blue-700 border-blue-200',
          prompt: 'Encourage a quick 10-minute setup drill to discover their daily target.',
          rationale: 'Small beginnings create solid lifelong study habits.'
        }
      ],
      subjects: [
        {
          id: `${newId}-math`,
          name: 'Mathematics',
          code: 'MTH00',
          formativeMastery: 78,
          evaluativeScore: 72,
          level: 'Level 5',
          rating: 'Substantial Achievement',
          recentTopics: ['Diagnostic Baseline', 'Review & Practice'],
          streak: '2-day active',
          needsRefresh: false
        },
        {
          id: `${newId}-sci`,
          name: 'Natural / Physical Sciences',
          code: 'SCI00',
          formativeMastery: 74,
          evaluativeScore: 70,
          level: 'Level 5',
          rating: 'Substantial Achievement',
          recentTopics: ['Diagnostic Baseline', 'Fundamental Laws'],
          streak: '2-day active',
          needsRefresh: false
        }
      ]
    };

    setLearners(prev => ({
      ...prev,
      [newId]: newLearnerObj
    }));

    setSelectedLearnerId(newId);
    setAddChildForm({ name: '', grade: 'Grade 10 FET', school: '', linkCode: '' });
    setAddChildError('');
    setIsAddChildModalOpen(false);

    setPulseToastMessage(`🎉 ${newLearnerObj.name} successfully linked to your Guardian Portal!`);
    setTimeout(() => setPulseToastMessage(''), 4500);
  };

  return (
    <div className={`min-h-screen bg-slate-50 text-slate-900 font-sans pb-16 ${className}`}>
      {/* Toast Notification */}
      {pulseToastMessage && (
        <div className="fixed top-5 right-5 z-50 max-w-md bg-[#13519C] text-white px-5 py-3.5 rounded-2xl shadow-xl border border-blue-400/30 flex items-center gap-3 animate-in fade-in slide-in-from-top-3 duration-200">
          <CheckCircle2 className="w-5 h-5 text-emerald-300 shrink-0" />
          <span className="text-sm font-medium leading-snug">{pulseToastMessage}</span>
          <button
            onClick={() => setPulseToastMessage('')}
            className="text-white/70 hover:text-white ml-auto"
            aria-label="Close notification"
          >
            <X className="w-4 h-4" />
          </button>
        </div>
      )}

      {/* ── TOP HEADER / GUARDIAN IDENTITY BAR ── */}
      <header className="bg-white border-b border-slate-200 sticky top-0 z-30 shadow-2xs">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5">
          <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
            {/* Identity & Portal Title */}
            <div className="flex items-center gap-3.5">
              <div className="w-11 h-11 rounded-2xl bg-[#13519C] flex items-center justify-center text-white font-bold text-lg shadow-sm shrink-0">
                <span className="font-mono">F</span>
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h1 className="text-xl sm:text-2xl font-bold tracking-tight text-slate-900 font-afacad">
                    Parent & Guardian Bridge
                  </h1>
                  <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-emerald-50 text-emerald-700 border border-emerald-200">
                    <ShieldCheck className="w-3.5 h-3.5" />
                    Verified WhatsApp
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-500 font-medium">
                  {parentName} • {parentPhone} • Sunday 18:00 Pulse Active
                </p>
              </div>
            </div>

            {/* Quick Actions */}
            <div className="flex items-center gap-2 sm:gap-3 flex-wrap">
              <button
                onClick={() => setIsInvoiceModalOpen(true)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl border border-slate-200 bg-slate-50 hover:bg-slate-100 text-xs font-semibold text-slate-700 transition cursor-pointer"
              >
                <CreditCard className="w-3.5 h-3.5 text-[#13519C]" />
                <span>Subscription & Invoicing</span>
              </button>

              <button
                onClick={() => setIsAddChildModalOpen(true)}
                className="inline-flex items-center gap-1.5 px-3.5 py-1.5 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-semibold shadow-xs transition cursor-pointer"
              >
                <UserPlus className="w-3.5 h-3.5" />
                <span>Add Child</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* ── MAIN CONTENT CONTAINER ── */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-6 space-y-6">

        {/* ── CHILD SELECTOR TABS & ZERO-NAGGING VALUE CALLOUT ── */}
        <section className="bg-white border border-slate-200/90 rounded-2xl p-4 sm:p-5 shadow-xs">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
            
            {/* Child Switcher Tabs */}
            <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-2">
              <span className="text-xs font-bold uppercase tracking-wider text-slate-600 sm:mr-2">
                Learner View:
              </span>
              <div className="flex flex-wrap items-center gap-2">
                {Object.values(learners).map((learner) => {
                  const isSelected = learner.id === selectedLearnerId;
                  return (
                    <button
                      key={learner.id}
                      onClick={() => setSelectedLearnerId(learner.id)}
                      className={`inline-flex items-center gap-2.5 px-4 py-2 rounded-xl text-sm font-semibold transition cursor-pointer border ${
                        isSelected
                          ? 'bg-[#13519C] text-white border-[#13519C] shadow-xs'
                          : 'bg-slate-50 hover:bg-slate-100 text-slate-700 border-slate-200'
                      }`}
                    >
                      <span className={`w-6 h-6 rounded-lg text-xs font-bold flex items-center justify-center ${
                        isSelected ? 'bg-white text-[#13519C]' : 'bg-slate-200 text-slate-700'
                      }`}>
                        {learner.avatar}
                      </span>
                      <span>{learner.name}</span>
                      <span className={`text-xs px-2 py-0.5 rounded-full font-normal ${
                        isSelected ? 'bg-white/20 text-white' : 'bg-slate-200/70 text-slate-600'
                      }`}>
                        {learner.grade}
                      </span>
                    </button>
                  );
                })}

                <button
                  onClick={() => setIsAddChildModalOpen(true)}
                  className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl border border-dashed border-slate-300 hover:border-[#13519C] text-xs font-semibold text-slate-500 hover:text-[#13519C] transition cursor-pointer"
                >
                  <UserPlus className="w-3.5 h-3.5" />
                  <span>Link Learner</span>
                </button>
              </div>
            </div>

            {/* Zero Nagging Trust Badge */}
            <div className="flex items-center gap-2 text-xs bg-amber-500/10 border border-amber-300/40 text-amber-900 px-3.5 py-2 rounded-xl font-medium">
              <Sparkles className="w-4 h-4 text-[#FF9100] shrink-0" />
              <span>
                <strong>Zero Nagging Philosophy:</strong> Objective cognitive tracking replaces stressful interrogation with transparent praise.
              </span>
            </div>
          </div>
        </section>

        {/* ── KEY VITALS STRIP ── */}
        <section className="grid grid-cols-2 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-slate-500 mb-1">
              <span className="text-xs font-medium uppercase tracking-wider">Weekly Focus Time</span>
              <Clock className="w-4 h-4 text-[#13519C]" />
            </div>
            <div className="text-2xl font-bold font-mono text-slate-900 tracking-tight">
              {activeLearner.focusTime}
            </div>
            <p className="text-xs text-emerald-600 font-medium mt-1 flex items-center gap-1">
              <TrendingUp className="w-3 h-3" />
              <span>+24m vs prior week</span>
            </p>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-slate-500 mb-1">
              <span className="text-xs font-medium uppercase tracking-wider">Questions & Accuracy</span>
              <Target className="w-4 h-4 text-emerald-600" />
            </div>
            <div className="text-2xl font-bold font-mono text-slate-900 tracking-tight">
              {activeLearner.questionsCompleted} <span className="text-sm font-normal text-slate-400">solved</span>
            </div>
            <p className="text-xs text-emerald-600 font-medium mt-1 flex items-center gap-1">
              <CheckCircle2 className="w-3 h-3" />
              <span>{activeLearner.accuracyRate}% first-attempt accuracy</span>
            </p>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-slate-500 mb-1">
              <span className="text-xs font-medium uppercase tracking-wider">Consistency Streak</span>
              <Flame className="w-4 h-4 text-[#FF9100]" />
            </div>
            <div className="text-2xl font-bold font-mono text-slate-900 tracking-tight flex items-center gap-1">
              <span>{activeLearner.streakDays}</span>
              <span className="text-sm font-normal text-slate-400">days in a row</span>
            </div>
            <p className="text-xs text-amber-700 font-medium mt-1">
              🔥 Ungameable XP: {activeLearner.ungameableXP.toLocaleString()}
            </p>
          </div>

          <div className="bg-white border border-slate-200/90 rounded-2xl p-4 shadow-xs">
            <div className="flex items-center justify-between text-slate-500 mb-1">
              <span className="text-xs font-medium uppercase tracking-wider">Cellular Data Saved</span>
              <Smartphone className="w-4 h-4 text-blue-600" />
            </div>
            <div className="text-2xl font-bold font-mono text-[#13519C] tracking-tight">
              R{activeLearner.savedRands}
            </div>
            <p className="text-xs text-slate-500 font-medium mt-1">
              Used only <span className="font-mono font-bold text-slate-700">{activeLearner.dataUsedMB} MB</span> this week
            </p>
          </div>
        </section>

        {/* ── GRID: SUNDAY ACADEMIC PULSE + DATA SAVINGS METER ── */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">

          {/* ── SUNDAY 18:00 ACADEMIC PULSE PREVIEW (7 COLS) ── */}
          <section className="lg:col-span-7 bg-white border border-slate-200/90 rounded-2xl shadow-xs overflow-hidden flex flex-col justify-between">
            <div>
              {/* Header */}
              <div className="p-5 border-b border-slate-100 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-600 border border-emerald-200 flex items-center justify-center shrink-0">
                    <MessageSquare className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <h2 className="text-lg font-bold text-slate-900 font-afacad">
                        Sunday 18:00 Academic Pulse Preview
                      </h2>
                      <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-[#FF9100]/15 text-[#f58200] border border-[#FF9100]/30">
                        Weekly Automated
                      </span>
                    </div>
                    <p className="text-xs text-slate-500">
                      Dispatched every Sunday evening via WhatsApp / SMS directly to your phone.
                    </p>
                  </div>
                </div>

                {/* View Switcher */}
                <div className="flex items-center gap-1 bg-slate-100 p-1 rounded-xl self-start sm:self-auto">
                  <button
                    onClick={() => setPulseViewMode('bubble')}
                    className={`px-3 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                      pulseViewMode === 'bubble'
                        ? 'bg-white text-slate-900 shadow-2xs'
                        : 'text-slate-500 hover:text-slate-800'
                    }`}
                  >
                    WhatsApp View
                  </button>
                  <button
                    onClick={() => setPulseViewMode('table')}
                    className={`px-3 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                      pulseViewMode === 'table'
                        ? 'bg-white text-slate-900 shadow-2xs'
                        : 'text-slate-500 hover:text-slate-800'
                    }`}
                  >
                    Full Metrics
                  </button>
                </div>
              </div>

              {/* Main Pulse Body */}
              <div className="p-5">
                {pulseViewMode === 'bubble' ? (
                  /* Authentic WhatsApp Message Bubble */
                  <div className="bg-[#EFEAE2] p-4 sm:p-5 rounded-2xl border border-slate-200 space-y-3 font-sans">
                    <div className="flex items-center justify-between text-xs text-slate-600 font-mono">
                      <span className="flex items-center gap-1.5 font-sans">
                        <span className="w-2.5 h-2.5 rounded-full bg-[#25D366] inline-block" />
                        <strong>Fundile Academic Pulse Bot</strong> • Verified Sender
                      </span>
                      <span>Sunday 18:00 SAST</span>
                    </div>

                    {/* WhatsApp Chat Bubble */}
                    <div className="bg-[#E7FFDB] rounded-2xl rounded-tl-xs p-4 shadow-xs border border-emerald-200/60 text-slate-800 text-sm space-y-3 leading-relaxed">
                      <div className="border-b border-emerald-200/50 pb-2">
                        <p className="font-bold text-[#13519C]">
                          📊 FUNDILE ACADEMIC PULSE: {activeLearner.name.toUpperCase()}
                        </p>
                        <p className="text-xs text-slate-600">
                          Period: Mon 22 Sep – Sun 28 Sep 2026 • {activeLearner.grade}
                        </p>
                      </div>

                      {/* Stat summary lines */}
                      <div className="space-y-1.5 text-xs sm:text-sm">
                        <div className="flex items-center gap-2">
                          <span>⏱️</span>
                          <span>
                            <strong>Total Focus Time:</strong> {activeLearner.focusTime} ({activeLearner.streakDays}-day streak 🔥)
                          </span>
                        </div>
                        <div className="flex items-center gap-2">
                          <span>🎯</span>
                          <span>
                            <strong>Drill Output:</strong> {activeLearner.questionsCompleted} questions completed • <strong>{activeLearner.accuracyRate}% accuracy</strong>
                          </span>
                        </div>
                        <div className="flex items-center gap-2">
                          <span>📶</span>
                          <span>
                            <strong>Bandwidth Used:</strong> {activeLearner.dataUsedMB} MB (<span className="text-emerald-700 font-bold">99.6% data savings</span>)
                          </span>
                        </div>
                      </div>

                      {/* Mastered Topics */}
                      <div className="bg-white/80 p-3 rounded-xl border border-emerald-200/60 text-xs space-y-1.5">
                        <p className="font-bold text-slate-900 flex items-center gap-1.5">
                          <Award className="w-3.5 h-3.5 text-[#FF9100]" />
                          <span>CAPS Topics Mastered This Week:</span>
                        </p>
                        <ul className="space-y-1 pl-1 text-slate-700">
                          {activeLearner.masteredTopics.map((top, idx) => (
                            <li key={idx} className="flex items-center justify-between">
                              <span className="truncate pr-2">• {top.name}</span>
                              <span className="font-mono font-bold text-emerald-700 shrink-0">{top.score}%</span>
                            </li>
                          ))}
                        </ul>
                      </div>

                      {/* Repaired Misconception */}
                      <div className="bg-amber-50/90 p-3 rounded-xl border border-amber-200 text-xs space-y-1">
                        <p className="font-bold text-amber-900 flex items-center gap-1.5">
                          <CheckCircle2 className="w-3.5 h-3.5 text-amber-600" />
                          <span>Repaired Misconception (Cognitive Fix):</span>
                        </p>
                        <p className="text-amber-950 font-medium">
                          <strong>{activeLearner.repairedMisconceptions[0]?.topic}:</strong> {activeLearner.repairedMisconceptions[0]?.issue}
                        </p>
                        <p className="text-slate-600 text-[11px]">
                          Fix: {activeLearner.repairedMisconceptions[0]?.resolution}
                        </p>
                      </div>

                      {/* Dinner table coaching trigger */}
                      <div className="bg-blue-50/80 p-3 rounded-xl border border-blue-200 text-xs space-y-1">
                        <p className="font-bold text-[#13519C] flex items-center gap-1.5">
                          <Lightbulb className="w-3.5 h-3.5 text-[#FF9100]" />
                          <span>Recommended Dinner-Table Coaching Question:</span>
                        </p>
                        <p className="italic text-slate-800">
                          &quot;{activeLearner.coachingTips[0]?.prompt}&quot;
                        </p>
                      </div>

                      {/* WhatsApp timestamp & double tick */}
                      <div className="flex items-center justify-end gap-1 text-[11px] text-slate-400 font-mono pt-1">
                        <span>18:00</span>
                        <span className="text-[#34B7F1] font-bold">✓✓</span>
                      </div>
                    </div>
                  </div>
                ) : (
                  /* Structured Full Metrics View */
                  <div className="space-y-4">
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                      <div className="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                        <span className="text-xs text-slate-500 font-medium">Weekly Total Active Focus</span>
                        <div className="text-xl font-bold font-mono text-slate-900 mt-1">{activeLearner.focusTime}</div>
                        <span className="text-xs text-slate-500">Across 6 targeted daily micro-drills</span>
                      </div>
                      <div className="p-3.5 bg-slate-50 rounded-xl border border-slate-200">
                        <span className="text-xs text-slate-500 font-medium">Cognitive Accuracy</span>
                        <div className="text-xl font-bold font-mono text-emerald-600 mt-1">{activeLearner.accuracyRate}%</div>
                        <span className="text-xs text-slate-500">{activeLearner.questionsCompleted} CAPS questions answered</span>
                      </div>
                    </div>

                    {/* Mastered topics list */}
                    <div className="p-4 bg-slate-50 rounded-xl border border-slate-200">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-slate-600 mb-2 flex items-center gap-1.5">
                        <Award className="w-3.5 h-3.5 text-amber-500" />
                        <span>CAPS Curriculum Mastery Unlocked</span>
                      </h3>
                      <div className="space-y-2">
                        {activeLearner.masteredTopics.map((topic, i) => (
                          <div key={i} className="flex items-center justify-between text-xs bg-white p-2.5 rounded-lg border border-slate-200">
                            <div>
                              <span className="font-semibold text-slate-800">{topic.name}</span>
                              <span className="ml-2 text-slate-400">({topic.subject})</span>
                            </div>
                            <span className="font-mono font-bold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded-md">
                              {topic.score}%
                            </span>
                          </div>
                        ))}
                      </div>
                    </div>

                    {/* Repaired Misconceptions Full List */}
                    <div className="p-4 bg-amber-50/60 rounded-xl border border-amber-200">
                      <h3 className="text-xs font-bold uppercase tracking-wider text-amber-900 mb-2 flex items-center gap-1.5">
                        <AlertTriangle className="w-3.5 h-3.5 text-amber-600" />
                        <span>Cognitive Misconceptions Diagnosed & Repaired</span>
                      </h3>
                      <div className="space-y-2">
                        {activeLearner.repairedMisconceptions.map((mis, idx) => (
                          <div key={idx} className="bg-white p-3 rounded-lg border border-amber-200/80 text-xs">
                            <div className="flex items-center justify-between">
                              <span className="font-bold text-amber-950">{mis.topic}</span>
                              <span className="text-[11px] text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded font-semibold">
                                {mis.status}
                              </span>
                            </div>
                            <p className="text-slate-700 mt-1 font-medium">{mis.issue}</p>
                            <p className="text-slate-500 text-[11px] mt-1">{mis.resolution}</p>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Pulse Action Toolbar */}
            <div className="p-4 bg-slate-50 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3">
              <div className="flex items-center gap-2">
                <button
                  onClick={handleSendTestPulse}
                  className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold transition cursor-pointer shadow-2xs"
                >
                  <Share2 className="w-3.5 h-3.5" />
                  <span>Send Test WhatsApp Pulse</span>
                </button>

                <button
                  onClick={handleCopyPulse}
                  className="inline-flex items-center gap-1.5 px-3 py-2 rounded-xl border border-slate-300 hover:bg-white text-xs font-semibold text-slate-700 transition cursor-pointer"
                >
                  {copiedPulseText ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5 text-slate-500" />}
                  <span>{copiedPulseText ? 'Copied to Clipboard!' : 'Copy Summary'}</span>
                </button>
              </div>

              <div className="text-xs text-slate-600 flex items-center gap-1.5">
                <Calendar className="w-3.5 h-3.5 text-slate-500" />
                <span>Next automated dispatch: <strong>Sunday at 18:00</strong></span>
              </div>
            </div>
          </section>

          {/* ── HOUSEHOLD DATA SAVINGS METER (5 COLS) ── */}
          <section className="lg:col-span-5 bg-white border border-slate-200/90 rounded-2xl shadow-xs p-5 flex flex-col justify-between">
            <div className="space-y-4">
              {/* Header */}
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-600 border border-blue-200 flex items-center justify-center shrink-0">
                  <Zap className="w-5 h-5 text-[#13519C]" />
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <h2 className="text-lg font-bold text-slate-900 font-afacad">
                      Cellular Data Savings Meter
                    </h2>
                    <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-emerald-100 text-emerald-800">
                      &lt; 2 MB / week
                    </span>
                  </div>
                  <p className="text-xs text-slate-500">
                    Client-side vector engine vs heavy video streaming tutoring.
                  </p>
                </div>
              </div>

              {/* Big Financial Highlight Card */}
              <div className="p-4 rounded-2xl bg-gradient-to-br from-[#13519C] to-[#0f3e77] text-white shadow-xs">
                <span className="text-xs uppercase tracking-wider font-semibold text-blue-200">
                  Total Mobile Airtime Saved This Month
                </span>
                <div className="text-3xl sm:text-4xl font-bold font-mono mt-1 tracking-tight flex items-baseline gap-2">
                  <span>R{totalSavedRands}</span>
                  <span className="text-xs font-normal text-blue-200">across 2 learners</span>
                </div>
                <p className="text-xs text-blue-100/90 mt-2 leading-relaxed">
                  Fundile caches full CAPS scaffolds locally in an offline PWA. No YouTube buffering, zero unexpected out-of-bundle airtime charges.
                </p>
              </div>

              {/* Visual Bandwidth Comparison Bar */}
              <div className="space-y-3 p-4 bg-slate-50 rounded-2xl border border-slate-200">
                <h3 className="text-xs font-bold text-slate-700 uppercase tracking-wider">
                  Weekly Bandwidth Consumption Comparison
                </h3>

                {/* Fundile Bar */}
                <div className="space-y-1">
                  <div className="flex justify-between text-xs font-semibold">
                    <span className="text-[#13519C] flex items-center gap-1">
                      <Zap className="w-3.5 h-3.5" /> Fundile Offline PWA
                    </span>
                    <span className="font-mono text-emerald-600 font-bold">{activeLearner.dataUsedMB} MB</span>
                  </div>
                  <div className="w-full bg-slate-200 h-3 rounded-full overflow-hidden">
                    <div
                      className="bg-emerald-500 h-full rounded-full transition-all duration-500"
                      style={{ width: `${Math.max(2, (activeLearner.dataUsedMB / activeLearner.videoEquivalentMB) * 100)}%` }}
                    />
                  </div>
                  <span className="text-[11px] text-slate-500">Uses compressed JSON &amp; vector SVG</span>
                </div>

                {/* Video Streaming Bar */}
                <div className="space-y-1 pt-2">
                  <div className="flex justify-between text-xs font-semibold">
                    <span className="text-rose-600 flex items-center gap-1">
                      <Smartphone className="w-3.5 h-3.5" /> Video Streaming Tutoring
                    </span>
                    <span className="font-mono text-rose-600 font-bold">{activeLearner.videoEquivalentMB} MB</span>
                  </div>
                  <div className="w-full bg-slate-200 h-3 rounded-full overflow-hidden">
                    <div className="bg-rose-500 h-full rounded-full w-full" />
                  </div>
                  <span className="text-[11px] text-slate-500">Heavy 720p/1080p video stream buffering</span>
                </div>

                {/* Efficiency calculation */}
                <div className="mt-3 pt-3 border-t border-slate-200 text-xs flex items-center justify-between text-slate-600">
                  <span>Bandwidth Efficiency:</span>
                  <span className="font-mono font-bold text-emerald-700 bg-emerald-100/70 px-2 py-0.5 rounded">
                    99.6% Data Reduction
                  </span>
                </div>
              </div>

              {/* Data Efficiency Highlights */}
              <div className="space-y-2 text-xs text-slate-600">
                <div className="flex items-start gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                  <span>
                    <strong>Load Shedding Resilient:</strong> Continues running smoothly when mobile towers revert to low-speed 2G/3G backup power.
                  </span>
                </div>
                <div className="flex items-start gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                  <span>
                    <strong>Household Data Pool:</strong> Combined weekly total across {Object.keys(learners).length} learners is just <strong>{totalMBUsed} MB</strong> vs <strong>{totalVideoEquivalentMB} MB</strong> streaming equivalent.
                  </span>
                </div>
              </div>
            </div>

            {/* Micro summary */}
            <div className="mt-4 pt-3 border-t border-slate-100 text-[11px] text-slate-600 flex items-center justify-between">
              <span>Standard Vodacom/MTN data rate saved:</span>
              <span className="font-mono font-bold text-slate-800">~R0.85 per MB out-of-bundle</span>
            </div>
          </section>
        </div>

        {/* ── ACTIONABLE DINNER-TABLE COACHING RECOMMENDATIONS ── */}
        <section className="bg-white border border-slate-200/90 rounded-2xl shadow-xs p-5 sm:p-6 space-y-4">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-600 border border-amber-200 flex items-center justify-center shrink-0">
                <Lightbulb className="w-5 h-5 text-[#FF9100]" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h2 className="text-xl font-bold text-slate-900 font-afacad">
                    Dinner-Table Coaching Recommendations
                  </h2>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-[#13519C]/10 text-[#13519C]">
                    Zero-Nagging Guarantee
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-500">
                  Positive, curiosity-driven conversation starters for {activeLearner.name}. No stressful interrogation required.
                </p>
              </div>
            </div>

            <div className="text-xs text-slate-500 flex items-center gap-1.5 self-start sm:self-auto bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200">
              <Info className="w-3.5 h-3.5 text-[#13519C]" />
              <span>Tailored automatically to today&apos;s cognitive mastery</span>
            </div>
          </div>

          {/* Coaching Tip Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {activeLearner.coachingTips.map((tip) => {
              const isCopied = copiedTipId === tip.id;
              return (
                <div
                  key={tip.id}
                  className="bg-slate-50 hover:bg-slate-100/70 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between transition group shadow-2xs"
                >
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="text-xl">{tip.icon}</span>
                      <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full border ${tip.badgeColor}`}>
                        {tip.category}
                      </span>
                    </div>

                    <p className="text-sm font-semibold text-slate-900 leading-snug">
                      &quot;{tip.prompt}&quot;
                    </p>

                    <p className="text-xs text-slate-500 leading-relaxed border-t border-slate-200/60 pt-2.5">
                      <strong className="text-slate-700">Why it works:</strong> {tip.rationale}
                    </p>
                  </div>

                  <div className="mt-4 pt-3 flex items-center justify-between">
                    <button
                      onClick={() => handleCopyTip(tip.id, tip.prompt)}
                      className="inline-flex items-center gap-1 text-xs font-semibold text-[#13519C] hover:text-[#0f3e77] transition cursor-pointer"
                    >
                      {isCopied ? <Check className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5" />}
                      <span>{isCopied ? 'Copied question!' : 'Copy to phone'}</span>
                    </button>
                    <span className="text-[11px] text-slate-500 font-mono">Dinner starter</span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Dinner Table Mindset Helper */}
          <div className="bg-emerald-50/70 border border-emerald-200 rounded-xl p-3.5 flex items-center gap-3 text-xs text-emerald-900">
            <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0" />
            <span>
              <strong>Tip for parents:</strong> Avoid asking <em>&quot;Did you do your homework?&quot;</em> — instead, ask them to explain a topic they mastered. It validates their hard work and sparks genuine pride!
            </span>
          </div>
        </section>

        {/* ── LIVE DUAL-RING MASTERY DIAL PREVIEW OF ACTIVE SUBJECTS ── */}
        <section className="bg-white border border-slate-200/90 rounded-2xl shadow-xs p-5 sm:p-6 space-y-5">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-indigo-500/10 text-indigo-600 border border-indigo-200 flex items-center justify-center shrink-0">
                <BarChart3 className="w-5 h-5 text-[#13519C]" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h2 className="text-xl font-bold text-slate-900 font-afacad">
                    Live Dual-Ring Subject Mastery
                  </h2>
                  <span className="px-2 py-0.5 rounded-full text-xs font-bold bg-[#FF9100]/15 text-[#f58200]">
                    CAPS Aligned
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-500">
                  Evaluative Exam Accuracy (Outer Amber Ring) vs Formative BKT Knowledge State (Inner Green Ring) for {activeLearner.name}.
                </p>
              </div>
            </div>

            {/* Legend */}
            <div className="flex items-center gap-3 text-xs font-mono self-start sm:self-auto bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200">
              <span className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-full bg-[#10B981]" />
                <span className="text-slate-700">Inner: BKT Mastery</span>
              </span>
              <span className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-full bg-[#F59E0B]" />
                <span className="text-slate-700">Outer: Exam Score</span>
              </span>
            </div>
          </div>

          {/* Subject Cards Grid with Dual-Ring MasteryDial */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
            {activeLearner.subjects.map((sub) => (
              <div
                key={sub.id}
                className="bg-slate-50/70 border border-slate-200 rounded-2xl p-4 flex flex-col justify-between hover:border-slate-300 transition"
              >
                <div>
                  {/* Subject Title & Code */}
                  <div className="flex items-center justify-between mb-2">
                    <div>
                      <h3 className="font-bold text-slate-900 text-sm">{sub.name}</h3>
                      <span className="text-[11px] font-mono text-slate-400">{sub.code}</span>
                    </div>
                    <span className="px-2 py-0.5 rounded-full text-[11px] font-bold bg-white border border-slate-200 text-slate-700 shadow-2xs">
                      {sub.level}
                    </span>
                  </div>

                  {/* Dual Ring MasteryDial */}
                  <div className="py-2">
                    <MasteryDial
                      formativeMastery={sub.formativeMastery}
                      evaluativeScore={sub.evaluativeScore}
                      size={135}
                      strokeWidth={8}
                      variant="light"
                      isRefreshRecommended={sub.needsRefresh}
                      onTriggerRefresher={() => {
                        setPulseToastMessage(`🎯 2-Question Refresher Sprint triggered for ${activeLearner.name} in ${sub.name}!`);
                        setTimeout(() => setPulseToastMessage(''), 4000);
                      }}
                    />
                  </div>

                  {/* Recent Topics Covered */}
                  <div className="mt-3 pt-3 border-t border-slate-200/80">
                    <span className="text-[11px] font-bold uppercase tracking-wider text-slate-600 block mb-1.5">
                      Recent Topic Drills
                    </span>
                    <ul className="space-y-1 text-xs text-slate-600">
                      {sub.recentTopics.map((topic, tidx) => (
                        <li key={tidx} className="flex items-center gap-1.5 truncate">
                          <span className="w-1.5 h-1.5 rounded-full bg-[#13519C]" />
                          <span className="truncate">{topic}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                </div>

                <div className="mt-4 pt-2 border-t border-slate-200/60 flex items-center justify-between text-[11px] text-slate-600">
                  <span>Rating:</span>
                  <span className="font-semibold text-slate-800">{sub.rating}</span>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* ── SUBSCRIPTION & INVOICING CARD ── */}
        <section className="bg-white border border-slate-200/90 rounded-2xl shadow-xs p-5 sm:p-6 space-y-4">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
            <div className="flex items-center gap-3.5">
              <div className="w-11 h-11 rounded-2xl bg-[#13519C]/10 text-[#13519C] border border-[#13519C]/20 flex items-center justify-center shrink-0">
                <CreditCard className="w-5 h-5 text-[#13519C]" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <h2 className="text-lg sm:text-xl font-bold text-slate-900 font-afacad">
                    Fundile Household Plan &amp; Billing
                  </h2>
                  <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-emerald-50 text-emerald-700 border border-emerald-200">
                    Active • 2 Learners Linked
                  </span>
                </div>
                <p className="text-xs sm:text-sm text-slate-500">
                  Full access for Nqobile and Sipho • Next renewal: <strong>15 October 2026</strong> (R149.00 / month incl. VAT)
                </p>
              </div>
            </div>

            {/* Invoicing Action Buttons */}
            <div className="flex items-center gap-2.5 flex-wrap">
              <button
                onClick={() => setIsInvoiceModalOpen(true)}
                className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-slate-50 hover:bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-700 transition cursor-pointer shadow-2xs"
              >
                <FileText className="w-3.5 h-3.5 text-[#13519C]" />
                <span>Download Tax Invoice / Receipt</span>
              </button>

              <button
                onClick={() => {
                  setPaymentPlan({
                    tier: 'pro',
                    name: 'Fundile Household Plan',
                    price: 149,
                    billingCycle: 'monthly',
                  });
                  setIsPaymentModalOpen(true);
                }}
                className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 border border-slate-300 text-xs font-semibold transition cursor-pointer shadow-2xs"
              >
                <CreditCard className="w-3.5 h-3.5 text-slate-600" />
                <span>Manage Payment Method</span>
              </button>

              <button
                onClick={() => {
                  setPaymentPlan({
                    tier: 'pro',
                    name: 'Fundile Household Plan (Annual Pro)',
                    price: 1428,
                    billingCycle: 'annual',
                  });
                  setIsPaymentModalOpen(true);
                }}
                className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-semibold transition cursor-pointer shadow-2xs"
              >
                <Sparkles className="w-3.5 h-3.5 text-amber-300" />
                <span>Renew / Upgrade Plan</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2 text-xs text-slate-600">
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-slate-600 block">Current Billing Cycle</span>
              <strong className="text-slate-900 font-mono text-sm">{householdBilling.cycle}</strong>
            </div>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-slate-600 block">Linked Learners</span>
              <strong className="text-slate-900 text-sm">Nqobile (Gr 10) &amp; Sipho (Gr 8)</strong>
            </div>
            <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
              <span className="text-slate-600 block">Payment Method</span>
              <strong className="text-slate-900 text-sm">{householdBilling.method}</strong>
            </div>
          </div>
        </section>

      </main>

      {/* ── MODAL 1: ADD CHILD MODAL ── */}
      {isAddChildModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs animate-in fade-in duration-200">
          <div className="bg-white border border-slate-200 rounded-2xl shadow-2xl max-w-md w-full overflow-hidden text-slate-900">
            
            {/* Modal Header */}
            <div className="p-5 border-b border-slate-100 flex items-center justify-between">
              <div className="flex items-center gap-2.5">
                <div className="w-9 h-9 rounded-xl bg-[#13519C]/10 text-[#13519C] flex items-center justify-center">
                  <UserPlus className="w-4 h-4" />
                </div>
                <div>
                  <h3 className="font-bold text-base text-slate-900 font-afacad">
                    Link a Learner to Your Portal
                  </h3>
                  <p className="text-xs text-slate-500">
                    Connect your child&apos;s phone in under 60 seconds
                  </p>
                </div>
              </div>
              <button
                onClick={() => setIsAddChildModalOpen(false)}
                className="text-slate-400 hover:text-slate-600 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Body Form */}
            <form onSubmit={handleAddChildSubmit} className="p-5 space-y-4 text-xs">
              {addChildError && (
                <div className="p-3 rounded-xl bg-rose-50 border border-rose-200 text-rose-700 text-xs">
                  {addChildError}
                </div>
              )}

              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  Learner Full Name
                </label>
                <input
                  type="text"
                  placeholder="e.g. Andile Dlamini"
                  value={addChildForm.name}
                  onChange={(e) => setAddChildForm(prev => ({ ...prev, name: e.target.value }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:border-[#13519C] text-sm"
                  required
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  Grade / Phase
                </label>
                <select
                  value={addChildForm.grade}
                  onChange={(e) => setAddChildForm(prev => ({ ...prev, grade: e.target.value }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:border-[#13519C] text-sm bg-white"
                >
                  <option value="Grade 8 Senior Phase">Grade 8 Senior Phase</option>
                  <option value="Grade 9 Senior Phase">Grade 9 Senior Phase</option>
                  <option value="Grade 10 FET">Grade 10 FET</option>
                  <option value="Grade 11 FET">Grade 11 FET</option>
                  <option value="Grade 12 Matric FET">Grade 12 Matric FET</option>
                </select>
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  School Name (Optional)
                </label>
                <input
                  type="text"
                  placeholder="e.g. Phakamani Secondary School"
                  value={addChildForm.school}
                  onChange={(e) => setAddChildForm(prev => ({ ...prev, school: e.target.value }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:border-[#13519C] text-sm"
                />
              </div>

              <div>
                <label className="block font-semibold text-slate-700 mb-1">
                  6-Character Learner Link Code
                </label>
                <input
                  type="text"
                  placeholder="e.g. PAR8M4"
                  maxLength={8}
                  value={addChildForm.linkCode}
                  onChange={(e) => setAddChildForm(prev => ({ ...prev, linkCode: e.target.value.toUpperCase() }))}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 focus:outline-none focus:border-[#13519C] font-mono text-base font-bold tracking-widest uppercase text-slate-900"
                  required
                />
                <p className="text-[11px] text-slate-600 mt-1.5 flex items-start gap-1">
                  <Info className="w-3.5 h-3.5 text-[#13519C] shrink-0 mt-0.5" />
                  <span>
                    Your child can find their link code inside their Fundile mobile app under: <strong>Profile &gt; Link Parent/Guardian</strong>.
                  </span>
                </p>
              </div>

              <div className="pt-2 flex items-center justify-end gap-2 border-t border-slate-100">
                <button
                  type="button"
                  onClick={() => setIsAddChildModalOpen(false)}
                  className="px-4 py-2 rounded-xl border border-slate-300 text-slate-600 hover:bg-slate-50 font-semibold cursor-pointer"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  className="px-5 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white font-semibold shadow-xs cursor-pointer"
                >
                  Connect Learner
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* ── MODAL 2: SARS-COMPLIANT TAX INVOICE / RECEIPT ── */}
      {isInvoiceModalOpen && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/60 backdrop-blur-xs animate-in fade-in duration-200">
          <div className="bg-white border border-slate-200 rounded-2xl shadow-2xl max-w-2xl w-full overflow-hidden text-slate-900 max-h-[90vh] flex flex-col">
            
            {/* Modal Header */}
            <div className="p-4 sm:p-5 border-b border-slate-200 flex items-center justify-between bg-slate-50">
              <div className="flex items-center gap-2">
                <FileText className="w-5 h-5 text-[#13519C]" />
                <h3 className="font-bold text-base text-slate-900 font-afacad">
                  Official SARS Tax Invoice &amp; Receipt
                </h3>
              </div>
              <button
                onClick={() => setIsInvoiceModalOpen(false)}
                className="text-slate-400 hover:text-slate-600 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Printable Tax Invoice Content */}
            <div className="p-6 overflow-y-auto space-y-6 text-xs text-slate-700 font-sans" id="printable-tax-invoice">
              
              {/* Invoice Header */}
              <div className="flex justify-between items-start border-b border-slate-200 pb-5">
                <div>
                  <h4 className="text-xl font-black text-[#13519C] font-mono tracking-tight">FUNDILE</h4>
                  <p className="text-[11px] text-slate-500 font-medium">Fundile Learning Technologies (Pty) Ltd</p>
                  <p className="text-[11px] text-slate-500">Reg No: 2024/182930/07</p>
                  <p className="text-[11px] text-slate-500">VAT Registration No: 4890284719</p>
                  <p className="text-[11px] text-slate-500">Rosebank Link, 173 Oxford Rd, Rosebank, 2196</p>
                </div>
                <div className="text-right">
                  <span className="px-2.5 py-1 rounded bg-emerald-100 text-emerald-800 text-[11px] font-bold uppercase tracking-wider">
                    Paid in Full
                  </span>
                  <div className="mt-2 text-slate-900 font-bold font-mono text-sm">
                    TAX INVOICE #INV-2026-09-8841
                  </div>
                  <p className="text-[11px] text-slate-500">Date: 28 September 2026</p>
                  <p className="text-[11px] text-slate-500">Payment Ref: PF-884192 (PayFast)</p>
                </div>
              </div>

              {/* Billed To */}
              <div className="grid grid-cols-2 gap-4 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div>
                  <span className="text-[11px] font-bold uppercase text-slate-600">Billed To (Guardian):</span>
                  <p className="font-bold text-slate-900 text-sm mt-0.5">{parentName}</p>
                  <p className="text-slate-600">{parentPhone}</p>
                  <p className="text-slate-600">nomvula.dlamini@fundile.parent.za</p>
                </div>
                <div>
                  <span className="text-[11px] font-bold uppercase text-slate-600">Covered Learners:</span>
                  <p className="text-slate-800 font-medium mt-0.5">• Nqobile Dlamini (Grade 10 FET)</p>
                  <p className="text-slate-800 font-medium">• Sipho Dlamini (Grade 8 Senior Phase)</p>
                </div>
              </div>

              {/* Line Items Table */}
              <div>
                <table className="w-full text-left border-collapse">
                  <thead>
                    <tr className="border-b border-slate-300 text-[11px] uppercase tracking-wider text-slate-500 font-semibold">
                      <th className="py-2">Description</th>
                      <th className="py-2 text-center">Period</th>
                      <th className="py-2 text-right">Qty</th>
                      <th className="py-2 text-right">Amount (excl. VAT)</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200">
                    <tr>
                      <td className="py-3">
                        <strong className="text-slate-900 font-medium">Fundile Household Family Plan</strong>
                        <p className="text-[11px] text-slate-500">Unlimited CAPS cognitive diagnostics, WhatsApp weekly pulse, &lt; 2 MB offline PWA</p>
                      </td>
                      <td className="py-3 text-center text-slate-600">Sep 2026</td>
                      <td className="py-3 text-right text-slate-600">1</td>
                      <td className="py-3 text-right font-mono font-medium text-slate-900">R129.57</td>
                    </tr>
                  </tbody>
                </table>
              </div>

              {/* Total Calculation */}
              <div className="border-t border-slate-200 pt-3 space-y-1.5 text-right font-mono">
                <div className="flex justify-between text-xs text-slate-600">
                  <span>Subtotal (Excl. VAT):</span>
                  <span>R129.57</span>
                </div>
                <div className="flex justify-between text-xs text-slate-600">
                  <span>Value Added Tax (15% VAT):</span>
                  <span>R19.43</span>
                </div>
                <div className="flex justify-between text-sm font-bold text-slate-900 border-t border-slate-200 pt-2">
                  <span>Total Paid (ZAR):</span>
                  <span className="text-[#13519C]">R149.00</span>
                </div>
              </div>

              <div className="p-3 rounded-xl bg-slate-50 border border-slate-200 text-[11px] text-slate-500 space-y-1">
                <p>This document serves as an official tax invoice in terms of Section 20 of the South African Value-Added Tax Act, 1991.</p>
                <p>For billing queries, contact support@fundile.co.za or WhatsApp Guardian Helpline +27 82 000 4819.</p>
              </div>
            </div>

            {/* Footer Actions */}
            <div className="p-4 bg-slate-50 border-t border-slate-200 flex items-center justify-between">
              <span className="text-xs text-slate-500 font-mono">Status: Verified EFT Complete</span>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => window.print()}
                  className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-white border border-slate-300 hover:bg-slate-100 text-xs font-semibold text-slate-700 transition cursor-pointer"
                >
                  <Printer className="w-3.5 h-3.5" />
                  <span>Print Receipt</span>
                </button>
                <button
                  onClick={() => {
                    setPulseToastMessage('📄 Tax invoice PDF downloaded to your device.');
                    setIsInvoiceModalOpen(false);
                  }}
                  className="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-semibold transition cursor-pointer"
                >
                  <Download className="w-3.5 h-3.5" />
                  <span>Download PDF</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── MODAL 3: IN-APP PAYMENT MODAL ── */}
      <InAppPaymentModal
        isOpen={isPaymentModalOpen}
        onClose={() => setIsPaymentModalOpen(false)}
        plan={paymentPlan}
        onSuccess={handlePaymentSuccess}
      />

    </div>
  );
}
