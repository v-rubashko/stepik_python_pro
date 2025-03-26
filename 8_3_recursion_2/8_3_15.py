def is_palindrome(string):
    if len(string) < 2:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False

print(is_palindrome('stepik'))
print(is_palindrome('levvel'))
print(is_palindrome('122333221'))