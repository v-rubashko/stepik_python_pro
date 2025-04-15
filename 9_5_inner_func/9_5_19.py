from datetime import date

def date_formatter(country_code):
    d = {'ru': '%d.%m.%Y',
         'us': '%m-%d-%Y',
         'ca': '%Y-%m-%d',
         'br': '%d/%m/%Y',
         'fr': '%d.%m.%Y',
         'pt': '%d-%m-%Y'}
    return lambda date_obj: date_obj.strftime(d[country_code])

date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('us')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('ca')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('br')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('fr')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('pt')
today = date(2022, 1, 25)
print(date_ru(today))