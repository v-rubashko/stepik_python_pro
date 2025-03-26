def get_all_values(nested_dicts, key):
    result = set()
    if key in nested_dicts:
        result.add(nested_dicts[key])
    for item in nested_dicts.values():
        if isinstance(item, dict):
            value = get_all_values(item, key)
            result.update(value)
    return result

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))