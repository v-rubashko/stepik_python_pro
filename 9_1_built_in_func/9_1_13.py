def my_pow(number):
    number_str = str(number)
    return sum(int(x[1]) ** x[0] for x in enumerate(number_str, 1))


print(my_pow(139))

print(my_pow(123))

print(my_pow(0))