import functools

def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            res_start = res[:start]
            res_end = res[end:]
            size = len(res) - len(res_start + res_end)
            return res_start + char * size + res_end

        return wrapper

    return decorator


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())