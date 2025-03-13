from collections import Counter

line = input()
result = Counter(line.split(','))
for key, value in sorted(result.items()):
    print(f'{key}: {value}')