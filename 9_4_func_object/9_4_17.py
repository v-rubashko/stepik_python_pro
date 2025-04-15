def polynom(x):
    polynom.__dict__.setdefault('values', set())
    value = x ** 2 + 1
    polynom.__dict__['values'].add(value)
    return value


for _ in range(10):
    polynom(10)

print(polynom.values)