from collections import Counter

line = input()
result = Counter(line.split(','))
max_len = len(max(result, key=lambda x: len(x)))
for key, value in sorted(result.items()):
    temp = 0
    for i in key:
        temp += ord(i) if i != ' ' else 0
    print(f'{key:{max_len}}: {temp} UC x {value} = {temp * value} UC')