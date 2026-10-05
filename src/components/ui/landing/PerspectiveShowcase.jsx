import React from 'react';
import HeroSimulation from './HeroSimulation';
import ParentSimulation from './ParentSimulation';
import TeacherSimulation from './TeacherSimulation';
import SchoolSimulation from './SchoolSimulation';

const PerspectiveShowcase = ({
    activePerspective = 'learners',
    onSelectPerspective,
    onGetStarted,
    onSignIn,
    isLightPalette = true,
}) => {
    // ── 1. LEARNERS (Default Interactive Question & Solution Simulator) ──
    if (activePerspective === 'learners') {
        return (
            <div className="w-full">
                <div className="text-center mb-8">
                    <p className="text-xs font-semibold uppercase tracking-[0.3em] text-[#FF9100] mb-2 font-bold">
                        Live Interactive Simulator
                    </p>
                    <h2
                        className="text-3xl sm:text-4xl font-bold tracking-tight text-slate-900"
                        style={{ fontFamily: 'Afacad, sans-serif' }}
                    >
                        See How Learners Master Exam Questions
                    </h2>
                    <p className="mt-2 text-sm sm:text-base max-w-2xl mx-auto text-slate-600">
                        Experience how learners solve questions step-by-step with 3-tier pre-baked hints, consequential marking, and authentic exam-standard rubrics.
                    </p>
                </div>
                <div className="relative">
                    <HeroSimulation key="hero-simulation-active" isLightPalette={isLightPalette} />
                </div>
            </div>
        );
    }

    // ── 2. PARENTS (Interactive WhatsApp Report & Data Savings Simulator) ──
    if (activePerspective === 'parents') {
        return (
            <ParentSimulation
                isLightPalette={isLightPalette}
                onGetStarted={onGetStarted}
                onSelectPerspective={onSelectPerspective}
            />
        );
    }

    // ── 3. TEACHERS (3-Click Test Paper, Memo & Class Heatmap Simulator) ──
    if (activePerspective === 'teachers') {
        return (
            <TeacherSimulation
                isLightPalette={isLightPalette}
                onGetStarted={onGetStarted}
                onSelectPerspective={onSelectPerspective}
            />
        );
    }

    // ── 4. SCHOOL ADMINS (Departmental Pacing & SGB Procurement Simulator) ──
    if (activePerspective === 'schools') {
        return (
            <SchoolSimulation
                isLightPalette={isLightPalette}
                onGetStarted={onGetStarted}
                onSelectPerspective={onSelectPerspective}
            />
        );
    }

    return null;
};

export default PerspectiveShowcase;
