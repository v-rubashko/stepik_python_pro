from collections import Counter

with open("pythonzen.txt", "r") as file:
     text = file.read()

result = Counter([x.lower() for x in text if x.isalpha()])
for k, v in sorted(result.items()):
    print(f'{k}: {v}')
