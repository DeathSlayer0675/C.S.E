import csv

with open("Sales Records.csv", 'r') as csv_old:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...")
        reader = csv.reader(csv_old)
        for row in reader:
            row = row[13]
            print(row)
print("Ok")
