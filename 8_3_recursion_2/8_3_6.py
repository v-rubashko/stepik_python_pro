def number_count(number):
    if number // 10 == 0:
        return 1
    else:
        return 1 + number_count(number // 10)

print(number_count(int(input())))