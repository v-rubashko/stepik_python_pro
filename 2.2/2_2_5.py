user_input = [i for i in range(1, int(input()) + 1)]
res_dict = {}
for item in user_input:
    item_sum = 0
    for i in str(item):
        item_sum += int(i)
    res_dict[item_sum] = res_dict.get(item_sum, []) + [item]
res = max(map(lambda x: len(x), res_dict.values()))
print(res)
