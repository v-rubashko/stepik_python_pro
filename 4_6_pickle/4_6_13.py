import pickle
import sys

data = [item.strip("\n") for item in sys.stdin]


# def func(*args):
#     return ' '.join(args)
#
#
# with open(data[0], "wb") as file:
#     pickle.dump(func, file)

with open(data[0], "rb") as file:
    obj = pickle.load(file)

print(obj(*data[1:]))
