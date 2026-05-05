# HOW TO RUN THE PROJECT

This document provides step-by-step instructions to run the Bitbucket DevOps CI/CD project locally.

## Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git
- Docker (optional, for containerized testing)

## Option 1: Local Python Execution

### Step 1: Create Virtual Environment
```bash
cd bitbucket-cicd-project
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements-dev.txt
```

### Step 3: Run Tests
```bash
# Run all tests with coverage
pytest tests/ -v --cov=app --cov-report=html

# Run only unit tests
pytest tests/test_unit.py -v

# Run only integration tests
pytest tests/test_integration.py -v

# Run specific test
pytest tests/test_unit.py::TestUserModel::test_user_creation -v
```

### Step 4: Run Application
```bash
# Start Flask development server
python -m app.main

# Application runs at: http://localhost:5000
```

### Step 5: Test API Endpoints
```bash
# In another terminal, test endpoints:

# Health check
curl http://localhost:5000/health

# Create user
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'

# Get user
curl http://localhost:5000/api/users/1

# List users
curl http://localhost:5000/api/users
```

## Option 2: Docker Execution

### Build Docker Image
```bash
docker build -f docker/Dockerfile -t bitbucket-cicd:latest .
```

### Run Application in Docker
```bash
docker run -p 5000:5000 bitbucket-cicd:latest

# Application runs at: http://localhost:5000
```

### Run Tests in Docker
```bash
docker build -f docker/Dockerfile.test -t bitbucket-cicd-test:latest .
docker run bitbucket-cicd-test:latest
```

### Docker Compose (if you have docker-compose.yml)
```bash
docker-compose up --build
```

## Option 3: Quick Start Scripts

### Windows
```bash
quickstart.bat
```

### Linux/macOS
```bash
bash quickstart.sh
```

These scripts will:
1. Create virtual environment
2. Install dependencies
3. Run code quality checks
4. Run full test suite with coverage
5. Start the Flask application

## Running Code Quality Checks

```bash
# Flake8 (code style)
flake8 app/ tests/

# Black (code formatting)
black --check app/ tests/

# Pylint (code analysis)
pylint app/

# All checks
flake8 app/ tests/ && black --check app/ tests/ && pylint app/
```

## Viewing Test Coverage Report

After running tests with coverage:

### HTML Report
```bash
# Coverage report is generated in htmlcov/index.html
# Open in browser:
# Windows:
start htmlcov/index.html
# macOS:
open htmlcov/index.html
# Linux:
xdg-open htmlcov/index.html
```

### Terminal Report
```bash
pytest --cov=app --cov-report=term-missing
```

## Expected Test Output

```
tests/test_unit.py::TestUserModel::test_user_creation PASSED           [20%]
tests/test_unit.py::TestEmailValidation::test_valid_email PASSED       [30%]
tests/test_integration.py::TestUserEndpoints::test_create_user_success PASSED [80%]
...

====== 25 passed in 2.34s ======
```

## Expected Application Output

```
WARNING in flask.app: This is a development server. Do not use it in production.
WARNING in werkzeug: Running on http://0.0.0.0:5000

 * Serving Flask app 'app.main'
 * Environment: production
 * Debug mode: off
 * Running on http://0.0.0.0:5000
 * Press CTRL+C to quit
```

## Stopping the Application

Press `Ctrl+C` in the terminal to stop the Flask application.

## Troubleshooting

### "Module not found: flask"
```bash
# Make sure virtual environment is activated
pip install -r requirements-dev.txt
```

### "Port 5000 already in use"
```bash
# Run on different port
python -m flask run --port 5001
```

### Tests fail locally
```bash
# Ensure all dependencies are installed
pip install -r requirements-dev.txt --upgrade

# Clear pytest cache
pytest --cache-clear

# Run with verbose output
pytest tests/ -vvv
```

### Docker build fails
```bash
# Clear Docker cache
docker system prune -a

# Rebuild
docker build -f docker/Dockerfile -t bitbucket-cicd:latest --no-cache .
```

## Project Demo Workflow

1. **Start Application**
   ```bash
   python -m app.main
   ```

2. **In Another Terminal - Create User**
   ```bash
   curl -X POST http://localhost:5000/api/users \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Smith", "email": "jane@example.com"}'
   ```

3. **List Created Users**
   ```bash
   curl http://localhost:5000/api/users
   ```

4. **Run Full Test Suite**
   ```bash
   pytest tests/ -v --cov=app
   ```

5. **View Coverage Report**
   ```bash
   # Open htmlcov/index.html in browser
   ```

## Performance Metrics

- **Startup Time**: ~2 seconds
- **Test Suite Duration**: ~6 seconds
- **Docker Build Time**: ~3 minutes (first time)
- **Docker Build Time**: ~30 seconds (with cache)
- **API Response Time**: <100ms

## Next Steps

After running the project locally:

1. Commit changes to git
2. Push to Bitbucket
3. Monitor Bitbucket Pipelines execution
4. Review test coverage reports
5. Explore FINDINGS.md for testing trends

## Support

For issues or questions:
1. Check GIT_SETUP.md for repository setup
2. Review README.md for project overview
3. Check FINDINGS.md for DevOps concepts
4. Review test files for usage examples
