from flask import Flask

from app.config import Config
from app.database import db
from flask_migrate import Migrate
from app.routes import pollution_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(pollution_bp, url_prefix="/api/pollution")

    return app
