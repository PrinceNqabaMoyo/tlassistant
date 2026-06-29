import React from 'react';
import FundileLogo from './FundileLogo';
import { ArrowRight, BookOpen, BrainCircuit, CheckCircle, GraduationCap, LayoutDashboard, PenTool, ShieldCheck, Sparkles, Target, Trophy, Users } from 'lucide-react';
import DemandCaptureForm from './DemandCaptureForm';
import CapsNscClarity from './landing/CapsNscClarity';
import LandingFaq from './landing/LandingFaq';
import NotAChatbot from './landing/NotAChatbot';
import FeatureClaims from './landing/FeatureClaims';
import heroLearners from '../../assets/landing/sa-learners-hero.jpg';
import { LIVE_AVAILABILITY_DETAIL, LIVE_AVAILABILITY_HEADLINE, LIVE_AVAILABILITY_NOTE } from '../../app/constants/availability';
import { HERO_COPY, HIDDEN_CURRICULUM, AUDIENCES, PRICING_COPY, PRINCIPLES } from '../../app/constants/landingCopy';

// Landing Page Component
const LandingPage = ({ db, onGetStarted, onSignIn, onViewSubscription, palette = 'dark' }) => {
    const [selectedResearchIndex, setSelectedResearchIndex] = React.useState(0);
    const [showProComingSoon, setShowProComingSoon] = React.useState(false);
    const currentYear = new Date().getFullYear();

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
            title: 'Curriculum-aligned support',
            description: 'Stay closer to what your subject and grade actually expect instead of jumping between random online resources.',
            accent: 'text-blue-300',
        },
        {
            icon: BrainCircuit,
            title: 'Teaching + learning support',
            description: 'Support classroom learning and independent study with guided practice, structured workflows, and clearer next steps.',
            accent: 'text-violet-300',
        },
        {
            icon: PenTool,
            title: 'Performance + mastery',
            description: 'Build stronger understanding through guided practice, repeated revision, and focused learning routines that improve results over time.',
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
            title: 'Socratic AI Tutors & Adaptive Progression',
            description: 'Specialised AI agents guide your learning. If you struggle, the system adapts and drops you to lower-level foundations to rebuild confidence.',
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

    const researchCards = [
        {
            id: 'paper-1',
            label: 'Accounting inquiry in South Africa',
            quote: `“Inquiry-based learning transforms the classroom into a space where curiosity drives discovery, and learners become active creators of knowledge rather than passive recipients.”`,
            summary: `Walusa and Qhosola-Mahlomaholo (2025) argue that inquiry-based learning fosters deeper engagement by encouraging learners to question, investigate, and construct their own understanding of accounting concepts. Their study demonstrates that this method not only enhances critical thinking and problem-solving but also nurtures independence and confidence in learners. By positioning students as active participants in knowledge creation, inquiry-based approaches prepare them for both academic success and real-world challenges.`,
            support: `This supports Fundile's inquiry-based design by showing why structured questioning, guided investigation, and active knowledge construction matter in accounting learning.`,
            reference: `Walusa, A., & Qhosola-Mahlomaholo, M. R. (2025). Enhancing critical thinking and problem-solving skills of grade 11 learners in accounting education in high school at uMgungundlovu district, South Africa.`
        },
        {
            id: 'paper-2',
            label: 'Problem-based learning and ethics',
            quote: `“Problem-based learning is perhaps the most innovative instructional method conceived in the history of education, and its most consistent finding is the superiority of PBL-trained learners in life-long learning.”`,
            summary: `Gerstein, Winter, and Hertz (2016) argue that problem-based learning is uniquely effective in teaching accounting ethics because it engages students in real-world dilemmas, fosters collaboration, and cultivates self-directed learning. They highlight that PBL equips learners with flexible thinking, critical reasoning, and intrinsic motivation — skills essential for ethical decision-making in professional practice.`,
            support: `This supports enquiry-based learning by showing that learners grow when they solve meaningful problems, reason through uncertainty, and build understanding through active exploration instead of memorising isolated facts.`,
            reference: `Gerstein, M., Winter, E., & Hertz, S. (2016). Teaching Accounting Ethics: A Problem-Based Learning Approach.`
        },
        {
            id: 'paper-3',
            label: 'Ownership and independent thinking',
            quote: `“Inquiry-based learning empowers students to take ownership of their education, transforming them into independent thinkers who can apply knowledge creatively to real-world challenges.”`,
            summary: `Hayat, Mahmood, and Akhter (2024) present inquiry-based learning as a transformative approach that cultivates independence, creativity, and critical thinking. By engaging learners in questioning, exploration, and problem-solving, the method shifts the classroom dynamic from passive absorption to active knowledge construction. Their findings emphasise that inquiry-based strategies prepare students for lifelong learning and adaptability.`,
            support: `This aligns with Fundile's goal of helping learners move from dependence on answers to confident, self-directed study supported by structured prompts and feedback.`,
            reference: `Hayat, Muhammad Usman, Azhar Mahmood, and Mirza Muhammad Akhter. Effect of Inquiry Based Learning on Academic Achievement of Students at Higher Secondary Level. (2024).`
        },
        {
            id: 'paper-4',
            label: 'Confidence, autonomy, and teamwork',
            quote: `“Students reported increased confidence, improved problem-solving skills, and greater engagement in the learning process… the inquiry-based methodology has helped me become a more confident and independent learner.”`,
            summary: `Martinez-Blasco, Markulin, and Bosch (2025) present a structured inquiry-based approach in accounting education through Study and Research Paths. Their findings across three implementations reveal that students engaged more deeply with accounting concepts and demonstrated enhanced teamwork, autonomy, and problem-solving abilities. Learners valued the real-world relevance of tasks, reported improved confidence, and appreciated the shift toward active, self-directed learning.`,
            support: `This supports enquiry-based learning by showing that carefully structured investigation can improve both academic performance and the learner confidence needed to keep progressing independently.`,
            reference: `Martinez-Blasco, M., Markulin, K., & Bosch, M. (2025). A proposal for inquiry-based learning in accounting using study and research paths.`
        },
        {
            id: 'paper-5',
            label: 'Student-question-based inquiry',
            quote: `“Student-question-based inquiry supports the learning of inquiry skills, improves discussion and reasoning, increases motivation, and strengthens confidence and ownership of learning.”`,
            summary: `Herranen and Aksela (2019) reviewed 30 studies on student-question-based inquiry and found that when students' own questions drive inquiry, learners demonstrate improved problem-solving, reasoning, and discussion skills. The approach also enhances motivation, engagement, and confidence, while fostering a sense of ownership over learning. The authors emphasise that teacher scaffolding remains important, but conclude that student-question-based inquiry is a powerful model for performance and lifelong learning.`,
            support: `This supports Fundile's guided-enquiry model: learners should be encouraged to ask, test, and refine questions, while the platform provides the scaffolding that keeps the enquiry productive.`,
            reference: `Herranen, J., & Aksela, M. (2019). Student-question-based inquiry in science education.`
        },
        {
            id: 'paper-6',
            label: 'Achievement, motivation, transfer',
            quote: `“Learners engaged in inquiry-based approaches demonstrated higher achievement, stronger motivation, and improved capacity to apply knowledge in new contexts.”`,
            summary: `Suhandi and colleagues (2018) argue that inquiry-based learning significantly enhances student outcomes by fostering deeper engagement, critical thinking, and transferable problem-solving skills. Their findings show that students not only achieve higher academic performance but also develop stronger motivation and confidence. By encouraging learners to actively question, investigate, and construct knowledge, inquiry-based methods prepare them for lifelong learning and adaptability.`,
            support: `This reinforces the case for an app like Fundile: enquiry-based support should not only help with today's task, but also improve motivation and transfer of understanding into new academic contexts.`,
            reference: `Suhandi, A., et al. (2018). Effectiveness of the use of question-driven levels of inquiry based instruction assisted visual multimedia supported teaching material on enhancing scientific explanation ability.`
        }
    ];

    const activeResearchCard = researchCards[selectedResearchIndex] || researchCards[0];
    const researchCardCount = researchCards.length;

    React.useEffect(() => {
        const timerId = window.setTimeout(() => {
            setSelectedResearchIndex((currentIndex) => (currentIndex + 1) % researchCardCount);
        }, 7000);

        return () => {
            window.clearTimeout(timerId);
        };
    }, [researchCardCount, selectedResearchIndex]);

    return (
        <div className={shellClassName}>
            <div className={`${overlayClassName} z-0`} />
            <div className={`absolute -left-24 top-40 z-10 h-72 w-72 rounded-full blur-3xl ${isLightPalette ? 'bg-[#13519C]/12' : 'bg-[#13519C]/25'}`} />
            <div className={`absolute right-0 top-24 z-20 h-96 w-96 rounded-full blur-3xl ${isLightPalette ? 'bg-[#FF9100]/8' : 'bg-[#FF9100]/10'}`} />

            <div className="fixed top-0 left-0 right-0 z-50 bg-[#13519C] border-b border-[#13519C]/20">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between items-center h-16">
                        <div className="flex items-center shrink-0">
                            <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48 text-white" />
                        </div>
                        <div className="flex items-center gap-3">
                            <button
                                type="button"
                                onClick={onSignIn}
                                className="rounded-lg border border-white/20 bg-white/10 px-3 py-1.5 text-sm sm:px-5 sm:py-2 sm:text-base font-medium text-white transition-all duration-300 hover:bg-white/20"
                            >
                                Sign in
                            </button>
                            <button 
                                onClick={onGetStarted}
                                className="bg-white text-[#13519C] px-3 py-1.5 text-sm sm:px-6 sm:py-2 sm:text-base rounded-lg hover:bg-gray-100 transition-all duration-300 font-medium"
                            >
                                Get Started
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <div className="relative z-30 px-4 pb-24 pt-20 sm:px-6 sm:pt-24 lg:px-8">
                <div className="mx-auto max-w-7xl">
                    <section className="grid gap-14 pb-10 pt-4 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:pb-16 lg:pt-8">
                        <div className="max-w-3xl">
                            <div className={`mb-6 inline-flex items-center gap-2 rounded-full px-4 py-2 text-sm font-medium ${isLightPalette ? 'border border-[#2B7BD8]/20 bg-white/85 text-[#13519C] shadow-sm shadow-sky-100/50' : 'border border-[#2B7BD8]/40 bg-[#13519C]/20 text-blue-100'}`}>
                                <Sparkles className="h-4 w-4 text-[#FFD166]" />
                                {HERO_COPY.eyebrow}
                            </div>
                            <div className="mb-6 flex flex-wrap gap-3">
                                <button
                                    type="button"
                                    onClick={() => scrollToSection('pricing')}
                                    className={`inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition ${isLightPalette ? 'border border-sky-200 bg-white text-[#13519C] hover:border-sky-300 hover:bg-sky-50' : 'border border-white/15 bg-white/5 text-white hover:border-white/30 hover:bg-white/10'}`}
                                >
                                    Pricing
                                </button>
                                <button
                                    type="button"
                                    onClick={() => scrollToSection('caps-nsc')}
                                    className={`inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition ${isLightPalette ? 'border border-sky-200 bg-white text-[#13519C] hover:border-sky-300 hover:bg-sky-50' : 'border border-white/15 bg-white/5 text-white hover:border-white/30 hover:bg-white/10'}`}
                                >
                                    CAPS &amp; NSC
                                </button>
                                <button
                                    type="button"
                                    onClick={() => scrollToSection('feature-claims')}
                                    className={`inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition ${isLightPalette ? 'border border-sky-200 bg-white text-[#13519C] hover:border-sky-300 hover:bg-sky-50' : 'border border-white/15 bg-white/5 text-white hover:border-white/30 hover:bg-white/10'}`}
                                >
                                    Demo video
                                </button>
                                <button
                                    type="button"
                                    onClick={() => scrollToSection('contact-footer')}
                                    className={`inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition ${isLightPalette ? 'border border-sky-200 bg-white text-[#13519C] hover:border-sky-300 hover:bg-sky-50' : 'border border-white/15 bg-white/5 text-white hover:border-white/30 hover:bg-white/10'}`}
                                >
                                    Contacts
                                </button>
                                <button
                                    type="button"
                                    onClick={() => scrollToSection('interest-form')}
                                    className={`inline-flex items-center justify-center rounded-full px-4 py-2 text-sm font-semibold transition ${isLightPalette ? 'border border-sky-200 bg-white text-[#13519C] hover:border-sky-300 hover:bg-sky-50' : 'border border-white/15 bg-white/5 text-white hover:border-white/30 hover:bg-white/10'}`}
                                >
                                    Request a subject
                                </button>
                            </div>
                            <h1 className={`text-5xl font-bold tracking-tight sm:text-6xl xl:text-7xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {HERO_COPY.title}
                            </h1>
                            <p className={`mt-6 max-w-2xl text-lg leading-8 sm:text-xl ${bodyTextClassName}`}>
                                {HERO_COPY.subtitle}
                            </p>
                            <div className={`mt-6 rounded-[28px] border px-5 py-4 ${isLightPalette ? 'border-sky-100 bg-white/95 shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FF9100]">Availability</p>
                                <p className={`mt-2 text-lg font-semibold ${heroSectionTextClassName}`}>{LIVE_AVAILABILITY_HEADLINE}</p>
                                <p className={`mt-2 text-sm leading-7 ${bodyTextClassName}`}>{LIVE_AVAILABILITY_NOTE}</p>
                                <p className={`mt-2 text-sm leading-7 ${mutedTextClassName}`}>{LIVE_AVAILABILITY_DETAIL}</p>
                            </div>
                            <div className="mt-8 flex flex-col gap-4 sm:flex-row">
                                <button
                                    onClick={onGetStarted}
                                    className="inline-flex items-center justify-center gap-2 rounded-2xl bg-[#FF9100] px-6 py-4 text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.25)] transition hover:bg-[#f58200]"
                                >
                                    Start with Fundile
                                    <ArrowRight className="h-5 w-5" />
                                </button>
                                <button
                                    type="button"
                                    onClick={onSignIn}
                                    className={`inline-flex items-center justify-center rounded-2xl px-6 py-4 text-base font-semibold transition ${isLightPalette ? 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300 hover:bg-slate-50' : 'border border-white/15 text-white/90 hover:border-white/30 hover:bg-white/5'}`}
                                >
                                    Returning user? Sign in
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
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>Curriculum alignment</p>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-white shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Built for</p>
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>Teaching + learning</p>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-white shadow-sm shadow-sky-100/40' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Focused on</p>
                                    <p className={`mt-2 text-xl font-semibold ${heroSectionTextClassName}`}>Performance + mastery</p>
                                </div>
                            </div>
                        </div>

                        <div className="relative">
                            <div className={`absolute inset-0 rounded-[32px] bg-[radial-gradient(circle_at_center,_rgba(255,145,0,0.18),_transparent_60%)] blur-3xl ${isLightPalette ? 'opacity-70' : ''}`} />
                            <div className={`relative overflow-hidden rounded-[32px] border shadow-2xl ${isLightPalette ? 'border-sky-100 bg-white/90 shadow-sky-100/60' : 'border-white/10 bg-white/[0.08] backdrop-blur-xl'}`}>
                                <img
                                    src={heroLearners}
                                    alt={HERO_COPY.imageAlt}
                                    loading="eager"
                                    className="h-full w-full object-cover"
                                />
                                <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-black/70 via-black/25 to-transparent px-6 py-5">
                                    <p className="text-sm font-medium text-white/90">{HERO_COPY.imageCaption}</p>
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

                    <section id="hidden-curriculum" className="mt-24">
                        <div className="max-w-3xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{HIDDEN_CURRICULUM.eyebrow}</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {HIDDEN_CURRICULUM.title}
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>{HIDDEN_CURRICULUM.body}</p>
                        </div>
                        <div className="mt-10 grid gap-5 md:grid-cols-3">
                            {HIDDEN_CURRICULUM.points.map((point) => (
                                <div key={point.title} className={surfaceClassName}>
                                    <h3 className={`text-xl font-semibold ${heroSectionTextClassName}`}>{point.title}</h3>
                                    <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{point.body}</p>
                                </div>
                            ))}
                        </div>
                    </section>

                    <section id="principles" className="mt-24">
                        <div className="max-w-3xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{PRINCIPLES.eyebrow}</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {PRINCIPLES.title}
                            </h2>
                        </div>
                        <div className="mt-10 grid gap-5 sm:grid-cols-2 xl:grid-cols-4">
                            {PRINCIPLES.items.map((item, index) => (
                                <div key={item.title} className={surfaceClassName}>
                                    <div className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-[#2B7BD8]' : 'text-blue-200'}`}>
                                        {String(index + 1).padStart(2, '0')}
                                    </div>
                                    <h3 className={`mt-4 text-xl font-semibold ${heroSectionTextClassName}`}>{item.title}</h3>
                                    <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{item.body}</p>
                                </div>
                            ))}
                        </div>
                    </section>

                    <NotAChatbot isLightPalette={isLightPalette} />

                    <section id="features" className="mt-24">
                        <div className="max-w-3xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">What you can do</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Everything you need to study with intention.
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

                    <CapsNscClarity isLightPalette={isLightPalette} />

                    <section id="pricing" className="mt-24 grid gap-8 lg:grid-cols-[0.92fr_1.08fr] lg:items-start">
                        <div className={`rounded-[32px] border p-8 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/35' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">Pricing</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {PRICING_COPY.title}
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>
                                {PRICING_COPY.anchor}
                            </p>
                            <div className={`mt-5 rounded-2xl border px-4 py-3 text-sm leading-7 ${isLightPalette ? 'border-sky-100 bg-slate-50 text-slate-600' : 'border-white/10 bg-slate-950/60 text-white/75'}`}>
                                {LIVE_AVAILABILITY_NOTE}
                            </div>
                            <div className="mt-8 flex flex-col gap-4 sm:flex-row">
                                <button
                                    type="button"
                                    onClick={() => onViewSubscription?.()}
                                    className="inline-flex items-center justify-center rounded-2xl bg-[#FF9100] px-6 py-4 text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.25)] transition hover:bg-[#f58200]"
                                >
                                    Get started with Standard
                                </button>
                                <a
                                    href="mailto:info@fundile.com"
                                    className={`inline-flex items-center justify-center rounded-2xl px-6 py-4 text-base font-semibold transition ${isLightPalette ? 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300 hover:bg-slate-50' : 'border border-white/15 text-white/90 hover:border-white/30 hover:bg-white/5'}`}
                                >
                                    Ask about school access
                                </a>
                            </div>
                            <p className={`mt-4 text-sm leading-7 ${mutedTextClassName}`}>
                                EFT payment is already supported inside Fundile through the existing Manage Subscription flow after sign-in.
                            </p>
                        </div>
                        <div className="grid gap-5 sm:grid-cols-3">
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-[#13519C]/5'}`}>
                                <p className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-slate-500' : 'text-slate-400'}`}>Free Tier</p>
                                <h3 className={`mt-4 text-2xl font-semibold ${heroSectionTextClassName}`}>R0 forever</h3>
                                <p className={`mt-3 leading-7 ${bodyTextClassName}`}>A safe learning environment for everyone. Get access to basic topic tracking, curriculum outlines, and select practice generators to test your knowledge.</p>
                                <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                    <span className={`rounded-full px-3 py-1 ${isLightPalette ? 'bg-slate-100 text-slate-700' : 'bg-slate-800 text-slate-300'}`}>Always Free</span>
                                </div>
                                <button
                                    type="button"
                                    onClick={onGetStarted}
                                    className={`mt-6 inline-flex w-full items-center justify-center rounded-2xl px-5 py-3 text-sm font-semibold transition ${isLightPalette ? 'bg-slate-100 text-slate-700 hover:bg-slate-200' : 'bg-white/10 text-white hover:bg-white/20'}`}
                                >
                                    Start Free
                                </button>
                            </div>
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-[#13519C]/18'}`}>
                                <p className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-[#2B7BD8]' : 'text-blue-200'}`}>Standard package</p>
                                <h3 className={`mt-4 text-2xl font-semibold ${heroSectionTextClassName}`}>R150 / mo</h3>
                                <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{PRICING_COPY.tiers.find((t) => t.key === 'standard').description}</p>
                                <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                    <span className={`rounded-full px-3 py-1 ${isLightPalette ? 'bg-[#13519C]/10 text-[#13519C]' : 'bg-[#2B7BD8]/20 text-blue-100'}`}>Live now</span>
                                    <span className={`rounded-full px-3 py-1 ${isLightPalette ? 'bg-emerald-100 text-emerald-700' : 'bg-emerald-500/15 text-emerald-200'}`}>Save R200 yearly</span>
                                </div>
                                <button
                                    type="button"
                                    onClick={() => onViewSubscription?.()}
                                    className="mt-6 inline-flex w-full items-center justify-center rounded-2xl bg-[#13519C] px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#0f3e77]"
                                >
                                    Start Standard
                                </button>
                            </div>
                            <div className={`rounded-[28px] border p-6 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-violet-500/10'}`}>
                                <p className={`text-sm font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-violet-600' : 'text-violet-200'}`}>Pro package</p>
                                <h3 className={`mt-4 text-2xl font-semibold ${heroSectionTextClassName}`}>R299 / mo</h3>
                                <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{PRICING_COPY.tiers.find((t) => t.key === 'pro').description}</p>
                                <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                    <span className={`rounded-full px-3 py-1 ${isLightPalette ? 'bg-violet-100 text-violet-700' : 'bg-violet-500/20 text-violet-100'}`}>Coming soon</span>
                                    <span className={`rounded-full px-3 py-1 ${isLightPalette ? 'bg-amber-100 text-amber-700' : 'bg-amber-500/15 text-amber-200'}`}>Save R488 yearly</span>
                                </div>
                                <button
                                    type="button"
                                    onClick={() => setShowProComingSoon(true)}
                                    className={`mt-6 inline-flex w-full items-center justify-center rounded-2xl px-5 py-3 text-sm font-semibold transition ${isLightPalette ? 'bg-violet-600 text-white hover:bg-violet-700' : 'bg-violet-500/85 text-white hover:bg-violet-500'}`}
                                >
                                    Explore Pro
                                </button>
                            </div>
                        </div>
                    </section>

                    <FeatureClaims isLightPalette={isLightPalette} />

                    <section id="research-evidence" className="mt-24">
                        <div className="max-w-4xl">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">Research-backed learning</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Why enquiry-based learning matters for a platform like Fundile.
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>
                                These studies highlight why guided enquiry, student questioning, problem-solving, and reflective feedback can improve confidence, motivation, and real understanding. Select a quote card to read the wider finding.
                            </p>
                        </div>

                        <div className="mt-10 grid gap-5 lg:grid-cols-[0.95fr_1.05fr] lg:items-start">
                            <div className="grid gap-4 sm:grid-cols-2">
                                {researchCards.map((card, index) => {
                                    const isActive = selectedResearchIndex === index;

                                    return (
                                        <button
                                            key={card.id}
                                            type="button"
                                            onClick={() => setSelectedResearchIndex(index)}
                                            className={`text-left rounded-[28px] border p-5 transition duration-300 ${isActive
                                                ? (isLightPalette
                                                    ? 'border-[#2B7BD8]/40 bg-white shadow-xl shadow-sky-100/60'
                                                    : 'border-[#2B7BD8]/45 bg-[#13519C]/18 shadow-lg shadow-[#13519C]/20')
                                                : (isLightPalette
                                                    ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30 hover:border-[#2B7BD8]/25'
                                                    : 'border-white/10 bg-white/5 hover:border-white/20 hover:bg-white/[0.08]')}`}
                                        >
                                            <div className="flex items-start justify-between gap-3">
                                                <div>
                                                    <p className={`text-xs font-semibold uppercase tracking-[0.25em] ${isLightPalette ? 'text-[#2B7BD8]' : 'text-blue-200'}`}>Paper {index + 1}</p>
                                                    <h3 className={`mt-3 text-lg font-semibold ${heroSectionTextClassName}`}>{card.label}</h3>
                                                </div>
                                                <span className={`rounded-full px-3 py-1 text-xs font-semibold ${isActive
                                                    ? (isLightPalette ? 'bg-[#13519C]/10 text-[#13519C]' : 'bg-[#2B7BD8]/20 text-blue-100')
                                                    : (isLightPalette ? 'bg-slate-100 text-slate-600' : 'bg-white/10 text-white/70')}`}
                                                >
                                                    {isActive ? 'Selected' : 'Open'}
                                                </span>
                                            </div>
                                            <p className={`mt-4 text-sm leading-7 ${bodyTextClassName}`}>{card.quote}</p>
                                        </button>
                                    );
                                })}
                            </div>

                            <div className="rounded-[32px] border border-sky-100 bg-white p-8 shadow-[0_24px_70px_rgba(148,163,184,0.2)]">
                                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#2B7BD8]">Selected insight</p>
                                <h3 className="mt-4 text-2xl font-semibold text-slate-950 sm:text-3xl">{activeResearchCard.label}</h3>
                                <p className="mt-5 text-lg leading-8 text-slate-900">{activeResearchCard.quote}</p>
                                <div className="mt-6 space-y-5">
                                    <div>
                                        <p className="text-sm font-semibold uppercase tracking-[0.22em] text-slate-500">What the paper says</p>
                                        <p className="mt-3 leading-8 text-slate-600">{activeResearchCard.summary}</p>
                                    </div>
                                    <div>
                                        <p className="text-sm font-semibold uppercase tracking-[0.22em] text-slate-500">Why it supports enquiry-based learning</p>
                                        <p className="mt-3 leading-8 text-slate-600">{activeResearchCard.support}</p>
                                    </div>
                                    <div className="rounded-2xl border border-slate-200 bg-slate-50 p-4">
                                        <p className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">Reference</p>
                                        <p className="mt-3 text-sm leading-7 text-slate-600">{activeResearchCard.reference}</p>
                                    </div>
                                </div>
                            </div>
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
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">{AUDIENCES.eyebrow}</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {AUDIENCES.title}
                            </h2>
                        </div>
                        <div className="mt-10 grid gap-5 lg:grid-cols-3">
                            {AUDIENCES.cards.map((card, index) => {
                                const Icon = audienceCards[index]?.icon || GraduationCap;
                                const isComingSoon = card.badge === 'Coming soon';
                                return (
                                    <div key={card.key} className={audienceCardClassName}>
                                        <div className="flex items-center justify-between">
                                            <Icon className={`h-8 w-8 ${isLightPalette ? 'text-[#13519C]' : 'text-[#FFD166]'}`} />
                                            <span className={`rounded-full px-3 py-1 text-xs font-semibold ${isComingSoon
                                                ? (isLightPalette ? 'bg-violet-100 text-violet-700' : 'bg-violet-500/20 text-violet-100')
                                                : (isLightPalette ? 'bg-emerald-100 text-emerald-700' : 'bg-emerald-500/15 text-emerald-200')}`}
                                            >
                                                {card.badge}
                                            </span>
                                        </div>
                                        <h3 className={`mt-5 text-2xl font-semibold ${heroSectionTextClassName}`}>{card.title}</h3>
                                        <p className={`mt-3 leading-7 ${bodyTextClassName}`}>{card.body}</p>
                                    </div>
                                );
                            })}
                        </div>
                    </section>
                    <LandingFaq isLightPalette={isLightPalette} />

                    <section id="interest-form" className="mt-24 grid gap-8 lg:grid-cols-[0.9fr_1.1fr] lg:items-start">
                        <div className={`rounded-[32px] border p-8 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/35' : 'border-white/10 bg-white/5 backdrop-blur-sm'}`}>
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">Help shape rollout</p>
                            <h2 className={`mt-4 text-4xl font-bold tracking-tight sm:text-5xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Need another grade or subject?
                            </h2>
                            <p className={`mt-5 text-lg leading-8 ${bodyTextClassName}`}>
                                {LIVE_AVAILABILITY_NOTE}
                            </p>
                            <p className={`mt-4 text-sm leading-7 ${mutedTextClassName}`}>
                                {LIVE_AVAILABILITY_DETAIL}
                            </p>
                            <div className="mt-8 grid gap-4 sm:grid-cols-2">
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-slate-50' : 'border-white/10 bg-slate-950/60'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Live now</p>
                                    <p className={`mt-2 text-lg font-semibold ${heroSectionTextClassName}`}>Grade 10 Accounting</p>
                                    <p className={`mt-1 text-sm ${bodyTextClassName}`}>Available today inside the current MVP rollout.</p>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-slate-50' : 'border-white/10 bg-slate-950/60'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Also live</p>
                                    <p className={`mt-2 text-lg font-semibold ${heroSectionTextClassName}`}>Grade 11 Accounting</p>
                                    <p className={`mt-1 text-sm ${bodyTextClassName}`}>More grades and subjects will follow once demand and readiness line up.</p>
                                </div>
                            </div>
                        </div>
                        <DemandCaptureForm
                            db={db}
                            source="landing_page"
                            title="Tell Fundile what you want next"
                            description="Share the next subject, grade, or rollout request you want Fundile to prioritise."
                            submitLabel="Send request"
                        />
                    </section>
                    <footer id="contact-footer" className={`mt-24 rounded-[32px] border px-6 py-10 sm:px-8 ${isLightPalette ? 'border-sky-100 bg-white shadow-lg shadow-sky-100/30' : 'border-white/10 bg-slate-950/70 backdrop-blur-sm'}`}>
                        <div className="grid gap-8 lg:grid-cols-[1.1fr_0.9fr] lg:items-end">
                            <div>
                                <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#FFD166]">Contact + privacy</p>
                                <h2 className={`mt-4 text-3xl font-bold tracking-tight sm:text-4xl ${heroSectionTextClassName}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Stay in touch with Fundile.
                                </h2>
                                <p className={`mt-5 max-w-2xl text-lg leading-8 ${bodyTextClassName}`}>
                                    For pricing, support, school enquiries, or general questions, contact us directly. You can also read our privacy statement for more information about how Fundile approaches personal information and POPIA-aligned privacy responsibilities.
                                </p>
                            </div>
                            <div className="grid gap-4 sm:grid-cols-2">
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-slate-50' : 'border-white/10 bg-white/5'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Email</p>
                                    <a href="mailto:info@fundile.com" className="mt-2 block text-lg font-semibold text-[#FF9100] hover:underline">info@fundile.com</a>
                                </div>
                                <div className={`rounded-2xl border p-4 ${isLightPalette ? 'border-sky-100 bg-slate-50' : 'border-white/10 bg-white/5'}`}>
                                    <p className={`text-sm font-medium ${mutedTextClassName}`}>Privacy</p>
                                    <a href="/privacy-statement.html" className="mt-2 block text-lg font-semibold text-[#FF9100] hover:underline">Read our privacy statement</a>
                                </div>
                            </div>
                        </div>
                        <div className={`mt-8 flex flex-col gap-3 border-t pt-6 text-sm sm:flex-row sm:items-center sm:justify-between ${isLightPalette ? 'border-sky-100 text-slate-500' : 'border-white/10 text-white/60'}`}>
                            <p>© {currentYear} Fundile. All rights reserved.</p>
                            <div className="flex flex-wrap gap-4">
                                <a href="mailto:info@fundile.com" className="hover:text-[#FF9100]">info@fundile.com</a>
                                <a href="/privacy-statement.html" className="hover:text-[#FF9100]">Privacy statement</a>
                            </div>
                        </div>
                    </footer>
                    {showProComingSoon && (
                        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/70 p-4 backdrop-blur-sm">
                            <div className={`w-full max-w-md rounded-[28px] border p-6 shadow-2xl ${isLightPalette ? 'border-sky-100 bg-white' : 'border-white/10 bg-slate-950'}`}>
                                <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FFD166]">Pro package</p>
                                <h3 className={`mt-4 text-2xl font-semibold ${heroSectionTextClassName}`}>Coming soon</h3>
                                <p className={`mt-3 leading-7 ${bodyTextClassName}`}>
                                    Coming soon, not yet available in South Africa.
                                </p>
                                <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:justify-end">
                                    <a
                                        href="mailto:info@fundile.com?subject=Fundile%20Pro%20interest"
                                        className="inline-flex items-center justify-center rounded-2xl bg-[#FF9100] px-5 py-3 text-sm font-semibold text-white transition hover:bg-[#f58200]"
                                    >
                                        Register interest
                                    </a>
                                    <button
                                        type="button"
                                        onClick={() => setShowProComingSoon(false)}
                                        className={`inline-flex items-center justify-center rounded-2xl px-5 py-3 text-sm font-semibold transition ${isLightPalette ? 'border border-slate-200 bg-white text-slate-700 hover:border-slate-300 hover:bg-slate-50' : 'border border-white/15 text-white/90 hover:border-white/30 hover:bg-white/5'}`}
                                    >
                                        Close
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default LandingPage;
