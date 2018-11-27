# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "gray", "magenta", "lime"]  # USE SQUARE BRACKETS!!!!!
print(colors)
print(colors[1])
print(colors[0])

# Length of colors list
print("There are %d things in the list." % len(colors))

# Changing Elements in a list
colors[1] = "green"
print(colors)

# Looping through lists
for item in colors:
    print(item)

disney_movies = ["Dumbo", "Lion King", "Mulan", "Beauty and The Beast", "Toy Story", "Snow White", "Cinderella"]
disney_movies[2] = "Alladin"
print(disney_movies)
print("The last thing is the list is %s" % disney_movies[len(disney_movies) - 1])

# Slicing a list
print(disney_movies[0:3])
print(disney_movies[0:4])
print(disney_movies[0:])
print(disney_movies[:4])

food_list = ["pizza", "tamales", "pie", "enchiladas", "burrito",
             "sushi", "poke", "flan", "poutine", "noodles", "chicken",
             "chile", "hot wings", "salmon", "chips", "lasagna", "soup",
             "fettuccine", "salad", "carne asada", "calamari", "tacos"]
print(len(food_list))

# Adding stuff to a list
food_list.append("bacon")
food_list.append("eggs")
# Notice that everything is object.method(parameters)
print(food_list)

food_list.insert(1, "waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)

snacks = ["ice cream", "pudding", "chips"]
print(len(snacks))

snacks.append("cookies")
print(snacks)

snacks.remove("chips")
print(snacks)

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)

# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Hangman hints
for i in range(len(list1)):
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")
'''
For character in list1:
    if character == "u":
        # repace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")


'''

