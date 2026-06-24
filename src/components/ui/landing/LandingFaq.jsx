import React from 'react';
import { ChevronDown } from 'lucide-react';
import { FAQ } from '../../../app/constants/landingCopy';

const LandingFaq = ({ isLightPalette }) => {
    const [openIndex, setOpenIndex] = React.useState(0);
    const heading = isLightPalette ? 'text-slate-950' : 'text-white';
    const body = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const item = isLightPalette
        ? 'rounded-[24px] border border-sky-100 bg-white shadow-sm shadow-sky-100/30'
        : 'rounded-[24px] border border-white/10 bg-white/5 backdrop-blur-sm';

    return (
        <section id="faq" className="mt-24">
            <div className="max-w-3xl">
                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{FAQ.eyebrow}</p>
                <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heading}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                    {FAQ.title}
                </h2>
            </div>
            <div className="mt-10 grid gap-4">
                {FAQ.items.map((faq, index) => {
                    const isOpen = openIndex === index;
                    return (
                        <div key={faq.q} className={item}>
                            <button
                                type="button"
                                onClick={() => setOpenIndex(isOpen ? -1 : index)}
                                className="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
                                aria-expanded={isOpen}
                            >
                                <span className={`text-lg font-semibold ${heading}`}>{faq.q}</span>
                                <ChevronDown className={`h-5 w-5 shrink-0 transition-transform ${isOpen ? 'rotate-180' : ''} ${body}`} />
                            </button>
                            {isOpen && (
                                <p className={`px-6 pb-6 leading-8 ${body}`}>{faq.a}</p>
                            )}
                        </div>
                    );
                })}
            </div>
        </section>
    );
};

export default LandingFaq;
