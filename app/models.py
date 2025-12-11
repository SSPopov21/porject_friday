from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class AirQualityData(db.Model):
    __tablename__ = 'air_quality_data'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    pm25 = db.Column(db.Float)
    pm10 = db.Column(db.Float)
    no2 = db.Column(db.Float)
    so2 = db.Column(db.Float)
    co2 = db.Column(db.Float)
    anomaly_score = db.Column(db.Float, nullable=True) # AI prediction
    
    def __repr__(self):
        return f'<AirQualityData {self.timestamp}>'
