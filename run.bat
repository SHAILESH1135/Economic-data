@echo off
echo Starting India Economic Data Analysis Dashboard...
echo.

echo Starting FastAPI Backend...
start cmd /k "title Economic Dashboard - Backend && echo Starting FastAPI Backend on http://localhost:8000... && .venv\Scripts\python backend\main.py"

echo Starting Vite React Frontend...
start cmd /k "title Economic Dashboard - Frontend && echo Starting Vite React Frontend... && cd frontend && npm run dev"

echo.
echo Both servers have been launched in separate windows!
echo Backend is running at: http://localhost:8000
echo Frontend is running at: http://localhost:5173
echo.
pause
