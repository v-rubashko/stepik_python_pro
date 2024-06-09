from datetime import datetime

with open("diary.txt", "r", encoding="utf-8") as file:
    notes = [x.strip("\n") for x in file.readlines()]

temp = []
res = []
for item in notes:
    if item != "":
        temp.append(item)
    else:
        res.append(temp)
        temp = []

res.append(temp)

for note in sorted(res, key=lambda x: datetime.strptime(x[0], "%d.%m.%Y; %H:%M")):
    print(note[0])
    print(*note[1:], sep="\n")
    print()