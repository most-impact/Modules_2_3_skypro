import pandas as pd


def read_csv_file(filename: str) -> list:
    if filename.endswith(".csv"):
        df = pd.read_csv(filename, encoding="utf-8")
        transactions = df.to_dict(orient="records")
        return transactions
    else:
        return []


def read_xlsx_file(filename: str) -> list:
    if filename.endswith(".xlsx"):
        data = pd.read_excel(filename)
        return data.to_dict("records")
    else:
        return []
