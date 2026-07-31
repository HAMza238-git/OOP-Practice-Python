students = {
    "Ali": 85,
    "Hamza": 92,
    "Ahmed": 78
}

for name, marks in students.items():
    print(name, ":", marks)

if "Hamza" in students:
    print("hamza", ":", students["Hamza"])

students["Ahmed"] = 90
print(students)

students["Danyal"] = 89
print(students)



