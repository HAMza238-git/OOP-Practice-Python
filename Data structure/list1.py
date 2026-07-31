class student:
    def __init__(self, name,):
        self.name = name
        self.courses = []

    def add_courses(self, courses):
        self.courses.append(courses)

    def display_student(self):
        print("Name", self.name)
        print("courses")
        for course in self.courses:
            print(course)

c1 = student("ali")


c1.add_courses("english")
c1.add_courses("Math")
c1.display_student()

