import math

class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    # getter methods
    # x and y are now READ-ONLY
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    def add(self, otherPoint):
        return Point(self.x + otherPoint.x, self.y + otherPoint.y)
    
    def __add__(self, otherPoint):
        return self.add(otherPoint)

    def multiply(self, otherPoint):
        return (self.x * otherPoint.x) + (self.y * otherPoint.y)

    def distance(self, otherPoint):
        return math.sqrt((self.x - otherPoint.x)**2 + (self.x - otherPoint.x)**2)

    # make our object printable

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return self.__str__()
    

p1 = Point(0,0)

p2 = Point(3, 4)
p3 = Point(6, 9)

p4 = p2.distance(p3)
print(p4)
