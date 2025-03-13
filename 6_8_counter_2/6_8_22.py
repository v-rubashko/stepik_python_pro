from collections import Counter

text = Counter(input().split())
total = 0
for i in range(int(input())):
    klass, price = input().split()
    temp = Counter({klass:1})
    text.subtract(temp)
    if text[klass] >= 0:
        total += int(price)

print(total)