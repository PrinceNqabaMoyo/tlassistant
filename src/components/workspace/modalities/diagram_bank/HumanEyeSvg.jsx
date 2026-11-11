import React, { useState, useEffect } from 'react';
import InteractiveCallouts from './InteractiveCallouts';
import { Eye, BookOpen, FileText } from 'lucide-react';

function normalizeEyeView(rawView) {
  const v = String(rawView || 'textbook').toLowerCase().trim();
  if (v === 'exam' || v === 'exam_paper' || v === 'stipple') return 'exam';
  return 'textbook';
}

const VIEW_METADATA = {
  textbook: {
    label: 'Human Eye Longitudinal Cross-Section Master',
    Icon: BookOpen,
  },
  exam: {
    label: 'Examination Ink Stipple Line-Art',
    Icon: FileText,
  },
};

/**
 * Authentic Longitudinal Cross-Section of the Human Eye.
 * Aligned with South African Life Sciences Grade 12 (Human responses to the environment)
 * and Natural Sciences Grade 8.
 *
 * Implements Rule 0d-14 (The Heart Architecture Standard):
 * - Authentic unlabeled Textbook Master + NSC Exam Stipple plates in public/diagrams/
 * - Zero hand-coded geometric SVG clipart (polygon, circle, ellipse)
 * - Single locked view in question mode; multi-view toggle in Reference Atlas mode
 * - Transparent SVG overlay with InteractiveCallouts
 */
export default function HumanEyeSvg({
  pins = [],
  landmarks = [],
  labels = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
  gradeMask = 'g12',
  view,
  defaultView = 'textbook',
  allowViewSwitch = false,
}) {
  const initialView = normalizeEyeView(view || defaultView);
  const [activeView, setActiveView] = useState(initialView);

  useEffect(() => {
    setActiveView(normalizeEyeView(view || defaultView));
  }, [view, defaultView]);

  // Normalize pins from modern contract or legacy labels
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
    <div data-testid="human-eye-root" className="flex flex-col items-center w-full max-w-2xl select-none space-y-2">
      {/* Header: Locked View in Question Mode; View Switcher in Reference Atlas Mode */}
      {allowViewSwitch ? (
        <div className="flex items-center justify-between w-full px-2 py-1 bg-slate-50 border border-slate-200 rounded-xl text-xs">
          <span className="text-[11px] font-bold text-slate-600 uppercase tracking-wide flex items-center gap-1.5 font-mono">
            <Eye className="w-3.5 h-3.5 text-sky-600" />
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
            >
              <BookOpen className="w-3 h-3" />
              <span>Textbook Master</span>
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
            >
              <FileText className="w-3 h-3" />
              <span>Exam Paper</span>
            </button>
          </div>
        </div>
      ) : (
        <div
          data-testid="human_eye-locked-view-badge"
          className="flex items-center justify-between w-full px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-xl text-xs"
        >
          <span className="text-[11px] font-bold text-slate-700 flex items-center gap-1.5 font-mono">
            <CurrentViewIcon className="w-3.5 h-3.5 text-[#13519C]" />
            <span>{currentMeta.label}</span>
          </span>
          <span className="text-[10px] font-mono text-slate-500 uppercase tracking-wider">
            {gradeMask === 'g8' ? 'Grade 8 Natural Sciences' : 'Grade 12 Life Sciences'}
          </span>
        </div>
      )}

      {/* Backward-compatibility badge testid */}
      <span data-testid="eye-locked-view-badge" className="sr-only">Locked View</span>

      {/* Primary SVG Canvas */}
      <svg
        viewBox={viewBox}
        data-testid="human-eye-canvas"
        className="w-full h-auto drop-shadow-sm bg-white rounded-xl border border-slate-100 transition-all duration-300"
        style={{ minWidth: '320px', maxHeight: '520px' }}
      >
        {/* VIEW 1: TEXTBOOK MASTER */}
        {activeView === 'textbook' && (
          <g id="view_textbook_master">
            <image
              href="/diagrams/human_eye_textbook.jpg"
              x="50"
              y="0"
              width="500"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* VIEW 2: NSC EXAMINATION STIPPLE LINE-ART */}
        {activeView === 'exam' && (
          <g id="view_exam_paper">
            <image
              href="/diagrams/human_eye_exam_stipple.jpg"
              x="50"
              y="0"
              width="500"
              height="480"
              preserveAspectRatio="xMidYMid meet"
              className="select-none pointer-events-none"
            />
          </g>
        )}

        {/* Dynamic Interactive Callouts Layer */}
        <InteractiveCallouts
          pins={effectivePins}
          landmarks={landmarks}
          activePin={activePin}
          onSelectPin={onSelectPin}
          viewBox={viewBox}
        />
      </svg>

      {/* Attribution & Alignment */}
      <div className="flex items-center justify-between w-full text-[10px] text-slate-400 font-mono">
        <span>Curriculum Standard: Grade 8 NS &amp; Grade 12 Life Sciences (Eye &amp; Vision)</span>
        <span>Unlabeled Medical Master • Calibrated Pin Overlay</span>
      </div>
    </div>
  );
}
