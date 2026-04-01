from flask import Flask
from app.routes import bp
from app.database import close_db
from app.models import init_db

# ============================================================
# Lesson 12 - App Factory Pattern
# File: app/__init__.py
# Purpose: Create and configure application in modular structure
# ============================================================

def create_app():
    # Create Flask application instance
    app = Flask(__name__)

    # Register routes from blueprint
    app.register_blueprint(bp)

    # Initialize database tables within app context
    with app.app_context():
        init_db()

    # Close DB automatically after each request
    app.teardown_appcontext(close_db)

    return app