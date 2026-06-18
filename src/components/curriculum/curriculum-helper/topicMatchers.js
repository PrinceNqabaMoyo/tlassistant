export const normalizeTopicName = (topicName) => String(topicName || '').trim().toLowerCase();

const normalizeLooseTopicName = (topicName) => String(topicName || '')
    .toLowerCase()
    .replace(/[-_]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();

export const isWholeNumbersTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('whole numbers') || normalized === 'whole numbers';
};

export const isIntegersTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('integers') || normalized === 'integers';
};

export const isFractionsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    if (normalized.includes('decimal notation')) return false;
    return normalized.includes('fractions') || normalized === 'fractions';
};

export const isDecimalNotationTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('decimal notation');
};

export const isExponentsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('exponents') || normalized === 'exponents';
};

export const isPatternsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('numeric and geometric patterns')
        || normalized.includes('numeric & geometric patterns')
        || normalized.includes('patterns')
        || normalized === 'numeric and geometric patterns';
};

export const isPatternsSequencesTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('patterns and sequences')
        || normalized.includes('patterns & sequences')
        || normalized.includes('patterns')
        || normalized.includes('sequences');
};

export const isPatternsSequencesSeriesTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    const hasSequences = normalized.includes('sequence') || normalized.includes('sequences');
    const hasSeries = normalized.includes('series');
    const hasPatterns = normalized.includes('pattern') || normalized.includes('patterns');
    return hasSeries && (hasSequences || hasPatterns);
};

export const isGrade12FunctionsTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    if (normalized.includes('algebraic studio')) return true;
    if (normalized.includes('functions and relations')) return true;
    if (normalized.includes('functions') || normalized.includes('function')) return true;
    if (normalized.includes('inverse function') || normalized.includes('inverse functions')) return true;
    if (normalized.includes('logarithm') || normalized.includes('logarithmic')) return true;
    if (normalized.includes('exponential')) return true;
    return false;
};

export const isGrade12FinanceTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    if (normalized.includes('finance')) return true;
    if (normalized.includes('growth and decay')) return true;
    if (normalized.includes('growth') && normalized.includes('decay')) return true;
    return false;
};

export const isGrade12TrigonometryTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    if (normalized === 'trigonometry') return true;
    if (normalized.includes('trigonometry')) return true;
    if (normalized.includes('trig')) return true;
    return false;
};

export const isFunctionsRelationshipsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('functions and relationships')
        || normalized.includes('functions & relationships')
        || normalized.includes('functions')
        || normalized.includes('relationships')
        || normalized === 'functions and relationships';
};

export const isAlgebraicExpressionsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('algebraic expressions')
        || normalized.includes('algebraic expression')
        || normalized === 'algebraic expressions';
};

export const isAlgebraicEquationsTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('algebraic equations')
        || normalized.includes('algebraic equation')
        || normalized === 'algebraic equations';
};

export const isEquationsInequalitiesTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('equations and inequalities')
        || normalized.includes('equations & inequalities')
        || (normalized.includes('equations') && normalized.includes('inequal'))
        || normalized.includes('inequal');
};

export const isTrigonometry1Topic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('trigonometry 1')
        || normalized.includes('trigonometry1')
        || normalized === 'trigonometry';
};

export const isGrade10IndigenousBookkeepingTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('informal')
        || normalized.includes('indigenous')
        || normalized.includes('bookkeeping');
};

export const isGrade11Geo2DShapesTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('2d shapes') || normalized.includes('2-d shapes');
};

export const isGrade7EMSMoneyNeeds = (topicName) => normalizeLooseTopicName(topicName).includes('money and needs');
export const isGrade7EMSBusinesses = (topicName) => normalizeLooseTopicName(topicName).includes('businesses');
export const isGrade7EMSAccountingConcepts = (topicName) => normalizeLooseTopicName(topicName).includes('accounting concepts');
export const isGrade7EMSIncomeExpenses = (topicName) => normalizeLooseTopicName(topicName).includes('income and expenses');
export const isGrade7EMSBudgets = (topicName) => normalizeLooseTopicName(topicName).includes('budgets');
export const isGrade7EMSEntrepreneurship = (topicName) => normalizeLooseTopicName(topicName).includes('entrepreneurship');

