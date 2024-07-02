import sys

data = [int(x) for x in sys.stdin]
if len(data) % 2 == 0:
    print("Дима" if data[-1] % 2 == 0 else "Анри")
else:
    print("Анри" if data[-1] % 2 == 0 else "Дима")
