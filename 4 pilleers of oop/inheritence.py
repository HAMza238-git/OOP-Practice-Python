class Person:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def display_info(self):
            print("name:", self.name,)
            print("age:", self.age)

class student(Person):
        def __init__(self, name, age, course):
                super().__init__(name, age)
                self.course = course

        def display_info(self):
                print("name:", self.name,)
                print("age:", self.age)
                print("course", self.course)

class graduateStudent(student):
        def __init__(self, name, age, course, research_thesis):
               super().__init__(name, age, course,)
               self.research_thesis = research_thesis


        def display_info(self):
                print("name:", self.name,)
                print("age:", self.age)
                print("course", self.course)
                print("research_thesis", self.research_thesis)


p1 = Person("Hamza", 45)
s1 = student("Ali", 20, "science",)
t1 = student("Shahid", 34, "Commerence")
g1 = graduateStudent("shahzad", 28, "Arts", "artificial intelligence")

p1.display_info()
s1.display_info()
t1.display_info()
g1.display_info()










