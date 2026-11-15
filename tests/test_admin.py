from unittest.mock import patch, MagicMock
import admin

def _mock_response(status_code, json_data):
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.json.return_value = json_data
    return mock_resp

@patch("admin.requests.get")
def test_get_all(mock_get, capsys):
    mock_get.return_value = _mock_response(200, [{"id": 1, "name": "Item 1", "quantity": 10}])
    admin.get_all()

    mock_get.assert_called_once_with(admin.BASE_URL)
    captured = capsys.readouterr()
    assert "200" in captured.out
    assert "Item 1" in captured.out

@patch("admin.requests.get")
def test_get_one(mock_get, capsys):
    mock_get.return_value = _mock_response(200, {"id": 1, "name": "Item 1", "quantity": 10})
    admin.get_one(1)

    mock_get.assert_called_once_with(f"{admin.BASE_URL}/1")
    captured = capsys.readouterr()
    assert "200" in captured.out

@patch("admin.requests.post")
def test_create_item(mock_post, capsys):
    mock_post.return_value = _mock_response(201, {"id": 3, "name": "Item 3", "quantity": 15})
    admin.create_item("Item 3", 15)

    mock_post.assert_called_once_with(
        admin.BASE_URL,
        json={"name": "Item 3", "quantity": 15}
    )
    captured = capsys.readouterr()
    assert "201" in captured.out

@patch("admin.requests.patch")
def test_update_item_only_quantity(mock_patch, capsys):
    mock_patch.return_value = _mock_response(200, {"id": 1, "name": "Item 1", "quantity": 50})
    admin.update_item(1, quantity=50)

    mock_patch.assert_called_once_with(
        f"{admin.BASE_URL}/1",
        json={"quantity": 50}
    )
    captured = capsys.readouterr()
    assert "200" in captured.out

@patch("admin.requests.delete")
def test_delete_item(mock_delete, capsys):
    mock_delete.return_value = _mock_response(200, {"message": "Item deleted"})
    admin.delete_item(1)

    mock_delete.assert_called_once_with(f"{admin.BASE_URL}/1")
    captured = capsys.readouterr()
    assert "200" in captured.out
