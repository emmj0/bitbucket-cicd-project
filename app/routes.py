"""
Application routes and error handlers.
"""

from werkzeug.exceptions import BadRequest

from flask import Blueprint, jsonify, request

from app.models import User, ValidationError, validate_user_input

api = Blueprint('api', __name__)


@api.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'service': 'Bitbucket DevOps CI/CD Project'
    })


@api.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'Invalid JSON'}), 400

        name = data.get('name')
        email = data.get('email')

        validate_user_input(name, email)

        user = User(name, email)
        return jsonify(user.to_dict()), 201

    except BadRequest:
        return jsonify({'error': 'Invalid JSON'}), 400
    except ValidationError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@api.route('/api/users', methods=['GET'])
def list_users():
    """List all users."""
    try:
        users = User.get_all()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@api.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID."""
    try:
        user = User.get_by_id(user_id)
        if not user:
            return jsonify({'error': 'User not found'}), 404
        return jsonify(user.to_dict()), 200
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


def register_error_handlers(app):
    """Register JSON error handlers on the Flask app."""

    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors."""
        return jsonify({'error': 'Endpoint not found'}), 404


    @app.errorhandler(500)
    def server_error(error):
        """Handle 500 errors."""
        return jsonify({'error': 'Internal server error'}), 500