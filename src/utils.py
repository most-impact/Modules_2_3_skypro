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
    total = 0.0
    operation_sum = transaction.get("operationAmount", {})
    currency_code = operation_sum.get("currency", {}).get("code", "")
    amount = float(operation_sum.get("amount", 0.0))
    if currency_code in ["USD", "EUR"]:
        rate_to_rub = get_current_exchange_rate(currency_code)
        total += amount * rate_to_rub
    elif currency_code == "RUB":
        total += amount
        logger.info("Function sum_amount completed successfully")
        return total
    else:
        logger.error("Something went wrong with the sum_amount function: %(error)s")
    return total
