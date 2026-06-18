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

const DemandCaptureForm = ({ db, source = 'public_surface', title, description, submitLabel = 'Register interest' }) => {
    const [formState, setFormState] = useState(INITIAL_FORM_STATE);
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [submitError, setSubmitError] = useState('');
    const [submitSuccess, setSubmitSuccess] = useState('');

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
        <div className="rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/30 sm:p-8">
            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#2B7BD8]">Interest form</p>
            <h3 className="mt-4 text-2xl font-semibold text-slate-950" style={{ fontFamily: 'Afacad, sans-serif' }}>
                {formTitle}
            </h3>
            <p className="mt-3 text-sm leading-7 text-slate-600">
                {formDescription}
            </p>

            <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
                <div className="grid gap-4 sm:grid-cols-2">
                    <label className="block text-sm font-medium text-slate-700">
                        Name
                        <input
                            type="text"
                            name="name"
                            value={formState.name}
                            onChange={handleChange}
                            className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                            placeholder="Your name"
                        />
                    </label>
                    <label className="block text-sm font-medium text-slate-700">
                        Email
                        <input
                            type="email"
                            name="email"
                            value={formState.email}
                            onChange={handleChange}
                            className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                            placeholder="name@example.com"
                        />
                    </label>
                </div>

                <div className="grid gap-4 sm:grid-cols-3">
                    <label className="block text-sm font-medium text-slate-700">
                        Curriculum
                        <select
                            name="curriculum"
                            value={formState.curriculum}
                            onChange={handleChange}
                            className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                        >
                            {DEMAND_CAPTURE_CURRICULUM_OPTIONS.map((option) => (
                                <option key={option} value={option}>{option}</option>
                            ))}
                        </select>
                    </label>
                    <label className="block text-sm font-medium text-slate-700">
                        Requested grade
                        <select
                            name="requestedGrade"
                            value={formState.requestedGrade}
                            onChange={handleChange}
                            className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                        >
                            <option value="">Select grade</option>
                            {DEMAND_CAPTURE_GRADE_OPTIONS.map((option) => (
                                <option key={option} value={option}>{option}</option>
                            ))}
                        </select>
                    </label>
                    <label className="block text-sm font-medium text-slate-700">
                        Requested subject
                        <select
                            name="requestedSubject"
                            value={formState.requestedSubject}
                            onChange={handleChange}
                            className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                        >
                            <option value="">Select subject</option>
                            {DEMAND_CAPTURE_SUBJECT_OPTIONS.map((option) => (
                                <option key={option} value={option}>{option}</option>
                            ))}
                        </select>
                    </label>
                </div>

                <label className="block text-sm font-medium text-slate-700">
                    School or role
                    <input
                        type="text"
                        name="schoolOrRole"
                        value={formState.schoolOrRole}
                        onChange={handleChange}
                        className="mt-2 block w-full rounded-2xl border border-slate-200 px-4 py-3 text-slate-900 outline-none transition focus:border-[#2B7BD8] focus:ring-2 focus:ring-[#2B7BD8]/15"
                        placeholder="Optional school, parent, teacher, or coordinator note"
                    />
                </label>

                {submitError && (
                    <div className="rounded-2xl border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
                        {submitError}
                    </div>
                )}

                {submitSuccess && (
                    <div className="flex items-start gap-3 rounded-2xl border border-emerald-200 bg-emerald-50 px-4 py-3 text-sm text-emerald-800">
                        <CheckCircle className="mt-0.5 h-5 w-5 shrink-0" />
                        <span>{submitSuccess}</span>
                    </div>
                )}

                <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
                    <p className="text-xs leading-6 text-slate-500">
                        Fundile uses this information for rollout prioritisation, not for a heavy onboarding flow.
                    </p>
                    <button
                        type="submit"
                        disabled={isSubmitting}
                        className={`inline-flex items-center justify-center gap-2 rounded-2xl px-5 py-3 text-sm font-semibold text-white transition ${isSubmitting ? 'bg-slate-300 cursor-not-allowed' : 'bg-[#13519C] hover:bg-[#0f3e77]'}`}
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