export const isGrade10EthicsTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized === 'ethics' || normalized.includes('ethics');
};

export const isGrade10GAAPTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('gaap')
        || normalized.includes('accounting principles')
        || normalized.includes('financial information and gaap')
        || (normalized.includes('principles') && normalized.includes('gaap'));
};

export const isGrade10InternalControlsTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized === 'internal control'
        || normalized === 'internal controls'
        || normalized.includes('internal control');
};

export const isGrade10SoleTraderTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    if (normalized.includes('year end') || normalized.includes('financial accounts')) return false;
    return normalized.includes('sole trader')
        || normalized.includes('sole-trader')
        || normalized.includes('financial accounting of a sole trader');
};

export const isGrade10SalariesWagesTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('salaries')
        || normalized.includes('wages')
        || normalized.includes('salaries and wages')
        || normalized.includes('salary')
        || normalized.includes('salaries & wages');
};

export const isGrade10FinalAccountsTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('final accounts')
        || normalized.includes('financial accounts')
        || normalized.includes('year-end')
        || normalized.includes('year end')
        || (normalized.includes('final') && normalized.includes('accounts'));
};

export const isGrade10VATTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('vat')
        || normalized.includes('value added tax')
        || normalized.includes('valued added tax')
        || normalized.includes('value-added tax');
};

export const isGrade10BSMicroEnvironment = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('micro') || normalized === 'micro-environment';
};

export const isGrade10BSBusinessFunctions = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('business functions') || normalized === 'business-functions';
};

export const isGrade10BSMarketEnvironment = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('market environment') || normalized === 'market-environment';
};

export const isGrade10BSMacroEnvironment = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('macro environment') || normalized === 'macro-environment';
};

export const isGrade10BSInterrelationship = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('interrelationship');
};

export const isGrade10BSBusinessSectors = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('sectors') || normalized === 'business-sectors';
};

export const isGrade10BSSocioEconomic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('socio-economic') || normalized.includes('socio economic');
};

export const isGrade10BSSocialResponsibility = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('social responsibility');
};

export const isGrade10BSEntrepreneurial = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('entrepreneurial');
};

export const isGrade10BSFormsOfOwnership = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('forms of ownership') || normalized === 'forms-of-ownership';
};

export const isGrade10BSConceptOfQuality = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('concept of quality') || normalized === 'concept-of-quality';
};

export const isGrade10BSCreativeThinking = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('creative thinking') || normalized.includes('problem solving');
};

export const isGrade10BSBusinessOpportunities = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('business opportunities') || normalized.includes('business opportunity');
};

export const isGrade10BSBusinessLocation = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('business location') || normalized.includes('location decision');
};

export const isGrade10BSContracts = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized === 'contracts' || normalized.includes('contract');
};

export const isGrade10BSPresentation = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('presentation of business information')
        || (normalized.includes('presentation') && normalized.includes('business information'));
};

export const isGrade10BSBusinessPlans = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('business plan');
};

export const isGrade11BSInfluences = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('influences on business environments');
};

export const isGrade11BSChallenges = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('challenges of the business environments');
};

export const isGrade11BSAdapting = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('adapting to the challenges');
};

export const isGrade11BSContemporarySocioEconomic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('contemporary socio-economic') || normalized.includes('contemporary socio economic');
};

export const isGrade11BSBusinessSectors = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized === 'business sectors' || normalized.includes('business sectors');
};

export const isGrade11BSBenefitsOfCompany = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('benefits of a company');
};

export const isGrade11BSAvenues = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('avenues of acquiring businesses');
};

export const isGrade11BSCreativeThinking = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('creative thinking') || normalized.includes('problem solving');
};

export const isGrade11BSStressCrisisChange = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('stress, crisis and change')
        || (normalized.includes('stress') && normalized.includes('crisis') && normalized.includes('change'));
};

export const isGrade11BSMarketingFunction = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('marketing function');
};

export const isGrade11BSProductionFunction = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('production function');
};

export const isGrade11BSProfessionalismEthics = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('professionalism and ethics')
        || (normalized.includes('professionalism') && normalized.includes('ethics'));
};

