import React, { useState } from 'react';
import { 
  Lock, 
  CheckCircle2, 
  Play, 
  Trophy, 
  Award, 
  Sparkles, 
  ChevronRight, 
  X,
  BookOpen,
  ArrowRight
} from 'lucide-react';
import ChallengeGate from './ChallengeGate';
import SimuLearnPlayer from '../simulearn/SimuLearnPlayer';

const SAMPLE_CURRICULUM_DATA = {
  Mathematics: {
    10: [
      {
        term: 1,
        title: 'Term 1: Algebraic Foundations & Trigonometry',
        nodes: [
          {
            id: 'alg_exp',
            title: 'Algebraic Expressions',
            subskills: ['Products (FOIL)', 'Common Factors', 'Difference of Squares', 'Quadratic Trinomials'],
            status: 'mastered',
            masteryScore: 94,
            medal: 'gold',
            simulearnKey: 'math_quadratic_trinomial',
            challengeKey: 'mathematics_10_algebraic_expressions',
            prerequisites: []
          },
          {
            id: 'eq_ineq',
            title: 'Equations & Inequalities',
            subskills: ['Linear Equations', 'Quadratic Equations', 'Simultaneous Equations', 'Linear Inequalities'],
            status: 'unlocked',
            masteryScore: 76,
            medal: 'bronze',
            simulearnKey: 'math_quadratic_trinomial',
            challengeKey: 'mathematics_10_equations_inequalities',
            prerequisites: ['alg_exp']
          },
          {
            id: 'trig_1',
            title: 'Trigonometry Basics',
            subskills: ['Right-Angled Triangle Ratios', 'Definitions (sin, cos, tan)', 'Special Angles (30°, 45°, 60°)', '2D Applications'],
            status: 'unlocked',
            masteryScore: 58,
            medal: null,
            simulearnKey: 'math_quadratic_trinomial',
            challengeKey: 'mathematics_10_algebraic_expressions',
            prerequisites: ['eq_ineq']
          },
          {
            id: 'term_1_exam',
            title: 'Term 1 Mastery Trophy',
            subskills: ['Comprehensive Term 1 Assessment'],
            status: 'locked',
            masteryScore: 0,
            medal: null,
            isTrophy: true,
            challengeKey: 'mathematics_10_algebraic_expressions',
            prerequisites: ['trig_1']
          }
        ]
      },
      {
        term: 2,
        title: 'Term 2: Functions & Analytical Geometry',
        nodes: [
          {
            id: 'functions_intro',
            title: 'Functions: Linear & Parabola',
            subskills: ['Straight Line Equations', 'Parabola Turning Points', 'Domain and Range'],
            status: 'locked',
            masteryScore: 0,
            medal: null,
            prerequisites: ['term_1_exam']
          },
          {
            id: 'analytical_geom',
            title: 'Analytical Geometry',
            subskills: ['Distance Formula', 'Midpoint Formula', 'Gradient of Line'],
            status: 'locked',
            masteryScore: 0,
            medal: null,
            prerequisites: ['functions_intro']
          }
        ]
      }
    ]
  },
  Accounting: {
    10: [
      {
        term: 1,
        title: 'Term 1: Sole Trader Accounting Cycle',
        nodes: [
          {
            id: 'crj_entry',
            title: 'Cash Receipts Journal (15% VAT)',
            subskills: ['Cash Sales', 'Output VAT', 'Cost of Sales Split', 'Sundry Accounts'],
            status: 'mastered',
            masteryScore: 90,
            medal: 'silver',
            simulearnKey: 'accounting_crj_vat',
            challengeKey: 'accounting_10_sole_trader_crj',
            prerequisites: []
          },
          {
            id: 'cpj_entry',
            title: 'Cash Payments Journal',
            subskills: ['EFT Payments', 'Trading Stock Purchases', 'Input VAT', 'Creditors Settlements'],
            status: 'unlocked',
            masteryScore: 72,
            medal: 'bronze',
            simulearnKey: 'accounting_crj_vat',
            challengeKey: 'accounting_10_sole_trader_crj',
            prerequisites: ['crj_entry']
          },
          {
            id: 'gl_ledger',
            title: 'General Ledger Accounts',
            subskills: ['Posting Journals', 'Balancing Balance Sheet Accounts', 'Trial Balance Extraction'],
            status: 'unlocked',
            masteryScore: 60,
            medal: null,
            simulearnKey: 'accounting_crj_vat',
            challengeKey: 'accounting_10_sole_trader_crj',
            prerequisites: ['cpj_entry']
          },
          {
            id: 'term_1_acct_trophy',
            title: 'Term 1 Sole Trader Trophy',
            subskills: ['Full Sole Trader Exam'],
            status: 'locked',
            masteryScore: 0,
            medal: null,
            isTrophy: true,
            challengeKey: 'accounting_10_sole_trader_crj',
            prerequisites: ['gl_ledger']
          }
        ]
      }
    ]
  }
};

