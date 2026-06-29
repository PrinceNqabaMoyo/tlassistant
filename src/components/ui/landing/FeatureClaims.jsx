import React from 'react';
import { PlayCircle } from 'lucide-react';
import { FEATURE_CLAIMS } from '../../../app/constants/landingCopy';

// Each "what the app does" claim with its own demo-media slot. A real clip can
// be dropped under any claim by setting demo.type = 'youtube' + demo.src in
// landingCopy.js; until then the slot shows a labelled "coming soon" placeholder
// (we never fake a demo).
const ClaimDemo = ({ demo, isLightPalette }) => {
    const frame = isLightPalette
        ? 'overflow-hidden rounded-[24px] border border-sky-100 bg-slate-50'
        : 'overflow-hidden rounded-[24px] border border-white/10 bg-slate-950/80';

    if (demo.type === 'youtube') {
        return (
            <div className={frame}>
                <iframe
                    className="aspect-video w-full"
                    src={demo.src}
                    title={demo.label}
                    frameBorder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    allowFullScreen
                ></iframe>
            </div>
        );
    }

    return (
        <div className={`${frame} flex aspect-video w-full flex-col items-center justify-center gap-2`}>
            <PlayCircle className={`h-10 w-10 ${isLightPalette ? 'text-slate-300' : 'text-white/30'}`} />
            <p className={`text-sm font-semibold ${isLightPalette ? 'text-slate-400' : 'text-white/40'}`}>{demo.label}</p>
        </div>
    );
};

const FeatureClaims = ({ isLightPalette }) => {
    const heading = isLightPalette ? 'text-slate-950' : 'text-white';
    const body = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const card = isLightPalette
        ? 'rounded-[28px] border border-sky-100 bg-white p-5 shadow-lg shadow-sky-100/35'
        : 'rounded-[28px] border border-white/10 bg-white/5 p-5 backdrop-blur-sm';

    return (
        <section id="feature-claims" className="mt-24">
            <div className="max-w-3xl">
                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{FEATURE_CLAIMS.eyebrow}</p>
                <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heading}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                    {FEATURE_CLAIMS.title}
                </h2>
                <p className={`mt-5 text-lg leading-8 ${body}`}>{FEATURE_CLAIMS.intro}</p>
            </div>

            <div className="mt-10 grid gap-5 lg:grid-cols-2">
                {FEATURE_CLAIMS.claims.map((claim) => (
                    <div key={claim.key} className={card}>
                        <ClaimDemo demo={claim.demo} isLightPalette={isLightPalette} />
                        <h3 className={`mt-5 text-xl font-semibold ${heading}`}>{claim.title}</h3>
                        <p className={`mt-3 leading-7 ${body}`}>{claim.body}</p>
                    </div>
                ))}
            </div>
        </section>
    );
};

export default FeatureClaims;
