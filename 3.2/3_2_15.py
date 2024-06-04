from datetime import date

def is_correct(day, month, year):
    try:
        date(int(year), int(month), int(day))


print(is_correct(31, 12, 2021))