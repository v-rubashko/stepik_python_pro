import csv


def condense_csv(file_name, id_name):
    with open(file_name, "r", encoding="utf-8") as file_in, open("condensed.csv", "w", encoding="utf-8", newline="") as file_out:
        data, writer = csv.reader(file_in), csv.writer(file_out)
        column = [id_name]
        res = {}
        for item in data:
            res[item[0]] = res.setdefault(item[0], [item[0]])
            res[item[0]].append(item[2])
            if item[1] not in column:
                column.append(item[1])
        writer.writerow(column)
        writer.writerows(res.values())

condense_csv("data_4_20.csv", id_name="ID")

