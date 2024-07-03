import csv

import pandas as pd


def read_csv_file(filename: str) -> list:
    data = []
    with open(filename, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            data.append(row)
    return data


def read_xlsx_file(filename: str) -> list:
    if filename.endswith(".xlsx"):
        data = pd.read_excel(filename)
        return data.to_dict("records")
    else:
        return []
