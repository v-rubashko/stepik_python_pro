from collections import Counter

fruits = Counter(input().lower().split())
max_fuit = max(fruits.values())
print(sorted(filter(lambda x: fruits[x] == max_fuit, fruits))[-1])