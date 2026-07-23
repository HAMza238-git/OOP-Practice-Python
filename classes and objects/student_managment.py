class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def  display_info(self):
        print("student_id", self.student_id)
        print("name", self.name)
        print("age", self.age)
        print("course", self.course)
        print("marks", self.marks)

    def calculate_average(self):
        total  = 0
        for val in self.marks:
         total += val
        print("hi", self.name, "your avg score is", total / len(self.marks))

    def is_pass(self):
        total  = 0
        for val in self.marks:
         total += val
        average = total / len(self.marks)
        if average > 50:
         print(self.name, "is pass")
        else:
         print(self.name, "is fail")
         
    def update_marks(self, new_marks):
       self.marks = new_marks
       print(self.marks)

s1 = Student(101, "Feroz", 20, "Computer Science", [78, 87, 89])
s2 = Student(102, "Shams", 21, "Arts", [23, 11, 9])

print(s1.name)
print(s2.course)
s1.display_info()
s2.display_info()
s1.calculate_average()
s2.calculate_average()
s1.is_pass()
s2.is_pass()
s1.update_marks([89,79,78])