from zipfile import ZipFile
from datetime import datetime

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    res = {}
    for item in info:
        if not item.is_dir():
            res[item.filename.split("/")[-1]] = [item.date_time, item.file_size, item.compress_size]

for key, value in sorted(res.items()):
    print(key)
    print(f"  Дата модификации файла: {datetime(*value[0])}")
    print(f"  Объем исходного файла: {value[1]} байт(а)")
    print(f"  Объем сжатого файла: {value[2]} байт(а)")
    print()
