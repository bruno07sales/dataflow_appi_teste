from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes.health import health_bp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(health_bp)
    print(app.config["SQLALCHEMY_DATABASE_URI"])

    return app