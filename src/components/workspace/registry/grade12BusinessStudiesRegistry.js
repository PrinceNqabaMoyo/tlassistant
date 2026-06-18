import { createGrade12BSTopicRegistry } from '../grade12/business-studies/shared/createGrade12BSRoute';

// Grade 12 Business Studies topics built on the config-driven shared layer.
// All 15 topics (Terms 1-3) are declared declaratively here and reduced into
// scaffold + practice registry entries by createGrade12BSTopicRegistry.
const TOPICS = [
    // ----- Term 1 -----
    {
        topicKey: 'grade12_bs_creative_thinking_problem_solving',
        modePrefix: 'grade12_bs_creative_thinking_problem_solving',
        topicTitle: 'Creative Thinking & Problem Solving',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses use structured problem-solving and creative thinking to overcome challenges and innovate.',
                sections: [
                    { variant: 'indigo', heading: 'Problem solving vs decision making', text: 'Problem solving works through a process to remove a challenge; decision making selects the best option.' },
                    { variant: 'note', heading: 'Creative thinking', text: 'Generating original, non-conventional ideas to solve problems.' },
                ],
            },
            {
                key: 'techniques',
                label: 'Techniques',
                sections: [
                    { variant: 'green', heading: 'Problem-solving techniques', bullets: ['Delphi Technique (experts)', 'Force Field Analysis (forces for/against)', 'Nominal Group Technique', 'Brainstorming', 'Mind-mapping'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_ethics_and_professionalism',
        modePrefix: 'grade12_bs_ethics_and_professionalism',
        topicTitle: 'Ethics & Professionalism',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Ethics is acting on moral principles; professionalism is conducting business to high standards.',
                sections: [
                    { variant: 'indigo', heading: 'Corporate governance', text: 'The system of rules and practices by which a business is directed and controlled.' },
                    { variant: 'note', heading: 'King Code', text: 'South African code of corporate governance promoting ethical, effective leadership.' },
                ],
            },
            {
                key: 'unethical',
                label: 'Unethical issues',
                sections: [
                    { variant: 'green', heading: 'Examples', bullets: ['Corruption & bribery', 'Price fixing', 'Unfair advertising', 'Sexual harassment', 'Nepotism'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_macro_environment_strategies',
        modePrefix: 'grade12_bs_macro_environment_strategies',
        topicTitle: 'Macro Environment: Business Strategies',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses analyse the environment with strategic tools and choose strategies to respond.',
                sections: [
                    { variant: 'indigo', heading: 'Analysis tools', bullets: ["Porter's Five Forces", 'PESTLE analysis', 'SWOT analysis'] },
                ],
            },
            {
                key: 'strategies',
                label: 'Strategies',
                sections: [
                    { variant: 'green', heading: 'Types of strategies', bullets: ['Integration (forward/backward/horizontal)', 'Intensive (market penetration/development)', 'Diversification', 'Defensive (retrenchment/divestiture)'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_impact_of_legislation',
        modePrefix: 'grade12_bs_impact_of_legislation',
        topicTitle: 'Impact of Recent Legislation',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Several Acts govern employment, equity and consumer protection in South Africa.',
                sections: [
                    { variant: 'indigo', heading: 'Key Acts', bullets: ['Basic Conditions of Employment Act (BCEA)', 'Labour Relations Act (LRA)', 'Employment Equity Act (EEA)', 'Skills Development Act (SDA)'] },
                ],
            },
            {
                key: 'bbbee',
                label: 'BBBEE',
                sections: [
                    { variant: 'green', heading: 'BBBEE pillars', bullets: ['Ownership', 'Management control', 'Skills development', 'Enterprise & supplier development', 'Socio-economic development'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_human_resources_function',
        modePrefix: 'grade12_bs_human_resources_function',
        topicTitle: 'Human Resources Function',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The HR function recruits, selects and contracts employees to meet the business\u2019s needs.',
                sections: [
                    { variant: 'indigo', heading: 'Recruitment', text: 'Attracting suitable candidates internally or externally.' },
                    { variant: 'note', heading: 'Selection', text: 'Choosing the best candidate through screening, interviews and checks.' },
                ],
            },
            {
                key: 'contracts',
                label: 'Contracts & benefits',
                sections: [
                    { variant: 'green', heading: 'Employment contract', bullets: ['Job title & duties', 'Remuneration', 'Working hours', 'Leave', 'Termination terms'] },
                    { variant: 'blue', heading: 'Fringe benefits', bullets: ['Medical aid', 'Pension/provident fund', 'Housing/transport allowances'] },
                ],
            },
        ],
    },
    // ----- Term 2 -----
    {
        topicKey: 'grade12_bs_business_sectors_environments',
        modePrefix: 'grade12_bs_business_sectors_environments',
        topicTitle: 'Business Sectors & their Environments',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The economy has three sectors, and businesses operate within three environments with differing control.',
                sections: [
                    { variant: 'indigo', heading: 'Three sectors', bullets: ['Primary (extract)', 'Secondary (manufacture)', 'Tertiary (services)'] },
                ],
            },
            {
                key: 'environments',
                label: 'Environments',
                sections: [
                    { variant: 'green', heading: 'Control', bullets: ['Micro (full control)', 'Market (partial control)', 'Macro (no control, adapt)'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_quality_of_performance',
        modePrefix: 'grade12_bs_quality_of_performance',
        topicTitle: 'Quality of Performance',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Quality management ensures consistently high standards across the business.',
                sections: [
                    { variant: 'indigo', heading: 'Control vs assurance', text: 'Quality control inspects the final product; quality assurance prevents defects during production.' },
                    { variant: 'note', heading: 'TQM', text: 'An integrated, organisation-wide approach to delivering quality.' },
                ],
            },
            {
                key: 'tqm',
                label: 'TQM elements',
                sections: [
                    { variant: 'green', heading: 'Elements', bullets: ['Total client satisfaction', 'Continuous skills development', 'Continuous improvement', 'Adequate financing', 'Monitoring & evaluation'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_management_and_leadership',
        modePrefix: 'grade12_bs_management_and_leadership',
        topicTitle: 'Management & Leadership',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Leadership inspires people while management organises resources; styles suit different situations.',
                sections: [
                    { variant: 'indigo', heading: 'Leadership styles', bullets: ['Autocratic', 'Democratic', 'Laissez-faire', 'Transactional', 'Charismatic'] },
                ],
            },
            {
                key: 'theories',
                label: 'Theories',
                sections: [
                    { variant: 'green', heading: 'Theories', bullets: ['Situational leadership', 'Transformational leadership', 'Transactional leadership', 'Leaders & followers'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_investment_securities',
        modePrefix: 'grade12_bs_investment_securities',
        topicTitle: 'Investment: Securities',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'The JSE provides a market to trade shares and securities; investors weigh risk, return and liquidity.',
                sections: [
                    { variant: 'indigo', heading: 'Shares', text: 'Ordinary shares carry votes and variable dividends; preference shares earn a fixed dividend, paid first.' },
                ],
            },
            {
                key: 'forms',
                label: 'Forms of investment',
                sections: [
                    { variant: 'green', heading: 'Options', bullets: ['Unit trusts', 'RSA Retail Savings Bonds', 'Fixed deposits', 'Shares'] },
                    { variant: 'note', heading: 'Interest', text: 'Simple interest is on the principal only; compound interest is on principal plus interest.' },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_investment_insurance',
        modePrefix: 'grade12_bs_investment_insurance',
        topicTitle: 'Investment: Insurance',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Insurance covers uncertain events; assurance covers certain events. Principles govern valid cover.',
                sections: [
                    { variant: 'indigo', heading: 'Insurance vs assurance', text: 'Insurance: event may happen (fire/theft). Assurance: event will happen (death).' },
                ],
            },
            {
                key: 'principles',
                label: 'Principles',
                sections: [
                    { variant: 'green', heading: 'Principles', bullets: ['Indemnity', 'Utmost good faith', 'Insurable interest', 'Average clause (under-insurance)'] },
                    { variant: 'blue', heading: 'Compulsory insurance', bullets: ['UIF', 'COIDA', 'Road Accident Fund'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_team_performance_conflict',
        modePrefix: 'grade12_bs_team_performance_conflict',
        topicTitle: 'Team Performance & Conflict Management',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Teams develop through stages and perform best when key criteria are met and conflict is well managed.',
                sections: [
                    { variant: 'indigo', heading: 'Stages of development', bullets: ['Forming', 'Storming', 'Norming', 'Performing', 'Adjourning'] },
                ],
            },
            {
                key: 'criteria',
                label: 'Criteria & conflict',
                sections: [
                    { variant: 'green', heading: 'Performance criteria', bullets: ['Shared values', 'Communication', 'Collaboration', 'Positive interpersonal behaviour'] },
                    { variant: 'blue', heading: 'Conflict resolution', bullets: ['Acknowledge & find the cause', 'Discuss openly', 'Listen actively', 'Agree a solution', 'Follow up'] },
                ],
            },
        ],
    },
    // ----- Term 3 -----
    {
        topicKey: 'grade12_bs_human_rights_inclusivity',
        modePrefix: 'grade12_bs_human_rights_inclusivity',
        topicTitle: 'Human Rights, Inclusivity & Environment',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses must uphold human rights, manage diversity and protect health and the environment.',
                sections: [
                    { variant: 'indigo', heading: 'Human rights', bullets: ['Equality', 'Dignity', 'Privacy', 'Safety'] },
                ],
            },
            {
                key: 'diversity',
                label: 'Diversity',
                sections: [
                    { variant: 'green', heading: 'Diversity issues', bullets: ['Race', 'Gender', 'Age', 'Language', 'Culture/religion', 'Disability'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_social_responsibility_csr_csi',
        modePrefix: 'grade12_bs_social_responsibility_csr_csi',
        topicTitle: 'Social Responsibility & Corporate Citizenship',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses contribute to society through CSR and CSI, measured by the triple bottom line.',
                sections: [
                    { variant: 'indigo', heading: 'Triple bottom line', text: 'People (social), planet (environmental) and profit (economic).' },
                    { variant: 'note', heading: 'CSR vs CSI', text: 'CSR is core strategy that may benefit the business; CSI uplifts communities with no direct benefit.' },
                ],
            },
            {
                key: 'issues',
                label: 'Socio-economic issues',
                sections: [
                    { variant: 'green', heading: 'Issues', bullets: ['Unemployment', 'Poverty', 'HIV/AIDS'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_presentation_data_responses',
        modePrefix: 'grade12_bs_presentation_data_responses',
        topicTitle: 'Presentation & Data Responses',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Effective presentations are prepared, well delivered and handle feedback professionally.',
                sections: [
                    { variant: 'indigo', heading: 'Verbal vs non-verbal', text: 'Verbal presentations use speech; non-verbal use reports, graphs and images.' },
                ],
            },
            {
                key: 'visual',
                label: 'Visual aids & feedback',
                sections: [
                    { variant: 'green', heading: 'Visual aids', bullets: ['Data projector / PowerPoint', 'Handouts', 'Graphs & tables', 'Multimedia'] },
                    { variant: 'blue', heading: 'Handling feedback', bullets: ['Stay calm', 'Listen fully', 'Answer factually', 'Follow up if unsure'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade12_bs_forms_of_ownership_success',
        modePrefix: 'grade12_bs_forms_of_ownership_success',
        topicTitle: 'Forms of Ownership: Success & Failure',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Each form of ownership has criteria that contribute to its success or failure.',
                sections: [
                    { variant: 'indigo', heading: 'Liability', text: 'Limited liability protects personal assets; unlimited liability puts them at risk.' },
                ],
            },
            {
                key: 'criteria',
                label: 'Success criteria',
                sections: [
                    { variant: 'green', heading: 'Criteria', bullets: ['Capital', 'Taxation', 'Division of profits', 'Management', 'Legislation', 'Continuity'] },
                ],
            },
        ],
    },
];

export const grade12BusinessStudiesRegistry = TOPICS.reduce((acc, topic) => {
    return { ...acc, ...createGrade12BSTopicRegistry(topic) };
}, {});

export const grade12BusinessStudiesTopics = TOPICS;
