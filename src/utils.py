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
        return float(response["rates"]["RUB"] * transaction["operationAmount"]["amount"])

    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        print(f"An error {e}")
        return 1.0
