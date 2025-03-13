from collections import Counter

with open('name_log.csv', 'r') as f:
    info = [line.strip().split(',')[1] for line in f.readlines()[1:]]

for k, v in sorted(Counter(info).items()):
    print(f'{k}: {v}')


