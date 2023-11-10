import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_database(app, db_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db = SQLAlchemy(app)
    db.init_app(app)
    return db