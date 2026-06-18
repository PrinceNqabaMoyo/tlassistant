import { hasStructuredTopicOrdering } from './subjectFlags';
import {
    normalizeTopicName,
    isWholeNumbersTopic,
    isIntegersTopic,
    isFractionsTopic,
    isDecimalNotationTopic,
    isExponentsTopic,
    isPatternsTopic,
    isPatternsSequencesTopic,
    isPatternsSequencesSeriesTopic,
    isGrade12FunctionsTopic,
    isGrade12FinanceTopic,
    isGrade12TrigonometryTopic,
    isFunctionsRelationshipsTopic,
    isAlgebraicExpressionsTopic,
    isAlgebraicEquationsTopic,
    isEquationsInequalitiesTopic,
    isTrigonometry1Topic,
    isGrade10IndigenousBookkeepingTopic,
    isGrade10EthicsTopic,
    isGrade10GAAPTopic,
    isGrade10InternalControlsTopic,
    isGrade10SoleTraderTopic,
    isGrade10SalariesWagesTopic,
    isGrade10FinalAccountsTopic,
    isGrade10VATTopic,
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
    isGrade11BSAdapting,
    isGrade11BSContemporarySocioEconomic,
    isGrade11BSBusinessSectors,
    isGrade11BSBenefitsOfCompany,
    isGrade11BSAvenues,
    isGrade11BSCreativeThinking,
    isGrade11BSStressCrisisChange,
    isGrade11BSMarketingFunction,
    isGrade11BSProductionFunction,
    isGrade11BSProfessionalismEthics,
    isGrade12BSCreativeThinking,
    isGrade12BSEthicsProfessionalism,
    isGrade12BSMacroEnvironmentStrategies,
    isGrade12BSImpactOfLegislation,
    isGrade12BSHumanResourcesFunction,
    isGrade12BSBusinessSectorsEnvironments,
    isGrade12BSQualityOfPerformance,
    isGrade12BSManagementLeadership,
    isGrade12BSInvestmentSecurities,
    isGrade12BSInvestmentInsurance,
    isGrade12BSTeamPerformanceConflict,
    isGrade12BSHumanRightsInclusivity,
    isGrade12BSSocialResponsibilityCsr,
    isGrade12BSPresentationDataResponses,
    isGrade12BSFormsOfOwnershipSuccess,
    isExponentsSurdsTopic,
    isAnalyticalGeometryTopic,
    isGeoConstructionTopic,
    isGeo2DShapesTopic,
    isGeoStraightLinesTopic,
} from './topicMatchers';

