# START PROJECT

> python -m venv venv

> pip install -r requirements.txt

> cd src

> alembic upgrade head

> python server.py

### migrations

ao criar uma novo model no database/model

> alembic revision --autogenerate -m "name"
> alembic upgrade head

### testing project

para testar as rotas

> pytest -v
