import React, { useState, useEffect, useRef } from 'react';
import { Bell, Check, Flame, Trophy, BookOpen, AlertTriangle, X, CheckCheck } from 'lucide-react';

export default function NotificationBell({ userId = 'std_learner_01' }) {
  const [isOpen, setIsOpen] = useState(false);
  const [notifications, setNotifications] = useState([
    {
      id: 'notif_demo_1',
      title: 'Streak Reminder 🔥',
      message: 'You have a 5-day streak! Practice 1 problem today to keep your streak bonus.',
      type: 'streak_reminder',
      read: false,
      created_at: '10m ago',
    },
    {
      id: 'notif_demo_2',
      title: 'New Credential Unlocked! 📌',
      message: 'You earned the Subskill Pin for VAT Calculation Prodigy.',
      type: 'badge_unlocked',
      read: false,
      created_at: '1h ago',
    },
    {
      id: 'notif_demo_3',
      title: 'Class Assignment: Accounting CRJ',
      message: 'Mrs. Ndlovu assigned Grade 10 Cash Receipts Journal Exercise 4.',
      type: 'assignment_due',
      read: false,
      created_at: '3h ago',
    },
  ]);

  const dropdownRef = useRef(null);

  // Close dropdown on outside click
  useEffect(() => {
    function handleClickOutside(event) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target)) {
        setIsOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const unreadCount = notifications.filter(n => !n.read).length;

  const markAsRead = (id) => {
    setNotifications(prev => prev.map(n => n.id === id ? { ...n, read: true } : n));
  };

  const markAllAsRead = () => {
    setNotifications(prev => prev.map(n => ({ ...n, read: true })));
  };

  const getIcon = (type) => {
    switch (type) {
      case 'streak_reminder':
        return <Flame className="w-4 h-4 text-amber-400" />;
      case 'badge_unlocked':
        return <Trophy className="w-4 h-4 text-emerald-400" />;
      case 'assignment_due':
        return <BookOpen className="w-4 h-4 text-sky-400" />;
      default:
        return <Bell className="w-4 h-4 text-indigo-400" />;
    }
  };

  return (
    <div className="relative" ref={dropdownRef}>
      {/* Bell Button with Unread Badge */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="relative p-2 rounded-xl bg-slate-900/80 hover:bg-slate-800 border border-slate-800 hover:border-slate-700 text-slate-300 hover:text-white transition-all shadow-sm flex items-center justify-center"
        aria-label="Notifications"
      >
        <Bell className="w-4 h-4 md:w-5 md:h-5" />
        {unreadCount > 0 && (
          <span className="absolute -top-1 -right-1 w-4 h-4 bg-rose-500 text-white text-[10px] font-extrabold rounded-full flex items-center justify-center shadow-md animate-pulse">
            {unreadCount}
          </span>
        )}
      </button>

      {/* Notifications Dropdown Panel */}
      {isOpen && (
        <div className="absolute right-0 mt-2 w-80 md:w-96 bg-slate-900/95 border border-slate-800 rounded-2xl shadow-2xl backdrop-blur-md z-50 overflow-hidden animate-fadeIn">
          {/* Header */}
          <div className="p-3.5 border-b border-slate-800/80 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-sm font-bold text-white">Notifications</span>
              {unreadCount > 0 && (
                <span className="bg-sky-500/20 text-sky-300 text-[10px] font-bold px-2 py-0.5 rounded-full border border-sky-400/30">
                  {unreadCount} New
                </span>
              )}
            </div>
            {unreadCount > 0 && (
              <button
                onClick={markAllAsRead}
                className="text-[11px] text-sky-400 hover:text-sky-300 font-semibold flex items-center gap-1 transition-colors"
              >
                <CheckCheck className="w-3.5 h-3.5" />
                <span>Mark all read</span>
              </button>
            )}
          </div>

          {/* List */}
          <div className="max-h-80 overflow-y-auto divide-y divide-slate-800/60">
            {notifications.length === 0 ? (
              <div className="p-6 text-center text-xs text-slate-500">
                No notifications right now.
              </div>
            ) : (
              notifications.map((n) => (
                <div
                  key={n.id}
                  onClick={() => markAsRead(n.id)}
                  className={`p-3.5 flex items-start gap-3 transition-colors cursor-pointer ${
                    n.read ? 'bg-slate-900/40 opacity-75' : 'bg-slate-800/40 hover:bg-slate-800/70'
                  }`}
                >
                  <div className="mt-0.5 p-1.5 rounded-lg bg-slate-800 border border-slate-700/60 shrink-0">
                    {getIcon(n.type)}
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between gap-1">
                      <h4 className="text-xs font-bold text-slate-200 truncate">{n.title}</h4>
                      <span className="text-[10px] text-slate-500 shrink-0">{n.created_at}</span>
                    </div>
                    <p className="text-xs text-slate-400 mt-0.5 leading-relaxed">{n.message}</p>
                  </div>
                  {!n.read && (
                    <span className="w-2 h-2 rounded-full bg-sky-400 shrink-0 self-center"></span>
                  )}
                </div>
              ))
            )}
          </div>

          {/* Footer */}
          <div className="p-2.5 bg-slate-950/60 border-t border-slate-800/60 text-center">
            <span className="text-[10px] text-slate-500">Fundile Learning Notifications · Real-time Sync</span>
          </div>
        </div>
      )}
    </div>
  );
}
