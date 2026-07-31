from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = 3.14 * self.radius * self.radius
        return area
    
class rectangle(shape):
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        area = self.lenght * self.width
        return area

circle1 = circle(5)
rectangle1 = rectangle(5, 5)

print(circle1.area())
print(rectangle1.area())
       