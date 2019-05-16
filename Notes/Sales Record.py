import csv

fruits = 0
clothes = 0
meat = 0
beverages = 0
office_supplies = 0
cosmetics = 0
snacks = 0
personal_care = 0
household = 0
vegetables = 0
baby_food = 0
cereal = 0

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

            if row[2] == "Fruits":
                fruits += float(row[13])

            if row[2] == "Clothes":
                clothes += float(row[13])

            if row[2] == "Meat":
                meat += float(row[13])

            if row[2] == "Beverages":
                beverages += float(row[13])

            if row[2] == "Office Supplies":
                office_supplies += float(row[13])

            if row[2] == "Cosmetics":
                cosmetics += float(row[13])

            if row[2] == "Snacks":
                snacks += float(row[13])

            if row[2] == "Personal Care":
                personal_care += float(row[13])

            if row[2] == "Household":
                household += float(row[13])

            if row[2] == "Vegetables":
                vegetables += float(row[13])

            if row[2] == "Baby Food":
                baby_food += float(row[13])

            if row[2] == "Cereal":
                cereal += float(row[13])

print("Fruits")
print(item_list)
