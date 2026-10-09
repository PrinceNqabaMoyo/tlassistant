import React, { useState, useEffect } from 'react';
import { createUserWithEmailAndPassword, fetchSignInMethodsForEmail, sendEmailVerification, signInWithEmailAndPassword } from 'firebase/auth';
import { doc, setDoc } from 'firebase/firestore';
import { Loader2, Eye, EyeOff } from 'lucide-react';
import { canBypassSignupGradeRestriction, LIVE_SIGNUP_GRADES } from '../../app/constants/access';

// Curriculum shell structure for the signup form (South African National Curriculum only)
const curriculumShell = {
    'CAPS': {
        name: 'South African National Curriculum (CAPS)',
        description: 'The official national curriculum for South Africa.',
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
    
    const [isLogin, setIsLogin] = useState(true);
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
    const signupPasswordSatisfiesPolicy = passwordSatisfiesPolicy(password);

    useEffect(() => {
        setIsLogin(initialMode !== 'signup');
        setError('');
    }, [initialMode]);

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

        if (!isLogin && role === 'student' && !canUseRestrictedSignupGrades && !LIVE_SIGNUP_GRADES.includes(Number(selectedGrade))) {
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
                const userData = { name: trimmedName, email: normalizedEmail, role, paymentReference: buildPaymentReference(user.uid) };

                if (role === 'student') {
                    userData.curriculum = selectedCurriculum;
                    userData.grade = selectedGrade;
                    userData.popiaGuardianConsent = true;
                    userData.popiaConsentTimestamp = new Date().toISOString();
                }

                await setDoc(doc(db, 'users', user.uid), userData);

                try {
                    await sendEmailVerification(user);
                    setError('Account created. Please verify your email (check your inbox/spam), then sign in.');
                } catch (verificationError) {
                    setError('Account created, but verification email could not be sent. Please try signing in and resend verification from Firebase, or contact support.');
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
                                            <span>Curriculum: South African National Curriculum (CAPS)</span>
                                            <span className="text-[10px] bg-white px-2 py-0.5 rounded-full border border-blue-200 font-bold">100% CAPS</span>
                                        </div>

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
                                        {!canUseRestrictedSignupGrades && (
                                            <p className="text-xs text-slate-500">
                                                Public sign-up is currently open for Grade 10 and Grade 11 only.
                                            </p>
                                        )}
                                    </>
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
