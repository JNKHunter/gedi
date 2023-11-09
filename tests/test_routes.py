from src import create_app
from src.models import Article, Predication
from src.database import db


def test_home(client):	
	response = client.get("/")
	assert b"Search for a gene" in response.data

def test_search_result(client):
	response = client.get("/results?gene=TP53")
	assert b"TP53 and its variants" in response.data
