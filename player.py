class Player:
    def __init__(self, name):
        self.name = name
        # encapsoluation = double underscore in front
        self.__level = 1
        self.__hp = 100

    @property
    def level(self):
        return self.__level

    def levelUp(self):
        self.__level += 1

    def attack(self, otherPlayer):
        otherPlayer.hp -= 10

p1 = Player("Lux")
p2 = Player("Yasuo")

p1.level = 100
p1.hp = 100000
print(p1.level)