def dict_travel(nested_dicts):
    for k, v in sorted(nested_dicts.items()):
        if isinstance(v, dict):
            dict_travel({f'{k}.{key}': val for key, val in v.items()})
        else:
            print(f'{k}: {v}')

data = {'firstname': 'Тимур',
        'lastname': 'Гуев',
        'birthdate': {'day': 10, 'month': 'October', 'year': 1993},
        'address': {'streetaddress': 'Часовая 25, кв. 127',
                    'city': {'region': 'Московская область', 'type': 'город', 'cityname': 'Москва'},
                    'postalcode': '125315'}}

dict_travel(data)
