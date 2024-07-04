import csv

with open("data.csv", "r", encoding="utf-8") as file_input:
    data_input = list(csv.reader(file_input))

column = ["domain", "count"]
res = {}
for item in data_input[1:]:
    res[item[2].split("@")[1]] = res.setdefault(item[2].split("@")[1], 0) + 1

with open("domain_usage.csv", "w", encoding="utf-8", newline="") as file_output:
    data_output = csv.writer(file_output, )
    data_output.writerow(column)
    for item in sorted(res.items(), key=lambda x: (x[1], x[0])):
        data_output.writerow(item)