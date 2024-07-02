from datetime import date, timedelta


def get_all_mondays(year):
    res = []
    dt = date(year, 1, 1)

    while dt.weekday() != 0:
        dt += timedelta(days=1)

    while dt.year == year:
        res.append(dt)
        dt += timedelta(days=7)

    return res


print(get_all_mondays(2021))