@echo off
echo 🔴 Closing all Chrome processes...
taskkill /F /IM chrome.exe >nul 2>&1

echo ✅ Chrome processes closed.

REM Set your Python path (Anaconda)
set PYTHON_PATH="F:\Users\NSG\anaconda3\python.exe"

REM Set the full path to your script
set SCRIPT_PATH="C:\Users\NSG\Desktop\python_playground\all projects\selenium projects\whatsapp automation\temp.py"

echo 🚀 Running WhatsApp automation script...
%PYTHON_PATH% %SCRIPT_PATH%

echo ✅ Script finished. Press any key to exit...
pause >nul
