def sum_number(number):
    if number < 10:
        return number
    else:
        return number % 10 + sum_number(number // 10)
    pass

print(sum_number(int(input())))