import pytest

from src.widget import get_mask_result, time_conversion


@pytest.mark.parametrize(
    "x, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **6758"),
        ("MasterCard 7158300734726758", "MasterCard 6831 98** **** 7658"),
        ("Счет 35383033474447895560", "Счет **5229"),
        ("Visa Classic 6831982476737658", "Visa Classic 5999 41** **** 6353"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 5999 41** **** 6353"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **6353"),
    ],
)
def test_get_mask_result(x: str, expected: str) -> None:
    """Возвращает исходную строку с замаскированным номером карты/счета"""
    assert get_mask_result(x) == expected


@pytest.mark.parametrize(
    "y, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ],
)
def test_time_conversion(y: str, expected: str) -> None:
    """Функции, возвращающая маску счета"""
    assert time_conversion(y) == expected
