import importlib.util
from pathlib import Path
import pytest

SERVER_PATH = Path(__file__).resolve().parent.parent / "server" / "server.py"
spec = importlib.util.spec_from_file_location("local_server", SERVER_PATH)
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)

@pytest.fixture(autouse=True)
def reset_inventory():
    """Reset the in-memory inventory before each test."""
    server.inventory = [
        server.Inventory(1, "Item 1", 10),
        server.Inventory(2, "Item 2", 5),
    ]

@pytest.fixture
def client():
    server.app.config["TESTING"] = True
    with server.app.test_client() as client:
        yield client

def test_get_all_inventory(client):
    res = client.get("/inventory")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 2
    assert data[0] == {"id": 1, "name": "Item 1", "quantity": 10}

def test_get_single_item_success(client):
    res = client.get("/inventory/1")
    assert res.status_code == 200
    assert res.get_json() == {"id": 1, "name": "Item 1", "quantity": 10}

def test_get_single_item_not_found(client):
    res = client.get("/inventory/999")
    assert res.status_code == 404
    assert res.get_json() == {"error": "Item not found"}

def test_create_item_success(client):
    res = client.post("/inventory", json={"name": "Item 3", "quantity": 20})
    assert res.status_code == 201
    assert res.get_json() == {"id": 3, "name": "Item 3", "quantity": 20}
    assert len(server.inventory) == 3

def test_create_item_invalid_input(client):
    res = client.post("/inventory", json={"name": "Missing Quantity"})
    assert res.status_code == 400
    assert res.get_json() == {"error": "Invalid input"}

def test_update_item_partial_quantity(client):
    res = client.patch("/inventory/1", json={"quantity": 99})
    assert res.status_code == 200
    assert res.get_json() == {"id": 1, "name": "Item 1", "quantity": 99}

def test_update_item_partial_name(client):
    res = client.patch("/inventory/2", json={"name": "Renamed Item"})
    assert res.status_code == 200
    assert res.get_json() == {"id": 2, "name": "Renamed Item", "quantity": 5}

def test_update_item_not_found(client):
    res = client.patch("/inventory/999", json={"quantity": 50})
    assert res.status_code == 404
    assert res.get_json() == {"error": "Item not found"}

def test_delete_item_success(client):
    res = client.delete("/inventory/1")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Item deleted"}
    assert len(server.inventory) == 1

def test_delete_item_not_found(client):
    res = client.delete("/inventory/999")
    assert res.status_code == 404
    assert res.get_json() == {"error": "Item not found"}
