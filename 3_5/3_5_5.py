from datetime import datetime

pattern = "%d.%m.%Y"
emp = [input().split() for _ in range(int(input()))]
min_bd = min(emp, key=lambda x: datetime.strptime(x[2], pattern))
c = 0
temp_name = ""

for item in emp:
    if min_bd[2] in item:
        c += 1
        temp_name = f"{item[0]} {item[1]}"

print(f"{min_bd[2]} {temp_name}" if c == 1 else f"{min_bd[2]} {c}")