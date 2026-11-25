# Employee class with constructor, default parameters and methods

class Employee:
    # Constructor with default parameters
    def __init__(self, emp_no=0, name="Not Given",
                 designation="Not Assigned", salary=0.0):
        self.emp_no = emp_no
        self.name = name
        self.designation = designation
        self.salary = salary

    # Takes the values of the attributes from the keyboard
    @staticmethod
    def accept_employee_details():
        emp_no = int(input("Enter employee number: "))
        name = input("Enter employee name: ")
        designation = input("Enter designation: ")
        salary = float(input("Enter salary: "))
        return emp_no, name, designation, salary

    # Displays all the values
    def display_employee_details(self):
        print("Employee Number :", self.emp_no)
        print("Name :", self.name)
        print("Designation :", self.designation)
        print("Salary :", self.salary)


# Object using default values of the constructor
print("--- Employee with default values ---")
e1 = Employee()
e1.display_employee_details()

# Object using values entered from the keyboard
print("\n--- Enter details of an employee ---")
details = Employee.accept_employee_details()
e2 = Employee(*details)

print("\n--- Employee details ---")
e2.display_employee_details()