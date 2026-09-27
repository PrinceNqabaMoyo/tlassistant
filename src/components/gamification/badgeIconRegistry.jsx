import React from 'react';
import {
  BookOpen,
  Landmark,
  Receipt,
  Sigma,
  Compass,
  Briefcase,
  TrendingUp,
  Coins,
  Scale,
  Atom,
  Zap,
  Dna,
  Leaf,
  FileSpreadsheet,
  Calculator,
  Cog,
  Ruler,
  Trophy,
  Award,
  Medal,
  Crown,
  Sparkles,
  Pin,
  Shield,
  Star
} from 'lucide-react';

/**
 * Standardized 9-Subject Icon Registry for CAPS Curriculum
 */
export const SUBJECT_ICON_REGISTRY = {
  'Accounting': {
    name: 'Accounting',
    icon: Landmark,
    accent: 'from-emerald-500 to-teal-700',
    textAccent: 'text-emerald-400',
    bgLight: 'bg-emerald-950/40 border-emerald-700/50',
  },
  'Mathematics': {
    name: 'Mathematics',
    icon: Sigma,
    accent: 'from-indigo-500 to-blue-700',
    textAccent: 'text-indigo-400',
    bgLight: 'bg-indigo-950/40 border-indigo-700/50',
  },
  'Business Studies': {
    name: 'Business Studies',
    icon: Briefcase,
    accent: 'from-amber-500 to-orange-700',
    textAccent: 'text-amber-400',
    bgLight: 'bg-amber-950/40 border-amber-700/50',
  },
  'EMS': {
    name: 'EMS',
    icon: Coins,
    accent: 'from-teal-500 to-emerald-700',
    textAccent: 'text-teal-400',
    bgLight: 'bg-teal-950/40 border-teal-700/50',
  },
  'Physical Sciences': {
    name: 'Physical Sciences',
    icon: Atom,
    accent: 'from-violet-500 to-purple-700',
    textAccent: 'text-violet-400',
    bgLight: 'bg-violet-950/40 border-violet-700/50',
  },
  'Life Sciences': {
    name: 'Life Sciences',
    icon: Dna,
    accent: 'from-green-500 to-emerald-800',
    textAccent: 'text-green-400',
    bgLight: 'bg-green-950/40 border-green-700/50',
  },
  'Mathematical Literacy': {
    name: 'Mathematical Literacy',
    icon: Calculator,
    accent: 'from-cyan-500 to-blue-700',
    textAccent: 'text-cyan-400',
    bgLight: 'bg-cyan-950/40 border-cyan-700/50',
  },
  'Technical Mathematics': {
    name: 'Technical Mathematics',
    icon: Cog,
    accent: 'from-rose-500 to-red-700',
    textAccent: 'text-rose-400',
    bgLight: 'bg-rose-950/40 border-rose-700/50',
  },
  'Olympiad': {
    name: 'Olympiad',
    icon: Trophy,
    accent: 'from-amber-400 to-yellow-600',
    textAccent: 'text-amber-300',
    bgLight: 'bg-amber-950/50 border-amber-600/60',
  }
};

/**
 * 4-Tier Badge Archetypes:
 * 1. subskill_pin: Sleek lapel pin with mini subject glyph
 * 2. topic_medal: Laurel circular medal with grade distinction (Bronze/Silver/Gold)
 * 3. term_trophy: Multi-column pedestal trophy
 * 4. subject_medallion: Imperial ornate medallion with heraldic shield
 */
