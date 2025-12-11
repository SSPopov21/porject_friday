from flask import jsonify
from app.api import api

@api.route("/status")
def status():
    return jsonify({'status': 'online', 'version': '1.0.0'})
