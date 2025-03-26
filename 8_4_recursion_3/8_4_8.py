def dict_travel(nested_dicts):
    res = []
    for key, value in nested_dicts.items():
        if not isinstance(value, dict):
            res.append(f'{key}: {value}')
        if isinstance(value, dict):
            dict_travel(value)
    return print(*sorted(res), sep='\n')

data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'c': 2}

dict_travel(data)