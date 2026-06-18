import React from 'react';
import FundileLogo from './FundileLogo';
import { ArrowRight, BookOpen, BrainCircuit, CheckCircle, GraduationCap, LayoutDashboard, PenTool, ShieldCheck, Sparkles, Target, Trophy, Users } from 'lucide-react';

// Landing Page Component
const LandingPage = ({ onGetStarted, palette = 'dark' }) => {
    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };

    const isLightPalette = palette === 'light';
    const shellClassName = isLightPalette ? 'relative min-h-screen bg-slate-50 text-slate-900' : 'relative min-h-screen bg-slate-950 text-white';
    const overlayClassName = isLightPalette
        ? 'absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(43,123,216,0.18),_transparent_34%),radial-gradient(circle_at_20%_20%,_rgba(255,145,0,0.10),_transparent_24%),linear-gradient(180deg,_#f8fbff_0%,_#eef5ff_45%,_#f8fafc_100%)]'
        : 'absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(43,123,216,0.28),_transparent_34%),radial-gradient(circle_at_20%_20%,_rgba(255,145,0,0.14),_transparent_25%),linear-gradient(180deg,_#08101f_0%,_#0b1328_45%,_#050914_100%)]';
    const heroSectionTextClassName = isLightPalette ? 'text-slate-950' : 'text-white';
    const bodyTextClassName = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const mutedTextClassName = isLightPalette ? 'text-slate-500' : 'text-white/70';
    const surfaceClassName = isLightPalette ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/40 transition duration-300 hover:-translate-y-1 hover:border-sky-200' : 'rounded-[28px] border border-white/10 bg-white/5 p-6 backdrop-blur-sm transition duration-300 hover:-translate-y-1 hover:border-white/20 hover:bg-white/[0.08]';
    const featureCardClassName = isLightPalette ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/35 transition duration-300 hover:border-[#2B7BD8]/30 hover:shadow-xl hover:shadow-sky-100/50' : 'rounded-[28px] border border-white/10 bg-slate-900/65 p-6 shadow-lg shadow-black/20 transition duration-300 hover:border-[#2B7BD8]/35 hover:bg-slate-900';
    const audienceCardClassName = isLightPalette ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/35' : 'rounded-[28px] border border-white/10 bg-white/5 p-6 backdrop-blur-sm';

    const valueCards = [
        {
            icon: Target,
            title: 'CAPS-aligned support',
            description: 'Stay closer to what your subject and grade actually expect instead of jumping between random online resources.',
            accent: 'text-blue-300',
        },
        {
            icon: BrainCircuit,
            title: 'Guided feedback',
            description: 'Get help that explains, checks, and guides instead of leaving you with a final answer and no understanding.',
            accent: 'text-violet-300',
        },
        {
            icon: PenTool,
            title: 'Study + classwork in one place',
            description: 'Move from structured practice to assignments and revision without switching tools or losing context.',
            accent: 'text-amber-300',
        },
    ];

    const featureCards = [
        {
            icon: BookOpen,
            title: 'Topic-based revision',
            description: 'Work through subjects by topic with clearer structure and less overwhelm.',
        },
        {
            icon: BrainCircuit,
            title: 'Curriculum Helper',
            description: 'Use guided tutoring and structured support when you need help understanding a concept.',
        },
        {
            icon: CheckCircle,
            title: 'Feedback that teaches',
            description: 'See what was right, what was missing, and how to improve on the next attempt.',
        },
        {
            icon: LayoutDashboard,
            title: 'One learning workspace',
            description: 'Keep writing, practising, and revising inside the same focused study environment.',
        },
        {
            icon: Trophy,
            title: 'Momentum over guesswork',
            description: 'Build confidence through repeated practice, clearer direction, and visible progress.',
        },
        {
            icon: ShieldCheck,
            title: 'Built for real study habits',
            description: 'Designed to support both independent learning and teacher-guided learning routines.',
        },
    ];

    const audienceCards = [
        {
            icon: GraduationCap,
            title: 'Students',
            description: 'For learners who want more structure, clearer feedback, and less confusion when studying alone.',
        },
        {
            icon: Users,
            title: 'Teachers',
            description: 'For educators who want students working in a space that supports revision, assignments, and guided practice.',
        },
        {
            icon: Sparkles,
            title: 'Families',
            description: 'For parents and guardians looking for a study tool that feels purposeful, supportive, and curriculum-aware.',
        },
    ];

    return (
        <div className={shellClassName}>
            <div className={`${overlayClassName} z-0`} />
            <div className={`absolute -left-24 top-40 z-10 h-72 w-72 rounded-full blur-3xl ${isLightPalette ? 'bg-[#13519C]/12' : 'bg-[#13519C]/25'}`} />
            <div className={`absolute right-0 top-24 z-20 h-96 w-96 rounded-full blur-3xl ${isLightPalette ? 'bg-[#FF9100]/8' : 'bg-[#FF9100]/10'}`} />

            <div className="fixed top-0 left-0 right-0 z-50 bg-[#13519C] border-b border-[#13519C]/20">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between items-center h-16">
                        <div className="flex items-center">
                            <FundileLogo className="h-48 w-48 text-white" />
                        </div>
                        <button 
                            onClick={onGetStarted}
                            className="bg-white text-[#13519C] px-6 py-2 rounded-lg hover:bg-gray-100 transition-all duration-300 font-medium"
                        >
                            Get Started
                        </button>
                    </div>
                </div>
            </div>

            <div className="relative z-30 px-4 pb-24 pt-20 sm:px-6 sm:pt-24 lg:px-8">
                <div className="mx-auto max-w-7xl">
                    <section className="grid gap-14 pb-10 pt-4 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:pb-16 lg:pt-8">
                        <div className="max-w-3xl">
                            <div className={`mb-6 inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-medium ${isLightPalette ? 'border border-[#2B7BD8]/20 bg-white/85 text-[#13519C] shadow-sm shadow-sky-100/50' : 'border border-[#2B7BD8]/40 bg-[#13519C]/20 text-blue-100'}`}>
                                <Sparkles className="h-4 w-4 text-[#FFD166]" />
                                Structured support for South African learners
                            </div>
                            <h1 className={`text-5xl font-bold tracking-tight sm:text-6xl xl:text-7xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Study with more structure, practice with more confidence.
                            </h1>
                            <p className={`mt-6 max-w-2xl text-lg leading-8 sm:text-xl ${bodyTextClassName}`}>
                                Fundile helps learners work through CAPS-aligned study support, guided feedback, and focused practice in one modern learning space.
                            </p>
                            <div className="mt-8 flex flex-col gap-4 sm:flex-row">
                                <button
                                    onClick={onGetStarted}
                                    className="inline-flex items-center justify-center gap-2 rounded-2xl bg-[#FF9100] px-6 py-4 text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.25)] transition hover:bg-[#f58200]"
                                >
                                    Start with Fundile
                                    <ArrowRight className="h-5 w-5" />
                                </button>
                                <button
                                    onClick={() => scrollToSection('why-fundile')}
                                    className={`inline-flex items-center justify-center rounded-2xl px-6 py-4 text-base font-semibold transition ${isLightPalette ? 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300 hover:bg-slate-50' : 'border border-white/15 text-white/90 hover:border-white/30 hover:bg-white/5'}`}
                                >
                                    Why Fundile?
                                </button>
                            </div>
                            <div className="mt-10 grid gap-4 sm:grid-cols-3">
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-white shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Designed around</p>
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>CAPS learning</p>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-white shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Built for</p>
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>Practice + guidance</p>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-white shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Focused on</p>
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>Clarity + momentum</p>
                                </div>
                            </div>
                        </div>

                        <div className="relative">
                            <div className={`absolute inset-0 rounded-[32px] bg-[radial-gradient(circle_at_center,_rgba(255,145,0,0.18),_transparent_60%)] blur-3xl ${isLightPalette ? 'opacity-70' : ''}`} />
                            <div className={`relative overflow-hidden rounded-[32px] border p-5 shadow-2xl ${isLightPalette ? 'border-sky-100 bg-white/90 shadow-sky-100/60' : 'border-white/10 bg-white/[0.08] backdrop-blur-xl'}`}>
                                <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-slate-50/90' : 'border-white/10 bg-slate-950/80'}`}>
                                    <div className={`flex items-center justify-between rounded-2xl border px-4 py-3 ${isLightPalette ? 'border-sky-100 bg-white' : 'border-white/10 bg-white/5'}`}>
                                        <div>
                                            <p className={`text-sm font-medium ${isLightPalette ? 'text-slate-500' : 'text-white/60'}`}>Inside Fundile</p>
                                            <p className={`text-lg font-semibold ${heroSectionTextClassName}`}>A single learning flow</p>
                                        </div>
                                        <div className={`rounded-full px-3 py-1 text-xs font-semibold uppercase tracking-[0.2em] ${isLightPalette ? 'bg-[#FF9100]/15 text-[#C76B00]' : 'bg-[#FF9100]/20 text-[#FFD166]'}`}>
                                            live support
                                        </div>
                                    </div>
                                    <div className="mt-5 space-y-4">
                                        <div className={`rounded-2xl p-4 ring-1 ring-inset ${isLightPalette ? 'bg-[#13519C]/8 ring-[#2B7BD8]/18' : 'bg-[#13519C]/18 ring-[#2B7BD8]/35'}`}>
                                            <div className="flex items-start gap-3">
                                                <Target className={`mt-1 h-5 w-5 ${isLightPalette ? 'text-[#13519C]' : 'text-blue-300'}`} />
                                                <div>
                                                    <p className={`font-semibold ${heroSectionTextClassName}`}>Choose a topic with intention</p>
                                                    <p className={`mt-1 text-sm ${bodyTextClassName}`}>Start from the exact subject area you need instead of searching aimlessly.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div className={`rounded-2xl p-4 ring-1 ring-inset ${isLightPalette ? 'bg-violet-500/6 ring-violet-400/18' : 'bg-violet-500/10 ring-violet-400/25'}`}>
                                            <div className="flex items-start gap-3">
                                                <BrainCircuit className={`mt-1 h-5 w-5 ${isLightPalette ? 'text-violet-600' : 'text-violet-300'}`} />
                                                <div>
                                                    <p className={`font-semibold ${heroSectionTextClassName}`}>Get guided help while you work</p>
                                                    <p className={`mt-1 text-sm ${bodyTextClassName}`}>Use tutoring support and structured prompts to keep moving.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div className={`rounded-2xl p-4 ring-1 ring-inset ${isLightPalette ? 'bg-amber-500/8 ring-amber-400/18' : 'bg-amber-500/10 ring-amber-300/25'}`}>
                                            <div className="flex items-start gap-3">
                                                <CheckCircle className={`mt-1 h-5 w-5 ${isLightPalette ? 'text-amber-600' : 'text-amber-300'}`} />
                                                <div>
                                                    <p className={`font-semibold ${heroSectionTextClassName}`}>Learn from feedback, not just answers</p>
                                                    <p className={`mt-1 text-sm ${bodyTextClassName}`}>Review your work, spot mistakes, and strengthen understanding over time.</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>

                    <section id="why-fundile" className="mt-8 grid gap-6 md:grid-cols-3">
                        {valueCards.map(({ icon: Icon, title, description, accent }) => (
                            <div key={title} className={surfaceClassName}>
                                <Icon className={`h-8 w-8 ${isLightPalette ? (accent === 'text-violet-300' ? 'text-violet-600' : accent === 'text-amber-300' ? 'text-amber-600' : 'text-[#13519C]') : accent}`} />
                                <h3 className={`mt-4 text-2xl font-semibold ${heroSectionTextClassName}`}>{title}</h3>
                                <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{description}</p>
                            </div>
                        ))}
                    </section>

                    <section id="features" className="mt-24">
                        <div className="max-w-3xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">What you can do</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                A long-scroll page should still answer one thing clearly: what can I actually do here?
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>
                                Fundile is built around practical learning workflows so learners can move from confusion to action more quickly.
                            </p>
                        </div>
                        <div className="mt-10 grid gap-5 md:grid-cols-2 xl:grid-cols-3">
                            {featureCards.map(({ icon: Icon, title, description }) => (
                                <div key={title} className={featureCardClassName}>
                                    <div className={`flex h-12 w-12 items-center justify-center rounded-2xl ring-1 ring-inset ${isLightPalette ? 'bg-slate-50 ring-slate-200' : 'bg-white/6 ring-white/10'}`}>
                                        <Icon className={`h-6 w-6 ${isLightPalette ? 'text-[#13519C]' : 'text-white'}`} />
                                    </div>
                                    <h3 className={`mt-5 text-xl font-semibold ${heroSectionTextClassName}`}>{title}</h3>
                                    <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{description}</p>
                                </div>
                            ))}
                        </div>
                    </section>

                    <section className="mt-24 grid gap-8 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
                        <div className={`rounded-[32px] border p-8 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/35' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">How it feels</p>
                            <h2 className={`mt-4 text-3xl font-bold sm:text-4xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Less noise. More direction.
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>
                                The goal is not to overwhelm learners with features. The goal is to help them know what to do next, why it matters, and how to improve.
                            </p>
                        </div>
                        <div className="grid gap-4 md:grid-cols-3">
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-[#13519C]/18'}`}>
                                <div className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-[#2B7BD8]' : 'text-blue-200'}`}>01</div>
                                <h3 className={`mt-4 text-xl font-semibold ${heroSectionTextClassName}`}>Find the right topic</h3>
                                <p className={`mt-3 ${bodyTextClassName}`}>Start from the subject and topic that matches your current need.</p>
                            </div>
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-violet-500/10'}`}>
                                <div className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-violet-600' : 'text-violet-200'}`}>02</div>
                                <h3 className={`mt-4 text-xl font-semibold ${heroSectionTextClassName}`}>Work with guidance</h3>
                                <p className={`mt-3 ${bodyTextClassName}`}>Use tutoring, prompts, and structured spaces to keep your thinking moving.</p>
                            </div>
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-amber-500/10'}`}>
                                <div className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-amber-600' : 'text-amber-200'}`}>03</div>
                                <h3 className={`mt-4 text-xl font-semibold ${heroSectionTextClassName}`}>Improve with feedback</h3>
                                <p className={`mt-3 ${bodyTextClassName}`}>Review answers and learn what to fix instead of stopping at the result.</p>
                            </div>
                        </div>
                    </section>

                    <section className="mt-24">
                        <div className="max-w-3xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">Who it is for</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Built for learners first, with space for teachers and families too.
                            </h2>
                        </div>
                        <div className="mt-10 grid gap-5 lg:grid-cols-3">
                            {audienceCards.map(({ icon: Icon, title, description }) => (
                                <div key={title} className={audienceCardClassName}>
                                    <Icon className={`h-8 w-8 ${isLightPalette ? 'text-[#13519C]' : 'text-[#FFD166]'}`} />
                                    <h3 className={`mt-5 text-2xl font-semibold ${heroSectionTextClassName}`}>{title}</h3>
                                    <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{description}</p>
                                </div>
                            ))}
                        </div>
                    </section>
                </div>
            </div>
        </div>
    );
};

export default LandingPage;
