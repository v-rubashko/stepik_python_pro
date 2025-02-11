from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open("data.pkl", "rb") as file:
    data = pickle.load(file)

for item in data:
    for i, j in zip(Animal._fields, item):
        print(f"{i}: {j}")
    print()

