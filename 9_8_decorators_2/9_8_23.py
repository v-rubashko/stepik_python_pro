import functools

def add_attrs(**kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for key, value in kwargs.items():
            setattr(wrapper, key, value)

        return wrapper

    return decorator