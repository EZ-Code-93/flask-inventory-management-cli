import sys
import pytest
from unittest.mock import patch
import main

@patch("main.admin.get_all")
def test_cli_list(mock_get_all, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "list"])
    main.main()
    mock_get_all.assert_called_once()

@patch("main.admin.get_one")
def test_cli_get(mock_get_one, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "get", "2"])
    main.main()
    mock_get_one.assert_called_once_with(2)

@patch("main.admin.create_item")
def test_cli_add(mock_create_item, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "add", "Laptop", "7"])
    main.main()
    mock_create_item.assert_called_once_with("Laptop", 7)

@patch("main.admin.update_item")
def test_cli_update(mock_update_item, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "update", "1", "--name", "Monitor", "--quantity", "12"])
    main.main()
    mock_update_item.assert_called_once_with(1, "Monitor", 12)

@patch("main.admin.delete_item")
def test_cli_delete(mock_delete_item, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py", "delete", "1"])
    main.main()
    mock_delete_item.assert_called_once_with(1)

def test_cli_missing_command_exits(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["main.py"])
    with pytest.raises(SystemExit):
        main.main()
