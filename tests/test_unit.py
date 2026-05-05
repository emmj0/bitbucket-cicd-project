"""
Unit tests for the application.
"""

import pytest
from app.models import User, ValidationError, validate_email, validate_user_input


class TestUserModel:
    """Tests for User model."""
    
    def test_user_creation(self):
        """Test creating a user."""
        user = User("John Doe", "john@example.com")
        assert user.name == "John Doe"
        assert user.email == "john@example.com"
        assert user.id == 1
    
    def test_user_id_increment(self):
        """Test that user IDs increment."""
        user1 = User("User 1", "user1@example.com")
        user2 = User("User 2", "user2@example.com")
        assert user1.id == 1
        assert user2.id == 2
    
    def test_user_to_dict(self):
        """Test converting user to dictionary."""
        user = User("Jane Doe", "jane@example.com")
        user_dict = user.to_dict()
        assert user_dict['name'] == "Jane Doe"
        assert user_dict['email'] == "jane@example.com"
        assert 'id' in user_dict
    
    def test_get_user_by_id(self):
        """Test getting user by ID."""
        user = User("Test User", "test@example.com")
        retrieved = User.get_by_id(user.id)
        assert retrieved == user
        assert retrieved.name == "Test User"
    
    def test_get_nonexistent_user(self):
        """Test getting non-existent user."""
        user = User.get_by_id(999)
        assert user is None
    
    def test_get_all_users(self):
        """Test getting all users."""
        user1 = User("User 1", "user1@example.com")
        user2 = User("User 2", "user2@example.com")
        all_users = User.get_all()
        assert len(all_users) == 2
        assert user1 in all_users
        assert user2 in all_users


class TestEmailValidation:
    """Tests for email validation."""
    
    def test_valid_email(self):
        """Test valid email."""
        assert validate_email("test@example.com") is True
        assert validate_email("user.name@domain.co.uk") is True
    
    def test_invalid_email_no_at(self):
        """Test email without @ symbol."""
        assert validate_email("testexample.com") is False
    
    def test_invalid_email_no_dot(self):
        """Test email without dot."""
        assert validate_email("test@example") is False
    
    def test_empty_email(self):
        """Test empty email."""
        assert validate_email("") is False
        assert validate_email(None) is False


class TestUserValidation:
    """Tests for user input validation."""
    
    def test_valid_input(self):
        """Test valid user input."""
        validate_user_input("John Doe", "john@example.com")
        # Should not raise exception
    
    def test_empty_name(self):
        """Test empty name raises ValidationError."""
        with pytest.raises(ValidationError, match="Name cannot be empty"):
            validate_user_input("", "john@example.com")
    
    def test_empty_email(self):
        """Test empty email raises ValidationError."""
        with pytest.raises(ValidationError, match="Email cannot be empty"):
            validate_user_input("John Doe", "")
    
    def test_invalid_email_format(self):
        """Test invalid email format raises ValidationError."""
        with pytest.raises(ValidationError, match="Invalid email format"):
            validate_user_input("John Doe", "invalid-email")
    
    def test_none_values(self):
        """Test None values raise ValidationError."""
        with pytest.raises(ValidationError):
            validate_user_input(None, "john@example.com")
