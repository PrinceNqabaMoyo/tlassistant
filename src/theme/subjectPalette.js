/**
 * Central Subject Palette Token System
 * Inspired by Shopify brand-pairing color theory and harmonized with:
 * - Fundile Brand Blue: #13519C (Reserved for Today's Desk, nav, and brand chrome)
 * - Fundile Brand Orange: #FF9100 (Reserved for CTAs, hints, and XP)
 * - Fundile White / Slate-50 canvas
 * 
 * Every base subject color passes WCAG AA (>= 4.5:1) with white text.
 * Every text color passes WCAG AA (>= 4.5:1) against its soft background tint.
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
    soft: '#EAF1FA',
    border: '#BFD3EC',
    text: '#13519C',
  },
  mathematics: {
    id: 'mathematics',
    name: 'Mathematics',
    shortName: 'Maths',
    base: '#6D28D9', // Royal Violet (orange's complement on color wheel)
    soft: '#F1EBFD',
    border: '#D6C6F7',
    text: '#5B21B6',
  },
  mathematical_literacy: {
    id: 'mathematical_literacy',
    name: 'Mathematical Literacy',
    shortName: 'Maths Lit',
    base: '#A21CAF', // Orchid Magenta
    soft: '#F9E9FB',
    border: '#EBC4F0',
    text: '#86198F',
  },
  technical_mathematics: {
    id: 'technical_mathematics',
    name: 'Technical Mathematics',
    shortName: 'Tech Maths',
    base: '#475569', // Slate / Graphite
    soft: '#EEF1F5',
    border: '#CBD5E1',
    text: '#334155',
  },
  accounting: {
    id: 'accounting',
    name: 'Accounting',
    shortName: 'Accounting',
    base: '#15803D', // Forest Green
    soft: '#E9F7EE',
    border: '#B7E2C6',
    text: '#166534',
  },
  business_studies: {
    id: 'business_studies',
    name: 'Business Studies',
    shortName: 'Business',
    base: '#BE123C', // Raspberry (Shopify logo preview)
    soft: '#FCE9EE',
    border: '#F5BFCD',
    text: '#9F1239',
  },
  physical_sciences: {
    id: 'physical_sciences',
    name: 'Physical Sciences',
    shortName: 'Physics',
    base: '#0F766E', // Deep Teal
    soft: '#E6F5F3',
    border: '#B3E0DA',
    text: '#115E59',
  },
  life_sciences: {
    id: 'life_sciences',
    name: 'Life Sciences',
    shortName: 'Life Sci',
    base: '#4D7C0F', // Olive Moss
    soft: '#F0F6E7',
    border: '#CFE3B4',
    text: '#3F6212',
  },
  ems: {
    id: 'ems',
    name: 'EMS',
    shortName: 'EMS',
    base: '#C2410C', // Terracotta
    soft: '#FDEEE6',
    border: '#F7C9B3',
    text: '#9A3412',
  },
  natural_sciences: {
    id: 'natural_sciences',
    name: 'Natural Sciences',
    shortName: 'Nat Sci',
    base: '#0E7490', // Lagoon
    soft: '#E6F3F7',
    border: '#B3DCE7',
    text: '#155E75',
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
