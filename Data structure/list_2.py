class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print("brand", self.brand)
        print("model", self.model)
        print()



class garage:
    def __init__(self):
        self.cars = []

    def add_cars(self, cars):
        self.cars.append(cars)

    def display_cars(self):
        print("cars")
        for car in self.cars:
            car.display_info()

car1 = car("toyota", "corola")
car2 = car("suzukui", "mehran")

garage = garage()
garage.add_cars(car1)
garage.add_cars(car2)
garage.display_cars()
