def power(degree):
    def mult(x):
        return x ** degree
    return mult

square = power(2)
print(square(5))

print(power(3)(3))

result = power(4)(2)
print(result)