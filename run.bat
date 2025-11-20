@echo off
echo 🚀 Starting Heart Disease Diagnosis App...
cd /d "%~dp0"
set PYTHONPATH=%PYTHONPATH%;%CD%
C:/Users/hoang/AppData/Local/Programs/Python/Python313/python.exe -m streamlit run app/streamlit_app.py --server.port=8501 --server.address=localhost --server.headless=false
pause