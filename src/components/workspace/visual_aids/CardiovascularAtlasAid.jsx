import React, { useState } from 'react';
import HumanHeartSvg from '../modalities/diagram_bank/HumanHeartSvg';
import { HeartPulse, Info } from 'lucide-react';

/**
 * Pedagogical Reference Landmarks for the Exploratory Visual Aid Sidecar.
 * Strictly highlights physiological circuits and directional oxygenation pathways
 * without leaking the specific chamber/valve target names tested by Pin A / Pin B.
 */
const ATLAS_LANDMARKS = [
  { text: 'Systemic Outflow (To Body)', anchor: [300, 95], default_box: [540, 65], side: 'right', role: 'landmark' },
  { text: 'Venous Inflow (From Body)', anchor: [210, 120], default_box: [60, 75], side: 'left', role: 'landmark' },
  { text: 'Pulmonary Outflow (To Lungs)', anchor: [350, 145], default_box: [540, 120], side: 'right', role: 'landmark' },
  { text: 'Deoxygenated Side (Right)', anchor: [215, 235], default_box: [60, 200], side: 'left', role: 'landmark' },
  { text: 'Oxygenated Side (Left)', anchor: [375, 215], default_box: [540, 215], side: 'right', role: 'landmark' },
  { text: 'Thin Wall (Low Pressure)', anchor: [270, 355], default_box: [60, 365], side: 'left', role: 'landmark' },
  { text: 'Thick Myocardium (High Pressure)', anchor: [380, 340], default_box: [540, 360], side: 'right', role: 'landmark' },
  { text: 'Septum (Prevents Mixing)', anchor: [325, 350], default_box: [540, 415], side: 'right', role: 'landmark' },
];

const CYCLE_STATES = [
  {
    id: 'static',
    label: 'Anatomical Overview',
    duration: 'Resting Reference',
    desc: 'Compare how the 3D coronal cross-section translates into a directional blood-flow schematic and a 2D examination line-art drawing.',
  },
  {
    id: 'atrial_systole',
    label: '1. Atrial Systole',
    duration: '0,1 s',
    desc: 'Both upper receiving chambers contract simultaneously for 0,1 s, forcing blood downward through the open atrioventricular valves into the lower pumping chambers.',
  },
  {
    id: 'ventricular_systole',
    label: '2. Ventricular Systole ("Lubb")',
    duration: '0,3 s',
    desc: 'The muscular lower chambers contract forcefully from the apex upward. High pressure snaps the atrioventricular valves shut ("lubb" sound) and ejects blood into the outgoing arteries.',
  },
  {
    id: 'general_diastole',
    label: '3. General Diastole ("Dubb")',
    duration: '0,4 s',
    desc: 'All four chambers relax for 0,4 s. Arterial back-pressure snaps the semilunar valves shut ("dubb" sound) while blood flows passively into the upper chambers.',
  },
];

export default function CardiovascularAtlasAid() {
  const [cycleState, setCycleState] = useState('static');
  const activeMeta = CYCLE_STATES.find((c) => c.id === cycleState) || CYCLE_STATES[0];

  return (
    <div data-testid="cardiovascular-atlas-aid" className="space-y-4">
      <div className="p-3 bg-white border border-slate-200 rounded-xl space-y-2.5">
        <div className="flex items-center justify-between">
          <span className="text-xs font-bold text-slate-800 flex items-center gap-1.5">
            <HeartPulse className="w-4 h-4 text-rose-600" />
            <span>Cardiac Cycle Phase Explorer</span>
          </span>
          <span className="text-[11px] font-mono text-indigo-700 bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
            {activeMeta.duration}
          </span>
        </div>

        <div className="grid grid-cols-2 gap-1.5">
          {CYCLE_STATES.map((st) => (
            <button
              key={st.id}
              type="button"
              data-testid={`btn-atlas-phase-${st.id}`}
              onClick={() => setCycleState(st.id)}
              className={`px-2.5 py-1.5 rounded-lg text-left text-[11px] font-semibold transition border ${
                cycleState === st.id
                  ? 'bg-[#13519C] text-white border-[#13519C] shadow-2xs'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              {st.label}
            </button>
          ))}
        </div>

        <div className="p-2.5 bg-slate-50 border border-slate-200/80 rounded-lg text-xs text-slate-700 flex items-start gap-2">
          <Info className="w-4 h-4 text-[#13519C] shrink-0 mt-0.5" />
          <span>{activeMeta.desc}</span>
        </div>
      </div>

      <div className="p-3 bg-white border border-slate-200 rounded-xl">
        <HumanHeartSvg
          pins={[]}
          landmarks={ATLAS_LANDMARKS}
          state={cycleState}
          gradeMask="g9"
          allowViewSwitch={true}
          defaultView="textbook"
        />
      </div>
    </div>
  );
}
