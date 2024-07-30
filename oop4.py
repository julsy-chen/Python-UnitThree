class Player:
    def __init__(self, name):
        self.__name = str(name)
        self.__health = 10
        self.__potion = 2

    @property
    def name(self):
        return self.__name
    
    @property 
    def health(self):
        return self.__health
    
    @property 
    def potion(self):
        return self.__potion
    
    def update(self, val, heal = False):
        pass

    def attack(self, otherPlayer):
        pass

    def risk(self):
        pass

    def heal(self)?:
        pass
    
    # make object printable
    def __str__(self):
        return f"{self.name} (Health: {self.health}, Potions: {self.potion})"
    
    def __repr__(self):
        return self.__str__()
    
class Enemy(Player):
    def move(self, other):
        option = randrange(1,4)
        if option == 1:
            print(f"{self.name} attacked")
            return self.attack(other)
        elif option == 2:
            print(f"{self.name} took a risk")

        else:
            print(f"{self.name} healed")
            return self.heal()
