def takes_positive(func):
    def wrapper(*args, **kwargs):
        for item in args:
            if not isinstance(item, int):
                return TypeError
            elif item <= 0:
                return ValueError

        for value in kwargs.values():
            if not isinstance(value, int):
                return TypeError
            elif value <= 0:
                return ValueError

        return func(*args, **kwargs)

    return wrapper
