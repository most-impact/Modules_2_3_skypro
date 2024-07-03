from datetime import datetime


def get_result_by_value(lst_with_dict: list, value: str = "EXECUTED") -> list:
    """Возвращает список, содержащий словари, у которых ключ state содержит переданное в функцию значение"""
    return [item for item in lst_with_dict if "state" in item and item["state"] == value]


def sort_lst_by_date(lst_with_dict: list, bool_value: bool = True) -> list:
    """Возвращает список, содержащий словари, у которых ключ state содержит переданное в функцию значение"""
    sorted_dates = sorted(lst_with_dict, key=lambda x: datetime.fromisoformat(x["date"]), reverse=bool_value)
    return sorted_dates
