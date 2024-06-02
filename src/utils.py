import json
import os
from typing import Any

from dotenv import load_dotenv

from src.external_api import get_current_exchange_rate
from src.logger import setup_logger

load_dotenv()
API_KEY = os.getenv("API_KEY")

logger = setup_logger()


def get_data_by_path(path: str) -> list[str] | dict:
    """Возвращает список словарей с информацией о банковских операциях"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list) or isinstance(data, dict):
                logger.info("Функция get_currency_rate выполнена успешно")
                return data
            else:
                logger.error("Данные имеют неправильный формат")
                return []
    except FileNotFoundError:
        logger.error("Такой директории или файла не существует")
        return []


def sum_of_transaction(transaction: dict[str, Any]) -> float:
    # Получение суммы транзакции в рублях
    rate = get_current_exchange_rate(transaction)
    if rate:
        logger.info("Функция sum_of_transaction выполнена успешно")
        return rate * float(transaction["operationAmount"]["amount"])
    else:
        logger.error("С функцией sum_of_transaction что-то пошло не так")
        return 1.0
