import { useState, useEffect } from 'react';
import { initializeApp } from 'firebase/app';
import { getAuth, onAuthStateChanged, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { getFirestore, doc, setDoc, getDoc, updateDoc } from 'firebase/firestore';
import { getStorage } from 'firebase/storage';
import { firebaseConfig } from '../constants/sourceDocuments';
import { OWNER_EMAILS } from '../app/constants/access';

const buildPaymentReference = (uid = '') => {
    const normalizedUid = String(uid).replace(/[^a-zA-Z0-9]/g, '').toUpperCase();
    return normalizedUid ? `FND-${normalizedUid.slice(0, 12)}` : 'FND-REF';
};

/** Check if Dec 1 auto-upgrade should trigger */
const shouldAutoUpgradeGrade = () => {
    const now = new Date();
    return now.getMonth() >= 11; // December = month 11
};

/** Check if subscription has expired */
const checkSubscriptionExpiry = (expiryValue, isOwner) => {
    if (isOwner) return false; // owners never expire
    if (!expiryValue) return true; // no expiry set = expired (no trial)
    // Handle Firestore Timestamp or Date or ISO string
    let expiryDate;
    if (expiryValue?.toDate) {
        expiryDate = expiryValue.toDate(); // Firestore Timestamp
    } else if (expiryValue instanceof Date) {
        expiryDate = expiryValue;
    } else {
        expiryDate = new Date(expiryValue);
    }
    if (isNaN(expiryDate.getTime())) return false;
    return new Date() > expiryDate;
};

/** Auto-upgrade: if Dec 1+ and max grade < 12, add next grade */
const getAutoUpgradedGrades = (subscribedGrades) => {
    if (!shouldAutoUpgradeGrade()) return null;
    if (!Array.isArray(subscribedGrades) || subscribedGrades.length === 0) return null;
    const maxGrade = Math.max(...subscribedGrades);
    if (maxGrade >= 12) return null;
    const nextGrade = maxGrade + 1;
    if (subscribedGrades.includes(nextGrade)) return null;
    return [...subscribedGrades, nextGrade];
};

const resolvePaymentStatus = (userData = {}, isOwner = false) => {
    if (isOwner) return 'approved';
    if (userData.paymentStatus) return userData.paymentStatus;
    if (userData.subscriptionExpiry && !checkSubscriptionExpiry(userData.subscriptionExpiry, false)) return 'approved';
    if (userData.hasUploadedPop) return 'pending_review';
    return 'not_submitted';
};

const resolveSubscriptionStatus = (userData = {}, isOwner = false) => {
    if (isOwner) return 'active';

    if (userData.subscriptionStatus) {
        if (userData.subscriptionStatus === 'active' && checkSubscriptionExpiry(userData.subscriptionExpiry, false)) {
            return 'expired';
        }

        return userData.subscriptionStatus;
    }

    if (!userData.subscriptionExpiry) {
        return 'inactive';
    }

    return checkSubscriptionExpiry(userData.subscriptionExpiry, false) ? 'expired' : 'active';
};

const buildSubscriptionFields = (isOwner = false, userData = {}) => ({
    paymentStatus: resolvePaymentStatus(userData, isOwner),
    subscriptionStatus: resolveSubscriptionStatus(userData, isOwner),
    hasUploadedPop: userData.hasUploadedPop ?? false,
    lastPaymentSubmittedAt: userData.lastPaymentSubmittedAt ?? null,
    lastPaymentReference: userData.lastPaymentReference ?? null,
    lastApprovedPaymentId: userData.lastApprovedPaymentId ?? null,
    lastRequestedGrade: userData.lastRequestedGrade ?? null
});

export const useAuthentication = () => {
    const [currentUser, setCurrentUser] = useState(null);
    const [authLoading, setAuthLoading] = useState(true);
    const [userRole, setUserRole] = useState(null);
    const [subscriptionExpired, setSubscriptionExpired] = useState(false);
    const [auth, setAuth] = useState(null);
    const [db, setDb] = useState(null);
    const [storage, setStorage] = useState(null);

    // Initialize Firebase only once on mount
    useEffect(() => {
        try {
            const app = initializeApp(firebaseConfig);
            const authInstance = getAuth(app);
            const dbInstance = getFirestore(app);
            const storageInstance = getStorage(app);
            
            
            setAuth(authInstance);
            setDb(dbInstance);
            setStorage(storageInstance);

            // Set up the authentication state change listener
            const unsubscribe = onAuthStateChanged(authInstance, async (user) => {
                if (user) {
                    try {
                        await user.reload();

                        const isOwner = OWNER_EMAILS.includes(user.email) && user.emailVerified === true;

                        // Get user document from Firestore
                        const userDoc = await getDoc(doc(dbInstance, 'users', user.uid));
                        if (userDoc.exists()) {
                            const userData = userDoc.data();
                            
                            // Immediately log out blocked or deleted users
                            if (userData.accountStatus === 'blocked' || userData.isDeleted) {
                                await signOut(authInstance);
                                setCurrentUser(null);
                                setUserRole(null);
                                setAuthLoading(false);
                                return;
                            }

                            const subscriptionFields = buildSubscriptionFields(isOwner, userData);
                            const resolvedPaymentReference = userData.paymentReference || buildPaymentReference(user.uid);
                            // Determine effective tier
                            const effectiveTier = isOwner ? 'owner' : (userData.tier || 'standard');

                            // Check subscription expiry
                            const expired = checkSubscriptionExpiry(userData.subscriptionExpiry, isOwner);
                            setSubscriptionExpired(expired);

                            const userPatch = {};
                            Object.entries(subscriptionFields).forEach(([key, value]) => {
                                if (userData[key] !== value) {
                                    userPatch[key] = value;
                                }
                            });

                            if (userData.paymentReference !== resolvedPaymentReference) {
                                userPatch.paymentReference = resolvedPaymentReference;
                            }

                            if (Object.keys(userPatch).length > 0) {
                                try {
                                    await updateDoc(doc(dbInstance, 'users', user.uid), userPatch);
                                } catch (e) {
                                    console.warn('Could not normalize subscriber fields:', e);
                                }
                            }

                            // Auto-upgrade grades on Dec 1+
                            let effectiveGrades = isOwner ? [7,8,9,10,11,12] : (userData.subscribedGrades || []);
                            if (!isOwner && !expired) {
                                const upgraded = getAutoUpgradedGrades(effectiveGrades);
                                if (upgraded) {
                                    effectiveGrades = upgraded;
                                    // Persist the upgrade to Firestore
                                    try {
                                        await updateDoc(doc(dbInstance, 'users', user.uid), { subscribedGrades: upgraded });
                                    } catch (e) {
                                        console.warn('Could not auto-upgrade grades:', e);
                                    }
                                }
                            }

                            setCurrentUser({
                                ...userData,
                                uid: user.uid,
                                email: user.email,
                                emailVerified: user.emailVerified,
                                isOwner,
                                isSuperAdmin: isOwner, // backward compat
                                tier: effectiveTier,
                                subscriptionExpired: expired,
                                subscribedGrades: effectiveGrades,
                                subscribedSubjects: isOwner ? ['all'] : (userData.subscribedSubjects || []),
                                paymentReference: resolvedPaymentReference,
                                ...subscriptionFields,
                                paymentStatus: subscriptionFields.paymentStatus,
                                subscriptionStatus: subscriptionFields.subscriptionStatus,
                                subscribedGrades: effectiveGrades,
                                subscribedSubjects: isOwner ? ['all'] : (userData.subscribedSubjects || [])
                            });
                            setUserRole(userData.role || 'student');
                        } else {
                            // Create new user document if it doesn't exist
                            const newUserData = {
                                email: user.email,
                                role: 'student',
                                createdAt: new Date(),
                                curriculum: null,
                                grade: null,
                                tier: isOwner ? 'owner' : 'standard',
                                subscribedGrades: isOwner ? [7,8,9,10,11,12] : [],
                                subscribedSubjects: isOwner ? ['all'] : [],
                                paymentReference: buildPaymentReference(user.uid),
                                subscriptionExpiry: null,
                                isOwner: isOwner,
                                ...buildSubscriptionFields(isOwner)
                            };
                            await setDoc(doc(dbInstance, 'users', user.uid), newUserData);
                            setCurrentUser({
                                uid: user.uid,
                                email: user.email,
                                emailVerified: user.emailVerified,
                                isOwner,
                                isSuperAdmin: isOwner, // backward compat
                                tier: isOwner ? 'owner' : 'standard',
                                subscribedGrades: isOwner ? [7,8,9,10,11,12] : [],
                                subscribedSubjects: isOwner ? ['all'] : [],
                                subscriptionExpired: false,
                                ...newUserData
                            });
                            setUserRole('student');
                        }
                    } catch (error) {
                        console.error('Error fetching user data:', error);
                        try {
                            await user.reload();
                        } catch (reloadError) {
                            console.error('Error reloading auth user:', reloadError);
                        }
                        const isOwner = OWNER_EMAILS.includes(user.email) && user.emailVerified === true;
                        setCurrentUser({
                            uid: user.uid,
                            email: user.email,
                            emailVerified: user.emailVerified,
                            isOwner,
                            isSuperAdmin: isOwner, // backward compat
                            paymentReference: buildPaymentReference(user.uid),
                            tier: isOwner ? 'owner' : 'standard',
                            paymentStatus: isOwner ? 'approved' : 'not_submitted',
                            subscriptionStatus: isOwner ? 'active' : 'inactive',
                            role: 'student'
                        });
                        setUserRole('student');
                    }
                } else {
                    setCurrentUser(null);
                    setUserRole(null);
                }
                setAuthLoading(false);
            });

            return () => unsubscribe();
        } catch (error) {
            console.error('Firebase initialization error:', error);
            setAuthLoading(false);
        }
    }, []); // Empty dependency array means this runs only once on mount

    const signUp = async (email, password, role = 'student') => {
        if (!auth || !db) {
            return { success: false, error: 'Firebase services not available' };
        }
        
        try {
            const userCredential = await createUserWithEmailAndPassword(auth, email, password);
            const user = userCredential.user;
            
            // Create user document in Firestore
            const userData = {
                email: user.email,
                role: role,
                createdAt: new Date(),
                curriculum: null,
                grade: null,
                tier: 'standard',
                subscribedGrades: [],
                subscribedSubjects: [],
                paymentReference: buildPaymentReference(user.uid),
                subscriptionExpiry: null,
                isOwner: false,
                ...buildSubscriptionFields(false)
            };
            await setDoc(doc(db, 'users', user.uid), userData);
            
            return { success: true, user: { uid: user.uid, email: user.email, ...userData } };
        } catch (error) {
            console.error('Sign up error:', error);
            return { success: false, error: error.message };
        }
    };

    const signIn = async (email, password) => {
        if (!auth || !db) {
            return { success: false, error: 'Firebase services not available' };
        }
        
        try {
            const userCredential = await signInWithEmailAndPassword(auth, email, password);
            return { success: true, user: userCredential.user };
        } catch (error) {
            console.error('Sign in error:', error);
            return { success: false, error: error.message };
        }
    };

    const refreshCurrentUser = async () => {
        if (!auth || !db || !auth.currentUser) {
            return { success: false, error: 'No authenticated user found' };
        }

        try {
            await auth.currentUser.reload();
            const user = auth.currentUser;
            const isOwner = OWNER_EMAILS.includes(user.email) && user.emailVerified === true;
            const userDoc = await getDoc(doc(db, 'users', user.uid));
            const userData = userDoc.exists() ? userDoc.data() : {};
            const subscriptionFields = buildSubscriptionFields(isOwner, userData);
            const resolvedPaymentReference = userData.paymentReference || buildPaymentReference(user.uid);
            const expired = checkSubscriptionExpiry(userData.subscriptionExpiry, isOwner);
            const effectiveTier = isOwner ? 'owner' : (userData.tier || 'standard');
            const effectiveGrades = isOwner ? [7,8,9,10,11,12] : (userData.subscribedGrades || []);
            const effectiveSubjects = isOwner ? ['all'] : (userData.subscribedSubjects || []);

            setSubscriptionExpired(expired);
            setCurrentUser({
                ...userData,
                uid: user.uid,
                email: user.email,
                emailVerified: user.emailVerified,
                isOwner,
                isSuperAdmin: isOwner,
                tier: effectiveTier,
                subscriptionExpired: expired,
                subscribedGrades: effectiveGrades,
                subscribedSubjects: effectiveSubjects,
                paymentReference: resolvedPaymentReference,
                ...subscriptionFields,
                paymentStatus: subscriptionFields.paymentStatus,
                subscriptionStatus: subscriptionFields.subscriptionStatus,
                subscribedGrades: effectiveGrades,
                subscribedSubjects: effectiveSubjects,
            });
            setUserRole(userData.role || 'student');

            return { success: true, user };
        } catch (error) {
            console.error('Refresh current user error:', error);
            return { success: false, error: error.message };
        }
    };

    const handleLogout = async () => {
        if (!auth) {
            return { success: false, error: 'Firebase services not available' };
        }
        
        try {
            await signOut(auth);
            return { success: true };
        } catch (error) {
            console.error('Logout error:', error);
            return { success: false, error: error.message };
        }
    };

    return {
        auth, // Return the Firebase Auth instance directly
        db,   // Return the Firestore instance directly
        storage,
        authService: { signUp, signIn, handleLogout },
        dbService: db,
        currentUser,
        authLoading,
        refreshCurrentUser,
        userRole,
        subscriptionExpired,
        handleLogout
    };
};
