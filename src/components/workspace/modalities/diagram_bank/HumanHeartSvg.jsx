import React, { useState, useEffect } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import { BookOpen, Activity, FileText } from 'lucide-react';

function normalizeHeartView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'flow' || v === 'blood_flow' || v === 'circulation') return 'flow';
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Textbook Coronal Cross-Section',
    Icon: BookOpen,
  },
  flow: {
    label: 'Directional Blood Flow Schematic',
    Icon: Activity,
  },
  exam: {
    label: 'Examination Line-Art Diagram',
    Icon: FileText,
  },
};

/**
 * Authentic Textbook & Examination Human Heart Visual Component.
 *
 * Architectural Modes:
 * - Question Card Mode (`allowViewSwitch = false`, default): Renders ONLY the single
 *   locked view prescribed by the backend question (`view`: 'textbook' | 'flow' | 'exam')
 *   with zero student-facing view switcher buttons.
 * - Exploratory Visual Aid / Reference Atlas Mode (`allowViewSwitch = true`): Exposes
 *   the multi-view toggle inside `CognitiveSidecarDrawer` so learners can compare how
 *   3D coronal anatomy translates into blood-flow schematics and 2D examination drawings.
 */
export default function HumanHeartSvg({
  pins = [],
  landmarks = [],
  labels = [],
  activePin,
  onSelectPin,
  state = 'static',
  gradeMask = 'g9',
  viewBox = '0 0 600 480',
  view,
  defaultView = 'textbook',
  allowViewSwitch = false,
}) {
  const initialView = normalizeHeartView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);

  useEffect(() => {
    setActiveView(normalizeHeartView(view || defaultView));
  }, [view, defaultView]);

  // Normalize pins if legacy labels prop was passed
  const effectivePins = (pins && pins.length > 0)
    ? pins
    : (labels && labels.length > 0
        ? labels.map((l) => ({
            pin: l.id || l.pin,
            anchor: [l.x !== undefined ? (l.x / 100) * 600 : 300, l.y !== undefined ? (l.y / 100) * 480 : 240],
            default_box: [l.x < 50 ? 60 : 540, l.y !== undefined ? (l.y / 100) * 480 : 240],
            side: l.x < 50 ? 'left' : 'right',
            role: 'target',
          }))
        : []);

  const currentMeta = VIEW_METADATA[activeView] || VIEW_METADATA.textbook;
  const CurrentViewIcon = currentMeta.Icon;

  return (
    <div className="flex flex-col items-center w-full max-w-2xl select-none space-y-2">
      {/* Visual Modality Header: Single Locked View in Question Mode; Interactive Switcher in Visual Aid / Reference Atlas Mode */}
      {allowViewSwitch ? (
        <div className="flex items-center justify-between w-full px-2 py-1 bg-slate-50 border border-slate-200 rounded-xl text-xs">
          <span className="text-[11px] font-bold text-slate-600 uppercase tracking-wide flex items-center gap-1.5 font-mono">
            <BookOpen className="w-3.5 h-3.5 text-blue-600" />
            Reference View:
          </span>
          <div className="flex gap-1">
            <button
              type="button"
              data-testid="btn-view-textbook"
              onClick={() => setActiveView('textbook')}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                activeView === 'textbook'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
              }`}
              title="Textbook Medical Coronal Section (Unlabeled Internal Anatomy)"
            >
              <BookOpen className="w-3 h-3" />
              <span>Textbook Cross-Section</span>
            </button>

            <button
              type="button"
              data-testid="btn-view-flow"
              onClick={() => setActiveView('flow')}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                activeView === 'flow'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
              }`}
              title="Directional Blood Circulation & Chamber Flow Vector"
            >
              <Activity className="w-3 h-3" />
              <span>Blood Flow</span>
            </button>

            <button
              type="button"
              data-testid="btn-view-exam"
              onClick={() => setActiveView('exam')}
              className={`px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer flex items-center gap-1 ${
                activeView === 'exam'
                  ? 'bg-[#13519C] text-white shadow-2xs'
                  : 'bg-white text-slate-700 hover:bg-slate-100 border border-slate-200'
              }`}
              title="Authentic Unlabeled Scientific Ink Stipple Line-Art"
            >
              <FileText className="w-3 h-3" />
              <span>Exam Paper</span>
            </button>
          </div>
        </div>
      ) : (
        <div
          data-testid="heart-locked-view-badge"
          className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
        >
          <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
            <CurrentViewIcon className="w-3.5 h-3.5 text-[#13519C]" />
            <span>{currentMeta.label}</span>
          </span>
          <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
            {gradeMask === 'g10' ? 'Grade 10 Life Sciences' : 'Grade 9 Natural Sciences'}
          </span>
        </div>
      )}

      {/* Primary SVG Presentation Canvas */}
      <svg
        viewBox={viewBox}
        className="w-full h-auto drop-shadow-sm bg-white rounded-xl border border-slate-100 transition-all duration-300"
        style={{ minWidth: '320px', maxHeight: '520px' }}
      >
        {/* VIEW 1: UNLABELED TEXTBOOK MEDICAL MASTER (Coronal Section with volumetric muscle depth) */}
        {activeView === 'textbook' && (
          <g id="view_textbook_master">
            <image
              href="/diagrams/generated_textbook_heart_coronal.jpg"
              x="60"
              y="0"
              width="480"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* VIEW 2: UNLABELED BLOOD FLOW VECTOR SCHEMATIC (Cleaned Wapcaplet SVG with zero baked labels) */}
        {activeView === 'flow' && (
          <g id="view_flow_schematic">
            <image
              href="/diagrams/wapcaplet_clean.svg"
              x="85"
              y="10"
              width="470"
              height="460"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* VIEW 3: UNLABELED SCIENTIFIC INK STIPPLE LINE-ART */}
        {activeView === 'exam' && (
          <g id="view_exam_paper">
            <image
              href="/diagrams/generated_exam_heart_stipple.jpg"
              x="60"
              y="0"
              width="480"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* Dynamic Interactive Callouts Layer (Elbow leader lines + Pins + Landmark labels) */}
        <InteractiveCallouts
          pins={effectivePins}
          landmarks={landmarks}
          activePin={activePin}
          onSelectPin={onSelectPin}
          viewBox={viewBox}
        />
      </svg>

      {/* Attribution & Curriculum Alignment Badge */}
      <div className="flex items-center justify-between w-full text-[10px] text-slate-400 font-mono">
        <span>Curriculum Standard: Grade 9 NS &amp; Grade 10 Life Sciences</span>
        <span>
          {activeView === 'flow'
            ? 'Vector Flow: Wapcaplet (CC-BY-SA 3.0, Unlabeled)'
            : 'Unlabeled Medical Master • Calibrated Pin Overlay'}
        </span>
      </div>
    </div>
  );
}
