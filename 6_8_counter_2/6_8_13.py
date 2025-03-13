from collections import Counter

fruits = Counter(input().lower().split())
min_fruit = min(fruits.values())
print(*sorted(filter(lambda x: fruits[x] == min_fruit, fruits)), sep=', ')
