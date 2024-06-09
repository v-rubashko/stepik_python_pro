from datetime import date

dates = [date.fromisoformat(input()) for _ in range(int(input()))]

for item in sorted(dates):
    print(item.strftime('%d/%m/%Y'))
