user_input = [i for i in input().split()]
res_dict = {}
for item in user_input:
    temp = res_dict.setdefault(item, 0)
    res_dict[item] += 1
res = [int(key) for key in res_dict.keys() if res_dict[key] > 1]
print(*sorted(res))
