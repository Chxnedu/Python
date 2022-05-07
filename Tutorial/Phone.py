# classes are used to define your own data type. the following code below is going to show you how to
# create classes

class Phone:

    def __init__(self, brand, ram, rom, refresh_rate):
        self.brand = brand
        self.ram = ram
        self.rom = rom
        self.refresh_rate = refresh_rate
    def has_high_refreshrate(self):
        if self.refresh_rate >= 90:
            return True
        else:
            return False

# you can also define functions inside a class defintion