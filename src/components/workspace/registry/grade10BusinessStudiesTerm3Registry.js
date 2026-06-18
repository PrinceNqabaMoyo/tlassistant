import { createGrade10BSTopicRegistry } from '../grade10/business-studies/shared/createGrade10BSRoute';

const TERM3_TOPICS = [
    {
        topicKey: 'grade10_bs_creative_thinking',
        modePrefix: 'grade10_bs_creative_thinking',
        topicTitle: 'Creative Thinking & Problem Solving',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Creative thinking helps a business generate new ideas, while problem solving applies a structured process to overcome challenges.',
                sections: [
                    { variant: 'indigo', heading: 'Creative thinking', text: 'The ability to generate original, unusual or useful ideas by looking at situations in new ways.' },
                    { variant: 'note', heading: 'Problem solving', text: 'A step-by-step process used to identify, analyse and resolve a business problem.' },
                ],
            },
            {
                key: 'techniques',
                label: 'Techniques',
                sections: [
                    { variant: 'green', heading: 'Problem-solving techniques', bullets: ['Brainstorming', 'Mind-mapping', 'Nominal group technique', 'Force-field analysis', 'Delphi technique', 'SCAMPER', 'Empty chair'] },
                    { variant: 'note', heading: 'The cycle', text: 'Identify the problem, generate alternatives, evaluate options, choose and implement a solution, then review the outcome.' },
                ],
            },
            {
                key: 'benefits',
                label: 'Benefits',
                sections: [
                    { variant: 'blue', heading: 'Why it matters', bullets: ['Gives a competitive advantage', 'Improves productivity and innovation', 'Helps the business adapt to change', 'Encourages teamwork and participation'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade10_bs_business_opportunities',
        modePrefix: 'grade10_bs_business_opportunities',
        topicTitle: 'Business Opportunities & Related Factors',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'A business opportunity is an idea that a person can turn into a business to generate income. Needs and desires of a target market create that opportunity.',
                sections: [
                    { variant: 'indigo', heading: 'Business opportunity', text: 'A favourable set of circumstances that creates the need for a new product or service.' },
                    { variant: 'note', heading: 'Market research', text: 'The process of gathering and analysing information about a target market to reduce risk and make informed decisions.' },
                ],
            },
            {
                key: 'research',
                label: 'Research',
                sections: [
                    { variant: 'green', heading: 'Research instruments', bullets: ['Surveys', 'Interviews', 'Questionnaires', 'Observations', 'Experiments'] },
                    { variant: 'note', heading: 'Internal vs external research', text: 'Internal research uses data already inside the business; external research collects new data from outside the business.' },
                ],
            },
            {
                key: 'swot',
                label: 'SWOT',
                sections: [
                    { variant: 'blue', heading: 'SWOT analysis', bullets: ['Strengths (internal, positive)', 'Weaknesses (internal, negative)', 'Opportunities (external, positive)', 'Threats (external, negative)'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade10_bs_business_location',
        modePrefix: 'grade10_bs_business_location',
        topicTitle: 'Business Location Decisions',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Choosing the right location is one of the most important decisions a business makes because it affects costs, customers and long-term success.',
                sections: [
                    { variant: 'indigo', heading: 'Why location matters', text: 'A good location attracts customers, lowers costs and gives access to labour and suppliers.' },
                ],
            },
            {
                key: 'factors',
                label: 'Factors',
                sections: [
                    { variant: 'green', heading: 'Factors that impact location', bullets: ['Proximity to the market/customers', 'Availability and cost of labour', 'Access to raw materials and suppliers', 'Transport and infrastructure', 'Cost of premises/rent and tax rebates', 'Safety, competition and legislation'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade10_bs_contracts',
        modePrefix: 'grade10_bs_contracts',
        topicTitle: 'Contracts',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'A contract is a legally binding agreement between two or more parties that creates rights and obligations.',
                sections: [
                    { variant: 'indigo', heading: 'Parties to a contract', text: 'The people or organisations who agree to the terms, e.g. lessor and lessee, employer and employee.' },
                    { variant: 'note', heading: 'Types of contracts', bullets: ['Employment contract', 'Lease/rental agreement', 'Sale agreement', 'Insurance contract'] },
                ],
            },
            {
                key: 'requirements',
                label: 'Legal requirements',
                sections: [
                    { variant: 'green', heading: 'For a contract to be valid', bullets: ['Contractual capacity of both parties', 'Agreement reached by both parties (consensus)', 'The performance must be legally possible', 'Terms must be reasonable and lawful', 'Legal formalities complied with', 'Not vague or unclear'] },
                ],
            },
            {
                key: 'termination',
                label: 'Termination',
                sections: [
                    { variant: 'blue', heading: 'How a contract ends', bullets: ['Proper performance of obligations', 'Mutual agreement', 'Expiry of the agreed period', 'Breach of contract'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade10_bs_presentation',
        modePrefix: 'grade10_bs_presentation',
        topicTitle: 'Presentation of Business Information',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'Businesses present information through written reports and verbal presentations supported by visual aids.',
                sections: [
                    { variant: 'indigo', heading: 'Business reports', text: 'A formal document that presents information, analysis and recommendations in a clear, structured way.' },
                ],
            },
            {
                key: 'visual-aids',
                label: 'Visual aids',
                sections: [
                    { variant: 'green', heading: 'Examples', bullets: ['Graphs and charts', 'Diagrams and tables', 'Symbols and pictures', 'Data projectors and interactive whiteboards', 'Video conferencing'] },
                    { variant: 'note', heading: 'Advantages', text: 'Make information easier to understand, keep the audience interested and summarise complex data.' },
                ],
            },
            {
                key: 'preparing',
                label: 'Preparing',
                sections: [
                    { variant: 'blue', heading: 'Factors to consider', bullets: ['Know your audience', 'Keep slides clear and uncluttered', 'Maintain eye contact and good body language', 'Stay within the time limit', 'Prepare for questions'] },
                ],
            },
        ],
    },
    {
        topicKey: 'grade10_bs_business_plans',
        modePrefix: 'grade10_bs_business_plans',
        topicTitle: 'Understanding Business Plans',
        visualAidsTabs: [
            {
                key: 'overview',
                label: 'Overview',
                intro: 'A business plan is a written document that describes the business, its goals and the strategies used to achieve them. It is used to attract investors and guide the business.',
                sections: [
                    { variant: 'indigo', heading: 'Importance', bullets: ['Attracts investors and finance', 'Sets clear goals and direction', 'Helps measure progress', 'Reduces risk through planning'] },
                ],
            },
            {
                key: 'components',
                label: 'Components',
                sections: [
                    { variant: 'green', heading: 'Components of a business plan', bullets: ['Executive summary', 'Vision, mission, goals and objectives', 'Description of products/services', 'Marketing plan and market research', 'Operational and financial plan', 'Legal requirements and forms of ownership'] },
                ],
            },
            {
                key: 'pestle',
                label: 'PESTLE',
                sections: [
                    { variant: 'blue', heading: 'PESTLE analysis', bullets: ['Political', 'Economic', 'Social', 'Technological', 'Legal', 'Environmental'] },
                ],
            },
        ],
    },
];

export const grade10BusinessStudiesTerm3Registry = TERM3_TOPICS.reduce((acc, topic) => {
    return { ...acc, ...createGrade10BSTopicRegistry(topic) };
}, {});

export const grade10BusinessStudiesTerm3Topics = TERM3_TOPICS;
