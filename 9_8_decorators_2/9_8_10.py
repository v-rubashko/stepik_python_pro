import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return res
        else:
            raise TypeError

    return wrapper


@returns_string
def nothing():
    return

print(nothing.__name__)
print(nothing.__doc__)

try:
    nothing()
except TypeError as e:
    print(type(e))