@echo off
copy /Y "%~dp0..\src\components\workspace\shared\WorkspaceModeShell.jsx" "%~dp0WorkspaceModeShell.20260518-0957.bak.jsx"
copy /Y "%~dp0..\src\components\curriculum\CurriculumHelper.jsx" "%~dp0CurriculumHelper.20260518-0957.bak.jsx"
dir "%~dp0WorkspaceModeShell.20260518-0957.bak.jsx"
dir "%~dp0CurriculumHelper.20260518-0957.bak.jsx"
