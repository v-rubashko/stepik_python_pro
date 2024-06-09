def index_of_nearest(numbers, number):
    if numbers:
        minimum = min(numbers, key=lambda num: abs(number - num))
        return numbers.index(minimum)
    return -1

print(index_of_nearest([7, 13, 3, 5, 18], 0))