from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.Config')
    db.init_app(app)

    with app.app_context():
        # Adding routes
        from . import routes

        # Build the database:
        # This will create the database file using SQLAlchemy
        db.create_all()

    return app