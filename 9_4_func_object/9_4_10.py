def numbers_sum(elems):
    '''Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.'''
    res = 0
    for item in elems:
        if type(item) in (int, float):
            res += item
    return res

print(numbers_sum([1, '2', 3, 4, 'five']))

print(numbers_sum.__doc__)