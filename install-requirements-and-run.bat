@echo off
pip install -r requirements.txt
cls
start "" /B pythonw "%~dp0src\main.py"
exit