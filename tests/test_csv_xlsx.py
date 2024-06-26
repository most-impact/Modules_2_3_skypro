import unittest
from typing import Any
from unittest.mock import patch

import pandas as pd

from src.csv_xlsx import read_xlsx_file, read_csv_file


def test_return_value_from_csv_file() -> None:
    """Проверка функции read_xlsx_file на корректность возвращаемых данных"""
    file_path = "../data/transactions.csv"
    transactions = read_csv_file(file_path)
    assert isinstance(transactions, list)
    assert all(isinstance(transaction, dict) for transaction in transactions)


def test_valid_csv_file() -> None:
    """Проверка функции read_csv_file на обработку файла другого формата"""
    file_path = "data.txt"
    transactions_ = read_csv_file(file_path)
    assert transactions_ == []


@patch("pandas.read_excel")
def test_read_from_xlsx(read_excel: Any) -> None:
    """Тестирование функции read_xlsx_file"""
    read_excel.return_value = pd.DataFrame({"Date": ["2022-01-01", "2022-02-01"], "Amount": [100.00, 200.00]})
    result_read_xlsx_file = read_xlsx_file("../data/transactions_excel.xlsx")
    expected_result = [{"Date": "2022-01-01", "Amount": 100.00}, {"Date": "2022-02-01", "Amount": 200.00}]
    unittest.TestCase().assertEqual(result_read_xlsx_file, expected_result)
