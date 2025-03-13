from collections import Counter

def print_bar_chart(data, mark):
    res = Counter(data)
    max_len = len(max(res, key=lambda x: len(x)))
    for k, v in res.most_common():
        print(f'{k.ljust(max_len)} |{mark * v}')



languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']

print_bar_chart('beegeek', '+')
print_bar_chart(languages, '#')