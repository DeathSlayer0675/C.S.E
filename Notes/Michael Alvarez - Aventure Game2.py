health_level = 100


class Room(object):
    def __init__(self, name, north, east, south, west, items=None, character=None, description=True):
        if items is None:
            items = []
        if character is None:
            character = []
        self.name = name
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.description = description
        self.items = items
        self.character = character


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []


class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name: str, health: int, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.inventory = []

    def take_damage(self, damage: int):
        if self.armor.armor_amt > damage:
            print("No damage is done because of some AMAZING armor.")
        else:
            self.health -= damage - self.armor.armor_amt
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
flashlight = Item("Flashlight")
crowbar = Weapon("Crowbar", 20)
microphone = Weapon("Microphone", 60)
evil_cupcake = Weapon("Cupcake", 80)
hook = Weapon("Pirate Hook", 45)
knife = Weapon("Knife", 35)
torch = Weapon("Blow Torch", 50)
magic_hat = Weapon("Magic Hat", 50)
dragon_helm = Armor("Helmet of Pyrokinesis", 15)
raven_plate = Armor("Chest-plate of Necromancy", 40)
leggings = Armor("Leggings of Teleportation", 30)
polar_boots = Armor("Boots of Permafrost", 15)
Stradivari = Weapon("Fiddle of Fire", 75)

# Characters
Orc = Character("Mac", 100, microphone, Armor("Generic Armor", 2))
Orc2 = Character("Bonnie", 100, crowbar, raven_plate)
Orc3 = Character("Chica", 100, evil_cupcake, Armor("Generic Armor", 2))
Orc4 = Character("Endo", 100, Weapon("Retractable Claws", 15*2), raven_plate)
Orc5 = Character("Freddy", 100, microphone, None)
Orc6 = Character("Foxy", 100, hook, Armor("Generic Armor", 2))
Orc7 = Character("Nightmare Freddy", 100, microphone, magic_hat)


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
            'SOUTHEAST': "F_RESTROOM"
        }
    },

    "M_RESTROOM": {
        "NAME": "M Restroom",
        "DESCRIPTION": "There appears to be a hatch "
                       "in one of the stalls",

        'PATHS': {
            'DOWN': "BASEMENT",
            'WEST': "RESTROOMS"

        }
    },

    "F_RESTROOM": {
        "NAME": "F Restroom",
        "DESCRIPTION": "There are four stalls. "
                       "One has a dead woman in it. "
                       "She appears to be wearing a key around her neck. ",
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
