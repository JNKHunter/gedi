Steps to run:
docker compose up

How to migrate the database:
flask db migrate -m 'predications foreign key'
flask db upgrade

Running tests
python -m pytest
