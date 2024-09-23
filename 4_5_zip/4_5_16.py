from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.infolist()
    cur_koef = 1
    for item in info:
        if not item.is_dir():
            if item.compress_size / item.file_size < cur_koef:
                cur_koef = item.compress_size / item.file_size
                cur_name = item.filename.split("/")[-1]

print(cur_name)
