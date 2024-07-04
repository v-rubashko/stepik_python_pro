import csv

with open("wifi.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file, delimiter=";"))

res = {}
for item in data[1:]:
    res[item[1]] = res.setdefault(item[1], 0) + int(item[-1])

for key, value in dict(sorted(sorted(res.items()), key=lambda x: x[1], reverse=True)).items():
    print(f"{key}: {value}")