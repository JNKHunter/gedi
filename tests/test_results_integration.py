from app import create_app
from app.models import Article, Predication
from app.database import db

def test_navigate_integrate(client):
	get_search_list = client.get("/")
	assert b"TP53" in get_search_list.data

	search_gene = client.get("/results?gene=TP53")
	assert b"TP53 and its variants" in search_gene.data