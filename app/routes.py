from app.models.pollution_data import Pollution_Data
from flask import Blueprint, jsonify, request
from app.database import db

from app.services import get_random_sensor_data, get_weather_data


pollution_bp = Blueprint("pollution_bp", __name__)


@pollution_bp.route("/")
def get_pollution():
    try:
        # page = request.args.get("page", 1, type=int)
        # res = db.paginate(db.select(Pollution_Data), per_page=10, page=page)
        # print("res", vars(res))
        start_date = request.args.get("start_date", None, type=str)
        end_date = request.args.get("end_date", None, type=str)
        query = ""

        if end_date and start_date:
            query = db.select(Pollution_Data).where(
                Pollution_Data.date.between(start_date, end_date)
            )
        else:
            query = db.select(Pollution_Data)

        data = db.session.execute(query).scalars().all()
        historical_data = []
        for x in data:
            historical_data.append(
                {
                    "id": x.id,
                    "air_quality_index": x.air_quality_index,
                    "water_quality_index": x.water_quality_index,
                    "ph_level": x.ph_level,
                    "temperature": x.temperature,
                    "date": x.date,
                }
            )
        return jsonify(
            {
                "data": {
                    "historical_data": historical_data,
                    "live_data": get_random_sensor_data(),
                    "weather": get_weather_data(),
                },
            }
        )
    except Exception as err:
        return jsonify({"error": str(err)})
