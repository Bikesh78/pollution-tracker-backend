from app.database import db


class Pollution_Data(db.Model):
    __tablename__ = "pollution_data"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    air_quality_index = db.Column(db.Integer, nullable=False)
    water_quality_index = db.Column(db.Integer, nullable=False)
    ph_level = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
