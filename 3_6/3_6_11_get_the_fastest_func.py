import math
import time
from math import factorial


def get_the_fastest_func(funcs, arg):
    res = {}
    for i in funcs:
        time_start = time.perf_counter()
        i(arg)
        time_end = time.perf_counter()
        res[i] = time_end - time_start
    return min(res, key=res.get)


def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))