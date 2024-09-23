from zipfile import ZipFile
import json

with ZipFile("data.zip") as zip_file:
    info = zip_file.infolist()
    res = []
    for item in info:
        current_file = item.filename
        if current_file.split(".")[-1] == "json":
            with zip_file.open(current_file) as file:
                try:
                    data = json.loads(file.read().decode("utf-8"))
                except:
                    pass
                if data["team"] == "Arsenal":
                    res.append(data["first_name"] + " " + data["last_name"])

print(*sorted(res), sep="\n")

