# Bitbucket DevOps CI/CD Project

## Overview
This project demonstrates a production-ready CI/CD pipeline using Bitbucket Pipelines with comprehensive testing, containerization, and deployment strategies. It showcases current DevOps best practices and testing trends.

## Project Structure
```
bitbucket-cicd-project/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Flask application
│   └── models.py               # Data models
├── tests/
│   ├── __init__.py
│   ├── test_unit.py           # Unit tests
│   ├── test_integration.py    # Integration tests
│   └── conftest.py            # Pytest configuration
├── docker/
│   ├── Dockerfile             # Production Docker image
│   └── Dockerfile.test        # Test Docker image
├── bitbucket-pipelines.yml    # CI/CD pipeline configuration
├── requirements.txt           # Python dependencies
├── requirements-dev.txt       # Development dependencies
├── pytest.ini                 # Pytest configuration
├── .gitignore                 # Git ignore patterns
├── README.md                  # Project documentation
└── FINDINGS.md               # Testing trends & analysis
```

## Features

### 1. **Automated Testing**
- Unit tests with pytest
- Integration tests with test fixtures
- Code coverage reporting
- Test result artifacts

### 2. **Continuous Integration (CI)**
- Automated builds on every commit
- Parallel test execution
- Docker image building and scanning
- Security vulnerability checks

### 3. **Code Quality**
- Python linting (pylint, flake8)
- Code formatting validation (black)
- Test coverage thresholds

### 4. **Containerization**
- Multi-stage Dockerfile for optimized production images
- Separate test container for pipeline testing
- Container image scanning for vulnerabilities

### 5. **Pipeline Automation**
- Branch-specific pipelines
- Pull request validation
- Automatic deployment to staging
- Artifact management

## Running the Project Locally

### Prerequisites
- Python 3.9+
- Docker and Docker Compose
- Git

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd bitbucket-cicd-project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Run the application
python -m app.main

# Run tests
pytest tests/ -v --cov=app

# Build Docker image
docker build -f docker/Dockerfile -t bitbucket-cicd-project:latest .

# Run in Docker
docker run -p 5000:5000 bitbucket-cicd-project:latest
```

## API Endpoints

### Health Check
```
GET /health
Response: {"status": "healthy", "version": "1.0.0"}
```

### Create User
```
POST /api/users
Body: {"name": "John Doe", "email": "john@example.com"}
Response: {"id": 1, "name": "John Doe", "email": "john@example.com"}
```

### Get User
```
GET /api/users/<id>
Response: {"id": 1, "name": "John Doe", "email": "john@example.com"}
```

### List Users
```
GET /api/users
Response: [{"id": 1, "name": "John Doe", "email": "john@example.com"}]
```

## Testing Strategy

### Test Pyramid
```
        E2E Tests (5%)
       /            \
      /              \
   Integration (25%)
    /              \
  /                  \
Unit Tests (70%)
```

### Test Execution Flow
1. **Lint & Format** (~30s): Python code quality checks
2. **Unit Tests** (~2m): 20+ tests with 85%+ coverage
3. **Build Image** (~3m): Docker image creation
4. **Integration Tests** (~4m): API endpoint testing
5. **Security Scan** (~2m): Vulnerability detection
6. **Deploy** (~2m): Staging deployment

## CI/CD Pipeline Details

### Bitbucket Pipelines Configuration
The `bitbucket-pipelines.yml` defines:
- **Triggers**: On every push and PR
- **Steps**: Parallel unit tests, sequential integration tests
- **Artifacts**: Coverage reports, test results
- **Deployments**: Staging environment on master branch

### Key Pipeline Features
- Caching for faster builds
- Parallel step execution
- Docker-in-Docker for image builds
- Artifact retention for 7 days
- Automatic retries on transient failures

## Tools & Technologies

| Category | Tools |
|----------|-------|
| **Language** | Python 3.9+ |
| **Framework** | Flask |
| **Testing** | pytest, pytest-cov |
| **Code Quality** | pylint, flake8, black |
| **Containerization** | Docker |
| **CI/CD** | Bitbucket Pipelines |
| **VCS** | Git/Bitbucket |

## Performance Considerations

- **Build Time**: ~12 minutes end-to-end
- **Test Execution**: ~6 minutes (parallel where possible)
- **Docker Image Size**: ~150MB (optimized multi-stage build)
- **Code Coverage Target**: 85%+

## Security Best Practices

1. **Secret Management**: Environment variables in Bitbucket (no hardcoded secrets)
2. **Dependency Scanning**: Automated vulnerability checks
3. **Image Scanning**: Container image security analysis
4. **Access Control**: Branch protection rules on master
5. **Audit Logs**: Pipeline execution tracking

## Deployment Strategy

### Environments
- **Development**: Automatic on feature branches
- **Staging**: Automatic on master branch
- **Production**: Manual trigger (not in this demo)

### Rollback Procedure
- Keep previous Docker images tagged with timestamps
- Use blue-green deployment strategy
- Maintain database migration reversibility

## Troubleshooting

### Common Issues

**Tests failing locally but passing in pipeline**
- Check Python version: `python --version`
- Verify all dependencies: `pip install -r requirements-dev.txt`
- Clear cache: `pytest --cache-clear`

**Docker build failures**
- Ensure Docker daemon is running
- Check disk space: `docker system prune`
- Rebuild without cache: `docker build --no-cache ...`

**Pipeline stuck**
- Check Bitbucket service status
- Review logs in Bitbucket UI
- Retry pipeline execution

## Contributing

1. Create feature branch: `git checkout -b feature/my-feature`
2. Make changes and run tests: `pytest`
3. Commit changes: `git commit -am "Add feature"`
4. Push to Bitbucket: `git push origin feature/my-feature`
5. Create pull request and await review

## Next Steps

See `FINDINGS.md` for:
- Current DevOps testing trends
- Future roadmap (Phase 2 & 3)
- Tools and frameworks recommendations
- Best practices guide

## License
MIT License

## Contact
For questions, refer to the DevOps team or create an issue in the repository.
