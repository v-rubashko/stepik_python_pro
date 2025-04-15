def zip_longest(*args, fill=None):
    max_len = max(map(len, args))
    for item in args:
        if len(item) < max_len:
            item.extend([fill] * (max_len - len(item)))
    return [item for item in zip(*args)]

print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))