export default function ProgressMap({
  subject = 'Mathematics',
  grade = '10',
  onSelectTopicForPractice,
  onOpenTrophyRoom
}) {
  const termsData = SAMPLE_CURRICULUM_DATA[subject]?.[grade] || SAMPLE_CURRICULUM_DATA.Mathematics[10];

  const [selectedNode, setSelectedNode] = useState(null);
  const [activeChallengeKey, setActiveChallengeKey] = useState(null);
  const [activeSimuLearnKey, setActiveSimuLearnKey] = useState(null);

  const handleNodeClick = (node) => {
    setSelectedNode(node);
  };

  const handleStartPractice = (node) => {
    if (onSelectTopicForPractice) {
      onSelectTopicForPractice({
        id: node.id,
        name: node.title,
        title: node.title,
        subskills: node.subskills
      });
    }
  };

  return (
    <div className="w-full flex flex-col items-center p-4 sm:p-6 text-slate-100 max-w-4xl mx-auto">
      {/* Skill Tree Header */}
      <div className="w-full flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-5 rounded-3xl bg-slate-900/90 border border-slate-800 shadow-xl mb-8">
        <div>
          <div className="flex items-center gap-2">
            <span className="text-xs px-2.5 py-0.5 rounded-full uppercase font-bold tracking-wider bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
              National Curriculum Skill Tree
            </span>
            <span className="text-xs text-slate-400">Grade {grade} {subject}</span>
          </div>
          <h2 className="text-xl font-bold text-slate-100 mt-1">Interactive Learning Highway</h2>
          <p className="text-xs text-slate-400">Master prerequisites, unlock topic nodes, and earn authenticated Topic Medals.</p>
        </div>

        {onOpenTrophyRoom && (
          <button
            onClick={onOpenTrophyRoom}
            className="flex items-center gap-2 px-4 py-2.5 rounded-2xl bg-slate-800 hover:bg-slate-700 text-amber-300 font-semibold text-xs border border-amber-500/30 shadow-lg shadow-amber-950/30 transition-all shrink-0"
          >
            <Trophy className="w-4 h-4" />
            <span>Open Trophy Room</span>
          </button>
        )}
      </div>

      {/* Terms & Path Nodes */}
      <div className="w-full space-y-10 relative">
        {termsData.map((termGroup) => (
          <div key={termGroup.term} className="space-y-4">
            {/* Term Section Header */}
            <div className="flex items-center gap-3">
              <div className="h-px bg-slate-800 flex-1" />
              <div className="px-4 py-1.5 rounded-full bg-slate-900 border border-slate-800 text-xs font-semibold text-slate-300 flex items-center gap-2 shadow-inner">
                <span className="w-2 h-2 rounded-full bg-indigo-400" />
                <span>{termGroup.title}</span>
              </div>
              <div className="h-px bg-slate-800 flex-1" />
            </div>

            {/* Nodes Stack with Connecting Line */}
            <div className="flex flex-col items-center gap-6 relative py-4">
              {/* Connecting vertical stroke */}
              <div className="absolute top-8 bottom-8 w-1 bg-slate-800/80 -z-10 rounded-full" />

              {termGroup.nodes.map((node, index) => {
                const isMastered = node.status === 'mastered';
                const isUnlocked = node.status === 'unlocked' || isMastered;
                const isLocked = node.status === 'locked';
                const isSelected = selectedNode?.id === node.id;

                let medalBadge = null;
                if (node.medal === 'gold') medalBadge = '🥇';
                else if (node.medal === 'silver') medalBadge = '🥈';
                else if (node.medal === 'bronze') medalBadge = '🥉';

                return (
                  <div key={node.id} className="relative flex flex-col items-center">
                    {/* Node Circle */}
                    <button
                      onClick={() => handleNodeClick(node)}
                      className={`relative w-16 h-16 sm:w-20 sm:h-20 rounded-3xl flex items-center justify-center text-xl sm:text-2xl transition-all duration-300 shadow-xl ${
                        isMastered
                          ? 'bg-gradient-to-tr from-emerald-600 to-teal-500 text-white ring-4 ring-emerald-500/30 scale-105'
                          : isUnlocked
                          ? 'bg-slate-900 border-2 border-indigo-500/80 text-indigo-300 hover:scale-105 hover:border-indigo-400 ring-4 ring-indigo-500/20'
                          : 'bg-slate-900/60 border border-slate-800 text-slate-600 opacity-60 cursor-not-allowed'
                      } ${isSelected ? 'ring-4 ring-amber-400 scale-110' : ''}`}
                    >
                      {node.isTrophy ? (
                        <Trophy className={`w-7 h-7 sm:w-8 sm:h-8 ${isUnlocked ? 'text-amber-300 animate-pulse' : 'text-slate-600'}`} />
                      ) : isMastered ? (
                        <CheckCircle2 className="w-7 h-7 sm:w-8 sm:h-8 text-white" />
                      ) : isLocked ? (
                        <Lock className="w-6 h-6 text-slate-600" />
                      ) : (
                        <span className="font-bold font-mono text-sm sm:text-base text-indigo-200">
                          {node.masteryScore}%
                        </span>
                      )}

                      {/* Medal Overlay Tag */}
                      {medalBadge && (
                        <span className="absolute -top-2 -right-2 text-base sm:text-lg filter drop-shadow-md">
                          {medalBadge}
                        </span>
                      )}
                    </button>

                    {/* Node Title Label */}
                    <div className="mt-2 text-center max-w-[200px]">
                      <div className="text-xs sm:text-sm font-semibold text-slate-200 truncate">
                        {node.title}
                      </div>
                      {isUnlocked && (
                        <div className="text-[10px] text-slate-400 mt-0.5">
                          {isMastered ? 'Mastery Verified' : `${node.subskills.length} Subskills`}
                        </div>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        ))}
      </div>

      {/* Selected Node Action Modal / Popover */}
      {selectedNode && (
        <div className="fixed inset-0 z-40 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-sm animate-fade-in">
          <div className="bg-slate-900 border border-slate-700/80 rounded-3xl shadow-2xl max-w-md w-full p-6 space-y-4 text-slate-100 relative">
            <button
              onClick={() => setSelectedNode(null)}
              className="absolute top-4 right-4 p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>

            <div className="flex items-center gap-3">
              <div className="w-12 h-12 rounded-2xl bg-indigo-500/20 border border-indigo-500/30 flex items-center justify-center text-xl font-bold text-indigo-300">
                {selectedNode.medal ? (selectedNode.medal === 'gold' ? '🥇' : selectedNode.medal === 'silver' ? '🥈' : '🥉') : '🎯'}
              </div>
              <div>
                <span className="text-[11px] px-2 py-0.5 rounded-full uppercase font-bold bg-slate-800 text-slate-300 border border-slate-700">
                  {selectedNode.status === 'mastered' ? 'Mastered Node' : selectedNode.status === 'unlocked' ? 'Unlocked Node' : 'Locked Node'}
                </span>
                <h3 className="text-base font-bold text-slate-100 mt-1">{selectedNode.title}</h3>
              </div>
            </div>

            {/* Subskills Breakdown */}
            <div className="space-y-1.5">
              <span className="text-[11px] font-semibold text-slate-400 uppercase">Core Subskills:</span>
              <div className="flex flex-wrap gap-1.5">
                {selectedNode.subskills?.map((sub, i) => (
                  <span key={i} className="text-xs px-2.5 py-1 rounded-lg bg-slate-950 border border-slate-800 text-slate-300">
                    {sub}
                  </span>
                ))}
              </div>
            </div>

            {/* Mastery Score Progress */}
            {selectedNode.status !== 'locked' && (
              <div className="p-3.5 rounded-2xl bg-slate-950 border border-slate-800 flex items-center justify-between">
                <div>
                  <div className="text-xs text-slate-400">Current Formative Mastery</div>
                  <div className="text-lg font-bold text-indigo-300 font-mono mt-0.5">{selectedNode.masteryScore}%</div>
                </div>
                <div className="text-xs text-right text-slate-400">
                  <div>Required for Gold Medal</div>
                  <div className="font-semibold text-amber-300">95% in Challenge</div>
                </div>
              </div>
            )}

            {/* Actions */}
            <div className="pt-2 flex flex-col gap-2.5">
              {selectedNode.status !== 'locked' ? (
                <>
                  <button
                    onClick={() => {
                      const node = selectedNode;
                      setSelectedNode(null);
                      handleStartPractice(node);
                    }}
                    className="w-full py-3 px-4 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-xs transition-colors flex items-center justify-center gap-2 shadow-lg shadow-indigo-950/50"
                  >
                    <BookOpen className="w-4 h-4" />
                    <span>Start Practice Questions</span>
                  </button>

                  <div className="grid grid-cols-2 gap-2">
                    <button
                      onClick={() => {
                        const simKey = selectedNode.simulearnKey || 'math_quadratic_trinomial';
                        setSelectedNode(null);
                        setActiveSimuLearnKey(simKey);
                      }}
                      className="py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-medium text-xs transition-colors flex items-center justify-center gap-1.5"
                    >
                      <span>🎥</span> Watch Simulation
                    </button>
                    <button
                      onClick={() => {
                        const chalKey = selectedNode.challengeKey || 'mathematics_10_algebraic_expressions';
                        setSelectedNode(null);
                        setActiveChallengeKey(chalKey);
                      }}
                      className="py-2.5 px-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-xs transition-colors flex items-center justify-center gap-1.5 shadow-md shadow-amber-500/20"
                    >
                      <span>🏅</span> Take Challenge
                    </button>
                  </div>
                </>
              ) : (
                <div className="p-3 rounded-xl bg-slate-950/60 border border-slate-800 text-xs text-slate-400 text-center">
                  🔒 Complete earlier topics with at least 60% mastery to unlock this module.
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      {/* Challenge Examination Gate Modal */}
      <ChallengeGate
        isOpen={!!activeChallengeKey}
        challengeKey={activeChallengeKey}
        onClose={() => setActiveChallengeKey(null)}
        onChallengePassed={(result) => {
          console.log('[Challenge Gate] Learner earned medal:', result);
        }}
        onViewTrophyRoom={() => {
          setActiveChallengeKey(null);
          if (onOpenTrophyRoom) onOpenTrophyRoom();
        }}
      />

      {/* SimuLearn Step Player Modal */}
      <SimuLearnPlayer
        isOpen={!!activeSimuLearnKey}
        archetypeKey={activeSimuLearnKey}
        onClose={() => setActiveSimuLearnKey(null)}
        onComplete={() => setActiveSimuLearnKey(null)}
      />
    </div>
  );
}
