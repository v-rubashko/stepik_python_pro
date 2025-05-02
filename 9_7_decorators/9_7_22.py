def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = reversed(args)
        kwargs = {x: y for x, y in reversed(kwargs.items())}
        result = func(*args, **kwargs)
        return result

    return wrapper


# @reverse_args
# def power(a, n):
#     return a ** n
#
#
# print(power(2, 3))
#
#
# @reverse_args
# def concat(a, b, c):
#     return a + b + c
#
#
# print(concat('apple', 'cherry', 'melon'))


@reverse_args
def concat(a, b, c, d):
    return a + b + c + d


print(concat('apple', 'banan', c = 'cherry', d = 'melon'))