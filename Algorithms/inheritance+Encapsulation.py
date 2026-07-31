class employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print("name", self.name)
        print("employee_id", self.employee_id)
class manager(employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id)
        self.__salary = salary
    def display_info(self):
        super().display_info()
        print("salary", self.__salary)

    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary):
        self.__salary = new_salary
     

manager1 = manager("junaid", "M101", 99999)
manager2 = manager("raheem", "M101", 88888)
managers = [manager1, manager2]
for manager in managers:
    manager.display_info()
manager1.set_salary(124500)
manager1.display_info()

