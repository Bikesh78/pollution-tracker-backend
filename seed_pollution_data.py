from datetime import datetime, timedelta
from app import create_app
from flask import g
from app.models.pollution_data import Pollution_Data
from app.database import db
from app.config import Config
from random import randrange, uniform

app = create_app()

app.config.from_object(Config)


def seed_pollution_data():
    today = datetime.today()
    with app.app_context():
        for x in range(90):
            new_item = Pollution_Data(
                air_quality_index=randrange(0, 300),
                date=today - timedelta(x),
                water_quality_index=randrange(0, 100),
                ph_level=round(uniform(0, 14), 2),
                temperature=round(uniform(10, 100), 2),
            )
            # with app.app_context():
            db.session.add(new_item)

        db.session.commit()
        print("Successfully seeded")


seed_pollution_data()
