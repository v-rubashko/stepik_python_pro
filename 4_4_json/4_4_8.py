import json

with open("data1.json", "r", encoding="utf-8") as file_1, open("data2.json", "r", encoding="utf-8") as file_2:
    data_1 = json.load(file_1)
    data_2 = json.load(file_2)

data = {**data_1, **data_2}

with open("data_merge.json", "w", encoding="utf-8") as file_out:
    json.dump(data, file_out)
