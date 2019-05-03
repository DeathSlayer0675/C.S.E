#The Luhn Formula:

#Drop the last digit from the number. The last digit is what we want to check against
#Reverse the numbers
#Multiply the digits in odd positions (1, 3, 5, etc.) by 2 and subtract 9 to all any result higher than 9
#Add all the numbers together
#The check digit (the last number of the card) is the amount that you would need to add to get a multiple of 10 (Modulo 10)

def validate(num: str):
    print(num)
    if not has_16_digits(num, str):
        return False
    return False




def has_16_digits(num,str):
    if len(num) == 16:
        print("16 = Y")
        return True

def take_last_digit(num, str):
    list_num = list(num)
    for index in range(len(list_num)):
        list_num.pop(15)





def reverse_it(string):
    print(string[::1])

reverse_it(num)

def has_16_digits(num, str):
    if len(num) == 16:
        print("16 = Y")

print(valid_card_number("4140606127913240"))
list_num = list(number)
for index in range(len(list_num)):
    list_num(index) = int(list_num[index])