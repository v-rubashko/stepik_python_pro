import csv, datetime

with open("name_log.csv", "r", encoding="utf-8") as file, open("new_name_log.csv", "w", encoding="utf-8", newline="") as file_out:
    data, writer = list(csv.reader(file)), csv.writer(file_out)
    writer.writerow(data[0])
    writer.writerows({i[1]: i for i in sorted(data[1:], key=lambda x: (x[1], x[2]))}.values())
