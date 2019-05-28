
class Room(object):
    def __init__(self, name, north, northeast, east, southeast, south, southwest, west, northwest,
                 up, down, items, character, description):
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
    def __init__(self, starting_location, health_level=100, shield=0, weapon=None):
        self.current_location = starting_location
        self.inventory = []
        self.health = health_level
        self.shield = shield
        self.weapon = weapon

    def move(self, new_location):
        """This moves the player to a new room
        :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """This method searches the current room so see if a room
        exists in that direction.
        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


PIZZERIA = Room("Security Office", None, None, "EAST_HALLWAY", None, None, None, "WEST_HALLWAY", None,
                None, None, None, None, "This is the room you are in right now."
                                        " There are doors on each side of you that leads "
                                        "to the East and West hallways.")

WEST_HALLWAY = Room("West Hallway", "DINING_AREA", None, "OFFICE", None, None, None, "SUPPLY_CLOSET", None, None,
                    None, None, None, "This hallway connects the dining area "
                                      "to the security office. " 
                                      "There appears to be a door west " 
                                      "that leads to the supply closet.")

EAST_HALLWAY = Room("East Hallway", "DINING_AREA", None, None, None, None, None, "OFFICE", None, None,
                    None, None, None, "This hallway connects the north dining area "
                                      "to the security office.")

SUPPLY_CLOSET = Room("Supply Closet", None, None, "WEST_HALLWAY", None, None, None, None, None, None, None,
                     None, None, "There's a flashlight on the wall "
                                                  "and a crow bar on the floor.")

DINING_AREA = Room("Dining Area", "SHOW_STAGE", None, "RESTROOMS", "KITCHEN", "EAST_HALLWAY", "WEST_HALLWAY",
                   "PIRATES_COVE", "BACKSTAGE", None, None, None, None, "There are a few party hats on the tables. "
                                                                        "The animatronics are standing on stage")

SHOW_STAGE = Room("Show Stage", None, None, None, None, "DINING_AREA", None, None, None, None, None, None,
                  None, "There are three animatronics standing here.")

BACKSTAGE = Room("Backstage", None, None, "DINING_AREA", None, None, None, None, None, None, None, None, None,
                 "There appears to be an endoskeleton "
                 "sitting on the table. ")

RESTROOMS = Room("Restrooms", None, "M_RESTROOM", None, "F_RESTROOM", None, None, None, None, None,
                 None, None, None, "There are two restrooms")

M_RESTROOM = Room("M Restroom", None, None, None, None, None, None, "RESTROOMS", None, None,
                  "BASEMENT", None, None, "There appears to be a hatch "
                                          "in one of the stalls")

F_RESTROOM = Room("F Restroom", None, None, None, None, None, None, "RESTROOMS", None, None, None,
                  None, None, "There are four stalls. "
                              "One has a dead woman in it. "
                              "She appears to be wearing a key around her neck.")

KITCHEN = Room("Kitchen", None, None, "DINING_AREA", None, None, None, None, None,
               None, None, None, None, "There is a knife in the cutting board.")

PIRATES_COVE = Room("Pirates Cove", None, None, "DINING_AREA", None, None, None,
                    None, None, None, None, None, None, "Foxy is rested on his stand. "
                                                        "His hook and eye-patch seem detachable.")
player = Player(PIZZERIA, 100, 0, None)

playing = True
current_node = ['PIZZERIA']

directions = ['north', 'northeast', 'east', 'southeast', 'south',
              'southwest', 'west', 'northwest', 'UP', 'DOWN']
short_directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw', 'u', 'd']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)

    command = input(">_")

    if command.lower() in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
