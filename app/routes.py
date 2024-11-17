from app.models.pollution_data import Pollution_Data
from flask import Blueprint, abort, jsonify, request


pollution_bp = Blueprint("pollution_bp", __name__)


@pollution_bp.route("/")
def get_pollution():
    try:
        data = Pollution_Data.query.all()
        res = []
        for x in data:
            res.append(
                {
                    "id": x.id,
                    "air_quality_index": x.air_quality_index,
                    "water_quality_index": x.water_quality_index,
                    "ph_level": x.ph_level,
                    "temperature": x.temperature,
                }
            )
        return jsonify({"data": res})
    except Exception as err:
        return jsonify({"error": str(err)})
