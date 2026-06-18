// API Utility Functions for Student Submissions
import { buildApiUrl } from './apiBaseUrl';
/**
 * Submit an ordered answer for a student assignment
 * @param {Object} params - Submission parameters
 * @param {string} params.assignmentId - Assignment ID
 * @param {string} params.studentId - Student ID
 * @param {string} params.questionId - Question ID
 * @param {Array} params.answerSequence - Answer sequence array
 * @param {string} params.authToken - Authentication token
 * @returns {Promise<Object>} Submission result
 */
export async function submitOrderdAnswer({ assignmentId, studentId, questionId, answerSequence, authToken }) {
  const res = await fetch(buildApiUrl('/api/submissions/submit'), {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': authToken,
    },
    body: JSON.stringify({
      assignmentId,
      studentId,
      questionId,
      answerSequence,
    }),
  });
  return res.json();
}

/**
 * List submissions for a student assignment
 * @param {Object} params - Query parameters
 * @param {string} params.assignmentId - Assignment ID (optional)
 * @param {string} params.studentId - Student ID (optional)
 * @param {number} params.pageSize - Number of results per page (default: 10)
 * @param {string} params.authToken - Authentication token
 * @returns {Promise<Object>} Submissions list
 */
export async function listSubmissions({ assignmentId, studentId, pageSize = 10, authToken }) {
  const params = new URLSearchParams();
  if (assignmentId) params.append('assignmentId', assignmentId);
  if (studentId) params.append('studentId', studentId);
  params.append('pageSize', pageSize);
  
  const res = await fetch(buildApiUrl(`/api/submissions/list?${params.toString()}`), {
    method: 'GET',
    headers: {
      'Authorization': authToken,
    },
  });
  return res.json();
}
