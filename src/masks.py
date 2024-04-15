from typing import Union


def get_mask_card(number_card: Union[str | int]) -> str:
    """ Функции, возвращающая маску карты"""
    number_card = str(number_card).replace(' ', '')    # replace - для избежания возможных пробелов во вводе
    return f"{number_card[:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: Union[str | int]) -> str:
    """ Функции, возвращающая маску счета"""
    number_card = str(number_card).replace(' ', '')    # replace - для избежания возможных пробелов во вводе
    return f"**{number_card[-4:]}"
