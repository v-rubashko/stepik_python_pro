n = [input().split(", ") for _ in range(int(input()))]
temp = n[0]
for i in range(1, len(n)):
    temp = set(temp).intersection(n[i])
if temp:
    print(*sorted(temp), sep=", ")
else:
    print("Сериал снять не удастся")
