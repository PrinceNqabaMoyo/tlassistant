import React, { useState } from 'react';
import { sendEmailVerification } from 'firebase/auth';
import { Loader2, LogOut, MailCheck, RefreshCcw, Send, ShieldCheck } from 'lucide-react';

export default function VerificationScreen({ auth, currentUser, onContinueToDashboard, onLogout, statusMessage = '' }) {
  const [status, setStatus] = useState('');
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [isResending, setIsResending] = useState(false);

  const emailAddress = currentUser?.email || auth?.currentUser?.email || 'your inbox';

  const handleRefreshStatus = async () => {
    if (!auth?.currentUser) {
      setStatus('We could not find your active session. Please sign in again.');
      return;
    }

    setIsRefreshing(true);
    setStatus('');

    try {
      await auth.currentUser.reload();

      if (auth.currentUser.emailVerified) {
        const result = await onContinueToDashboard?.();

        if (result?.success === false) {
          setStatus(result.error || 'Your email is verified, but we could not refresh your session. Please sign in again.');
        }

        return;
      }

      setStatus('We still see your account as unverified. Open the email we sent, click the verification link, then try again.');
    } catch (error) {
      setStatus(error.message || 'We could not refresh your verification status. Please try again.');
    } finally {
      setIsRefreshing(false);
    }
  };

  const handleResendVerification = async () => {
    if (!auth?.currentUser) {
      setStatus('We could not find your active session. Please sign in again.');
      return;
    }

    setIsResending(true);
    setStatus('');

    try {
      await sendEmailVerification(auth.currentUser);
      setStatus('Verification email sent. Please check your inbox and spam folder, then come back here and refresh your status.');
    } catch (error) {
      setStatus(error.message || 'We could not resend the verification email right now. Please wait a moment and try again.');
    } finally {
      setIsResending(false);
    }
  };

  return (
    <div className="min-h-screen bg-[linear-gradient(180deg,_#f8fbff_0%,_#eef5ff_46%,_#f8fafc_100%)] px-4 py-10 text-slate-900 sm:px-6 lg:px-8">
      <div className="mx-auto flex min-h-[80vh] max-w-3xl items-center justify-center">
        <div className="w-full rounded-[32px] border border-sky-100 bg-white p-8 shadow-[0_24px_80px_rgba(43,123,216,0.10)] sm:p-10">
          <div className="mx-auto flex h-16 w-16 items-center justify-center rounded-full bg-[#13519C]/10 text-[#13519C]">
            <MailCheck className="h-8 w-8" />
          </div>
          <div className="mt-6 text-center">
            <p className="text-sm font-semibold uppercase tracking-[0.3em] text-[#2B7BD8]">Verify your email</p>
            <h1 className="mt-4 text-3xl font-bold tracking-tight text-slate-950 sm:text-4xl" style={{ fontFamily: 'Afacad, sans-serif' }}>
              Check your inbox before entering Fundile.
            </h1>
            <p className="mt-4 text-base leading-7 text-slate-600">
              We sent a verification email to <span className="font-semibold text-slate-900">{emailAddress}</span>. For security, you need to verify that address before you can access your dashboard.
            </p>
          </div>
          <div className="mt-8 rounded-3xl border border-sky-100 bg-slate-50 p-6">
            <div className="flex items-start gap-3">
              <ShieldCheck className="mt-1 h-5 w-5 text-[#13519C]" />
              <div className="space-y-3 text-sm leading-7 text-slate-600">
                <p>Open the verification email and click the link inside it.</p>
                <p>If you do not see it within a minute or two, check your spam or junk folder.</p>
                <p>After verifying, return here and refresh your status to continue to your dashboard.</p>
              </div>
            </div>
          </div>
          {statusMessage ? (
            <div className="mt-6 rounded-2xl border border-emerald-100 bg-emerald-50 px-4 py-3 text-sm text-emerald-800">
              {statusMessage}
            </div>
          ) : null}
          {status ? (
            <div className="mt-6 rounded-2xl border border-sky-100 bg-sky-50 px-4 py-3 text-sm text-[#13519C]">
              {status}
            </div>
          ) : null}
          <div className="mt-8 flex flex-col gap-4 sm:flex-row">
            <button
              type="button"
              onClick={handleRefreshStatus}
              disabled={isRefreshing}
              className="inline-flex flex-1 items-center justify-center gap-2 rounded-2xl bg-[#13519C] px-6 py-4 text-base font-semibold text-white transition hover:bg-[#0f3e77] disabled:cursor-not-allowed disabled:bg-slate-400"
            >
              {isRefreshing ? <Loader2 className="h-5 w-5 animate-spin" /> : <RefreshCcw className="h-5 w-5" />}
              I have verified my email
            </button>
            <button
              type="button"
              onClick={handleResendVerification}
              disabled={isResending}
              className="inline-flex flex-1 items-center justify-center gap-2 rounded-2xl border border-slate-200 bg-white px-6 py-4 text-base font-semibold text-slate-700 transition hover:border-slate-300 hover:bg-slate-50 disabled:cursor-not-allowed disabled:text-slate-400"
            >
              {isResending ? <Loader2 className="h-5 w-5 animate-spin" /> : <Send className="h-5 w-5" />}
              Resend verification email
            </button>
          </div>
          <button
            type="button"
            onClick={onLogout}
            className="mt-4 inline-flex w-full items-center justify-center gap-2 rounded-2xl border border-transparent px-6 py-3 text-sm font-semibold text-slate-500 transition hover:bg-slate-50 hover:text-slate-700"
          >
            <LogOut className="h-4 w-4" />
            Sign out
          </button>
        </div>
      </div>
    </div>
  );
}