export const isGrade11BSEntrepreneurialAssessment = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('assessment of entrepreneurial')
        || (normalized.includes('entrepreneurial') && normalized.includes('qualit'));
};

export const isGrade11BSCitizenship = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('citizenship');
};

export const isGrade11BSBusinessPlanTransformation = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('transformation of a business plan')
        || normalized.includes('business plan into an action plan')
        || (normalized.includes('business plan') && normalized.includes('action plan'));
};

export const isGrade11BSStartBusinessVenture = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('start a business venture')
        || normalized.includes('business venture based on an action plan');
};

export const isGrade11BSPresentationOfInformation = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('presentation of business information')
        || (normalized.includes('presentation') && normalized.includes('business information'));
};

export const isExponentsSurdsTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('exponents and surds')
        || normalized.includes('exponents & surds')
        || (normalized.includes('exponents') && normalized.includes('surd'));
};

export const isAnalyticalGeometryTopic = (topicName) => {
    const normalized = normalizeLooseTopicName(topicName);
    return normalized.includes('analytical geometry')
        || normalized.includes('analytic geometry')
        || (normalized.includes('analytical') && normalized.includes('geometry'));
};

export const isGeoConstructionTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('construction of geometric figures')
        || normalized.includes('construction of geometric figure')
        || normalized === 'construction of geometric figures';
};

export const isGeo2DShapesTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('geometry of 2d shapes')
        || normalized.includes('geometry of 2d shape')
        || normalized === 'geometry of 2d shapes';
};

export const isGeoStraightLinesTopic = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('geometry of straight lines')
        || normalized.includes('geometry straight lines')
        || normalized === 'geometry of straight lines';
};

// ----- Grade 12 Business Studies matchers -----
export const isGrade12BSCreativeThinking = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('creative thinking') || normalized.includes('problem solving');
};

export const isGrade12BSEthicsProfessionalism = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('ethics and professionalism')
        || (normalized.includes('ethics') && normalized.includes('professionalism'));
};

export const isGrade12BSMacroEnvironmentStrategies = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('macro environment')
        || (normalized.includes('business strateg'));
};

export const isGrade12BSImpactOfLegislation = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('bbbee')
        || normalized.includes('broad-based black economic empowerment')
        || normalized.includes('broad based black economic empowerment')
        || normalized.includes('implications of the legislation')
        || (normalized.includes('legislation') && normalized.includes('human resources'));
};

export const isGrade12BSHumanResourcesFunction = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('human resources function')
        || (normalized.includes('human resource') && !normalized.includes('legislation'));
};

export const isGrade12BSBusinessSectorsEnvironments = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('business sectors and their environment')
        || (normalized.includes('business sectors') && normalized.includes('environment'));
};

export const isGrade12BSQualityOfPerformance = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('quality of performance');
};

export const isGrade12BSManagementLeadership = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('management and leadership')
        || (normalized.includes('management') && normalized.includes('leadership'));
};

export const isGrade12BSInvestmentSecurities = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('investment securities')
        || (normalized.includes('investment') && normalized.includes('securities'));
};

export const isGrade12BSInvestmentInsurance = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('investment insurance')
        || (normalized.includes('investment') && normalized.includes('insurance'));
};

export const isGrade12BSTeamPerformanceConflict = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('team performance')
        || (normalized.includes('team') && normalized.includes('conflict'));
};

export const isGrade12BSHumanRightsInclusivity = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('human rights')
        || normalized.includes('inclusivity')
        || (normalized.includes('human rights') && normalized.includes('environment'));
};

export const isGrade12BSSocialResponsibilityCsr = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('social responsibility')
        || normalized.includes('corporate citizenship')
        || normalized.includes('corporate social');
};

export const isGrade12BSPresentationDataResponses = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('presentation and data responses')
        || (normalized.includes('presentation') && normalized.includes('data response'));
};

export const isGrade12BSFormsOfOwnershipSuccess = (topicName) => {
    const normalized = normalizeTopicName(topicName);
    return normalized.includes('forms of ownership')
        || (normalized.includes('ownership') && normalized.includes('success'));
};
