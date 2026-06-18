@echo off
copy /Y "%~dp0..\src\components\workspace\registry\grade11BusinessStudiesRegistry.js" "%~dp0grade11BusinessStudiesRegistry.20260517-1452.bak.js"
copy /Y "%~dp0..\src\components\curriculum\CurriculumHelper.jsx" "%~dp0CurriculumHelper.20260517-1452.bak.jsx"
dir "%~dp0grade11BusinessStudiesRegistry.20260517-1452.bak.js" "%~dp0CurriculumHelper.20260517-1452.bak.jsx"
