# Heart Disease App - Quick Start
# Chỉ cần gõ: python start.py

import os
import sys
import subprocess
from pathlib import Path

# Set working directory
os.chdir(Path(__file__).parent)

# Set environment
os.environ['PYTHONPATH'] = f"{os.environ.get('PYTHONPATH', '')};{os.getcwd()}"

print("🚀 Heart Disease Diagnosis App")
print("🌐 http://localhost:8501")

# Start app
subprocess.run([
    sys.executable, "-m", "streamlit", "run", 
    "app/streamlit_app.py",
    "--server.port=8501",
    "--server.address=localhost"
])