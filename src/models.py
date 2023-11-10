from flask_sqlalchemy import SQLAlchemy
from src.database import db

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    uri = db.Column(db.String(255))    

class Predication(db.Model):
    __tablename__ = 'predications'

    id = db.Column(db.Integer, primary_key=True)
    gene = db.Column(db.String(100))
    disease = db.Column(db.String(100))
    pred_type = db.Column(db.String(100))
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)