import json
from typing import Any
from unittest.mock import patch

from src.utils import get_current_exchange_rate, get_data_by_path

sample = {
    "id": 667307132,
    "state": "EXECUTED",
    "date": "2019-07-13T18:51:29.313309",
    "operationAmount": {"amount": "97853.86", "currency": {"code": "RUB"}},
    "description": "Перевод с карты на счет",
    "from": "Maestro 1308795367077170",
    "to": "Счет 96527012349577388612",
}


@patch("builtins.open", create=True)
def test_get_data_by_path() -> None:
    """Тестирование функции get_data_by_path"""
    with patch("builtins.open") as mock_open:
        path = "data/operations.json"
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = json.dumps(sample)
        assert get_data_by_path(path) == sample
        mock_open.assert_called_once_with(path, "r", encoding="utf-8")


@patch("requests.get")
def test_get_current_rate(mock_get: Any) -> None:
    """Тестирование функции get_current_exchange_rate"""
    mock_get.return_value.json.return_value = {"rates": {"RUB": 1}}
    assert get_current_exchange_rate(sample) == 97853.86
