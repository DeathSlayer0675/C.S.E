states = {"CA": "California",
          "FL": "Florida",
          "AK": "Alaska",
          "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK":{
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA":{
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno"
            "Los Angeles"
            "San Francisco"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}

print(complex_dictionary["AK"]["CITIES"][0])

print(complex_dictionary["FL"]["NAME"])
print(complex_dictionary["GA"]["CITIES"][0])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items() :
    print(key)
    print(value)
    print("-" * 20)

print()
for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 20)
    print("=" * 20)
