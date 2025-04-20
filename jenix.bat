@echo off
setlocal enabledelayedexpansion

echo Starting Jenix v0.2.0...

REM Check if Python is installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH.
    echo Please install Python from https://www.python.org/downloads/
    goto end
)

REM Check Python version
for /f "tokens=2" %%V in ('python --version 2^>^&1') do (
    set pyver=%%V
)
echo Using Python version: !pyver!

REM Check if requests package is installed
python -c "import requests" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required package: requests
    pip install requests
    if %errorlevel% neq 0 (
        echo Failed to install requests package.
        echo Try running: pip install -r "%~dp0requirements.txt"
        goto end
    )
)

REM Check if Ollama is running
python "%~dp0check_ollama.py" >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Cannot connect to Ollama. Make sure it's running.
    goto end
)

REM Check for Windows Terminal for better color support
where wt >nul 2>&1
if %errorlevel% equ 0 (
    echo Windows Terminal detected. Colors will be enabled.
    set "TERM=xterm-256color"
) else (
    echo Standard Windows console detected. Consider installing Windows Terminal for better display.
)

REM Run the script
python "%~dp0jenix.py" %*
if %errorlevel% neq 0 (
    echo.
    echo An error occurred while running Jenix.
)

:end
pause
endlocal