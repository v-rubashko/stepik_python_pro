import json, csv

with open("students.json", "r", encoding="utf-8") as file_in, open("data.csv", "w", encoding="utf-8", newline="") as file_out:
    data = json.load(file_in)
    res = []
    for item in data:
        if item["age"] >= 18 and item["progress"] >= 75:
            res.append([item["name"], item["phone"]])
    writer = csv.writer(file_out)
    writer.writerow(["name", "phone"])
    writer.writerows(sorted(res))
