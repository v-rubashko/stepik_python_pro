import time

def calculate_it(func, *args):
    time_start = time.perf_counter()
    res = func(*args)
    time_end = time.perf_counter()
    return res, time_end - time_start

def add(a, b, c):
    time.sleep(3)
    return a + b + c

print(calculate_it(add, 1, 2, 3))