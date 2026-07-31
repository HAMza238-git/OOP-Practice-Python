# class Employee:
#     def __init__(self, First, Second, Pay):
#         self.First = First
#         self.Second = Second
#         self.Pay = Pay
#         self.Email = First + '.' + Second + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.First, self.Second)

# emp_1 = Employee('Hamza', 'Saeed', 60000)
# emp_2 = Employee('Ali', 'Syed', 80000)


# print(emp_1.Pay)
# print(emp_2.Email)

# print(emp_1.fullname())
# print(emp_2.fullname())






# class student:
#     name = "ali"

# s1 = student()
# s2 = student()
# print(s2.name)





# class car:
#     color = "blue"

# car1 = car()
# print(car1.color)    





# class student:
#     college_name = "punjab college"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

# s1 = student("karan", 78)
# print(s1.name, s1.marks)

# s2 = student("ali", 787)
# print(s2.name, s2.marks)

# print(s2.college_name)





# methods
# class student:
#     college_name = "punjab college"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")

#     def welcome(self):
#         print("welcome class,", self.name )

#     def get_marks(self):
#         return self.marks

# s1 = student("karan", 78)
# s1.welcome()
# print(s1.get_marks())






# # example question
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg of marks are:", sum/3)


# s1 = student("tonny", [78, 67,76])
# s1.get_avg()

# movies = []
# mov1 = input("enter 1st movie",)
# mov2 = input("enter 2nd movie",)
# mov3 = input("enter 3rd movie",)

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

# list1 = [1, 2, 1]
# list2 = [1, 2, 2]
# copy_list1 = list1.copy()
# copy_list2 = list2.copy()

# copy_list1.reverse()
# copy_list2.reverse()

# if list1 == copy_list1:
#     print("its palidrom ")
# else:

#     print("its not palidrom")

# if list2 == copy_list2:
#     print("its palidrom")
# else:
#     print("its not palidram")

