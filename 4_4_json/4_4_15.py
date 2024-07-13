import json

with open("food_services.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    district_all = {}
    operating_all = {}
    for item in data:
        district_all.setdefault(item["District"], 0)
        district_all[item["District"]] += 1
        if item["OperatingCompany"]:
            operating_all.setdefault(item["OperatingCompany"], 0)
            operating_all[item["OperatingCompany"]] += 1
    district_max = max(district_all, key=lambda x: district_all[x])
    operating_max = max(operating_all, key=lambda x:operating_all[x])

print(f"{district_max}: {district_all[district_max]}")
print(f"{operating_max}: {operating_all[operating_max]}")
