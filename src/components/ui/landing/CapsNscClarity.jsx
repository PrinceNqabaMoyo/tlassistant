import React from 'react';
import { ArrowRight, ArrowDown } from 'lucide-react';
import { CAPS_NSC } from '../../../app/constants/landingCopy';

// The trust centrepiece: dissolves the "IEB/SACAI teach a different curriculum"
// myth with the accurate frame — CAPS (one curriculum) → DBE/IEB/SACAI (exam
// styles) → one NSC (Umalusi-assured). Wording lives in landingCopy.js.
const CapsNscClarity = ({ isLightPalette }) => {
    const heading = isLightPalette ? 'text-slate-950' : 'text-white';
    const body = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const muted = isLightPalette ? 'text-slate-500' : 'text-white/60';
    const card = isLightPalette
        ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/35'
        : 'rounded-[28px] border border-white/10 bg-white/5 p-6 backdrop-blur-sm';
    const chip = isLightPalette
        ? 'rounded-2xl border border-sky-100 bg-slate-50 px-4 py-3 text-center'
        : 'rounded-2xl border border-white/10 bg-slate-950/60 px-4 py-3 text-center';

    const { flow, table, aligned } = CAPS_NSC;

    return (
        <section id="caps-nsc" className="mt-24">
            <div className="max-w-3xl">
                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{CAPS_NSC.eyebrow}</p>
                <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heading}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                    {CAPS_NSC.title}
                </h2>
                <p className={`mt-5 text-lg leading-8 ${body}`}>{CAPS_NSC.intro}</p>
            </div>

            {/* "Did you know" highlight band */}
            <div className={`mt-8 rounded-[28px] border px-6 py-5 ${isLightPalette ? 'border-[#FF9100]/30 bg-[#FF9100]/8' : 'border-[#FF9100]/35 bg-[#FF9100]/12'}`}>
                <p className={`text-lg font-semibold leading-8 ${heading}`}>{CAPS_NSC.didYouKnow}</p>
            </div>

            {/* CAPS -> three bodies -> one NSC flow */}
            <div className={`mt-10 ${card}`}>
                <div className="grid items-center gap-4 lg:grid-cols-[0.9fr_auto_1.4fr_auto_0.9fr]">
                    <div className={`${chip} h-full`}>
                        <p className={`text-lg font-bold ${heading}`}>{flow.foundation.label}</p>
                        <p className={`mt-1 text-xs leading-5 ${muted}`}>{flow.foundation.caption}</p>
                    </div>

                    <div className="flex justify-center">
                        <ArrowRight className={`hidden h-6 w-6 lg:block ${muted}`} />
                        <ArrowDown className={`h-6 w-6 lg:hidden ${muted}`} />
                    </div>

                    <div className="grid gap-3 sm:grid-cols-3">
                        {flow.bodies.map((b) => (
                            <div key={b.label} className={chip}>
                                <p className={`text-base font-bold ${heading}`}>{b.label}</p>
                                <p className={`mt-1 text-xs leading-5 ${muted}`}>{b.caption}</p>
                            </div>
                        ))}
                    </div>

                    <div className="flex justify-center">
                        <ArrowRight className={`hidden h-6 w-6 lg:block ${muted}`} />
                        <ArrowDown className={`h-6 w-6 lg:hidden ${muted}`} />
                    </div>

                    <div className={`rounded-2xl border px-4 py-3 text-center ${isLightPalette ? 'border-[#2B7BD8]/30 bg-[#13519C]/8' : 'border-[#2B7BD8]/40 bg-[#13519C]/20'} h-full`}>
                        <p className={`text-lg font-bold ${heading}`}>{flow.outcome.label}</p>
                        <p className={`mt-1 text-xs leading-5 ${muted}`}>{flow.outcome.caption}</p>
                    </div>
                </div>
            </div>

            {/* Comparison table */}
            <div className={`mt-6 overflow-hidden ${card}`}>
                <div className="overflow-x-auto">
                    <table className="w-full border-collapse text-left text-sm">
                        <thead>
                            <tr>
                                <th className={`py-3 pr-4 text-xs font-semibold uppercase tracking-[0.2em] ${muted}`}></th>
                                {table.columns.map((col) => (
                                    <th key={col} className={`py-3 px-4 text-base font-bold ${heading}`}>{col}</th>
                                ))}
                            </tr>
                        </thead>
                        <tbody>
                            {table.rows.map((row, rIdx) => (
                                <tr key={row.label} className={rIdx < table.rows.length - 1 ? (isLightPalette ? 'border-b border-sky-100' : 'border-b border-white/10') : ''}>
                                    <td className={`py-3 pr-4 align-top text-sm font-semibold ${heading}`}>{row.label}</td>
                                    {row.values.map((v, i) => (
                                        <td key={i} className={`py-3 px-4 align-top leading-6 ${body}`}>{v}</td>
                                    ))}
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
                <p className={`mt-3 text-xs leading-6 ${muted}`}>
                    The first three rows are identical across all three bodies — that is the point. Only assessment style differs.
                </p>
            </div>

            <div className={`mt-6 rounded-[28px] border px-6 py-5 ${isLightPalette ? 'border-[#2B7BD8]/25 bg-[#13519C]/6' : 'border-[#2B7BD8]/35 bg-[#13519C]/15'}`}>
                <p className={`text-lg font-semibold leading-8 ${heading}`}>{CAPS_NSC.framing}</p>
                <p className={`mt-3 text-xs leading-6 ${muted}`}>{CAPS_NSC.disclaimer}</p>
            </div>

            {/* Plain-language "curriculum aligned" promise */}
            <div className={`mt-6 ${card}`}>
                <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FFD166]">{aligned.heading}</p>
                <p className={`mt-3 text-lg leading-8 ${body}`}>{aligned.body}</p>
                <div className="mt-4 flex flex-wrap gap-3">
                    {aligned.bodies.map((b) => (
                        <span
                            key={b}
                            className={`inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-semibold ${isLightPalette ? 'bg-[#13519C]/10 text-[#13519C]' : 'bg-[#2B7BD8]/20 text-blue-100'}`}
                        >
                            <span className="h-1.5 w-1.5 rounded-full bg-[#FF9100]" />
                            {b}
                        </span>
                    ))}
                </div>
            </div>
        </section>
    );
};

export default CapsNscClarity;
