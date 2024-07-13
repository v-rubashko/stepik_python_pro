import json

with open("food_services.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    types = {}
    for item in data:
        types.setdefault(item["TypeObject"], [])
        types[item["TypeObject"]].append([item["Name"], item["SeatsCount"]])
    res = []
    for key, value in types.items():
        res.append([key, *max(value, key=lambda x: x[1])])
    res.sort()

for i in res:
    print(f"{i[0]}: {i[1]}, {i[2]}")
