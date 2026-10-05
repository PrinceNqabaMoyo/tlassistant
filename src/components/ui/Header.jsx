import React, { useState } from 'react';
import { Bell, LogOut, X, Smartphone, Users } from 'lucide-react';
import FundileLogo from './FundileLogo';
import InstallAppModal from './InstallAppModal';
import ProfilePhotoModal from '../profile/ProfilePhotoModal';
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
  onOpenPersonaSwitcher = null,
}) => {
  const [showNotifications, setShowNotifications] = useState(false);
  const [showLogoutConfirm, setShowLogoutConfirm] = useState(false);
  const [showInstallModal, setShowInstallModal] = useState(false);
  const [showProfilePhotoModal, setShowProfilePhotoModal] = useState(false);

  const unreadNotificationCount = studentNotifications.filter((notification) => !notification.isRead).length;
  const systemNoticeCount = pendingAssignments.length > 0 ? 1 : 0;
  const unreadCount = unreadNotificationCount + systemNoticeCount;

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
            <FundileLogo className="h-28 w-28 sm:h-48 sm:w-48 text-white" wordmarkColor="white" />
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

            {/* Switch Persona / Oversight Testing Cockpit Button */}
            {onOpenPersonaSwitcher && (
              <button
                type="button"
                onClick={onOpenPersonaSwitcher}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-amber-500/20 hover:bg-amber-500/35 text-amber-200 text-xs font-bold transition border border-amber-400/40 cursor-pointer shrink-0 shadow-xs"
                title="Switch Persona: 300 School Students, 100 Homeschoolers, 60 Teachers, 330 Parents"
              >
                <Users className="w-3.5 h-3.5 text-amber-300" />
                <span className="hidden md:inline">Switch Persona (400+ Mock)</span>
                <span className="md:hidden">Personas</span>
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
                      onClick={() => setShowProfilePhotoModal(true)}
                      className="group relative h-9 w-9 sm:h-10 sm:w-10 rounded-full ring-2 ring-white/40 hover:ring-[#FF9100] transition-all overflow-hidden flex items-center justify-center bg-white/20 text-white font-bold text-xs sm:text-sm shrink-0 cursor-pointer shadow-inner"
                      title="Update Profile Picture"
                    >
                      {userPhoto ? (
                        <img src={userPhoto} alt={currentUser.name || 'User'} className="h-full w-full object-cover" />
                      ) : (
                        <span>{userInitials}</span>
                      )}
                      <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity text-xs">
                        📸
                      </div>
                    </button>
                  );
                })()}

                <span className="text-white font-medium hidden md:inline text-xs sm:text-sm" style={{ fontFamily: 'Afacad, sans-serif' }}>
                  Welcome, {currentUser.name} ({currentUser.role})
                </span>

                {currentUser.isSuperAdmin && (
                  <div className="flex flex-col sm:flex-row items-end sm:items-center gap-1 sm:gap-2 lg:gap-3 justify-end flex-1 min-w-0">
                    {/* 5-Role Super Admin Switcher */}
                    <div className="flex flex-wrap items-center gap-1 sm:space-x-1.5 bg-white/10 rounded-full p-1 justify-end">
                      {[
                        { role: 'student', label: 'Student' },
                        { role: 'parent', label: 'Parent' },
                        { role: 'teacher', label: 'Teacher' },
                        { role: 'school', label: 'School' },
                        { role: 'admin', label: 'Super Admin' },
                      ].map((item) => (
                        <button
                          key={item.role}
                          type="button"
                          onClick={() => setSuperAdminMode && setSuperAdminMode(item.role)}
                          className={`px-2 sm:px-2.5 py-1 rounded-full text-[10px] sm:text-xs transition-colors cursor-pointer ${
                            superAdminMode === item.role
                              ? 'bg-white/30 text-white font-bold shadow-xs'
                              : 'text-white/80 hover:bg-white/20'
                          }`}
                        >
                          {item.label}
                        </button>
                      ))}
                    </div>

                    {/* Tier Switcher */}
                    <div className="flex flex-wrap items-center gap-0.5 sm:space-x-1.5 bg-purple-500/30 rounded-full p-1 justify-end">
                      <span className="hidden sm:inline px-2 text-[10px] font-medium uppercase tracking-[0.1em] text-white/70">Tier:</span>
                      <button
                        type="button"
                        onClick={() => setSuperAdminTier && setSuperAdminTier('standard')}
                        className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-xs transition-colors cursor-pointer ${
                          superAdminTier === 'standard'
                            ? 'bg-purple-500 text-white font-bold shadow-xs'
                            : 'text-white/80 hover:bg-purple-500/50'
                        }`}
                      >
                        <span className="sm:hidden">Std</span>
                        <span className="hidden sm:inline">Standard</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => setSuperAdminTier && setSuperAdminTier('pro')}
                        className={`px-2 sm:px-3 py-1 rounded-full text-[10px] sm:text-xs transition-colors cursor-pointer ${
                          superAdminTier === 'pro'
                            ? 'bg-purple-500 text-white font-bold shadow-xs'
                            : 'text-white/80 hover:bg-purple-500/50'
                        }`}
                      >
                        Pro
                      </button>
                    </div>
                  </div>
                )}

                {currentUser.role === 'student' && (
                  <div className="relative">
                    <button onClick={() => setShowNotifications(!showNotifications)} className="p-2 rounded-full hover:bg-white/20 text-white relative" title="Notifications">
                      <Bell className="h-5 w-5" />
                      {unreadCount > 0 && (
                        <span className="absolute -top-1 -right-1 flex min-h-5 min-w-5 items-center justify-center rounded-full bg-red-500 px-1 text-[10px] font-bold text-white ring-2 ring-[#13519C]">
                          {unreadCount > 9 ? '9+' : unreadCount}
                        </span>
                      )}
                    </button>
                    {showNotifications && (
                      <div className="absolute top-full right-0 mt-2 w-96 max-w-[calc(100vw-2rem)] rounded-2xl border border-gray-200 bg-white p-4 shadow-lg z-50">
                        <div className="mb-3 flex items-center justify-between gap-3">
                          <h3 className="font-medium text-gray-900">Notifications</h3>
                          <div className="flex items-center gap-2">
                            {unreadNotificationCount > 0 && (
                              <button
                                type="button"
                                onClick={() => onMarkAllNotificationsRead && onMarkAllNotificationsRead()}
                                className="rounded-full border border-slate-200 px-3 py-1 text-xs font-semibold text-slate-600 transition hover:border-slate-300 hover:bg-slate-50"
                              >
                                Mark all read
                              </button>
                            )}
                            <button
                              onClick={() => setShowNotifications(false)}
                              className="text-gray-400 hover:text-gray-600"
                            >
                              <X className="h-4 w-4" />
                            </button>
                          </div>
                        </div>

                        {studentNotifications.length === 0 && pendingAssignments.length === 0 ? (
                          <p className="text-gray-500 text-center py-4">No new notifications</p>
                        ) : (
                          <div className="space-y-3">
                            {studentNotifications.map((notification) => (
                              <button
                                key={notification.id}
                                type="button"
                                onClick={() => onMarkNotificationRead && onMarkNotificationRead(notification.id)}
                                className={`block w-full rounded-2xl border px-4 py-3 text-left transition ${notification.isRead ? 'border-slate-200 bg-slate-50' : 'border-blue-200 bg-blue-50/80'}`}
                              >
                                <div className="flex items-start justify-between gap-3">
                                  <div>
                                    <p className="text-sm font-semibold text-slate-900">{notification.title || 'Notification'}</p>
                                    <p className="mt-1 text-sm leading-6 text-slate-600">{notification.message}</p>
                                  </div>
                                  {!notification.isRead && <span className="mt-1 h-2.5 w-2.5 shrink-0 rounded-full bg-blue-500" />}
                                </div>
                                <div className="mt-2 flex items-center justify-between text-xs text-slate-500">
                                  <span className="uppercase tracking-[0.2em]">{notification.type || 'notice'}</span>
                                  <span>{formatNotificationDate(notification.createdAt)}</span>
                                </div>
                              </button>
                            ))}

                            {pendingAssignments.length > 0 && (
                              <div className="rounded-2xl border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-800">
                                Class assignments are not yet available in South Africa.
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    )}
                  </div>
                )}

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

      {/* Mount ProfilePhotoModal for taking/uploading profile photo */}
      <ProfilePhotoModal
        isOpen={showProfilePhotoModal}
        onClose={() => setShowProfilePhotoModal(false)}
      />
    </header>
  );
};

export default Header;
