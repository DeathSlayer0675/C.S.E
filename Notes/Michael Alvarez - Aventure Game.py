class Room(object):
    def __init__(self, name, description=True, north=None, south=None, east=None, items=[]):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.description = description
        self.items = items


world_map = {
    "PIZZERIA": {
        "NAME": "Security Office",
        "DESCRIPTION": "This is the room you are in right now. "
                       "There are doors on each side of you that leads "
                       "to the East and West hallways.",
        'PATHS': {
            'WEST': "WEST_HALLWAY",
            'EAST': "EAST_HALLWAY"
        }
    },
    'WEST_HALLWAY': {
        "NAME": "West Hallway",
        "DESCRIPTION": "This hallway connects the dining area to the security office. "
                       "There appears to be a door to your left "
                       "that leads to the supply closet",
        'PATHS': {
            'NORTH': "DINING_AREA",
            'EAST': "OFFICE",
            'WEST': "SUPPLY_CLOSET"
        }
    },
    'EAST_HALLWAY': {
        "NAME": "East Hallway",
        "DESCRIPTION": "This hallway connects the dining area "
                       "to the security office",
        'PATHS': {
            'NORTH': "DINING_AREA",
            'WEST': "OFFICE"
        }
    },
    'SUPPLY_CLOSET': {
        "NAME": "Supply Closet",
        "DESCRIPTION": "There's a flashlight on the wall "
                       "and a crow bar on the floor.",
        'PATHS': {
            'EAST': "WEST_HALLWAY"
        }
    },
    'DINING_AREA': {
        "NAME": "Dining Area",
        "DESCRIPTION": "There are a few party hats on the tables. "                       
                       "The animatronics are standing on stage",

        'PATHS': {
            'NORTHWEST': "BACKSTAGE",
            'NORTH': "SHOW_STAGE",
            'EAST': "RESTROOMS",
            'SOUTHEAST': "KITCHEN",
            'SOUTH': "EAST_HALLWAY",
            'SOUTHWEST': "WEST_HALLWAY",
            'WEST': "PIRATES_COVE"
        }
    },
    'SHOW_STAGE': {
        "NAME": "Show Stage",
        "DESCRIPTION": "There are three animatronics standing here. ",

        'PATHS': {
            'SOUTH': "DINING_AREA",
        }
    },

    'BACKSTAGE': {
        "NAME": "Backstage",
        "Description": "There appears to be an endoskeleton "
                       "sitting on the table. ",
        'Paths': {
            'EAST': "DINING_AREA"
        }
    },

    "RESTROOMS": {
        "NAME": "Restrooms",
        "DESCRIPTION": "There are two restrooms",

        'PATHS': {
            'WEST': "DINING_AREA",
            'NORTHEAST': "M_RESTROOM",
        }
    },

    "M_RESTROOM": {
        "NAME": "M Restroom",
        "DESCRIPTION": "There appears to be a hatch "
                       "in one of the stalls",

        'PATHS': {
            'UP': "",
            'DOWN': "",
            'WEST': ""

        }
    },

    "F_RESTROOM": {
        "NAME": "F Restroom",
        "DESCRIPTION": "",
    },

    'KITCHEN': {
        "NAME": "Kitchen",
        "DESCRIPTION": "There is a knife in the cutting board.",

        'PATHS': {
            'EAST': "DINING_AREA",
        }
    },
    'PIRATES_COVE': {
        "NAME": "Pirates Cove",
        "DESCRIPTION": "Foxy is rested on his stand. "
                       "His hook and eye-patch seem detachable.",
        'PATHS': {
            'EAST': "DINING_AREA",
        }
    }
}

playing = True
current_node = world_map['PIZZERIA']
directions = ['NORTH', 'NORTHEAST', 'EAST', 'SOUTHEAST', 'SOUTH',
              'SOUTHWEST', 'WEST', 'NORTHWEST', 'UP', 'DOWN']

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
