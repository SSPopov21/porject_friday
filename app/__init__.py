from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from config import config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
mail = Mail()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    # Blueprint registration
    from app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from app.ai import ai as ai_blueprint
    app.register_blueprint(ai_blueprint, url_prefix='/ai')

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
