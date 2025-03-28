def convert(number):
    return (bin(number).replace('0b', ''), oct(number).replace('0o', ''), hex(number).replace('0x', '').upper())


print(convert(15))

print(convert(-24))

print(convert(1))
