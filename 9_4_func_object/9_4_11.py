old_print = print
def print(*args, sep=' ', end='\n'):
    old_print(*[item.upper() if isinstance(item, str) else item for item in args], sep=sep.upper(), end=end.upper())


print('beegeek', [1, 2, 3], 4)

print('bee', 'geek', sep=' and ', end=' wow')

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' 1to ', end=' LOVE')