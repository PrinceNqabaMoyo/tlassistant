import React, { useState, useMemo } from 'react';
import { Search, Info, Sparkles, SlidersHorizontal, Layers, Atom } from 'lucide-react';

// Curriculum element dataset with accurate atomic numbers, masses, electron configurations, and Pauling electronegativities
const ELEMENTS = [
  // Period 1
  { number: 1, symbol: 'H', name: 'Hydrogen', mass: 1.008, period: 1, group: 1, category: 'nonmetal', electronegativity: 2.20, valence: 1, shells: [1], config: '1s¹' },
  { number: 2, symbol: 'He', name: 'Helium', mass: 4.003, period: 1, group: 18, category: 'noble_gas', electronegativity: null, valence: 0, shells: [2], config: '1s²' },

  // Period 2
  { number: 3, symbol: 'Li', name: 'Lithium', mass: 6.941, period: 2, group: 1, category: 'alkali_metal', electronegativity: 0.98, valence: 1, shells: [2, 1], config: '[He] 2s¹' },
  { number: 4, symbol: 'Be', name: 'Beryllium', mass: 9.012, period: 2, group: 2, category: 'alkaline_earth', electronegativity: 1.57, valence: 2, shells: [2, 2], config: '[He] 2s²' },
  { number: 5, symbol: 'B', name: 'Boron', mass: 10.81, period: 2, group: 13, category: 'metalloid', electronegativity: 2.04, valence: 3, shells: [2, 3], config: '[He] 2s² 2p¹' },
  { number: 6, symbol: 'C', name: 'Carbon', mass: 12.011, period: 2, group: 14, category: 'nonmetal', electronegativity: 2.55, valence: 4, shells: [2, 4], config: '[He] 2s² 2p²' },
  { number: 7, symbol: 'N', name: 'Nitrogen', mass: 14.007, period: 2, group: 15, category: 'nonmetal', electronegativity: 3.04, valence: 5, shells: [2, 5], config: '[He] 2s² 2p³' },
  { number: 8, symbol: 'O', name: 'Oxygen', mass: 15.999, period: 2, group: 16, category: 'nonmetal', electronegativity: 3.44, valence: 6, shells: [2, 6], config: '[He] 2s² 2p⁴' },
  { number: 9, symbol: 'F', name: 'Fluorine', mass: 18.998, period: 2, group: 17, category: 'halogen', electronegativity: 3.98, valence: 7, shells: [2, 7], config: '[He] 2s² 2p⁵' },
  { number: 10, symbol: 'Ne', name: 'Neon', mass: 20.180, period: 2, group: 18, category: 'noble_gas', electronegativity: null, valence: 8, shells: [2, 8], config: '[He] 2s² 2p⁶' },

  // Period 3
  { number: 11, symbol: 'Na', name: 'Sodium', mass: 22.990, period: 3, group: 1, category: 'alkali_metal', electronegativity: 0.93, valence: 1, shells: [2, 8, 1], config: '[Ne] 3s¹' },
  { number: 12, symbol: 'Mg', name: 'Magnesium', mass: 24.305, period: 3, group: 2, category: 'alkaline_earth', electronegativity: 1.31, valence: 2, shells: [2, 8, 2], config: '[Ne] 3s²' },
  { number: 13, symbol: 'Al', name: 'Aluminium', mass: 26.982, period: 3, group: 13, category: 'post_transition', electronegativity: 1.61, valence: 3, shells: [2, 8, 3], config: '[Ne] 3s² 3p¹' },
  { number: 14, symbol: 'Si', name: 'Silicon', mass: 28.085, period: 3, group: 14, category: 'metalloid', electronegativity: 1.90, valence: 4, shells: [2, 8, 4], config: '[Ne] 3s² 3p²' },
  { number: 15, symbol: 'P', name: 'Phosphorus', mass: 30.974, period: 3, group: 15, category: 'nonmetal', electronegativity: 2.19, valence: 5, shells: [2, 8, 5], config: '[Ne] 3s² 3p³' },
  { number: 16, symbol: 'S', name: 'Sulfur', mass: 32.065, period: 3, group: 16, category: 'nonmetal', electronegativity: 2.58, valence: 6, shells: [2, 8, 6], config: '[Ne] 3s² 3p⁴' },
  { number: 17, symbol: 'Cl', name: 'Chlorine', mass: 35.453, period: 3, group: 17, category: 'halogen', electronegativity: 3.16, valence: 7, shells: [2, 8, 7], config: '[Ne] 3s² 3p⁵' },
  { number: 18, symbol: 'Ar', name: 'Argon', mass: 39.948, period: 3, group: 18, category: 'noble_gas', electronegativity: null, valence: 8, shells: [2, 8, 8], config: '[Ne] 3s² 3p⁶' },

  // Period 4
  { number: 19, symbol: 'K', name: 'Potassium', mass: 39.098, period: 4, group: 1, category: 'alkali_metal', electronegativity: 0.82, valence: 1, shells: [2, 8, 8, 1], config: '[Ar] 4s¹' },
  { number: 20, symbol: 'Ca', name: 'Calcium', mass: 40.078, period: 4, group: 2, category: 'alkaline_earth', electronegativity: 1.00, valence: 2, shells: [2, 8, 8, 2], config: '[Ar] 4s²' },
  { number: 21, symbol: 'Sc', name: 'Scandium', mass: 44.956, period: 4, group: 3, category: 'transition_metal', electronegativity: 1.36, valence: 3, shells: [2, 8, 9, 2], config: '[Ar] 3d¹ 4s²' },
  { number: 22, symbol: 'Ti', name: 'Titanium', mass: 47.867, period: 4, group: 4, category: 'transition_metal', electronegativity: 1.54, valence: 4, shells: [2, 8, 10, 2], config: '[Ar] 3d² 4s²' },
  { number: 23, symbol: 'V', name: 'Vanadium', mass: 50.942, period: 4, group: 5, category: 'transition_metal', electronegativity: 1.63, valence: 5, shells: [2, 8, 11, 2], config: '[Ar] 3d³ 4s²' },
  { number: 24, symbol: 'Cr', name: 'Chromium', mass: 51.996, period: 4, group: 6, category: 'transition_metal', electronegativity: 1.66, valence: 6, shells: [2, 8, 13, 1], config: '[Ar] 3d⁵ 4s¹' },
  { number: 25, symbol: 'Mn', name: 'Manganese', mass: 54.938, period: 4, group: 7, category: 'transition_metal', electronegativity: 1.55, valence: 7, shells: [2, 8, 13, 2], config: '[Ar] 3d⁵ 4s²' },
  { number: 26, symbol: 'Fe', name: 'Iron', mass: 55.845, period: 4, group: 8, category: 'transition_metal', electronegativity: 1.83, valence: 2, shells: [2, 8, 14, 2], config: '[Ar] 3d⁶ 4s²' },
  { number: 27, symbol: 'Co', name: 'Cobalt', mass: 58.933, period: 4, group: 9, category: 'transition_metal', electronegativity: 1.88, valence: 2, shells: [2, 8, 15, 2], config: '[Ar] 3d⁷ 4s²' },
  { number: 28, symbol: 'Ni', name: 'Nickel', mass: 58.693, period: 4, group: 10, category: 'transition_metal', electronegativity: 1.91, valence: 2, shells: [2, 8, 16, 2], config: '[Ar] 3d⁸ 4s²' },
  { number: 29, symbol: 'Cu', name: 'Copper', mass: 63.546, period: 4, group: 11, category: 'transition_metal', electronegativity: 1.90, valence: 1, shells: [2, 8, 18, 1], config: '[Ar] 3d¹⁰ 4s¹' },
  { number: 30, symbol: 'Zn', name: 'Zinc', mass: 65.38, period: 4, group: 12, category: 'transition_metal', electronegativity: 1.65, valence: 2, shells: [2, 8, 18, 2], config: '[Ar] 3d¹⁰ 4s²' },
  { number: 31, symbol: 'Ga', name: 'Gallium', mass: 69.723, period: 4, group: 13, category: 'post_transition', electronegativity: 1.81, valence: 3, shells: [2, 8, 18, 3], config: '[Ar] 3d¹⁰ 4s² 4p¹' },
  { number: 32, symbol: 'Ge', name: 'Germanium', mass: 72.630, period: 4, group: 14, category: 'metalloid', electronegativity: 2.01, valence: 4, shells: [2, 8, 18, 4], config: '[Ar] 3d¹⁰ 4s² 4p²' },
  { number: 33, symbol: 'As', name: 'Arsenic', mass: 74.922, period: 4, group: 15, category: 'metalloid', electronegativity: 2.18, valence: 5, shells: [2, 8, 18, 5], config: '[Ar] 3d¹⁰ 4s² 4p³' },
  { number: 34, symbol: 'Se', name: 'Selenium', mass: 78.96, period: 4, group: 16, category: 'nonmetal', electronegativity: 2.55, valence: 6, shells: [2, 8, 18, 6], config: '[Ar] 3d¹⁰ 4s² 4p⁴' },
  { number: 35, symbol: 'Br', name: 'Bromine', mass: 79.904, period: 4, group: 17, category: 'halogen', electronegativity: 2.96, valence: 7, shells: [2, 8, 18, 7], config: '[Ar] 3d¹⁰ 4s² 4p⁵' },
  { number: 36, symbol: 'Kr', name: 'Krypton', mass: 83.798, period: 4, group: 18, category: 'noble_gas', electronegativity: 3.00, valence: 8, shells: [2, 8, 18, 8], config: '[Ar] 3d¹⁰ 4s² 4p⁶' },

  // Period 5 Key Elements
  { number: 37, symbol: 'Rb', name: 'Rubidium', mass: 85.468, period: 5, group: 1, category: 'alkali_metal', electronegativity: 0.82, valence: 1, shells: [2, 8, 18, 8, 1], config: '[Kr] 5s¹' },
  { number: 38, symbol: 'Sr', name: 'Strontium', mass: 87.62, period: 5, group: 2, category: 'alkaline_earth', electronegativity: 0.95, valence: 2, shells: [2, 8, 18, 8, 2], config: '[Kr] 5s²' },
  { number: 47, symbol: 'Ag', name: 'Silver', mass: 107.87, period: 5, group: 11, category: 'transition_metal', electronegativity: 1.93, valence: 1, shells: [2, 8, 18, 18, 1], config: '[Kr] 4d¹⁰ 5s¹' },
  { number: 50, symbol: 'Sn', name: 'Tin', mass: 118.71, period: 5, group: 14, category: 'post_transition', electronegativity: 1.96, valence: 4, shells: [2, 8, 18, 18, 4], config: '[Kr] 4d¹⁰ 5s² 5p²' },
  { number: 53, symbol: 'I', name: 'Iodine', mass: 126.90, period: 5, group: 17, category: 'halogen', electronegativity: 2.66, valence: 7, shells: [2, 8, 18, 18, 7], config: '[Kr] 4d¹⁰ 5s² 5p⁵' },
  { number: 54, symbol: 'Xe', name: 'Xenon', mass: 131.29, period: 5, group: 18, category: 'noble_gas', electronegativity: 2.60, valence: 8, shells: [2, 8, 18, 18, 8], config: '[Kr] 4d¹⁰ 5s² 5p⁶' },

  // Period 6 Key Elements
  { number: 55, symbol: 'Cs', name: 'Caesium', mass: 132.91, period: 6, group: 1, category: 'alkali_metal', electronegativity: 0.79, valence: 1, shells: [2, 8, 18, 18, 8, 1], config: '[Xe] 6s¹' },
  { number: 56, symbol: 'Ba', name: 'Barium', mass: 137.33, period: 6, group: 2, category: 'alkaline_earth', electronegativity: 0.89, valence: 2, shells: [2, 8, 18, 18, 8, 2], config: '[Xe] 6s²' },
  { number: 78, symbol: 'Pt', name: 'Platinum', mass: 195.08, period: 6, group: 10, category: 'transition_metal', electronegativity: 2.28, valence: 4, shells: [2, 8, 18, 32, 17, 1], config: '[Xe] 4f¹⁴ 5d⁹ 6s¹' },
  { number: 79, symbol: 'Au', name: 'Gold', mass: 196.97, period: 6, group: 11, category: 'transition_metal', electronegativity: 2.54, valence: 3, shells: [2, 8, 18, 32, 18, 1], config: '[Xe] 4f¹⁴ 5d¹⁰ 6s¹' },
  { number: 80, symbol: 'Hg', name: 'Mercury', mass: 200.59, period: 6, group: 12, category: 'transition_metal', electronegativity: 2.00, valence: 2, shells: [2, 8, 18, 32, 18, 2], config: '[Xe] 4f¹⁴ 5d¹⁰ 6s²' },
  { number: 82, symbol: 'Pb', name: 'Lead', mass: 207.2, period: 6, group: 14, category: 'post_transition', electronegativity: 2.33, valence: 4, shells: [2, 8, 18, 32, 18, 4], config: '[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²' },
  { number: 92, symbol: 'U', name: 'Uranium', mass: 238.03, period: 7, group: 3, category: 'actinide', electronegativity: 1.38, valence: 6, shells: [2, 8, 18, 32, 21, 9, 2], config: '[Rn] 5f³ 6d¹ 7s²' }
];

