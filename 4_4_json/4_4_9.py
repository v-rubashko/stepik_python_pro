import json

with open("people.json", "r", encoding="utf-8") as file:
    data = json.load(file)

res = set()

for item in data:
    for key in item.keys():
        res.add(key)

for item in data:
    for key in res:
        item.setdefault(key, None)

with open("updated_people.json", "w", encoding="utf-8") as file_out:
    json.dump(data, file_out, indent=3)