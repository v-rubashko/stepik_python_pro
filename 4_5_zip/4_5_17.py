from zipfile import ZipFile
from datetime import datetime

dead_line = datetime(2021, 11, 30, 14, 22, 0)

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    result = []
    for item in info:
        if not item.is_dir():
            if datetime(*item.date_time) > dead_line:
                result.append(item.filename.split("/")[-1])

print(*sorted(result), sep="\n")
