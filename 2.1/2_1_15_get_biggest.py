def get_biggest(numbers):
    if numbers:
        res = ""
        while numbers:
            temp = str(max(sorted(numbers, reverse=True), key=lambda x: int(str(x)[0])))
            for item in filter(lambda x: str(x)[0] == temp[0], numbers):
                if len(temp) > len(str(item)):
                    if str(item) + temp > temp + str(item):
                        temp = str(item)
            res += temp
            numbers.remove(int(temp))

        return int(res)
    else:
        return -1



print(get_biggest([13, 221, 423, 53, 1, 2, 22, 58, 78554, 34, 65, 65, 2, 1]))
