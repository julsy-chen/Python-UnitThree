class Dog:
    def __init__(self, name):
        self.name = name
        self.needToPee = True

    def bark(self):
        return "bork"
    
    def speak(self):
        return f"I am {self.name}."
    
    def pee(self):
        if self.needToPee == True:
            print(f"{self.name} is peeing on a very nice white rug")
            self.needToPee = False
        else:
            print(f"{self.name} does not need to pee")


    
dog1 = Dog("Death, Destroyer of Death")
print(dog1.bark())
print(dog1.speak())