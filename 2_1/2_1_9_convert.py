def convert(string):
    count_lower = 0
    count_upper = 0
    for i in string:
        if i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
    if count_upper > count_lower:
        return string.upper()
    else:
        return string.lower()


print(convert('pi31415!'))