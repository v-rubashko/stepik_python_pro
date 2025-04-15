func = input()
a, b = input().split()
res = [eval(func) for x in range(int(a), int(b) + 1)]

print(f'Минимальное значение функции {func} на отрезке [{a}; {b}] равно {min(res)}')
print(f'Максимальное значение функции {func} на отрезке [{a}; {b}] равно {max(res)}')