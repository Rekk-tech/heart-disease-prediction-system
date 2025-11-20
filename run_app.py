#!/usr/bin/env python3
"""
Simple runner for Heart Disease Diagnosis App
"""
import os
import sys
import subprocess
from pathlib import Path

def main():
    # Get script directory
    script_dir = Path(__file__).parent.absolute()
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Set PYTHONPATH
    pythonpath = os.environ.get('PYTHONPATH', '')
    os.environ['PYTHONPATH'] = f"{pythonpath};{script_dir}" if pythonpath else str(script_dir)
    
    print("🚀 Starting Heart Disease Diagnosis App...")
    print("🌐 App will open at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the app")
    print()
    
    try:
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app/streamlit_app.py",
            "--server.port=8501",
            "--server.address=localhost",
            "--server.headless=false",
            "--server.enableCORS=false",
            "--server.enableXsrfProtection=false"
        ])
    except KeyboardInterrupt:
        print("\n✅ App stopped successfully!")
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()