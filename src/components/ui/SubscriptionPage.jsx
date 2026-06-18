import React from 'react';
import { ArrowRight, CreditCard, Paperclip, ShieldCheck } from 'lucide-react';
import FundileLogo from './FundileLogo';
import { EftUploadModal } from '../student/EftUploadModal';
import DemandCaptureForm from './DemandCaptureForm';
import { LIVE_AVAILABILITY_DETAIL, LIVE_AVAILABILITY_HEADLINE, LIVE_AVAILABILITY_NOTE } from '../../app/constants/availability';

const SubscriptionPage = ({
    currentUser,
    storage,
    db,
    targetGrade,
    onNavigateHome,
    onNavigateSignIn,
    onNavigateSignUp,
    onNavigateApp,
}) => {
    const fileInputRef = React.useRef(null);
    const [isPopUploadRevealed, setIsPopUploadRevealed] = React.useState(false);
    const paymentReference = currentUser?.paymentReference || currentUser?.lastPaymentReference || 'FND-REF';

    const handleChoosePop = () => {
        setIsPopUploadRevealed(true);
        fileInputRef.current?.click();
    };

    return (
        <div className="min-h-screen bg-[linear-gradient(180deg,_#f8fbff_0%,_#eef5ff_46%,_#f8fafc_100%)] text-slate-900">
            <div className="fixed inset-x-0 top-0 z-50 border-b border-sky-100 bg-white/95 backdrop-blur-sm">
                <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center">
                        <FundileLogo className="h-48 w-48" wordmarkColor="#13519C" />
                    </div>
                    <button
                        type="button"
                        onClick={onNavigateHome}
                        className="rounded-lg border border-sky-100 bg-slate-50 px-5 py-2 font-medium text-[#13519C] transition hover:bg-sky-50"
                    >
                        Home
                    </button>
                </div>
            </div>

            <main className="mx-auto max-w-7xl px-4 pb-20 pt-24 sm:px-6 lg:px-8">
                <div className="space-y-6 lg:space-y-8">
                    <section className="grid gap-5 xl:grid-cols-[1.15fr_0.9fr_0.9fr] xl:items-stretch">
                        <div className="rounded-[32px] border border-sky-100 bg-white p-8 shadow-[0_24px_80px_rgba(43,123,216,0.10)]">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#2B7BD8]">Subscription</p>
                            <h1 className="mt-4 text-4xl font-bold tracking-tight text-slate-950 sm:text-5xl" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                Fundile currently only accepts EFT payments.
                            </h1>
                            <p className="mt-4 text-sm leading-7 text-slate-500">
                                {currentUser
                                    ? 'Your account is signed in. Make the EFT, then attach the POP from this page using the paperclip button.'
                                    : 'Sign in to upload proof of payment in the subscription page. Banking details provided below.'}
                            </p>
                            <p className="mt-5 text-lg leading-8 text-slate-600">
                                Choose the package that fits your needs, make your EFT payment, and then upload your proof of payment so your subscription request can be linked to your Fundile profile.
                            </p>
                        </div>

                        <div className="rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/40">
                            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#2B7BD8]">Standard package</p>
                            <h2 className="mt-4 text-2xl font-semibold text-slate-950">R150 monthly or R1600 for 12 months</h2>
                            <p className="mt-3 leading-7 text-slate-600">
                                Save R200 on the annual option. Standard gives access to the currently available Grade 10 and Grade 11 Accounting experience.
                            </p>
                            <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                <span className="rounded-full bg-[#13519C]/10 px-3 py-1 text-[#13519C]">Available now</span>
                                <span className="rounded-full bg-emerald-100 px-3 py-1 text-emerald-700">Save R200 yearly</span>
                            </div>
                        </div>

                        <div className="rounded-[28px] border border-violet-100 bg-white p-6 shadow-lg shadow-violet-100/40">
                            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-violet-600">Pro package</p>
                            <h2 className="mt-4 text-2xl font-semibold text-slate-950">R299 monthly or R3100 for 12 months</h2>
                            <p className="mt-3 leading-7 text-slate-600">
                                Save R488 on the annual option. Pro connects to an LLM to provide running comments on student questions, answers, and procedures.
                            </p>
                            <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                <span className="rounded-full bg-violet-100 px-3 py-1 text-violet-700">Coming soon</span>
                                <span className="rounded-full bg-amber-100 px-3 py-1 text-amber-700">Not yet available in South Africa</span>
                            </div>
                        </div>
                    </section>

                    <section className="space-y-5">
                        <div className="rounded-[28px] border border-sky-100 bg-white px-6 py-5 shadow-lg shadow-sky-100/40">
                            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FF9100]">Availability</p>
                            <p className="mt-2 text-lg font-semibold text-slate-950">{LIVE_AVAILABILITY_HEADLINE}</p>
                            <p className="mt-2 text-sm leading-7 text-slate-600">{LIVE_AVAILABILITY_NOTE}</p>
                            <p className="mt-2 text-sm leading-7 text-slate-500">{LIVE_AVAILABILITY_DETAIL}</p>
                        </div>
                    </section>

                    <section className="grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
                        <div className="rounded-2xl border border-sky-100 bg-slate-50 p-5">
                            <div className="flex items-center gap-3 text-[#13519C]">
                                <CreditCard className="h-5 w-5" />
                                <span className="text-sm font-semibold uppercase tracking-[0.25em]">Banking details</span>
                            </div>
                            <div className="mt-4 space-y-2 text-sm text-slate-600">
                                <p><span className="font-semibold text-slate-900">Bank:</span> Access Bank</p>
                                <p><span className="font-semibold text-slate-900">Account No:</span> 51622451787</p>
                                <p><span className="font-semibold text-slate-900">Branch Code:</span> 410506</p>
                            </div>
                        </div>

                        <div className="rounded-2xl border border-sky-100 bg-slate-50 p-5">
                            <div className="flex items-center gap-3 text-[#13519C]">
                                <ShieldCheck className="h-5 w-5" />
                                <span className="text-sm font-semibold uppercase tracking-[0.25em]">How access works</span>
                            </div>
                            <p className="mt-4 text-sm leading-7 text-slate-600">
                                Standard currently covers the live Grade 10 and Grade 11 Accounting experience, and active yearly subscriptions automatically roll into the next grade from December when eligible.
                            </p>
                        </div>

                        {currentUser && (
                            <div className="rounded-2xl border border-sky-100 bg-slate-50 p-5 sm:col-span-2 xl:col-span-1">
                                <div className="flex items-center gap-3 text-[#13519C]">
                                    <Paperclip className="h-5 w-5" />
                                    <span className="text-sm font-semibold uppercase tracking-[0.25em]">Your payment reference</span>
                                </div>
                                <p className="mt-4 text-sm leading-7 text-slate-600">
                                    Use this exact reference in the EFT narration or transfer description so the proof of payment can be matched to your Fundile account quickly.
                                </p>
                                <p className="mt-4 break-all rounded-2xl bg-white px-4 py-3 font-mono text-sm font-semibold text-slate-900 shadow-sm">
                                    {paymentReference}
                                </p>
                            </div>
                        )}
                    </section>

                    <section className="space-y-5">
                        {currentUser ? (
                            <EftUploadModal
                                compact
                                currentUser={currentUser}
                                storage={storage}
                                db={db}
                                onClose={onNavigateApp || onNavigateHome}
                                targetGrade={targetGrade || currentUser?.grade}
                                fileInputRef={fileInputRef}
                                revealed={isPopUploadRevealed}
                            />
                        ) : null}
                    </section>

                    <section className="rounded-[28px] border border-sky-100 bg-white px-6 py-5 shadow-lg shadow-sky-100/40">
                        <div className="flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
                            <div>
                                <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#2B7BD8]">Proof of payment</p>
                                <p className="mt-2 text-sm leading-7 text-slate-600">
                                    {currentUser
                                        ? (currentUser?.paymentStatus === 'pending_review' 
                                            ? 'Your proof of payment has been received and is currently being reviewed.'
                                            : 'Use the orange button to attach your proof of payment after making the EFT. The upload island appears above once you choose a file.')
                                        : 'Sign in to upload proof of payment after you complete the EFT.'}
                                </p>
                            </div>

                            <div className="flex flex-col gap-4 sm:flex-row">
                                {currentUser ? (
                                    <>
                                        {currentUser?.paymentStatus === 'pending_review' ? (
                                            <button
                                                type="button"
                                                disabled
                                                className="inline-flex items-center justify-center gap-2 rounded-2xl bg-slate-300 px-6 py-4 text-base font-semibold text-slate-500 transition cursor-not-allowed"
                                            >
                                                Awaiting POP approval
                                            </button>
                                        ) : (
                                            <button
                                                type="button"
                                                onClick={handleChoosePop}
                                                className="inline-flex items-center justify-center gap-2 rounded-2xl bg-[#FF9100] px-6 py-4 text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.25)] transition hover:bg-[#f58200]"
                                            >
                                                Attach proof of payment
                                                <Paperclip className="h-5 w-5" />
                                            </button>
                                        )}
                                        <button
                                            type="button"
                                            onClick={onNavigateApp || onNavigateHome}
                                            className="inline-flex items-center justify-center rounded-2xl border border-slate-200 bg-white px-6 py-4 text-base font-semibold text-slate-700 transition hover:border-slate-300 hover:bg-slate-50"
                                        >
                                            Back to dashboard
                                        </button>
                                    </>
                                ) : (
                                    <>
                                        <button
                                            type="button"
                                            onClick={onNavigateSignIn}
                                            className="inline-flex items-center justify-center gap-2 rounded-2xl bg-[#FF9100] px-6 py-4 text-base font-semibold text-white shadow-[0_16px_50px_rgba(255,145,0,0.25)] transition hover:bg-[#f58200]"
                                        >
                                            Sign in to upload proof of payment
                                            <ArrowRight className="h-5 w-5" />
                                        </button>
                                        <button
                                            type="button"
                                            onClick={onNavigateSignUp}
                                            className="inline-flex items-center justify-center rounded-2xl border border-slate-200 bg-white px-6 py-4 text-base font-semibold text-slate-700 transition hover:border-slate-300 hover:bg-slate-50"
                                        >
                                            Create account
                                        </button>
                                    </>
                                )}
                            </div>
                        </div>
                    </section>

                    {!currentUser && (
                        <DemandCaptureForm
                            db={db}
                            source="subscription_page"
                            title="Need a different grade or subject before you subscribe?"
                            description="Tell Fundile what you need next so pricing and rollout decisions stay aligned with real demand."
                            submitLabel="Register your need"
                        />
                    )}
                </div>
            </main>
        </div>
    );
};

export default SubscriptionPage;
