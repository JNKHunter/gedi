from src.app import create_app

def test_home(client):
	response = client.get("/")
	assert b"Search for a gene" in response.data

def test_app_instantiation():
	assert create_app != None
	