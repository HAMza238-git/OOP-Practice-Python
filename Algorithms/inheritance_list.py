class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display_info(self):
        print("name :", self.name)
        print("age :", self.age)

class student(person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def display_info(self):
        super().display_info()
        print("roll no :", self.roll_no)
s1 = student("hamza", 24, "S101")
s2 = student("junaid", 32, "S102")
students = [s1, s2]

for student in students:
    student.display_info()