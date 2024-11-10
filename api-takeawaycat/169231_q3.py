class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary for {self.name} has been updated to ${self.salary}.")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Employee {employee.name} (ID: {employee.employee_id}) added to department '{self.department_name}'.")

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for department '{self.department_name}' is: ${total_salary}")
        return total_salary

    def display_all_employees(self):
        print(f"Employees in department '{self.department_name}':")
        for employee in self.employees:
            employee.display_details()



def main():
    
    department = Department("Engineering")

    
    employee1 = Employee("Alice", "E001", 70000)
    employee2 = Employee("Bob", "E002", 80000)

    
    department.add_employee(employee1)
    department.add_employee(employee2)

    
    employee1.update_salary(75000)

   
    department.display_all_employees()

    
    department.calculate_total_salary()


if __name__ == "__main__":
    main()
