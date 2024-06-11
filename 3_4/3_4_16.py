from datetime import timedelta

h, m, s = map(int, input().split(":"))
dt = timedelta(hours=h, minutes=m, seconds=s)

print(int(dt.total_seconds()))
