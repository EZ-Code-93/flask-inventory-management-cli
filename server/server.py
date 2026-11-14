from flask import Flask, request, jsonify

app = Flask(__name__)

class Inventory:
    def __init__(self, id, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity
        }

inventory = [
    Inventory(1, "Item 1", 10),
    Inventory(2, "Item 2", 5)
]

@app.route("/inventory", methods=["GET"])
def get_inventory():
    return jsonify([item.to_dict() for item in inventory]), 200

@app.route("/inventory/<int:id>", methods=["GET"])
def get_inventory_item(id):
    item = next((item for item in inventory if item.id == id), None)
    if item:
        return jsonify(item.to_dict()), 200
    return jsonify({"error": "Item not found"}), 404

@app.route("/inventory", methods=["POST"])
def add_inventory_item():
    data = request.get_json()
    if not data or "name" not in data or "quantity" not in data:
        return jsonify({"error": "Invalid input"}), 400
    new_id = max([item.id for item in inventory], default=0) + 1
    new_item = Inventory(new_id, data["name"], data["quantity"])
    inventory.append(new_item)
    return jsonify(new_item.to_dict()), 201

@app.route("/inventory/<int:id>", methods=["PATCH"])
def update_inventory_item(id):
    data = request.get_json()
    item = next((item for item in inventory if item.id == id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    if "name" in data:
        item.name = data["name"]
    if "quantity" in data:
        item.quantity = data["quantity"]
    return jsonify(item.to_dict()), 200

@app.route("/inventory/<int:id>", methods=["DELETE"])
def delete_inventory_item(id):
    global inventory
    item = next((item for item in inventory if item.id == id), None)
    if not item:
        return jsonify({"error": "Item not found"}), 404
    inventory = [item for item in inventory if item.id != id]
    return jsonify({"message": "Item deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5555)