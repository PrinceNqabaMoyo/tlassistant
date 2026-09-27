import React from 'react';
import { Lightbulb, Layers, HelpCircle, ArrowRight, ShieldCheck, Sparkles } from 'lucide-react';

const DEFAULT_CHIP_TEMPLATES = [
  { id: 'explain_rule', icon: Lightbulb, label: 'Why do we use this rule?', query: 'explain_underlying_rule' },
  { id: 'break_steps', icon: Layers, label: 'Break this into 2 smaller steps', query: 'decompose_step' },
  { id: 'common_pitfall', icon: HelpCircle, label: 'What is the most common mistake here?', query: 'explain_common_misconception' },
];

export default function DeclarativeSocraticChips({
  misconceptionTags = [],
  activeSubskill = '',
  onSelectChip,
  isLoading = false,
}) {
  // Generate contextual chips based on misconception tags
  const getContextualChips = () => {
    if (!misconceptionTags || misconceptionTags.length === 0) {
      return DEFAULT_CHIP_TEMPLATES;
    }

    const tag = misconceptionTags[0];
    const chips = [...DEFAULT_CHIP_TEMPLATES];

    if (tag.includes('vat') || tag.includes('net_vs_gross')) {
      chips[0] = { id: 'vat_rule', icon: Lightbulb, label: 'Explain Net vs Gross VAT calculation', query: 'explain_vat_rule' };
    } else if (tag.includes('debit_credit') || tag.includes('contra')) {
      chips[0] = { id: 'contra_rule', icon: Lightbulb, label: 'Why is Bank debited instead of credited?', query: 'explain_contra_rule' };
    } else if (tag.includes('sign') || tag.includes('factor')) {
      chips[0] = { id: 'math_factor', icon: Lightbulb, label: 'How do I determine the signs when factoring?', query: 'explain_factoring_signs' };
    }

    return chips;
  };

  const chips = getContextualChips();

  return (
    <div className="w-full bg-slate-900/90 border border-slate-800 rounded-2xl p-3.5 backdrop-blur shadow-lg flex flex-col gap-2.5">
      <div className="flex items-center justify-between text-xs text-slate-400 font-medium px-1">
        <span className="flex items-center gap-1.5 text-indigo-400 font-semibold uppercase tracking-wider text-[11px]">
          <Sparkles className="w-3.5 h-3.5" /> Socratic Assistance
        </span>
        <span className="text-[11px] text-slate-500">1-Tap Guidance</span>
      </div>

      <div className="flex flex-wrap gap-2">
        {chips.map((chip) => {
          const Icon = chip.icon;
          return (
            <button
              key={chip.id}
              disabled={isLoading}
              onClick={() => onSelectChip(chip.query, chip.label)}
              className="flex items-center gap-2 px-3 py-2 rounded-xl bg-slate-800/90 hover:bg-indigo-950/60 hover:border-indigo-500/50 border border-slate-700/70 text-slate-200 hover:text-indigo-200 text-xs font-medium transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed group text-left"
            >
              <Icon className="w-3.5 h-3.5 text-indigo-400 group-hover:text-indigo-300 shrink-0" />
              <span>{chip.label}</span>
              <ArrowRight className="w-3 h-3 text-slate-500 group-hover:text-indigo-400 transition-transform group-hover:translate-x-0.5 ml-auto" />
            </button>
          );
        })}
      </div>
    </div>
  );
}
