from flask import Flask
from app.routes import bp
from app.database import close_db
from app.models import init_db

def create_app():
    app = Flask(__name__)

    app.register_blueprint(bp)

    with app.app_context():
        init_db()

    app.teardown_appcontext(close_db)

    return app