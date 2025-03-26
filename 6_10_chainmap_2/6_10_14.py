from collections import ChainMap

def deep_update(chainmap, key, value):
    if key in chainmap:
        for item in chainmap.maps:
            if key in item:
                item[key] = value
    else:
        chainmap[key] = value


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)