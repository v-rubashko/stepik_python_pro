import csv

with open("titanic.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file, delimiter=";"))

res = [print(x[1]) for x in sorted(data[1:], key=lambda x: x[2], reverse=True) if int(x[0]) == 1 and float(x[-1]) < 18]
