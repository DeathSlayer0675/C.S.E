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
                       "The animatronics are standing on stage",

        'PATHS': {
            'NORTH': "SHOW_STAGE",
            'NORTH_WEST': "BACKSTAGE",
            'WEST': "WEST_HALLWAY",
            'EAST': "EAST_HALLWAY",
            'SOUTH_WEST': "PIRATES_COVE",
            'SOUTH_EAST': "KITCHEN",
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
            'EAST': "DINING_AREA",
        }
    },
    "RESTROOMS": {
        "NAME": "Restrooms",
        "DESCRIPTION": "There are two restrooms",
    },
}

playing = True
current_node = world_map['OFFICE']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
