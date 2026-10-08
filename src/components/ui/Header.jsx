import React, { useState, useMemo } from 'react';
import { Bell, LogOut, X, Smartphone, Users } from 'lucide-react';
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
            {/* Start 2-week Free Trial Button (if not already subscribed / active trial) */}
            {!hasActiveSubscription && (
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
