class Artifact:
    def __init__(self):
        self.lightTotal = 0

    def weapons(self, weapon_list):
        a = 0
        for light in weapon_list:
            a += light*0.12
        self.lightTotal += a

    def armor(self, armor_list):
        b = 0
        for light in armor_list:
            b += light*0.1
        self.lightTotal += b

    def classItems(self, item_list):
        i = 0
        for light in item_list:
            i += light*0.08
        self.lightTotal += i