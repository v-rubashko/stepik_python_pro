from zipfile import ZipFile

with ZipFile("workbook.zip") as zip_file:
    info = zip_file.namelist()
    count = 0
    for i in info:
        if "." in i:
            count += 1

print(count)
