/**
 * Central Subject Palette Token System
 * Enhanced with High-Saturation Jewel Tones & Radiant Glow Tokens
 * 
 * Every base subject color passes WCAG AA (>= 4.5:1) with white text.
 * Every text color passes WCAG AA (>= 4.5:1) against its soft background tint.
 * Luminous gradient stops and ambient neon glow tokens provide genuine visual radiance.
 */

export const BRAND = {
  blue: '#13519C',
  blueDark: '#0F4280',
  orange: '#FF9100',
  onOrange: '#0B2545', // Deep navy for AA contrast on orange backgrounds
  white: '#FFFFFF',
};

export const SUBJECT_PALETTE = {
  desk: {
    id: 'desk',
    name: "Today's Desk",
    shortName: 'Desk',
    base: '#13519C',
    light: '#2563EB',
    deep: '#0F4280',
    gradient: 'linear-gradient(135deg, #2563EB 0%, #13519C 60%, #0F4280 100%)',
    soft: '#EAF1FA',
    border: '#BFD3EC',
    glowBorder: 'rgba(37, 99, 235, 0.45)',
    text: '#13519C',
    glowColor: 'rgba(19, 81, 156, 0.55)',
    shadowColor: 'rgba(19, 81, 156, 0.35)',
    glow: '0 0 22px 2px rgba(19, 81, 156, 0.5), 0 4px 14px rgba(19, 81, 156, 0.3)',
    glowLg: '0 0 38px 4px rgba(19, 81, 156, 0.6), 0 14px 30px -4px rgba(19, 81, 156, 0.4)',
    glowSm: '0 0 14px 2px rgba(19, 81, 156, 0.45)',
  },
  mathematics: {
    id: 'mathematics',
    name: 'Mathematics',
    shortName: 'Maths',
    base: '#2563EB', // Royal Cobalt Blue (WCAG AA 5.17:1 on white)
    light: '#3B82F6',
    deep: '#1D4ED8',
    gradient: 'linear-gradient(135deg, #3B82F6 0%, #2563EB 60%, #1D4ED8 100%)',
    soft: '#EFF6FF',
    border: '#BFDBFE',
    glowBorder: 'rgba(59, 130, 246, 0.5)',
    text: '#1E40AF',
    glowColor: 'rgba(59, 130, 246, 0.55)',
    shadowColor: 'rgba(37, 99, 235, 0.35)',
    glow: '0 0 24px 2px rgba(59, 130, 246, 0.55), 0 6px 16px -2px rgba(37, 99, 235, 0.35)',
    glowLg: '0 0 40px 5px rgba(59, 130, 246, 0.65), 0 16px 36px -6px rgba(37, 99, 235, 0.4)',
    glowSm: '0 0 14px 2px rgba(59, 130, 246, 0.45)',
  },
  mathematical_literacy: {
    id: 'mathematical_literacy',
    name: 'Mathematical Literacy',
    shortName: 'Maths Lit',
    base: '#C026D3', // Vivid Fuchsia / Orchid (WCAG AA 4.71:1 on white)
    light: '#E879F9',
    deep: '#A21CAF',
    gradient: 'linear-gradient(135deg, #E879F9 0%, #C026D3 60%, #A21CAF 100%)',
    soft: '#FDF4FF',
    border: '#F5D0FE',
    glowBorder: 'rgba(217, 70, 239, 0.5)',
    text: '#86198F',
    glowColor: 'rgba(217, 70, 239, 0.55)',
    shadowColor: 'rgba(192, 38, 211, 0.35)',
    glow: '0 0 24px 2px rgba(217, 70, 239, 0.55), 0 6px 16px -2px rgba(192, 38, 211, 0.35)',
    glowLg: '0 0 40px 5px rgba(217, 70, 239, 0.65), 0 16px 36px -6px rgba(192, 38, 211, 0.4)',
    glowSm: '0 0 14px 2px rgba(217, 70, 239, 0.45)',
  },
  technical_mathematics: {
    id: 'technical_mathematics',
    name: 'Technical Mathematics',
    shortName: 'Tech Maths',
    base: '#4F46E5', // Electric Indigo (WCAG AA 6.29:1 on white)
    light: '#6366F1',
    deep: '#4338CA',
    gradient: 'linear-gradient(135deg, #6366F1 0%, #4F46E5 60%, #4338CA 100%)',
    soft: '#EEF2FF',
    border: '#C7D2FE',
    glowBorder: 'rgba(99, 102, 241, 0.5)',
    text: '#3730A3',
    glowColor: 'rgba(99, 102, 241, 0.55)',
    shadowColor: 'rgba(79, 70, 229, 0.35)',
    glow: '0 0 24px 2px rgba(99, 102, 241, 0.55), 0 6px 16px -2px rgba(79, 70, 229, 0.35)',
    glowLg: '0 0 40px 5px rgba(99, 102, 241, 0.65), 0 16px 36px -6px rgba(79, 70, 229, 0.4)',
    glowSm: '0 0 14px 2px rgba(99, 102, 241, 0.45)',
  },
  accounting: {
    id: 'accounting',
    name: 'Accounting',
    shortName: 'Accounting',
    base: '#047857', // Rich Emerald Green (WCAG AA 5.48:1 on white)
    light: '#10B981', // Electric Emerald highlight
    deep: '#065F46',
    gradient: 'linear-gradient(135deg, #10B981 0%, #059669 50%, #047857 100%)',
    soft: '#ECFDF5',
    border: '#A7F3D0',
    glowBorder: 'rgba(16, 185, 129, 0.5)',
    text: '#065F46',
    glowColor: 'rgba(16, 185, 129, 0.55)',
    shadowColor: 'rgba(4, 120, 87, 0.35)',
    glow: '0 0 24px 2px rgba(16, 185, 129, 0.55), 0 6px 16px -2px rgba(4, 120, 87, 0.35)',
    glowLg: '0 0 40px 5px rgba(16, 185, 129, 0.65), 0 16px 36px -6px rgba(4, 120, 87, 0.4)',
    glowSm: '0 0 14px 2px rgba(16, 185, 129, 0.45)',
  },
  business_studies: {
    id: 'business_studies',
    name: 'Business Studies',
    shortName: 'Business',
    base: '#E11D48', // Vivid Ruby / Crimson (WCAG AA 4.70:1 on white)
    light: '#F43F5E',
    deep: '#BE123C',
    gradient: 'linear-gradient(135deg, #F43F5E 0%, #E11D48 60%, #BE123C 100%)',
    soft: '#FFF1F2',
    border: '#FECDD3',
    glowBorder: 'rgba(244, 63, 94, 0.5)',
    text: '#9F1239',
    glowColor: 'rgba(244, 63, 94, 0.55)',
    shadowColor: 'rgba(225, 29, 72, 0.35)',
    glow: '0 0 24px 2px rgba(244, 63, 94, 0.55), 0 6px 16px -2px rgba(225, 29, 72, 0.35)',
    glowLg: '0 0 40px 5px rgba(244, 63, 94, 0.65), 0 16px 36px -6px rgba(225, 29, 72, 0.4)',
    glowSm: '0 0 14px 2px rgba(244, 63, 94, 0.45)',
  },
  physical_sciences: {
    id: 'physical_sciences',
    name: 'Physical Sciences',
    shortName: 'Physics',
    base: '#0E7490', // Deep Laser Cyan / Teal (WCAG AA 5.36:1 on white)
    light: '#06B6D4', // Luminous Cyan highlight
    deep: '#155E75',
    gradient: 'linear-gradient(135deg, #06B6D4 0%, #0891B2 50%, #0E7490 100%)',
    soft: '#ECFEFF',
    border: '#A5F3FC',
    glowBorder: 'rgba(6, 182, 212, 0.5)',
    text: '#155E75',
    glowColor: 'rgba(6, 182, 212, 0.55)',
    shadowColor: 'rgba(14, 116, 144, 0.35)',
    glow: '0 0 24px 2px rgba(6, 182, 212, 0.55), 0 6px 16px -2px rgba(14, 116, 144, 0.35)',
    glowLg: '0 0 40px 5px rgba(6, 182, 212, 0.65), 0 16px 36px -6px rgba(14, 116, 144, 0.4)',
    glowSm: '0 0 14px 2px rgba(6, 182, 212, 0.45)',
  },
  life_sciences: {
    id: 'life_sciences',
    name: 'Life Sciences',
    shortName: 'Life Sci',
    base: '#4D7C0F', // Rich Leaf Green (WCAG AA 4.99:1 on white)
    light: '#84CC16', // Fresh Vibrant Lime highlight
    deep: '#365314',
    gradient: 'linear-gradient(135deg, #84CC16 0%, #65A30D 50%, #4D7C0F 100%)',
    soft: '#F7FEE7',
    border: '#D9F99D',
    glowBorder: 'rgba(132, 204, 22, 0.5)',
    text: '#3F6212',
    glowColor: 'rgba(132, 204, 22, 0.55)',
    shadowColor: 'rgba(77, 124, 15, 0.35)',
    glow: '0 0 24px 2px rgba(132, 204, 22, 0.55), 0 6px 16px -2px rgba(77, 124, 15, 0.35)',
    glowLg: '0 0 40px 5px rgba(132, 204, 22, 0.65), 0 16px 36px -6px rgba(77, 124, 15, 0.4)',
    glowSm: '0 0 14px 2px rgba(132, 204, 22, 0.45)',
  },
  ems: {
    id: 'ems',
    name: 'EMS',
    shortName: 'EMS',
    base: '#C2410C', // Terracotta (WCAG AA 5.18:1 on white)
    light: '#FB923C', // Warm Amber highlight
    deep: '#9A3412',
    gradient: 'linear-gradient(135deg, #FB923C 0%, #EA580C 50%, #C2410C 100%)',
    soft: '#FFF7ED',
    border: '#FED7AA',
    glowBorder: 'rgba(251, 146, 60, 0.5)',
    text: '#9A3412',
    glowColor: 'rgba(251, 146, 60, 0.55)',
    shadowColor: 'rgba(194, 65, 12, 0.35)',
    glow: '0 0 24px 2px rgba(251, 146, 60, 0.55), 0 6px 16px -2px rgba(194, 65, 12, 0.35)',
    glowLg: '0 0 40px 5px rgba(251, 146, 60, 0.65), 0 16px 36px -6px rgba(194, 65, 12, 0.4)',
    glowSm: '0 0 14px 2px rgba(251, 146, 60, 0.45)',
  },
  natural_sciences: {
    id: 'natural_sciences',
    name: 'Natural Sciences',
    shortName: 'Nat Sci',
    base: '#0369A1', // Deep Sky Blue (WCAG AA 5.93:1 on white)
    light: '#38BDF8', // Luminous Sky highlight
    deep: '#075985',
    gradient: 'linear-gradient(135deg, #38BDF8 0%, #0284C7 50%, #0369A1 100%)',
    soft: '#F0F9FF',
    border: '#BAE6FD',
    glowBorder: 'rgba(56, 189, 248, 0.5)',
    text: '#075985',
    glowColor: 'rgba(56, 189, 248, 0.55)',
    shadowColor: 'rgba(3, 105, 161, 0.35)',
    glow: '0 0 24px 2px rgba(56, 189, 248, 0.55), 0 6px 16px -2px rgba(3, 105, 161, 0.35)',
    glowLg: '0 0 40px 5px rgba(56, 189, 248, 0.65), 0 16px 36px -6px rgba(3, 105, 161, 0.4)',
    glowSm: '0 0 14px 2px rgba(56, 189, 248, 0.45)',
  },
};

const ALIASES = {
  maths: 'mathematics',
  math: 'mathematics',
  mathslit: 'mathematical_literacy',
  maths_lit: 'mathematical_literacy',
  techmaths: 'technical_mathematics',
  tech_maths: 'technical_mathematics',
  physics: 'physical_sciences',
  phys: 'physical_sciences',
  lifesci: 'life_sciences',
  life_sci: 'life_sciences',
  business: 'business_studies',
  natsci: 'natural_sciences',
  nat_sci: 'natural_sciences',
};

export const getSubjectTheme = (id) => {
  if (!id) return SUBJECT_PALETTE.desk;
  const normalized = String(id).toLowerCase().trim().replace(/[\s-]+/g, '_');
  const targetId = ALIASES[normalized] || normalized;
  return SUBJECT_PALETTE[targetId] || SUBJECT_PALETTE.desk;
};
