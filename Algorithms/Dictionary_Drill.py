employees = {
    "Ali": 50000,
    "Hamza": 75000,
    "Ahmed": 60000
}

for name, salaries in employees.items():
    print(name, ":", salaries)

highest_employee = "Ali"
highest_salary = employees["Ali"]

for name, salaries in employees.items():
    if salaries > highest_salary:
        highest_salary = salaries
        highest_employee = name

print("the", highest_employee, "has the highest salary :", highest_salary)



