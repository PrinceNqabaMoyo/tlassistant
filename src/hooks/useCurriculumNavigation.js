import { useState, useCallback } from 'react';

export const useCurriculumNavigation = () => {
    const [view, setView] = useState('curriculum');
    const [allCurricula, setAllCurricula] = useState({});
    const [selectedCurriculumKey, setSelectedCurriculumKey] = useState(null);
    const [selectedGrade, setSelectedGrade] = useState(null);
    const [selectedSubject, setSelectedSubject] = useState(null);
    const [activeTopic, setActiveTopic] = useState(null);
    const [isCurriculumPageVisible, setIsCurriculumPageVisible] = useState(false);
    const [navigationStack, setNavigationStack] = useState([{ view: 'curriculum', label: 'Curricula' }]);

    const addViewToStack = useCallback((newView, label, data = {}) => {
        setNavigationStack(prevStack => [...prevStack, { view: newView, label, ...data }]);
    }, []);

    const updateHelperNavigationLabel = useCallback((label) => {
        // This function can be implemented based on specific navigation requirements
        console.log('Navigation label updated:', label);
    }, []);

    return {
        view,
        setView,
        allCurricula,
        setAllCurricula,
        selectedCurriculumKey,
        setSelectedCurriculumKey,
        selectedGrade,
        setSelectedGrade,
        selectedSubject,
        setSelectedSubject,
        activeTopic,
        setActiveTopic,
        isCurriculumPageVisible,
        setIsCurriculumPageVisible,
        navigationStack,
        setNavigationStack,
        addViewToStack,
        updateHelperNavigationLabel
    };
};
