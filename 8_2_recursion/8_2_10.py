def triangle(h):
    if h > 1:
        triangle(h - 1)
    print('*' * h)

triangle(3)
triangle(5)