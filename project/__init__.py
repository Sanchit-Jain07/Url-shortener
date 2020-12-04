from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_object('project.config.Config')

    db.init_app(app)
    
    from .models import Links

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
