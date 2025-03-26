def recursive_sum(nested_lists):
    res = 0
    for item in nested_lists:
        if isinstance(item, int):
            res += item
        if isinstance(item, list):
            res += recursive_sum(item)
    return res

my_list = [1, [4, 4], 2, [1, [2, 10]]]

print(recursive_sum(my_list))

my_list = []

print(recursive_sum(my_list))