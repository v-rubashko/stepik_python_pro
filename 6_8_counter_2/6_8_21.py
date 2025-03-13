import csv
import json
from collections import Counter


def product_sum(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        result = {}
        for item in list(csv.reader(f))[1:]:
            result[item[0]] = int(item[1]) + int(item[2]) + int(item[3])
    return Counter(result)

product_total = product_sum('quarter1.csv') + product_sum('quarter2.csv') + product_sum('quarter3.csv') + product_sum('quarter4.csv')

with open('prices.json', 'r', encoding='utf-8') as f:
    prices = json.loads(f.read())

itogo = 0
for k, v in product_total.items():
    itogo += product_total[k] * prices[k]

print(itogo)