from fastapi.testclient import TestClient
from main import app
from core.database import get_db

test_client = TestClient(app)

def test_create_user(get_test_db, get_test_user):
    app.dependency_overrides[get_db] = lambda: get_test_db
    response = test_client.post("/auth/register", json=get_test_user)
    assert response.status_code == 201