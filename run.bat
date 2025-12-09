@echo off
REM Quick run script for Bloomberg Data Downloader

if "%1"=="" (
    echo Usage: run.bat SYMBOL
    echo Example: run.bat HDFCB
    echo Example: run.bat IOCL
    exit /b 1
)

echo ========================================
echo Downloading Bloomberg data for %1
echo ========================================
echo.

call venv\Scripts\activate.bat
python download_bloomberg_data.py --symbol %1

pause