export const getTopicDisplayName = (topicName, flags) => {
    if (flags.isGrade10Accounting && isGrade10IndigenousBookkeepingTopic(topicName)) return 'Informal / Indigenous bookkeeping';
    if (flags.isGrade10Accounting && isGrade10EthicsTopic(topicName)) return 'Ethics';
    if (flags.isGrade10Accounting && isGrade10GAAPTopic(topicName)) return 'GAAP';
    if (flags.isGrade10Accounting && isGrade10InternalControlsTopic(topicName)) return 'Internal Controls';
    if (flags.isGrade10Accounting && isGrade10FinalAccountsTopic(topicName)) return 'Final Accounts & Year-end';
    if (flags.isGrade10Accounting && isGrade10SoleTraderTopic(topicName)) return 'Financial accounting and bookkeeping of a sole trader';
    if (flags.isGrade10Accounting && isGrade10VATTopic(topicName)) return 'Value Added Tax (VAT)';
    if (flags.isGrade10Accounting && isGrade10SalariesWagesTopic(topicName)) return 'Salaries & Wages Journal';

    if (flags.isGrade10BusinessStudies && isGrade10BSMicroEnvironment(topicName)) return 'Components of the micro environment';
    if (flags.isGrade10BusinessStudies && isGrade10BSBusinessFunctions(topicName)) return 'Business functions and the activities of the business';
    if (flags.isGrade10BusinessStudies && isGrade10BSMarketEnvironment(topicName)) return 'The market environment';
    if (flags.isGrade10BusinessStudies && isGrade10BSMacroEnvironment(topicName)) return 'The macro environment';
    if (flags.isGrade10BusinessStudies && isGrade10BSInterrelationship(topicName)) return 'The interrelationship of the micro, market and macro environments';
    if (flags.isGrade10BusinessStudies && isGrade10BSBusinessSectors(topicName)) return 'Business sectors';
    if (flags.isGrade10BusinessStudies && isGrade10BSSocioEconomic(topicName)) return 'Contemporary socio-economic issues';
    if (flags.isGrade10BusinessStudies && isGrade10BSSocialResponsibility(topicName)) return 'Social responsibility';
    if (flags.isGrade10BusinessStudies && isGrade10BSEntrepreneurial(topicName)) return 'Entrepreneurial qualities';
    if (flags.isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(topicName)) return 'Forms of ownership';
    if (flags.isGrade10BusinessStudies && isGrade10BSConceptOfQuality(topicName)) return 'The concept of quality';

    if (flags.isGrade10Math && isAlgebraicExpressionsTopic(topicName)) return 'Algebraic expressions';
    if (flags.isGrade10Math && isExponentsTopic(topicName)) return 'Exponents';
    if (flags.isGrade10Math && isPatternsSequencesTopic(topicName)) return 'Patterns and sequences';
    if (flags.isGrade10Math && isEquationsInequalitiesTopic(topicName)) return 'Equations and inequalities';
    if (flags.isGrade10Math && isTrigonometry1Topic(topicName)) return 'Trigonometry 1';

    if (flags.isGrade11Math && isExponentsSurdsTopic(topicName)) return 'Exponents and surds';
    if (flags.isGrade11Math && isAnalyticalGeometryTopic(topicName)) return 'Analytical geometry';

    if (flags.isGrade12Math && isPatternsSequencesSeriesTopic(topicName)) return 'Sequences and series';
    if (flags.isGrade12Math && isGrade12FunctionsTopic(topicName)) return 'Functions';
    if (flags.isGrade12Math && isGrade12FinanceTopic(topicName)) return 'Finance';
    if (flags.isGrade12Math && isGrade12TrigonometryTopic(topicName)) return 'Trigonometry';

    if (flags.isGrade8Math && isFunctionsRelationshipsTopic(topicName)) return 'Functions and relationships 1';
    if (flags.isGrade8Math && isAlgebraicExpressionsTopic(topicName)) return 'Algebraic expressions 1';
    if (flags.isGrade9Math && isFunctionsRelationshipsTopic(topicName)) return 'Functions and relationships 1';
    if (flags.isGrade9Math && isAlgebraicExpressionsTopic(topicName)) return 'Algebraic expressions 1';
    if (flags.isGrade9Math && isAlgebraicEquationsTopic(topicName)) return 'Algebraic equations 1';
    if (flags.isGrade8Math && isAlgebraicEquationsTopic(topicName)) return 'Algebraic equations 1';

    return topicName;
};

