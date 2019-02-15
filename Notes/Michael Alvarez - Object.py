class Computer(object):
    def __init__(self, charge_left=90, broke=True):
        self.screen = True
        self.camera = 1
        self.microphone = 1
        self.battery_left = charge_left
        self.pod = broke
    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100


