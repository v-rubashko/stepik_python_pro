import pickle

file_name = input()
control_number = int(input())

with open(file_name, "rb") as file:
    obj = pickle.load(file)

data = [item for item in obj if isinstance(item, int)]
if data:
    if isinstance(obj, dict):
        res = sum(data)
    else:
        res = min(data) * max(data)
else:
    res = 0

print("Контрольные суммы совпадают" if control_number == res else "Контрольные суммы не совпадают")
