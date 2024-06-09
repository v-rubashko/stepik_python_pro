def spell(*args):
    res = {}
    for item in args:
        if res.get(item[0].lower(), 0) < len(item):
            res[item[0].lower()] = len(item)
    return res


words = ['Россия', 'Австрия', 'Австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*words))