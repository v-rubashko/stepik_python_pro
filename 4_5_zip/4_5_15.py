from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    sum_file_size = 0
    sum_file_compressed = 0
    for item in info:
        sum_file_size += item.file_size
        sum_file_compressed += item.compress_size

print(f"Объем исходных файлов: {sum_file_size} байт(а)")
print(f"Объем сжатых файлов: {sum_file_compressed} байт(а)")
