from flask import Flask, request, render_template, Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.database import db
from app.models import Article, Predication

bp = Blueprint("main", __name__)

@bp.route("/")
def main():
    return render_template('index.html')

@bp.route("/results")
def results():
    args = request.args.to_dict()                
    query = db.session.query(Article, Predication).join(Article, Article.id == Predication.article_id)
    query = query.filter(Predication.gene == args["gene"])
    results = query.all()
    list(set(results))
    return render_template('results.html',input=args["gene"],results=results)