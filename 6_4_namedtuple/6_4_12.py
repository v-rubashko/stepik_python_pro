import csv
from collections import namedtuple
from datetime import datetime

friends = namedtuple("friends", ["surname", "name", "meeting_date", "meeting_time"])

with open("meetings.csv", "r", encoding="utf-8") as file:
    data = list(csv.reader(file))
    friends = namedtuple("friends", data[0])
    res = [friends(*item) for item in data[1:]]
    for item in sorted(res, key=lambda x: datetime.strptime(x.meeting_date + " " + x.meeting_time, "%d.%m.%Y %H:%M")):
        print(f"{item.surname} {item.name}")
