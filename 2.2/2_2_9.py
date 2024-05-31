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
print(sort_files_dict)


# print(files)