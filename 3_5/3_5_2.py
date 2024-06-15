from datetime import datetime, timedelta

res = {x:0 for x in range(7)}
start = datetime.strptime("13.01.0001", "%d.%m.%Y")
end = datetime.strptime("13.12.9999", "%d.%m.%Y")

while start <= end:
    if start.day == 13:
        res[start.weekday()] += 1
    start += timedelta(days=1)

for value in res.values():
    print(value)