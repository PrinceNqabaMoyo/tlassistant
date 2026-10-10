import React, { useState, useMemo } from 'react';
import { Bell, LogOut, X, Smartphone, Users, Mail } from 'lucide-react';
import { getAuth, sendEmailVerification } from 'firebase/auth';
import FundileLogo from './FundileLogo';
import InstallAppModal from './InstallAppModal';
import UserProfileModal from '../profile/UserProfileModal';
import MessageBoardModal from '../notifications/MessageBoardModal';
import studentStore from '../../services/studentStore';
import { isStandaloneApp } from '../../hooks/useCoreState';

const formatNotificationDate = (value) => {
  if (!value) {
    return 'Just now';
  }

  const dateValue = value?.toDate ? value.toDate() : new Date(value);
  if (Number.isNaN(dateValue.getTime())) {
    return 'Just now';
  }

  return dateValue.toLocaleDateString(undefined, { month: 'short', day: 'numeric' });
};

const isSubscriptionExpired = (expiryValue) => {
  if (!expiryValue) return true;
  let expiryDate;
  if (expiryValue?.toDate) {
    expiryDate = expiryValue.toDate();
  } else if (expiryValue instanceof Date) {
    expiryDate = expiryValue;
  } else {
    expiryDate = new Date(expiryValue);
  }
  if (isNaN(expiryDate.getTime())) return false;
  return new Date() > expiryDate;
};

