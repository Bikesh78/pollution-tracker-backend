from flask import Flask

from app.config import Config
from app.database import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    if __name__ == "__main__":
        app.run(debug=True)

    return app
