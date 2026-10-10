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

    const isTrialActive = Boolean(
        currentUser?.paymentStatus === 'trial_active' ||
        (currentUser?.subscriptionExpiry && new Date(currentUser.subscriptionExpiry?.toDate ? currentUser.subscriptionExpiry.toDate() : currentUser.subscriptionExpiry) > new Date() && currentUser?.paymentStatus !== 'approved')
    );

    const trialDaysLeft = React.useMemo(() => {
        if (!currentUser?.subscriptionExpiry) return 14;
        const expiry = currentUser.subscriptionExpiry?.toDate ? currentUser.subscriptionExpiry.toDate() : new Date(currentUser.subscriptionExpiry);
        const diff = expiry.getTime() - Date.now();
        return Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)));
    }, [currentUser?.subscriptionExpiry]);

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
                    {/* Active Free Trial Status Card */}
                    {isTrialActive && (
                        <div className="rounded-[28px] border-2 border-emerald-500 bg-gradient-to-r from-emerald-500/10 via-white to-sky-50 p-6 sm:p-8 shadow-lg shadow-emerald-500/10">
                            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                                <div className="space-y-1.5">
                                    <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-xs font-extrabold uppercase tracking-wider">
                                        <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                                        14-Day Free Trial Active • Grade {currentUser?.grade || targetGrade || 10}
                                    </div>
                                    <h2 className="text-2xl sm:text-3xl font-bold text-slate-950" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                        You have {trialDaysLeft} {trialDaysLeft === 1 ? 'day' : 'days'} remaining in your free trial
                                    </h2>
                                    <p className="text-sm text-slate-600 max-w-2xl leading-relaxed">
                                        All your Grade {currentUser?.grade || targetGrade || 10} subjects are fully accessible right now. You can continue practicing freely, or use the banking details below anytime to activate an uninterrupted Term or Annual Pass via EFT.
                                    </p>
                                </div>
                                <button
                                    type="button"
                                    onClick={onNavigateApp || onNavigateHome}
                                    className="inline-flex items-center justify-center gap-2 rounded-2xl bg-[#13519C] hover:bg-[#0f3e77] text-white px-6 py-3.5 text-sm font-bold shadow-md shadow-blue-900/20 transition cursor-pointer shrink-0"
                                >
                                    Continue Learning →
                                </button>
                            </div>
                        </div>
                    )}

                    <section className="grid gap-5 xl:grid-cols-[1.15fr_0.9fr_0.9fr] xl:items-stretch">
                        <div className="rounded-[32px] border border-sky-100 bg-white p-8 shadow-[0_24px_80px_rgba(43,123,216,0.10)]">
                            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#2B7BD8]">
                                {isTrialActive ? 'Extend Your Access' : 'Subscription'}
                            </p>
                            <h1 className="mt-4 text-4xl font-bold tracking-tight text-slate-950 sm:text-5xl" style={{ fontFamily: 'Afacad, sans-serif' }}>
                                {isTrialActive ? 'Activate Permanent Access via EFT.' : 'Fundile currently only accepts EFT payments.'}
                            </h1>
                            <p className="mt-4 text-sm leading-7 text-slate-500">
                                {isTrialActive
                                    ? 'Your trial access is already active. When you make an EFT for a Term or Annual pass, attach your POP below to lock in permanent access.'
                                    : (currentUser
                                        ? 'Your account is signed in. Make the EFT, then attach the POP from this page using the paperclip button.'
                                        : 'Sign in to upload proof of payment in the subscription page. Banking details provided below.')}
                            </p>
                            <p className="mt-5 text-lg leading-8 text-slate-600">
                                Choose the package that fits your needs, make your EFT payment, and then upload your proof of payment so your subscription request can be linked to your Fundile profile.
                            </p>
                        </div>

                        <div className="rounded-[28px] border border-sky-100 bg-white p-6 shadow-lg shadow-sky-100/40">
                            <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#2B7BD8]">Monthly Access</p>
                            <h2 className="mt-4 text-2xl font-semibold text-slate-950">R149 / month</h2>
                            <p className="mt-3 leading-7 text-slate-600">
                                Complete self-paced access across all 259 topics in Grades 7–12. Cancel anytime.
                            </p>
                            <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                <span className="rounded-full bg-[#13519C]/10 px-3 py-1 text-[#13519C]">Available now</span>
                                <span className="rounded-full bg-slate-100 px-3 py-1 text-slate-700">Cancel anytime</span>
                            </div>
                        </div>

                        <div className="rounded-[28px] border-2 border-[#13519C] bg-white p-6 shadow-lg shadow-blue-900/10">
                            <div className="flex items-center justify-between">
                                <p className="text-sm font-semibold uppercase tracking-[0.25em] text-[#FF9100]">Term &amp; Annual Passes</p>
                                <span className="rounded-full bg-amber-100 px-2.5 py-0.5 text-xs font-bold text-[#FF9100]">Best Value</span>
                            </div>
                            <h2 className="mt-4 text-2xl font-semibold text-slate-950">R349 / Term or R999 / Year</h2>
                            <p className="mt-3 leading-7 text-slate-600">
                                R349 per 3-month school term (save R98) or R999 for full 12-month academic year (save R789, ~R83/mo).
                            </p>
                            <div className="mt-5 flex flex-wrap gap-3 text-sm font-semibold">
                                <span className="rounded-full bg-amber-100 px-3 py-1 text-amber-800">Term Pass: ~R116/mo</span>
                                <span className="rounded-full bg-emerald-100 px-3 py-1 text-emerald-800">Annual Pass: ~R83/mo</span>
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
