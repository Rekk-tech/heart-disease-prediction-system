# Heart Disease Diagnosis App - PowerShell Runner
Write-Host "🚀 Starting Heart Disease Diagnosis App..." -ForegroundColor Green

# Set working directory to script location
Set-Location -Path $PSScriptRoot

# Set PYTHONPATH
$env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"

# Start Streamlit app
Write-Host "🌐 Opening app at: http://localhost:8501" -ForegroundColor Cyan
C:/Users/hoang/AppData/Local/Programs/Python/Python313/python.exe -m streamlit run app/streamlit_app.py --server.port=8501 --server.address=localhost --server.headless=false

Write-Host "Press any key to exit..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")