import React from 'react';
import { X, Check } from 'lucide-react';
import { NOT_A_CHATBOT } from '../../../app/constants/landingCopy';

// The core differentiator: Fundile is not a chatbot. A side-by-side that
// contrasts "AI chatbot" with "Fundile" across the aspects the learner cares
// about. Wording lives in landingCopy.js.
const NotAChatbot = ({ isLightPalette }) => {
    const heading = isLightPalette ? 'text-slate-950' : 'text-white';
    const body = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const muted = isLightPalette ? 'text-slate-500' : 'text-white/60';
    const card = isLightPalette
        ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/35'
        : 'rounded-[28px] border border-white/10 bg-white/5 p-6 backdrop-blur-sm';

    return (
        <section id="not-a-chatbot" className="mt-24">
            <div className="max-w-3xl">
                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{NOT_A_CHATBOT.eyebrow}</p>
                <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heading}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                    {NOT_A_CHATBOT.title}
                </h2>
                <p className={`mt-5 text-lg leading-8 ${body}`}>{NOT_A_CHATBOT.intro}</p>
            </div>

            <div className="mt-10 grid gap-5 lg:grid-cols-2">
                {/* AI chatbot column */}
                <div className={card}>
                    <div className="flex items-center gap-3">
                        <span className={`flex h-10 w-10 items-center justify-center rounded-2xl ${isLightPalette ? 'bg-rose-100 text-rose-600' : 'bg-rose-500/15 text-rose-300'}`}>
                            <X className="h-5 w-5" />
                        </span>
                        <h3 className={`text-2xl font-semibold ${heading}`}>An AI chatbot</h3>
                    </div>
                    <ul className="mt-6 space-y-4">
                        {NOT_A_CHATBOT.rows.map((row) => (
                            <li key={row.aspect}>
                                <p className={`text-xs font-semibold uppercase tracking-[0.2em] ${muted}`}>{row.aspect}</p>
                                <p className={`mt-1 leading-7 ${body}`}>{row.chatbot}</p>
                            </li>
                        ))}
                    </ul>
                </div>

                {/* Fundile column */}
                <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-[#2B7BD8]/30 bg-[#13519C]/6 shadow-lg shadow-sky-100/40' : 'border-[#2B7BD8]/40 bg-[#13519C]/18 backdrop-blur-sm'}`}>
                    <div className="flex items-center gap-3">
                        <span className={`flex h-10 w-10 items-center justify-center rounded-2xl ${isLightPalette ? 'bg-emerald-100 text-emerald-600' : 'bg-emerald-500/15 text-emerald-300'}`}>
                            <Check className="h-5 w-5" />
                        </span>
                        <h3 className={`text-2xl font-semibold ${heading}`}>Fundile</h3>
                    </div>
                    <ul className="mt-6 space-y-4">
                        {NOT_A_CHATBOT.rows.map((row) => (
                            <li key={row.aspect}>
                                <p className={`text-xs font-semibold uppercase tracking-[0.2em] ${muted}`}>{row.aspect}</p>
                                <p className={`mt-1 font-medium leading-7 ${heading}`}>{row.fundile}</p>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>
        </section>
    );
};

export default NotAChatbot;
