@echo off
REM Quick start script for Bitbucket DevOps CI/CD Project (Windows)

echo.
echo ================================================
echo Bitbucket DevOps CI/CD Project - Quick Start
echo ================================================
echo.

REM Step 1: Create virtual environment
echo Step 1: Creating Python virtual environment...
python -m venv venv
call venv\Scripts\activate.bat
echo [OK] Virtual environment created
echo.

REM Step 2: Install dependencies
echo Step 2: Installing dependencies...
pip install -q -r requirements-dev.txt
echo [OK] Dependencies installed
echo.

REM Step 3: Run linting
echo Step 3: Running code quality checks...
flake8 app/ tests/
echo [OK] Code quality checks completed
echo.

REM Step 4: Run tests
echo Step 4: Running test suite...
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing
echo [OK] Tests completed
echo.

REM Step 5: Run application
echo Step 5: Starting Flask application...
echo Application will be available at http://localhost:5000
echo Press Ctrl+C to stop
echo.
python -m app.main
pause
