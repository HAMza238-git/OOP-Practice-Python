class car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print("brand:", self.brand)
        print("model:", self.model)
        print("year:", self.year)

        
car1 = car("audi", "CX", 2009)
car2 = car("Mercedies", "bcg", 2022)
car3 = car("toyota", "corola", 2015)

print(car1.brand, car1.model, car1.year)
print(car2.brand, car2.model, car2.year)
print(car3.brand, car3.model, car3.year)
car1.display_info()
car2.display_info()
car3.display_info()
