from collections import ChainMap

def get_value(chainmap, key, from_left=True):
    if key not in chainmap:
        return None
    elif from_left:
        return chainmap[key]
    else:
        chainmap.maps.reverse()
        return chainmap[key]
    pass

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))
