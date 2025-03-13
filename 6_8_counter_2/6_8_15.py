from collections import Counter

words = Counter(input().lower().split())
res = {}
for key, value in words.items():
    res[len(key)] =res.get(len(key), 0) + 1 * value

for key, value in sorted(res.items(), key=lambda x: x[1]):
    print(f'Слов длины {key}: {value}')
