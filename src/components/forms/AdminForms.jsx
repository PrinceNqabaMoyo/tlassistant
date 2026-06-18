import React, { useState, useEffect } from 'react';
import { getAuth } from 'firebase/auth';
import { collection, getDocs, getDoc, doc, updateDoc, query, where, Timestamp } from 'firebase/firestore';
import { Users, Settings, BarChart3, Shield, Database, Activity, FileText, Plus, Edit, Trash2, Eye, CheckCircle, XCircle, ChevronLeft, School } from 'lucide-react';
import { buildApiUrl } from '../../utils/apiBaseUrl';

const getDateValue = (value) => {
    if (!value) return null;
    if (typeof value.toDate === 'function') return value.toDate();
    if (typeof value === 'object' && value.seconds) return new Date(value.seconds * 1000);
    const parsed = new Date(value);
    return Number.isNaN(parsed.getTime()) ? null : parsed;
};

const formatDateValue = (value, fallback = 'Unknown') => {
    const date = getDateValue(value);
    return date ? date.toLocaleString(undefined, {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    }) : fallback;
};

const getDaysLeft = (value) => {
    const expiryDate = getDateValue(value);
    if (!expiryDate) return 0;
    const difference = expiryDate.getTime() - Date.now();
    if (difference <= 0) return 0;
    return Math.ceil(difference / (24 * 60 * 60 * 1000));
};

const getPaymentStatusValue = (user = {}) => {
    if (user.paymentStatus) return user.paymentStatus;
    if (user.subscriptionExpiry && getDaysLeft(user.subscriptionExpiry) > 0) return 'approved';
    if (user.hasUploadedPop) return 'pending_review';
    return 'not_submitted';
};

const getSubscriptionStatusValue = (user = {}) => {
    if (user.subscriptionStatus === 'active' && getDaysLeft(user.subscriptionExpiry) === 0) return 'expired';
    if (user.subscriptionStatus) return user.subscriptionStatus;
    if (!user.subscriptionExpiry) return 'inactive';
    return getDaysLeft(user.subscriptionExpiry) > 0 ? 'active' : 'expired';
};

const getPaymentStatusClasses = (status) => {
    switch (status) {
        case 'approved':
            return 'bg-emerald-100 text-emerald-700';
        case 'pending_review':
            return 'bg-amber-100 text-amber-700';
        case 'rejected':
            return 'bg-red-100 text-red-700';
        default:
            return 'bg-gray-100 text-gray-700';
    }
};

const getSubscriptionStatusClasses = (status) => {
    switch (status) {
        case 'active':
            return 'bg-blue-100 text-blue-700';
        case 'expired':
            return 'bg-orange-100 text-orange-700';
        case 'pending_review':
            return 'bg-amber-100 text-amber-700';
        default:
            return 'bg-gray-100 text-gray-700';
    }
};

const mapUserWithSubscriptionState = (user = {}) => ({
    ...user,
    paymentStatus: getPaymentStatusValue(user),
    subscriptionStatus: getSubscriptionStatusValue(user),
    daysLeft: getDaysLeft(user.subscriptionExpiry)
});