export const TIER_METADATA = {
  subskill_pin: {
    name: 'Subskill Pin',
    badgeType: 'pin',
    frameIcon: Pin,
    border: 'border-emerald-500/40 bg-gradient-to-br from-emerald-950/30 to-slate-900/60 text-emerald-300',
    glow: 'shadow-emerald-950/30',
    ring: 'ring-emerald-500/30',
    badgeLabel: '📍 PIN'
  },
  topic_medal: {
    name: 'Topic Medal',
    badgeType: 'medal',
    frameIcon: Medal,
    border: 'border-amber-500/50 bg-gradient-to-br from-amber-950/30 to-slate-900/70 text-amber-300',
    glow: 'shadow-amber-950/30',
    ring: 'ring-amber-500/40',
    badgeLabel: '🏅 MEDAL'
  },
  term_trophy: {
    name: 'Term Trophy',
    badgeType: 'trophy',
    frameIcon: Trophy,
    border: 'border-indigo-500/50 bg-gradient-to-br from-indigo-950/30 to-slate-900/70 text-indigo-300',
    glow: 'shadow-indigo-950/40',
    ring: 'ring-indigo-500/40',
    badgeLabel: '🏆 TROPHY'
  },
  subject_medallion: {
    name: 'Subject Medallion',
    badgeType: 'medallion',
    frameIcon: Crown,
    border: 'border-purple-500/60 bg-gradient-to-br from-purple-950/40 to-slate-900/80 text-purple-200',
    glow: 'shadow-purple-950/50',
    ring: 'ring-purple-500/50',
    badgeLabel: '👑 MEDALLION'
  }
};

/**
 * Returns subject visual metadata and Lucide icon.
 */
export function getSubjectMeta(subject) {
  if (!subject) return SUBJECT_ICON_REGISTRY['Mathematics'];
  // Normalise subject lookup
  const key = Object.keys(SUBJECT_ICON_REGISTRY).find(
    k => k.toLowerCase() === subject.trim().toLowerCase()
  );
  return key ? SUBJECT_ICON_REGISTRY[key] : SUBJECT_ICON_REGISTRY['Mathematics'];
}

/**
 * Renders the authentic visual icon for a badge based on subject and tier.
 */
export function BadgeVisualEmblem({ subject, tier = 'subskill_pin', grade = null, size = 'md' }) {
  const subjectMeta = getSubjectMeta(subject);
  const SubjectIcon = subjectMeta.icon;
  const tierMeta = TIER_METADATA[tier] || TIER_METADATA.subskill_pin;
  const FrameIcon = tierMeta.frameIcon;

  const isGold = grade?.toLowerCase() === 'gold';
  const isSilver = grade?.toLowerCase() === 'silver';
  const isBronze = grade?.toLowerCase() === 'bronze';

  const gradeRing = isGold
    ? 'ring-2 ring-amber-400 bg-amber-500/20'
    : isSilver
    ? 'ring-2 ring-slate-300 bg-slate-400/20'
    : isBronze
    ? 'ring-2 ring-amber-700 bg-amber-800/20'
    : '';

  const dim = size === 'sm' ? 'w-8 h-8' : size === 'lg' ? 'w-14 h-14' : 'w-10 h-10';
  const iconDim = size === 'sm' ? 'w-4 h-4' : size === 'lg' ? 'w-7 h-7' : 'w-5 h-5';
  const miniDim = size === 'sm' ? 'w-2.5 h-2.5' : size === 'lg' ? 'w-4 h-4' : 'w-3.5 h-3.5';

  return (
    <div className={`relative ${dim} rounded-xl bg-slate-900/90 border border-slate-700/80 flex items-center justify-center shadow-inner shrink-0 ${gradeRing} group-hover:scale-105 transition-transform duration-300`}>
      {/* Background Subject Gradient Splash */}
      <div className={`absolute inset-0 rounded-xl bg-gradient-to-br ${subjectMeta.accent} opacity-15`} />

      {/* Primary Subject Icon */}
      <SubjectIcon className={`${iconDim} ${subjectMeta.textAccent} relative z-10`} />

      {/* Tier Corner Badge Indicator */}
      <div className="absolute -bottom-1 -right-1 w-4 h-4 rounded-full bg-slate-950 border border-slate-700 flex items-center justify-center text-[9px] shadow-sm z-20">
        <FrameIcon className={`${miniDim} text-slate-300`} />
      </div>
    </div>
  );
}
