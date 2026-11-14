import requests

BASE_URL = "http://127.0.0.1:5555/inventory"

def get_all():
    response = requests.get(BASE_URL)
    print(response.status_code, response.json())

def get_one(item_id):
    response = requests.get(f"{BASE_URL}/{item_id}")
    print(response.status_code, response.json())

def create_item(name, quantity):
    payload = {"name": name, "quantity": quantity}
    response = requests.post(BASE_URL, json=payload)
    print(response.status_code, response.json())

def update_item(item_id, name=None, quantity=None):
    payload = {}
    if name is not None:
        payload["name"] = name
    if quantity is not None:
        payload["quantity"] = quantity
    
    response = requests.patch(f"{BASE_URL}/{item_id}", json=payload)
    print(response.status_code, response.json())

def delete_item(item_id):
    response = requests.delete(f"{BASE_URL}/{item_id}")
    print(response.status_code, response.json())
