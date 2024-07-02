import calendar
from datetime import datetime

dt = datetime.strptime(input(), "%Y-%m-%d")

print(calendar.day_name[dt.weekday()])