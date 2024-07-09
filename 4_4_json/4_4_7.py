import json

with open("data.json", "r", encoding="utf-8") as file_in:
    data = json.load(file_in)

res =[]
for item in data:
    if item is not None:
        if isinstance(item, bool):
            res.append(not item)
        elif isinstance(item, str):
            res.append(item + "!")
        elif isinstance(item, int):
            res.append((item + 1))
        elif isinstance(item, list):
            res.append(item * 2)
        elif isinstance(item, dict):
            item["newkey"] = None
            res.append(item)

with open("updated_data.json", "w", encoding="utf-8") as file_out:
    json.dump(res, file_out)
