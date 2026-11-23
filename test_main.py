
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello, World!"
    }


def test_addition():
    response = client.get("/addition?a=10&b=5")

    assert response.status_code == 200
    assert response.json() == {
        "result a+b=": 15,
        "developer": "Dev1"
    }


def test_greeting():
    response = client.get("/greeting?name=Dev2")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello Dev2, welcome to the application!"
    }


def test_soustraction():
    response = client.get("/soustraction?a=10&b=5")

    assert response.status_code == 200
    assert response.json() == {
        "result a-b=": 5,
        "developer": "Dev1"
    }


def test_soustraction_negative_result():
    response = client.get("/soustraction?a=5&b=10")

    assert response.status_code == 200
    assert response.json()["result a-b="] == -5


def test_soustraction_with_zero():
    response = client.get("/soustraction?a=10&b=0")

    assert response.status_code == 200
    assert response.json()["result a-b="] == 10
