from datetime import date

def print_good_dates(dates):
    for item in sorted(dates):
        if item.year == 1992 and item.day + item.month == 29:
            print(item.strftime('%B %d, %Y'))

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)