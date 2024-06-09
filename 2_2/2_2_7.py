glas_let = ("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")
pattern = [i for i, c in enumerate(input()) if c in glas_let]
res = []
for _ in range(int(input())):
    word = input()
    pattern_temp = [i for i, c in enumerate(word) if c in glas_let]
    if pattern == pattern_temp:
        res.append(word)
print(*res, sep="\n")
