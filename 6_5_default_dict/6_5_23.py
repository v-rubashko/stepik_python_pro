from collections import defaultdict

def flip_dict(dict_of_list):
    res = defaultdict(list)
    for k, v in dict_of_list.items():
        for i in v:
            res[i].append(k)
    return res


data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')