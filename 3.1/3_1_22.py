from datetime import date

def saturdays_between_two_dates(start, end):
    if end < start:
        start, end = end, start
    return sum(date.fromordinal(item).weekday() == 5 for item in range(start.toordinal(), end.toordinal() + 1))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)

print(saturdays_between_two_dates(date1, date2))