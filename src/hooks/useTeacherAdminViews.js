import { useState } from 'react';

export const useTeacherAdminViews = () => {
    const [teacherView, setTeacherView] = useState('dashboard');
    const [adminView, setAdminView] = useState('dashboard');
    const [schoolAdminView, setSchoolAdminView] = useState('dashboard');

    return {
        teacherView,
        setTeacherView,
        adminView,
        setAdminView,
        schoolAdminView,
        setSchoolAdminView,
    };
};
