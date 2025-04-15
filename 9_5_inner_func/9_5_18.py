def sourcetemplate(url):
    def func(**kwargs):
        if kwargs:
            result = url + '?' + '&'.join(key + '=' + str(value) for key, value in sorted(kwargs.items()))
        else:
            result = url
        return result
    return func

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load(name='timur'))

url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))

url = 'https://beegeek.ru'
load = sourcetemplate(url)
print(load())

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))