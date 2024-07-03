import re
import time
from typing import Any

from src.csv_xlsx import read_csv_file, read_xlsx_file
from src.generators import transaction_descriptions
from src.library_re import get_dict_by_search_string
from src.processing import get_result_by_value, sort_lst_by_date
from src.utils import get_data_by_path, sum_of_transaction
from src.widget import get_mask_result, time_conversion


def format_open_file() -> Any:
    """Функция для открытия определённого файла"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    file_open = input("Выберите необходимый пункт меню: 1.JSON 2.CSV 3.Excel\n")
    if file_open == "1" or file_open.lower() == "json":
        print("Для обработки выбран json файл.")
        return get_data_by_path("data/operations.json")
    elif file_open == "2" or file_open.lower() == "csv":
        print("Для обработки выбран CSV файл.")
        return read_csv_file("data/transactions.csv")
    elif file_open == "3" or file_open.lower() == "excel":
        print("Для обработки выбран Excel файл.")
        return read_xlsx_file("data/transactions_excel.xlsx")
    else:
        print("Некорректный ввод, повторите ввод")
        return format_open_file()


def filter_status(data: list) -> list:
    """Функция для выбора статуса EXECUTED, CANCELED, PENDING"""
    print("Введите статус по которому необходимо выполнить фильтрацию.")
    format_ = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
    if format_.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        print("Статус не корректен, введите ещё раз")
        return filter_status(data)

    data = get_result_by_value(data, format_.upper())
    return data


def sort_by_date(data: list) -> list | dict:
    """Сортирует список транзакций"""
    sort = input("Отсортировать операции по дате? Да/Нет \n")
    if sort.lower() == "да":
        figure = input("1.По возрастанию 2.По убыванию \n")
        if figure.lower() in ["по возрастанию", "1"]:
            return sort_lst_by_date(data)
        elif figure.lower() in ["по убыванию", "2"]:
            return sort_lst_by_date(data, bool_value=True)
        else:
            print("Не корректное значение, введите ещё раз")
            return sort_by_date(data)
    elif sort.lower() == "нет":
        return data
    else:
        print("Не корректный ответ, повторите ввод")
        return sort_by_date(data)


def filter_user_keyword(data: list) -> Any:
    """Фильтрация по введённому слову"""
    keyword = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет \n")
    if keyword.lower() == "да":
        find_ = input("Что бы вы хотели найти?\n")
        return get_dict_by_search_string(data, find_)
    elif keyword.lower() == "нет":
        return data
    else:
        print("Некорректный ввод, введите ещё раз")
        return filter_user_keyword(data)


def print_transaction(data: list) -> None:
    """Вывод отформатированного списка транзакций"""
    print("Распечатываю итоговый список транзакций")
    time.sleep(2)
    if data and len(data) != 0:
        descriptions_iterator = transaction_descriptions(data)
        for transaction in data:
            print(time_conversion(transaction["date"]), next(descriptions_iterator))
            if re.search("Перевод", transaction["description"]):
                print(get_mask_result(transaction["from"]), "->", get_mask_result(transaction["to"]))
            else:
                print(get_mask_result(transaction["to"]))
                print(f"Сумма: {sum_of_transaction(transaction)} руб.")
    else:
        print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")


def main() -> None:
    """Функция запускающая обработку транзакций"""
    result = format_open_file()
    result = filter_status(result)
    result = sort_by_date(result)
    result = filter_user_keyword(result)
    print_transaction(result)


if __name__ == "__main__":
    main()
