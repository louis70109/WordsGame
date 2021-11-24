import unittest
from unittest import mock

import sqlalchemy
from _pytest.monkeypatch import MonkeyPatch
from mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from testcontainers.postgres import PostgresContainer
from test.support import EnvironmentVarGuard
from main import app
from sql_app.crud import get_user
import os

from sql_app.database import Base, get_db

with PostgresContainer("postgres:9.5").with_bind_ports(5432, 47000) as postgres:
    DB_URI = postgres.get_connection_url()
    # postgres.get_container_host_ip()

print("@@@@@@@@@@@@@@@@")
print(DB_URI)
print()
print("@@@@@@@@@@@@@@@@")
engine = create_engine(DB_URI)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db()
client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


# def test_get_db_check():
#     import sqlalchemy
#
# with PostgresContainer("postgres:9.5") as postgres:
#         DB_URI = postgres.get_connection_url()
#         os.environ["DATABASE_URI"] = f'postgres://{postgres.POSTGRES_USER}:{postgres.POSTGRES_PASSWORD}@{postgres.get_container_host_ip()}:65235/{postgres.POSTGRES_DB}'


    # DB_URI = f'postgres://{postgres.POSTGRES_USER}:{postgres.POSTGRES_PASSWORD}@{postgres.get_container_host_ip()}:65235/{postgres.POSTGRES_DB}'


#         # postgresql: // postgres: postgres @ db / postgres
#         # postgresql + psycopg2: // test: test @ localhost:65186 / test
#         print(postgres.get_connection_url())
#         print(os.getenv("DATABASE_URI"))
#         response = client.get("/users")
#         print(response.json())


class TestClient(unittest.TestCase):
    def setUp(self):
        pass
        # with PostgresContainer("postgres:9.5") as postgres:
        #     print(os.getenv("DATABASE_URI"))
        #     self.env = EnvironmentVarGuard()
        #     self.env.set('DATABASE_URI', postgres.get_connection_url())
        # with PostgresContainer("postgres:9.5") as postgres:
        #     print(os.getenv("DATABASE_URI"))
        #
        #     os.environ["DATABASE_URI"] = postgres.get_connection_url()

        # postgresql: // postgres: postgres @ db / postgres
        # postgresql + psycopg2: // test: test @ localhost:65186 / test
        # print(postgres.get_connection_url())

    def test_read_main(self):
        print("___________________-")
        print(os.getenv('DATABASE_URI'))
        import time
        time.sleep(10000)
        response = client.get("/users")

        print(response.json())
        raise "hi"
