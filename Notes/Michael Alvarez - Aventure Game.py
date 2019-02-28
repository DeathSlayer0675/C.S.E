world_map = {
    "OFFICE": {
        "NAME": "Security Office",
        "DESCRIPTION": "This is the room you are in right now."
                       "There are doors on each side of you that lead "
                       "to the East and West hallways.",
        'PATHS': {
            'WEST': "WEST_HALLWAY",
            'EAST': "EAST_HALLWAY"
        }
    },
    'WEST_HALLWAY': {
        "NAME": "West Hallway",
        "DESCRIPTION": "This hallway connects the dining area to the security office"
                       "There appears to be a door to your left "
                       "that leads to the supply closet",
        "PATHS": {
            'NORTH': "DINING_AREA",
            'EAST': "OFFICE",
            'WEST': "SUPPLY_CLOSET"
        }
    },
    'EAST_HALLWAY': {
        "NAME": "East Hallway",
        "DESCRIPTION": "This hallway connects the dining area "
                       "to the security office",
        "PATHS": {
            'NORTH': "DINING_AREA",
            'WEST': "OFFICE"
        }
    },
    'DINING AREA': {
        "NAME": "Dining Area",
        "DESCRIPTION": "There are a few party hats on the tables"
                       "The animatronics are standing on stage"
        ,
        'PATHS': {
            'NORTH': "SHOW_STAGE",
            'WEST': "WEST_HALLWAY",
            'EAST': "EAST_HALLWAY",
            'SOUTH_EAST': "PIRATES_COVE"
        }
    },
    'SHOW_STAGE': {
        "NAME": "Show Stage",
        "DESCRIPTION": "This hallway connects the dining area to the security office"
                       "There appears to be a door to your left "
                       "that leads to the supply closet",
        "PATHS": {
            'NORTH': "DINING_AREA",
        }
    },
    'PIRATES_COVE': {
        "NAME": "East Hallway",
        "DESCRIPTION": "This hallway connects the dining area "
                       "to the security office",
        "PATHS": {
            'NORTH': "DINING_AREA",

        }
    },
    "Bean": {
        "NAME": "Dining Area",
        "DESCRIPTION": "There are a few ",
    },
}