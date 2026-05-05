"""
Application initialization module.
"""

from flask import Flask
from app.routes import api, register_error_handlers

def create_app():
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    app.register_blueprint(api)
    register_error_handlers(app)
    
    return app
