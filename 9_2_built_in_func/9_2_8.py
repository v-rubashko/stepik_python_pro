def hash_as_key(objects):
    result = {}
    for item in objects:
        if hash(item) not in result:
            result[hash(item)] = item
        elif not isinstance(result[hash(item)], list):
            result[hash(item)] = [result[hash(item)]] + [item]
        else:
            result[hash(item)].append(item)
    return result

data = [1, 2, 5, 3, 4, 5, 5]

print(hash_as_key(data))


data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))


data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))

data = [(1, 2, 3), (1, 2, 3), (0, 0, 0), 10, (144, 75, 60), 20, 30]

print(hash_as_key(data))