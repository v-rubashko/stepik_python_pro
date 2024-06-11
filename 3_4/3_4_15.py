from datetime import timedelta, datetime

user_date = input()
user_date_formated = datetime.strptime(user_date, "%d.%m.%Y")
yesterday = user_date_formated - timedelta(days=1)
tomorrow = user_date_formated + timedelta(days=1)
print(yesterday.strftime("%d.%m.%Y"))
print(tomorrow.strftime("%d.%m.%Y"))