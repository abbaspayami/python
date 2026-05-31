import csv

with open("docs/data.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "name", "salary"])
    writer.writerow([1, "Abbas", 100])
    writer.writerow([2, "Nikoo", 200])

with open("docs/data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)