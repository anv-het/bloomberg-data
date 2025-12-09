@echo off
echo ========================================
echo Bloomberg Data Downloader
echo ========================================
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

echo Virtual environment activated!
echo.
echo Usage:
echo   python download_bloomberg_data.py --symbol HDFCB
echo   python batch_download.py --count 5
echo   python test_download.py
echo.
echo Type 'deactivate' to exit virtual environment
echo.

REM Keep command prompt open
cmd /k
