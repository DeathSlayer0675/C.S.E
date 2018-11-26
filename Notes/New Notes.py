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