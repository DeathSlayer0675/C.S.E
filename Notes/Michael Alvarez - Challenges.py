# Challenge 1
def challenge1(first_name, last_name):

    return last_name + ", " + first_name


name1 = challenge1("Michael", "Alvarez")
print(name1)

# Challenge 2
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))
# Challenge 3
b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)
# Challenge 4
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
# Challenge 5
r = 3
area = 3.14*r**2
print(area)

# Challenge 6
rad = 5
volume = 1.33 * 3.14 * r**3
print(volume)

# Challenge 7
n = 3
value = n + (n * n) + (n * n * n)
print(value)

# Challenge 8


def near_thousand(x):
    return (abs(1000 - x) <= 100) or (abs(2000 - x) <= 100)


print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))
print(near_thousand(2200))

# Challenge 9


def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels


print(is_vowel('c'))
print(is_vowel('e'))