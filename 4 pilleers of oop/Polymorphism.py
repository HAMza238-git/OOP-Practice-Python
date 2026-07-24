class animal():
    def sound(self):
        print("All animals make sound",)

class Dog(animal):
    def sound(self):
        print("Dog Bark",)

class Cat(animal):
    def sound(self):
        print("Cat Meow",)

class Cow(animal):
    def sound(self):
        print("Cow moos")

a1 = animal()
d1 = Dog()
c1 = Cat()
cc1 = Cow()

a1.sound()
d1.sound()
c1.sound()
cc1.sound()