import React from 'react';
import { Bell, X, Play } from 'lucide-react';

const Notifications = ({ assignments, onStartAssignment, onClose }) => (
  <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div className="bg-white rounded-lg p-6 max-w-md w-full mx-4 max-h-96 overflow-y-auto">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-semibold text-gray-900 flex items-center">
          <Bell className="h-5 w-5 mr-2 text-blue-600" />
          Pending Assignments ({assignments.length})
        </h3>
        <button
          onClick={onClose}
          className="text-gray-400 hover:text-gray-600"
        >
          <X className="h-6 w-6" />
        </button>
      </div>
      
      {assignments.length === 0 ? (
        <p className="text-gray-500 text-center py-8">No pending assignments</p>
      ) : (
        <div className="space-y-3">
          {assignments.map((assignment) => (
            <div
              key={assignment.id}
              className="border border-gray-200 rounded-lg p-4 hover:border-blue-300 transition-colors"
            >
              <h4 className="font-medium text-gray-900 mb-2">
                {assignment.title || 'Untitled Assignment'}
              </h4>
              <p className="text-sm text-gray-600 mb-3">
                {assignment.description || 'No description available'}
              </p>
              <div className="flex justify-between items-center">
                <span className="text-xs text-gray-500">
                  Due: {assignment.dueDate ? new Date(assignment.dueDate).toLocaleDateString() : 'No due date'}
                </span>
                <button
                  onClick={() => onStartAssignment(assignment)}
                  className="bg-blue-600 text-white px-3 py-1 rounded-md text-sm hover:bg-blue-700 transition-colors flex items-center"
                >
                  <Play className="h-3 w-3 mr-1" />
                  Start
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  </div>
);

export default Notifications;
