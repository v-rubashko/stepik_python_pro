from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
date_1 = datetime.strptime(input(), pattern)
date_2 = datetime.strptime(input(), pattern)

while not (date_1.day + date_1.month) % 2:
    date_1 += timedelta(days=1)

while date_1 <= date_2:
    if date_1.weekday() != 0 and date_1.weekday() != 3:
        print(date_1.strftime(pattern))
    date_1 += timedelta(days=3)