import sys

a = sorted([line.split() for line in sys.stdin], key = lambda x: int(x[1]))
print(a[1][0])