from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

all_prod = ChainMap(bread, meat, sauce, vegetables, toppings)
user_input = Counter(input().split(','))
total = 0
max_len = max(map(lambda x: len(f'{x} x {user_input[x]}'), user_input))

for k, v in sorted(user_input.items()):
    total += v * all_prod[k]
    print(f'{k.ljust(max_len - 2 - len(str(v)))}x {v}')

max_len = max(len(f'ИТОГ: {total}р'), max_len)

print('-' * max_len)
print(f'ИТОГ: {total}р')