export const getCoveredTopicIndex = (topicName, flags) => {
    const normalized = normalizeTopicName(topicName);

    const mapping = flags.isGrade7Math
        ? {
            'working with whole numbers': 1,
            'whole numbers': 1,
            'exponents': 2,
            'construction of geometric figures': 3,
            'construction of geometric figure': 3,
            'geometry of 2d shapes': 4,
            'geometry of straight lines': 5,
        }
        : flags.isGrade8Math
            ? {
                'whole numbers': 1,
                'integers': 2,
                'exponents': 3,
                'numeric and geometric patterns': 4,
                'functions and relationships': 5,
                'functions and relationships 1': 5,
                'algebraic expressions': 6,
                'algebraic expressions 1': 6,
                'algebraic equations': 7,
                'algebraic equations 1': 7,
            }
            : flags.isGrade9Math
                ? {
                    'whole numbers': 1,
                    'integers': 2,
                    'fractions': 3,
                    'the decimal notation for fractions': 4,
                    'decimal notation for fractions': 4,
                    'fractions in decimal notation': 4,
                    'decimal notation': 4,
                    'exponents': 5,
                    'numeric and geometric patterns': 6,
                    'numeric & geometric patterns': 6,
                    'patterns': 6,
                    'functions and relationships': 7,
                    'functions & relationships': 7,
                    'algebraic expressions': 8,
                    'algebraic expressions 1': 8,
                    'algebraic equations': 9,
                    'algebraic equations 1': 9,
                }
                : flags.isGrade10Math
                    ? {
                        'algebraic expressions': 1,
                        'algebraic expression': 1,
                        'exponents': 2,
                        'patterns and sequences': 3,
                        'patterns & sequences': 3,
                        'patterns': 3,
                        'sequences': 3,
                        'equations and inequalities': 4,
                        'equations & inequalities': 4,
                        'inequalities': 4,
                        'trigonometry 1': 5,
                        'trigonometry1': 5,
                        'trigonometry': 5,
                    }
                    : flags.isGrade11Math
                        ? {
                            'exponents and surds': 1,
                            'exponents & surds': 1,
                            'exponents surds': 1,
                            'exponents-and-surds': 1,
                            'equations and inequalities': 2,
                            'equations & inequalities': 2,
                            'equations-and-inequalities': 2,
                            'patterns and sequences': 3,
                            'patterns & sequences': 3,
                            'patterns': 3,
                            'sequences': 3,
                            'analytical geometry': 4,
                            'analytic geometry': 4,
                            'analytical-geometry': 4,
                        }
                        : flags.isGrade12Math
                            ? {
                                'sequences and series': 1,
                                'functions': 2,
                                'finance': 3,
                                'financial mathematics': 3,
                                'trigonometry': 4,
                                'trigonometry studio': 4,
                            }
                            : flags.isGrade10BusinessStudies
                                ? {
                                    'micro environment': 1,
                                    'business functions': 2,
                                    'the market environment': 3,
                                    'market environment': 3,
                                    'the macro environment': 4,
                                    'macro environment': 4,
                                    'interrelationship of environments': 5,
                                    'interrelationship': 5,
                                    'business sectors': 6,
                                    'socio-economic issues': 7,
                                    'socio economic issues': 7,
                                    'social responsibility': 8,
                                    'entrepreneurial qualities': 9,
                                    'forms of ownership': 10,
                                    'the concept of quality': 11,
                                    'concept of quality': 11,
                                }
                                : flags.isGrade11BusinessStudies
                                    ? {
                                        'influences on business environments': 1,
                                        'the challenges of the business environments': 2,
                                        'adapting to the challenges in the business environments': 3,
                                        'contemporary socio-economic issues and businesses': 4,
                                        'contemporary socio economic issues and businesses': 4,
                                        'business sectors': 5,
                                        'benefits of a company over other forms of ownership': 6,
                                        'avenues of acquiring businesses': 7,
                                        'creative thinking and problem solving': 8,
                                        'stress, crisis and change management': 9,
                                        'stress crisis and change management': 9,
                                        'the marketing function': 10,
                                        'the production function': 11,
                                        'professionalism and ethics': 12,
                                    }
                                    : {};

    const hit = mapping[normalized];
    if (Number.isFinite(hit)) return hit;

    if (flags.isGrade10Accounting && isGrade10IndigenousBookkeepingTopic(topicName)) return 1;
    if (flags.isGrade10Accounting && isGrade10EthicsTopic(topicName)) return 2;
    if (flags.isGrade10Accounting && isGrade10GAAPTopic(topicName)) return 3;
    if (flags.isGrade10Accounting && isGrade10InternalControlsTopic(topicName)) return 4;
    if (flags.isGrade10Accounting && isGrade10SoleTraderTopic(topicName)) return 5;
    if (flags.isGrade10Accounting && isGrade10VATTopic(topicName)) return 6;
    if (flags.isGrade10Accounting && isGrade10SalariesWagesTopic(topicName)) return 7;
    if (flags.isGrade10Accounting && isGrade10FinalAccountsTopic(topicName)) return 8;

    if (flags.isGrade10BusinessStudies && isGrade10BSMicroEnvironment(topicName)) return 1;
    if (flags.isGrade10BusinessStudies && isGrade10BSBusinessFunctions(topicName)) return 2;
    if (flags.isGrade10BusinessStudies && isGrade10BSMarketEnvironment(topicName)) return 3;
    if (flags.isGrade10BusinessStudies && isGrade10BSMacroEnvironment(topicName)) return 4;
    if (flags.isGrade10BusinessStudies && isGrade10BSInterrelationship(topicName)) return 5;
    if (flags.isGrade10BusinessStudies && isGrade10BSBusinessSectors(topicName)) return 6;
    if (flags.isGrade10BusinessStudies && isGrade10BSSocioEconomic(topicName)) return 7;
    if (flags.isGrade10BusinessStudies && isGrade10BSSocialResponsibility(topicName)) return 8;
    if (flags.isGrade10BusinessStudies && isGrade10BSEntrepreneurial(topicName)) return 9;
    if (flags.isGrade10BusinessStudies && isGrade10BSFormsOfOwnership(topicName)) return 10;
    if (flags.isGrade10BusinessStudies && isGrade10BSConceptOfQuality(topicName)) return 11;

    if (flags.isGrade11BusinessStudies && isGrade11BSInfluences(topicName)) return 1;
    if (flags.isGrade11BusinessStudies && isGrade11BSChallenges(topicName)) return 2;
    if (flags.isGrade11BusinessStudies && isGrade11BSAdapting(topicName)) return 3;
    if (flags.isGrade11BusinessStudies && isGrade11BSContemporarySocioEconomic(topicName)) return 4;
    if (flags.isGrade11BusinessStudies && isGrade11BSBusinessSectors(topicName)) return 5;
    if (flags.isGrade11BusinessStudies && isGrade11BSBenefitsOfCompany(topicName)) return 6;
    if (flags.isGrade11BusinessStudies && isGrade11BSAvenues(topicName)) return 7;
    if (flags.isGrade11BusinessStudies && isGrade11BSCreativeThinking(topicName)) return 8;
    if (flags.isGrade11BusinessStudies && isGrade11BSStressCrisisChange(topicName)) return 9;
    if (flags.isGrade11BusinessStudies && isGrade11BSMarketingFunction(topicName)) return 10;
    if (flags.isGrade11BusinessStudies && isGrade11BSProductionFunction(topicName)) return 11;
    if (flags.isGrade11BusinessStudies && isGrade11BSProfessionalismEthics(topicName)) return 12;

    if (flags.isGrade12BusinessStudies && isGrade12BSCreativeThinking(topicName)) return 1;
    if (flags.isGrade12BusinessStudies && isGrade12BSEthicsProfessionalism(topicName)) return 2;
    if (flags.isGrade12BusinessStudies && isGrade12BSMacroEnvironmentStrategies(topicName)) return 3;
    if (flags.isGrade12BusinessStudies && isGrade12BSImpactOfLegislation(topicName)) return 4;
    if (flags.isGrade12BusinessStudies && isGrade12BSHumanResourcesFunction(topicName)) return 5;
    if (flags.isGrade12BusinessStudies && isGrade12BSBusinessSectorsEnvironments(topicName)) return 6;
    if (flags.isGrade12BusinessStudies && isGrade12BSQualityOfPerformance(topicName)) return 7;
    if (flags.isGrade12BusinessStudies && isGrade12BSManagementLeadership(topicName)) return 8;
    if (flags.isGrade12BusinessStudies && isGrade12BSInvestmentSecurities(topicName)) return 9;
    if (flags.isGrade12BusinessStudies && isGrade12BSInvestmentInsurance(topicName)) return 10;
    if (flags.isGrade12BusinessStudies && isGrade12BSTeamPerformanceConflict(topicName)) return 11;
    if (flags.isGrade12BusinessStudies && isGrade12BSHumanRightsInclusivity(topicName)) return 12;
    if (flags.isGrade12BusinessStudies && isGrade12BSSocialResponsibilityCsr(topicName)) return 13;
    if (flags.isGrade12BusinessStudies && isGrade12BSPresentationDataResponses(topicName)) return 14;
    if (flags.isGrade12BusinessStudies && isGrade12BSFormsOfOwnershipSuccess(topicName)) return 15;

    if (flags.isGrade10Math && isPatternsSequencesTopic(topicName)) return 3;
    if (flags.isGrade10Math && isAlgebraicExpressionsTopic(topicName)) return 1;
    if (flags.isGrade10Math && isExponentsTopic(topicName)) return 2;
    if (flags.isGrade10Math && isEquationsInequalitiesTopic(topicName)) return 4;
    if (flags.isGrade10Math && isTrigonometry1Topic(topicName)) return 5;

    if (flags.isGrade11Math && isExponentsSurdsTopic(topicName)) return 1;
    if (flags.isGrade11Math && isEquationsInequalitiesTopic(topicName)) return 2;
    if (flags.isGrade11Math && isPatternsSequencesTopic(topicName)) return 3;
    if (flags.isGrade11Math && isAnalyticalGeometryTopic(topicName)) return 4;

    if (flags.isGrade12Math && isPatternsSequencesSeriesTopic(topicName)) return 1;
    if (flags.isGrade12Math && isGrade12FunctionsTopic(topicName)) return 2;
    if (flags.isGrade12Math && isGrade12FinanceTopic(topicName)) return 3;
    if (flags.isGrade12Math && isGrade12TrigonometryTopic(topicName)) return 4;

    return null;
};

