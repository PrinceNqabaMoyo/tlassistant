import {
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
    isGrade11BSEntrepreneurialAssessment,
    isGrade11BSCitizenship,
    isGrade11BSBusinessPlanTransformation,
    isGrade11BSStartBusinessVenture,
    isGrade11BSPresentationOfInformation,
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
    isGrade7EMSMoneyNeeds,
    isGrade7EMSBusinesses,
    isGrade7EMSAccountingConcepts,
    isGrade7EMSIncomeExpenses,
    isGrade7EMSBudgets,
    isGrade7EMSEntrepreneurship,
} from './topicMatchers';

export const getScaffoldRouteForTopic = (topicName, flags) => {
    if (flags.isGrade7Math) {
        if (isWholeNumbersTopic(topicName)) return 'grade7_whole_scaffold';
        if (isExponentsTopic(topicName)) return 'grade7_exponents_scaffold';
        if (isGeoConstructionTopic(topicName)) return 'grade7_geo_construct_scaffold';
        if (isGeo2DShapesTopic(topicName)) return 'grade7_geo2d_scaffold';
        if (isGeoStraightLinesTopic(topicName)) return 'grade7_straight_lines_scaffold';
    }

    if (flags.isGrade7EMS || flags.subject === 'ems' || (flags.isGrade7 && String(flags.subjectName || '').toLowerCase() === 'ems')) {
        if (isGrade7EMSMoneyNeeds(topicName)) return 'grade7_ems_money_needs_scaffold';
        if (isGrade7EMSBusinesses(topicName)) return 'grade7_ems_businesses_scaffold';
        if (isGrade7EMSAccountingConcepts(topicName)) return 'grade7_ems_accounting_concepts_scaffold';
        if (isGrade7EMSIncomeExpenses(topicName)) return 'grade7_ems_income_expenses_scaffold';
        if (isGrade7EMSBudgets(topicName)) return 'grade7_ems_budgets_scaffold';
        if (isGrade7EMSEntrepreneurship(topicName)) return 'grade7_ems_entrepreneurship_scaffold';
    }

    if (flags.isGrade8Math) {
        if (isWholeNumbersTopic(topicName)) return 'grade8_whole_scaffold';
        if (isIntegersTopic(topicName)) return 'grade8_integers_scaffold';
        if (isExponentsTopic(topicName)) return 'grade8_exponents_scaffold';
        if (isPatternsTopic(topicName)) return 'grade8_patterns_scaffold';
        if (isFunctionsRelationshipsTopic(topicName)) return 'grade8_functions_1_scaffold';
        if (isAlgebraicExpressionsTopic(topicName)) return 'grade8_algebraic_expressions_1_scaffold';
        if (isAlgebraicEquationsTopic(topicName)) return 'grade8_algebraic_equations_1_scaffold';
    }

    if (flags.isGrade9Math) {
        if (isWholeNumbersTopic(topicName)) return 'grade9_whole_scaffold';
        if (isIntegersTopic(topicName)) return 'grade9_integers_scaffold';
        if (isFractionsTopic(topicName)) return 'grade9_fractions_scaffold';
        if (isDecimalNotationTopic(topicName)) return 'grade9_decimal_notation_scaffold';
        if (isExponentsTopic(topicName)) return 'grade9_exponents_scaffold';
        if (isPatternsTopic(topicName)) return 'grade9_patterns_scaffold';
        if (isFunctionsRelationshipsTopic(topicName)) return 'grade9_functions_relationships_1_scaffold';
        if (isAlgebraicExpressionsTopic(topicName)) return 'grade9_algebraic_expressions_1_scaffold';
        if (isAlgebraicEquationsTopic(topicName)) return 'grade9_algebraic_equations_1_scaffold';
    }

    if (flags.isGrade10Math) {
        if (isAlgebraicExpressionsTopic(topicName)) return 'grade10_algebraic_expressions_scaffold';
        if (isExponentsTopic(topicName)) return 'grade10_exponents_scaffold';
        if (isPatternsSequencesTopic(topicName)) return 'grade10_patterns_sequences_scaffold';
        if (isEquationsInequalitiesTopic(topicName)) return 'grade10_equations_inequalities_scaffold';
        if (isTrigonometry1Topic(topicName)) return 'grade10_trigonometry_1_scaffold';
    }

    if (flags.isGrade10Accounting) {
        if (isGrade10IndigenousBookkeepingTopic(topicName)) return 'grade10_accounting_indigenous_scaffold';
        if (isGrade10EthicsTopic(topicName)) return 'grade10_accounting_ethics_scaffold';
        if (isGrade10GAAPTopic(topicName)) return 'grade10_accounting_gaap_scaffold';
        if (isGrade10InternalControlsTopic(topicName)) return 'grade10_accounting_internal_control_scaffold';
        if (isGrade10VATTopic(topicName)) return 'grade10_accounting_vat_scaffold';
        if (isGrade10SalariesWagesTopic(topicName)) return 'grade10_accounting_salaries_wages_scaffold';
        if (isGrade10FinalAccountsTopic(topicName)) return 'grade10_accounting_final_accounts_scaffold';
        if (isGrade10SoleTraderTopic(topicName)) return 'grade10_accounting_sole_trader_scaffold';
    }

    if (flags.isGrade10BusinessStudies) {
        if (isGrade10BSMicroEnvironment(topicName)) return 'grade10_bs_micro_environment_scaffold';
        if (isGrade10BSBusinessFunctions(topicName)) return 'grade10_bs_business_functions_scaffold';
        if (isGrade10BSMarketEnvironment(topicName)) return 'grade10_bs_market_environment_scaffold';
        if (isGrade10BSMacroEnvironment(topicName)) return 'grade10_bs_macro_environment_scaffold';
        if (isGrade10BSInterrelationship(topicName)) return 'grade10_bs_interrelationship_scaffold';
        if (isGrade10BSBusinessSectors(topicName)) return 'grade10_bs_business_sectors_scaffold';
        if (isGrade10BSSocioEconomic(topicName)) return 'grade10_bs_socio_economic_issues_scaffold';
        if (isGrade10BSSocialResponsibility(topicName)) return 'grade10_bs_social_responsibility_scaffold';
        if (isGrade10BSEntrepreneurial(topicName)) return 'grade10_bs_entrepreneurial_qualities_scaffold';
        if (isGrade10BSFormsOfOwnership(topicName)) return 'grade10_bs_forms_of_ownership_scaffold';
        if (isGrade10BSConceptOfQuality(topicName)) return 'grade10_bs_concept_of_quality_scaffold';
    }

    if (flags.isGrade11BusinessStudies) {
        if (isGrade11BSInfluences(topicName)) return 'grade11_bs_influences_on_business_environments_scaffold';
        if (isGrade11BSAdapting(topicName)) return 'grade11_bs_adapting_to_challenges_scaffold';
        if (isGrade11BSChallenges(topicName)) return 'grade11_bs_challenges_of_the_business_environments_scaffold';
        if (isGrade11BSContemporarySocioEconomic(topicName)) return 'grade11_bs_socio_economic_issues_scaffold';
        if (isGrade11BSBenefitsOfCompany(topicName)) return 'grade11_bs_benefits_of_a_company_scaffold';
        if (isGrade11BSAvenues(topicName)) return 'grade11_bs_avenues_of_acquiring_businesses_scaffold';
        if (isGrade11BSBusinessSectors(topicName)) return 'grade11_bs_business_sectors_scaffold';
        if (isGrade11BSCreativeThinking(topicName)) return 'grade11_bs_creative_thinking_scaffold';
        if (isGrade11BSStressCrisisChange(topicName)) return 'grade11_bs_stress_crisis_change_scaffold';
        if (isGrade11BSMarketingFunction(topicName)) return 'grade11_bs_marketing_function_scaffold';
        if (isGrade11BSProductionFunction(topicName)) return 'grade11_bs_production_function_scaffold';
        if (isGrade11BSProfessionalismEthics(topicName)) return 'grade11_bs_professionalism_and_ethics_scaffold';
        if (isGrade11BSEntrepreneurialAssessment(topicName)) return 'grade11_bs_entrepreneurial_assessment_scaffold';
        if (isGrade11BSCitizenship(topicName)) return 'grade11_bs_citizenship_responsibilities_scaffold';
        if (isGrade11BSBusinessPlanTransformation(topicName)) return 'grade11_bs_business_plan_transformation_scaffold';
        if (isGrade11BSStartBusinessVenture(topicName)) return 'grade11_bs_start_business_venture_scaffold';
        if (isGrade11BSPresentationOfInformation(topicName)) return 'grade11_bs_presentation_of_information_scaffold';
    }

    if (flags.isGrade12BusinessStudies) {
        if (isGrade12BSImpactOfLegislation(topicName)) return 'grade12_bs_impact_of_legislation_scaffold';
        if (isGrade12BSHumanResourcesFunction(topicName)) return 'grade12_bs_human_resources_function_scaffold';
        if (isGrade12BSCreativeThinking(topicName)) return 'grade12_bs_creative_thinking_problem_solving_scaffold';
        if (isGrade12BSEthicsProfessionalism(topicName)) return 'grade12_bs_ethics_and_professionalism_scaffold';
        if (isGrade12BSMacroEnvironmentStrategies(topicName)) return 'grade12_bs_macro_environment_strategies_scaffold';
        if (isGrade12BSBusinessSectorsEnvironments(topicName)) return 'grade12_bs_business_sectors_environments_scaffold';
        if (isGrade12BSQualityOfPerformance(topicName)) return 'grade12_bs_quality_of_performance_scaffold';
        if (isGrade12BSManagementLeadership(topicName)) return 'grade12_bs_management_and_leadership_scaffold';
        if (isGrade12BSInvestmentSecurities(topicName)) return 'grade12_bs_investment_securities_scaffold';
        if (isGrade12BSInvestmentInsurance(topicName)) return 'grade12_bs_investment_insurance_scaffold';
        if (isGrade12BSTeamPerformanceConflict(topicName)) return 'grade12_bs_team_performance_conflict_scaffold';
        if (isGrade12BSHumanRightsInclusivity(topicName)) return 'grade12_bs_human_rights_inclusivity_scaffold';
        if (isGrade12BSSocialResponsibilityCsr(topicName)) return 'grade12_bs_social_responsibility_csr_csi_scaffold';
        if (isGrade12BSPresentationDataResponses(topicName)) return 'grade12_bs_presentation_data_responses_scaffold';
        if (isGrade12BSFormsOfOwnershipSuccess(topicName)) return 'grade12_bs_forms_of_ownership_success_scaffold';
    }

    if (flags.isGrade11Math) {
        if (isExponentsSurdsTopic(topicName)) return 'grade11_exponents_surds_scaffold';
        if (isEquationsInequalitiesTopic(topicName)) return 'grade11_equations_inequalities_scaffold';
        if (isPatternsSequencesTopic(topicName)) return 'grade11_patterns_sequences_scaffold';
        if (isAnalyticalGeometryTopic(topicName)) return 'grade11_analytical_geometry_scaffold';
    }

    if (flags.isGrade11Accounting) {
        const normalized = String(topicName || '').toLowerCase();
        if (normalized.includes('ethics') || normalized.includes('internal control')) return 'grade11_accounting_ethics_internal_control_scaffold';
        if (normalized.includes('reconciliation')) return 'grade11_accounting_reconciliation_scaffold';
        if (normalized.includes('fixed') || normalized.includes('tangible') || normalized.includes('assets')) return 'grade11_accounting_fixed_assets_scaffold';
        if (normalized.includes('partnership')) return 'grade11_accounting_partnerships_scaffold';
        if (normalized.includes('club') || normalized.includes('non-profit') || normalized.includes('nonprofit')) return 'grade11_accounting_clubs_nonprofit_scaffold';
        if (normalized.includes('analysis') && (normalized.includes('interpretation') || normalized.includes('intepretation'))) return 'grade11_accounting_analysis_interpretation_scaffold';
        return 'grade11_accounting_scaffold';
    }

    if (flags.isGrade12Math) {
        if (isPatternsSequencesSeriesTopic(topicName)) return 'grade12_patterns_sequences_series_scaffold';
        if (isGrade12FunctionsTopic(topicName)) return 'grade12_functions_scaffold';
        if (isGrade12FinanceTopic(topicName)) return 'grade12_finance_scaffold';
        if (isGrade12TrigonometryTopic(topicName)) return 'grade12_trigonometry_scaffold';
    }

    if (flags.isGrade12Accounting) {
        const normalized = String(topicName || '').toLowerCase();
        if (normalized.includes('concepts')) return 'grade12_accounting_concepts_scaffold';
        if (normalized.includes('bookkeeping') || normalized.includes('unique ledger')) return 'grade12_accounting_bookkeeping_scaffold';
        if (normalized.includes('preparation of financial statements')) return 'grade12_accounting_finance_scaffold';
        if (normalized.includes('analysis and interpretation')) return 'grade12_accounting_analysis_scaffold';
        if (normalized.includes('audits') || normalized.includes('corporate governance')) return 'grade12_accounting_audits_scaffold';
        if (normalized.includes('fixed') || normalized.includes('tangible')) return 'grade12_accounting_fixed_assets_t2_scaffold';
        if (normalized.includes('inventor')) return 'grade12_accounting_inventory_scaffold';
        if (normalized.includes('reconcil')) return 'grade12_accounting_reconciliation_t2_scaffold';
        if (normalized.includes('vat') || normalized.includes('value added tax')) return 'grade12_accounting_vat_t2_scaffold';
        return 'grade12_accounting_scaffold';
    }

    return null;
};
