import React, { useMemo, useRef, useState } from 'react';
import { getAuth } from 'firebase/auth';
import { collection, addDoc, doc, updateDoc, serverTimestamp } from 'firebase/firestore';
import { X, UploadCloud, CheckCircle, AlertCircle, Loader2, Copy, ShieldCheck } from 'lucide-react';
import GraduationCapSplash from '../ui/GraduationCapSplash';
import { buildApiUrl } from '../../utils/apiBaseUrl';

const MAX_POP_FILE_SIZE_BYTES = 10 * 1024 * 1024;
const ACCEPTED_POP_FILE_TYPES = ['application/pdf', 'image/jpeg', 'image/png'];
const POP_UPLOAD_TIMEOUT_MS = 5 * 60 * 1000;
const POP_FILE_REQUIREMENTS_LABEL = 'PDF, JPG, or PNG up to 10 MB';

const formatFileSize = (bytes = 0) => {
    if (!bytes) return '0 KB';
    if (bytes >= 1024 * 1024) return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
    return `${Math.max(1, Math.round(bytes / 1024))} KB`;
};

const sanitizeFileName = (value = '') => String(value).replace(/[^a-zA-Z0-9._-]/g, '_');

const validatePopFile = (selectedFile) => {
    if (!selectedFile) {
        return 'Please select a valid PDF or image file first.';
    }

    if (!ACCEPTED_POP_FILE_TYPES.includes(selectedFile.type)) {
        return 'Only PDF, JPG, and PNG files are accepted for proof of payment uploads.';
    }

    if (selectedFile.size > MAX_POP_FILE_SIZE_BYTES) {
        return 'The selected file is too large. Please upload a file smaller than 10 MB.';
    }

    return '';
};

const mapUploadErrorMessage = (error, timedOut = false) => {
    if (timedOut) {
        return 'The upload took too long and was cancelled. Please try again with a smaller file or a stronger connection.';
    }

    if (error?.code === 'storage/unauthorized') {
        return 'Upload permission was denied. Please sign in again or contact support.';
    }

    if (error?.code === 'storage/canceled') {
        return 'The upload was cancelled before completion. Please try again.';
    }

    if (error?.code === 'storage/retry-limit-exceeded') {
        return 'The upload could not finish because the connection kept failing. Please try again.';
    }

    if (error?.code === 'storage/invalid-checksum') {
        return 'The uploaded file could not be verified. Please re-export the POP and try again.';
    }

    if (error?.message === 'Missing Firebase bearer token.') {
        return 'Please sign in again before uploading your proof of payment.';
    }

    return error?.message || 'Failed to securely upload the file.';
};

