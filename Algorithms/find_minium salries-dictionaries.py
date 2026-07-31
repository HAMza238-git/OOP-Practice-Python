employees = {
    "Ali": 50000,
    "Hamza": 75000,
    "Ahmed": 60000
}

lowest_name = "Ali"
lowest_salaries = employees["Ali"]

for name, salaries in employees.items():
    if salaries < lowest_salaries:
        lowest_salaries = salaries
        lowest_name = name

print("the", lowest_name, "has the lowest salary :", lowest_salaries)

