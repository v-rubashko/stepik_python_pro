from datetime import date

def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 2)

print(get_date_range(date1, date2))