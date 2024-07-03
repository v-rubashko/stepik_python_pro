import csv

with open("deniro.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file))

column_number = int(input())
s_d = sorted(data, key=lambda x: int(x[column_number - 1]) if x[column_number - 1].isdigit() else x[column_number - 1])
for item in s_d:
    print(*item, sep=",")