def is_power(number):
    if number == 1:
        return True
    elif number % 2 == 0:
        return is_power(number / 2)
    else:
        return False



print(is_power(512))
print(is_power(1))
print(is_power(5))
print(is_power(6))
print(is_power(8))
