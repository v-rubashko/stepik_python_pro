from datetime import date, timedelta


def get_all_thursday(year):
    res = []
    for i in range(1, 13):
        dt = date(year, i, 1)
        while dt.weekday() != 3:
            dt += timedelta(days=1)
        temp = 1
        for j in range(3):
            if temp == 3:
                res.append(dt)
            temp += 1
            dt += timedelta(days=7)

    return res


for item in get_all_thursday(int(input())):
    print(item.strftime("%d.%m.%Y"))