const CATEGORIES = {
  alkali_metal: { label: 'Alkali Metals', bg: 'bg-rose-50 border-rose-300 text-rose-800', badge: 'bg-rose-100 text-rose-800' },
  alkaline_earth: { label: 'Alkaline Earth', bg: 'bg-amber-50 border-amber-300 text-amber-800', badge: 'bg-amber-100 text-amber-800' },
  transition_metal: { label: 'Transition Metals', bg: 'bg-sky-50 border-sky-300 text-sky-800', badge: 'bg-sky-100 text-sky-800' },
  post_transition: { label: 'Post-Transition', bg: 'bg-emerald-50 border-emerald-300 text-emerald-800', badge: 'bg-emerald-100 text-emerald-800' },
  metalloid: { label: 'Metalloids', bg: 'bg-teal-50 border-teal-300 text-teal-800', badge: 'bg-teal-100 text-teal-800' },
  nonmetal: { label: 'Reactive Nonmetals', bg: 'bg-blue-50 border-blue-300 text-blue-800', badge: 'bg-blue-100 text-blue-800' },
  halogen: { label: 'Halogens', bg: 'bg-indigo-50 border-indigo-300 text-indigo-800', badge: 'bg-indigo-100 text-indigo-800' },
  noble_gas: { label: 'Noble Gases', bg: 'bg-purple-50 border-purple-300 text-purple-800', badge: 'bg-purple-100 text-purple-800' },
  actinide: { label: 'Actinides', bg: 'bg-orange-50 border-orange-300 text-orange-800', badge: 'bg-orange-100 text-orange-800' }
};

