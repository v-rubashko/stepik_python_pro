def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)


numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)



numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)