export const getOrderedTopicNames = (availableTopics, flags) => {
    const topics = Array.isArray(availableTopics) ? availableTopics.slice() : [];
    if (!hasStructuredTopicOrdering(flags)) return topics;

    const ordered = topics.sort((a, b) => {
        const ia = getCoveredTopicIndex(a, flags);
        const ib = getCoveredTopicIndex(b, flags);

        if (ia !== null && ib !== null) return ia - ib;
        if (ia !== null) return -1;
        if (ib !== null) return 1;
        return String(a).localeCompare(String(b));
    });

    const seen = new Set();
    const deduped = [];
    for (const topicName of ordered) {
        const idx = getCoveredTopicIndex(topicName, flags);
        const displayKey = `display:${normalizeTopicName(getTopicDisplayName(topicName, flags))}`;
        const key = idx !== null ? `idx:${idx}` : `name:${normalizeTopicName(topicName)}`;

        if (seen.has(displayKey)) continue;
        if (seen.has(key)) continue;

        seen.add(key);
        seen.add(displayKey);
        deduped.push(topicName);
    }

    return deduped;
};

export const getTopicTerm = (topicName, flags) => {
    const normalized = normalizeTopicName(topicName);

    if (flags.isGrade10Accounting) {
        if (normalized.includes('informal') || normalized.includes('indigenous') || normalized.includes('bookkeeping')) return 'Term 1';
        if (normalized.includes('ethics')) return 'Term 1';
        if (normalized.includes('gaap') || normalized.includes('accounting principles')) return 'Term 1';
        if (normalized.includes('internal control')) return 'Term 1';
        if (normalized.includes('financial accounts') || normalized.includes('final accounts') || normalized.includes('year end')) return 'Term 2';
        if (normalized.includes('sole trader')) return 'Term 1';
        if (normalized.includes('salaries') || normalized.includes('wages')) return 'Term 2';
        if (normalized.includes('vat') || normalized.includes('value added tax') || normalized.includes('valued added tax')) return 'Term 2';
    }

    if (flags.isGrade10BusinessStudies) {
        if (isGrade10BSMicroEnvironment(topicName)) return 'Term 1';
        if (isGrade10BSBusinessFunctions(topicName)) return 'Term 1';
        if (isGrade10BSMarketEnvironment(topicName)) return 'Term 1';
        if (isGrade10BSMacroEnvironment(topicName)) return 'Term 1';
        if (isGrade10BSInterrelationship(topicName)) return 'Term 1';
        if (isGrade10BSBusinessSectors(topicName)) return 'Term 1';
        if (isGrade10BSSocioEconomic(topicName)) return 'Term 2';
        if (isGrade10BSSocialResponsibility(topicName)) return 'Term 2';
        if (isGrade10BSEntrepreneurial(topicName)) return 'Term 2';
        if (isGrade10BSFormsOfOwnership(topicName)) return 'Term 2';
        if (isGrade10BSConceptOfQuality(topicName)) return 'Term 2';
    }

    if (flags.isGrade11BusinessStudies) {
        if (isGrade11BSInfluences(topicName)) return 'Term 1';
        if (isGrade11BSChallenges(topicName)) return 'Term 1';
        if (isGrade11BSAdapting(topicName)) return 'Term 1';
        if (isGrade11BSContemporarySocioEconomic(topicName)) return 'Term 1';
        if (isGrade11BSBusinessSectors(topicName)) return 'Term 1';
        if (isGrade11BSBenefitsOfCompany(topicName)) return 'Term 1';
        if (isGrade11BSAvenues(topicName)) return 'Term 1';
        if (isGrade11BSCreativeThinking(topicName)) return 'Term 2';
        if (isGrade11BSStressCrisisChange(topicName)) return 'Term 2';
        if (isGrade11BSMarketingFunction(topicName)) return 'Term 2';
        if (isGrade11BSProductionFunction(topicName)) return 'Term 2';
        if (isGrade11BSProfessionalismEthics(topicName)) return 'Term 2';
    }

    if (flags.isGrade12BusinessStudies) {
        if (isGrade12BSImpactOfLegislation(topicName)) return 'Term 1';
        if (isGrade12BSHumanResourcesFunction(topicName)) return 'Term 1';
        if (isGrade12BSCreativeThinking(topicName)) return 'Term 1';
        if (isGrade12BSEthicsProfessionalism(topicName)) return 'Term 1';
        if (isGrade12BSMacroEnvironmentStrategies(topicName)) return 'Term 1';
        if (isGrade12BSBusinessSectorsEnvironments(topicName)) return 'Term 2';
        if (isGrade12BSQualityOfPerformance(topicName)) return 'Term 2';
        if (isGrade12BSManagementLeadership(topicName)) return 'Term 2';
        if (isGrade12BSInvestmentSecurities(topicName)) return 'Term 2';
        if (isGrade12BSInvestmentInsurance(topicName)) return 'Term 2';
        if (isGrade12BSTeamPerformanceConflict(topicName)) return 'Term 2';
        if (isGrade12BSHumanRightsInclusivity(topicName)) return 'Term 3';
        if (isGrade12BSSocialResponsibilityCsr(topicName)) return 'Term 3';
        if (isGrade12BSPresentationDataResponses(topicName)) return 'Term 3';
        if (isGrade12BSFormsOfOwnershipSuccess(topicName)) return 'Term 3';
    }

    if (flags.isGrade11Accounting) {
        if (normalized.includes('ethics') || normalized.includes('internal control')) return 'Term 1';
        if (normalized.includes('reconciliation')) return 'Term 1';
        if (normalized.includes('fixed') || normalized.includes('tangible') || normalized.includes('assets')) return 'Term 1';
        if (normalized.includes('partnership')) return 'Term 1';
        if (normalized.includes('club') || normalized.includes('non-profit') || normalized.includes('nonprofit')) return 'Term 2';
        if (normalized.includes('analysis') && (normalized.includes('interpretation') || normalized.includes('intepretation'))) return 'Term 2';
    }

    if (flags.isGrade12Accounting) {
        if (normalized.includes('concepts')) return 'Term 1';
        if (normalized.includes('bookkeeping') || normalized.includes('unique ledger')) return 'Term 1';
        if (normalized.includes('preparation of financial statements')) return 'Term 1';
        if (normalized.includes('analysis and interpretation')) return 'Term 1';
        if (normalized.includes('audits') || normalized.includes('corporate governance')) return 'Term 1';
        if (normalized.includes('fixed') || normalized.includes('tangible assets')) return 'Term 2';
        if (normalized.includes('inventor')) return 'Term 2';
        if (normalized.includes('reconciliation')) return 'Term 2';
        if (normalized.includes('vat') || normalized.includes('value added tax')) return 'Term 2';
    }

    return null;
};

