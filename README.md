Steps to run:
docker compose up

How to migrate the database:
flask db init
flask db migrate -m 'initial'
flask db upgrade

Running tests
python -m pytest

Set DATABASE_URL environment variable:
`export DB_URI=PATH_TO_SQLITE_DB_OR_POSTGRES_OR_OTHER_DB`
