def linear(nested_lists):
    result = []
    for item in nested_lists:
        if isinstance(item, int):
            result.append(item)
        if isinstance(item, list):
            result.extend(linear(item))
    return result

my_list = [3, [4], [5, [6, [7, 8]]]]

print(linear(my_list))

my_list = [10, 20, 30, 40, 50]

print(linear(my_list))