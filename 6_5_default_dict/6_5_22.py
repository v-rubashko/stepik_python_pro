from collections import defaultdict

def wins(pairs):
    res = defaultdict(set)
    for item in pairs:
        res[item[0]].add(item[1])
    return res


result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))