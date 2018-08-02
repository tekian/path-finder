@echo off

ECHO Checking Python command present..
WHERE python.exe >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    ECHO Python is not installed!
    ECHO https://www.python.org/downloads/
    set /p temp=""
    EXIT /b
)

FOR /F "tokens=* USEBACKQ" %%F IN (`python.exe -V`) DO ( SET var=%%F )

ECHO Checking Python version is 3..
ECHO.%var% | findstr /C:"Python 3">nul || (
    ECHO You have old version of Python!
    ECHO https://www.python.org/downloads/
    set /p temp=""
    EXIT /b
)

ECHO Checking dependencies are installed..
pip3.exe -q install -r %~dp0requirements.txt
IF %ERRORLEVEL% NEQ 0 (
    ECHO "Failed to install dependencies!"

    set /p temp=""
    EXIT /b
)

ECHO Starting application..
python.exe %~dp0src\pathfinder.py