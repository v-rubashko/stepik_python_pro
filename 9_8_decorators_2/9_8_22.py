import functools

def takes(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*largs, **kwargs):
            for item in largs + tuple(kwargs.values()):
                if type(item) not in args:
                    return TypeError
            return func(*largs, **kwargs)

        return wrapper

    return decorator