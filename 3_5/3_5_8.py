from datetime import datetime, timedelta

def choose_plural(amount, declensions):
    rule = {2: [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 0: [1], 1: [2, 3, 4]}
    for key, value in rule.items():
        if amount % 100 in value:
            return f"{amount} {declensions[key]}"
        elif amount % 10 in value:
            return f"{amount} {declensions[key]}"

template = [["день", "дня", "дней"], ["час", "часа", "часов"], ["минута", "минуты", "минут"]]
pattern = "%d.%m.%Y %H:%M"
start = datetime.strptime("08.11.2022 12:00", pattern)
today = datetime.strptime(input(), pattern)
dt = start - today

if dt.total_seconds() > 0:
    d = int(dt.total_seconds() // 86400)
    h = int((dt.total_seconds() - d * 86400) // 3600)
    m = int((dt.total_seconds() - d * 86400 - h * 3600) // 60)
    part_1 = (choose_plural(d, template[0]) if d >= 1 else "")
    part_2 = (choose_plural(h, template[1]) if h >= 1 else "")
    part_3 = (choose_plural(m, template[2]) if m >= 1 else "")
    if d:
        if h:
            print(f"До выхода курса осталось: {part_1} и {part_2}")
        else:
            print(f"До выхода курса осталось: {part_1}")
    elif h:
        if m:
            print(f"До выхода курса осталось: {part_2} и {part_3}")
        else:
            print(f"До выхода курса осталось: {part_2}")
    else:
        print(f"До выхода курса осталось: {part_3}")
else:
    print("Курс уже вышел!")