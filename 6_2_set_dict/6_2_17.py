user_alpha = list(input())

my_dict = {}
temp = 97

for i in user_alpha:
    my_dict.setdefault(chr(temp), i)
    temp += 1

user_str = input()
res = ""
for j in user_str:
    if j.lower() in my_dict:
        res += my_dict[j.lower()]
    else:
        res += j

print(res)

