import unittest
from _pytest.monkeypatch import MonkeyPatch
from mock import patch
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer

from main import app
from sql_app.crud import get_user

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_get_db_check():
    import sqlalchemy

    with PostgresContainer("postgres:9.5") as postgres:
        e = sqlalchemy.create_engine(postgres.get_connection_url())
        result, = e.execute("select version()")
        print(result)


# class TestClient(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     def test_read_main(self):
#         response = client.get("/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.json(), {"message": "Hello World!"})
