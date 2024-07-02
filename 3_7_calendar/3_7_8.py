import calendar
import datetime

dt = datetime.datetime.strptime(input(), "%Y %b")

print(calendar.month(dt.year, dt.month))