export const EftUploadModal = ({ isOpen, onClose, currentUser, db, targetGrade, embedded = false, compact = false, fileInputRef = null, revealed = false }) => {
    const [file, setFile] = useState(null);
    const [selectedPlan, setSelectedPlan] = useState('monthly'); // 'monthly' | 'yearly'
    const [status, setStatus] = useState('idle'); // 'idle' | 'uploading' | 'uploaded' | 'submitting' | 'success' | 'upload_error' | 'submit_error'
    const [errorMessage, setErrorMessage] = useState('');
    const [showProComingSoon, setShowProComingSoon] = useState(false);
    const [uploadProgress, setUploadProgress] = useState(0);
    const [uploadStage, setUploadStage] = useState('Ready to receive your proof of payment.');
    const [recentEvents, setRecentEvents] = useState([]);
    const [copyFeedback, setCopyFeedback] = useState('');
    const [uploadedPop, setUploadedPop] = useState(null);
    const uploadTimeoutRef = useRef(null);
    const uploadTimedOutRef = useRef(false);
    const uploadStageRef = useRef('Ready to receive your proof of payment.');
    const uploadProgressRef = useRef(0);
    const uploadStatusRef = useRef('idle');
    const displayProgressIntervalRef = useRef(null);
    const uploadRequestRef = useRef(null);
    const internalFileInputRef = useRef(null);

    const referenceId = currentUser?.paymentReference || currentUser?.lastPaymentReference || (currentUser?.uid ? `FND-${String(currentUser.uid).replace(/[^a-zA-Z0-9]/g, '').toUpperCase().slice(0, 12)}` : 'FND-REF');
    const selectedPlanDetails = useMemo(() => {
        if (selectedPlan === 'yearly') {
            return {
                label: 'Standard - 12 Months (R1600)',
                amount: 1600,
            };
        }

        return {
            label: 'Standard - 1 Month (R150)',
            amount: 150,
        };
    }, [selectedPlan]);
    const selectedPlanLabel = selectedPlanDetails.label;
    const selectedPlanAmount = selectedPlanDetails.amount;
    const isUploading = status === 'uploading';
    const isSubmitting = status === 'submitting';
    const isBusy = isUploading || isSubmitting;
    const isPendingReview = currentUser?.paymentStatus === 'pending_review';
    const hasError = status === 'upload_error' || status === 'submit_error';
    const canSubmitUploadedPop = Boolean(file && uploadedPop) && (status === 'uploaded' || status === 'submit_error');
    const isPlanLocked = isBusy || canSubmitUploadedPop || status === 'success' || isPendingReview;
    const resolvedFileInputRef = fileInputRef || internalFileInputRef;
    const effectivePlanLabel = compact ? 'Standard EFT POP' : selectedPlanLabel;
    const effectivePlanKey = compact ? 'standard' : selectedPlan;
    const effectivePlanAmount = compact ? null : selectedPlanAmount;
    const shouldShowCompactPanel = revealed || Boolean(file) || status !== 'idle' || isPendingReview;
    const visibleUploadProgress = status === 'uploaded' || status === 'submitting' || status === 'submit_error' || status === 'success' ? 100 : uploadProgress;

    if (!embedded && !compact && !isOpen) return null;

    const clearUploadTimeout = () => {
        if (uploadTimeoutRef.current) {
            clearTimeout(uploadTimeoutRef.current);
            uploadTimeoutRef.current = null;
        }
    };

    const clearDisplayProgressInterval = () => {
        if (displayProgressIntervalRef.current) {
            clearInterval(displayProgressIntervalRef.current);
            displayProgressIntervalRef.current = null;
        }
    };

    const syncUploadStatus = (nextStatus) => {
        uploadStatusRef.current = nextStatus;
        setStatus(nextStatus);
    };

    const syncUploadProgress = (nextProgress) => {
        uploadProgressRef.current = nextProgress;
        setUploadProgress(nextProgress);
    };

    const clearActiveUploadRequest = () => {
        uploadRequestRef.current = null;
    };

    const getFirebaseIdToken = async () => {
        const auth = getAuth();
        const authUser = auth.currentUser;

        if (!authUser || !currentUser?.uid || authUser.uid !== currentUser.uid) {
            throw new Error('Missing Firebase bearer token.');
        }

        return authUser.getIdToken();
    };

    const removeUploadedStorageObject = async (storagePath) => {
        if (!storagePath) {
            return;
        }

        try {
            const idToken = await getFirebaseIdToken();
            const response = await fetch(buildApiUrl('/api/payments/pop-delete'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}`,
                },
                body: JSON.stringify({ storagePath }),
            });

            if (!response.ok) {
                const payload = await response.json().catch(() => ({}));
                throw new Error(payload?.error || 'Failed to remove the uploaded POP file.');
            }
        } catch (error) {
            console.warn('[POP Upload] Failed to remove previously uploaded storage object', error);
        }
    };

    const resetSelectedFileState = () => {
        setFile(null);
        setUploadedPop(null);
        syncUploadStatus('idle');
        setErrorMessage('');
        syncUploadProgress(0);
        setRecentEvents([]);
        clearDisplayProgressInterval();
        updateUploadStage('Ready to receive your proof of payment.');

        if (resolvedFileInputRef?.current) {
            resolvedFileInputRef.current.value = '';
        }
    };

    const updateUploadStage = (nextStage) => {
        uploadStageRef.current = nextStage;
        setUploadStage(nextStage);
    };

    const appendRecentEvent = (message) => {
        console.info(`[POP Upload] ${message}`);
        setRecentEvents((prev) => [...prev.slice(-3), message]);
    };

    const startBackendUpload = async (selectedFile) => {
        if (!currentUser) {
            setUploadedPop(null);
            setErrorMessage('You need to be signed in before uploading a proof of payment.');
            syncUploadStatus('upload_error');
            updateUploadStage('Upload cannot start because your account session is not ready.');
            return;
        }

        syncUploadStatus('uploading');
        setErrorMessage('');
        setUploadedPop(null);
        syncUploadProgress(0);
        setRecentEvents([]);
        uploadTimedOutRef.current = false;
        updateUploadStage('Starting secure POP upload...');
        appendRecentEvent('POP upload started.');

        try {
            const idToken = await getFirebaseIdToken();
            const formData = new FormData();
            formData.append('file', selectedFile);

            clearUploadTimeout();

            const uploadResult = await new Promise((resolve, reject) => {
                const xhr = new XMLHttpRequest();
                uploadRequestRef.current = xhr;
                xhr.open('POST', buildApiUrl('/api/payments/pop-upload'));
                xhr.setRequestHeader('Authorization', `Bearer ${idToken}`);
                xhr.responseType = 'json';

                xhr.upload.onprogress = (event) => {
                    if (!event.lengthComputable) {
                        return;
                    }

                    const nextProgress = event.total > 0
                        ? Math.min(100, Math.round((event.loaded / event.total) * 100))
                        : 0;
                    syncUploadProgress(nextProgress);
                    updateUploadStage(
                        nextProgress >= 100
                            ? 'POP upload reached 100%. Finalising secure storage...'
                            : `Uploading proof of payment (${nextProgress}%)`
                    );
                };

                xhr.onload = () => {
                    clearActiveUploadRequest();
                    let payload = xhr.response;
                    if (!payload || typeof payload !== 'object') {
                        try {
                            payload = xhr.responseText ? JSON.parse(xhr.responseText) : {};
                        } catch (parseError) {
                            payload = {};
                        }
                    }

                    if (xhr.status >= 200 && xhr.status < 300 && payload?.success && payload?.upload) {
                        resolve(payload.upload);
                        return;
                    }

                    reject(new Error(payload?.error || `POP upload failed with status ${xhr.status}.`));
                };

                xhr.onerror = () => {
                    clearActiveUploadRequest();
                    reject(new Error('Could not reach the POP upload service.'));
                };

                xhr.onabort = () => {
                    clearActiveUploadRequest();
                    reject(new Error(uploadTimedOutRef.current ? 'The upload took too long and was cancelled.' : 'The upload was cancelled before completion. Please try again.'));
                };

                uploadTimeoutRef.current = window.setTimeout(() => {
                    uploadTimedOutRef.current = true;
                    xhr.abort();
                }, POP_UPLOAD_TIMEOUT_MS);

                xhr.send(formData);
            });

            clearUploadTimeout();
            appendRecentEvent('POP upload completed.');

            setUploadedPop(uploadResult);
            syncUploadProgress(100);
            updateUploadStage('POP upload complete. Submit is now unlocked.');
            appendRecentEvent('POP is ready for final submission.');
            syncUploadStatus('uploaded');
        } catch (error) {
            const timedOut = uploadTimedOutRef.current;
            console.error(`[POP Upload] Failed during ${uploadStageRef.current}`, error);
            setUploadedPop(null);
            setErrorMessage(mapUploadErrorMessage(error, timedOut));
            appendRecentEvent(`Upload failed during ${uploadStageRef.current}.`);
            updateUploadStage(timedOut ? 'Upload timed out before the POP could finish uploading.' : 'Upload failed before the POP could finish uploading.');
            syncUploadStatus('upload_error');
        } finally {
            clearUploadTimeout();
            clearActiveUploadRequest();
            uploadTimedOutRef.current = false;
        }
    };

    const handleRemoveSelectedFile = async () => {
        if (isBusy) {
            return;
        }

        const storagePathToRemove = uploadedPop?.storagePath || null;
        resetSelectedFileState();
        await removeUploadedStorageObject(storagePathToRemove);
    };

    const handleFileChange = async (e) => {
        console.info('[POP Upload] File selection started');
        const selectedFile = e.target.files && e.target.files[0] ? e.target.files[0] : null;

        if (!selectedFile) {
            return;
        }

        const validationMessage = validatePopFile(selectedFile);
        if (validationMessage) {
            setFile(null);
            setUploadedPop(null);
            syncUploadStatus('upload_error');
            setErrorMessage(validationMessage);
            syncUploadProgress(0);
            setRecentEvents([]);
            clearDisplayProgressInterval();
            updateUploadStage('File validation failed.');
            appendRecentEvent(`File rejected: ${selectedFile.name}`);
            e.target.value = '';
            return;
        }

        const storagePathToRemove = uploadedPop?.storagePath || null;

        setFile(selectedFile);
        setUploadedPop(null);
        syncUploadStatus('idle');
        setErrorMessage('');
        syncUploadProgress(0);
        setRecentEvents([]);
        clearDisplayProgressInterval();
        updateUploadStage('Preparing selected file for secure upload.');
        appendRecentEvent(`File selected: ${selectedFile.name} (${formatFileSize(selectedFile.size)})`);

        if (storagePathToRemove) {
            await removeUploadedStorageObject(storagePathToRemove);
        }

        await startBackendUpload(selectedFile);
    };

    const handleCopy = async (value, label) => {
        if (!value) {
            return;
        }

        try {
            await navigator.clipboard.writeText(value);
            setCopyFeedback(`${label} copied.`);
            window.setTimeout(() => setCopyFeedback(''), 1800);
        } catch (error) {
            console.error(`[POP Upload] Failed to copy ${label.toLowerCase()}`, error);
            setCopyFeedback(`Unable to copy ${label.toLowerCase()}. Please copy it manually.`);
            window.setTimeout(() => setCopyFeedback(''), 2400);
        }
    };

    const handleUpload = async () => {
        if (isBusy) {
            return;
        }

        if (!file) {
            setErrorMessage('Please select a proof of payment file to continue.');
            syncUploadStatus('upload_error');
            updateUploadStage('Choose a proof of payment file to continue.');
            return;
        }

        if (!uploadedPop || uploadProgressRef.current < 100) {
            setErrorMessage('Please wait for the upload to reach 100% before submitting your proof of payment.');
            syncUploadStatus(uploadedPop ? 'submit_error' : 'upload_error');
            updateUploadStage('Upload must finish before submission can continue.');
            return;
        }

        if (!db || !currentUser) {
            setErrorMessage('Firebase services are not fully initialized.');
            syncUploadStatus('submit_error');
            updateUploadStage('Submission cannot start because the payment services are not ready.');
            return;
        }

        syncUploadStatus('submitting');
        setErrorMessage('');
        syncUploadProgress(100);

        try {
            let paymentDoc;
            try {
                updateUploadStage('Saving payment record...');
                appendRecentEvent('Firestore payment record write started.');
                const paymentRef = collection(db, 'pending_payments');
                paymentDoc = await addDoc(paymentRef, {
                    userId: currentUser.uid,
                    email: currentUser.email || 'No Email',
                    name: currentUser.name || currentUser.displayName || 'App User',
                    requestedGrade: targetGrade || 'Any',
                    plan: effectivePlanLabel,
                    planKey: effectivePlanKey,
                    amountDeposited: effectivePlanAmount,
                    paymentReference: referenceId,
                    referenceUsed: referenceId,
                    popUrl: '', // Send empty string instead of null to satisfy strict Firestore schema rules
                    popFileName: uploadedPop.fileName,
                    popMimeType: uploadedPop.mimeType,
                    popFileSizeBytes: uploadedPop.fileSizeBytes,
                    storagePath: uploadedPop.storagePath,
                    storageProvider: uploadedPop.storageProvider || 'supabase',
                    status: 'pending',
                    timestamp: serverTimestamp()
                });
                appendRecentEvent('Firestore payment record saved.');
            } catch (err) {
                console.error('[POP Upload] Firestore pending_payments write rejected:', err);
                throw new Error('Database rejected the payment record. This is usually caused by strict Firestore rules.');
            }

            try {
                updateUploadStage('Updating your Fundile profile...');
                appendRecentEvent('User profile update started.');
                await updateDoc(doc(db, 'users', currentUser.uid), {
                    paymentStatus: 'pending_review',
                    subscriptionStatus: currentUser.subscriptionStatus === 'active' ? 'active' : 'inactive',
                    hasUploadedPop: true,
                    lastPaymentSubmittedAt: serverTimestamp(),
                    paymentReference: referenceId,
                    lastPaymentReference: referenceId,
                    lastRequestedGrade: targetGrade || null,
                    lastApprovedPaymentId: currentUser.lastApprovedPaymentId || null,
                    latestPendingPaymentId: paymentDoc.id
                });
                appendRecentEvent('User profile updated.');
            } catch (err) {
                console.error('[POP Upload] Firestore users update rejected:', err);
                throw new Error('Payment saved, but failed to update your user profile.');
            }

            syncUploadProgress(100);
            updateUploadStage('Submission received and awaiting review.');
            syncUploadStatus('success');
        } catch (error) {
            console.error(`[POP Upload] Failed during ${uploadStageRef.current}`, error);
            setErrorMessage(error?.message || 'Submission failed after the POP upload completed. Please try again.');
            appendRecentEvent(`Submission failed during ${uploadStageRef.current}.`);
            updateUploadStage('Submission failed after the POP upload completed. Please try again.');
            syncUploadStatus('submit_error');
        } finally {
            clearUploadTimeout();
            clearActiveUploadRequest();
        }
    };

    if (compact) {
        return (
            <div className="w-full">
                <input ref={resolvedFileInputRef} type="file" className="hidden" accept=".pdf,image/png,image/jpeg" onChange={handleFileChange} disabled={isBusy || isPendingReview} />
                <div className={`overflow-hidden transition-all duration-300 ${shouldShowCompactPanel ? 'max-h-80 opacity-100' : 'max-h-0 opacity-0'}`}>
                    <div className="rounded-[28px] border border-sky-100 bg-white px-6 py-5 shadow-lg shadow-sky-100/40">
                        {isPendingReview ? (
                            <div className="flex flex-col items-center justify-center py-4">
                                <CheckCircle className="h-12 w-12 text-emerald-500 mb-3" />
                                <p className="text-sm font-semibold uppercase tracking-[0.2em] text-emerald-700">Awaiting Approval</p>
                                <p className="mt-2 text-center text-sm leading-7 text-slate-600">
                                    Your proof of payment has been received and is currently being reviewed by an administrator.
                                </p>
                            </div>
                        ) : (
                            <>
                                <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
                                    <div>
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-[#13519C]">Upload progress</p>
                                        <p className="mt-2 text-4xl font-bold text-[#13519C]">{visibleUploadProgress}%</p>
                                    </div>
                                    {file && status !== 'success' ? (
                                        <button
                                            type="button"
                                            onClick={handleUpload}
                                            disabled={!canSubmitUploadedPop || isBusy}
                                            className={`inline-flex items-center justify-center gap-2 rounded-2xl px-5 py-3 text-sm font-semibold text-white transition ${
                                                !canSubmitUploadedPop || isBusy
                                                    ? 'cursor-not-allowed bg-slate-300'
                                                    : 'bg-[#13519C] hover:bg-[#0f3e77]'
                                            }`}
                                        >
                                            {isUploading ? (
                                                <>
                                                    <Loader2 className="h-4 w-4 animate-spin" />
                                                    Uploading {visibleUploadProgress}%
                                                </>
                                            ) : isSubmitting ? (
                                                <>
                                                    <Loader2 className="h-4 w-4 animate-spin" />
                                                    Submitting
                                                </>
                                            ) : (
                                                'Submit POP'
                                            )}
                                        </button>
                                    ) : null}
                                </div>
                                <p className={`mt-3 text-sm leading-7 ${hasError ? 'text-red-700' : status === 'success' ? 'text-emerald-700' : 'text-slate-600'}`}>
                                    {status === 'success'
                                        ? 'POP upload complete.'
                                        : hasError
                                            ? errorMessage
                                            : isUploading || isSubmitting
                                                ? uploadStage
                                                : canSubmitUploadedPop
                                                    ? 'POP uploaded. Click Submit POP to send it for review.'
                                                    : file
                                                        ? uploadStage
                                                    : 'Choose a proof of payment file to continue.'}
                                </p>
                                {file && status !== 'success' ? (
                                    <div className="mt-2 flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
                                        <p className="break-all text-xs text-slate-500">{file.name}</p>
                                        <button
                                            type="button"
                                            onClick={handleRemoveSelectedFile}
                                            disabled={isBusy}
                                            className={`inline-flex items-center justify-center rounded-xl px-3 py-2 text-xs font-semibold transition ${
                                                isBusy
                                                    ? 'cursor-not-allowed text-slate-400'
                                                    : 'text-red-600 hover:bg-red-50'
                                            }`}
                                        >
                                            Remove file
                                        </button>
                                    </div>
                                ) : null}
                                {status === 'success' ? (
                                    <p className="mt-1 text-xs font-medium uppercase tracking-[0.2em] text-emerald-700">Ready for review</p>
                                ) : null}
                            </>
                        )}
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className={embedded ? 'w-full' : 'fixed inset-0 z-50 flex items-center justify-center p-4 bg-gray-900/60 backdrop-blur-sm'}>
            <div className={embedded ? 'w-full overflow-hidden rounded-[32px] border border-sky-100 bg-white shadow-[0_24px_80px_rgba(43,123,216,0.10)] flex flex-col' : 'bg-white rounded-2xl shadow-2xl w-full max-w-3xl overflow-hidden flex flex-col max-h-[90vh]'}>
                
                {/* Header */}
                <div className={`bg-gradient-to-r from-blue-600 to-indigo-700 px-6 py-4 flex justify-between items-start text-white shrink-0 gap-4 ${embedded ? 'sm:px-8 sm:py-5' : ''}`}>
                    <div className="flex flex-col gap-3">
                        <div className="flex items-center gap-3">
                            <GraduationCapSplash className="h-10 w-10" hideAccentSquares />
                            <span className="text-2xl font-bold tracking-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>fundile</span>
                        </div>
                        <div>
                            <h2 className="text-xl font-bold uppercase tracking-[0.2em]">{embedded ? 'Proof of Payment Upload' : 'Subscription'}</h2>
                            <p className="text-sm text-white/85">{embedded ? 'Finish your EFT submission here using the payment reference shown above.' : `Payment for Grade ${targetGrade} Access`}</p>
                        </div>
                    </div>
                    {!embedded && (
                        <button onClick={isUploading ? undefined : onClose} disabled={isUploading} className={`p-1 rounded-full transition-colors ${isUploading ? 'cursor-not-allowed opacity-60' : 'hover:bg-white/20'}`}>
                            <X size={24} />
                        </button>
                    )}
                </div>

                {/* Scrollable Content */}
                <div className={`w-full ${embedded ? 'p-6 sm:p-8' : 'p-6 overflow-y-auto'}`}>
                    {isPendingReview ? (
                        <div className="py-2">
                            <div className="rounded-3xl border border-emerald-100 bg-emerald-50/70 p-6">
                                <div className="flex flex-col items-center text-center">
                                    <CheckCircle className="w-16 h-16 text-emerald-500 mb-4" />
                                    <h3 className="text-2xl font-bold text-gray-800 mb-2">Awaiting Approval</h3>
                                    <p className="max-w-2xl text-gray-600">
                                        Your proof of payment has been received and is currently being reviewed by an administrator.
                                    </p>
                                </div>
                                <div className="mt-6 flex justify-center">
                                    {onClose ? (
                                        <button
                                            onClick={onClose}
                                            className="px-8 py-3 bg-indigo-600 text-white rounded-full font-semibold hover:bg-indigo-700 transition"
                                        >
                                            {embedded ? 'Back to dashboard' : 'Continue Exploring'}
                                        </button>
                                    ) : null}
                                </div>
                            </div>
                        </div>
                    ) : status === 'success' ? (
                        <div className="py-2">
                            <div className="rounded-3xl border border-emerald-100 bg-emerald-50/70 p-6">
                                <div className="flex flex-col items-center text-center">
                                    <CheckCircle className="w-16 h-16 text-emerald-500 mb-4" />
                                    <h3 className="text-2xl font-bold text-gray-800 mb-2">Proof of payment submitted successfully</h3>
                                    <p className="max-w-2xl text-gray-600">
                                        Fundile has received your Standard package proof of payment. Your submission is now awaiting review, and your subscription status will be updated once the EFT has been confirmed.
                                    </p>
                                </div>
                                <div className="mt-6 grid gap-4 md:grid-cols-2">
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Package</p>
                                        <p className="mt-2 text-base font-semibold text-gray-900">{selectedPlanLabel}</p>
                                    </div>
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Reference used</p>
                                        <p className="mt-2 break-all font-mono text-sm font-semibold text-gray-900">{referenceId}</p>
                                    </div>
                                </div>
                                <div className="mt-6 rounded-2xl bg-white p-4 shadow-sm">
                                    <div className="flex items-start gap-3">
                                        <ShieldCheck className="mt-0.5 h-5 w-5 text-indigo-600" />
                                        <div>
                                            <p className="font-semibold text-gray-900">What happens next</p>
                                            <p className="mt-1 text-sm leading-6 text-gray-600">
                                                We will review the POP, confirm the EFT payment, and update your subscription access. If support asks for a resend, use the same payment reference above so we can match it quickly.
                                            </p>
                                        </div>
                                    </div>
                                </div>
                                <div className="mt-6 flex justify-center">
                                    {onClose ? (
                                        <button
                                            onClick={onClose}
                                            className="px-8 py-3 bg-indigo-600 text-white rounded-full font-semibold hover:bg-indigo-700 transition"
                                        >
                                            {embedded ? 'Back to dashboard' : 'Continue Exploring'}
                                        </button>
                                    ) : null}
                                </div>
                            </div>
                        </div>
                    ) : (
                        <div className="space-y-6">
                            {currentUser?.paymentStatus === 'pending_review' && (
                                <div className="rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-800">
                                    We already show a POP under review on your profile. Upload another one only if you were asked to resubmit or your previous file was incorrect.
                                </div>
                            )}
                            
                            {/* Banking Details */}
                            <div className="rounded-2xl border border-blue-100 bg-blue-50/70 p-5 text-sm text-gray-700">
                                <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
                                    <div>
                                        <h3 className="font-semibold text-blue-900 text-base">Fundile Banking Details</h3>
                                        <p className="mt-1 text-sm text-blue-900/80">Use these details for the EFT, then upload the proof of payment in this section.</p>
                                    </div>
                                    <div className="rounded-2xl bg-white px-4 py-3 text-sm text-slate-700 shadow-sm">
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Payment flow</p>
                                        <p className="mt-2">Pay by EFT, upload the proof, then wait for review confirmation.</p>
                                    </div>
                                </div>
                                <div className="mt-4 grid gap-3 md:grid-cols-2 xl:grid-cols-4">
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Bank</p>
                                        <p className="mt-2 font-semibold text-gray-900">Access Bank</p>
                                    </div>
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <div className="flex items-start justify-between gap-3">
                                            <div>
                                                <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Account number</p>
                                                <p className="mt-2 font-semibold text-gray-900">51622451787</p>
                                            </div>
                                            <button type="button" onClick={() => handleCopy('51622451787', 'Account number')} className="rounded-full border border-gray-200 p-2 text-gray-500 transition hover:border-indigo-300 hover:text-indigo-600">
                                                <Copy className="h-4 w-4" />
                                            </button>
                                        </div>
                                    </div>
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <div className="flex items-start justify-between gap-3">
                                            <div>
                                                <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Branch code</p>
                                                <p className="mt-2 font-semibold text-gray-900">410506</p>
                                            </div>
                                            <button type="button" onClick={() => handleCopy('410506', 'Branch code')} className="rounded-full border border-gray-200 p-2 text-gray-500 transition hover:border-indigo-300 hover:text-indigo-600">
                                                <Copy className="h-4 w-4" />
                                            </button>
                                        </div>
                                    </div>
                                    <div className="rounded-2xl bg-white p-4 shadow-sm">
                                        <div className="flex items-start justify-between gap-3">
                                            <div>
                                                <p className="text-xs font-semibold uppercase tracking-[0.2em] text-gray-500">Reference to use</p>
                                                <p className="mt-2 break-all font-mono text-sm font-semibold text-gray-900">{referenceId}</p>
                                            </div>
                                            <button type="button" onClick={() => handleCopy(referenceId, 'Reference')} className="rounded-full border border-gray-200 p-2 text-gray-500 transition hover:border-indigo-300 hover:text-indigo-600">
                                                <Copy className="h-4 w-4" />
                                            </button>
                                        </div>
                                    </div>
                                </div>
                                {copyFeedback && <p className="mt-3 text-sm font-medium text-indigo-700">{copyFeedback}</p>}
                            </div>

                            <div>
                                <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-2">Choose Your Package</h3>
                                <p className="mb-3 text-sm text-gray-600">Standard is the active EFT package. Pro is still marked coming soon.</p>
                                <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                                    <div className="rounded-xl border-2 border-indigo-600 bg-indigo-50 p-4">
                                        <div className="flex items-start justify-between gap-3">
                                            <div>
                                                <div className="text-xs font-semibold uppercase tracking-wider text-indigo-600">Live now</div>
                                                <div className="text-lg font-bold text-indigo-900">Standard</div>
                                            </div>
                                            <span className="rounded-full bg-indigo-100 px-2 py-1 text-[10px] font-bold uppercase tracking-wide text-indigo-700">EFT enabled</span>
                                        </div>
                                        <p className="mt-3 text-sm leading-6 text-gray-600">
                                            Access all available subjects in the selected grade, with automatic rollover into the next grade when the active subscription overlaps the new year.
                                        </p>
                                        <div className="mt-4 flex flex-wrap gap-2 text-xs font-semibold text-indigo-700">
                                            <span className="rounded-full bg-white px-3 py-1">R150 monthly</span>
                                            <span className="rounded-full bg-white px-3 py-1">R1600 yearly</span>
                                        </div>
                                    </div>
                                    <button
                                        type="button"
                                        onClick={() => setShowProComingSoon(true)}
                                        className="rounded-xl border-2 border-dashed border-violet-200 bg-gray-50 p-4 text-left transition hover:border-violet-300 hover:bg-violet-50/60"
                                    >
                                        <div className="flex items-start justify-between gap-3">
                                            <div>
                                                <div className="text-xs font-semibold uppercase tracking-wider text-violet-600">Unavailable</div>
                                                <div className="text-lg font-bold text-gray-800">Pro</div>
                                            </div>
                                            <span className="rounded-full bg-violet-100 px-2 py-1 text-[10px] font-bold uppercase tracking-wide text-violet-700">Coming soon</span>
                                        </div>
                                        <p className="mt-3 text-sm leading-6 text-gray-600">
                                            Planned to include an LLM connection that can provide running comments on student questions, answers, and procedures.
                                        </p>
                                        <div className="mt-4 flex flex-wrap gap-2 text-xs font-semibold text-violet-700">
                                            <span className="rounded-full bg-white px-3 py-1">R299 monthly</span>
                                            <span className="rounded-full bg-white px-3 py-1">R3100 yearly</span>
                                        </div>
                                    </button>
                                </div>
                            </div>

                            <div>
                                <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-2">Select Your Standard Billing Plan</h3>
                                <p className="mb-3 text-sm text-gray-600">Choose the Standard package duration for EFT payment.</p>
                                <div className="grid grid-cols-2 gap-3">
                                    <button 
                                        onClick={() => setSelectedPlan('monthly')}
                                        disabled={isPlanLocked}
                                        className={`border-2 rounded-xl p-3 text-center transition-all ${
                                            selectedPlan === 'monthly' ? 'border-indigo-600 bg-indigo-50 ring-2 ring-indigo-200' : 'border-gray-200 hover:border-indigo-300 bg-gray-50'
                                        }`}
                                    >
                                        <div className={`font-bold text-lg ${selectedPlan === 'monthly' ? 'text-indigo-700' : 'text-gray-700'}`}>R150</div>
                                        <div className="text-xs font-medium text-gray-500">1 Month</div>
                                    </button>
                                    
                                    <button 
                                        onClick={() => setSelectedPlan('yearly')}
                                        disabled={isPlanLocked}
                                        className={`border-2 rounded-xl p-3 text-center transition-all relative ${
                                            selectedPlan === 'yearly' ? 'border-indigo-600 bg-indigo-50 ring-2 ring-indigo-200' : 'border-gray-200 hover:border-indigo-300 bg-gray-50'
                                        }`}
                                    >
                                        <span className="absolute -top-2.5 -right-2 bg-emerald-500 text-white text-[10px] font-bold px-2 py-0.5 rounded-full shadow-sm">Save R200!</span>
                                        <div className={`font-bold text-lg ${selectedPlan === 'yearly' ? 'text-indigo-700' : 'text-gray-700'}`}>R1,600</div>
                                        <div className="text-xs font-medium text-gray-500">12 Months</div>
                                    </button>
                                </div>
                                <div className="mt-3 rounded-xl border border-indigo-100 bg-indigo-50/70 px-4 py-3 text-sm text-indigo-900">
                                    You are submitting Proof of Payment for <span className="font-semibold">{selectedPlanLabel}</span>.
                                </div>
                            </div>

                            {/* File Upload Area */}
                            <div>
                                <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-2">Upload Proof of Payment</h3>
                                <div className="mb-3 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 text-sm text-slate-600">
                                    Accepted files: <span className="font-semibold text-slate-800">{POP_FILE_REQUIREMENTS_LABEL}</span>. Upload the receipt, transfer confirmation, or POP generated by your bank.
                                </div>
                                <label className={`flex flex-col items-center justify-center w-full min-h-40 border-2 border-dashed rounded-xl bg-gray-50 transition-colors ${isBusy ? 'cursor-not-allowed border-indigo-200 bg-indigo-50/70' : 'cursor-pointer border-gray-300 hover:bg-gray-100 hover:border-indigo-400'}`}>
                                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                                        <UploadCloud className="w-8 h-8 mb-2 text-gray-400" />
                                        <p className="text-sm text-gray-600">
                                            {file ? (
                                                <span className="font-semibold text-indigo-600">{file.name}</span>
                                            ) : (
                                                <span><span className="font-semibold text-indigo-600">Click to upload</span> your POP</span>
                                            )}
                                        </p>
                                        <p className="mt-2 text-xs text-gray-500">{file ? `${formatFileSize(file.size)} · ${file.type || 'Unknown type'}` : POP_FILE_REQUIREMENTS_LABEL}</p>
                                    </div>
                                    <input type="file" className="hidden" accept=".pdf,image/png,image/jpeg" onChange={handleFileChange} disabled={isBusy} />
                                </label>
                                {file && (
                                    <div className="mt-3 rounded-2xl border border-gray-200 bg-white px-4 py-3 text-sm text-gray-700 shadow-sm">
                                        <div className="flex flex-col gap-2 sm:flex-row sm:items-center sm:justify-between">
                                            <span className="font-medium text-gray-900">Selected POP</span>
                                            <div className="flex items-center gap-3">
                                                <span className="text-gray-500">{formatFileSize(file.size)}</span>
                                                <button
                                                    type="button"
                                                    onClick={handleRemoveSelectedFile}
                                                    disabled={isBusy}
                                                    className={`rounded-xl px-3 py-1.5 text-xs font-semibold transition ${
                                                        isBusy
                                                            ? 'cursor-not-allowed text-gray-400'
                                                            : 'text-red-600 hover:bg-red-50'
                                                    }`}
                                                >
                                                    Remove file
                                                </button>
                                            </div>
                                        </div>
                                        <p className="mt-1 break-all font-semibold text-indigo-700">{file.name}</p>
                                    </div>
                                )}
                            </div>

                            <div className="rounded-2xl border border-indigo-100 bg-indigo-50/70 p-4">
                                <div className="flex items-center justify-between gap-4">
                                    <div>
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-indigo-600">Upload status</p>
                                        <p className="mt-2 text-sm font-semibold text-indigo-950">{uploadStage}</p>
                                    </div>
                                    <div className="text-right">
                                        <p className="text-2xl font-bold text-indigo-700">{visibleUploadProgress}%</p>
                                        <p className="text-xs text-indigo-700/80">Current progress</p>
                                    </div>
                                </div>
                                <div className="mt-4 h-2 overflow-hidden rounded-full bg-indigo-100">
                                    <div className="h-full rounded-full bg-indigo-600 transition-all duration-300" style={{ width: `${visibleUploadProgress > 0 ? Math.max(visibleUploadProgress, 4) : 0}%` }} />
                                </div>
                                {recentEvents.length > 0 && (
                                    <div className="mt-4 rounded-2xl bg-white/80 px-4 py-3">
                                        <p className="text-xs font-semibold uppercase tracking-[0.2em] text-slate-500">Latest checks</p>
                                        <div className="mt-2 space-y-2 text-sm text-slate-700">
                                            {recentEvents.map((eventMessage) => (
                                                <p key={eventMessage}>{eventMessage}</p>
                                            ))}
                                        </div>
                                    </div>
                                )}
                            </div>

                            {/* Error Box */}
                            {hasError && (
                                <div className="p-3 bg-red-50 border border-red-200 rounded-lg flex items-start gap-2 text-sm text-red-700">
                                    <AlertCircle className="shrink-0 w-5 h-5" />
                                    <span>{errorMessage}</span>
                                </div>
                            )}

                        </div>
                    )}
                </div>

                {/* Footer */}
                {status !== 'success' && (
                    <div className="bg-gray-50 px-6 py-4 border-t border-gray-100 flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between shrink-0">
                        <p className="text-sm text-gray-500">Uploads show live progress and now fail with a clear reason instead of hanging silently.</p>
                        <div className="flex justify-end">
                        {onClose ? (
                            <button
                                onClick={onClose}
                                className="px-4 py-2 text-gray-600 font-medium hover:text-gray-800 transition mr-4"
                                disabled={isBusy}
                            >
                                {embedded ? 'Return to dashboard' : 'Cancel'}
                            </button>
                        ) : null}
                        <button
                            onClick={handleUpload}
                            disabled={!canSubmitUploadedPop || isBusy}
                            className={`flex items-center gap-2 px-6 py-2 rounded-full font-semibold text-white shadow-md transition-all ${
                                !canSubmitUploadedPop || isBusy 
                                ? 'bg-indigo-300 cursor-not-allowed' 
                                : 'bg-indigo-600 hover:bg-indigo-700 hover:shadow-lg'
                            }`}
                        >
                            {isUploading ? (
                                <>
                                    <Loader2 className="w-5 h-5 animate-spin" /> Uploading {visibleUploadProgress}%
                                </>
                            ) : isSubmitting ? (
                                <>
                                    <Loader2 className="w-5 h-5 animate-spin" /> Submitting
                                </>
                            ) : (
                                'Submit Standard POP'
                            )}
                        </button>
                        </div>
                    </div>
                )}
            </div>
            {showProComingSoon && (
                <div className="fixed inset-0 z-[60] flex items-center justify-center bg-gray-900/60 p-4 backdrop-blur-sm">
                    <div className="w-full max-w-sm rounded-2xl bg-white p-6 shadow-2xl">
                        <h3 className="text-xl font-bold text-gray-900">Pro package</h3>
                        <p className="mt-3 text-sm leading-6 text-gray-600">
                            Coming soon, not yet available in South Africa.
                        </p>
                        <div className="mt-6 flex justify-end">
                            <button
                                type="button"
                                onClick={() => setShowProComingSoon(false)}
                                className="rounded-full bg-violet-600 px-5 py-2 text-sm font-semibold text-white transition hover:bg-violet-700"
                            >
                                Close
                            </button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
};
