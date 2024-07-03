import csv

data_dict = {}

with open("salary_data.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file, delimiter=";"))
    for row in data[1:]:
        data_dict.setdefault(row[0], [])
        data_dict[row[0]].append(int(row[1]))

res_sorted = sorted(data_dict, key=lambda x: (sum(data_dict[x]) / len(data_dict[x]), x))
print(*res_sorted, sep = "\n")