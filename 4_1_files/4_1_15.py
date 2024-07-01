import sys

text = ""

for item in sys.stdin:
    if not item.strip().startswith("#"):
        text += item

print(text)