# -*- coding: utf-8 -*-


import subprocess
import os

file = "app.py"  # Change this to run a different file

if os.path.exists(file):
    print(f"🚀 Launching Streamlit app: {file}")
    subprocess.run(["streamlit", "run", file])
else:
    print(f"❌ File {file} not found.")
