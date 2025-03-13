from collections import Counter

def count_occurences(word, words):
    res = Counter(map(lambda x: x.lower(), words.split()))
    return res[word.lower()]

word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))