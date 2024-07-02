import calendar
from datetime import datetime, date

def get_days_in_month(year, month):
    dt = datetime.strptime(str(year) + month, "%Y%B")
    res = []
    for item in range(1, calendar.monthrange(dt.year, dt.month)[1] + 1):
        res.append(date(dt.year, dt.month, item))
    return res

print(get_days_in_month(2021, 'December'))