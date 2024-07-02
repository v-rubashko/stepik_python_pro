import sys

res = [x.strip() for x in sys.stdin.readlines()]
category = res[-1]
res.pop(-1)
news = {}

for item in res:
    news.setdefault(item.split("/")[1].strip(), []).append([item.split("/")[0].strip(), item.split("/")[2].strip()])

for note in sorted(sorted(news[category]), key=lambda x: float(x[1])):
    print(note[0])