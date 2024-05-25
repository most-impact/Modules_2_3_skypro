import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_data_by_path(path: str) -> list[str] | dict:
    """Возвращает список словарей с информацией о банковских операциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list) or isinstance(data, dict):
                return data
            else:
                raise ValueError("Invalid data format")
    except FileNotFoundError:
        return []


def get_current_exchange_rate(transaction: dict[str, Any]) -> float:
    # Получение актуального курса доллара и/или евро в рублях
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers).json()
        return response["rates"]["RUB"] * float(transaction["operationAmount"]["amount"])

    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"An error {e}")
        return 1.0


print(get_current_exchange_rate({
    "id": 619287771,
    "state": "EXECUTED",
    "date": "2019-08-19T16:30:41.967497",
    "operationAmount": {
        "amount": "81150.87",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 17691325653939384901",
    "to": "Счет 49304996510329747621"
}))
