import csv
with open("My_People.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        rows = [row for row in reader]


print(rows)