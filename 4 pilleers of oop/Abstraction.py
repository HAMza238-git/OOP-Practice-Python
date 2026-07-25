from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog Bark",)

class Cat(Animal):
    def sound(self):
        print("Cat meow",)


d1 = Dog()
c1 = Cat()

d1.sound()
c1.sound()


