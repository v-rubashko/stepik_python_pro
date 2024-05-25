def is_valid(string):
    return string.isdigit() and len(string) in (4, 5, 6)

print(is_valid("1098123"))