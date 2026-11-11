import json
import sys
sys.path.insert(0, 'caps-ai-backend')
from app.services.generator_registry import ALL_GENERATORS

manifest_path = 'caps-ai-backend/app/services/caps_term_registry_data.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    entries = json.load(f)

# (subject, grade, name_substring): new_generator_key
CORRECTIONS = {
    # Grade 10 BS
    ('Business Studies', '10', 'the market environment'): 'grade10_bs_market_environment',
    ('Business Studies', '10', 'the macro environment'): 'grade10_bs_macro_environment',
    ('Business Studies', '10', 'interrelationship'): 'grade10_bs_interrelationship',
    ('Business Studies', '10', 'business sectors'): 'grade10_bs_business_sectors',
    ('Business Studies', '10', 'business opportunities'): 'grade10_bs_business_opportunities',
    ('Business Studies', '10', 'business location'): 'grade10_bs_business_location',
    ('Business Studies', '10', 'presentation of business'): 'grade10_bs_presentation',
    ('Business Studies', '10', 'understanding business plans'): 'grade10_bs_business_plans',
    
    # Grade 11 BS
    ('Business Studies', '11', 'influencies on business'): 'grade11_bs_influences_on_business_environments',
    ('Business Studies', '11', 'the challenges of the business'): 'grade11_bs_challenges_of_business_environments',
    ('Business Studies', '11', 'contemporary socio economic'): 'grade11_bs_socio_economic_issues',
    ('Business Studies', '11', 'business sectors'): 'grade11_bs_business_sectors',
    ('Business Studies', '11', 'transformation of a business plan'): 'grade11_bs_business_plan_transformation',
    ('Business Studies', '11', 'a business venture based on a business plan'): 'grade11_bs_start_business_venture',
    ('Business Studies', '11', 'presentation of business'): 'grade11_bs_presentation_of_information',
    ('Business Studies', '11', 'the marketing function'): 'grade11_bs_marketing_function',
    ('Business Studies', '11', 'the production function'): 'grade11_bs_production_function',
    ('Business Studies', '11', 'assessment of enterpreneural'): 'grade11_bs_entrepreneurial_assessment',
    ('Business Studies', '11', 'human resources'): 'grade11_bs_human_resources_function',
    
    # Grade 12 BS
    ('Business Studies', '12', 'impact of recent legislation'): 'grade12_bs_impact_of_legislation',
    ('Business Studies', '12', 'human rights inclusivity'): 'grade12_bs_human_rights_inclusivity',
    ('Business Studies', '12', 'management & leadership'): 'grade12_bs_management_and_leadership',
    ('Business Studies', '12', 'quality of performance'): 'grade12_bs_quality_of_performance',
    ('Business Studies', '12', 'investments insurance'): 'grade12_bs_investment_insurance',
    ('Business Studies', '12', 'investement securities'): 'grade12_bs_investment_securities',
    
    # Maths Lit
    ('Mathematical Literacy', '10', 'conversions and time'): 'mathematical_literacy_measurement',
    ('Mathematical Literacy', '11', 'conversions and time'): 'mathematical_literacy_measurement',
    ('Mathematical Literacy', '12', 'conversions & time'): 'mathematical_literacy_measurement',
    
    # Life Sciences Gr 10
    ('Life Sciences', '10', 'cells the basic units'): 'natural_sciences_cell_cytology',
    ('Life Sciences', '10', 'cell division'): 'natural_sciences_cell_cytology',
}

changes_count = 0
for e in entries:
    s = e['subject']
    g = str(e['grade'])
    n = e['name'].lower()
    
    for (cs, cg, cn), new_key in CORRECTIONS.items():
        if s == cs and g == cg and cn in n:
            old_key = e['generator_key']
            if old_key != new_key:
                assert new_key in ALL_GENERATORS, f"Target key '{new_key}' not in ALL_GENERATORS!"
                print(f"Update: [{s} Gr{g}] '{e['name']}': '{old_key}' -> '{new_key}'")
                e['generator_key'] = new_key
                changes_count += 1
            break

print(f"\nTotal corrections to apply: {changes_count}")

# Save updated manifest
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

print(f"Successfully saved updated manifest to {manifest_path} with {len(entries)} entries.")
