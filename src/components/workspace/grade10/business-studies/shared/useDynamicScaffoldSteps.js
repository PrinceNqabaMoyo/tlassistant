import { useEffect, useState } from 'react';

const DEFAULT_STEPS = [
    { key: 'concepts', title: 'Concepts (MCQ)' },
    { key: 'discussion', title: 'Semantic/Essay (Discussion)' },
];

const DEFAULT_ENDPOINT = '/api/business-studies/grade10/sections';

/**
 * Fetch scaffold steps dynamically from the curriculum `.md` file.
 * Falls back to DEFAULT_STEPS if the backend is unreachable.
 */
export const useDynamicScaffoldSteps = ({ topicKey, buildApiUrl, enabled = true, sectionsEndpoint = DEFAULT_ENDPOINT }) => {
    const [steps, setSteps] = useState(DEFAULT_STEPS);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        if (!enabled || !buildApiUrl) return;

        let cancelled = false;
        setLoading(true);

        const fetchSections = async () => {
            try {
                const res = await fetch(buildApiUrl(`${sectionsEndpoint}?topic=${encodeURIComponent(topicKey)}`));
                if (!res.ok) throw new Error(`Sections fetch failed: HTTP ${res.status}`);
                const data = await res.json();
                if (!cancelled && data?.steps && data.steps.length > 0) {
                    setSteps(data.steps);
                }
            } catch (err) {
                if (!cancelled) {
                    console.warn('Failed to fetch sections, using defaults:', err);
                }
            } finally {
                if (!cancelled) setLoading(false);
            }
        };

        fetchSections();
        return () => { cancelled = true; };
    }, [topicKey, buildApiUrl, enabled, sectionsEndpoint]);

    return { steps, loading };
};
