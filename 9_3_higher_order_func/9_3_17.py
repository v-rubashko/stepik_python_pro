def print_operation_table(operation, rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(str(operation(i, j)).ljust(3), end=' ')
        print()


print_operation_table(lambda a, b: a * b, 5, 5)

print_operation_table(pow, 5, 4)