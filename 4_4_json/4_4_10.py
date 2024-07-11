import json

with open("countries.json", "r", encoding="utf-8") as file:
    data = json.load(file)

res = {}

for item in data:
    res.setdefault(item["religion"], [])
    res[item["religion"]].append(item["country"])

with open("religion.json", "w", encoding="utf-8") as file_out:
    json.dump(res, file_out, indent=3)
