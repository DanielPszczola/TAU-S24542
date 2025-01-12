import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_users_empty():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == []


def test_create_user():
    user_data = {"name": "Jan Kowalski", "email": "jan@kowalski.pl"}
    response = client.post("/users", json=user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Jan Kowalski"
    assert response.json()["email"] == "jan@kowalski.pl"


def test_get_users_after_creation():
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Jan Kowalski"


def test_get_nonexistent_user():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_update_user():
    update_data = {"name": "Jan Nowak", "email": "jan@nowak.pl"}
    response = client.put("/users/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Jan Nowak"


def test_update_nonexistent_user():
    update_data = {"name": "Fake User", "email": "fake@user.pl"}
    response = client.put("/users/999", json=update_data)
    assert response.status_code == 404


def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted successfully"


def test_delete_nonexistent_user():
    response = client.delete("/users/999")
    assert response.status_code == 404
