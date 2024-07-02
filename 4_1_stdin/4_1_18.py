import sys

data = [int(x.strip()) for x in sys.stdin]
ap = set()
gp = set()
for i in range(1, len(data) - 1):
    if data[i] - data[i - 1] == data[i + 1] - data[i]:
        ap.add(1)
    else:
        ap.add(2)

    if data[i] / data[i - 1] == data[i + 1] / data[i]:
        gp.add(1)
    else:
        gp.add(2)

if 2 not in ap and 1 in ap:
    print("Арифметическая прогрессия")
elif 2 not in gp and 1 in gp:
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")