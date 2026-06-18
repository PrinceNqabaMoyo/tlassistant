import React from 'react';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { CLASS_ASSIGNMENTS_BLOCKED_MESSAGE } from '../../app/constants/access';

const SchoolAdminView = ({ currentUser }) => {
  const canAccessSchoolAdmin = !!(currentUser?.isOwner || currentUser?.isSuperAdmin);

  if (!canAccessSchoolAdmin) {
    return (
      <div className="p-4 sm:p-6 lg:p-8">
        <FeatureGatePanel
          title="School Admin Mode"
          description={CLASS_ASSIGNMENTS_BLOCKED_MESSAGE}
          badge="Coming soon"
        />
      </div>
    );
  }

  return (
    <div className="p-4 sm:p-6 lg:p-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-8">School Administration</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* Teacher Management */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">Teaching Staff</h3>
          <p className="text-gray-600 mb-4">Onboard, transfer, or offboard teachers and assign subjects/grades.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            Manage Staff
          </button>
        </div>

        {/* Class Oversight */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">Class Oversight</h3>
          <p className="text-gray-600 mb-4">View all school classes, reassign teachers, and archive inactive classes.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            View Classes
          </button>
        </div>

        {/* Marks & Reports */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">Marks & Reports</h3>
          <p className="text-gray-600 mb-4">Collect and export marks across all grades and subjects.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            View Reports
          </button>
        </div>

        {/* Student Enrollment */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">Student Enrollment</h3>
          <p className="text-gray-600 mb-4">Bulk-enroll Fundile-subscribed students into school classes.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            Enroll Students
          </button>
        </div>

        {/* Subscription Tracking */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">Subscription Tracking</h3>
          <p className="text-gray-600 mb-4">Monitor which students have active Fundile subscriptions per class.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            View Subscriptions
          </button>
        </div>

        {/* School Settings */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-xl font-semibold text-gray-800 mb-2">School Settings</h3>
          <p className="text-gray-600 mb-4">Configure term dates, grading scales, and report templates.</p>
          <button
            disabled
            className="w-full bg-gray-300 text-gray-600 py-2 px-4 rounded-lg cursor-not-allowed"
          >
            Configure
          </button>
        </div>
      </div>
    </div>
  );
};

export default SchoolAdminView;
