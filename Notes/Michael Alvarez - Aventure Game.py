health_level = 100


class Room(object):
    def __init__(self, name, north, northeast, east, southeast, south, southwest, west, northwest, up, down, items, character, description):
        if items is None:
            items = []
        if character is None:
            character = []
        self.name = name
        self.north = north
        self.northeast = northeast
        self.east = east
        self.southeast = southeast
        self.south = south
        self.southwest = southwest
        self.west = west
        self.northwest = northwest
        self.up = up
        self.down = down
        self.description = description
        self.items = items
        self.character = character


class Player(object):
    def __init__(self, starting_location,health_level, shield=0, weapon):
        self.current_location = starting_location
        self.inventory = []
        self.health = health_level
        self.shield = shield
        self.weapon = weapon


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
    def __init__(self, name: str, health: int, weapon, armor, drops=None):
        if drops is None:
            drops = []
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor
        self.inventory = []
        self.drops = drops

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
Orc = Character("Bonnie", 25, Weapon("Retractable Claws", 30), Armor("Exoskeleton", 50))
Orc2 = Character("Chica", 25, evil_cupcake, Armor("Exoskeleton", 50))
Orc3 = Character("Endo", 25, Weapon("Retractable Claws", 30), raven_plate)
Orc4 = Character("Freddy", 25, microphone, Armor("Exoskeleton", 50),[microphone])
Orc5 = Character("Foxy", 25, hook, Armor("Exoskeleton", 50),[hook])
Orc6 = Character("Nightmare Freddy", 25, [microphone, magic_hat], Armor("Exoskeleton", 50),[magic_hat])



PIZZERIA = Room("Security Office", None, None, "EAST_HALLWAY",None,None,None, "WEST_HALLWAY",None, None, None, None, None, "This is the room you are in right now."
                                                                                                                           " There are doors on each side of you that leads "
                                                                                                                           "to the East and West hallways.")

WEST_HALLWAY = Room("West Hallway", "DINING_AREA", None, "OFFICE", None, None, None, "SUPPLY_CLOSET", None, None, None, "This hallway connects the dining area "
                                                                                                                        "to the security office. "
                                                                                                                        "There appears to be a door to your left "
                                                                                                                        "that leads to the supply closet")

EAST_HALLWAY = Room("East Hallway", "DINING_AREA", None, None, None, None, None, "OFFICE", None, None, None, "This hallway connects the dining area "  
                                                                                                             "to the security office")

SUPPLY_CLOSET = Room("Supply Closet", None, None,"WEST_HALLWAY", None, None, None, None, None, None, None, [crowbar, flashlight], None, "There's a flashlight on the wall "
                                                                                                                                        "and a crow bar on the floor.")

DINING_AREA = Room("Dining Area", "SHOW_STAGE", None, "RESTROOMS", "KITCHEN", "EAST_HALLWAY", "WEST_HALLWAY", "PIRATES_COVE", "BACKSTAGE", None, None, None, None, "There are a few party hats on the tables. "
                                                                                                                                                                   "The animatronics are standing on stage")

SHOW_STAGE = Room("Show Stage", None, None, None, None, "DINING_AREA", None, None, None, None, None, None,[Orc, Orc2, Orc4], "There are three animatronics standing here.")

BACKSTAGE = Room("Backstage", None, None, "DINING_AREA", None, None, None, None, None, None, None, None, Orc3, "There appears to be an endoskeleton "
                                                                                                               "sitting on the table. ")

RESTROOMS = Room("Restrooms", None,"M_RESTROOM", None, "F_RESTROOM", None, None, None, None, None, None, None, None, "There are two restrooms")

M_RESTROOM = Room ("M Restroom", None, None, None, None, None, None, "RESTROOMS", None, None, "BASEMENT", None, None, "There appears to be a hatch "
                                                                                                                      "in one of the stalls")

F_RESTROOM = Room("F Restroom", None, None, None, None, None, None, None, None, None, None, None, None, "There are four stalls. "
                                                                                                        "One has a dead woman in it. "
                                                                                                        "She appears to be wearing a key around her neck.")

KITCHEN = Room("Kitchen", None, None, "DINING_AREA", None, None, None, None, None, None, None, None, None, "There is a knife in the cutting board.")

PIRATES_COVE = Room("Pirates Cove", None, None, "DINING_AREA", None, None, None, None, None, None, None, None, None,"Foxy is rested on his stand. "
                                                                                                                    "His hook and eye-patch seem detachable.")
player = Player('OFFICE', 100, 0, None)

playing = True
current_node = ['PIZZERIA']
directions = ['NORTH', 'NORTHEAST', 'EAST', 'SOUTHEAST', 'SOUTH',
              'SOUTHWEST', 'WEST', 'NORTHWEST', 'UP', 'DOWN']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions(pos)
        command.lower() in ['q', 'quit', 'exit']:
        playing = False

    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = [room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
