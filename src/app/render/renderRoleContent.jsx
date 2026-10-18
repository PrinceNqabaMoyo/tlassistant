import React from 'react';
import { Loader2 } from 'lucide-react';

import AuthScreen from '../../components/auth/AuthScreen';
import RenderStudentContent from './renderStudentContent';

const TeacherView = React.lazy(() => import('../../components/teacher/TeacherView'));
const AdminView = React.lazy(() => import('../../components/admin/AdminView'));
const ParentDashboard = React.lazy(() => import('../../components/parent/ParentDashboard'));
const SchoolAdminView = React.lazy(() => import('../../components/admin/SchoolAdminView'));

function RoleLoadingFallback() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[60vh] p-8 space-y-3">
      <Loader2 className="h-8 w-8 animate-spin text-[#13519C]" />
      <span className="text-xs font-semibold text-slate-500">Loading workspace...</span>
    </div>
  );
}

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
      return (
        <React.Suspense fallback={<RoleLoadingFallback />}>
          <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />
        </React.Suspense>
      );
    }
    if (effectiveRole === 'teacher') {
      return (
        <React.Suspense fallback={<RoleLoadingFallback />}>
          <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />
        </React.Suspense>
      );
    }
    if (effectiveRole === 'parent') {
      return (
        <React.Suspense fallback={<RoleLoadingFallback />}>
          <ParentDashboard 
            currentUser={effectiveCurrentUser} 
            db={dbService} 
            onLaunchLearnerWorkspace={parentProps?.onLaunchLearnerWorkspace} 
          />
        </React.Suspense>
      );
    }
    if (effectiveRole === 'school' || effectiveRole === 'school_admin') {
      return (
        <React.Suspense fallback={<RoleLoadingFallback />}>
          <SchoolAdminView currentUser={effectiveCurrentUser} db={dbService} />
        </React.Suspense>
      );
    }
  }

  if (effectiveRole === 'admin') {
    return (
      <React.Suspense fallback={<RoleLoadingFallback />}>
        <AdminView view={adminView} setView={setAdminView} db={dbService} currentUser={effectiveCurrentUser} />
      </React.Suspense>
    );
  }

  if (effectiveRole === 'teacher') {
    return (
      <React.Suspense fallback={<RoleLoadingFallback />}>
        <TeacherView view={teacherView} setView={setTeacherView} db={dbService} currentUser={effectiveCurrentUser} />
      </React.Suspense>
    );
  }

  if (effectiveRole === 'parent') {
    return (
      <React.Suspense fallback={<RoleLoadingFallback />}>
        <ParentDashboard 
          currentUser={effectiveCurrentUser} 
          db={dbService} 
          onLaunchLearnerWorkspace={parentProps?.onLaunchLearnerWorkspace} 
        />
      </React.Suspense>
    );
  }

  if (effectiveRole === 'school' || effectiveRole === 'school_admin') {
    return (
      <React.Suspense fallback={<RoleLoadingFallback />}>
        <SchoolAdminView currentUser={effectiveCurrentUser} db={dbService} />
      </React.Suspense>
    );
  }

  if (effectiveRole === 'student') {
    return <RenderStudentContent studentContentProps={studentContentProps} />;
  }

  return <div className="p-8 text-center">Loading user profile or role not assigned.</div>;
}
