from datetime import timedelta, datetime

def num_of_sundays(year):
    dt = datetime(year=year, month=1, day=1)
    counter = 0
    while dt.year == year:
        if dt.weekday() == 6:
            counter += 1
        dt += timedelta(hours=24)
    return counter

print(num_of_sundays(768))