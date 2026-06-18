import React, { useEffect } from 'react';
import { AdminDashboard, PendingPayments, UserManagement, InterestSubmissions } from '../forms/AdminForms';
import SchoolAdminView from './SchoolAdminView';

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
                return (
                    <div className="p-8">
                        <h2 className="text-2xl font-bold">Class Management</h2>
                        <p>Here, admins can create classes and assign teachers.</p>
                    </div>
                ); 
            case 'eftApprovals':
                if (!canManageSubscribers) {
                    return <AdminDashboard setView={setView} onSelect={handleSelectView} currentUser={currentUser} db={db} />;
                }
                return <PendingPayments currentUser={currentUser} db={db} onBack={handleNavigateDashboard} />;
            case 'interestSubmissions':
                return <InterestSubmissions db={db} onBack={handleNavigateDashboard} />;
            case 'schoolAdmin':
                return <SchoolAdminView currentUser={currentUser} />;
            case 'dashboard': 
            default: 
                return <AdminDashboard setView={setView} onSelect={handleSelectView} currentUser={currentUser} db={db} />; 
        } 
    }; 
    
    return <div>{renderAdminContent()}</div>; 
};

export default AdminView;
