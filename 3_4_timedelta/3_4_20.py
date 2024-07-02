from datetime import timedelta, datetime

pattern = "%d.%m.%Y"
dates = [datetime.strptime(x, pattern) for x in input().split()]
res = []

for i in range(len(dates) - 1):
    temp = dates[i] - dates[i + 1]
    res.append(abs(temp.days))

print(res)