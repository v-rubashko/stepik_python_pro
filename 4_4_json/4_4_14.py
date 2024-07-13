import json, csv, datetime

with open("exam_results.csv", "r", encoding="utf-8") as file_in:
    rows = list(csv.reader(file_in))
    res = {}
    for item in rows[1:]:
        key = item[0] + " " + item[1] + " " + item[4]
        res.setdefault(key, [])
        res[key].append([int(item[2]), datetime.datetime.fromisoformat(item[3])])

with open("best_scores.json", "w", encoding="utf-8") as file_out:
    res_out = []
    for key, value in res.items():
        best_score = max(value)
        res_out.append({"name": key.split()[0], "surname": key.split()[1], "best_score": max(value)[0],
                        "date_and_time": datetime.datetime.isoformat(max(value)[1], sep=" "), "email": key.split()[2]})
    res_out.sort(key=lambda x: x["email"])
    json.dump(res_out, file_out, indent=3)
