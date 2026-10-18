import React, { useState, useEffect } from 'react';
import { createUserWithEmailAndPassword, fetchSignInMethodsForEmail, sendEmailVerification, signInWithEmailAndPassword } from 'firebase/auth';
import { doc, setDoc } from 'firebase/firestore';
import { Loader2, Eye, EyeOff } from 'lucide-react';
import { canBypassSignupGradeRestriction, LIVE_SIGNUP_GRADES } from '../../app/constants/access';
import { getApprovedSchools, registerSchool, validateMasterPasskey, claimMasterPasskey, validateFacultyPasscode, bindTeacherToSchool } from '../../services/schoolEnrollmentService';

// Curriculum shell structure for the signup form (South African National Curriculum only)
const curriculumShell = {
    'CAPS': {
        name: 'South African National Curriculum',
        description: 'The official national curriculum standards for South Africa.',
        grades: [7, 8, 9, 10, 11, 12]
    }
};

const buildPaymentReference = (uid = '') => {
    const normalizedUid = String(uid).replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
    return normalizedUid ? `FND-${normalizedUid.slice(0, 12)}` : 'FND-REF';
};

const PASSWORD_POLICY_MESSAGE = 'Password must include at least 6 characters, with uppercase, lowercase, a number, and a special character.';

const passwordSatisfiesPolicy = (password = '') => /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{6,}$/.test(password);

const formatSignInMethod = (method) => {
    switch (method) {
        case 'password':
            return 'email and password';
        case 'google.com':
            return 'Google';
        case 'facebook.com':
            return 'Facebook';
        case 'github.com':
            return 'GitHub';
        case 'apple.com':
            return 'Apple';
        default:
            return method;
    }
};

const formatAuthError = async ({ auth, error, email, isLogin }) => {
    const code = error?.code || '';

    switch (code) {
        case 'auth/weak-password':
            return PASSWORD_POLICY_MESSAGE;
        case 'auth/email-already-in-use': {
            try {
                const methods = auth && email ? await fetchSignInMethodsForEmail(auth, email) : [];
                if (methods.length > 0) {
                    const readableMethods = methods.map(formatSignInMethod).join(' or ');
                    return `An account already exists for ${email}. Sign in using ${readableMethods} instead.`;
                }
            } catch (lookupError) {
                console.error('Error checking sign-in methods for duplicate email:', lookupError);
            }

            return `An account already exists for ${email}. Sign in instead or reset your password if you no longer remember it.`;
        }
        case 'auth/account-exists-with-different-credential': {
            try {
                const methods = auth && email ? await fetchSignInMethodsForEmail(auth, email) : [];
                if (methods.length > 0) {
                    const readableMethods = methods.map(formatSignInMethod).join(' or ');
                    return `This email is already linked to ${readableMethods}. Sign in with that method first, then complete any account linking from the authenticated flow.`;
                }
            } catch (lookupError) {
                console.error('Error checking sign-in methods for linked account conflict:', lookupError);
            }

            return 'This email is already linked to another sign-in method. Sign in with the existing method first, then link the account.';
        }
        case 'auth/invalid-email':
            return 'Enter a valid email address.';
        case 'auth/invalid-credential':
        case 'auth/user-not-found':
        case 'auth/wrong-password':
            return isLogin ? 'Incorrect email or password.' : 'We could not verify those account details.';
        case 'auth/too-many-requests':
            return 'Too many attempts were made. Please wait a moment and try again.';
        case 'auth/network-request-failed':
            return 'Connection failed. Please check your internet connection and try again.';
        default:
            return error?.message || 'Authentication failed. Please try again.';
    }
};

const AuthBackground = () => {
    const [isMobile, setIsMobile] = useState(window.innerWidth < 768);
    const [randomMobileIndex] = useState(() => Math.floor(Math.random() * 3));

    const desktopImage = '/backgrounds/desktop-bg.jpg';
    const mobileImages = [
        '/backgrounds/mobile-bg-1.jpg',
        '/backgrounds/mobile-bg-2.jpg',
        '/backgrounds/mobile-bg-3.jpg'
    ];

    useEffect(() => {
        const checkMobile = () => {
            setIsMobile(window.innerWidth < 768);
        };
        window.addEventListener('resize', checkMobile);
        return () => window.removeEventListener('resize', checkMobile);
    }, []);

    const getBackgroundImage = () => {
        return isMobile ? mobileImages[randomMobileIndex] : desktopImage;
    };

    return (
        <div className="fixed inset-0 overflow-hidden">
            {/* Background image layer */}
            <div
                className="absolute inset-0 z-0 bg-cover bg-center bg-no-repeat"
                style={{
                    backgroundImage: `url(${getBackgroundImage()})`,
                }}
            />

            {/* Slight dark overlay for readability */}
            <div className="absolute inset-0 z-10 bg-black/30" />

            {/* Stylish gradient overlay from bottom */}
            <div className="absolute inset-0 z-20 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
        </div>
    );
};

