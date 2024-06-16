from datetime import datetime

pattern = "%d.%m.%Y"
emp = [input().split() for _ in range(int(input()))]
emp_dict = {}

for item in emp:
    emp_dict[datetime.strptime(item[2], pattern)] = emp_dict.setdefault(datetime.strptime(item[2], pattern), 0) + 1

print(*[key.strftime(pattern) for key, value in sorted(emp_dict.items()) if value == max(emp_dict.values())], sep="\n")