export const getSelectedTopicDisplayName = (topicName, flags) => {
    if (!topicName) return '';
    const idx = getCoveredTopicIndex(topicName, flags);
    const displayName = getTopicDisplayName(topicName, flags);
    if (!idx) return displayName;
    if (flags.isGrade10Math || flags.isGrade11Math || flags.isGrade12Math) return `${idx} ${displayName}`;
    return `${idx}. ${displayName}`;
};

export const getTopicCardTitle = (topicName, flags) => {
    const idx = getCoveredTopicIndex(topicName, flags);
    const displayName = getTopicDisplayName(topicName, flags);
    let title = idx ? `${idx}. ${displayName}` : displayName;

    if ((flags.isGrade10Math || flags.isGrade11Math || flags.isGrade12Math) && idx) {
        title = `${idx} ${displayName}`;
    }

    if (flags.isGrade9Math && isPatternsTopic(topicName) && idx === 6) {
        title = `${idx}. Numeric and geometric patterns`;
    }

    if (flags.isGrade9Math && isFunctionsRelationshipsTopic(topicName) && idx === 7) {
        title = '7 Functions and relationships 1';
    }

    if (flags.isGrade9Math && isAlgebraicExpressionsTopic(topicName) && idx === 8) {
        title = '8 Algebraic expressions 1';
    }

    if (flags.isGrade9Math && isAlgebraicEquationsTopic(topicName) && idx === 9) {
        title = '9 Algebraic equations 1';
    }

    return title;
};

export const shouldHideGeneratedPracticeButton = (topicName, flags) => (
    (flags.isGrade7Math && (
        isWholeNumbersTopic(topicName)
        || isExponentsTopic(topicName)
        || isGeoConstructionTopic(topicName)
        || isGeo2DShapesTopic(topicName)
        || isGeoStraightLinesTopic(topicName)
    ))
    || (flags.isGrade8Math && (
        isWholeNumbersTopic(topicName)
        || isIntegersTopic(topicName)
        || isExponentsTopic(topicName)
        || isPatternsTopic(topicName)
        || isFunctionsRelationshipsTopic(topicName)
        || isAlgebraicExpressionsTopic(topicName)
        || isAlgebraicEquationsTopic(topicName)
    ))
    || (flags.isGrade9Math && (
        isWholeNumbersTopic(topicName)
        || isIntegersTopic(topicName)
        || isFractionsTopic(topicName)
        || isDecimalNotationTopic(topicName)
        || isExponentsTopic(topicName)
        || isPatternsTopic(topicName)
    ))
);
