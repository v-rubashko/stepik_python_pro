from datetime import datetime, timedelta

pattern = "%d.%m.%Y"
today = datetime.strptime(input(), pattern)
emp = [input().split() for _ in range(int(input()))]
bd_7 = []

for item in emp:
    temp_today = datetime(year=(datetime.strptime(item[2], pattern) - timedelta(days=7)).year, month=today.month, day=today.day)
    if temp_today + timedelta(days=7) >= datetime.strptime(item[2], pattern) > temp_today:
        bd_7.append([f"{item[0]} {item[1]}", datetime.strptime(item[2], pattern)])

if len(bd_7) != 0:
    print(max(bd_7, key=lambda x: x[1])[0])
else:
    print("Дни рождения не планируются")