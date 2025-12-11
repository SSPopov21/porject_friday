from flask import jsonify
from app.main import main
from app.models import AirQualityData

@main.route("/api/data", methods=['GET'])
def get_data():
    data = AirQualityData.query.limit(100).all()
    result = []
    for entry in data:
         result.append({
             'timestamp': entry.timestamp,
             'pm25': entry.pm25,
             'pm10': entry.pm10,
             'co2': entry.co2
         })
    return jsonify(result)
