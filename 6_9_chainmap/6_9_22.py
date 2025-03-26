import json
from collections import ChainMap

with open('zoo.json', 'r', encoding='utf-8') as f:
    text = ChainMap(*json.loads(f.read()))

res = sum(text.values())
print(res)




