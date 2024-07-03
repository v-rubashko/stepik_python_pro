import csv

def csv_columns(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))
    return {key: value for key, *value in zip(*data)}


print(csv_columns("data.csv"))