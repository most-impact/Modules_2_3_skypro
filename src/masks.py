from src.logger import setup_logger

logger = setup_logger()


def get_mask_card(number_card: str) -> str:
    """Функции, возвращающая маску карты"""
    if len(number_card) == 16:
        number_card = str(number_card).replace(" ", "")  # replace - для избежания возможных пробелов во вводе
        logger.info("Функция get_mask_card выполнена успешно")
        return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"
    else:
        logger.error("В функции get_mask_card что-то пошло не так")
        return ""


def get_mask_account(number_card: str) -> str:
    """Функции, возвращающая маску счета"""
    if len(number_card) == 21:
        number_card = str(number_card).replace(" ", "")  # replace - для избежания возможных пробелов во вводе
        logger.info("Функция get_mask_account выполнена успешно")
        return f"**{number_card[-4:]}"
    else:
        logger.error("В функции get_mask_account что-то пошло не так")
        return ""
