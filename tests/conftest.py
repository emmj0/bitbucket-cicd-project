"""
Test configuration and fixtures.
"""

import pytest
from app import create_app
from app.models import User


@pytest.fixture
def app():
    """Create application for testing."""
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture(autouse=True)
def reset_users():
    """Reset users before each test."""
    User.reset()
    yield
    User.reset()
