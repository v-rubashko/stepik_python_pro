fib = lambda n: n if n <= 1 else fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(5))