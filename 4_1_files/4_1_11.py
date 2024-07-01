import sys
from datetime import datetime

data = [datetime.strptime(line.strip(), "%Y-%m-%d") for line in sys.stdin]

print((max(data) - min(data)).days)