export default function PeriodicTableAid({ grade = null }) {
  const [search, setSearch] = useState('');
  const [selectedElement, setSelectedElement] = useState(ELEMENTS[0]); // default Hydrogen
  const [viewMode, setViewMode] = useState(() => (Number(grade) >= 7 && Number(grade) <= 9 ? 'metals_split' : 'standard')); // 'standard' | 'metals_split' | 'electronegativity' | 'shells'
  const [activeCategory, setActiveCategory] = useState('all');

  const getMacroMetalClass = (el) => {
    if (el.category === 'metalloid') {
      return { group: 'Semi-Metal (Metalloid)', bg: 'bg-amber-100 border-amber-400 text-amber-900 font-bold' };
    }
    if (['nonmetal', 'halogen', 'noble_gas'].includes(el.category)) {
      return { group: 'Non-Metal', bg: 'bg-emerald-50 border-emerald-300 text-emerald-900' };
    }
    return { group: 'Metal', bg: 'bg-sky-50 border-sky-300 text-sky-900' };
  };

  const filteredElements = useMemo(() => {
    const s = search.trim().toLowerCase();
    return ELEMENTS.filter((el) => {
      const matchSearch =
        !s ||
        el.symbol.toLowerCase().includes(s) ||
        el.name.toLowerCase().includes(s) ||
        String(el.number) === s;
      const matchCat = activeCategory === 'all' || el.category === activeCategory;
      return matchSearch && matchCat;
    });
  }, [search, activeCategory]);

  // Color generator for electronegativity heatmap
  const getEnColor = (en) => {
    if (en === null || en === undefined) return 'bg-slate-100 text-slate-500 border-slate-200';
    // Range roughly 0.7 to 4.0
    const ratio = Math.min(1, Math.max(0, (en - 0.7) / (4.0 - 0.7)));
    if (ratio < 0.25) return 'bg-blue-50 border-blue-200 text-blue-900';
    if (ratio < 0.5) return 'bg-teal-50 border-teal-300 text-teal-900';
    if (ratio < 0.75) return 'bg-amber-100 border-amber-300 text-amber-900';
    return 'bg-rose-100 border-rose-300 text-rose-900 font-bold';
  };

  return (
    <div data-testid="periodic-table-aid" className="space-y-4 text-slate-800">
      {/* Search & View Controls */}
      <div className="flex flex-wrap items-center justify-between gap-2 bg-slate-50 p-2.5 rounded-xl border border-slate-200">
        <div className="relative flex-1 min-w-[180px]">
          <Search className="w-4 h-4 text-slate-400 absolute left-2.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            data-testid="input-element-search"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search element (e.g. Na, Carbon, 17)..."
            className="w-full pl-8 pr-3 py-1.5 text-xs rounded-lg border border-slate-200 focus:outline-none focus:ring-1 focus:ring-[#13519C]"
          />
        </div>

        <div className="flex flex-wrap items-center gap-1">
          <button
            data-testid="btn-view-metals-split"
            onClick={() => setViewMode('metals_split')}
            className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-colors ${
              viewMode === 'metals_split'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
            }`}
          >
            Metals / Semi-Metals / Non-Metals
          </button>
          <button
            data-testid="btn-view-standard"
            onClick={() => setViewMode('standard')}
            className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-colors ${
              viewMode === 'standard'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
            }`}
          >
            Families
          </button>
          <button
            data-testid="btn-view-electronegativity"
            onClick={() => setViewMode('electronegativity')}
            className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-colors ${
              viewMode === 'electronegativity'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
            }`}
          >
            Electronegativity
          </button>
          <button
            data-testid="btn-view-shells"
            onClick={() => setViewMode('shells')}
            className={`px-2.5 py-1 text-xs font-semibold rounded-md transition-colors ${
              viewMode === 'shells'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'bg-white text-slate-600 hover:bg-slate-100 border border-slate-200'
            }`}
          >
            Valence & Shells
          </button>
        </div>
      </div>

      {/* Category Pills Filter */}
      <div className="flex flex-wrap gap-1">
        <button
          onClick={() => setActiveCategory('all')}
          className={`px-2 py-0.5 text-[11px] rounded-full border transition-colors ${
            activeCategory === 'all'
              ? 'bg-slate-800 text-white border-slate-800'
              : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50'
          }`}
        >
          All Elements ({ELEMENTS.length})
        </button>
        {Object.entries(CATEGORIES).map(([key, cat]) => (
          <button
            key={key}
            onClick={() => setActiveCategory(activeCategory === key ? 'all' : key)}
            className={`px-2 py-0.5 text-[11px] rounded-full border transition-colors ${
              activeCategory === key
                ? `${cat.bg} font-bold shadow-sm`
                : 'bg-white text-slate-600 border-slate-200 hover:bg-slate-50'
            }`}
          >
            {cat.label}
          </button>
        ))}
      </div>

      {/* Grid of Elements */}
      <div className="overflow-x-auto pb-2">
        <div className="grid grid-cols-6 sm:grid-cols-9 md:grid-cols-10 gap-1.5 min-w-[340px]">
          {filteredElements.map((el) => {
            const isSelected = selectedElement?.number === el.number;
            const cat = CATEGORIES[el.category] || CATEGORIES.nonmetal;
            const macro = getMacroMetalClass(el);
            const heatBg =
              viewMode === 'electronegativity'
                ? getEnColor(el.electronegativity)
                : viewMode === 'metals_split'
                ? macro.bg
                : cat.bg;
            const isFirst20 = el.number <= 20;

            return (
              <button
                key={el.number}
                data-testid={`element-cell-${el.symbol}`}
                onClick={() => setSelectedElement(el)}
                className={`flex flex-col p-1.5 rounded-lg border text-left transition-all ${heatBg} ${
                  isSelected ? 'ring-2 ring-[#13519C] shadow-md scale-105 z-10' : 'hover:border-slate-400'
                } ${viewMode === 'metals_split' && isFirst20 ? 'ring-1 ring-slate-300' : ''}`}
              >
                <div className="flex justify-between items-center text-[10px] font-mono text-slate-500">
                  <span>{el.number}</span>
                  {viewMode === 'electronegativity' && (
                    <span className="font-semibold">{el.electronegativity ?? '—'}</span>
                  )}
                  {viewMode === 'shells' && (
                    <span className="font-semibold text-emerald-700">{el.valence}v</span>
                  )}
                </div>
                <div className="text-sm font-bold tracking-tight text-slate-900">{el.symbol}</div>
                <div className="text-[9px] truncate text-slate-600">{el.name}</div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Selected Element Inspector Card */}
      {selectedElement && (
        <div
          data-testid="element-inspector"
          className="bg-white p-3.5 rounded-xl border border-slate-200 shadow-sm space-y-3"
        >
          <div className="flex items-start justify-between">
            <div className="flex items-center gap-3">
              <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-indigo-50 to-blue-100 border border-indigo-200 flex flex-col items-center justify-center shadow-inner">
                <span className="text-[10px] font-mono text-slate-500 -mb-1">{selectedElement.number}</span>
                <span className="text-2xl font-black text-slate-900">{selectedElement.symbol}</span>
                <span className="text-[9px] font-mono text-slate-600">{selectedElement.mass}</span>
              </div>
              <div>
                <h4 className="text-base font-bold text-slate-900 flex items-center gap-2">
                  {selectedElement.name}
                  <span className="text-xs font-mono text-slate-500">Z = {selectedElement.number}</span>
                </h4>
                <div className="flex flex-wrap gap-1.5 mt-1">
                  <span className={`px-2 py-0.5 text-[10px] font-semibold rounded-full border ${CATEGORIES[selectedElement.category]?.badge}`}>
                    {CATEGORIES[selectedElement.category]?.label || 'Element'}
                  </span>
                  <span className="px-2 py-0.5 text-[10px] font-mono rounded-full bg-slate-100 text-slate-700">
                    Group {selectedElement.group} · Period {selectedElement.period}
                  </span>
                </div>
              </div>
            </div>

            {/* Valence Badge */}
            <div className="text-right">
              <div className="text-[10px] uppercase tracking-wider text-slate-400 font-bold">Valence e⁻</div>
              <div className="text-xl font-mono font-black text-[#13519C]">
                {selectedElement.valence}
              </div>
            </div>
          </div>

          {/* Bohr Model SVG Diagram & Shell Structure */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2 border-t border-slate-100">
            <div className="flex flex-col items-center justify-center p-2 bg-slate-50 rounded-lg border border-slate-200">
              <span className="text-[11px] font-semibold text-slate-600 mb-1 flex items-center gap-1">
                <Atom className="w-3.5 h-3.5 text-indigo-600" />
                Bohr Electron Shells
              </span>
              <svg viewBox="0 0 120 120" className="w-24 h-24">
                {/* Nucleus */}
                <circle cx="60" cy="60" r="10" fill="#13519C" />
                <text x="60" y="63" textAnchor="middle" fill="#ffffff" fontSize="7" fontWeight="bold">
                  {selectedElement.symbol}
                </text>

                {/* Shell rings and electron dots */}
                {selectedElement.shells.map((count, sIdx) => {
                  const radius = 18 + sIdx * 9;
                  const dots = [];
                  for (let i = 0; i < count; i++) {
                    const angle = (i * 2 * Math.PI) / count;
                    const dx = 60 + radius * Math.cos(angle);
                    const dy = 60 + radius * Math.sin(angle);
                    dots.push(<circle key={i} cx={dx} cy={dy} r="2" fill="#E11D48" />);
                  }
                  return (
                    <g key={sIdx}>
                      <circle cx="60" cy="60" r={radius} fill="none" stroke="#94A3B8" strokeDasharray="2 2" strokeWidth="0.8" />
                      {dots}
                    </g>
                  );
                })}
              </svg>
              <span className="text-[10px] font-mono text-slate-500 mt-1">
                Shells: {selectedElement.shells.join(' : ')}
              </span>
            </div>

            {/* Physical & Chemical Trends Details */}
            <div className="space-y-2 text-xs">
              <div className="flex justify-between items-center py-1 border-b border-slate-100">
                <span className="text-slate-500">Electron Configuration</span>
                <span className="font-mono font-bold text-slate-800">{selectedElement.config}</span>
              </div>
              <div className="flex justify-between items-center py-1 border-b border-slate-100">
                <span className="text-slate-500">Electronegativity (Pauling)</span>
                <span className="font-mono font-bold text-slate-800">
                  {selectedElement.electronegativity !== null ? selectedElement.electronegativity : 'N/A (Inert)'}
                </span>
              </div>
              <div className="flex justify-between items-center py-1 border-b border-slate-100">
                <span className="text-slate-500">Relative Atomic Mass ($A_r$)</span>
                <span className="font-mono font-bold text-slate-800">{selectedElement.mass} u</span>
              </div>
              <div className="text-[11px] text-slate-600 bg-amber-50/70 p-2 rounded border border-amber-200">
                <span className="font-semibold text-amber-900">National Curriculum Standards Note:</span>{' '}
                {selectedElement.valence === 1 && selectedElement.category === 'alkali_metal'
                  ? 'Readily loses 1 valence electron to form stable +1 cation.'
                  : selectedElement.category === 'halogen'
                  ? 'Needs 1 electron to achieve octet configuration; highly reactive oxidising agent.'
                  : selectedElement.category === 'noble_gas'
                  ? 'Complete outer valence shell; inert stable octet / duplet.'
                  : `Group ${selectedElement.group} element with ${selectedElement.shells.length} electron energy levels.`}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
