def clock(number, length, delta):
    if number < 4:
        print(" " * delta + str(number) * length + " " * delta)
        clock(number + 1, length - 4, delta + 2)
    print(" " * delta + str(number) * length + " " * delta)

clock(1, 16, 0)