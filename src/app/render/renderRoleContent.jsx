import React from 'react';
import { Loader2 } from 'lucide-react';

import AuthScreen from '../../components/auth/AuthScreen';
import { TeacherView } from '../../components/teacher';
import { AdminView } from '../../components/admin';
import ParentDashboard from '../../components/parent/ParentDashboard';
import SchoolAdminView from '../../components/admin/SchoolAdminView';
import RenderStudentContent from './renderStudentContent';

export default function RenderRoleContent({ roleContentProps }) {
  const {
    auth: authProps,
    routing,
    roleState,
    services,
    studentContentProps,
    parentProps,
  } = roleContentProps;

  const {
    auth,
    authLoading,
  } = authProps;

  const {
    effectiveCurrentUser,
    effectiveRole,
  } = routing;

  const {
    adminView,
    setAdminView,
    setTeacherView,
    teacherView,
  } = roleState;

  const {
    db,
    dbService,
  } = services;

  if (authLoading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <Loader2 className="h-12 w-12 animate-spin text-blue-600" />
      </div>
    );
  }

  if (!effectiveCurrentUser) {
    return <AuthScreen auth={auth} db={db} />;
  }

  if (effectiveCurrentUser.isSuperAdmin) {
    if (effectiveRole === 'admin') {
      return <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />;
    }
    if (effectiveRole === 'teacher') {
      return <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />;
    }
    if (effectiveRole === 'parent') {
      return (
        <ParentDashboard 
          currentUser={effectiveCurrentUser} 
          db={dbService} 
          onLaunchLearnerWorkspace={parentProps?.onLaunchLearnerWorkspace} 
        />
      );
    }
    if (effectiveRole === 'school' || effectiveRole === 'school_admin') {
      return <SchoolAdminView currentUser={effectiveCurrentUser} />;
    }
  }

  if (effectiveRole === 'admin') {
    return <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />;
  }

  if (effectiveRole === 'teacher') {
    return <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />;
  }

  if (effectiveRole === 'parent') {
    return (
      <ParentDashboard 
        currentUser={effectiveCurrentUser} 
        db={dbService} 
        onLaunchLearnerWorkspace={parentProps?.onLaunchLearnerWorkspace} 
      />
    );
  }

  if (effectiveRole === 'school' || effectiveRole === 'school_admin') {
    return <SchoolAdminView currentUser={effectiveCurrentUser} />;
  }

  if (effectiveRole === 'student') {
    return <RenderStudentContent studentContentProps={studentContentProps} />;
  }

  return <div className="p-8 text-center">Loading user profile or role not assigned.</div>;
}
