from app import create_app
from app.models import Article, Predication
from app.database import db


def test_home(client):	
	response = client.get("/")
	assert b"Search for a gene" in response.data

def test_search_result(client):
	response = client.get("/results?gene=TP53")
	assert b"TP53 and its variants" in response.data