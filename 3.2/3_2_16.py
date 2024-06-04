from datetime import date


def is_correct(user_input):
    day, month, year = user_input.split(".")
    try:
        date(int(year), int(month), int(day))
        return True
    except:
        return False


temp = ""
count = 0
while temp != "end":
    temp = input()
    if temp == "end":
        pass
    elif is_correct(temp):
        print("Корректная")
        count += 1
    else:
        print("Некорректная")

print(count)
