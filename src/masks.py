def get_mask_card(number_card: str) -> str:
    """Функции, возвращающая маску карты"""
    type_card_or_account = " ".join(number_card.split()[:-1])
    return f"{type_card_or_account} {number_card[-16:-12]} {number_card[-12:-10]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """Функции, возвращающая маску счета"""
    return f"{''.join(number_card.split()[:-1])} **{number_card[-4:]}"
