user_input = eval(input())

if isinstance(user_input, list):
    print(user_input[-1])
elif isinstance(user_input, tuple):
    print(user_input[0])
else:
    print(len(user_input))