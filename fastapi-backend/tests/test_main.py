import unittest
from testcontainers.postgres import PostgresContainer
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from sql_app.database import Base, get_db


def db_mask(postgres):
    engine = create_engine(postgres.get_connection_url())
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        try:
            db = TestingSessionLocal()
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


# def test_health_check():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Hello World!"}


class TestClient(unittest.TestCase):

    def setUp(self):
        pass

    def db_layer_access_check(self):
        with PostgresContainer("postgres:9.5") as postgres:
            e = sqlalchemy.create_engine(postgres.get_connection_url())
            result = e.execute("select version()")

    def test_health_check(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World!"}

    def test_get_user_list(self):
        with PostgresContainer("postgres:9.5") as postgres:
            db_mask(postgres)
            response = client.get("/users/")

            print(response.json())
            assert response.status_code == 200
