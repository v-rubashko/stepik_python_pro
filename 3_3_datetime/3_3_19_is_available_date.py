from datetime import datetime

def is_available_date(booked_dates, date_for_booking):
    period = []
    if "-" in date_for_booking:
        date_start, date_end = date_for_booking.split("-")
        period.append(datetime.strptime(date_start, "%d.%m.%Y"))
        period.append(datetime.strptime(date_end, "%d.%m.%Y"))
    else:
        period.append(datetime.strptime(date_for_booking, "%d.%m.%Y"))

    for item in booked_dates:
        if "-" in item:
            booked_start, booked_end = datetime.strptime(item.split("-")[0], "%d.%m.%Y"), datetime.strptime(item.split("-")[1], "%d.%m.%Y")
            if len(period) == 1:
                if booked_start <= period[0] <= booked_end:
                    return False
            else:
                if period[0] <= booked_start <= period[1] or period[0] <= booked_end <= period[1] or (booked_start < period[0] and booked_end > period[1]):
                    return False
        else:
            if len(period) == 1:
                if datetime.strptime(item, "%d.%m.%Y") == period[0]:
                    return False
            else:
                if period[0] <= datetime.strptime(item, "%d.%m.%Y") <= period[1]:
                    return False
    return True

dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))