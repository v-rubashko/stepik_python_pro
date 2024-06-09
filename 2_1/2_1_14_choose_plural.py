def choose_plural(amount, declensions):
    rule = {2: [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 0: [1], 1: [2, 3, 4]}
    for key, value in rule.items():
        if amount % 100 in value:
            return f"{amount} {declensions[key]}"
        elif amount % 10 in value:
            return f"{amount} {declensions[key]}"


print(choose_plural(12, ('гвоздь', 'гвоздя', 'гвоздей')))