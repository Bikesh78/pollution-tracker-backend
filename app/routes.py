from datetime import datetime
from random import randrange, uniform
from app.models.pollution_data import Pollution_Data
from flask import Blueprint, abort, jsonify, request
from app.database import db


pollution_bp = Blueprint("pollution_bp", __name__)


def get_random_sensor_data():
    return {
        "air_quality_index": randrange(0, 300),
        "date": datetime.now(),
        "water_quality_index": randrange(0, 100),
        "ph_level": round(uniform(0, 14), 2),
        "temperature": round(uniform(10, 100), 2),
    }


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
        res = []
        for x in data:
            res.append(
                {
                    "id": x.id,
                    "air_quality_index": x.air_quality_index,
                    "water_quality_index": x.water_quality_index,
                    "ph_level": x.ph_level,
                    "temperature": x.temperature,
                    "date": x.date,
                }
            )
        return jsonify({"data": res, "live_data": get_random_sensor_data()})
    except Exception as err:
        return jsonify({"error": str(err)})
