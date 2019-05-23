class Sharpener(object):
    def __init__(self, sharp=True):
        self.blade = sharp
        self.plug = 1
        self.size_setting =
        self.sharpen = True
        self.container = 1
        self.power = True

    def sharpen(self, time):
        self.sharpen += time
        if self.sharpen > 100:
            self.battery_left = 100

    def make_call(self, duration):
        if not self.screen:
            print("You can't make a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 5
        if self.battery_left <= 0:
            print("You can't. The phone is dead.")
            return
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self. = 0
            print("Your phone dies during the conversation.")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation.")
        else:
            print("You successfully make the phone call.")
            print("Your phone is now at %s" % self.battery_left)

    def smash_phone(self):
        print("SMASH!!!!!!!!!!")
        print("It broke")
        self.screen = False


Sharpener.make_call(1)
Sharpener.make_call(2)
Sharpener.charge(100)
Sharpener.make_call(10)
Sharpener.smash_phone(self)
Sharpener.make_call(1)

print(Special_Random.RandomWiebe.my_random())