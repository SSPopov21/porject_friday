from app import create_app, db
from app.models import AirQualityData
import random
from datetime import datetime, timedelta

app = create_app('development')

with app.app_context():
    print("Seeding database...")
    # Clear existing data
    db.session.query(AirQualityData).delete()
    
    # Generate 50 data points
    start_time = datetime.now()
    for i in range(50):
        timestamp = start_time - timedelta(hours=i)
        pm25 = random.uniform(10, 100)
        pm10 = random.uniform(20, 150)
        co2 = random.uniform(300, 600)
        
        # Simulate an anomaly
        anomaly_score = 0.0
        if pm25 > 80 or co2 > 550:
            anomaly_score = 0.9
        
        data = AirQualityData(
            timestamp=timestamp,
            pm25=round(pm25, 2),
            pm10=round(pm10, 2),
            co2=round(co2, 2),
            no2=round(random.uniform(0, 50), 2),
            so2=round(random.uniform(0, 20), 2),
            anomaly_score=anomaly_score
        )
        db.session.add(data)
    
    db.session.commit()
    print("Database seeded with 50 records!")
