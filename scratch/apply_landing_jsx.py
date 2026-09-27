import re

# Read current LandingPage.jsx
with open('src/components/ui/LandingPage.jsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update imports
new_imports = '''import React, { useState, useEffect, useRef, useCallback } from 'react';
import FundileLogo from './FundileLogo';
import {
    ArrowRight,
    Sparkles,
    MessageCircleWarning,
    ChevronDown,
    CheckCircle2,
    GraduationCap,
    Users,
    BookOpen,
    Building2,
    Mail,
    Activity,
    Wrench,
    CheckSquare,
    Radar,
    ShieldCheck,
    Landmark,
    Home,
    Star,
    Check,
} from 'lucide-react';
import DemandCaptureForm from './DemandCaptureForm';
import ScrollReveal from './landing/ScrollReveal';'''

# Replace old import block
old_import_pattern = re.compile(
    r"import React, { useState, useEffect, useRef, useCallback } from 'react';.*?import ScrollReveal from './landing/ScrollReveal';",
    re.DOTALL
)
if old_import_pattern.search(content):
    content = old_import_pattern.sub(new_imports, content)
    print("Updated imports successfully.")
else:
    print("WARNING: Old imports pattern not found!")

# 2. Update handlers: scrollToSimulator and handlePerspectiveChange
old_handlers = '''    const scrollToSimulator = () => {
        simulatorRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    const handlePerspectiveChange = (perspective) => {
        setActivePerspective(perspective);
        setTimeout(() => {
            simulatorRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }, 50);
    };

    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    };'''

new_handlers = '''    const PERSPECTIVE_LABELS = {
        learners: 'Learner Experience • Step-by-Step Scaffolding',
        parents: 'Parent Overview • Transparent Weekly Progress',
        teachers: 'Teacher Workflow • Instant Exam Authoring',
        schools: 'School Administration • SASAMS & ATP Pacing',
    };

    const scrollToSimulator = () => {
        const el = document.getElementById('features');
        if (el) {
            const yOffset = -110;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };

    const handlePerspectiveChange = (perspective) => {
        setActivePerspective(perspective);
        const sectionMap = {
            learners: 'problem-promise',
            parents: 'not-a-chatbot',
            teachers: 'structured-system',
            schools: 'pricing',
        };
        const targetId = sectionMap[perspective] || 'features';
        const el = document.getElementById(targetId);
        if (el) {
            const yOffset = -110;
            const y = el.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };

    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            const yOffset = -110;
            const y = section.getBoundingClientRect().top + window.pageYOffset + yOffset;
            window.scrollTo({ top: y, behavior: 'smooth' });
        }
    };'''

if old_handlers in content:
    content = content.replace(old_handlers, new_handlers)
    print("Updated handlers successfully.")
else:
    print("WARNING: Old handlers not found!")

# 3. Update right helper info in secondary ribbon
old_ribbon_right = '''                        {/* Right Helper Info */}
                        <div className="shrink-0 hidden lg:flex items-center gap-2">
                            <span className="text-[11px] font-medium text-slate-500">
                                {activePerspective === 'learners' ? 'Learner experience' : `${activePerspective.charAt(0).toUpperCase() + activePerspective.slice(1)} perspective`}
                            </span>
                        </div>'''

new_ribbon_right = '''                        {/* Right Helper Info */}
                        <div className="shrink-0 hidden lg:flex items-center gap-2">
                            <span className="text-[11px] font-semibold text-slate-500 bg-slate-100 px-3 py-1 rounded-full border border-slate-200 flex items-center gap-1.5">
                                <span className="w-2 h-2 rounded-full bg-[#FF9100]" />
                                <span>{PERSPECTIVE_LABELS[activePerspective] || 'Learner Experience'}</span>
                            </span>
                        </div>'''

if old_ribbon_right in content:
    content = content.replace(old_ribbon_right, new_ribbon_right)
    print("Updated ribbon right pill successfully.")
else:
    print("WARNING: Old ribbon right not found!")

# 4. Replace the lower content canvas (from PerspectiveShowcase to the end of the lower canvas)
old_canvas_start = '{/* Perspective Showcase / Multi-Audience Simulators'
# Find the start of the lower canvas content
idx_start = content.find(old_canvas_start)
if idx_start == -1:
    print("ERROR: old_canvas_start not found!")

# Find where the lower canvas ends: before </div>\n            </div>\n        </div>\n    );\n};\n\nexport default LandingPage;
idx_end = content.rfind('                </div>\n            </div>\n        </div>\n    );\n};')
if idx_end == -1:
    idx_end = content.rfind('</div>\n            </div>\n        </div>\n    );\n};')

print(f"Canvas start idx: {idx_start}, end idx: {idx_end}")

new_lower_canvas = '''{/* 1. CORE COGNITIVE PILLARS */}
                    <section id="features" className="scroll-mt-32 pt-2 pb-16">
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                            {/* Pillar 1: Smart Diagnostic Autopsy */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-orange-50 text-[#FF9100] flex items-center justify-center shrink-0 border border-orange-100">
                                        <Activity className="w-4 h-4" />
                                    </div>
                                    <span>Smart Diagnostic Autopsy</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    Automatically pinpoints the exact calculation step where marks were lost, just like a master teacher spotting an error pattern on a graded test paper.
                                </p>
                            </div>

                            {/* Pillar 2: 5-Minute Focus Fixes */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center shrink-0 border border-emerald-100">
                                        <Wrench className="w-4 h-4" />
                                    </div>
                                    <span>5-Minute Focus Fixes</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    Quick 3-question targeted practice sessions isolated purely to the single prerequisite step you stumbled on (such as calculating 15% VAT) before resuming full problems.
                                </p>
                            </div>

                            {/* Pillar 3: Fair Step Marking */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center shrink-0 border border-purple-100">
                                        <CheckSquare className="w-4 h-4" />
                                    </div>
                                    <span>Fair Step Marking</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    You receive full method marks [M] for applying correct formulas and logic on subsequent steps, even if an early arithmetic calculation had a minor slip.
                                </p>
                            </div>

                            {/* Pillar 4: Skill Radar Calibration */}
                            <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 shadow-xs hover:shadow-md transition duration-300">
                                <div className="flex items-center gap-2.5 text-[#13519C] font-bold text-xs uppercase tracking-wider mb-2.5">
                                    <div className="w-8 h-8 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center shrink-0 border border-blue-100">
                                        <Radar className="w-4 h-4" />
                                    </div>
                                    <span>Skill Radar Calibration</span>
                                </div>
                                <p className="text-xs leading-relaxed text-slate-600">
                                    A thought-paced 2 to 4 check radar that skips drills you've already mastered and jumps straight to your optimal challenge tier without anxiety-inducing timers.
                                </p>
                            </div>
                        </div>
                    </section>

                    {/* 2. THE PROBLEM → THE PROMISE */}
                    <ScrollReveal delay={0.1}>
                        <section id="problem-promise" className="mt-8 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    The Hidden Curriculum
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Most learners are surprised by the exam. They should not be.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Day-to-day classwork rarely looks like the final exam, so the real "rules of the game" stay hidden until it is too late. Fundile closes that gap: every topic is practised at exam standard, with transparent feedback on exactly where you went wrong — no surprises in November.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Exam-standard from day one
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Practice questions are pitched at authentic exam level from the first topic, not only at revision time.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        See where you went wrong
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Step-by-step marking shows the exact line your method broke down — and still credits the work that was correct with fair method marks.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Unlimited practice
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Deterministic generators produce endless fresh variants of any question, so you practise until it is automatic.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 3. A STRUCTURED, ADAPTIVE LEARNING SYSTEM */}
                    <ScrollReveal delay={0.1}>
                        <section id="structured-system" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    How It Works
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    A structured, adaptive learning system.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    From diagnosing prerequisites to mastering final exam papers, our deterministic progression guides learners without calculation errors or generic chatbot guessing.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 01
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Pick a Topic or Take a Diagnostic
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Choose the exact subject, grade, and topic you need, or begin with a diagnostic autopsy that pinpoints your baseline against the national curriculum standard.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 02
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Scaffold → Practice → Assessment
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Progress through guided scaffolding, move to independent practice, and unlock exam-standard assessments with pre-baked 3-tier hints.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="text-xs font-bold uppercase tracking-[0.2em] text-[#13519C] mb-2">
                                        Step 03
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Precision Gap Autopsy & 5-Minute Focus Fixes
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        If your working stumbles, Fundile isolates the exact flawed step, awards consequential method marks, and deploys targeted 5-minute focus fixes and SimuLearn visual animations.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 4. ACTIVE COGNITIVE LEARNING VS. PASSIVE CHATBOTS */}
                    <ScrollReveal delay={0.1}>
                        <section id="not-a-chatbot" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Active Cognitive Learning vs. Passive Chatbots
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Fundile is not an AI chatbot.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Generic chatbots answer questions for you, encouraging passive copy-pasting and hallucinating non-existent formulas. Fundile asks you the question, enforces authentic exam-standard method working, and intervenes with precision when your logic breaks down.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-2">
                                {/* Chatbot Column */}
                                <div className="rounded-[28px] border border-rose-200/90 bg-rose-50/40 p-6 sm:p-8 shadow-xs">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-rose-100 text-rose-700">
                                            <MessageCircleWarning className="h-5 w-5" />
                                        </div>
                                        <div>
                                            <h3 className="text-lg sm:text-xl font-bold text-rose-950">Generic AI Chatbots</h3>
                                            <span className="text-xs font-medium text-rose-700">Passive • Hallucination Risk • Zero Accountability</span>
                                        </div>
                                    </div>
                                    <ul className="space-y-3.5 text-sm text-rose-900/80">
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Gives the answer away:</strong> Solves homework for the learner without building neural pathways or cognitive automaticity.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Prone to hallucinations:</strong> Invents numbers, mixes up financial accounting rules, and calculates false arithmetic answers with total confidence.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-rose-500 font-bold shrink-0">✕</span>
                                            <span><strong>Zero curriculum discipline:</strong> Unaware of South African national curriculum term weightings, official formula sheets, or method marking rubrics.</span>
                                        </li>
                                    </ul>
                                </div>

                                {/* Fundile Column */}
                                <div className="rounded-[28px] border-2 border-[#13519C] bg-white p-6 sm:p-8 shadow-md shadow-blue-900/10">
                                    <div className="flex items-center gap-3 mb-4">
                                        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-50 text-[#13519C]">
                                            <Sparkles className="h-5 w-5 text-[#FF9100]" />
                                        </div>
                                        <div>
                                            <h3 className="text-lg sm:text-xl font-bold text-slate-900">Fundile Cognitive Engine</h3>
                                            <span className="text-xs font-bold text-[#13519C]">Active • 100% Deterministic • National Standard</span>
                                        </div>
                                    </div>
                                    <ul className="space-y-3.5 text-sm text-slate-700">
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Stepwise procedure tracking:</strong> Awards authentic method marks, carry-over accuracy, and isolates the single line an error occurred.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Zero-LLM mathematical ground truth:</strong> Seeded SymPy symbolic math and accounting ledger graph engines guarantee 100% internal consistency.</span>
                                        </li>
                                        <li className="flex items-start gap-2.5">
                                            <span className="text-emerald-600 font-bold shrink-0">✓</span>
                                            <span><strong>Diagnostic error autopsies:</strong> Tags specific misconceptions (e.g. net vs gross VAT formula) and deploys 5-minute targeted focus fixes.</span>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 5. UNIVERSAL NATIONAL CURRICULUM STANDARDS */}
                    <ScrollReveal delay={0.1}>
                        <section id="curriculum-alignment" className="mt-24 scroll-mt-32">
                            <div className="max-w-3xl mb-10">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Curriculum Standards & Exam Alignment
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    The difference is not the curriculum — it is the preparation.
                                </h2>
                                <div className="mt-4 p-4 rounded-2xl bg-blue-50 border border-blue-200/80 text-sm sm:text-base text-slate-700 leading-relaxed">
                                    <strong className="text-[#13519C] block mb-1">Did you know?</strong>
                                    There is only one official national curriculum standard in South Africa, which underpins public, private, and independent school examinations nationwide.
                                </div>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Many families believe private or independent schools follow a completely different curriculum. In reality, the South African National Curriculum forms the statutory foundation for all schools—the difference lies in preparation and assessment depth. Fundile prepares learners to excel at the highest level of examination standards across all examining bodies.
                                </p>
                            </div>

                            <div className="grid gap-6 md:grid-cols-3">
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-blue-50 text-[#13519C] flex items-center justify-center font-bold mb-4">
                                        <Landmark className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Public School Examinations
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Comprehensive coverage of official national curriculum statements with authentic past exam question archetypes and official time pacing.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-700 flex items-center justify-center font-bold mb-4">
                                        <ShieldCheck className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Independent & Private School Examinations
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Higher-order multi-step questions, unseen conceptual synthesis, and rigorous rubric definitions benchmarked for top academic standards.
                                    </p>
                                </div>

                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-6 sm:p-7 shadow-xs hover:shadow-md transition duration-300">
                                    <div className="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold mb-4">
                                        <Home className="w-5 h-5" />
                                    </div>
                                    <h3 className="text-lg sm:text-xl font-bold text-slate-900 mb-2">
                                        Distance & Home-Education Assessments
                                    </h3>
                                    <p className="text-sm leading-relaxed text-slate-600">
                                        Clear structured pacing with diagnostic radar checkpoints, assuring independent homeschoolers complete the national syllabus with certainty.
                                    </p>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 6. SIMPLE & TRANSPARENT PRICING */}
                    <ScrollReveal delay={0.1}>
                        <section id="pricing" className="mt-24 scroll-mt-32">
                            <div className="text-center max-w-3xl mx-auto mb-14">
                                <span className="text-xs font-bold uppercase tracking-[0.25em] text-[#13519C] bg-blue-50 border border-blue-200/60 px-3 py-1 rounded-full inline-block mb-3">
                                    Simple &amp; Transparent Pricing
                                </span>
                                <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight text-slate-900" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                    Accessible for Independent Learners. Scalable for Schools.
                                </h2>
                                <p className="mt-4 text-base sm:text-lg leading-relaxed text-slate-600">
                                    Private tutoring costs R150 to R350 per hour. Fundile gives you 24/7 unlimited exam practice, diagnostic autopsies, and step-by-step guidance for less than one tutoring session.
                                </p>
                            </div>

                            {/* Pricing Islands Grid (3 Distinct Audiences) */}
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto items-stretch">
                                {/* Island 1: Standard Individual Learner */}
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-7 shadow-xs flex flex-col justify-between hover:shadow-md transition duration-300">
                                    <div>
                                        <div className="flex justify-between items-center mb-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-[#13519C]">Individual Learner</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-50 text-[#13519C] border border-blue-200">Live Now</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Standard Pass</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Complete self-paced revision for Grades 7–12.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-4xl font-extrabold text-slate-900">R150</span>
                                            <span className="text-xs font-medium text-slate-500"> / learner / month</span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-600 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Full access to all 476+ national curriculum topics</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Unlimited deterministic question generator</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Step-by-step Fair Step Marking (consequential accuracy)</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-emerald-600 shrink-0" />
                                                <span>Offline PWA installation (1.4 MB total data)</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <button 
                                            type="button"
                                            onClick={onGetStarted}
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-[#13519C] bg-blue-50 hover:bg-blue-100 border border-blue-200 transition cursor-pointer"
                                        >
                                            Start Free Trial
                                        </button>
                                    </div>
                                </div>

                                {/* Island 2: Pro Cognitive Package (Featured) */}
                                <div className="rounded-[28px] border-2 border-[#13519C] bg-white p-7 shadow-lg shadow-blue-900/10 flex flex-col justify-between relative">
                                    <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full text-xs font-extrabold bg-[#13519C] text-white shadow-sm flex items-center gap-1">
                                        <Star className="w-3 h-3 text-[#FF9100] fill-[#FF9100]" />
                                        <span>RECOMMENDED • 2-WEEK FREE TRIAL</span>
                                    </div>

                                    <div>
                                        <div className="flex justify-between items-center mb-2 mt-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-purple-700">Pro Intelligence</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-purple-50 text-purple-700 border border-purple-200">Full Suite</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Pro Package</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Everything in Standard, plus our full Socratic cognitive tutor & SimuLearn.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-4xl font-extrabold text-slate-900">R299</span>
                                            <span className="text-xs font-medium text-slate-500"> / learner / month</span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-700 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span><strong>Everything in Standard</strong></span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Fundile Socratic™ Tutor with on-rails suggestion chips</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>SimuLearn visual animations (saves 95% data over video)</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Diagnostic error autopsies & 5-minute focus fixes</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-[#FF9100] shrink-0" />
                                                <span>Sunday WhatsApp Parent Coaching Pulse</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <button 
                                            type="button"
                                            onClick={onGetStarted}
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-white bg-[#FF9100] hover:bg-[#e68200] shadow-md transition cursor-pointer"
                                        >
                                            Start 2-Week Free Trial
                                        </button>
                                    </div>
                                </div>

                                {/* Island 3: Whole School SGB & Institutional */}
                                <div className="rounded-[28px] border border-slate-200/90 bg-white p-7 shadow-xs flex flex-col justify-between hover:shadow-md transition duration-300">
                                    <div>
                                        <div className="flex justify-between items-center mb-2">
                                            <span className="text-xs font-bold uppercase tracking-wider text-cyan-800">Schools &amp; Leadership</span>
                                            <span className="px-2.5 py-0.5 rounded-full text-xs font-bold bg-cyan-50 text-cyan-800 border border-cyan-200">Volume Tier</span>
                                        </div>
                                        <h3 className="text-2xl font-bold text-slate-900 mt-2">Institutional License</h3>
                                        <p className="text-xs text-slate-500 mt-1 mb-4">Complete infrastructure for classrooms, HODs, and school governing bodies.</p>
                                        
                                        <div className="mt-4">
                                            <span className="text-3xl font-extrabold text-slate-900">From R65</span>
                                            <span className="text-xs font-medium text-slate-500"> / learner / month</span>
                                        </div>

                                        <ul className="mt-6 space-y-3 text-xs text-slate-600 border-t border-slate-100 pt-6">
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-cyan-600 shrink-0" />
                                                <span>Teacher & HOD LMS Cockpits with real student photos</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-cyan-600 shrink-0" />
                                                <span>Unlimited 3-click printable A4 test papers & memos</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-cyan-600 shrink-0" />
                                                <span>1-Click official SASAMS Excel mark sheet export</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-cyan-600 shrink-0" />
                                                <span>Curriculum pacing variance radar (ATP vs reality)</span>
                                            </li>
                                            <li className="flex items-center gap-2">
                                                <Check className="w-4 h-4 text-cyan-600 shrink-0" />
                                                <span>SGB formal quotation & invoice procurement support</span>
                                            </li>
                                        </ul>
                                    </div>

                                    <div className="mt-8 pt-4">
                                        <a 
                                            href="mailto:info@fundile.com?subject=School%20Volume%20Pricing%20%26%20Institutional%20Inquiry" 
                                            className="w-full inline-flex items-center justify-center py-3.5 px-4 rounded-xl text-xs font-bold text-white bg-cyan-700 hover:bg-cyan-800 transition cursor-pointer"
                                        >
                                            Contact info@fundile.com
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </section>
                    </ScrollReveal>

                    {/* 7. DEMAND CAPTURE */}
                    <ScrollReveal delay={0.1}>
                        <section id="interest-form" className="mt-24">
                            <DemandCaptureForm isLightPalette={true} />
                        </section>
                    </ScrollReveal>

                    {/* 8. AUTHENTIC INSTITUTIONAL FOOTER & POPIA */}
                    <footer className="mt-24 border-t border-slate-200 pt-12 pb-8">
                        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 mb-10">
                            {/* Brand & Mission Column */}
                            <div className="md:col-span-2 space-y-4">
                                <div className="flex items-center gap-3">
                                    <FundileLogo className="h-28 w-28 sm:h-36 sm:w-36 text-[#13519C]" />
                                </div>
                                <p className="text-xs text-slate-500 leading-relaxed max-w-md">
                                    Fundile is South Africa’s deterministic curriculum engine and school management system. Grounded in the official National Curriculum Standards across Grades 7–12, we eliminate calculation hallucinations and empower learners, teachers, parents, and school leadership with measurable academic certainty.
                                </p>
                                <div className="flex items-center gap-3 pt-2">
                                    <span className="inline-flex items-center px-2.5 py-1 rounded-md bg-emerald-50 text-emerald-800 text-[11px] font-semibold border border-emerald-200">
                                        <ShieldCheck className="w-3.5 h-3.5 mr-1 text-emerald-600" /> POPIA Compliant (Sec 35)
                                    </span>
                                    <span className="inline-flex items-center px-2.5 py-1 rounded-md bg-blue-50 text-[#13519C] text-[11px] font-semibold border border-blue-200">
                                        <Check className="w-3.5 h-3.5 mr-1 text-[#FF9100]" /> 100% National Standard
                                    </span>
                                </div>
                            </div>

                            {/* Stakeholders & Quick Links */}
                            <div>
                                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-900 mb-3">Stakeholders</h4>
                                <ul className="space-y-2 text-xs text-slate-600">
                                    <li><button type="button" onClick={() => handlePerspectiveChange('learners')} className="hover:text-[#13519C] transition cursor-pointer">For High School Learners</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('parents')} className="hover:text-[#13519C] transition cursor-pointer">For Supportive Parents</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('teachers')} className="hover:text-[#13519C] transition cursor-pointer">For Classroom Teachers</button></li>
                                    <li><button type="button" onClick={() => handlePerspectiveChange('schools')} className="hover:text-[#13519C] transition cursor-pointer">For School Admins & HODs</button></li>
                                    <li><button type="button" onClick={() => scrollToSection('features')} className="hover:text-[#13519C] transition cursor-pointer">Core Features</button></li>
                                </ul>
                            </div>

                            {/* Contact & Legal Links */}
                            <div>
                                <h4 className="text-xs font-bold uppercase tracking-wider text-slate-900 mb-3">Institutional & Legal</h4>
                                <ul className="space-y-2 text-xs text-slate-600">
                                    <li>
                                        <a href="mailto:info@fundile.com" className="hover:text-[#13519C] transition flex items-center gap-1.5">
                                            <Mail className="w-3.5 h-3.5 text-slate-400" /> info@fundile.com
                                        </a>
                                    </li>
                                    <li>
                                        <a href="mailto:info@fundile.com?subject=School%20Pricing%20%26%20Institutional%20Inquiry" className="hover:text-[#13519C] transition flex items-center gap-1.5 font-semibold text-[#13519C]">
                                            <Building2 className="w-3.5 h-3.5" /> Institutional Inquiries
                                        </a>
                                    </li>
                                    <li>
                                        <a href="/privacy-statement.html" className="hover:text-[#13519C] transition flex items-center gap-1.5">
                                            <ShieldCheck className="w-3.5 h-3.5 text-slate-400" /> Privacy Policy (POPIA)
                                        </a>
                                    </li>
                                    <li>
                                        <button type="button" onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })} className="hover:text-[#13519C] transition cursor-pointer">Back to Top</button>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        {/* Bottom Bar */}
                        <div className="border-t border-slate-200 pt-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-slate-500 text-xs">
                            <div>
                                © {new Date().getFullYear()} Fundile. All rights reserved. 100% Aligned with South African National Curriculum Standards.
                            </div>
                            <div className="text-slate-400 text-[11px]">
                                Trusted preparation for public, private, and independent school examinations nationwide.
                            </div>
                        </div>
                    </footer>
'''

content = content[:idx_start] + new_lower_canvas + '\n' + content[idx_end:]

with open('src/components/ui/LandingPage.jsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated LandingPage.jsx successfully.")
