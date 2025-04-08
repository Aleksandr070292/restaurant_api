import pytest
from httpx import AsyncClient
from app.main import app
from app.database import Base, engine, SessionLocal

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_get_tables(client):
    response = await client.get("/tables/")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.asyncio
async def test_create_table(client):
    response = await client.post("/tables/", json={"name": "Table 1", "seats": 4, "location": "зал"})
    assert response.status_code == 200
    assert response.json()["name"] == "Table 1"