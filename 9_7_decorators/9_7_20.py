def upper_decorator(func):
    def wrapper(*args, **kwargs):
        args_changed = [str(x).upper() for x in args]
        kwargs_changed = {x:str(y).upper() for x, y in kwargs.items()}
        result = func(*args_changed, **kwargs_changed)
        return result

    return wrapper

print = upper_decorator(print)
print('hi', 'there', end='!')
print('are you in trouble?')
print(111, 222, 333, sep='xxx')



# def uppercase_decorator(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#
#     return wrapper
#
#
# @uppercase_decorator
# def greet():
#     return 'Hello world!'
#
# print(greet())