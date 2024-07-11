import csv, json

with open("playgrounds.csv", "r", encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter=";")
    res = {}
    for row in rows:
        res.setdefault(row["AdmArea"], {})
        res[row["AdmArea"]].setdefault(row["District"], [])
        res[row["AdmArea"]][row["District"]].append(row["Address"])

with open("addresses.json", "w", encoding="utf-8") as file_out:
    json.dump(res, file_out, indent=3, ensure_ascii=False)
