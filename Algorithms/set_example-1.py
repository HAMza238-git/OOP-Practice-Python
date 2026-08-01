student1 = {"Math", "Physics", "English", "Chemistry"}

student2 = {"Biology", "Physics", "Math", "Computer"}

for student in student1:
    print(student)
print()

for student in student2:
    print(student)
print()

student = student1.intersection(student2)
print(student)

student = student1.union(student2)
print(student)


student1 = {"Math", "Physics", "English", "Chemistry"}

student2 = {"Physics", "Math", "Computer"}

different = student1.difference(student2)
print(different)