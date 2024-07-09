import sys, json

res = ""

for i in sys.stdin:
    res += i

data = json.loads(res)

for key, value in data.items():
    print(f"{key}: {value}" if type(value) is not list else f"{key}: {', '.join(map(str, value))}")