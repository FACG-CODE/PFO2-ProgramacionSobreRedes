@echo off
cd /d "%~dp0\src"
pip show flask >nul 2>&1 || pip install flask
pip show werkzeug >nul 2>&1 || pip install werkzeug
python servidor.py
pause