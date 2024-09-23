from zipfile import ZipFile

with ZipFile("desktop.zip") as zip_file:
    info = zip_file.infolist()
    mult = 0
    for item in info:
        temp_item = item.filename.split('/')
        if "." in temp_item[-1]:
            if item.file_size / 1073741824 > 1:
                size_result = str(int(item.file_size / 1073741824 + 0.5)) + " GB"
            elif item.file_size / 1048576 > 1:
                size_result = str(int(item.file_size / 1048576 + 0.5)) + " MB"
            elif item.file_size / 1024 > 1:
                size_result = str(int(item.file_size / 1024 + 0.5)) + " KB"
            else:
                size_result = str(item.file_size) + " B"
            temp = f"{'  ' * (len(temp_item) - 1)}{temp_item[-1]} {size_result}"
        else:
            temp = "  " * (len(temp_item) - 2) + temp_item[-2]
        print(temp)


