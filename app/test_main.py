from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items", json={"nome": "Lápis", "descricao": "De escrever"})
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "Lápis"
    assert data["descricao"] == "De escrever"

def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_item():
    # cria o item
    create = client.post("/items", json={"nome": "Apagar", "descricao": "Item temporário"})
    item_id = create.json()["id"]

    # e então deleta o item para finds de test
    delete = client.delete(f"/items/{item_id}")
    assert delete.status_code == 200
    assert delete.json()["message"] == "Item deleted"