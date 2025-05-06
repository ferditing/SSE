import pytest
from fastapi.testclient import TestClient

# import from your backend entrypoint
from main import app  
from app.models import Base
from app.db import engine


# ─── Reset the test database before & after ────────────────────────────────────
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

# ─── Register an instructor and grab their token ───────────────────────────────
@pytest.fixture(scope="module")
def instructor_token():
    res = client.post(
        "/api/register",
        json={
            "name": "Bob",
            "email": "bob@example.com",
            "password": "pass1234",
            "role": "instructor"
        }
    )
    # now returns 201 Created
    assert res.status_code == 201
    data = res.json()
    assert "access_token" in data
    return data["access_token"]

# ─── Test login (uses the above fixture so the user exists) ────────────────────
def test_login(instructor_token):
    res = client.post(
        "/api/login",
        json={"email": "bob@example.com", "password": "pass1234"}
    )
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data

# ─── Test course creation as that instructor ──────────────────────────────────
def test_create_course(instructor_token):
    res = client.post(
        "/api/courses",
        headers={"Authorization": f"Bearer {instructor_token}"},
        json={
            "title": "Test Course",
            "description": "A course created in tests",
            "instructor_id": 1
        }
    )
    assert res.status_code == 201
    data = res.json()
    assert data["title"] == "Test Course"
    assert data["instructor_id"] == 1
