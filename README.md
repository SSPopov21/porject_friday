# Air Quality Aanalysis System

A Flask-based web application for monitoring and analyzing air quality data (PM2.5, PM10, CO2).

## Features
- **User Authentication**: Secure Login & Registration with email verification simulation.
- **Interactive Dashboard**: Protected route showing real-time air quality charts.
- **REST API**: Endpoints for data retrieval and anomaly prediction.
- **AI Modules**: Modular structure for integration of anomaly detection models.
- **Premium UI**: Modern Glassmorphism design using Vanilla CSS.

## Setup
1. **Clone the repository.**
2. **Setup Environment:**
   ```bash
   # Windows PowerShell
   $env:FLASK_APP="run.py"
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize Database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. **Run the Application:**
   ```bash
   python run.py
   ```

## API Documentation
- `POST /auth/api/login`: Authenticate and receive a token (simulated).
- `GET /api/data`: Retrieve air quality readings.
- `POST /ai/predict`: Submit data for anomaly detection.

## Project Structure
- `app/auth`: Authentication logic (Blueprints).
- `app/main`: Dashboard and Core routes.
- `app/ai`: AI prediction modules.
- `app/api`: General API endpoints.