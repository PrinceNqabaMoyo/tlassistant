import React from 'react';
import { ChevronLeft } from 'lucide-react';

import EnhancedMathKeypad from '../../components/EnhancedMathKeypad';
import AdminTokenUsageDisplay from '../../components/ui/AdminTokenUsageDisplay';
import MessageModal from '../../components/ui/MessageModal';
import Header from '../../components/ui/Header';

const BackButton = ({ navigationStack, onNavigateBack, currentView }) => {
  if (navigationStack.length <= 1 || currentView === 'curriculum') {
    return null;
  }

  return (
    <button
      onClick={onNavigateBack}
      className="fixed top-20 left-4 z-50 bg-white hover:bg-gray-100 text-gray-700 rounded-full p-3 shadow-lg border border-gray-200 transition-all duration-200 hover:shadow-xl"
      title="Go back"
    >
      <ChevronLeft className="h-6 w-6" />
    </button>
  );
};

export default function AppShell({ shellProps }) {
  const {
    brandPalette,
    children,
    currentUser,
    currentView,
    handleMathInput,
    isKeypadVisible,
    message,
    navigationStack,
    onCloseMessage,
    onMarkAllNotificationsRead,
    onMarkNotificationRead,
    onLogout,
    onNavigateBack,
    pendingAssignments,
    setBrandPalette,
    setSuperAdminMode,
    setIsKeypadVisible,
    studentNotifications,
    superAdminMode,
  } = shellProps;

  return (
    <div className="min-h-screen bg-gray-50 font-sans">
      <BackButton
        navigationStack={navigationStack}
        onNavigateBack={onNavigateBack}
        currentView={currentView}
      />
      <Header
        currentUser={currentUser}
        onLogout={onLogout}
        onMarkAllNotificationsRead={onMarkAllNotificationsRead}
        onMarkNotificationRead={onMarkNotificationRead}
        pendingAssignments={pendingAssignments}
        studentNotifications={studentNotifications}
        superAdminMode={superAdminMode}
        setSuperAdminMode={setSuperAdminMode}
        brandPalette={brandPalette}
        setBrandPalette={setBrandPalette}
      />
      <main className="max-w-7xl mx-auto">
        {children}
      </main>
      <EnhancedMathKeypad
        isVisible={isKeypadVisible}
        onClose={() => setIsKeypadVisible(false)}
        onKeyClick={handleMathInput}
      />
      <footer className="bg-white mt-12 border-t">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8 text-center text-gray-500">
          <p>&copy; {new Date().getFullYear()} Fundile. All rights reserved.</p>
        </div>
      </footer>
      <MessageModal message={message} onClose={onCloseMessage} />
      <AdminTokenUsageDisplay currentUser={currentUser} />
    </div>
  );
}
