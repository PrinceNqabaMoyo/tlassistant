import React, { useState } from 'react';
import BadgeCard from './BadgeCard';
import { Crown, Trophy, Medal, Pin, Sparkles } from 'lucide-react';
import { TIER_METADATA } from './badgeIconRegistry';

const SAMPLE_BADGES = [
  { id: '1', tier: 'subskill_pin', title: 'Quadratic Trinomials', subject: 'Mathematics', xp: 50, earnedAt: '2026-09-18' },
  { id: '2', tier: 'subskill_pin', title: 'CRJ 15% VAT Split', subject: 'Accounting', xp: 50, earnedAt: '2026-09-17' },
  { id: '3', tier: 'subskill_pin', title: 'Kinematics Equations', subject: 'Physical Sciences', xp: 50, earnedAt: '2026-09-16' },
  { id: '4', tier: 'topic_medal', title: 'Algebraic Expressions', subject: 'Mathematics', grade: 'gold', xp: 350, earnedAt: '2026-09-15' },
  { id: '5', tier: 'topic_medal', title: 'Sole Trader Accounting', subject: 'Accounting', grade: 'silver', xp: 200, earnedAt: '2026-09-14' },
  { id: '6', tier: 'term_trophy', title: 'Term 1 Accounting Trophy', subject: 'Accounting', xp: 750, earnedAt: '2026-09-12' },
  { id: '7', tier: 'term_trophy', title: 'Term 1 Mathematics Trophy', subject: 'Mathematics', xp: 750, isLocked: true },
  { id: '8', tier: 'subject_medallion', title: 'Grade 10 Accounting Medallion', subject: 'Accounting', xp: 2000, isLocked: true }
];

export default function GamificationSummary({
  isOpen = false,
  onClose,
  badges = SAMPLE_BADGES,
  totalXP = 1450,
  level = 4,
  streakDays = 5
}) {
  const [activeTab, setActiveTab] = useState('all');

  if (!isOpen) return null;

  const filteredBadges = activeTab === 'all'
    ? badges
    : badges.filter(b => b.tier === activeTab);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-slate-950/80 backdrop-blur-md animate-fade-in">
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl max-w-2xl w-full flex flex-col max-h-[85vh] overflow-hidden text-slate-100">
        {/* Header */}
        <div className="p-5 border-b border-slate-800 bg-slate-950/60 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-purple-500/20 text-purple-300 flex items-center justify-center text-xl border border-purple-500/30">
              <Crown className="w-5 h-5 text-purple-300" />
            </div>
            <div>
              <h3 className="text-base font-bold text-slate-100">Academic Trophy Room & Credentials</h3>
              <p className="text-xs text-slate-400">4-Tier Verified Mastery • Ungameable Academic XP</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-slate-100 hover:bg-slate-800 transition-colors"
          >
            ✕
          </button>
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-3 gap-3 p-4 bg-slate-950/40 border-b border-slate-800 text-center">
          <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="text-[11px] text-slate-400 font-medium">Ungameable XP</div>
            <div className="text-base sm:text-lg font-bold text-indigo-300 font-mono mt-0.5">{totalXP.toLocaleString()}</div>
          </div>
          <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="text-[11px] text-slate-400 font-medium">Current Level</div>
            <div className="text-base sm:text-lg font-bold text-purple-300 font-mono mt-0.5">Level {level}</div>
          </div>
          <div className="p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
            <div className="text-[11px] text-slate-400 font-medium">Study Streak</div>
            <div className="text-base sm:text-lg font-bold text-amber-300 font-mono mt-0.5">🔥 {streakDays} Days</div>
          </div>
        </div>

        {/* Tier Tabs */}
        <div className="flex items-center gap-1.5 px-4 pt-3 pb-1 border-b border-slate-800 text-xs overflow-x-auto">
          {[
            { id: 'all', label: 'All Badges', icon: Sparkles },
            { id: 'subskill_pin', label: 'Subskill Pins', icon: Pin },
            { id: 'topic_medal', label: 'Topic Medals', icon: Medal },
            { id: 'term_trophy', label: 'Term Trophies', icon: Trophy },
            { id: 'subject_medallion', label: 'Medallions', icon: Crown }
          ].map(tab => {
            const TabIcon = tab.icon;
            return (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg whitespace-nowrap font-medium transition-colors ${
                  activeTab === tab.id
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <TabIcon className="w-3.5 h-3.5" />
                <span>{tab.label}</span>
              </button>
            );
          })}
        </div>

        {/* Badges Grid */}
        <div className="p-4 overflow-y-auto flex-1 grid grid-cols-1 sm:grid-cols-2 gap-3">
          {filteredBadges.map(badge => (
            <BadgeCard
              key={badge.id}
              tier={badge.tier}
              title={badge.title}
              subject={badge.subject}
              xp={badge.xp}
              isLocked={badge.isLocked}
              grade={badge.grade}
              earnedAt={badge.earnedAt}
            />
          ))}
        </div>

        {/* Footer */}
        <div className="p-3 bg-slate-950/70 border-t border-slate-800 text-center text-xs text-slate-500">
          Badges reflect authenticated national curriculum standard performance and cannot be padded.
        </div>
      </div>
    </div>
  );
}
