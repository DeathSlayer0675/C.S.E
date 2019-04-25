import csv

with open("Book1.csv", 'r') as old_csv:
    reader = csv.reader(old_csv)
    for row in reader:
        old_number = row[0]
        # print(int(old_number) + 1)
        print(old_number)

with open ("MyNewFile.csv", 'w', newline='') as old_csv:
    print("Writing file...")
    reader = csv.reader(old_csv)
    writer = csv.writer(new_csv)
    for row in reader:
        old_number = row[0]
        first_num = int(old_number)