"""
Application initialization module.
"""

from flask import Flask

def create_app():
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    return app
