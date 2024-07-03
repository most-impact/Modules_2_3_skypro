import re
from collections import Counter


def get_dict_by_search_string(transactions_list: list, search_string: str) -> list:
    """Функция, которая возвращает список словарей с наличием строки поиска в описании"""
    result = [
        transaction
        for transaction in transactions_list
        if "description" in transaction and re.search(search_string, transaction["description"])
    ]
    return result


def categorize_transactions(transactions_list: list, categories: dict) -> dict:
    """Подсчет операций в каждой категории"""
    category_counts_2: dict = Counter()

    for transaction in transactions_list:
        if "description" in transaction:
            for category, keywords in categories.items():
                if any(keyword.lower() in transaction["description"].lower() for keyword in keywords):
                    category_counts_2[category] += 1
                    break

    return dict(category_counts_2)
