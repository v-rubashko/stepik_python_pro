from datetime import datetime, timedelta

pattern = "%H:%M"
pattern_date = "%d.%m.%Y"

schedule = {
    0: (datetime.strptime("9:00", pattern), datetime.strptime("21:00", pattern)),
    1: (datetime.strptime("9:00", pattern), datetime.strptime("21:00", pattern)),
    2: (datetime.strptime("9:00", pattern), datetime.strptime("21:00", pattern)),
    3: (datetime.strptime("9:00", pattern), datetime.strptime("21:00", pattern)),
    4: (datetime.strptime("9:00", pattern), datetime.strptime("21:00", pattern)),
    5: (datetime.strptime("10:00", pattern), datetime.strptime("18:00", pattern)),
    6: (datetime.strptime("10:00", pattern), datetime.strptime("18:00", pattern))
}

user_input = input().split()
user_date = datetime.strptime(user_input[0], pattern_date)
user_time = datetime.strptime(user_input[1], pattern)

if schedule[user_date.weekday()][0] <= user_time < schedule[user_date.weekday()][1]:
    print(int((schedule[user_date.weekday()][1] - user_time).total_seconds() // 60))
else:
    print("Магазин не работает")
