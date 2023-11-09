from flask import Flask
import pytest
from src import create_app
from src.database import db
from src.models import Article, Predication


@pytest.fixture()
def app():	
	app = create_app("sqlite://")

	with app.app_context():
		db.create_all()

		new_article = Article(
		title='TP53 and its variants',
		uri='http://example.com')

		db.session.add(new_article)
		db.session.commit()

		new_predication = Predication(
			gene='TP53',
			disease = 'Breast Cancer',
			pred_type = 'Co-Occurance',
			article_id = new_article.id
		)

		db.session.add(new_predication)
		db.session.commit()

	yield app

@pytest.fixture()
def client(app):
    return app.test_client()