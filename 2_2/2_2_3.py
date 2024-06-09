n, x, y, a, b = [int(number) for number in input().split()]
user_output = list(range(1, n + 1))
user_output[x - 1:y] = reversed(user_output[x - 1:y])
user_output[a - 1:b] = reversed(user_output[a - 1:b])
print(*user_output)