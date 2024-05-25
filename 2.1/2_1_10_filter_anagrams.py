def filter_anagrams(word, words):
    return [item for item in words if sorted(item) == sorted(word)]


print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))