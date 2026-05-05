#!/usr/bin/env bash
# Quick start script for Bitbucket DevOps CI/CD Project

echo "================================================"
echo "Bitbucket DevOps CI/CD Project - Quick Start"
echo "================================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Step 1: Create virtual environment
echo -e "${BLUE}Step 1: Creating Python virtual environment...${NC}"
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
echo -e "${GREEN}✓ Virtual environment created${NC}"
echo ""

# Step 2: Install dependencies
echo -e "${BLUE}Step 2: Installing dependencies...${NC}"
pip install -q -r requirements-dev.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"
echo ""

# Step 3: Run linting
echo -e "${BLUE}Step 3: Running code quality checks...${NC}"
flake8 app/ tests/ || true
echo -e "${GREEN}✓ Code quality checks completed${NC}"
echo ""

# Step 4: Run tests
echo -e "${BLUE}Step 4: Running test suite...${NC}"
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing
echo -e "${GREEN}✓ Tests completed${NC}"
echo ""

# Step 5: Run application
echo -e "${BLUE}Step 5: Starting Flask application...${NC}"
echo "Application will be available at http://localhost:5000"
echo "Press Ctrl+C to stop"
echo ""
python -m app.main
