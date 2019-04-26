import csv


def validate(num: str):
    if not all 16_digits(num):
        return False
    if divisible_by_2(num) and divisible_by_3(num):
        return True
    return False


def divisible_by_3(num: str):
    first_num = int(num[0])
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False

def all_16_digits
# with open("Book1.csv", 'r') as old_csv:
#     reader = csv.reader(old_csv)
#     for row in reader:
#         old_number = row[0]
#         # print(int(old_number) + 1)
#         print(old_number)
#
#
# with open ("MyNewFile.csv", 'w', newline='') as old_csv:
#     print("Writing file...")
#     reader = csv.reader(old_csv)
#     writer = csv.writer(new_csv)
#     for row in reader:
#         old_number = row[0]
#         first_num = int(old_number)

with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            if validate(old_number):
                writer.writerow(row)
    print("Done")