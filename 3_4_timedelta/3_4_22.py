from datetime import datetime, timedelta

pattern = '%H:%M'
start = datetime.strptime(input(), pattern)
end = datetime.strptime(input(), pattern)
temp = start
dt = timedelta(minutes=45)

while temp <= end - dt:
    print(f"{temp.strftime(pattern)} - {(temp + dt).strftime(pattern)}")
    temp += dt + timedelta(minutes=10)