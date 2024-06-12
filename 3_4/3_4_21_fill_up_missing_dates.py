from datetime import datetime, timedelta

def fill_up_missing_dates(dates):
    pattern = "%d.%m.%Y"
    dates_convert = [datetime.strptime(dt, pattern) for dt in dates]
    res = []
    temp = sorted(dates_convert)[0]

    while temp <= sorted(dates_convert)[-1]:
        res.append(temp.strftime(pattern))
        temp += timedelta(days=1)

    return res

dates = ['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021']

print(fill_up_missing_dates(dates))