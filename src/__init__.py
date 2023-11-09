from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from src.database import db
from src import routes
import os

database_uri = os.getenv('DATABASE_URI')

def create_app(database_uri=None):
    app = Flask(__name__)
    
    if database_uri == None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE_URI')    
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

    db.init_app(app)
    app.register_blueprint(routes.bp)
    return app