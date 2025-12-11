from flask import jsonify
from app.ai import ai

@ai.route("/predict", methods=['POST'])
def predict():
    return jsonify({'prediction': 'Normal', 'details': 'No anomaly detected'})