const AuthScreen = ({ auth, db, initialMode = 'signin', onToggleMode, onNavigateHome, onNavigateToSubscription, statusMessage = '' }) => {
    
    const [isLogin, setIsLogin] = useState(() => initialMode !== 'signup');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [name, setName] = useState('');
    const [role, setRole] = useState('student');
    const [selectedCurriculum, setSelectedCurriculum] = useState('CAPS');
    const [selectedGrade, setSelectedGrade] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [showConfirmPassword, setShowConfirmPassword] = useState(false);
    const [hasParentalConsent, setHasParentalConsent] = useState(false);
    const [onboardingPlan, setOnboardingPlan] = useState('free_trial');
    const [accountAffiliation, setAccountAffiliation] = useState('independent'); // 'independent' | 'school_linked'
    const availableSchools = getApprovedSchools();
    const [selectedSchool, setSelectedSchool] = useState(() => availableSchools[0]?.id || '');
    const [masterPass, setMasterPass] = useState('');
    const [masterPassValidation, setMasterPassValidation] = useState(null);
    const [teacherAffiliation, setTeacherAffiliation] = useState('institutional'); // 'institutional' | 'independent'
    const [teacherSchool, setTeacherSchool] = useState(() => availableSchools[0]?.id || '');
    const [teacherSubject, setTeacherSubject] = useState('Accounting');
    const [facultyPasscode, setFacultyPasscode] = useState('');
    const [facultyPassValidation, setFacultyPassValidation] = useState(null);
    const [adminSchoolName, setAdminSchoolName] = useState('');
    const [adminEmis, setAdminEmis] = useState('');
    const [adminProvince, setAdminProvince] = useState('KwaZulu-Natal');
    const [adminDistrict, setAdminDistrict] = useState('Pinetown District');
    const [adminBillingModel, setAdminBillingModel] = useState('bulk_prepaid');
    const [adminFacultyPasscode, setAdminFacultyPasscode] = useState('WHS-TEACH-2026');
    const signupPasswordSatisfiesPolicy = passwordSatisfiesPolicy(password);

    useEffect(() => {
        setIsLogin(initialMode !== 'signup');
        setError('');
    }, [initialMode]);

    useEffect(() => {
        const schools = getApprovedSchools();
        if (schools.length > 0) {
            if (!selectedSchool || !schools.some(s => s.id === selectedSchool)) {
                setSelectedSchool(schools[0].id);
            }
            if (!teacherSchool || !schools.some(s => s.id === teacherSchool)) {
                setTeacherSchool(schools[0].id);
            }
        }
    }, [isLogin, role, accountAffiliation, teacherAffiliation]);

    const canUseRestrictedSignupGrades = canBypassSignupGradeRestriction(email);
    const visibleGrades = canUseRestrictedSignupGrades
        ? curriculumShell[selectedCurriculum]?.grades || []
        : LIVE_SIGNUP_GRADES;

    const handleCurriculumChange = (event) => {
        setSelectedCurriculum(event.target.value || 'CAPS');
        setSelectedGrade('');
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        const normalizedEmail = email.trim().toLowerCase();
        const trimmedName = name.trim();

        if (!isLogin && password !== confirmPassword) {
            setError('Passwords do not match');
            return;
        }

        if (!isLogin && !signupPasswordSatisfiesPolicy) {
            setError(PASSWORD_POLICY_MESSAGE);
            return;
        }

        if (!isLogin && !trimmedName) {
            setError('Full name is required');
            return;
        }

        if (!isLogin && role === 'student' && accountAffiliation === 'school_linked') {
            const check = validateMasterPasskey(masterPass, selectedSchool);
            if (!check.valid) {
                setError(check.error || 'Please enter a valid School Master Pass key.');
                return;
            }
        }

        if (!isLogin && role === 'teacher' && teacherAffiliation === 'institutional') {
            const check = validateFacultyPasscode(facultyPasscode, teacherSchool);
            if (!check.valid) {
                setError(check.error || 'Please enter a valid Institutional Faculty Passcode.');
                return;
            }
        }

        if (!isLogin && role === 'school_admin') {
            if (!adminSchoolName.trim()) {
                setError('Official School Name is required to register an institution.');
                return;
            }
            if (!adminEmis.trim()) {
                setError('EMIS Number is required for official institutional registration.');
                return;
            }
        }

        if (!isLogin && role === 'student' && accountAffiliation === 'independent' && !canUseRestrictedSignupGrades && !LIVE_SIGNUP_GRADES.includes(Number(selectedGrade))) {
            setError('Fundile sign-up is currently limited to Grades 10 and 11.');
            return;
        }

        if (!isLogin && role === 'student' && !hasParentalConsent) {
            setError('Parental or legal guardian consent is required to register under South Africa POPIA Section 35.');
            return;
        }

        setLoading(true);
        try {
            if (isLogin) {
                await signInWithEmailAndPassword(auth, normalizedEmail, password);
            } else {
                const userCredential = await createUserWithEmailAndPassword(auth, normalizedEmail, password);
                const user = userCredential.user;
                const paymentRef = buildPaymentReference(user.uid);
                const isSchoolLinked = role === 'student' && accountAffiliation === 'school_linked';
                const passCheck = isSchoolLinked ? validateMasterPasskey(masterPass, selectedSchool) : null;
                const isTrial = !isSchoolLinked && role === 'student' && onboardingPlan === 'free_trial';
                const trialDays = 14;
                const trialExpiry = new Date(Date.now() + trialDays * 24 * 60 * 60 * 1000);
                const graceUntil = new Date(Date.now() + 48 * 60 * 60 * 1000);
                const numericGrade = passCheck?.grade ? Number(passCheck.grade) : (selectedGrade ? Number(selectedGrade) : 10);

                const userData = {
                    name: trimmedName,
                    email: normalizedEmail,
                    role,
                    paymentReference: paymentRef,
                    tier: 'standard',
                    onboardingPlan: isSchoolLinked ? 'school_institutional' : (role === 'teacher' ? 'educator_lms' : onboardingPlan),
                    createdAt: new Date().toISOString(),
                    emailVerificationGraceUntil: graceUntil.toISOString(),
                    subscribedGrades: [numericGrade],
                    subscribedSubjects: ['all'],
                };

                if (isSchoolLinked) {
                    claimMasterPasskey(masterPass, { name: trimmedName, email: normalizedEmail, uid: user.uid }, selectedSchool);
                    userData.accountAffiliation = 'school_linked';
                    userData.schoolId = selectedSchool;
                    userData.schoolName = passCheck?.school?.name || 'Westville High School';
                    userData.masterPassKey = masterPass;
                    userData.subscriptionStatus = 'active';
                    userData.paymentStatus = 'institutional_bulk_covered';
                    userData.subscriptionExpiry = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toISOString();
                    try {
                        localStorage.setItem('fundile_pending_subject_enrollment', 'true');
                    } catch (_) {}
                } else if (role === 'teacher' && teacherAffiliation === 'institutional') {
                    const facultyCheck = validateFacultyPasscode(facultyPasscode, teacherSchool);
                    userData.teacherAffiliation = 'institutional';
                    userData.isInstitutionalTeacher = true;
                    userData.schoolId = teacherSchool;
                    userData.schoolName = facultyCheck?.schoolName || 'Westville High School';
                    userData.facultyPasscode = facultyPasscode.toUpperCase();
                    userData.subject = teacherSubject;
                    userData.department = facultyCheck?.department || 'Commercial Sciences';
                    userData.subscriptionStatus = 'active';
                    userData.paymentStatus = 'institutional_faculty_active';
                    userData.subscriptionExpiry = new Date(Date.now() + 365 * 24 * 60 * 60 * 1000).toISOString();
                    bindTeacherToSchool(
                        { uid: user.uid, name: trimmedName, email: normalizedEmail },
                        facultyPasscode,
                        teacherSchool,
                        teacherSubject
                    );
                } else if (role === 'teacher') {
                    userData.teacherAffiliation = 'independent';
                    userData.isInstitutionalTeacher = false;
                    userData.subscriptionStatus = 'active';
                    userData.paymentStatus = 'educator_active';
                } else if (role === 'school_admin') {
                    const registeredSchool = registerSchool({
                        schoolId: adminSchoolName.toLowerCase().includes('westville') ? 'sch_westville_high' : undefined,
                        name: adminSchoolName.trim(),
                        emisNumber: adminEmis.trim(),
                        province: adminProvince,
                        district: adminDistrict.trim(),
                        billingModel: adminBillingModel,
                        facultyPasscode: adminFacultyPasscode.trim() || 'WHS-TEACH-2026'
                    });
                    userData.role = 'school_admin';
                    userData.schoolId = registeredSchool.id;
                    userData.schoolName = registeredSchool.name;
                    userData.emisNumber = registeredSchool.emisNumber;
                    userData.facultyPasscode = adminFacultyPasscode.trim() || 'WHS-TEACH-2026';
                    userData.isInstitutionalAdmin = true;
                    userData.billingModel = adminBillingModel;
                    userData.subscriptionStatus = 'pending_clearance';
                    userData.paymentStatus = 'pending_pop_upload';
                    userData.hasUploadedPop = false;
                    userData.subscriptionExpiry = null;
                } else if (isTrial) {
                    userData.subscriptionStatus = 'active';
                    userData.subscriptionExpiry = trialExpiry.toISOString();
                    userData.paymentStatus = 'trial_active';
                    userData.trialStartedAt = new Date().toISOString();
                } else {
                    userData.subscriptionStatus = 'inactive';
                    userData.subscriptionExpiry = null;
                    userData.paymentStatus = 'not_submitted';
                }

                if (role === 'student') {
                    userData.curriculum = selectedCurriculum;
                    userData.grade = String(numericGrade);
                    userData.popiaGuardianConsent = true;
                    userData.popiaConsentTimestamp = new Date().toISOString();
                }

                await setDoc(doc(db, 'users', user.uid), userData);

                const isTestEmail = email.endsWith('.test') || email.includes('fundile.test') || email.includes('@example.com');
                if (!isTestEmail) {
                    try {
                        await sendEmailVerification(user);
                    } catch (verificationError) {
                        console.warn('Could not send verification email immediately:', verificationError);
                    }
                } else {
                    console.info('[Auth] Simulated test email detected — bypassing outbound SMTP verification dispatch to avoid mailbox bounce.');
                }

                if (!isTrial && !isSchoolLinked && role !== 'teacher' && role !== 'school_admin' && onNavigateToSubscription) {
                    onNavigateToSubscription();
                }
            }
        } catch (err) {
            const friendlyError = await formatAuthError({
                auth,
                error: err,
                email: normalizedEmail,
                isLogin,
            });
            setError(friendlyError);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="relative min-h-screen">
            <AuthBackground />
            <div className="relative z-10 flex items-center justify-center min-h-screen py-12 px-4 sm:px-6 lg:px-8">
                <div className="max-w-md w-full space-y-8 bg-white/95 backdrop-blur-sm p-10 rounded-xl shadow-2xl border border-white/20">
                    <div className="flex items-center justify-between gap-3 text-sm">
                        <button
                            type="button"
                            onClick={onNavigateHome}
                            className="font-medium text-blue-600 hover:text-blue-500"
                        >
                            Home
                        </button>
                        <button
                            type="button"
                            onClick={onNavigateToSubscription}
                            className="font-medium text-blue-600 hover:text-blue-500"
                        >
                            Subscription
                        </button>
                    </div>
                    <div className="text-center">
                        <h2 className="text-3xl font-extrabold text-gray-900">
                            {isLogin ? 'Sign in to your account' : 'Create a new account'}
                        </h2>
                    </div>
                    <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
                        {!isLogin && (
                            <div className="space-y-4">
                                <input 
                                    id="name" 
                                    name="name" 
                                    type="text" 
                                    required 
                                    data-testid="input-signup-name"
                                    className="appearance-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm" 
                                    placeholder="Full Name" 
                                    value={name} 
                                    onChange={e => setName(e.target.value)} 
                                />

                                <select 
                                    id="role" 
                                    name="role" 
                                    value={role} 
                                    data-testid="select-signup-role"
                                    onChange={e => setRole(e.target.value)} 
                                    className="block w-full py-3 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm font-medium text-slate-800"
                                >
                                    <option value="student">Student / Learner</option>
                                    <option value="parent">Parent / Guardian</option>
                                    <option value="teacher">Teacher / Educator</option>
                                    <option value="school_admin">School Administrator</option>
                                </select>

                                {role === 'student' && (
                                    <>
                                        <div className="bg-blue-50/80 border border-blue-200/90 p-2.5 rounded-md text-xs text-[#13519C] font-semibold flex items-center justify-between">
                                            <span>Curriculum: South African National Curriculum</span>
                                            <span className="text-[10px] bg-white px-2 py-0.5 rounded-full border border-blue-200 font-bold">National Standards</span>
                                        </div>

                                        {/* Account Type: Independent vs. School-Linked */}
                                        <div className="space-y-2 pt-1 text-left">
                                            <label className="text-xs font-bold text-slate-700 block">
                                                Student Enrollment Type:
                                            </label>
                                            <div className="grid grid-cols-2 gap-2">
                                                <label className={`flex items-center gap-2 p-2.5 rounded-xl border cursor-pointer transition text-xs font-bold ${
                                                    accountAffiliation === 'independent'
                                                        ? 'bg-blue-50/80 border-[#13519C] text-[#13519C] ring-1 ring-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                                                }`}>
                                                    <input 
                                                        type="radio" 
                                                        name="accountAffiliation" 
                                                        value="independent" 
                                                        data-testid="radio-account-independent"
                                                        checked={accountAffiliation === 'independent'}
                                                        onChange={() => {
                                                            setAccountAffiliation('independent');
                                                            setMasterPassValidation(null);
                                                        }}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>Independent</span>
                                                </label>

                                                <label className={`flex items-center gap-2 p-2.5 rounded-xl border cursor-pointer transition text-xs font-bold ${
                                                    accountAffiliation === 'school_linked'
                                                        ? 'bg-blue-50/80 border-[#13519C] text-[#13519C] ring-1 ring-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                                                }`}>
                                                    <input 
                                                        type="radio" 
                                                        name="accountAffiliation" 
                                                        value="school_linked" 
                                                        data-testid="radio-account-school-linked"
                                                        checked={accountAffiliation === 'school_linked'}
                                                        onChange={() => setAccountAffiliation('school_linked')}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>School-Linked</span>
                                                </label>
                                            </div>
                                        </div>

                                        {/* School-Linked Inputs: School Dropdown & Master Pass Key */}
                                        {accountAffiliation === 'school_linked' ? (
                                            <div className="space-y-3 p-3 rounded-xl bg-slate-50 border border-slate-200/90 text-left">
                                                <div>
                                                    <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                        Select Approved School:
                                                    </label>
                                                    <select
                                                        value={selectedSchool}
                                                        data-testid="select-signup-school"
                                                        onChange={e => {
                                                            setSelectedSchool(e.target.value);
                                                            setMasterPassValidation(null);
                                                        }}
                                                        className="block w-full py-2.5 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-semibold text-slate-800"
                                                    >
                                                        {availableSchools.length === 0 ? (
                                                            <option value="">No registered schools available</option>
                                                        ) : (
                                                            availableSchools.map(sch => (
                                                                <option key={sch.id} value={sch.id}>
                                                                    {sch.name} ({sch.province})
                                                                </option>
                                                            ))
                                                        )}
                                                    </select>
                                                </div>

                                                <div>
                                                    <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                        Grade Master Pass Key:
                                                    </label>
                                                    <input
                                                        type="text"
                                                        placeholder="e.g. WHS-GR10-8421"
                                                        value={masterPass}
                                                        data-testid="input-school-master-pass"
                                                        onChange={e => {
                                                            const val = e.target.value.toUpperCase();
                                                            setMasterPass(val);
                                                            if (val.length >= 8) {
                                                                const check = validateMasterPasskey(val, selectedSchool);
                                                                setMasterPassValidation(check);
                                                                if (check.valid && check.grade) {
                                                                    setSelectedGrade(String(check.grade));
                                                                }
                                                            } else {
                                                                setMasterPassValidation(null);
                                                            }
                                                        }}
                                                        className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-mono font-bold uppercase text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                                    />

                                                    {masterPassValidation && masterPassValidation.valid ? (
                                                        <div data-testid="badge-master-pass-verified" className="mt-2 p-2 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-semibold flex items-center gap-1.5">
                                                            <span className="w-2 h-2 rounded-full bg-emerald-500 shrink-0" />
                                                            <span>✓ Grade {masterPassValidation.grade} Master Pass Verified • Institutional Subscription covered by {masterPassValidation.school?.name}</span>
                                                        </div>
                                                    ) : masterPass.length >= 8 ? (
                                                        <div className="mt-1.5 text-[11px] text-rose-600 font-medium">
                                                            Invalid or unclaimed passkey. Check your printed slip from your school.
                                                        </div>
                                                    ) : (
                                                        <div className="mt-1 text-[10px] text-slate-500">
                                                            Enter the single-use master pass provided on your school voucher slip.
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        ) : (
                                            /* Independent Learner Grade Selection */
                                            <select 
                                                id="grade" 
                                                name="grade" 
                                                value={selectedGrade}
                                                data-testid="select-signup-grade"
                                                onChange={e => setSelectedGrade(e.target.value)} 
                                                className="block w-full py-3 px-3 border border-gray-300 bg-white rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                                            >
                                                <option value="">Select Grade</option>
                                                {visibleGrades.map(grade => (
                                                    <option key={grade} value={grade}>Grade {grade}</option>
                                                ))}
                                            </select>
                                        )}
                                    </>
                                )}

                                {/* Onboarding Preference: 14-Day Free Trial vs. Direct EFT Subscription (For Independent Learners) */}
                                {role === 'student' && accountAffiliation === 'independent' && (
                                    <div className="space-y-2 pt-1 text-left">
                                        <label className="text-xs font-bold text-slate-700 block">
                                            Onboarding Preference:
                                        </label>
                                        <div className="space-y-2">
                                            <label className={`flex items-start gap-2.5 p-2.5 rounded-xl border cursor-pointer transition ${
                                                onboardingPlan === 'free_trial' 
                                                    ? 'bg-blue-50/80 border-[#13519C] ring-1 ring-[#13519C]' 
                                                    : 'bg-white border-slate-200 hover:bg-slate-50'
                                            }`}>
                                                <input 
                                                    type="radio" 
                                                    name="onboardingPlan" 
                                                    value="free_trial" 
                                                    data-testid="radio-plan-free-trial"
                                                    checked={onboardingPlan === 'free_trial'}
                                                    onChange={() => setOnboardingPlan('free_trial')}
                                                    className="mt-0.5 h-4 w-4 text-[#13519C] focus:ring-[#13519C]"
                                                />
                                                <div className="text-xs leading-snug">
                                                    <span className="font-bold text-slate-900 flex items-center gap-1.5">
                                                        <span>Start with 14-day free trial</span>
                                                        <span className="px-1.5 py-0.2 rounded-full bg-emerald-100 text-emerald-800 text-[10px] font-extrabold border border-emerald-200">Recommended</span>
                                                    </span>
                                                    <span className="text-slate-600 block mt-0.5 text-[11px]">
                                                        Immediate full access to all your Grade {selectedGrade || '10'} subjects • No card required upfront.
                                                    </span>
                                                </div>
                                            </label>

                                            <label className={`flex items-start gap-2.5 p-2.5 rounded-xl border cursor-pointer transition ${
                                                onboardingPlan === 'direct_subscription' 
                                                    ? 'bg-amber-50/80 border-[#FF9100] ring-1 ring-[#FF9100]' 
                                                    : 'bg-white border-slate-200 hover:bg-slate-50'
                                            }`}>
                                                <input 
                                                    type="radio" 
                                                    name="onboardingPlan" 
                                                    value="direct_subscription" 
                                                    data-testid="radio-plan-direct-sub"
                                                    checked={onboardingPlan === 'direct_subscription'}
                                                    onChange={() => setOnboardingPlan('direct_subscription')}
                                                    className="mt-0.5 h-4 w-4 text-[#FF9100] focus:ring-[#FF9100]"
                                                />
                                                <div className="text-xs leading-snug">
                                                    <span className="font-bold text-slate-900 block">
                                                        Skip trial &amp; proceed straight to subscription
                                                    </span>
                                                    <span className="text-slate-600 block mt-0.5 text-[11px]">
                                                        Select Term Pass (R349) / Monthly (R149) and submit EFT Proof of Payment.
                                                    </span>
                                                </div>
                                            </label>
                                        </div>
                                    </div>
                                )}

                                {/* Educator Specific Institutional Onboarding */}
                                {role === 'teacher' && (
                                    <>
                                        <div className="bg-emerald-50/80 border border-emerald-200/90 p-2.5 rounded-md text-xs text-emerald-800 font-semibold flex items-center justify-between">
                                            <span>National Curriculum Faculty Portal</span>
                                            <span className="text-[10px] bg-white px-2 py-0.5 rounded-full border border-emerald-200 font-bold">Grades 7–12</span>
                                        </div>

                                        {/* Educator Affiliation: Institutional vs. Independent Private Tutor */}
                                        <div className="space-y-2 pt-1 text-left">
                                            <label className="text-xs font-bold text-slate-700 block">
                                                Educator Affiliation:
                                            </label>
                                            <div className="grid grid-cols-2 gap-2">
                                                <label className={`flex items-center gap-2 p-2.5 rounded-xl border cursor-pointer transition text-xs font-bold ${
                                                    teacherAffiliation === 'institutional'
                                                        ? 'bg-blue-50/80 border-[#13519C] text-[#13519C] ring-1 ring-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                                                }`}>
                                                    <input 
                                                        type="radio" 
                                                        name="teacherAffiliation" 
                                                        value="institutional" 
                                                        data-testid="radio-teacher-institutional"
                                                        checked={teacherAffiliation === 'institutional'}
                                                        onChange={() => setTeacherAffiliation('institutional')}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>Institutional School</span>
                                                </label>

                                                <label className={`flex items-center gap-2 p-2.5 rounded-xl border cursor-pointer transition text-xs font-bold ${
                                                    teacherAffiliation === 'independent'
                                                        ? 'bg-blue-50/80 border-[#13519C] text-[#13519C] ring-1 ring-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                                                }`}>
                                                    <input 
                                                        type="radio" 
                                                        name="teacherAffiliation" 
                                                        value="independent" 
                                                        data-testid="radio-teacher-independent"
                                                        checked={teacherAffiliation === 'independent'}
                                                        onChange={() => {
                                                            setTeacherAffiliation('independent');
                                                            setFacultyPassValidation(null);
                                                        }}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>Private Tutor</span>
                                                </label>
                                            </div>
                                        </div>

                                        {/* Institutional Teacher Inputs: School, Subject, and Faculty Invite Code */}
                                        {teacherAffiliation === 'institutional' ? (
                                            <div className="space-y-3 p-3 rounded-xl bg-slate-50 border border-slate-200/90 text-left">
                                                <div>
                                                    <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                        Select Institutional School:
                                                    </label>
                                                    <select
                                                        value={teacherSchool}
                                                        data-testid="select-signup-teacher-school"
                                                        onChange={e => {
                                                            setTeacherSchool(e.target.value);
                                                            setFacultyPassValidation(null);
                                                        }}
                                                        className="block w-full py-2.5 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-semibold text-slate-800"
                                                    >
                                                        {availableSchools.length === 0 ? (
                                                            <option value="">No registered schools available</option>
                                                        ) : (
                                                            availableSchools.map(sch => (
                                                                <option key={sch.id} value={sch.id}>
                                                                    {sch.name} ({sch.province})
                                                                </option>
                                                            ))
                                                        )}
                                                    </select>
                                                </div>

                                                <div>
                                                    <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                        Primary Teaching Department:
                                                    </label>
                                                    <select
                                                        value={teacherSubject}
                                                        data-testid="select-signup-teacher-subject"
                                                        onChange={e => setTeacherSubject(e.target.value)}
                                                        className="block w-full py-2.5 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-semibold text-slate-800"
                                                    >
                                                        <option value="Accounting">Accounting (Commercial Sciences)</option>
                                                        <option value="Mathematics">Mathematics (STEM)</option>
                                                        <option value="Physical Sciences">Physical Sciences (Sciences)</option>
                                                        <option value="Business Studies">Business Studies (Commerce)</option>
                                                        <option value="EMS">EMS (Economic &amp; Management Sciences)</option>
                                                    </select>
                                                </div>

                                                <div>
                                                    <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                        School Faculty Passcode / Invite Token:
                                                    </label>
                                                    <input
                                                        type="text"
                                                        placeholder="e.g. WHS-TEACH-2026"
                                                        value={facultyPasscode}
                                                        data-testid="input-teacher-invite-code"
                                                        onChange={e => {
                                                            const val = e.target.value.toUpperCase();
                                                            setFacultyPasscode(val);
                                                            if (val.length >= 6) {
                                                                const check = validateFacultyPasscode(val, teacherSchool);
                                                                setFacultyPassValidation(check);
                                                            } else {
                                                                setFacultyPassValidation(null);
                                                            }
                                                        }}
                                                        className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-mono font-bold uppercase text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                                    />

                                                    {facultyPassValidation && facultyPassValidation.valid ? (
                                                        <div data-testid="badge-faculty-pass-verified" className="mt-2 p-2 rounded-lg bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px] font-semibold flex items-center gap-1.5">
                                                            <span className="w-2 h-2 rounded-full bg-emerald-500 shrink-0" />
                                                            <span>✓ Verified Faculty Passcode • {facultyPassValidation.schoolName} ({facultyPassValidation.department}) • Departmental Rosters Ready</span>
                                                        </div>
                                                    ) : facultyPasscode.length >= 6 ? (
                                                        <div className="mt-1.5 text-[11px] text-rose-600 font-medium">
                                                            Invalid faculty passcode for this school. Consult your Principal or HOD.
                                                        </div>
                                                    ) : (
                                                        <div className="mt-1 text-[10px] text-slate-500">
                                                            Enter the faculty passcode provided by your school administration or HOD.
                                                        </div>
                                                    )}
                                                </div>
                                            </div>
                                        ) : (
                                            <div className="p-3 rounded-xl bg-blue-50/60 border border-blue-200/80 text-left text-xs text-slate-700">
                                                <span className="font-bold text-[#13519C] block mb-1">Independent Private Educator</span>
                                                <span>You can create custom classes, invite learners directly with 6-character join codes, and generate exam-standard test papers.</span>
                                            </div>
                                        )}
                                    </>
                                )}

                                {/* School Administrator Institutional Registration Form */}
                                {role === 'school_admin' && (
                                    <div className="space-y-3 p-3.5 rounded-xl bg-slate-50 border border-slate-200/90 text-left">
                                        <div className="bg-[#13519C]/10 border border-[#13519C]/30 p-2.5 rounded-lg text-xs text-[#13519C] font-semibold flex items-center justify-between">
                                            <span>Institutional School Accreditation &amp; Governance</span>
                                            <span className="text-[10px] bg-white px-2 py-0.5 rounded-full border border-blue-200 font-bold">SASAMS Aligned</span>
                                        </div>

                                        <div>
                                            <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                Official School Name <span className="text-rose-500">*</span>:
                                            </label>
                                            <input
                                                type="text"
                                                placeholder="e.g. Westville High School"
                                                required
                                                value={adminSchoolName}
                                                data-testid="input-signup-school-name"
                                                onChange={e => setAdminSchoolName(e.target.value)}
                                                className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-semibold text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                            />
                                        </div>

                                        <div className="grid grid-cols-2 gap-2">
                                            <div>
                                                <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                    EMIS Number <span className="text-rose-500">*</span>:
                                                </label>
                                                <input
                                                    type="text"
                                                    placeholder="e.g. 500124892"
                                                    required
                                                    value={adminEmis}
                                                    data-testid="input-signup-school-emis"
                                                    onChange={e => setAdminEmis(e.target.value)}
                                                    className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-mono font-bold text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                                />
                                            </div>
                                            <div>
                                                <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                    Province:
                                                </label>
                                                <select
                                                    value={adminProvince}
                                                    data-testid="select-signup-school-province"
                                                    onChange={e => setAdminProvince(e.target.value)}
                                                    className="block w-full py-2 px-2.5 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-semibold text-slate-800"
                                                >
                                                    <option value="KwaZulu-Natal">KwaZulu-Natal</option>
                                                    <option value="Gauteng">Gauteng</option>
                                                    <option value="Western Cape">Western Cape</option>
                                                    <option value="Eastern Cape">Eastern Cape</option>
                                                    <option value="Free State">Free State</option>
                                                    <option value="Limpopo">Limpopo</option>
                                                    <option value="Mpumalanga">Mpumalanga</option>
                                                    <option value="North West">North West</option>
                                                    <option value="Northern Cape">Northern Cape</option>
                                                </select>
                                            </div>
                                        </div>

                                        <div>
                                            <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                District / Circuit:
                                            </label>
                                            <input
                                                type="text"
                                                placeholder="e.g. Pinetown District"
                                                value={adminDistrict}
                                                data-testid="input-signup-school-district"
                                                onChange={e => setAdminDistrict(e.target.value)}
                                                className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                            />
                                        </div>

                                        <div>
                                            <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                License &amp; Billing Model:
                                            </label>
                                            <div className="grid grid-cols-2 gap-2">
                                                <label className={`flex items-center gap-2 p-2 rounded-lg border cursor-pointer text-xs font-bold ${
                                                    adminBillingModel === 'bulk_prepaid'
                                                        ? 'bg-blue-50 border-[#13519C] text-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-600'
                                                }`}>
                                                    <input
                                                        type="radio"
                                                        name="adminBillingModel"
                                                        value="bulk_prepaid"
                                                        data-testid="radio-school-billing-bulk"
                                                        checked={adminBillingModel === 'bulk_prepaid'}
                                                        onChange={() => setAdminBillingModel('bulk_prepaid')}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>Institutional Bulk</span>
                                                </label>
                                                <label className={`flex items-center gap-2 p-2 rounded-lg border cursor-pointer text-xs font-bold ${
                                                    adminBillingModel === 'individual'
                                                        ? 'bg-blue-50 border-[#13519C] text-[#13519C]'
                                                        : 'bg-white border-slate-200 text-slate-600'
                                                }`}>
                                                    <input
                                                        type="radio"
                                                        name="adminBillingModel"
                                                        value="individual"
                                                        data-testid="radio-school-billing-individual"
                                                        checked={adminBillingModel === 'individual'}
                                                        onChange={() => setAdminBillingModel('individual')}
                                                        className="h-3.5 w-3.5 text-[#13519C]"
                                                    />
                                                    <span>Individual Learner</span>
                                                </label>
                                            </div>
                                        </div>

                                        <div>
                                            <label className="block text-[11px] font-bold text-slate-600 mb-1">
                                                Faculty Passcode (For your teachers):
                                            </label>
                                            <input
                                                type="text"
                                                placeholder="e.g. WHS-TEACH-2026"
                                                value={adminFacultyPasscode}
                                                data-testid="input-signup-faculty-passcode"
                                                onChange={e => setAdminFacultyPasscode(e.target.value.toUpperCase())}
                                                className="block w-full py-2 px-3 border border-gray-300 bg-white rounded-md shadow-xs text-xs font-mono font-bold uppercase text-slate-900 placeholder-slate-400 focus:outline-none focus:border-[#13519C]"
                                            />
                                            <p className="text-[10px] text-slate-500 mt-1">
                                                Your educators will enter this passcode to link with your school and inherit assigned class rosters.
                                            </p>
                                        </div>
                                    </div>
                                )}
                            </div>
                        )}

                        {/* Email and Password */}
                        <div className="space-y-4">
                            <input 
                                id="email-address" 
                                name="email" 
                                type="email" 
                                autoComplete="email" 
                                required 
                                data-testid={isLogin ? 'input-signin-email' : 'input-signup-email'}
                                className="appearance-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm" 
                                placeholder="Email address" 
                                value={email} 
                                onChange={e => setEmail(e.target.value)} 
                            />

                            <div className="relative">
                                <input 
                                    id="password" 
                                    name="password" 
                                    type={showPassword ? "text" : "password"}
                                    autoComplete={isLogin ? "current-password" : "new-password"} 
                                    required 
                                    data-testid={isLogin ? 'input-signin-password' : 'input-signup-password'}
                                    className="appearance-none relative block w-full px-3 py-3 pr-10 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm" 
                                    placeholder="Password" 
                                    value={password} 
                                    onChange={e => setPassword(e.target.value)} 
                                />
                                <button
                                    type="button"
                                    className="absolute inset-y-0 right-0 pr-3 flex items-center z-20 cursor-pointer hover:bg-gray-100 rounded-r-md transition-colors duration-200"
                                    onClick={() => setShowPassword(!showPassword)}
                                    style={{ minWidth: '40px', minHeight: '40px' }}
                                >
                                    {showPassword ? (
                                        <EyeOff className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                                    ) : (
                                        <Eye className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                                    )}
                                </button>
                            </div>

                            {!isLogin && (
                                <div className="relative">
                                    <input 
                                        id="confirmPassword" 
                                        name="confirmPassword" 
                                        type={showConfirmPassword ? "text" : "password"}
                                        autoComplete="new-password" 
                                        required 
                                        data-testid="input-signup-confirm-password"
                                        className="appearance-none relative block w-full px-3 py-3 pr-10 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500 focus:z-10 sm:text-sm" 
                                        placeholder="Confirm Password" 
                                        value={confirmPassword} 
                                        onChange={e => setConfirmPassword(e.target.value)} 
                                    />
                                    <button
                                        type="button"
                                        className="absolute inset-y-0 right-0 pr-3 flex items-center z-20 cursor-pointer hover:bg-gray-100 rounded-r-md transition-colors duration-200"
                                        onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                                        style={{ minWidth: '40px', minHeight: '40px' }}
                                    >
                                        {showConfirmPassword ? (
                                            <EyeOff className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                                        ) : (
                                            <Eye className="h-5 w-5 text-gray-400 hover:text-gray-600" />
                                        )}
                                    </button>
                                </div>
                            )}
                            {!isLogin && (
                                <p className="text-xs text-slate-500">
                                    Password policy: at least 6 characters with uppercase, lowercase, a number, and a special character.
                                </p>
                            )}

                            {!isLogin && role === 'student' && (
                                <div className="flex items-start gap-2.5 p-3 rounded-lg bg-blue-50/70 border border-blue-200/80 text-left mt-3">
                                    <input
                                        id="popia-consent"
                                        name="popiaConsent"
                                        type="checkbox"
                                        required
                                        data-testid="checkbox-popia-consent"
                                        checked={hasParentalConsent}
                                        onChange={(e) => setHasParentalConsent(e.target.checked)}
                                        className="mt-0.5 h-4 w-4 rounded border-gray-300 text-blue-600 focus:ring-blue-500 cursor-pointer"
                                    />
                                    <label htmlFor="popia-consent" className="text-xs text-slate-700 leading-snug cursor-pointer select-none">
                                        <span className="font-semibold text-slate-900">Parental / Guardian Consent (POPIA Sec 35):</span>{' '}
                                        I confirm that I am 18 years or older, OR that I have obtained explicit consent from my parent or legal guardian to create this educational learning account.
                                    </label>
                                </div>
                            )}
                        </div>

                        {statusMessage && <p className="text-sm text-emerald-700">{statusMessage}</p>}
                        {error && <p className="text-sm text-red-600">{error}</p>}

                        <button 
                            type="submit" 
                            data-testid="btn-auth-submit"
                            disabled={loading || (!isLogin && (password !== confirmPassword || !signupPasswordSatisfiesPolicy || (role === 'student' && (!selectedCurriculum || !selectedGrade || !hasParentalConsent))))} 
                            className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:bg-gray-400"
                        >
                            {loading ? <Loader2 className="h-5 w-5 animate-spin" /> : (isLogin ? 'Sign in' : 'Sign up')}
                        </button>
                    </form>

                    <div className="text-sm text-center">
                        <button 
                            data-testid="btn-toggle-auth-mode"
                            onClick={() => {
                                if (onToggleMode) {
                                    onToggleMode();
                                    return;
                                }

                                setIsLogin(!isLogin);
                            }} 
                            className="font-medium text-blue-600 hover:text-blue-500"
                        >
                            {isLogin ? "Don't have an account? Sign up" : 'Already have an account? Sign in'}
                        </button>
                    </div>

                    <div className="text-sm text-center text-gray-600">
                        <button
                            type="button"
                            onClick={onNavigateToSubscription}
                            className="font-medium text-blue-600 hover:text-blue-500"
                        >
                            View Fundile subscription and EFT details
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AuthScreen;
