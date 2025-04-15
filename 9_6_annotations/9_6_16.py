def cyclic_shift(numbers: list[int | float], step: int) -> None:
    numbers[:] = [numbers[i - step % len(numbers)] for i in range(len(numbers))]


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)