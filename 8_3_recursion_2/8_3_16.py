def to_binary(number):
    if number <= 1:
        return str(number)
    return to_binary(number // 2) + str(number % 2)




print(to_binary(256))


