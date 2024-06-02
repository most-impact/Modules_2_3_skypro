import os

import requests
from dotenv import load_dotenv

from src.logger import setup_logger

load_dotenv()
API_KEY = os.getenv("API_KEY")

logger = setup_logger()


def get_current_exchange_rate(transaction: dict) -> float:
    # Получение актуального курса доллара и/или евро в рублях
    try:
        currency = transaction["operationAmount"]["currency"]["code"]
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers).json()
        logger.info("Функция get_mask_card выполнена успешно")
        return float(response["rates"]["RUB"])
    except (requests.exceptions.RequestException, KeyError, ValueError) as e:
        logger.error(f"Ошибка {e} в функции get_current_exchange_rate")
        return 1.0
