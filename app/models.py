"""
Data models for the application.
"""

class User:
    """User model."""
    
    _counter = 0
    _users = {}
    
    def __init__(self, name: str, email: str):
        """Initialize a user.
        
        Args:
            name: User's full name
            email: User's email address
        """
        User._counter += 1
        self.id = User._counter
        self.name = name
        self.email = email
        User._users[self.id] = self
    
    def to_dict(self):
        """Convert user to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
    
    @classmethod
    def get_by_id(cls, user_id: int):
        """Get user by ID."""
        return cls._users.get(user_id)
    
    @classmethod
    def get_all(cls):
        """Get all users."""
        return list(cls._users.values())
    
    @classmethod
    def reset(cls):
        """Reset for testing purposes."""
        cls._counter = 0
        cls._users = {}


class ValidationError(Exception):
    """Custom validation error."""
    pass


def validate_email(email: str) -> bool:
    """Validate email format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not email or '@' not in email or '.' not in email:
        return False
    return True


def validate_user_input(name: str, email: str):
    """Validate user input.
    
    Args:
        name: User's name
        email: User's email
        
    Raises:
        ValidationError: If validation fails
    """
    if not name or len(name.strip()) == 0:
        raise ValidationError("Name cannot be empty")
    
    if not email or len(email.strip()) == 0:
        raise ValidationError("Email cannot be empty")
    
    if not validate_email(email):
        raise ValidationError("Invalid email format")
