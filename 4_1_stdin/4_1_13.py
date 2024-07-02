import sys

data = [int(x) for x in sys.stdin]

print(f"Рост самого низкого ученика: {min(data)}\n"
      f"Рост самого высокого ученика: {max(data)}\n"
      f"Средний рост: {sum(data) / len(data)}" if data else "нет учеников")