import csv

with (open("prices.csv", "r", encoding="utf-8") as file):
    reader = csv.DictReader(file, delimiter=";")
    rows = list(reader)
    res = []
    for row in rows:
        temp = []
        temp.append(row["Магазин"])
        del row["Магазин"]
        temp.extend(min(row.items(), key=lambda x: (int(x[1]), x[0])))
        res.append(temp)
    min_price_product = min(res, key=lambda x: (int(x[2]), x[1], x[0]))

print(f"{min_price_product[1]}: {min_price_product[0]}")
