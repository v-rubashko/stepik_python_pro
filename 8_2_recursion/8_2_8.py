def rec():
    x = int(input())
    if x != 0:
        rec()
    print(x)

rec()