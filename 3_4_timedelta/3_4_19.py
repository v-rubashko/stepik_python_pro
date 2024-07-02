from datetime import timedelta, datetime

pattern = "%d.%m.%Y"
user_date = datetime.strptime(input(), pattern)
temp = 2

for i in range(10):
    print(user_date.strftime(pattern))
    user_date += temp * timedelta(hours=24)
    temp += 1