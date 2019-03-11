class PencilSharpener(object):
    def __init__(self, sharp=True):
        self.blade = sharp
        self.plug = 1
        self.size_setting = 6
        self.sharpen = True
        self.container = 1

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
            self.battery_left = 0
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


my_phone.make_call(60)
my_phone.make_call(10)
my_phone.charge(100)
my_phone.make_call(10)
my_phone.smash_phone()
my_phone.make_call(1)

print(Special_Random.RandomWiebe.my_random())