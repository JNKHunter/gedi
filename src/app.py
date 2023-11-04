#!/usr/bin/env python3
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app():

    app = Flask(__name__)

    @app.route("/")
    def main():
        return render_template('index.html')

    @app.route("/echo_user_input", methods=["POST"])
    def echo_input():
        return render_template('results.html',input=request.form.get("user_input",""))

    return app

def setup_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gedi.db'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/postgres'
    db = SQLAlchemy(app)
    return db

app = create_app()
db = setup_database(app)

migrate = Migrate(app,db)

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(255))

class Predication(db.Model):
    __tablename__ = 'predications'

    id = db.Column(db.Integer, primary_key=True)
    gene = db.Column(db.String(100))
    disease =  db.Column(db.String(100))
    pred_type = db.Column(db.String(100))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)        