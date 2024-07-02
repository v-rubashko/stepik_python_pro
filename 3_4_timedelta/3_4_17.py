from datetime import timedelta, datetime

pattern = "%H:%M:%S"
dt = datetime.strptime(input(), pattern) + timedelta(seconds=int(input()))

print(dt.strftime(pattern))

print(datetime.strptime(input(), pattern))