@echo off
copy /Y "%~dp0..\BSGR11 enhancement plan.md" "%~dp0BSGR11 enhancement plan.20260517-1408.bak.md"
copy /Y "%~dp0..\caps-ai-backend\app\utils\grade11_business_studies\term_1\influences_on_business_environments_generator.py" "%~dp0influences_on_business_environments_generator.20260517-1408.bak.py"
copy /Y "%~dp0..\caps-ai-backend\app\utils\grade11_business_studies\term_1\influences_on_business_environments_family_spec.md" "%~dp0influences_on_business_environments_family_spec.20260517-1408.bak.md"
dir "%~dp0BSGR11 enhancement plan.20260517-1408.bak.md" "%~dp0influences_on_business_environments_generator.20260517-1408.bak.py" "%~dp0influences_on_business_environments_family_spec.20260517-1408.bak.md"
