import csv

with (open("student_counts.csv", "r", encoding="utf-8") as file,
      open("sorted_student_counts.csv", "w", encoding="utf-8", newline="") as file_out):
    reader = csv.DictReader(file)
    column = ["year"] + sorted(reader.fieldnames[1:], key=lambda x: (int(x.split("-")[0]), x.split("-")[1]))
    rows = list(reader)
    writer = csv.DictWriter(file_out, fieldnames=column)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)
