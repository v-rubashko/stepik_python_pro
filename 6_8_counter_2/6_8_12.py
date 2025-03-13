from collections import Counter
x = Counter(input().lower().split()).most_common()
print(x[0][0])