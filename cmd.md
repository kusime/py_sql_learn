alembic revision --autogenerate -m "create tables"
alembic upgrade head

alembic current
alembic history

alembic downgrade 8d4b3cb61f6
alembic upgrade 3f1cb7f09b7a
