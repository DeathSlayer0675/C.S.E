health_level = 100

class Weapon(object):
    def __init__(self,name):
        self.name = name


class Microphone(Weapon):
    def __init__(self):
        super(Microphone,self).__init__("Microphone")

class Food(object):
    def __init__(self,name):
        self.name = name


class Armor(object):
    def __init__(self,name):
        self.name = name
