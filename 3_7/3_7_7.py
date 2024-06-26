import calendar

years = [int(input()) for _ in range(int(input()))]

for item in years:
    print(calendar.isleap(item))