import sys, datetime

dates = [datetime.datetime.strptime(item.strip(), "%d.%m.%Y") for item in sys.stdin]

if len(dates) == len(set(dates)):
    if dates == sorted(dates):
        print("ASC")
    elif dates == sorted(dates, reverse=True):
        print("DESC")
    else:
        print("MIX")
else:
    print("MIX")
