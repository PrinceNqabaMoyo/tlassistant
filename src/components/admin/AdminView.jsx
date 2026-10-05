import React, { useEffect } from 'react';
import { AdminDashboard, PendingPayments, UserManagement, InterestSubmissions } from '../forms/AdminForms';
import SchoolAdminView from './SchoolAdminView';
import {
    SystemAnalyticsView,
    ContentManagementView,
    CompetitionSetupView,
    SystemSettingsView,
    SecurityAccessView
} from './SuperAdminPanels';

const AdminView = ({ view, setView, db, currentUser }) => { 
    const canManageSubscribers = !!(currentUser?.isOwner || currentUser?.isSuperAdmin);

    useEffect(() => {
        console.log('[AdminView] Current view state:', view);
    }, [view]);

    const handleNavigateDashboard = () => {
        console.log('[AdminView] Navigating back to dashboard from:', view);
        setView('dashboard');
    };

    const handleSelectView = (key) => {
        console.log('[AdminView] Selecting new view:', key);
        setView(key);
    };

    const renderAdminContent = () => { 
        switch(view) { 
            case 'user_management': 
            case 'userManagement':
                return <UserManagement currentUser={currentUser} db={db} onBack={handleNavigateDashboard} mode="general" />;
            case 'subscriberManagement':
                if (!canManageSubscribers) {
                    return <AdminDashboard setView={setView} onSelect={handleSelectView} currentUser={currentUser} db={db} />;
                }
                return <UserManagement currentUser={currentUser} db={db} onBack={handleNavigateDashboard} mode="subscriber" />;
            case 'class_management': 
            case 'classManagement':
                return <SchoolAdminView currentUser={currentUser} onBack={handleNavigateDashboard} />;
            case 'systemAnalytics':
                return <SystemAnalyticsView onBack={handleNavigateDashboard} />;
            case 'contentManagement':
                return <ContentManagementView onBack={handleNavigateDashboard} />;
            case 'competitionSetup':
                return <CompetitionSetupView onBack={handleNavigateDashboard} />;
            case 'systemSettings':
                return <SystemSettingsView onBack={handleNavigateDashboard} />;
            case 'securityAccess':
                return <SecurityAccessView onBack={handleNavigateDashboard} />;
            case 'eftApprovals':
                if (!canManageSubscribers) {
                    return <AdminDashboard setView={setView} onSelect={handleSelectView} currentUser={currentUser} db={db} />;
                }
                return <PendingPayments currentUser={currentUser} db={db} onBack={handleNavigateDashboard} />;
            case 'interestSubmissions':
                return <InterestSubmissions db={db} onBack={handleNavigateDashboard} />;
            case 'schoolAdmin':
                return <SchoolAdminView currentUser={currentUser} onBack={handleNavigateDashboard} />;
            case 'dashboard': 
            default: 
                return <AdminDashboard setView={setView} onSelect={handleSelectView} currentUser={currentUser} db={db} />; 
        } 
    }; 
    
    return <div>{renderAdminContent()}</div>; 
};

export default AdminView;
