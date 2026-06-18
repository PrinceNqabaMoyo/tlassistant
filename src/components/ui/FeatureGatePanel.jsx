import React from 'react';
import { ArrowRight, AlertCircle } from 'lucide-react';

export default function FeatureGatePanel({
  title,
  description,
  badge,
  buttonLabel,
  onButtonClick,
  icon: Icon = AlertCircle,
}) {
  return (
    <div className="rounded-3xl border border-sky-100 bg-white p-6 shadow-sm shadow-sky-100/40">
      {badge ? (
        <span className="inline-flex rounded-full bg-[#13519C]/10 px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] text-[#13519C]">
          {badge}
        </span>
      ) : null}
      <div className="mt-4 flex items-start gap-4">
        <div className="rounded-2xl bg-amber-100 p-3 text-amber-700">
          <Icon className="h-6 w-6" />
        </div>
        <div className="flex-1">
          <h3 className="text-xl font-semibold text-slate-900">{title}</h3>
          <p className="mt-2 text-sm leading-7 text-slate-600">{description}</p>
          {buttonLabel && onButtonClick ? (
            <button
              type="button"
              onClick={onButtonClick}
              className="mt-5 inline-flex items-center gap-2 rounded-2xl bg-[#13519C] px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#0f3e77]"
            >
              {buttonLabel}
              <ArrowRight className="h-4 w-4" />
            </button>
          ) : null}
        </div>
      </div>
    </div>
  );
}
