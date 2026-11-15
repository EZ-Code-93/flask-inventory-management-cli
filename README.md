# Flask Inventory Management CLI

A lightweight RESTful inventory management system built with **Flask** and an interactive command-line interface (**CLI**) powered by `argparse` and `requests`.

---

## Project Structure

```text
flask-inventory-management-cli/
├── server/
│   └── server.py        # Flask REST API server
├── tests/
│   ├── conftest.py      # Pytest path configuration
│   ├── test_admin.py    # Unit tests for API client functions
│   ├── test_main.py     # Unit tests for CLI argument parsing
│   └── test_server.py   # Unit tests for Flask endpoints
├── admin.py             # HTTP client wrapper for CRUD operations
├── main.py              # CLI entry point using argparse
├── Pipfile              # Pipenv dependencies and Python version
└── README.md
```

---

## Prerequisites & Dependencies

* **Python:** `3.15`
* **Dependency Manager:** [Pipenv](https://pypa.io)
* **Packages:**
  * `flask` — Backend web server and REST API routing
  * `requests` — HTTP client for communicating with the Flask API
  * `pytest` — Automated unit testing framework

---

## Installation & Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com<your-username>/flask-inventory-management-cli.git
   cd flask-inventory-management-cli
   ```

2. **Install dependencies using Pipenv:**
   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**
   ```bash
   pipenv shell
   ```

---

## Usage

### 1. Start the Flask Server
In your first terminal window (inside the `pipenv shell`), start the Flask server on port `5555`:

```bash
python server/server.py
```

The API will be available at `http://127.0.0`. Keep this terminal running while using the CLI.

### 2. Run CLI Commands
Open a second terminal window, activate `pipenv shell`, and use `main.py` to manage inventory items:

* **List all inventory items:**
  ```bash
  python main.py list
  ```

* **Get a single item by ID:**
  ```bash
  python main.py get 1
  ```

* **Add a new item:**
  ```bash
  python main.py add "Wireless Mouse" 15
  ```

* **Update an existing item (partial or full update):**
  ```bash
  python main.py update 1 --quantity 25
  python main.py update 1 --name "Mechanical Keyboard"
  python main.py update 1 --name "USB-C Hub" --quantity 40
  ```

* **Delete an item by ID:**
  ```bash
  python main.py delete 2
  ```

---

## API Endpoints Reference

| Method | Endpoint | Description | Request Body Example |
| :--- | :--- | :--- | :--- |
| `GET` | `/inventory` | Retrieve all inventory items | *None* |
| `GET` | `/inventory/<id>` | Retrieve a single item by ID | *None* |
| `POST` | `/inventory` | Create a new inventory item | `{"name": "Item 3", "quantity": 10}` |
| `PATCH` | `/inventory/<id>` | Update an item's name and/or quantity | `{"quantity": 20}` |
| `DELETE` | `/inventory/<id>` | Delete an item by ID | *None* |

---

## Running Tests

This project includes a full `pytest` unit test suite covering the Flask server routes, HTTP client functions, and CLI argument parser. No running server is required to execute the tests.

```bash
pytest -v
```

---

## Notes

* Inventory data is stored **in memory** while `server.py` is running and resets to the default seed items whenever the server restarts.
