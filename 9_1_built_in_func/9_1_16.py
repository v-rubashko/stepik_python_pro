text = input()

list_1 = []
list_2 = []
list_3 = []
list_4 = []

for i in text:
    if i.islower():
        list_1.append(i)
    elif i.isupper():
        list_2.append(i)
    elif int(i) % 2 == 1:
        list_3.append(i)
    else:
        list_4.append(i)
result = sorted(list_1) + sorted(list_2) + sorted(list_3) + sorted(list_4)
print(*result, sep='')