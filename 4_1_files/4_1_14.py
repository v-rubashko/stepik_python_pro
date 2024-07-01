import sys
counter = 0
for item in sys.stdin:
    if item.strip()[0] == "#":
        counter += 1

print(counter)