from typing import Iterator, Union


def filter_by_currency(transactions: list[dict[str, Union[int, str, dict[str, dict[str, str]]]]], currency: str)\
        -> Iterator[dict[str, Union[int, str, dict[str, dict[str, str]]]]]:
    """Возвращает итераторы по очереди операции, в которых указана заданная валюта"""
    for item in transactions:
        if item["operationAmount"]["currency"]["code"] == currency:
            yield item


def transaction_descriptions(transactions: list[dict[str, Union[int, str, dict[str, dict[str, str]]]]]) -> Iterator[str]:
    """Возвращает итератор по описаниям транзакций"""
    for item in transactions:
        yield item["description"]


def card_number_generator(from_: int, to_: int) -> Iterator[str]:
    """Возвращает сгенерированный номер карты"""
    for i in range(from_, to_ + 1):
        result = str(i).zfill(16)
        yield f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:]}"
