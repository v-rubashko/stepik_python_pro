def print_given(*args, **kwargs):
    for item in args:
        print(item, type(item))
    for item, value in sorted(kwargs.items()):
        print(item, value, type(value))

print_given(1, [1, 2, 3], 'three', two=2)