import React, { useMemo, useState } from 'react';
import { addDoc, collection, serverTimestamp } from 'firebase/firestore';
import { CheckCircle, Loader2, Send } from 'lucide-react';

import {
    DEMAND_CAPTURE_CURRICULUM_OPTIONS,
    DEMAND_CAPTURE_GRADE_OPTIONS,
    DEMAND_CAPTURE_SUBJECT_OPTIONS,
} from '../../app/constants/availability';

const INITIAL_FORM_STATE = {
    name: '',
    email: '',
    curriculum: DEMAND_CAPTURE_CURRICULUM_OPTIONS[0],
    requestedGrade: '',
    requestedSubject: '',
    schoolOrRole: '',
};

const isValidEmail = (value = '') => /\S+@\S+\.\S+/.test(value);

const DemandCaptureForm = ({
    db,
    source = 'public_surface',
    title,
    description,
    submitLabel = 'Register interest',
    isLightPalette = false,
}) => {
    const [formState, setFormState] = useState(INITIAL_FORM_STATE);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitError, setSubmitError] = useState('');
    const [submitSuccess, setSubmitSuccess] = useState('');

    const containerClass = isLightPalette
        ? 'rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/30 sm:p-8'
        : 'rounded-[28px] border border-white/10 bg-slate-900/90 p-6 shadow-2xl backdrop-blur-md sm:p-8';
    const titleClass = isLightPalette ? 'text-slate-950' : 'text-white';
    const bodyClass = isLightPalette ? 'text-slate-600' : 'text-slate-300';
    const labelClass = isLightPalette ? 'block text-sm font-medium text-slate-700' : 'block text-sm font-medium text-slate-300';
    const inputClass = isLightPalette
        ? 'mt-2 block w-full rounded-2xl border border-slate-200 bg-white px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15'
        : 'mt-2 block w-full rounded-2xl border border-slate-700/80 bg-slate-950/80 px-4 py-3 text-white placeholder-slate-500 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/30';
    const mutedClass = isLightPalette ? 'text-xs leading-6 text-slate-500' : 'text-xs leading-6 text-slate-400';

    const formTitle = useMemo(() => title || 'Tell Fundile what you need next', [title]);
    const formDescription = useMemo(
        () => description || 'Share the subject or grade you want next so rollout decisions can follow real demand.',
        [description]
    );

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormState((current) => ({ ...current, [name]: value }));
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setSubmitError('');
        setSubmitSuccess('');

        if (!formState.name.trim()) {
            setSubmitError('Please enter your name.');
            return;
        }

        if (!isValidEmail(formState.email)) {
            setSubmitError('Please enter a valid email address.');
            return;
        }

        if (!formState.requestedGrade) {
            setSubmitError('Please choose the grade you want Fundile to support.');
            return;
        }

        if (!formState.requestedSubject) {
            setSubmitError('Please choose the subject you want Fundile to support.');
            return;
        }

        if (!db) {
            setSubmitError('Demand capture is temporarily unavailable. Please email info@fundile.com instead.');
            return;
        }

        setIsSubmitting(true);
        try {
            await addDoc(collection(db, 'interest_submissions'), {
                name: formState.name.trim(),
                email: formState.email.trim().toLowerCase(),
                curriculum: formState.curriculum,
                requestedGrade: formState.requestedGrade,
                requestedSubject: formState.requestedSubject,
                schoolOrRole: formState.schoolOrRole.trim(),
                source,
                status: 'new',
                createdAt: serverTimestamp(),
            });

            setSubmitSuccess('Thanks. Fundile has saved your interest and will use it to prioritise rollout.');
            setFormState(INITIAL_FORM_STATE);
        } catch (error) {
            console.error('[Demand Capture] Failed to submit interest form', error);
            setSubmitError('Your request could not be submitted right now. Please try again or email info@fundile.com.');
        } finally {
            setIsSubmitting(false);
        }
    };

    return (
        <div className={containerClass}>
            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FFD166]">Interest form</p>
            <h3 className={`mt-4 text-2xl font-semibold ${titleClass}`} style={{ fontFamily: 'Afacad, sans-serif' }}>
                {formTitle}
            </h3>
            <p className={`mt-3 text-sm leading-7 ${bodyClass}`}>
                {formDescription}
            </p>

            <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
                <div className="grid gap-4 sm:grid-cols-2">
                    <label className={labelClass}>
                        Name
                        <input
                            type="text"
                            name="name"
                            value={formState.name}
                            onChange={handleChange}
                            className={inputClass}
                            placeholder="Your name"
                        />
                    </label>
                    <label className={labelClass}>
                        Email
                        <input
                            type="email"
                            name="email"
                            value={formState.email}
                            onChange={handleChange}
                            className={inputClass}
                            placeholder="name@example.com"
                        />
                    </label>
                </div>

                <div className="grid gap-4 sm:grid-cols-3">
                    <label className={labelClass}>
                        Curriculum
                        <select
                            name="curriculum"
                            value={formState.curriculum}
                            onChange={handleChange}
                            className={inputClass}
                        >
                            {DEMAND_CAPTURE_CURRICULUM_OPTIONS.map((option) => (
                                <option key={option} value={option} className={isLightPalette ? 'bg-white text-slate-900' : 'bg-slate-900 text-white'}>{option}</option>
                            ))}
                        </select>
                    </label>
                    <label className={labelClass}>
                        Requested grade
                        <select
                            name="requestedGrade"
                            value={formState.requestedGrade}
                            onChange={handleChange}
                            className={inputClass}
                        >
                            <option value="" className={isLightPalette ? 'bg-white text-slate-900' : 'bg-slate-900 text-white'}>Select grade</option>
                            {DEMAND_CAPTURE_GRADE_OPTIONS.map((option) => (
                                <option key={option} value={option} className={isLightPalette ? 'bg-white text-slate-900' : 'bg-slate-900 text-white'}>{option}</option>
                            ))}
                        </select>
                    </label>
                    <label className={labelClass}>
                        Requested subject
                        <select
                            name="requestedSubject"
                            value={formState.requestedSubject}
                            onChange={handleChange}
                            className={inputClass}
                        >
                            <option value="" className={isLightPalette ? 'bg-white text-slate-900' : 'bg-slate-900 text-white'}>Select subject</option>
                            {DEMAND_CAPTURE_SUBJECT_OPTIONS.map((option) => (
                                <option key={option} value={option} className={isLightPalette ? 'bg-white text-slate-900' : 'bg-slate-900 text-white'}>{option}</option>
                            ))}
                        </select>
                    </label>
                </div>

                <label className={labelClass}>
                    School or role
                    <input
                        type="text"
                        name="schoolOrRole"
                        value={formState.schoolOrRole}
                        onChange={handleChange}
                        className={inputClass}
                        placeholder="Optional school, parent, teacher, or coordinator note"
                    />
                </label>

                {submitError && (
                    <div className="rounded-2xl border border-red-500/30 bg-red-500/10 px-4 py-3 text-sm text-red-400">
                        {submitError}
                    </div>
                )}

                {submitSuccess && (
                    <div className="flex items-start gap-3 rounded-2xl border border-emerald-500/30 bg-emerald-500/10 px-4 py-3 text-sm text-emerald-400">
                        <CheckCircle className="mt-0.5 h-5 w-5 shrink-0" />
                        <span>{submitSuccess}</span>
                    </div>
                )}

                <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                    <p className={mutedClass}>
                        Fundile uses this information for rollout prioritisation, not for a heavy onboarding flow.
                    </p>
                    <button
                        type="submit"
                        disabled={isSubmitting}
                        className={`inline-flex items-center justify-center gap-2 rounded-2xl px-6 py-3.5 text-sm font-semibold text-white transition ${
                            isSubmitting
                                ? 'bg-slate-700 cursor-not-allowed text-slate-400'
                                : isLightPalette
                                ? 'bg-[#13519C] hover:bg-[#0f3e77]'
                                : 'bg-[#FF9100] hover:bg-[#f58200] shadow-[0_16px_50px_rgba(255,145,0,0.25)]'
                        }`}
                    >
                        {isSubmitting ? (
                            <>
                                <Loader2 className="h-4 w-4 animate-spin" /> Sending...
                            </>
                        ) : (
                            <>
                                <Send className="h-4 w-4" /> {submitLabel}
                            </>
                        )}
                    </button>
                </div>
            </form>
        </div>
    );
};

export default DemandCaptureForm;
