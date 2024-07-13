import json, datetime

pattern = "%H:%M"
with open("pools.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    res = {}
    date_start = datetime.datetime.strptime("10:00", pattern)
    date_end = datetime.datetime.strptime("12:00", pattern)
    for item in data:
        time_open = datetime.datetime.strptime(item["WorkingHoursSummer"]["Понедельник"].split("-")[0], pattern)
        time_close = datetime.datetime.strptime(item["WorkingHoursSummer"]["Понедельник"].split("-")[1], pattern)
        if time_open <= date_start and time_close >= date_end:
            res.setdefault(item["Address"], (item["DimensionsSummer"]["Length"], item["DimensionsSummer"]["Width"]))

pool_max = max(res, key=lambda x: (float(res[x][0]), float(res[x][1])))
print(f"{res[pool_max][0]}x{res[pool_max][1]}")
print(pool_max)
