import React, { useState, useEffect } from 'react';
import { 
  X, 
  Bell, 
  Send, 
  Clock, 
  Check, 
  Trash2, 
  Calendar, 
  Sparkles, 
  ShieldCheck, 
  MessageSquare,
  AlertCircle
} from 'lucide-react';
import studentStore from '../../services/studentStore';

/**
 * MessageBoardModal
 * Communication center for Fundile and authentic school educators.
 * 
 * Rules & Invariants:
 * - Displays active announcements from teachers, schools, and Fundile.
 * - Auto-deletes messages 3 days after the specified deadline (Item 9).
 * - Allows Teachers, School Admins, and Super Admins to broadcast messages.
 */
export default function MessageBoardModal({
  isOpen = false,
  onClose = () => {},
  currentUser = null,
}) {
  const [messages, setMessages] = useState([]);
  const [activeTab, setActiveTab] = useState('inbox'); // 'inbox' | 'compose'
  
  // Compose message state (for teachers / admins)
  const [senderName, setSenderName] = useState('');
  const [subjectTopic, setSubjectTopic] = useState('Accounting');
  const [messageText, setMessageText] = useState('');
  const [deadlineDate, setDeadlineDate] = useState('');
  const [dispatchStatus, setDispatchStatus] = useState(null);

  const isTeacherOrAdmin = Boolean(
    currentUser?.isSuperAdmin || 
    currentUser?.role === 'teacher' || 
    currentUser?.role === 'admin' || 
    currentUser?.role === 'school' || 
    currentUser?.role === 'school_admin'
  );

  const refreshMessages = () => {
    const valid = studentStore.getValidMessages();
    setMessages([...valid]);
  };

  useEffect(() => {
    if (isOpen) {
      refreshMessages();
      setSenderName(currentUser?.name || (isTeacherOrAdmin ? 'Classroom Educator' : 'Teacher'));
    }
  }, [isOpen, currentUser, isTeacherOrAdmin]);

  const handleMarkRead = (id) => {
    studentStore.markMessageRead(id);
    refreshMessages();
  };

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!messageText.trim()) return;

    studentStore.addMessage({
      sender: senderName.trim() || 'Educator',
      senderRole: currentUser?.role === 'admin' ? 'Super Admin' : currentUser?.role === 'school' ? 'School Admin' : 'Teacher',
      subject: subjectTopic,
      text: messageText.trim(),
      deadline: deadlineDate ? new Date(deadlineDate).toISOString() : null,
    });

    setMessageText('');
    setDeadlineDate('');
    setDispatchStatus('Message dispatched successfully to student message boards.');
    refreshMessages();
    setTimeout(() => {
      setDispatchStatus(null);
      setActiveTab('inbox');
    }, 1500);
  };

  if (!isOpen) return null;

  const unreadCount = messages.filter((m) => !m.isRead).length;

  return (
    <div 
      className="fixed inset-0 z-[130] flex items-center justify-center bg-black/60 backdrop-blur-xs p-3 sm:p-4 select-none animate-in fade-in duration-150"
      onClick={onClose}
    >
      <div 
        className="w-full max-w-lg bg-white rounded-3xl border border-slate-200 shadow-2xl overflow-hidden flex flex-col max-h-[85vh]"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="bg-[#13519C] text-white px-6 py-4 flex items-center justify-between shrink-0">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center border border-white/20 relative">
              <Bell className="w-5 h-5 text-[#FF9100]" />
              {unreadCount > 0 && (
                <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-500 text-[10px] font-bold text-white flex items-center justify-center ring-2 ring-[#13519C]">
                  {unreadCount}
                </span>
              )}
            </div>
            <div>
              <h3 className="text-lg font-bold text-white leading-tight" style={{ fontFamily: 'Afacad, sans-serif' }}>
                Message Board
              </h3>
              <p className="text-xs text-blue-200">
                Official communications from Fundile and your teachers
              </p>
            </div>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="p-1.5 rounded-full text-white/80 hover:text-white hover:bg-white/10 transition cursor-pointer"
            title="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Tab switcher if user is teacher or admin */}
        {isTeacherOrAdmin && (
          <div className="grid grid-cols-2 p-1.5 bg-slate-100 border-b border-slate-200 text-xs font-bold shrink-0">
            <button
              type="button"
              onClick={() => setActiveTab('inbox')}
              className={`py-2 rounded-xl transition cursor-pointer text-center ${
                activeTab === 'inbox'
                  ? 'bg-white text-[#13519C] shadow-xs'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Inbox Messages ({messages.length})
            </button>
            <button
              type="button"
              onClick={() => setActiveTab('compose')}
              className={`py-2 rounded-xl transition cursor-pointer text-center ${
                activeTab === 'compose'
                  ? 'bg-white text-[#13519C] shadow-xs'
                  : 'text-slate-600 hover:text-slate-900'
              }`}
            >
              Compose Broadcast ✍️
            </button>
          </div>
        )}

        {/* Body */}
        <div className="p-5 overflow-y-auto flex-1 font-sans space-y-3">
          {activeTab === 'compose' && isTeacherOrAdmin ? (
            /* COMPOSE TAB (Teachers & Admins) */
            <form onSubmit={handleSendMessage} className="space-y-4">
              <div className="p-3 bg-blue-50 border border-blue-200 rounded-2xl text-xs text-[#13519C]">
                💡 Messages sent here arrive on student message boards. Messages with deadlines auto-delete 3 days after the deadline.
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Sender Name / Title</label>
                <input
                  type="text"
                  value={senderName}
                  onChange={(e) => setSenderName(e.target.value)}
                  required
                  placeholder="e.g. Mrs. P. Khumalo"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-xs focus:ring-2 focus:ring-[#13519C]"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Subject</label>
                <select
                  value={subjectTopic}
                  onChange={(e) => setSubjectTopic(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-xs bg-white focus:ring-2 focus:ring-[#13519C]"
                >
                  <option value="Accounting">Accounting</option>
                  <option value="Mathematics">Mathematics</option>
                  <option value="Physical Sciences">Physical Sciences</option>
                  <option value="Business Studies">Business Studies</option>
                  <option value="Life Sciences">Life Sciences</option>
                  <option value="EMS">EMS</option>
                  <option value="School Notice">School Administration Notice</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Message Content</label>
                <textarea
                  rows={3}
                  value={messageText}
                  onChange={(e) => setMessageText(e.target.value)}
                  required
                  placeholder="e.g. Class task sent for Cash Receipts Journal, deadline Friday 17:00."
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-xs focus:ring-2 focus:ring-[#13519C]"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Task Deadline (Auto-expires 3 days after)</label>
                <input
                  type="datetime-local"
                  value={deadlineDate}
                  onChange={(e) => setDeadlineDate(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-xs bg-white"
                />
              </div>

              {dispatchStatus && (
                <div className="p-2.5 rounded-xl bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold">
                  ✓ {dispatchStatus}
                </div>
              )}

              <button
                type="submit"
                className="w-full py-2.5 rounded-xl bg-[#13519C] text-white font-bold text-xs hover:bg-[#0b376b] transition cursor-pointer flex items-center justify-center gap-2 shadow-md"
              >
                <Send className="w-3.5 h-3.5" />
                <span>Send Broadcast Message</span>
              </button>
            </form>
          ) : (
            /* INBOX TAB */
            messages.length === 0 ? (
              <div className="py-12 text-center space-y-2">
                <div className="w-12 h-12 rounded-full bg-slate-100 text-slate-400 mx-auto flex items-center justify-center">
                  <Bell className="w-6 h-6" />
                </div>
                <h4 className="text-sm font-bold text-slate-700">No Active Messages</h4>
                <p className="text-xs text-slate-500 max-w-xs mx-auto">
                  Your message board is up to date. Class task notices from teachers appear here.
                </p>
              </div>
            ) : (
              messages.map((msg) => (
                <div
                  key={msg.id}
                  onClick={() => handleMarkRead(msg.id)}
                  className={`p-4 rounded-2xl border transition-all cursor-pointer relative space-y-2 ${
                    msg.isRead
                      ? 'bg-white border-slate-200/90 hover:border-slate-300'
                      : 'bg-blue-50/70 border-blue-200 shadow-xs ring-1 ring-blue-100'
                  }`}
                >
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                      <span className="font-bold text-xs text-slate-900">{msg.sender}</span>
                      <span className="px-2 py-0.5 rounded-full bg-blue-100 text-[#13519C] text-[10px] font-extrabold">
                        {msg.subject}
                      </span>
                      {!msg.isRead && (
                        <span className="w-2 h-2 rounded-full bg-rose-500 animate-pulse" />
                      )}
                    </div>
                    <span className="text-[10px] text-slate-400 font-medium">
                      {msg.date}
                    </span>
                  </div>

                  <p className="text-xs text-slate-700 leading-relaxed font-normal">
                    {msg.text}
                  </p>

                  {msg.deadline && (
                    <div className="flex items-center justify-between pt-1 text-[10px] text-amber-800 border-t border-slate-100">
                      <span className="flex items-center gap-1 font-semibold">
                        <Clock className="w-3 h-3 text-amber-600" />
                        <span>Deadline: {new Date(msg.deadline).toLocaleDateString('en-ZA', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })}</span>
                      </span>
                      <span className="text-slate-400">
                        Auto-deletes 3 days post-deadline
                      </span>
                    </div>
                  )}
                </div>
              ))
            )
          )}
        </div>

        {/* Footer */}
        <div className="p-3.5 bg-slate-50 border-t border-slate-200 flex items-center justify-between text-xs text-slate-500 shrink-0">
          <span>POPIA Section 35 Protected Communications</span>
          <button
            type="button"
            onClick={onClose}
            className="px-4 py-1.5 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold transition cursor-pointer"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}
