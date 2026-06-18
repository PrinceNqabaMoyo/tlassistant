import React from 'react';
import TopicModeCard from './TopicModeCard';
import {
    isGrade10BSMicroEnvironment,
    isGrade10BSBusinessFunctions,
    isGrade10BSMarketEnvironment,
    isGrade10BSMacroEnvironment,
    isGrade10BSInterrelationship,
    isGrade10BSBusinessSectors,
    isGrade10BSSocioEconomic,
    isGrade10BSSocialResponsibility,
    isGrade10BSEntrepreneurial,
    isGrade10BSFormsOfOwnership,
    isGrade10BSConceptOfQuality,
    isGrade11BSInfluences,
    isGrade11BSChallenges,
} from '../topicMatchers';

const BusinessStudiesTopicModeCards = ({ selectedTopic, selectedTopicDisplayName, getTopicTerm, navigateToWorkspaceWithMode, flags }) => {
    const topicName = selectedTopic?.name;
    if (!topicName) return null;

    const cards = [
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSMicroEnvironment(topicName),
            title: 'Topic 1: Micro Environment',
            description: 'Term 1. Internal environment of the business, Vision/Mission/Goals/Objectives, Organisational culture & resources, Eight business functions, and levels/tasks of management.',
            scaffoldMode: 'grade10_bs_micro_environment_scaffold',
            scaffoldLabel: 'Micro Environment • Scaffold',
            practiceMode: 'grade10_bs_micro_environment_practice',
            practiceLabel: 'Micro Environment • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSBusinessFunctions(topicName),
            title: 'Topic 2: Business Functions',
            description: 'Term 1. Focus on General Management, Administration, Financial, Purchasing, and Public Relations. Understanding the roles and differences between management and leadership.',
            scaffoldMode: 'grade10_bs_business_functions_scaffold',
            scaffoldLabel: 'Business functions • Scaffold',
            practiceMode: 'grade10_bs_business_functions_practice',
            practiceLabel: 'Business functions • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSMarketEnvironment(topicName),
            title: 'Topic 3: Market Environment',
            description: 'Term 1. External forces directly affecting the business. Consumers, suppliers, intermediaries, competitors, civil society, NGOs, CBOs, and regulators.',
            scaffoldMode: 'grade10_bs_market_environment_scaffold',
            scaffoldLabel: 'Market Environment • Scaffold',
            practiceMode: 'grade10_bs_market_environment_practice',
            practiceLabel: 'Market Environment • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSMacroEnvironment(topicName),
            title: 'Topic 4: Macro Environment',
            description: 'Term 1. External forces beyond business control. PESTLE analysis (Political, Economic, Social, Technological, Legal, Environmental).',
            scaffoldMode: 'grade10_bs_macro_environment_scaffold',
            scaffoldLabel: 'Macro Environment • Scaffold',
            practiceMode: 'grade10_bs_macro_environment_practice',
            practiceLabel: 'Macro Environment • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSInterrelationship(topicName),
            title: 'Topic 5: Interrelationship of Environments',
            description: 'Term 1. How micro, market and macro environments interact and influence each other.',
            scaffoldMode: 'grade10_bs_interrelationship_scaffold',
            scaffoldLabel: 'Interrelationship of environments • Scaffold',
            practiceMode: 'grade10_bs_interrelationship_practice',
            practiceLabel: 'Interrelationship of environments • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSBusinessSectors(topicName),
            title: 'Topic 6: Business Sectors',
            description: 'Term 1. Primary, Secondary and Tertiary sectors. Formal vs informal sectors, and public vs private sectors.',
            scaffoldMode: 'grade10_bs_business_sectors_scaffold',
            scaffoldLabel: 'Business sectors • Scaffold',
            practiceMode: 'grade10_bs_business_sectors_practice',
            practiceLabel: 'Business sectors • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSSocioEconomic(topicName),
            title: 'Topic 7: Socio-economic Issues',
            description: 'Term 2. Poverty, inequality, inclusivity, unemployment, HIV/Aids, gambling, piracy, counterfeiting, strikes, violence, and crime.',
            scaffoldMode: 'grade10_bs_socio_economic_issues_scaffold',
            scaffoldLabel: 'Socio-economic Issues • Scaffold',
            practiceMode: 'grade10_bs_socio_economic_issues_practice',
            practiceLabel: 'Socio-economic Issues • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSSocialResponsibility(topicName),
            title: 'Topic 8: Social Responsibility',
            description: 'Term 2. Initiatives businesses take to improve the well-being of the community and environment. CSI projects.',
            scaffoldMode: 'grade10_bs_social_responsibility_scaffold',
            scaffoldLabel: 'Social responsibility • Scaffold',
            practiceMode: 'grade10_bs_social_responsibility_practice',
            practiceLabel: 'Social responsibility • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSEntrepreneurial(topicName),
            title: 'Topic 9: Entrepreneurial Qualities',
            description: 'Term 2. Key characteristics of successful entrepreneurs, identifying business opportunities, and assessing feasibility.',
            scaffoldMode: 'grade10_bs_entrepreneurial_qualities_scaffold',
            scaffoldLabel: 'Entrepreneurial qualities • Scaffold',
            practiceMode: 'grade10_bs_entrepreneurial_qualities_practice',
            practiceLabel: 'Entrepreneurial qualities • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(topicName),
            title: 'Topic 10: Forms of Ownership',
            description: 'Term 2. Sole traders, partnerships, close corporations, companies (private, public, personal liability, state-owned), and cooperatives.',
            scaffoldMode: 'grade10_bs_forms_of_ownership_scaffold',
            scaffoldLabel: 'Forms of Ownership • Scaffold',
            practiceMode: 'grade10_bs_forms_of_ownership_practice',
            practiceLabel: 'Forms of Ownership • Practice',
        },
        {
            condition: flags.isGrade10BusinessStudies && isGrade10BSConceptOfQuality(topicName),
            title: 'Topic 11: Concept of Quality',
            description: 'Term 2. Quality control vs quality assurance, SABS, ISO, and total quality management (TQM).',
            scaffoldMode: 'grade10_bs_concept_of_quality_scaffold',
            scaffoldLabel: 'Concept of Quality • Scaffold',
            practiceMode: 'grade10_bs_concept_of_quality_practice',
            practiceLabel: 'Concept of Quality • Practice',
        },
        {
            condition: flags.isGrade11BusinessStudies && (isGrade11BSInfluences(topicName) || isGrade11BSChallenges(topicName)),
            title: selectedTopicDisplayName,
            description: `${getTopicTerm(topicName)}. Choose a mode to begin. Scaffold follows the guided step sequence for concepts, application, and discussion with hints and memo comparison. Practice lets you choose a subskill or use mixed practice for a marked review flow.`,
            scaffoldMode: isGrade11BSInfluences(topicName)
                ? 'grade11_bs_influences_on_business_environments_scaffold'
                : 'grade11_bs_challenges_of_the_business_environments_scaffold',
            scaffoldLabel: `${selectedTopicDisplayName} • Scaffold`,
            practiceMode: isGrade11BSInfluences(topicName)
                ? 'grade11_bs_influences_on_business_environments_practice'
                : 'grade11_bs_challenges_of_the_business_environments_practice',
            practiceLabel: `${selectedTopicDisplayName} • Practice`,
        },
    ];

    const card = cards.find((entry) => entry.condition);
    if (!card) return null;

    return (
        <TopicModeCard
            title={card.title}
            description={card.description}
            onStartScaffold={() => navigateToWorkspaceWithMode(card.scaffoldMode, card.scaffoldLabel)}
            onStartPractice={() => navigateToWorkspaceWithMode(card.practiceMode, card.practiceLabel)}
            containerClassName={card.containerClassName}
            titleClassName={card.titleClassName}
            descriptionClassName={card.descriptionClassName}
            scaffoldButtonClassName={card.scaffoldButtonClassName}
            practiceButtonClassName={card.practiceButtonClassName}
        />
    );
};

export default BusinessStudiesTopicModeCards;
