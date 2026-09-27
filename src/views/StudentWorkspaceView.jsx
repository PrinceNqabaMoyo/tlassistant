import React, { useState, useEffect } from 'react';
import SubjectShelf from '../components/navigation/SubjectShelf';
import MasteryDial from '../components/student/MasteryDial';
import MicroBenchmarkModal from '../components/student/MicroBenchmarkModal';
import SimuLearnPlayer from '../components/simulearn/SimuLearnPlayer';
import XPProgressBar from '../components/gamification/XPProgressBar';
import GamificationSummary from '../components/gamification/GamificationSummary';
import ProgressMap from '../components/gamification/ProgressMap';
import ChallengeGate from '../components/gamification/ChallengeGate';
import ParentReportModal from '../components/student/ParentReportModal';
import ParentLinkModal from '../components/student/ParentLinkModal';
import StudentDashboard from '../components/student/StudentDashboard';
import OlympiadDashboard from '../components/olympiad/OlympiadDashboard';
import NotificationBell from '../components/navigation/NotificationBell';
import CognitivePacingAlert from '../components/student/CognitivePacingAlert';
import { Workspace } from '../components/workspace';
import { telemetryBuffer } from '../utils/telemetryBuffer';

export default function StudentWorkspaceView(props) {
  const {
    currentSubject,
    currentGrade,
    topic,
    onSelectSubject,
    onSelectTopic,
    masteryScores = {},
    ...workspaceProps
  } = props;

  const [viewMode, setViewMode] = useState('dashboard'); // 'dashboard' | 'practice' | 'curriculum_map'
  const [showBenchmark, setShowBenchmark] = useState(false);
  const [showSimuLearn, setShowSimuLearn] = useState(false);
  const [showTrophyRoom, setShowTrophyRoom] = useState(false);
  const [showParentReport, setShowParentReport] = useState(false);
  const [showParentLink, setShowParentLink] = useState(false);
  const [activeChallengeKey, setActiveChallengeKey] = useState(null);
  const [formativeMastery, setFormativeMastery] = useState(65);
  const [evaluativeScore, setEvaluativeScore] = useState(72);
  const [totalXP, setTotalXP] = useState(1450);
  const [level, setLevel] = useState(4);
  const [streakDays, setStreakDays] = useState(5);

  // Initialize telemetry on topic change
  useEffect(() => {
    if (topic?.name || topic?.id) {
      telemetryBuffer.startQuestion(topic.id || topic.name);
    }
  }, [topic]);

  const handleCompleteBenchmark = (answers) => {
    setShowBenchmark(false);
    setFormativeMastery(75);
    setTotalXP(prev => prev + 50);
  };

  const handleSelectTopicFromMap = (selectedNode) => {
    if (onSelectTopic) {
      onSelectTopic(selectedNode);
    }
    setViewMode('practice');
  };

  // Determine archetype key based on current subject
  const getSimuLearnKey = () => {
    const subj = (currentSubject || '').toLowerCase();
    if (subj.includes('account') || subj.includes('ems')) return 'accounting_crj_vat';
    if (subj.includes('physic') || subj.includes('science')) return 'physics_kinematics_dx';
    if (subj.includes('life') || subj.includes('bio')) return 'lifesciences_punnett_square';
    if (subj.includes('lit') || subj.includes('tax')) return 'mathlit_sars_income_tax';
    return 'math_quadratic_trinomial';
  };

  const getChallengeKey = () => {
    const subj = (currentSubject || '').toLowerCase();
    if (subj.includes('account') || subj.includes('ems')) return 'accounting_10_sole_trader_crj';
    return 'mathematics_10_algebraic_expressions';
  };

  return (
    <div className="flex flex-col min-h-screen bg-slate-50 text-slate-900">
      {/* 1-Tap Pinned Subject Shelf */}
      <SubjectShelf
        currentSubject={currentSubject || 'Mathematics'}
        currentGrade={currentGrade || '10'}
        masterySummary={masteryScores}
        onSelectSubject={onSelectSubject}
      />

      {/* Sub-Header Mode Switcher: Dashboard vs Practice Mode vs Curriculum Map */}
      <div className="w-full bg-white/95 border-b border-slate-200 px-4 py-2 flex items-center justify-between gap-3 max-w-7xl mx-auto flex-wrap shadow-2xs">
        <div className="flex items-center bg-slate-100 rounded-xl p-1 border border-slate-200">
          <button
            onClick={() => setViewMode('dashboard')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              viewMode === 'dashboard'
                ? 'bg-white text-brand-blue shadow-xs font-bold ring-1 ring-slate-200'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            📊 Dashboard
          </button>
          <button
            onClick={() => setViewMode('practice')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              viewMode === 'practice'
                ? 'bg-white text-brand-blue shadow-xs font-bold ring-1 ring-slate-200'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            ⚡ Practice Mode
          </button>
          <button
            onClick={() => setViewMode('curriculum_map')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all flex items-center gap-1.5 cursor-pointer ${
              viewMode === 'curriculum_map'
                ? 'bg-white text-brand-blue shadow-xs font-bold ring-1 ring-slate-200'
                : 'text-slate-600 hover:text-slate-900'
            }`}
          >
            <span>🗺️ Curriculum Map</span>
            <span className="w-1.5 h-1.5 rounded-full bg-brand-orange" />
          </button>
          <button
            onClick={() => setViewMode('olympiad')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all flex items-center gap-1.5 cursor-pointer ${
              viewMode === 'olympiad'
                ? 'bg-amber-100 text-amber-900 font-bold shadow-xs'
                : 'text-amber-700 hover:text-amber-800'
            }`}
          >
            <span>🏆 Olympiad</span>
          </button>
        </div>

        <div className="flex items-center gap-2.5">
          <NotificationBell />
          <button
            onClick={() => setActiveChallengeKey(getChallengeKey())}
            className="px-3 py-1.5 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-200 text-xs font-semibold transition-colors flex items-center gap-1.5 shadow-2xs"
          >
            <span>🏅</span> Take Milestone Challenge
          </button>
        </div>
      </div>

      {/* Main Container */}
      {viewMode === 'dashboard' ? (
        <div className="flex-1 p-3 sm:p-6 max-w-7xl mx-auto w-full">
          <StudentDashboard
            currentUser={{ name: 'Learner', grade: currentGrade || '10', curriculum: 'CAPS' }}
            onNavigateToSubject={(subjId) => {
              if (onSelectSubject) onSelectSubject(subjId);
              setViewMode('practice');
            }}
            onOpenSimuLearn={() => setShowSimuLearn(true)}
            onOpenReport={() => setShowParentReport(true)}
            onOpenGamification={() => setShowTrophyRoom(true)}
            onOpenOlympiad={() => setViewMode('olympiad')}
            onOpenSubscription={() => alert('Subscription Modal Opened')}
            onOpenParentLink={() => setShowParentLink(true)}
            daysRemaining={12}
            userStats={{
              xp: totalXP,
              level: level,
              streakDays: streakDays,
              sessionsCompleted: 18,
              recentScores: [68, 75, 82, 78, 88],
            }}
          />
        </div>
      ) : viewMode === 'olympiad' ? (
        <div className="flex-1 p-3 sm:p-6 max-w-7xl mx-auto w-full">
          <OlympiadDashboard
            currentUser={{ name: 'Learner', grade: currentGrade || '10' }}
            isCapsQualified={true}
            onBackToWorkspace={() => setViewMode('practice')}
          />
        </div>
      ) : viewMode === 'curriculum_map' ? (
        <div className="flex-1 p-3 sm:p-6 max-w-7xl mx-auto w-full">
          <ProgressMap
            subject={currentSubject || 'Mathematics'}
            grade={currentGrade || '10'}
            onSelectTopicForPractice={handleSelectTopicFromMap}
            onOpenTrophyRoom={() => setShowTrophyRoom(true)}
          />
        </div>
      ) : (
        <div className="flex-1 flex flex-col lg:flex-row gap-4 p-3 sm:p-4 max-w-7xl mx-auto w-full">
          {/* Main Learning Workspace */}
          <main className="flex-1 flex flex-col min-w-0 bg-white rounded-2xl border border-slate-200 shadow-sm p-3 sm:p-5 overflow-hidden">
            <Workspace
              {...workspaceProps}
              topic={topic}
              selectedSubject={currentSubject}
              selectedGrade={currentGrade}
            />
          </main>

          {/* Diagnostic Sidebar with Dual-Track Mastery Dial, XP Bar & SimuLearn Trigger */}
          <aside className="w-full lg:w-72 shrink-0 flex flex-col gap-4">
            <XPProgressBar
              level={level}
              currentXP={totalXP}
              progressPercent={68}
              streakDays={streakDays}
              onClick={() => setShowTrophyRoom(true)}
            />

            <MasteryDial
              formativeMastery={formativeMastery}
              evaluativeScore={evaluativeScore}
            />

            <div className="p-4 bg-white rounded-2xl border border-slate-200 text-xs text-slate-600 space-y-3 shadow-sm">
              <h4 className="font-semibold text-slate-900">SimuLearn Diagnostic</h4>
              <p>Struggling with the concept? Watch a high-clarity canonical worked simulation at 0.1% data cost.</p>
              <button
                onClick={() => setShowSimuLearn(true)}
                className="w-full py-2 px-3 rounded-lg bg-brand-blue hover:bg-brand-cobalt text-white font-semibold transition-colors text-center flex items-center justify-center gap-1.5 shadow-xs cursor-pointer"
              >
                <span>🎥</span> Watch Step Simulation
              </button>
              <button
                onClick={() => setShowParentReport(true)}
                className="w-full py-2 px-3 rounded-lg bg-blue-50 hover:bg-blue-100 text-brand-blue font-semibold transition-colors text-center flex items-center justify-center gap-1.5 border border-blue-200 cursor-pointer"
              >
                <span>📄</span> Diagnostic Academic Report
              </button>
              <button
                onClick={() => setShowBenchmark(true)}
                className="w-full py-1.5 px-3 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition-colors text-center border border-slate-200"
              >
                Recalibrate Benchmark Level
              </button>
            </div>
          </aside>
        </div>
      )}

      {/* Parent & Student Diagnostic Report Modal */}
      <ParentReportModal
        isOpen={showParentReport}
        onClose={() => setShowParentReport(false)}
        studentName="Learner"
        grade={currentGrade || '10'}
        streakDays={streakDays}
        totalXP={totalXP}
        subjectMastery={{
          [currentSubject || 'Mathematics']: formativeMastery,
          'Accounting': 82,
          'Physical Sciences': 68
        }}
      />

      {/* Parent Linking Modal (6-Character Code OQ1) */}
      <ParentLinkModal
        isOpen={showParentLink}
        onClose={() => setShowParentLink(false)}
        studentName={props.currentUser?.name || 'Thabo Ndlovu'}
        parentCode="PAR8M4"
        grade={currentGrade || '10'}
        onOpenReport={() => {
          setShowParentLink(false);
          setShowParentReport(true);
        }}
      />

      {/* Challenge Examination Gate Modal */}
      <ChallengeGate
        isOpen={!!activeChallengeKey}
        challengeKey={activeChallengeKey}
        onClose={() => setActiveChallengeKey(null)}
        onChallengePassed={(result) => {
          setTotalXP(prev => prev + (result.xp_awarded || 100));
        }}
        onViewTrophyRoom={() => {
          setActiveChallengeKey(null);
          setShowTrophyRoom(true);
        }}
      />

      {/* Trophy Room Modal */}
      <GamificationSummary
        isOpen={showTrophyRoom}
        onClose={() => setShowTrophyRoom(false)}
        totalXP={totalXP}
        level={level}
        streakDays={streakDays}
      />

      {/* SimuLearn Animation Player Modal */}
      <SimuLearnPlayer
        isOpen={showSimuLearn}
        archetypeKey={getSimuLearnKey()}
        onClose={() => setShowSimuLearn(false)}
        onComplete={() => setShowSimuLearn(false)}
      />

      {/* 3-Question Micro-Benchmark Modal */}
      <MicroBenchmarkModal
        isOpen={showBenchmark}
        topicTitle={topic?.name || topic?.title || 'Current Topic'}
        subject={currentSubject || 'Mathematics'}
        grade={currentGrade || '10'}
        currentUser={props.currentUser}
        onCompleteBenchmark={handleCompleteBenchmark}
        onClose={() => setShowBenchmark(false)}
      />

      {/* 45-Minute Cognitive Pacing Guardrail */}
      <CognitivePacingAlert
        onOpenSimuLearn={() => setShowSimuLearn(true)}
        isPracticing={viewMode === 'practice'}
      />
    </div>
  );
}


