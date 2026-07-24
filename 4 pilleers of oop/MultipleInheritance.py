class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name", self.name)
        print("age", self.age)

class athlete:
    def __init__(self, sports):
        self.sports = sports

    def display_sport(self):
        print("sports", self.sports)

class student(person, athlete):
    def __init__(self, name, age, sports):
        person.__init__(self, name, age)
        athlete.__init__(self, sports)

    def display_all(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Sport:", self.sports)
        
        
       

p1 = person("hamza", 25)
a1 = athlete("cricket")
s1 = student("zain", 34, "football")

p1.display_info()
a1.display_sport()
s1.display_all()