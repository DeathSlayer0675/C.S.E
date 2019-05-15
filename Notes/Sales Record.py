import csv

Total = 0
Divide = 0

with open("Sales Records.csv", 'r') as csv_old:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        print("Writing file...")
        reader = csv.reader(csv_old)
        item_list = []
        for row in reader:
            if row[0] == 'Region':
                continue
            item_type = row[2]
            if item_type not in item_list:
                item_list.append(item_type)
            if item_type == "Cosmetics":
                Total += float(row[13])
                Divide += 1

print(Total / Divide)
print(item_list)
