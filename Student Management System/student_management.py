class Student:
    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display_info(self):
        print("student ID", self.student_id)
        print("Name", self.name)
        print("Student age", self.age)
        print("Course", self.course)
        print("Marks", self.marks)
        print()

    def calculate_average(self):
        return (sum(self.marks) / len(self.marks))

    def calculate_grade(self):
        average = self.calculate_average()
        if average >= 95:
            return "Grade A"
        elif average >= 80:
            return "Grade B"
        elif average >= 60:
            return "Grade C"
        else:
           return "Fail"


class Student_management():
    def __init__(self,):
        self.students = []

    def add_students(self, student):
        self.students.append(student)

    def display_all_students(self):
        for student in self.students:
            student.display_info()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                student.display_info()
                return
        print("record not found",)

    def update_marks(self, student_id, new_marks):
        for student in self.students:
            if student.student_id == student_id:
                student.marks = new_marks
                student.display_info()
                print("marks updated successfully",)
                return
        print("record not found",)

    def delete_student(self, student_id, ):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("student deleted successfully",)
                return
        print("record not found",)

    def search_student_name(self, name):
        for student in self.students:
            if student.name == name:
                student.display_info()
                return
        print("record not found")

    def top_student(self):
        if not self.students:
         print("No students available")
         return

        top_student = self.students[0]

        for student in self.students:
             if student.calculate_average() > top_student.calculate_average():
                 top_student = student

        print("Top Student")
        print("Name:", top_student.name)
        print("Average:", top_student.calculate_average())
        print("Grade:", top_student.calculate_grade())



system = Student_management()

# s1 = Student("1001", "Junaid", 21, "Computer Science", [78,98,67])
# s2 = Student("1002", "Raheem", 20, "Software Science", [77,94,68])

# system.add_students(s1)
# system.add_students(s2)
# system.display_all_students()
# system.search_student("1003")
# system.search_student("1002",)
# system.update_marks("1001", [89,78,87])
# system.delete_student("1003")
# system.search_student_name("Raheem",)
# print(s1.calculate_average())
# print(s1.calculate_grade())
# system.top_student()

while True:
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID")
    print("4. Search Student by Name")
    print("5. Update Marks")
    print("6. Delete Student")
    print("7. Top Student")
    print("8. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = list(map(int, input("Enter marks separated by spaces: ").split()))

        student = Student(student_id, name, age, course, marks)
        system.add_students(student)
        print("Student added successfully!")

    elif choice == "2":
        system.display_all_students()
    elif choice == "3":
        student_id = input("Enter Student ID: ")
        system.search_student(student_id)
    elif choice == "4":
        name = input("Enter Student Name: ")
        system.search_student_name(name)
    elif choice == "5":
        student_id = input("Enter Student ID: ")
        new_marks = list(map(int, input("Enter new marks separated by spaces: ").split()))
        system.update_marks(student_id, new_marks)
    elif choice == "6":
        student_id = input("Enter Student ID: ")
        system.delete_student(student_id)
    elif choice == "7":
        system.top_student()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
         print("Invalid choice")
         
        

                                    