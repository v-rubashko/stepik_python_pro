from collections import ChainMap

def get_all_values(chainmap, key):
    return {d[key] for d in chainmap.maps if key in d}


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)