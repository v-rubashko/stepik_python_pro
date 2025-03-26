def func(start, end):
    if start <= end:
        print(start)
        func(start + 1, end)

func(1, 100)