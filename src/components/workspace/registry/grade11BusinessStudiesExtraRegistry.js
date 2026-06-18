import { createGrade11BSTopicRegistry } from '../grade11/business-studies/shared/createGrade11BSRoute';

// Grade 11 Business Studies topics built on the config-driven shared layer.
// Term 1 topics 1-2 (influences, challenges) keep their bespoke components in
// grade11BusinessStudiesRegistry.js; everything else is declarative config here.
const EXTRA_TOPICS = [
    // ----- Term 1 -----
    {
        topicKey: 'grade11_bs_adapting_to_challenges',
        modePrefix: 'grade11_bs_adapting_to_challenges',
        topicTitle: 'Adapting to Challenges in the Business Environments',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses adapt to challenges in the macro environment by restructuring, influencing role players and building relationships.',
                sections: [
                    { variant: 'indigo', heading: 'Restructuring', text: 'Adapting the business through mergers, takeovers, acquisitions and strategic alliances.' },
                    { variant: 'note', heading: 'Information management', text: 'Gathering and using information to respond to changes in the environment.' },
                ],
            },
            {
                key: 'influence',
                label: 'Influencing',
                sections: [
                    { variant: 'green', heading: 'Ways to influence', bullets: ['Lobbying decision-makers', 'Hedging against risk', 'Social responsibility programmes', 'Power relations'] },
                ],
            },
            {
                key: 'relationships',
                label: 'Relationships',
                sections: [
                    { variant: 'blue', heading: 'Lobbying, networking & power', bullets: ['Lobbying to influence policy', 'Networking to build contacts', 'Forming power relations with role players'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_socio_economic_issues',
        modePrefix: 'grade11_bs_socio_economic_issues',
        topicTitle: 'Contemporary Socio-economic Issues',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Socio-economic issues such as piracy, dumping and infringement of intellectual property affect how businesses operate.',
                sections: [
                    { variant: 'indigo', heading: 'Piracy', text: 'The illegal copying and selling of products protected by copyright.' },
                    { variant: 'note', heading: 'Dumping', text: 'Selling goods in another country below cost or below the home-market price.' },
                ],
            },
            {
                key: 'ip',
                label: 'Intellectual property',
                sections: [
                    { variant: 'green', heading: 'Protection', bullets: ['Patent (inventions)', 'Copyright (creative works)', 'Trademark (brand identity)'] },
                ],
            },
            {
                key: 'ir',
                label: 'Industrial relations',
                sections: [
                    { variant: 'blue', heading: 'Role players', bullets: ['Trade unions', 'Lockouts and strikes', 'Labour Relations Act'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_business_sectors',
        modePrefix: 'grade11_bs_business_sectors',
        topicTitle: 'Business Sectors',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The economy is divided into the primary, secondary and tertiary sectors, which are linked to one another.',
                sections: [
                    { variant: 'indigo', heading: 'The three sectors', bullets: ['Primary: extracts raw materials', 'Secondary: processes/manufactures goods', 'Tertiary: provides services'] },
                ],
            },
            {
                key: 'links',
                label: 'Links',
                sections: [
                    { variant: 'green', heading: 'Forward & backward links', text: 'A backward link buys inputs from an earlier sector; a forward link supplies outputs to a later sector.' },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_benefits_of_a_company',
        modePrefix: 'grade11_bs_benefits_of_a_company',
        topicTitle: 'Benefits of a Company',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'A company offers benefits over other forms of ownership, such as limited liability and continuity.',
                sections: [
                    { variant: 'indigo', heading: 'Limited liability', text: 'Shareholders are only liable for the amount they invested, protecting personal assets.' },
                    { variant: 'note', heading: 'Continuity', text: 'A company has a separate legal identity and continues despite changes in ownership.' },
                ],
            },
            {
                key: 'formation',
                label: 'Formation',
                sections: [
                    { variant: 'green', heading: 'Formation documents', bullets: ['Memorandum of Incorporation (MOI)', 'Prospectus (public companies)', 'Notice of Incorporation'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_avenues_of_acquiring_businesses',
        modePrefix: 'grade11_bs_avenues_of_acquiring_businesses',
        topicTitle: 'Avenues of Acquiring Businesses',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Entrepreneurs can acquire a business through franchising, outsourcing, leasing or buying an existing business.',
                sections: [
                    { variant: 'indigo', heading: 'Franchising', text: 'The franchisor licenses its brand and model to a franchisee for fees.' },
                    { variant: 'note', heading: 'Leasing', text: 'A lessee rents an asset owned by a lessor for a specified period.' },
                ],
            },
            {
                key: 'avenues',
                label: 'Avenues',
                sections: [
                    { variant: 'green', heading: 'Options', bullets: ['Franchising', 'Outsourcing', 'Leasing', 'Buying an existing business'] },
                ],
            },
        ],
    },
    // ----- Term 2 -----
    {
        topicKey: 'grade11_bs_creative_thinking',
        modePrefix: 'grade11_bs_creative_thinking',
        topicTitle: 'Creative Thinking & Problem Solving',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Creative thinking generates new ideas; problem solving applies a structured process to overcome challenges.',
                sections: [
                    { variant: 'indigo', heading: 'Creative thinking', text: 'The ability to think of original, diverse or new ideas to solve problems.' },
                    { variant: 'note', heading: 'Routine vs creative', text: 'Routine thinking repeats the same steps; creative thinking finds non-conventional solutions.' },
                ],
            },
            {
                key: 'techniques',
                label: 'Techniques',
                sections: [
                    { variant: 'green', heading: 'Problem-solving techniques', bullets: ['Delphi Technique (experts)', 'Force Field Analysis (forces for/against)', 'Brainstorming', 'Mind-mapping'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_stress_crisis_change',
        modePrefix: 'grade11_bs_stress_crisis_change',
        topicTitle: 'Stress, Crisis & Change Management',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses must manage stress, respond to crises and lead employees through change.',
                sections: [
                    { variant: 'indigo', heading: 'Stress', text: 'Mental or emotional strain from demanding circumstances such as overload and deadlines.' },
                    { variant: 'note', heading: 'Crisis vs change', text: 'Crisis management deals with emergencies; change management deals with planned development.' },
                ],
            },
            {
                key: 'kotter',
                label: "Kotter's steps",
                sections: [
                    { variant: 'blue', heading: '8 steps of leading change', bullets: ['Establish urgency', 'Form a coalition', 'Create a vision', 'Communicate the vision', 'Empower action', 'Create short-term wins', 'Consolidate gains', 'Anchor in culture'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_marketing_function',
        modePrefix: 'grade11_bs_marketing_function',
        topicTitle: 'The Marketing Function',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The marketing function promotes the buying and selling of products through the marketing mix.',
                sections: [
                    { variant: 'indigo', heading: 'Marketing activities', bullets: ['Standardisation & grading', 'Storage', 'Transport', 'Financing', 'Risk bearing', 'Buying & selling'] },
                ],
            },
            {
                key: 'mix',
                label: 'Marketing mix',
                sections: [
                    { variant: 'green', heading: 'Pricing techniques', bullets: ['Cost-based', 'Mark-up', 'Penetration', 'Skimming', 'Psychological', 'Bait'] },
                    { variant: 'note', heading: 'Distribution', text: 'Direct (no intermediaries) vs indirect (wholesalers/retailers) channels.' },
                ],
            },
            {
                key: 'communication',
                label: 'Communication',
                sections: [
                    { variant: 'blue', heading: 'Communication policy', bullets: ['Advertising (paid)', 'Sales promotion', 'Publicity (unpaid)', 'Personal selling'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_production_function',
        modePrefix: 'grade11_bs_production_function',
        topicTitle: 'The Production Function',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The production function turns inputs into outputs through planned and controlled processes.',
                sections: [
                    { variant: 'indigo', heading: 'Production methods', bullets: ['Mass production (large, identical)', 'Batch production (groups)', 'Job production (one unique item)'] },
                ],
            },
            {
                key: 'safety-quality',
                label: 'Safety & quality',
                sections: [
                    { variant: 'green', heading: 'Safety & quality', bullets: ['Occupational Health and Safety Act (No. 85 of 1993)', 'Quality control (final inspection)', 'Total Quality Management (TQM)', 'SABS standards'] },
                ],
            },
            {
                key: 'costs',
                label: 'Costs',
                sections: [
                    { variant: 'blue', heading: 'Production costs', bullets: ['Fixed vs variable costs', 'Total and unit costs', 'Break-even point (revenue = costs)'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_professionalism_and_ethics',
        modePrefix: 'grade11_bs_professionalism_and_ethics',
        topicTitle: 'Professionalism & Ethics',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Professionalism is using skills in a profession; ethics is acting on moral principles of right and wrong.',
                sections: [
                    { variant: 'indigo', heading: 'Professionalism vs ethics', text: 'Professionalism is applying knowledge in a job; ethics is choosing what is morally right.' },
                ],
            },
            {
                key: 'theories',
                label: 'Theories',
                sections: [
                    { variant: 'green', heading: 'Theories of ethics', bullets: ['Consequential theory (outcomes)', 'Common good approach (community)', 'Rights approach (protecting rights)'] },
                ],
            },
        ],
    },
    // ----- Term 3 -----
    {
        topicKey: 'grade11_bs_entrepreneurial_assessment',
        modePrefix: 'grade11_bs_entrepreneurial_assessment',
        topicTitle: 'Assessment of Entrepreneurial Qualities',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Successful entrepreneurs show particular qualities and businesses are assessed against key success factors.',
                sections: [
                    { variant: 'indigo', heading: 'Qualities', bullets: ['Confidence', 'Passion & perseverance', 'Creativity', 'Opportunity-seeking', 'Customer focus', 'Risk-taking'] },
                ],
            },
            {
                key: 'success',
                label: 'Success factors',
                sections: [
                    { variant: 'green', heading: 'Key success factors', bullets: ['Sustainability', 'Profitability', 'A solid customer base', 'Good governance'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_citizenship_responsibilities',
        modePrefix: 'grade11_bs_citizenship_responsibilities',
        topicTitle: 'Citizenship & Responsibilities',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Citizenship brings rights and responsibilities, and businesses contribute to community development.',
                sections: [
                    { variant: 'indigo', heading: 'Citizenship', text: 'Being part of a country with its rights, privileges and duties.' },
                    { variant: 'note', heading: 'Why businesses get involved', text: 'BBBEE compliance, skills shortages and social issues such as HIV/AIDS.' },
                ],
            },
            {
                key: 'institutions',
                label: 'Institutions',
                sections: [
                    { variant: 'green', heading: 'Role players', bullets: ['Individual business practitioners', 'Civil society', 'NGOs', 'CBOs'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_business_plan_transformation',
        modePrefix: 'grade11_bs_business_plan_transformation',
        topicTitle: 'Transforming a Business Plan into an Action Plan',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'A business plan sets the goals; an action plan breaks them into tasks with timing.',
                sections: [
                    { variant: 'indigo', heading: 'Business vs action plan', text: 'A business plan describes goals and methods; an action plan is a checklist of tasks to achieve them.' },
                ],
            },
            {
                key: 'tools',
                label: 'Planning tools',
                sections: [
                    { variant: 'green', heading: 'Tools', bullets: ['Gantt chart (visual schedule)', 'Work Breakdown Structure (WBS)', 'Timelines (chronological)'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_start_business_venture',
        modePrefix: 'grade11_bs_start_business_venture',
        topicTitle: 'Starting a Business Venture',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Before start-up, entrepreneurs consider key factors and how to fund the venture.',
                sections: [
                    { variant: 'indigo', heading: 'Initiation aspects', bullets: ['Strategy', 'Operations', 'Productivity', 'Size of the business'] },
                ],
            },
            {
                key: 'funding',
                label: 'Funding',
                sections: [
                    { variant: 'green', heading: 'Choice of funding', bullets: ['Amount of capital needed', 'Cost of finance', 'Risk', 'Nature of the finance'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade11_bs_presentation_of_information',
        modePrefix: 'grade11_bs_presentation_of_information',
        topicTitle: 'Presentation of Business Information',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses present information verbally and non-verbally, supported by visual aids and written reports.',
                sections: [
                    { variant: 'indigo', heading: 'Verbal vs non-verbal', text: 'Verbal presentations use speech; non-verbal presentations use no spoken words.' },
                ],
            },
            {
                key: 'visual-aids',
                label: 'Visual aids',
                sections: [
                    { variant: 'green', heading: 'Visual aids', bullets: ['Graphs', 'Tables', 'Diagrams', 'Posters', 'Handouts', 'Transparencies/slides'] },
                ],
            },
            {
                key: 'reports',
                label: 'Reports',
                sections: [
                    { variant: 'blue', heading: 'Report writing steps', bullets: ['Plan the purpose & audience', 'Gather & analyse data', 'Structure the report', 'Write clearly', 'Review & edit'] },
                ],
            },
        ],
    },
];

export const grade11BusinessStudiesExtraRegistry = EXTRA_TOPICS.reduce((acc, topic) => {
    return { ...acc, ...createGrade11BSTopicRegistry(topic) };
}, {});

export const grade11BusinessStudiesExtraTopics = EXTRA_TOPICS;
