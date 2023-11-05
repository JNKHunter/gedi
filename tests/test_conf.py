import pytest

from src.app import create_app

@pytest.fixture()
def app():
	
	app = create_app()
	db = setup_database(app)
	migrate = Migrate(app,db)
	print("HEEEEELLLLOOOO")
	yield app

@pytest.fixture()
def client(app):
	print("HEEEEELLLLOOOO")
	return app.test_client()