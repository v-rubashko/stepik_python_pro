def triangle(h):
    if h > 0:
        print('*' * h)
        triangle(h - 1)

triangle(3)
triangle(5)