class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display_info(self):
        print("Brand", self.brand)
        print("model", self.model)

class garage:
    def __init__(self):
        self.car = []


    def add_car(self, car):
        self.car.append(car)
        print("the car is addred to garage")

    def display_car(self):
        print("cars")
        for car in self.car:
            car.display_info()

        print("All cars displayed successfully.")

    def search_car(self, brand):
        for car in self.car:
            if car.brand == brand:
                car.display_info()
                print("the car is")
                return
        print("car not found")

    def remove_car(self, brand):
        for car in self.car:
            if car.brand == brand:
                self.car.remove(car)
                print("the car is removed from garage")
                return
        print("car is not in garage")

car1 = car("toyota", "corola")
car2 = car("suzuki", "mehran")

garage = garage()
garage.add_car(car1)
garage.add_car(car2)
garage.display_car()
garage.search_car("toyota")
garage.remove_car("toyota")
garage.display_car()





    

