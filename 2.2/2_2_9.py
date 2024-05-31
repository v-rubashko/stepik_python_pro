with open("files.txt", "r", encoding="utf-8") as file:
    files = list(map(str.strip, file.readlines()))

files_dict = {}

for item in files:
    name = item.split()[0]
    size = item.split()[1]
    ext = item.split()[2]
    files_dict[name.split(".")[1]] = files_dict.setdefault(name.split(".")[1], [])
    files_dict[name.split(".")[1]].append([name, size, ext])
    files_dict[name.split(".")[1]].sort()

sort_files_dict = dict(sorted(files_dict.items()))

current = {
    "B": 1,
    "KB": 1024,
    "MB": 1048576,
    "GB": 1073741824
}

for value in sort_files_dict.values():
    size_sum = 0
    for item in value:
        size_sum += int(item[1]) * current[item[2]]
        print(item[0])
    print("----------")
    if size_sum / 1073741824 > 1:
        size_result = str(int(size_sum / 1073741824 + 0.5)) + " GB"
    elif size_sum / 1048576 > 1:
        size_result = str(int(size_sum / 1048576 + 0.5)) + " MB"
    elif size_sum / 1024 > 1:
        size_result = str(int(size_sum / 1024 + 0.5)) + " KB"
    else:
        size_result = str(size_sum) + " B"
    print(f"Summary: {size_result}\n")