const Header = ({
  currentUser,
  onLogout,
  onMarkAllNotificationsRead,
  onMarkNotificationRead,
  pendingAssignments = [],
  studentNotifications = [],
  superAdminMode,
  setSuperAdminMode,
  superAdminTier,
  setSuperAdminTier,
  onStartTrial,
  onNavigateToSubscription,
  onNavigateHome,
  onOpenPersonaSwitcher = null,
}) => {
  const [showNotifications, setShowNotifications] = useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);
  const [showInstallModal, setShowInstallModal] = useState(false);
  const [showProfileModal, setShowProfileModal] = useState(false);
  const [showMessageBoard, setShowMessageBoard] = useState(false);
  const [resendingEmail, setResendingEmail] = useState(false);
  const [emailResentSuccess, setEmailResentSuccess] = useState(false);
  const [isGraceBannerDismissed, setIsGraceBannerDismissed] = useState(false);

  const showVerificationGraceBanner = Boolean(
    currentUser &&
    !currentUser.emailVerified &&
    !currentUser.isSuperAdmin &&
    !currentUser.isOwner &&
    !isGraceBannerDismissed
  );

  const handleResendVerification = async () => {
    try {
      setResendingEmail(true);
      const auth = getAuth();
      if (auth.currentUser) {
        await sendEmailVerification(auth.currentUser);
        setEmailResentSuccess(true);
        setTimeout(() => setEmailResentSuccess(false), 5000);
      }
    } catch (err) {
      console.warn('Could not resend verification email:', err);
    } finally {
      setResendingEmail(false);
    }
  };

  const unreadMessageCount = useMemo(() => {
    try {
      return (studentStore.getValidMessages() || []).filter(m => !m.isRead).length;
    } catch {
      return 0;
    }
  }, [showMessageBoard]);
  const unreadNotificationCount = studentNotifications.filter((notification) => !notification.isRead).length;
  const systemNoticeCount = pendingAssignments.length > 0 ? 1 : 0;
  const unreadCount = unreadNotificationCount + systemNoticeCount + unreadMessageCount;

  const isStandalone = isStandaloneApp();
  const hasActiveSubscription = Boolean(
    currentUser?.isSuperAdmin ||
    currentUser?.isOwner ||
    currentUser?.subscriptionStatus === 'active' ||
    currentUser?.paymentStatus === 'approved' ||
    currentUser?.trialActive ||
    (currentUser?.subscriptionExpiry && !isSubscriptionExpired(currentUser.subscriptionExpiry))
  );

  const isTrialUser = Boolean(!currentUser?.isSuperAdmin && !currentUser?.isOwner && (currentUser?.paymentStatus === 'trial_active' || currentUser?.onboardingPlan === 'free_trial' || (currentUser?.subscriptionExpiry && !isSubscriptionExpired(currentUser.subscriptionExpiry) && currentUser?.paymentStatus !== 'approved')));
  
  const trialDaysLeft = useMemo(() => {
    if (!currentUser?.subscriptionExpiry) return 0;
    const expiry = currentUser.subscriptionExpiry?.toDate ? currentUser.subscriptionExpiry.toDate() : new Date(currentUser.subscriptionExpiry);
    const diff = expiry.getTime() - Date.now();
    return Math.max(0, Math.ceil(diff / (1000 * 60 * 60 * 24)));
  }, [currentUser?.subscriptionExpiry]);

  const handleTrialClick = () => {
    if (typeof onStartTrial === 'function') {
      onStartTrial();
    } else if (typeof onNavigateToSubscription === 'function') {
      onNavigateToSubscription();
    }
  };

  return (
    <header className="bg-[#13519C] shadow-md sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center space-x-3 shrink-0">
            {!isStandalone && typeof onNavigateHome === 'function' ? (
              <button
                type="button"
                onClick={onNavigateHome}
                className="cursor-pointer focus:outline-hidden transition hover:opacity-90 active:scale-98 text-left"
                title="Fundile Home - Back to Landing Page"
              >
                <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48 text-white" wordmarkColor="white" />
              </button>
            ) : (
              <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48 text-white" wordmarkColor="white" />
            )}
          </div>

          <div className="flex items-center space-x-2 sm:space-x-3">
            {/* Active 14-Day Free Trial Indicator (Grade-Scoped) */}
            {isTrialUser && trialDaysLeft > 3 && (
              <button
                type="button"
                onClick={() => typeof onNavigateToSubscription === 'function' && onNavigateToSubscription()}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-emerald-500/20 border border-emerald-400/40 text-emerald-100 text-xs font-bold cursor-pointer hover:bg-emerald-500/30 transition shadow-xs shrink-0"
                title="14-day free trial active. Click to view subscription passes."
              >
                <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
                <span className="hidden sm:inline">14-Day Free Trial • Grade {currentUser?.grade || 10} • </span>
                <span>{trialDaysLeft}d left</span>
              </button>
            )}

            {/* Trial Winding Down Alert (< 4 Days Left) */}
            {isTrialUser && trialDaysLeft <= 3 && trialDaysLeft > 0 && (
              <button
                type="button"
                onClick={() => typeof onNavigateToSubscription === 'function' && onNavigateToSubscription()}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-[#FF9100]/25 border border-orange-400/60 text-amber-200 text-xs font-bold cursor-pointer hover:bg-[#FF9100]/35 transition shadow-xs shrink-0 animate-pulse"
                title="Trial winding down! Click to extend your pass."
              >
                <span>⚠️ {trialDaysLeft} {trialDaysLeft === 1 ? 'day' : 'days'} left</span>
                <span className="bg-[#FF9100] text-white px-1.5 py-0.5 rounded text-[10px] font-extrabold ml-1 hidden sm:inline">Extend Pass →</span>
              </button>
            )}

            {/* Expired Trial Indicator */}
            {isTrialUser && trialDaysLeft === 0 && (
              <button
                type="button"
                onClick={() => typeof onNavigateToSubscription === 'function' && onNavigateToSubscription()}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-rose-600/30 border border-rose-400/60 text-rose-200 text-xs font-bold cursor-pointer hover:bg-rose-600/40 transition shadow-xs shrink-0"
                title="Trial concluded. Click to subscribe."
              >
                <span>Trial Expired • Activate Pass →</span>
              </button>
            )}

            {/* Fallback Start Trial Button if completely non-subscribed & no trial */}
            {!hasActiveSubscription && !isTrialUser && (
              <button
                type="button"
                onClick={handleTrialClick}
                className="inline-flex flex-col items-center justify-center px-3 py-1 rounded-xl bg-[#FF9100] hover:bg-[#e07f00] text-white text-xs font-bold shadow-md shadow-orange-950/20 transition hover:scale-105 cursor-pointer shrink-0 text-center leading-tight border border-orange-400/30"
                title="Start 2-week Free Trial"
              >
                <span className="text-[10px] font-semibold text-amber-100 leading-tight">Start 2-week</span>
                <span className="text-xs font-extrabold leading-tight">free trial</span>
              </button>
            )}

            {/* Install App Button (if NOT running as installed Standalone app) */}
            {!isStandalone && (
              <button
                type="button"
                onClick={() => setShowInstallModal(true)}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-white/15 hover:bg-white/25 text-white text-xs font-bold transition border border-white/20 cursor-pointer shrink-0"
                title="Install Fundile App on Phone or PC"
              >
                <Smartphone className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Install App</span>
              </button>
            )}

            {/* Super Admin Mock School Tester (Oversight Testing Only) */}
            {currentUser?.isSuperAdmin && onOpenPersonaSwitcher && (
              <button
                type="button"
                onClick={onOpenPersonaSwitcher}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/35 text-amber-200 text-xs font-bold transition border border-amber-400/40 cursor-pointer shrink-0 shadow-xs"
                title="Super Admin Mock School Testing: Switch between mock students, teachers, and parents"
              >
                <Users className="w-3.5 h-3.5 text-amber-300" />
                <span className="hidden md:inline">Mock School Tester</span>
                <span className="md:hidden">Mock</span>
              </button>
            )}

            {currentUser && (
              <>
                {/* Profile Photo Avatar Button */}
                {(() => {
                  const userPhoto = currentUser?.photoURL || (typeof window !== 'undefined' ? localStorage.getItem('fundile_user_photoURL') : null);
                  const userInitials = (currentUser?.name || currentUser?.displayName || 'FL')
                    .split(' ')
                    .filter(Boolean)
                    .map((n) => n[0])
                    .slice(0, 2)
                    .join('')
                    .toUpperCase();

                  return (
                    <button
                      type="button"
                      onClick={() => setShowProfileModal(true)}
                      className="group relative h-9 w-9 sm:h-10 sm:w-10 rounded-full ring-2 ring-white/40 hover:ring-[#FF9100] transition-all overflow-hidden flex items-center justify-center bg-white/20 text-white font-bold text-xs sm:text-sm shrink-0 cursor-pointer shadow-inner"
                      title="View & Edit Profile"
                    >
                      {userPhoto ? (
                        <img src={userPhoto} alt={currentUser.name || 'User'} className="h-full w-full object-cover" />
                      ) : (
                        <span>{userInitials}</span>
                      )}
                      <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity text-xs">
                        ⚙️
                      </div>
                    </button>
                  );
                })()}

                <button
                  type="button"
                  onClick={() => setShowProfileModal(true)}
                  className="text-white hover:text-blue-100 font-medium hidden md:inline text-xs sm:text-sm cursor-pointer transition"
                  style={{ fontFamily: 'Afacad, sans-serif' }}
                >
                  Welcome, {currentUser.name} ({currentUser.role})
                </button>

                <div className="relative">
                  <button
                    type="button"
                    onClick={() => setShowMessageBoard(true)}
                    className="p-2 rounded-full hover:bg-white/20 text-white relative cursor-pointer"
                    title="Message Board & Communications"
                  >
                    <Bell className="h-5 w-5" />
                    {unreadCount > 0 && (
                      <span className="absolute -top-1 -right-1 flex min-h-5 min-w-5 items-center justify-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white ring-2 ring-[#13519C]">
                        {unreadCount > 9 ? '9+' : unreadCount}
                      </span>
                    )}
                  </button>
                </div>

                <button onClick={() => setShowLogoutConfirm(true)} className="flex items-center space-x-2 bg-white/20 hover:bg-white/30 text-white rounded-full p-2" title="Logout">
                  <LogOut className="h-5 w-5" />
                </button>
              </>
            )}
          </div>
        </div>
      </div>

      {/* 48-Hour Email Verification Grace Banner */}
      {showVerificationGraceBanner && (
        <div className="bg-amber-500 text-slate-950 px-4 py-2 text-xs font-medium border-t border-amber-600/30 flex items-center justify-between gap-3 shadow-inner">
          <div className="flex items-center gap-2 overflow-hidden text-ellipsis">
            <span className="font-extrabold text-amber-950 shrink-0">✉️ Verify Email:</span>
            <span className="truncate">
              A verification link was sent to <strong className="font-bold underline decoration-amber-950/40">{currentUser.email}</strong>. You have full access during your 48-hour grace period.
            </span>
          </div>
          <div className="flex items-center gap-2 shrink-0">
            {emailResentSuccess ? (
              <span className="text-emerald-950 font-bold bg-amber-400 px-2 py-0.5 rounded text-[11px]">
                Link sent! Check spam folder ✓
              </span>
            ) : (
              <button
                type="button"
                onClick={handleResendVerification}
                disabled={resendingEmail}
                className="bg-amber-950 hover:bg-black text-amber-100 hover:text-white px-2.5 py-1 rounded-lg font-bold text-[11px] transition cursor-pointer disabled:opacity-50"
              >
                {resendingEmail ? 'Sending...' : 'Resend Link'}
              </button>
            )}
            <button
              type="button"
              onClick={() => setIsGraceBannerDismissed(true)}
              className="text-amber-950/80 hover:text-amber-950 p-1 cursor-pointer"
              title="Dismiss banner"
            >
              <X className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}

      {/* Logout Confirmation Modal */}
      {showLogoutConfirm && (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-[100] px-4">
          <div className="bg-white rounded-2xl p-6 max-w-sm w-full shadow-xl">
            <h3 className="text-xl font-bold text-gray-900 mb-2">Confirm Logout</h3>
            <p className="text-gray-600 mb-6">Are you sure you want to log out of your account?</p>
            <div className="flex justify-end space-x-3">
              <button
                onClick={() => setShowLogoutConfirm(false)}
                className="px-4 py-2 text-gray-700 font-semibold hover:bg-gray-100 rounded-xl transition-colors cursor-pointer"
              >
                Cancel
              </button>
              <button
                onClick={() => {
                  setShowLogoutConfirm(false);
                  if (onLogout) onLogout();
                }}
                className="px-4 py-2 bg-red-600 text-white font-semibold hover:bg-red-700 rounded-xl transition-colors cursor-pointer"
              >
                Log Out
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Mount InstallAppModal for 1-click / 1-tap installation */}
      <InstallAppModal
        isOpen={showInstallModal}
        onClose={() => setShowInstallModal(false)}
      />

      {/* Mount UserProfileModal for profile editing, parent links, and clean super admin switcher */}
      <UserProfileModal
        isOpen={showProfileModal}
        onClose={() => setShowProfileModal(false)}
        currentUser={currentUser}
        onLogout={onLogout}
        superAdminMode={superAdminMode}
        setSuperAdminMode={setSuperAdminMode}
        superAdminTier={superAdminTier}
        setSuperAdminTier={setSuperAdminTier}
        onOpenPersonaSwitcher={onOpenPersonaSwitcher}
      />

      {/* Mount MessageBoardModal */}
      {showMessageBoard && (
        <MessageBoardModal
          currentUser={currentUser}
          onClose={() => setShowMessageBoard(false)}
        />
      )}
    </header>
  );
};

export default Header;