// Admin Dashboard Component
export const AdminDashboard = ({ currentUser, db, onSelect }) => {
    const [users, setUsers] = useState([]);
    const [systemStats, setSystemStats] = useState({});
    const [loading, setLoading] = useState(true);

    const canManageSubscribers = !!(currentUser?.isOwner || currentUser?.isSuperAdmin);
    const subscriberUsers = users.map(mapUserWithSubscriptionState);
    const activeSubscribers = subscriberUsers.filter((user) => user.subscriptionStatus === 'active');
    const pendingSubscribers = subscriberUsers.filter((user) => user.paymentStatus === 'pending_review');

    useEffect(() => {
        const loadAdminData = async () => {
            if (!currentUser || !db) return;
            
            try {
                // Load users
                const usersRef = collection(db, 'users');
                const usersSnapshot = await getDocs(usersRef);
                
                const usersList = [];
                usersSnapshot.forEach((doc) => {
                    usersList.push({ id: doc.id, ...doc.data() });
                });
                setUsers(usersList);

                // Load system statistics
                const statsRef = collection(db, 'systemStats');
                const statsSnapshot = await getDocs(statsRef);
                
                const stats = {};
                statsSnapshot.forEach((doc) => {
                    stats[doc.id] = doc.data();
                });
                setSystemStats(stats);

                setLoading(false);
            } catch (error) {
                console.error('Error loading admin data:', error);
                setLoading(false);
            }
        };

        loadAdminData();
    }, [currentUser, db]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <h1 className="text-3xl font-bold text-gray-900 mb-8">Administrator Dashboard</h1>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">User Management</h3>
                        <Users className="h-6 w-6 text-blue-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Manage students, roles, and school-wide access</p>
                    <button
                        onClick={() => onSelect('userManagement')}
                        className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
                    >
                        Manage Users
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        {users.length} total users
                    </div>
                </div>

                {canManageSubscribers && (
                    <div className="bg-white rounded-lg shadow-md p-6 border-2 border-blue-100">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-semibold text-gray-800">Subscriber Management</h3>
                            <Users className="h-6 w-6 text-blue-600" />
                        </div>
                        <p className="text-gray-600 mb-4">Review payment status, active access, and subscriber profiles</p>
                        <button
                            onClick={() => onSelect('subscriberManagement')}
                            className="w-full bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 transition-colors"
                        >
                            Manage Subscribers
                        </button>
                        <div className="mt-3 text-sm text-gray-500">
                            {activeSubscribers.length} active · {pendingSubscribers.length} pending review
                        </div>
                    </div>
                )}

                {/* System Analytics */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">System Analytics</h3>
                        <BarChart3 className="h-6 w-6 text-green-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Monitor system performance and usage</p>
                    <button
                        onClick={() => onSelect('systemAnalytics')}
                        className="w-full bg-green-600 text-white py-2 px-4 rounded-lg hover:bg-green-700 transition-colors"
                    >
                        View Analytics
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Real-time monitoring
                    </div>
                </div>

                {/* Content Management */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Content Management</h3>
                        <Database className="h-6 w-6 text-purple-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Manage curriculum content and resources</p>
                    <button
                        onClick={() => onSelect('contentManagement')}
                        className="w-full bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition-colors"
                    >
                        Manage Content
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Curriculum & resources
                    </div>
                </div>

                {/* Competition Setup */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Competitions</h3>
                        <Activity className="h-6 w-6 text-orange-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Set up and manage competitions</p>
                    <button
                        onClick={() => onSelect('competitionSetup')}
                        className="w-full bg-orange-600 text-white py-2 px-4 rounded-lg hover:bg-orange-700 transition-colors"
                    >
                        Setup Competitions
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Event management
                    </div>
                </div>

                {/* System Settings */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">System Settings</h3>
                        <Settings className="h-6 w-6 text-indigo-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Configure system-wide settings</p>
                    <button
                        onClick={() => onSelect('systemSettings')}
                        className="w-full bg-indigo-600 text-white py-2 px-4 rounded-lg hover:bg-indigo-700 transition-colors"
                    >
                        Configure System
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Global configuration
                    </div>
                </div>

                {/* Security & Access */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Security</h3>
                        <Shield className="h-6 w-6 text-red-600" />
                    </div>
                    <p className="text-gray-600 mb-4">Manage security and access controls</p>
                    <button
                        onClick={() => onSelect('securityAccess')}
                        className="w-full bg-red-600 text-white py-2 px-4 rounded-lg hover:bg-red-700 transition-colors"
                    >
                        Security Settings
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        Access control & security
                    </div>
                </div>

                {canManageSubscribers && (
                    <div className="bg-white rounded-lg shadow-md p-6 border-2 border-amber-200">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-semibold text-gray-800">EFT Approvals</h3>
                            <FileText className="h-6 w-6 text-amber-600" />
                        </div>
                        <p className="text-gray-600 mb-4">Review and approve student payment uploads</p>
                        <button
                            onClick={() => onSelect('eftApprovals')}
                            className="w-full bg-amber-600 text-white py-2 px-4 rounded-lg hover:bg-amber-700 transition-colors"
                        >
                            Review Payments
                        </button>
                        <div className="mt-3 text-sm text-amber-600 font-medium">
                            ⚡ Action required
                        </div>
                    </div>
                )}

                {/* Interest Submissions */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <div className="flex items-center justify-between mb-4">
                        <h3 className="text-xl font-semibold text-gray-800">Interest Submissions</h3>
                        <FileText className="h-6 w-6 text-sky-600" />
                    </div>
                    <p className="text-gray-600 mb-4">View demand capture form responses</p>
                    <button
                        onClick={() => onSelect('interestSubmissions')}
                        className="w-full bg-sky-600 text-white py-2 px-4 rounded-lg hover:bg-sky-700 transition-colors"
                    >
                        View Interest
                    </button>
                    <div className="mt-3 text-sm text-gray-500">
                        From public landing page
                    </div>
                </div>

                {/* School Administration */}
                {canManageSubscribers && (
                    <div className="bg-white rounded-lg shadow-md p-6 border-2 border-teal-200">
                        <div className="flex items-center justify-between mb-4">
                            <h3 className="text-xl font-semibold text-gray-800">School Admin</h3>
                            <School className="h-6 w-6 text-teal-600" />
                        </div>
                        <p className="text-gray-600 mb-4">Manage school-wide teachers, classes, marks, and staff</p>
                        <button
                            onClick={() => onSelect('schoolAdmin')}
                            className="w-full bg-teal-600 text-white py-2 px-4 rounded-lg hover:bg-teal-700 transition-colors"
                        >
                            Open School Admin
                        </button>
                        <div className="mt-3 text-sm text-teal-600 font-medium">
                            LMS management layer
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

// User Management Component
export const UserManagement = ({ currentUser, db, onBack, mode = 'general' }) => {
    const [users, setUsers] = useState([]);
    const [selectedUser, setSelectedUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [searchTerm, setSearchTerm] = useState('');
    const [filterRole, setFilterRole] = useState('all');
    const [filterPaymentStatus, setFilterPaymentStatus] = useState('all');
    const [showDeleted, setShowDeleted] = useState(false);

    const isSubscriberMode = mode === 'subscriber';

    useEffect(() => {
        const loadUsers = async () => {
            if (!currentUser || !db) return;
            
            try {
                const usersRef = collection(db, 'users');
                const usersSnapshot = await getDocs(usersRef);
                
                const usersList = [];
                usersSnapshot.forEach((doc) => {
                    usersList.push(mapUserWithSubscriptionState({ id: doc.id, ...doc.data() }));
                });
                setUsers(usersList);
                setLoading(false);
            } catch (error) {
                console.error('Error loading users:', error);
                setLoading(false);
            }
        };

        loadUsers();
    }, [currentUser, db]);

    const filteredUsers = users.filter(user => {
        if (!showDeleted && user.isDeleted) return false;
        const matchesSearch = user.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
                             user.email?.toLowerCase().includes(searchTerm.toLowerCase());
        const matchesRole = filterRole === 'all' || user.role === filterRole;
        const matchesPaymentStatus = !isSubscriberMode || filterPaymentStatus === 'all' || user.paymentStatus === filterPaymentStatus;
        return matchesSearch && matchesRole && matchesPaymentStatus;
    });

    const handleToggleBlock = async (user) => {
        try {
            const newStatus = user.accountStatus === 'blocked' ? 'active' : 'blocked';
            const userRef = doc(db, 'users', user.id);
            await updateDoc(userRef, { accountStatus: newStatus });
            
            const updatedUser = { ...user, accountStatus: newStatus };
            setUsers(prev => prev.map(u => u.id === user.id ? mapUserWithSubscriptionState(updatedUser) : u));
            if (selectedUser?.id === user.id) setSelectedUser(updatedUser);
        } catch (error) {
            console.error('Error updating user block status:', error);
            alert('Failed to update status');
        }
    };

    const handleSoftDelete = async (user) => {
        if (!window.confirm(`Are you sure you want to delete ${user.name}? This will hide them and block access.`)) return;
        try {
            const userRef = doc(db, 'users', user.id);
            await updateDoc(userRef, { isDeleted: true });
            
            const updatedUser = { ...user, isDeleted: true };
            setUsers(prev => prev.map(u => u.id === user.id ? mapUserWithSubscriptionState(updatedUser) : u));
            if (selectedUser?.id === user.id) setSelectedUser(null);
        } catch (error) {
            console.error('Error soft deleting user:', error);
            alert('Failed to delete user');
        }
    };

    const handleRoleChange = async (userId, newRole) => {
        try {
            const userRef = doc(db, 'users', userId);
            await updateDoc(userRef, { role: newRole });
            
            setUsers(prev => prev.map(user => 
                user.id === userId ? mapUserWithSubscriptionState({ ...user, role: newRole }) : user
            ));
            setSelectedUser(prev => prev?.id === userId ? mapUserWithSubscriptionState({ ...prev, role: newRole }) : prev);
        } catch (error) {
            console.error('Error updating user role:', error);
        }
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button
                    type="button"
                    onClick={(e) => {
                        console.log('[UserManagement] Back button clicked!', e);
                        onBack();
                    }}
                    className="flex items-center text-blue-600 hover:text-blue-800 transition-colors cursor-pointer relative z-50 bg-transparent border-0 outline-none"
                    style={{ minWidth: '150px', minHeight: '40px' }}
                >
                    <ChevronLeft className="h-5 w-5 mr-2" />
                    Back to Dashboard
                </button>
                <h1 className="text-3xl font-bold text-gray-900">{isSubscriberMode ? 'Subscriber Management' : 'User Management'}</h1>
            </div>

            {/* Search and Filter */}
            <div className="mb-6 space-y-4">
                <div className="flex flex-col sm:flex-row gap-4">
                    <input
                        type="text"
                        placeholder="Search users by name or email..."
                        value={searchTerm}
                        onChange={(e) => setSearchTerm(e.target.value)}
                        className="flex-1 p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    />
                    <select
                        value={filterRole}
                        onChange={(e) => setFilterRole(e.target.value)}
                        className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    >
                        <option value="all">All Roles</option>
                        <option value="student">Students</option>
                        <option value="teacher">Teachers</option>
                        <option value="admin">Administrators</option>
                    </select>
                    {isSubscriberMode && (
                        <select
                            value={filterPaymentStatus}
                            onChange={(e) => setFilterPaymentStatus(e.target.value)}
                            className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                        >
                            <option value="all">All Payment States</option>
                            <option value="not_submitted">Not Submitted</option>
                            <option value="pending_review">Pending Review</option>
                            <option value="approved">Approved</option>
                            <option value="rejected">Rejected</option>
                        </select>
                    )}
                </div>
                <div className="flex items-center">
                    <label className="flex items-center cursor-pointer">
                        <input
                            type="checkbox"
                            checked={showDeleted}
                            onChange={(e) => setShowDeleted(e.target.checked)}
                            className="form-checkbox h-4 w-4 text-blue-600 rounded border-gray-300"
                        />
                        <span className="ml-2 text-sm text-gray-600">Show deleted users</span>
                    </label>
                </div>
            </div>

            {isSubscriberMode && selectedUser && (
                <div className="mb-6 rounded-2xl border border-blue-100 bg-white p-6 shadow-sm">
                    <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
                        <div>
                            <h2 className="text-2xl font-semibold text-gray-900">{selectedUser.name || 'Unnamed User'}</h2>
                            <p className="text-gray-500">{selectedUser.email || 'No email available'}</p>
                        </div>
                        <button
                            onClick={() => setSelectedUser(null)}
                            className="text-sm font-medium text-blue-600 hover:text-blue-800"
                        >
                            Close details
                        </button>
                    </div>
                    <div className="mt-5 grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
                        <div className="rounded-xl bg-slate-50 p-4">
                            <p className="text-sm text-slate-500">Payment status</p>
                            <p className="mt-2 text-lg font-semibold text-slate-900">{selectedUser.paymentStatus}</p>
                        </div>
                        <div className="rounded-xl bg-slate-50 p-4">
                            <p className="text-sm text-slate-500">Subscription status</p>
                            <p className="mt-2 text-lg font-semibold text-slate-900">{selectedUser.subscriptionStatus}</p>
                        </div>
                        <div className="rounded-xl bg-slate-50 p-4">
                            <p className="text-sm text-slate-500">Days left</p>
                            <p className="mt-2 text-lg font-semibold text-slate-900">{selectedUser.daysLeft}</p>
                        </div>
                        <div className="rounded-xl bg-slate-50 p-4">
                            <p className="text-sm text-slate-500">Last payment ref</p>
                            <p className="mt-2 truncate font-mono text-sm font-semibold text-slate-900">{selectedUser.lastPaymentReference || 'None'}</p>
                        </div>
                    </div>
                    <div className="mt-5 grid grid-cols-1 gap-4 md:grid-cols-2 xl:grid-cols-4">
                        <div>
                            <p className="text-sm text-gray-500">Grade</p>
                            <p className="font-medium text-gray-900">{selectedUser.grade || selectedUser.lastRequestedGrade || 'Not set'}</p>
                        </div>
                        <div>
                            <p className="text-sm text-gray-500">Created</p>
                            <p className="font-medium text-gray-900">{formatDateValue(selectedUser.createdAt)}</p>
                        </div>
                        <div>
                            <p className="text-sm text-gray-500">Last POP submitted</p>
                            <p className="font-medium text-gray-900">{formatDateValue(selectedUser.lastPaymentSubmittedAt, 'Never')}</p>
                        </div>
                        <div>
                            <p className="text-sm text-gray-500">Subscribed grades</p>
                            <p className="font-medium text-gray-900">{Array.isArray(selectedUser.subscribedGrades) && selectedUser.subscribedGrades.length > 0 ? selectedUser.subscribedGrades.join(', ') : 'None'}</p>
                        </div>
                    </div>
                </div>
            )}

            {/* Users List */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {filteredUsers.map(user => (
                    <div key={user.id} className="bg-white rounded-lg shadow-md p-6">
                        <div className="flex items-center justify-between mb-4">
                            <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                                <span className="text-blue-600 font-semibold text-lg">
                                    {user.name?.charAt(0) || 'U'}
                                </span>
                            </div>
                            <div className="flex space-x-2">
                                <button
                                    onClick={() => handleToggleBlock(user)}
                                    className={`p-2 rounded-lg transition-colors ${
                                        user.accountStatus === 'blocked' 
                                            ? 'text-red-600 bg-red-50 hover:bg-red-100' 
                                            : 'text-gray-500 hover:bg-gray-100'
                                    }`}
                                    title={user.accountStatus === 'blocked' ? 'Unblock User' : 'Block User'}
                                >
                                    {user.accountStatus === 'blocked' ? <XCircle className="h-4 w-4" /> : <Shield className="h-4 w-4" />}
                                </button>
                                <button
                                    onClick={() => handleSoftDelete(user)}
                                    className={`p-2 rounded-lg transition-colors ${
                                        user.isDeleted 
                                            ? 'text-red-300 cursor-not-allowed' 
                                            : 'text-red-600 hover:bg-red-50'
                                    }`}
                                    disabled={user.isDeleted}
                                    title="Delete User"
                                >
                                    <Trash2 className="h-4 w-4" />
                                </button>
                                <button
                                    onClick={() => setSelectedUser(user)}
                                    className="p-2 text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                                    title="View Details"
                                >
                                    <Eye className="h-4 w-4" />
                                </button>
                                <button
                                    onClick={() => {/* Edit user */}}
                                    className="p-2 text-green-600 hover:bg-green-50 rounded-lg transition-colors"
                                    title="Edit User"
                                >
                                    <Edit className="h-4 w-4" />
                                </button>
                            </div>
                        </div>
                        
                        <h3 className="text-lg font-semibold text-gray-800 mb-2">{user.name || 'Unnamed User'}</h3>
                        <p className="text-gray-600 text-sm mb-3">{user.email}</p>
                        
                        <div className="space-y-2">
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-500">Role:</span>
                                <select
                                    value={user.role || 'student'}
                                    onChange={(e) => handleRoleChange(user.id, e.target.value)}
                                    className="text-sm border border-gray-300 rounded px-2 py-1"
                                >
                                    <option value="student">Student</option>
                                    <option value="teacher">Teacher</option>
                                    <option value="admin">Administrator</option>
                                </select>
                            </div>
                            {isSubscriberMode ? (
                                <>
                                    <div className="flex justify-between text-sm">
                                        <span className="text-gray-500">Payment:</span>
                                        <span className={`px-2 py-1 rounded-full text-xs ${getPaymentStatusClasses(user.paymentStatus)}`}>
                                            {user.paymentStatus}
                                        </span>
                                    </div>
                                    <div className="flex justify-between text-sm">
                                        <span className="text-gray-500">Subscription:</span>
                                        <span className={`px-2 py-1 rounded-full text-xs ${getSubscriptionStatusClasses(user.subscriptionStatus)}`}>
                                            {user.subscriptionStatus}
                                        </span>
                                    </div>
                                    <div className="flex justify-between text-sm">
                                        <span className="text-gray-500">Days left:</span>
                                        <span className="font-medium text-gray-900">{user.daysLeft}</span>
                                    </div>
                                </>
                            ) : (
                                <div className="flex justify-between text-sm">
                                    <span className="text-gray-500">Status:</span>
                                    <span className={`px-2 py-1 rounded-full text-xs ${
                                        user.status === 'active' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'
                                    }`}>
                                        {user.status || 'inactive'}
                                    </span>
                                </div>
                            )}
                            <div className="flex justify-between text-sm">
                                <span className="text-gray-500">Created:</span>
                                <span className="font-medium">
                                    {formatDateValue(user.createdAt)}
                                </span>
                            </div>
                        </div>
                    </div>
                ))}
            </div>

            {filteredUsers.length === 0 && (
                <div className="text-center py-12">
                    <Users className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-gray-900 mb-2">No users found</h3>
                    <p className="text-gray-500">
                        {searchTerm || filterRole !== 'all' ? 'Try adjusting your search or filter terms.' : 'No users in the system yet.'}
                    </p>
                </div>
            )}
        </div>
    );
};

// System Analytics Component
export const SystemAnalytics = ({ currentUser, db, onBack }) => {
    const [analytics, setAnalytics] = useState({});
    const [loading, setLoading] = useState(true);
    const [timeRange, setTimeRange] = useState('7d');

    useEffect(() => {
        const loadAnalytics = async () => {
            if (!currentUser || !db) return;
            
            try {
                // Simulate loading analytics data
                await new Promise(resolve => setTimeout(resolve, 1000));
                
                const mockAnalytics = {
                    users: {
                        total: 1250,
                        active: 890,
                        newThisWeek: 45,
                        growth: 12.5
                    },
                    usage: {
                        dailyActive: 456,
                        weeklyActive: 1200,
                        monthlyActive: 2100,
                        avgSessionTime: 25
                    },
                    performance: {
                        responseTime: 120,
                        uptime: 99.9,
                        errors: 0.1,
                        loadAverage: 0.8
                    }
                };
                
                setAnalytics(mockAnalytics);
                setLoading(false);
            } catch (error) {
                console.error('Error loading analytics:', error);
                setLoading(false);
            }
        };

        loadAnalytics();
    }, [currentUser, db, timeRange]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button
                    onClick={onBack}
                    className="flex items-center text-blue-600 hover:text-blue-800 transition-colors"
                >
                    <ChevronLeft className="h-5 w-5 mr-2" />
                    Back to Dashboard
                </button>
                <h1 className="text-3xl font-bold text-gray-900">System Analytics</h1>
            </div>

            {/* Time Range Selector */}
            <div className="mb-6">
                <select
                    value={timeRange}
                    onChange={(e) => setTimeRange(e.target.value)}
                    className="p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                >
                    <option value="24h">Last 24 Hours</option>
                    <option value="7d">Last 7 Days</option>
                    <option value="30d">Last 30 Days</option>
                    <option value="90d">Last 90 Days</option>
                </select>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {/* User Statistics */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4">User Statistics</h3>
                    <div className="space-y-4">
                        <div className="flex justify-between">
                            <span className="text-gray-600">Total Users</span>
                            <span className="font-semibold">{analytics.users?.total?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Active Users</span>
                            <span className="font-semibold text-green-600">{analytics.users?.active?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">New This Week</span>
                            <span className="font-semibold text-blue-600">+{analytics.users?.newThisWeek}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Growth Rate</span>
                            <span className="font-semibold text-green-600">+{analytics.users?.growth}%</span>
                        </div>
                    </div>
                </div>

                {/* Usage Statistics */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4">Usage Statistics</h3>
                    <div className="space-y-4">
                        <div className="flex justify-between">
                            <span className="text-gray-600">Daily Active</span>
                            <span className="font-semibold">{analytics.usage?.dailyActive?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Weekly Active</span>
                            <span className="font-semibold">{analytics.usage?.weeklyActive?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Monthly Active</span>
                            <span className="font-semibold">{analytics.usage?.monthlyActive?.toLocaleString()}</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Avg Session</span>
                            <span className="font-semibold">{analytics.usage?.avgSessionTime} min</span>
                        </div>
                    </div>
                </div>

                {/* Performance Statistics */}
                <div className="bg-white rounded-lg shadow-md p-6">
                    <h3 className="text-xl font-semibold text-gray-800 mb-4">Performance</h3>
                    <div className="space-y-4">
                        <div className="flex justify-between">
                            <span className="text-gray-600">Response Time</span>
                            <span className="font-semibold">{analytics.performance?.responseTime}ms</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Uptime</span>
                            <span className="font-semibold text-green-600">{analytics.performance?.uptime}%</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Error Rate</span>
                            <span className="font-semibold text-red-600">{analytics.performance?.errors}%</span>
                        </div>
                        <div className="flex justify-between">
                            <span className="text-gray-600">Load Average</span>
                            <span className="font-semibold">{analytics.performance?.loadAverage}</span>
                        </div>
                    </div>
                </div>
            </div>

            {/* Charts Placeholder */}
            <div className="mt-8 bg-white rounded-lg shadow-md p-6">
                <h3 className="text-xl font-semibold text-gray-800 mb-4">Usage Trends</h3>
                <div className="h-64 bg-gray-50 rounded-lg flex items-center justify-center">
                    <div className="text-center">
                        <BarChart3 className="h-16 w-16 text-gray-400 mx-auto mb-4" />
                        <p className="text-gray-500">Charts and graphs would be displayed here</p>
                        <p className="text-sm text-gray-400">Integration with charting library needed</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

// EFT Pending Payments Approval Component
export const PendingPayments = ({ currentUser, db, onBack }) => {
    const [payments, setPayments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [actionLoading, setActionLoading] = useState(null); // tracks which payment is being actioned
    const [viewingPaymentId, setViewingPaymentId] = useState(null);
    const [filter, setFilter] = useState('pending'); // 'pending' | 'approved' | 'rejected' | 'all'

    useEffect(() => {
        const loadPayments = async () => {
            if (!db) return;
            try {
                const paymentsRef = collection(db, 'pending_payments');
                let q;
                if (filter === 'all') {
                    q = paymentsRef;
                } else {
                    q = query(paymentsRef, where('status', '==', filter));
                }
                const snapshot = await getDocs(q);
                const list = [];
                snapshot.forEach((d) => {
                    const data = d.data();
                    list.push({
                        id: d.id,
                        ...data,
                        timestampDisplay: data.timestamp?.toDate ? data.timestamp.toDate().toLocaleString() : 'Unknown'
                    });
                });
                // Sort newest first
                list.sort((a, b) => {
                    const ta = a.timestamp?.toDate ? a.timestamp.toDate().getTime() : 0;
                    const tb = b.timestamp?.toDate ? b.timestamp.toDate().getTime() : 0;
                    return tb - ta;
                });
                setPayments(list);
            } catch (error) {
                console.error('Error loading pending payments:', error);
            } finally {
                setLoading(false);
            }
        };
        loadPayments();
    }, [db, filter]);

    const handleApprove = async (payment, durationDays) => {
        if (!db) return;
        setActionLoading(payment.id);
        try {
            // 1. Fetch user profile first to check existing subscription status
            const userRef = doc(db, 'users', payment.userId);
            const userSnap = await getDoc(userRef);
            if (!userSnap.exists()) {
                throw new Error('User profile not found for this payment.');
            }

            const existingUserData = userSnap.data();
            
            // Calculate new expiry date by stacking days if already active
            const now = new Date();
            let baseDate = now;
            if (existingUserData.subscriptionStatus === 'active' && existingUserData.subscriptionExpiry) {
                const currentExpiry = getDateValue(existingUserData.subscriptionExpiry);
                // Stack only if the current expiry is in the future
                if (currentExpiry && currentExpiry.getTime() > now.getTime()) {
                    baseDate = currentExpiry;
                }
            }
            const expiryDate = new Date(baseDate.getTime() + durationDays * 24 * 60 * 60 * 1000);
            
            const grade = Number(payment.requestedGrade) || null;

            const existingGrades = Array.isArray(existingUserData.subscribedGrades) ? existingUserData.subscribedGrades : [];

            const updatedGrades = grade && !existingGrades.includes(grade)
                ? [...existingGrades, grade]
                : existingGrades;

            // 2. Update the user's subscription fields
            await updateDoc(userRef, {
                subscriptionExpiry: Timestamp.fromDate(expiryDate),
                subscriptionStatus: 'active',
                paymentStatus: 'approved',
                subscribedGrades: updatedGrades,
                tier: existingUserData.tier || 'standard',
                hasUploadedPop: true,
                lastApprovedPaymentId: payment.id,
                lastPaymentSubmittedAt: existingUserData.lastPaymentSubmittedAt || payment.timestamp || Timestamp.now(),
                paymentReference: payment.paymentReference || payment.referenceUsed || existingUserData.paymentReference || null,
                lastPaymentReference: payment.paymentReference || payment.referenceUsed || existingUserData.lastPaymentReference || null,
                lastRequestedGrade: payment.requestedGrade || existingUserData.lastRequestedGrade || null,
                latestPendingPaymentId: null
            });

            // 2. Mark the payment as approved
            const paymentRef = doc(db, 'pending_payments', payment.id);
            await updateDoc(paymentRef, {
                status: 'approved',
                approvedBy: currentUser?.email || 'admin',
                approvedAt: Timestamp.now(),
                durationDays: durationDays,
                expiryDate: Timestamp.fromDate(expiryDate),
                syncedUserPaymentStatus: 'approved',
                syncedUserSubscriptionStatus: 'active'
            });

            // 3. Update local state
            setPayments(prev => prev.map(p =>
                p.id === payment.id ? { ...p, status: 'approved', durationDays, expiryDate: Timestamp.fromDate(expiryDate) } : p
            ));
        } catch (error) {
            console.error('Error approving payment:', error);
            alert('Failed to approve payment: ' + error.message);
        } finally {
            setActionLoading(null);
        }
    };

    const handleReject = async (payment) => {
        if (!db) return;
        setActionLoading(payment.id);
        try {
            const userRef = doc(db, 'users', payment.userId);
            const userSnap = await getDoc(userRef);
            if (!userSnap.exists()) {
                throw new Error('User profile not found for this payment.');
            }

            const existingUserData = userSnap.data();
            const nextSubscriptionStatus = existingUserData.subscriptionExpiry
                ? (getDaysLeft(existingUserData.subscriptionExpiry) > 0 ? 'active' : 'expired')
                : 'inactive';

            await updateDoc(userRef, {
                paymentStatus: 'rejected',
                subscriptionStatus: nextSubscriptionStatus,
                hasUploadedPop: true,
                lastPaymentSubmittedAt: existingUserData.lastPaymentSubmittedAt || payment.timestamp || Timestamp.now(),
                paymentReference: payment.paymentReference || payment.referenceUsed || existingUserData.paymentReference || null,
                lastPaymentReference: payment.paymentReference || payment.referenceUsed || existingUserData.lastPaymentReference || null,
                lastRequestedGrade: payment.requestedGrade || existingUserData.lastRequestedGrade || null,
                latestPendingPaymentId: null
            });

            const paymentRef = doc(db, 'pending_payments', payment.id);
            await updateDoc(paymentRef, {
                status: 'rejected',
                rejectedBy: currentUser?.email || 'admin',
                rejectedAt: Timestamp.now(),
                syncedUserPaymentStatus: 'rejected',
                syncedUserSubscriptionStatus: nextSubscriptionStatus
            });
            setPayments(prev => prev.map(p =>
                p.id === payment.id ? { ...p, status: 'rejected' } : p
            ));
        } catch (error) {
            console.error('Error rejecting payment:', error);
            alert('Failed to reject payment: ' + error.message);
        } finally {
            setActionLoading(null);
        }
    };

    const handleViewPop = async (payment) => {
        if (!payment?.storagePath && payment?.popUrl) {
            window.open(payment.popUrl, '_blank', 'noopener,noreferrer');
            return;
        }

        if (!payment?.storagePath) {
            alert('This payment record does not include a POP storage path.');
            return;
        }

        setViewingPaymentId(payment.id);

        try {
            const auth = getAuth();
            const authUser = auth.currentUser;
            if (!authUser) {
                throw new Error('Please sign in again before viewing POP files.');
            }

            const idToken = await authUser.getIdToken();
            const response = await fetch(buildApiUrl('/api/payments/pop-view-url'), {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${idToken}`,
                },
                body: JSON.stringify({ storagePath: payment.storagePath }),
            });

            const payload = await response.json().catch(() => ({}));

            if (!response.ok || !payload?.success || !payload?.url) {
                throw new Error(payload?.error || 'Could not prepare the POP preview link.');
            }

            window.open(payload.url, '_blank', 'noopener,noreferrer');
        } catch (error) {
            console.error('Error creating signed POP URL:', error);
            alert(error?.message || 'Could not open the POP file.');
        } finally {
            setViewingPaymentId(null);
        }
    };

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-amber-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button
                    type="button"
                    onClick={(e) => {
                        console.log('[PendingPayments] Back button clicked!', e);
                        onBack();
                    }}
                    className="flex items-center text-blue-600 hover:text-blue-800 transition-colors cursor-pointer relative z-50 bg-transparent border-0 outline-none"
                    style={{ minWidth: '150px', minHeight: '40px' }}
                >
                    <ChevronLeft className="h-5 w-5 mr-2" />
                    Back to Dashboard
                </button>
                <h1 className="text-2xl sm:text-3xl font-bold text-gray-900">EFT Payment Approvals</h1>
            </div>

            {/* Filter Tabs */}
            <div className="flex gap-2 mb-6 flex-wrap">
                {['pending', 'approved', 'rejected', 'all'].map(f => (
                    <button
                        key={f}
                        onClick={() => { setLoading(true); setFilter(f); }}
                        className={`px-4 py-2 rounded-full text-sm font-semibold capitalize transition-colors ${
                            filter === f
                            ? 'bg-amber-600 text-white shadow-md'
                            : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                        }`}
                    >
                        {f}
                    </button>
                ))}
            </div>

            {payments.length === 0 ? (
                <div className="text-center py-16 bg-white rounded-xl shadow">
                    <FileText className="h-16 w-16 text-gray-300 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-gray-700">No {filter} payments found</h3>
                    <p className="text-sm text-gray-400 mt-1">Check back later or change filters.</p>
                </div>
            ) : (
                <div className="space-y-4">
                    {payments.map(payment => (
                        <div key={payment.id} className={`bg-white rounded-xl shadow-md p-5 border-l-4 ${
                            payment.status === 'approved' ? 'border-emerald-500' :
                            payment.status === 'rejected' ? 'border-red-400' :
                            'border-amber-400'
                        }`}>
                            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                                {/* Left: User Info */}
                                <div className="flex-1 min-w-0">
                                    <div className="flex items-center gap-2 mb-1">
                                        <span className={`inline-block px-2 py-0.5 rounded-full text-xs font-bold uppercase ${
                                            payment.status === 'approved' ? 'bg-emerald-100 text-emerald-700' :
                                            payment.status === 'rejected' ? 'bg-red-100 text-red-700' :
                                            'bg-amber-100 text-amber-700'
                                        }`}>
                                            {payment.status}
                                        </span>
                                        <span className="text-xs text-gray-400">{payment.timestampDisplay}</span>
                                    </div>
                                    <p className="font-semibold text-gray-800 truncate">{payment.email}</p>
                                    <p className="text-sm text-gray-500">Grade {payment.requestedGrade} · {payment.plan}</p>
                                    <p className="text-xs text-gray-400 mt-0.5">Ref: <span className="font-mono">{payment.paymentReference || payment.referenceUsed}</span></p>
                                </div>

                                {/* Right: Actions */}
                                <div className="flex items-center gap-2 shrink-0">
                                    {/* View POP */}
                                    {(payment.storagePath || payment.popUrl) && (
                                        <button
                                            type="button"
                                            onClick={() => handleViewPop(payment)}
                                            disabled={viewingPaymentId === payment.id}
                                            className="flex items-center gap-1 px-3 py-2 bg-blue-50 text-blue-700 rounded-lg text-sm font-medium hover:bg-blue-100 transition disabled:opacity-50"
                                        >
                                            <Eye className="w-4 h-4" /> {viewingPaymentId === payment.id ? 'Opening...' : 'View POP'}
                                        </button>
                                    )}

                                    {payment.status === 'pending' && (
                                        <>
                                            <button
                                                onClick={() => handleApprove(payment, 31)}
                                                disabled={actionLoading === payment.id}
                                                className="flex items-center gap-1 px-3 py-2 bg-emerald-600 text-white rounded-lg text-sm font-semibold hover:bg-emerald-700 transition disabled:opacity-50"
                                            >
                                                <CheckCircle className="w-4 h-4" /> 1 Mo
                                            </button>
                                            <button
                                                onClick={() => handleApprove(payment, 365)}
                                                disabled={actionLoading === payment.id}
                                                className="flex items-center gap-1 px-3 py-2 bg-indigo-600 text-white rounded-lg text-sm font-semibold hover:bg-indigo-700 transition disabled:opacity-50"
                                            >
                                                <CheckCircle className="w-4 h-4" /> 12 Mo
                                            </button>
                                            <button
                                                onClick={() => handleReject(payment)}
                                                disabled={actionLoading === payment.id}
                                                className="flex items-center gap-1 px-3 py-2 bg-red-50 text-red-700 rounded-lg text-sm font-semibold hover:bg-red-100 transition disabled:opacity-50"
                                            >
                                                <XCircle className="w-4 h-4" /> Reject
                                            </button>
                                        </>
                                    )}
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export const InterestSubmissions = ({ db, onBack }) => {
    const [submissions, setSubmissions] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const loadSubmissions = async () => {
            if (!db) return;
            try {
                const subRef = collection(db, 'interest_submissions');
                const snapshot = await getDocs(subRef);
                const list = [];
                snapshot.forEach(doc => {
                    const data = doc.data();
                    list.push({
                        id: doc.id,
                        ...data,
                        createdAtDisplay: formatDateValue(data.createdAt)
                    });
                });
                list.sort((a, b) => {
                    const ta = a.createdAt?.toDate ? a.createdAt.toDate().getTime() : 0;
                    const tb = b.createdAt?.toDate ? b.createdAt.toDate().getTime() : 0;
                    return tb - ta;
                });
                setSubmissions(list);
            } catch (error) {
                console.error('Error loading submissions:', error);
            } finally {
                setLoading(false);
            }
        };
        loadSubmissions();
    }, [db]);

    if (loading) {
        return (
            <div className="flex items-center justify-center min-h-64">
                <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-sky-600"></div>
            </div>
        );
    }

    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <div className="flex items-center justify-between mb-6">
                <button onClick={onBack} className="flex items-center text-blue-600 hover:text-blue-800 transition-colors">
                    <ChevronLeft className="h-5 w-5 mr-2" /> Back to Dashboard
                </button>
                <h1 className="text-2xl font-bold text-gray-900">Interest Submissions</h1>
            </div>
            {submissions.length === 0 ? (
                <div className="text-center py-12 bg-white rounded-xl shadow">
                    <p className="text-gray-500">No submissions found.</p>
                </div>
            ) : (
                <div className="space-y-4">
                    {submissions.map(sub => (
                        <div key={sub.id} className="bg-white rounded-lg shadow p-5 border-l-4 border-sky-400">
                            <div className="flex justify-between items-start mb-2">
                                <div>
                                    <h3 className="font-semibold text-lg">{sub.name}</h3>
                                    <p className="text-sm text-gray-500">{sub.email}</p>
                                </div>
                                <span className="text-xs text-gray-400">{sub.createdAtDisplay}</span>
                            </div>
                            <div className="grid grid-cols-2 md:grid-cols-4 gap-2 text-sm mt-3 bg-slate-50 p-3 rounded-lg">
                                <div><span className="text-gray-500 block text-xs">Curriculum</span>{sub.curriculum}</div>
                                <div><span className="text-gray-500 block text-xs">Grade</span>{sub.requestedGrade}</div>
                                <div><span className="text-gray-500 block text-xs">Subject</span>{sub.requestedSubject}</div>
                                <div><span className="text-gray-500 block text-xs">Role/School</span>{sub.schoolOrRole || '-'}</div>
                            </div>
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};
