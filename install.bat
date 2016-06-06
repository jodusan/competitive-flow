REM Change this to your compiler FOLDER path
set "compilerPath=%ProgramFiles%\CodeBlocks\MinGW\bin\"

@setlocal enableextensions
@cd /d "%~dp0"

mkdir "%ProgramFiles%\CompetitiveFlow"
copy cf-paste.py "%ProgramFiles%\CompetitiveFlow\cf-paste.py"
copy cf-tool.py "%ProgramFiles%\CompetitiveFlow\cf-tool.py"
@endlocal
setx path "%PATH%%compilerPath%;%ProgramFiles%\CompetitiveFlow\"
pause
